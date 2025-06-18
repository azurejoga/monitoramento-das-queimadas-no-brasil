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
| 402bd704-f023-343e-9200-f3553504cc0d | -11.62249 | -46.77561 | 2025-06-18 04:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 232ec3ff-c538-3621-b429-98d7ba47edf8 | -8.13061 | -47.98842 | 2025-06-18 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 959d3490-e00d-343a-8339-cb00537c9241 | -10.36081 | -57.24574 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6776f201-98ee-3cfa-9ede-526f7e5b3aee | -10.62501 | -54.91777 | 2025-06-18 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd45acdb-0ed9-3633-9e42-59f4106542b6 | -8.59966 | -48.05827 | 2025-06-18 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19b3a785-f456-3ede-9f51-0f4b3e5b4e0f | -6.77309 | -55.4852 | 2025-06-18 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ab7032e-ffb9-38e5-9c5f-840b7a6acb7a | -9.88342 | -47.80928 | 2025-06-18 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 293c21f3-0e50-3d90-8f63-164a109460a5 | -9.26507 | -50.03772 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af27dd4d-86cf-3b23-8d8f-308622829e19 | -5.569 | -45.20312 | 2025-06-18 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04c41827-77ec-31f1-9f87-bb6eb5b392c3 | -9.41818 | -48.43145 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fe6dd43-cc06-3ea7-8582-a2a646f80e5a | -7.94455 | -48.03909 | 2025-06-18 04:38:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14286a7e-f131-3483-88cd-b90ac2753c5d | -7.54386 | -45.65036 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0cbf7f7-cf9f-3fd8-bef3-8d7b82a39379 | -6.41755 | -44.8012 | 2025-06-18 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df2aedee-31d1-3175-99f0-e830716a4f1f | -11.12987 | -53.93754 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7411656e-d620-33e1-92e7-8f897727398a | -9.50813 | -55.9634 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a55fc9dd-81e0-3b3f-9c6c-320c5c432f5c | -6.24019 | -43.36528 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96f6c955-2e10-3eb3-9525-ea889f7498d7 | -6.03322 | -44.05459 | 2025-06-18 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18eac9f-f31d-31dc-95f0-7e10814126ec | -4.8117 | -46.82162 | 2025-06-18 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db5ec38e-a0d3-371c-a227-731f2be1d79a | -6.13639 | -42.97179 | 2025-06-18 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7ab2041c-697d-3764-b736-d51ac238668c | -11.12623 | -53.93691 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 40bcdd90-9c77-3293-8632-8bb777717f2b | -9.46107 | -57.85503 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e40d80e-3898-377d-a31e-22835a5fa73a | -10.91743 | -56.8447 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16bd0024-db3a-36d9-ba9e-e744c361e605 | -7.54481 | -45.64383 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e5f0213-5978-3697-8bbc-0e282dffcafd | -6.86866 | -44.83932 | 2025-06-18 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ce86f79-d27c-3806-9edf-3bcc9304bf5d | -10.47796 | -48.66714 | 2025-06-18 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03f02a3d-c49d-3c7f-9e18-f95464dddbfe | -9.84293 | -44.70502 | 2025-06-18 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deb53295-17e4-3541-8d44-28f2a512c4f8 | -9.8456 | -44.70129 | 2025-06-18 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fc49960-79d8-374a-94e9-37e09f07f91e | -6.23957 | -43.36943 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b869a1de-0447-317a-bc40-405ed6d63076 | -5.84995 | -43.63577 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bba186b1-151d-3763-ab51-a46d16a3bb9d | -11.13366 | -53.93633 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 16d531a9-a7bd-3094-920f-da13a31f8eb6 | -5.61015 | -45.97759 | 2025-06-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebfbb2aa-9639-3f4f-ac7b-a0fc10e61b7d | -9.27301 | -49.61795 | 2025-06-18 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21897ed8-e0bf-3338-8f9a-88c78571476e | -7.16479 | -43.46983 | 2025-06-18 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 591dda54-2cb8-31e0-b0ac-523000ed9539 | -10.5756 | -49.64733 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d70bac62-bf2e-3db9-8270-d94a273ea5d2 | -10.88137 | -54.31569 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf229d0b-4bc9-32e4-92d8-835f287049f6 | -5.90818 | -43.44802 | 2025-06-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fe3b7051-511d-38e8-b5b9-ac7d910196d3 | -11.07672 | -55.05266 | 2025-06-18 04:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 067a6b2b-557b-3421-9125-05230f92633c | -5.00656 | -56.17512 | 2025-06-18 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ae2d8e-88d0-35db-90e6-450b8a8d17dc | -9.32369 | -47.83004 | 2025-06-18 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 866f7e40-ed32-39c1-8f68-cf120dd67f88 | -9.46282 | -57.84887 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67ca5d43-fa48-3353-8531-a08ce49792b2 | -11.3383 | -45.21581 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8cd77c7-3d00-35f9-8b52-889ac894e94f | -11.56833 | -44.67128 | 2025-06-18 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d349efd9-a9b5-33ac-b41d-11ac5b703ffe | -11.13001 | -53.93572 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d6bf6bfe-7fb6-38c1-b3ce-94992a2dc015 | -6.12428 | -42.53469 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 967df9b4-fd00-3038-976f-fc3f320a7c4b | -7.25454 | -44.64505 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 669f0e53-053b-3380-a24c-65c3ade6d169 | -9.26728 | -50.0452 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b79a48be-1c51-36ce-8639-3640984b8db9 | -8.44007 | -46.9083 | 2025-06-18 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd1d2d21-5248-3b35-8364-4bb4f33444c0 | -9.25812 | -50.03689 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ca5abbf-6165-3aea-80aa-c3e2edda80f3 | -8.00728 | -46.80595 | 2025-06-18 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ec0ce78-8d2a-3abe-acc0-d203126672cb | -10.85312 | -53.77707 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5898e75c-e6e1-3786-b50d-dc1a47532e5b | -11.13441 | -53.93198 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 8f4637e8-0c78-3837-9c9f-2294346e52f0 | -11.1306 | -53.93319 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c1af3faf-f278-30be-8215-80e326c7d805 | -7.25055 | -44.64432 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2ce5d5f-16b5-3a2f-aee6-08059bac0c88 | -10.29404 | -57.14403 | 2025-06-18 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea8cd54d-a3a8-30ef-8582-385178f5045c | -7.48633 | -49.57663 | 2025-06-18 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b27ee7cf-0b2e-3a72-9610-94a7bad6242d | -11.33419 | -45.21527 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ced0c05-8748-3adf-8279-5a4a5747bfc9 | -9.45726 | -57.8488 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9139557d-6c73-3ee5-aec2-2da7616e7a9a | -9.48631 | -56.08747 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| da294417-0d99-355c-a2aa-de4d674f21fe | -10.92104 | -56.84987 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1e8ff81-3f59-368a-a3d9-48dd0dec88ac | -7.54246 | -45.65957 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9b29cc9-2240-3ee9-aad9-693b34a1280a | -7.43995 | -44.89853 | 2025-06-18 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d703579b-08f1-36b6-bdad-c99b2d53b4a7 | -10.98321 | -45.11095 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc2d0a3d-a192-37e6-8e6b-75c11be27117 | -3.72789 | -53.99097 | 2025-06-18 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b27725-0fb2-318f-a448-4ded0ff87f16 | -11.7957 | -43.79016 | 2025-06-18 04:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f61bdede-0fce-3374-87f5-485b0260e30b | -5.61079 | -45.9734 | 2025-06-18 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 897236e5-3db2-3c88-aba6-358a9b82e9d3 | -12.13804 | -47.41896 | 2025-06-18 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daed6850-0da5-3164-a220-1b7195495e50 | -11.07973 | -55.05836 | 2025-06-18 04:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c32d08f-213b-329b-9174-5f0d543eef06 | -3.7279 | -53.98968 | 2025-06-18 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 602f67d7-606c-32e7-9ab5-2e6b02ca5718 | -8.07343 | -43.11073 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e12a6b0c-bb9e-32ce-b757-2d3c2b72d520 | -6.67126 | -43.18713 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b2433ea5-8103-3555-95ee-fef1214fd2c7 | -5.91244 | -43.44864 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ef9a49ea-ffd3-31ac-be30-140445db47a7 | -11.55746 | -52.01706 | 2025-06-18 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd643b2d-0fa8-3e83-be83-cf90f3146f1d | -10.84513 | -53.7801 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c308085-bb5e-3fd3-92a2-0cda81146365 | -9.51167 | -55.96806 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e518bab-a04e-304e-9c5e-6fad13d188a8 | -11.12636 | -53.93509 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 918f194a-9268-3ca9-b913-8bc64c58b37b | -8.1111 | -45.54682 | 2025-06-18 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3fd7895-f35f-34cb-9930-e07dd9c04afa | -6.36088 | -43.65693 | 2025-06-18 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35914723-3357-35a9-8f95-206c12e7c403 | -10.55209 | -48.63694 | 2025-06-18 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4829fd0-295a-3a3d-bf72-6ef651614511 | -11.08362 | -55.05904 | 2025-06-18 04:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca470752-1905-311d-895d-f35ac21c5570 | -11.22002 | -50.77855 | 2025-06-18 04:38:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee8d00e0-a2a1-3b73-a3b2-59af7bf9df4d | -5.90333 | -43.45136 | 2025-06-18 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e0120cf1-7a11-3959-bbf7-1a913b37d059 | -12.05274 | -46.97754 | 2025-06-18 04:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3968f27-3a35-33ac-92c1-ac862b93e689 | -6.67512 | -43.22203 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 49872bc5-cb32-312a-8cf4-1cfe0e910b05 | -9.51235 | -55.96413 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba269bf-b371-3bc3-b053-48c09acab1c2 | -7.54008 | -45.64979 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41869042-3276-3102-9233-7e1f40c213ac | -9.45707 | -57.85336 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9abaa0a1-4727-3bfb-81c4-8f49df58224d | -10.85748 | -53.77342 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0567a62d-4255-38a6-8234-42fd5a476ebd | -9.86132 | -47.88518 | 2025-06-18 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87d22148-5a2f-369d-b3a9-2da136c12639 | -8.59125 | -51.56865 | 2025-06-18 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 851bf74e-6947-32bb-b365-c9a4252e1d06 | -9.44541 | -48.15854 | 2025-06-18 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba107c9-48de-3665-b294-4f8ba146d527 | -8.72656 | -49.0285 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b324b518-4ce3-3a93-b0ee-c6587e1deed9 | -6.11905 | -42.53867 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b07e10f2-f2fc-3322-8c6c-d7ca27044fca | -10.34755 | -44.30812 | 2025-06-18 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 174f63da-d235-362b-8bc0-c62c4a7ae52c | -7.16067 | -55.45464 | 2025-06-18 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91342676-bdf9-3f84-8428-108238108e06 | -10.57837 | -49.65138 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f65e0e57-ef72-3e77-85d4-ec9fce5fce36 | -10.87912 | -49.54989 | 2025-06-18 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f57507f8-27ba-3b5b-8404-20f0796f58b6 | -12.13741 | -47.42324 | 2025-06-18 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db289eb8-fe14-3b8d-9d95-53c0a2186be1 | -7.81073 | -46.57557 | 2025-06-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 571422ea-721f-3c47-958b-da80e1df0ccd | -10.5908 | -49.46115 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abdd2f58-ba2b-3a1f-a86c-8ce884f83683 | -9.20302 | -49.67485 | 2025-06-18 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README17.md)
