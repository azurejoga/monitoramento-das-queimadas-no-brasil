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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89a49350-5c77-35bd-9298-598ecad614e6 | -10.05639 | -46.27273 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5aeaad0-b0f9-3153-8a73-09c05587868b | -10.28873 | -45.28954 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 607ac5e8-f605-39a6-85e9-a90b6a823414 | -7.45473 | -42.12503 | 2026-09-11 04:08:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 827347f2-1153-3c99-a2be-4cc8c35fa3f3 | -8.28309 | -47.78695 | 2026-09-11 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33cdab6f-b5ac-30cf-a29b-4f06f3cfaf1d | -7.98941 | -45.56074 | 2026-09-11 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5894ccc-0848-3137-a018-09a538fc0840 | -10.41686 | -45.13026 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1648f01b-fe0e-399b-abae-94214190e3b6 | -10.73442 | -46.15086 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a923cd71-5f3d-3ca4-886f-dab3f503e9a8 | -4.24481 | -49.94506 | 2026-09-11 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7af7da60-d007-3fed-a62a-243fdaf75b9a | -9.31404 | -44.35804 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b867632-d316-3126-b2b5-22f829bf62e2 | -9.70018 | -43.40398 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 09012a16-0958-3332-97a5-e53ba247a487 | -9.31178 | -44.37131 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8added0-1057-3804-8e43-5b1fee7e2c7a | -10.05068 | -44.88544 | 2026-09-11 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28d401e5-dd9f-36fe-a8c4-8adc4c082764 | -10.63897 | -46.12181 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 143d9423-294a-380a-b37c-8f1e23c6e458 | -9.31329 | -44.36245 | 2026-09-11 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9bdbfe82-1fda-3407-a699-b18e07c72176 | -11.19265 | -45.02433 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ceb06c3c-1616-306e-aa6a-6fb170408ba2 | -8.48904 | -44.75188 | 2026-09-11 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d9be8d50-527e-395e-b8cd-9a1c593d9a38 | -8.94034 | -44.40023 | 2026-09-11 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 423f6938-efde-36a5-9d7d-40eaec0bb2ea | -10.46777 | -48.66059 | 2026-09-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1375045-e2e6-320c-805d-9735d86be12d | -10.54297 | -51.35427 | 2026-09-11 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68d8fda8-a4be-3f03-a087-5be285b84abd | -10.48388 | -48.6529 | 2026-09-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac145c08-3a7f-3553-87f3-99007fdbba7c | -6.09698 | -47.38177 | 2026-09-11 04:08:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7cc60e8-15c0-3529-8369-fa3583f3ed43 | -8.72878 | -50.60011 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f4afb0-7cc1-38c5-ad52-1ce83ebd1817 | -9.63413 | -49.02074 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6ce9f845-9940-392d-b096-ec7318733ef0 | -7.1563 | -44.74776 | 2026-09-11 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 108c3b46-1033-349f-92ee-e7bd4666580c | -8.62912 | -44.4026 | 2026-09-11 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b886b805-f075-36fb-9d44-3cd5e91a7c96 | -4.30125 | -49.10658 | 2026-09-11 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4b611ce5-ce99-3250-9ebb-86a439a2f212 | -8.7088 | -49.61763 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b02b5e19-df90-3c8c-b2f2-661589b48407 | -7.14809 | -45.86951 | 2026-09-11 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62cfa5fb-4981-3538-a467-867545f65883 | -10.42144 | -45.12626 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 658ecca6-1b6a-3722-8cfb-f081ca8e9c77 | -9.17218 | -49.95124 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f8ba08f-5048-3b29-aa8f-f1b7d20d2f07 | -8.93588 | -44.40417 | 2026-09-11 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ea99916-f7df-377d-93c5-58061d83e363 | -9.36849 | -49.37715 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afa3541f-a2a7-3325-ad91-1f209f414a2f | -9.70149 | -43.46085 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceac65bb-fc41-33e1-a67f-557952dfd037 | -10.74841 | -45.91745 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80d8c05a-a3c4-377c-9d7c-9704bc20b3d2 | -10.78198 | -45.95217 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bd5adeaa-3a35-3b64-9495-e2b9afccd8b9 | -7.15159 | -45.87412 | 2026-09-11 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38693442-3f3a-3c98-af59-4d6efa915445 | -8.94103 | -44.41899 | 2026-09-11 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df97fda4-b72c-34ae-8290-5cce513baeff | -8.70823 | -49.62082 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9f4f5d24-5a3b-35a8-a1fc-ce0a300cd234 | -8.70758 | -49.62423 | 2026-09-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3407a949-17ea-3ef1-b363-1d0707ba16d5 | -8.90574 | -43.8867 | 2026-09-11 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5fc867c-efa4-3006-aa1e-b6971b103af2 | -11.4087 | -47.73038 | 2026-09-11 04:08:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aad9e8b-518f-35f7-b30d-3d5b1990f7c3 | -9.6292 | -49.01983 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 447b71f1-1244-38d3-9713-6d6fa2a07daf | -10.77675 | -45.93567 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fdaff97-d6a9-3bfd-9f6f-a66da82883c0 | -11.33892 | -45.78374 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6248cfa6-b543-32df-9c25-0ffe8f129892 | -10.95485 | -48.31363 | 2026-09-11 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad8e3e16-efc8-39e3-87c4-c62cc44ba526 | -5.70258 | -45.84661 | 2026-09-11 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 979fe3ad-e5b1-3858-a128-75535d07cffa | -4.29642 | -49.10215 | 2026-09-11 04:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c4c3eeaa-b968-30de-8822-880c08f9f482 | -11.39428 | -43.96422 | 2026-09-11 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad217764-79ac-3d0e-aa04-028441cc160e | -10.75617 | -46.19141 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d929627-ab36-3282-8288-890b6c1cf28f | -9.78613 | -43.45403 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34cbbeeb-3996-3543-8328-eb44974a4426 | -7.98756 | -43.99709 | 2026-09-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e820d533-135e-3a80-bc34-6ac216354e94 | -5.4778 | -45.13198 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4270df65-f438-34c9-89fe-3faffc54de23 | -10.41765 | -45.12561 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47852491-4380-339b-a692-097abd8f7f81 | -9.17807 | -49.94894 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b2dccc1-56bf-367b-9382-ab3b563eeb6a | -8.77797 | -44.18318 | 2026-09-11 04:08:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2aa59580-e6f9-3aef-818a-5308002e88e9 | -9.63399 | -47.6867 | 2026-09-11 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48e2e5ec-60a9-30f6-b26b-0b378d187b68 | -5.67197 | -44.94441 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8540161-4122-31e5-9927-1d8de9dabac1 | -10.6411 | -46.13308 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 061eb153-5fc5-3795-a545-df73c1b210ea | -5.48263 | -45.1299 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47c47fe2-d08c-33c4-9c37-aec69c73760a | -6.28597 | -41.69841 | 2026-09-11 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93025992-04e6-3187-8187-c41b552be133 | -11.33929 | -45.78582 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2376fb62-4c15-319f-bf49-ccfa4f8af2eb | -11.39076 | -43.96361 | 2026-09-11 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2f21503-6da9-3024-806a-22de6ac9e243 | -9.12248 | -48.52504 | 2026-09-11 04:08:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5190e9f-df9e-328b-8a8c-61f3b1ef833b | -9.17158 | -49.95457 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40562e4d-133f-34c7-a893-f47a565b4adf | -11.40466 | -43.9454 | 2026-09-11 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53147391-10df-38af-ade6-48752b101d1d | -11.19143 | -42.78823 | 2026-09-11 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c5e7c909-8002-3347-b280-c4acd21f9094 | -9.68328 | -43.46191 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9275678f-c05d-3a18-b62b-64b9caf21a8e | -7.02254 | -45.11142 | 2026-09-11 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22f75874-20da-3e65-b9c9-be95b1ff1947 | -10.98145 | -47.88575 | 2026-09-11 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4819659b-4aaf-3ebb-bf9c-41fb942e03d7 | -9.77674 | -43.4413 | 2026-09-11 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd8761cd-bbf4-3493-a23a-4835ac6f310e | -10.78375 | -45.94213 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 6f88437a-b6cb-38c6-b7b9-682707ed75dc | -10.27893 | -45.27785 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7b1bfc8-000a-39c7-ab0f-2c0aa0563679 | -10.78682 | -45.94784 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| e6cfab3a-c1a9-3193-ba79-9dc51c33116b | -5.48324 | -45.12616 | 2026-09-11 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc1edbb1-7d9b-3ca5-98dc-9d4afdfc3bfc | -5.33417 | -45.58935 | 2026-09-11 04:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc086afb-0949-337e-8c1d-04176cb2c3a3 | -10.77957 | -45.94941 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a953b207-486b-3694-8d74-659c1f6c57ba | -11.19203 | -42.78455 | 2026-09-11 04:08:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ddfe690e-6771-39d5-98dc-d03292c24480 | -10.27975 | -45.27309 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a07467e5-d27a-3957-abf5-7d73145f2221 | -10.06056 | -46.26974 | 2026-09-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1192dd01-6c60-3a31-a89e-3c982450f691 | -7.18354 | -43.60331 | 2026-09-11 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 380b7414-f3e1-3161-9a92-7eccc9987000 | -7.09572 | -45.03997 | 2026-09-11 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7abecc7-0b98-38dc-a34b-77555063642b | -9.17279 | -49.94791 | 2026-09-11 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676f72d7-9afb-3c3b-882d-fe441ced0cd3 | -9.3923 | -49.39067 | 2026-09-11 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed635322-c9a3-3bc5-91a2-4c8c4ed37455 | -7.00448 | -43.86681 | 2026-09-11 04:08:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ffbf8e99-5059-3aa4-b4e9-beb281859c1d | -10.77281 | -45.93493 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5744fda6-4505-32e1-b4ae-fd579234ce91 | -9.05826 | -45.78206 | 2026-09-11 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b89e8a8-db3e-38ed-9e95-93ea81193f67 | -10.21988 | -45.21657 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c02a036-30ea-3287-a419-407f40e9068d | -8.27844 | -47.78613 | 2026-09-11 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 839195a2-3e56-32ea-9344-0dfac2fdac8b | -7.15225 | -45.87025 | 2026-09-11 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d328d19-948a-3748-83fd-e029fdad2d28 | -8.62168 | -47.41055 | 2026-09-11 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ad1b472-42c0-3c48-9bd9-168eb916c6a9 | -5.29667 | -44.46944 | 2026-09-11 04:08:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2cc9d626-b7e2-3837-bbb7-e95a28b51905 | -7.34804 | -44.19641 | 2026-09-11 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75c6cb59-bd3d-3fa5-aafd-f522bf56f877 | -8.72948 | -50.59642 | 2026-09-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2294d28b-760a-33fc-a299-76a048f93717 | -10.78503 | -45.958 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3c95475-bf07-3055-84ba-17667bbb5395 | -6.71944 | -45.49044 | 2026-09-11 04:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e45a180-ee93-3e19-ab06-0340765f89ce | -10.36015 | -48.13394 | 2026-09-11 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2e9efad1-9f8c-3ad1-8dbd-7309dd712762 | -11.766 | -43.05308 | 2026-09-11 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 426e2ed6-7911-37f6-a7d5-a600ea889964 | -10.64358 | -46.11908 | 2026-09-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8561ed64-542e-3320-87b5-d87d668159d5 | -10.22148 | -45.20711 | 2026-09-11 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfe72c71-8ab5-3596-a36f-c1310cc669a0 | -8.48685 | -44.74184 | 2026-09-11 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README13.md)
