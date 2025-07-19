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
| 1b204a17-b545-36d1-9872-0ea9709b91b0 | -9.80711 | -48.55962 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3e4b29a-01d2-3cd4-91a9-48fc2bb17724 | -12.97479 | -46.92451 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b1208d4-1e13-3a0c-8ec3-adb2f4953126 | -10.62697 | -44.76448 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8eede488-04ae-386c-88d1-f4fceca505b3 | -15.89765 | -43.45616 | 2025-07-19 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d86caac4-c72b-363e-a064-277968126669 | -9.80379 | -48.55909 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 698a1015-4ae4-33fe-97f7-f31e99512c28 | -14.83746 | -49.11864 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a42f2e7-9b4c-3c61-ba1c-98d1db438ce0 | -11.47921 | -47.32183 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f865d097-a5ad-3bc3-8d00-931c355a5e00 | -10.81756 | -49.29063 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43c6ad3e-728d-3874-867b-31d8e06b7816 | -10.88087 | -47.15191 | 2025-07-19 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb03dd74-a985-3ec8-8e75-c655ea7e0181 | -11.48262 | -47.32236 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f0909301-8272-30ca-b5d9-6354ea3169e5 | -9.81333 | -47.73974 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d65c0eb4-27f8-37a2-b918-ba1dbd0c8b89 | -10.75303 | -52.76419 | 2025-07-19 04:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f5a3d1c-f9f4-39b8-9d40-3c6a57816426 | -12.06431 | -47.34921 | 2025-07-19 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 686ea86a-4c2e-3788-88a4-f137bfdff0bf | -10.98473 | -49.39377 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2abf698-f858-3a38-b1a3-809cf0fadd8a | -10.47125 | -47.94836 | 2025-07-19 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3da31ffe-7285-3408-9fca-24402319be3f | -11.73395 | -48.52538 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c022b3b2-dbee-3807-95b2-832892d8c91e | -12.99051 | -46.93893 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf6df684-458e-37dd-a326-4ca0e0e37013 | -11.02419 | -50.43153 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43e7ebd6-b3fc-3872-8c81-f56501a6a046 | -8.30644 | -55.10763 | 2025-07-19 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fc8e152-8179-3c51-9608-ae6e24f4b240 | -10.63388 | -44.76273 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 219085e9-2234-305d-817d-767cdefc2add | -11.56968 | -47.09478 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a84eceb8-4570-3292-b44d-b16f193a0127 | -12.46296 | -46.92899 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86687bc4-ac5b-36f8-86bb-e950b088f690 | -11.46309 | -48.15489 | 2025-07-19 04:36:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7857f90b-68cb-304b-9115-7466c486811d | -11.32247 | -55.21079 | 2025-07-19 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 335b0d33-0b61-3812-98df-208034402d4c | -9.01406 | -59.5384 | 2025-07-19 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e02ff7da-fd28-3dfa-8212-09723c81ff88 | -11.96304 | -46.39545 | 2025-07-19 04:36:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1706ce3b-f803-3e5a-a080-bcccc3f1ddd9 | -12.99339 | -46.94354 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52626540-bc6f-37a2-89a3-1f24c7cd2b59 | -12.57629 | -44.74825 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef60858b-19c2-3508-89e6-b84435ab6db9 | -11.56053 | -47.08561 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5cf1153-9d45-3a18-89d9-d97fa0e0cd1d | -10.63086 | -45.23537 | 2025-07-19 04:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f910767-1eae-3c6c-aacf-0a510875269e | -10.41758 | -48.61408 | 2025-07-19 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 165f7d0e-082d-35cc-a9e6-eb5bf367a8b8 | -8.9663 | -61.50912 | 2025-07-19 04:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73fc84a3-916c-3f83-9e7c-376363c27027 | -11.41282 | -42.07384 | 2025-07-19 04:36:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69d6a6bd-8962-3914-ba41-09bcda42fb88 | -10.67033 | -49.68378 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 793f0eee-fb63-33b4-9576-5ae73fcd7935 | -8.26334 | -55.16645 | 2025-07-19 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12247b77-29a5-3c05-b72d-ccf84a49166b | -11.55938 | -47.09319 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df3bd457-1439-3415-b69a-79ec7cc3deb5 | -15.7252 | -46.86254 | 2025-07-19 04:36:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a7b177b-4fa3-322b-b114-861080495d4a | -12.57561 | -44.75323 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e81aefde-2ec4-3825-b330-4e4a2ede7ba0 | -11.47183 | -47.32449 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d46fb46-89ea-35f2-8880-68beace217d6 | -10.67874 | -49.6742 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7121eb6-e0e1-3ecb-a35a-d179d5fcf984 | -13.60523 | -45.63809 | 2025-07-19 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a43b7b-fadd-3326-b867-5364a5415c59 | -9.79992 | -48.56206 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ee61613-59f2-33f3-bf03-d05866314c43 | -9.81388 | -47.73619 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4a39158c-7327-3bd1-8bb5-df48de503831 | -10.20941 | -48.3656 | 2025-07-19 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2264e5ee-de03-353c-9756-b4b69d8a500c | -11.55653 | -47.08886 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8709b7f0-164e-3b89-afd1-14e45f93f449 | -9.80555 | -47.74577 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1666a328-83ca-3f31-8210-f983ac7c9f57 | -10.67091 | -49.68022 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33c4aeec-a803-3cf5-8fe3-db89f3fe9a0e | -11.46198 | -48.16203 | 2025-07-19 04:36:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f6fd467-4f62-3163-b577-5ed46ae48c77 | -11.37367 | -54.34439 | 2025-07-19 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6354cf84-7fa9-34e4-ba11-cbbf9de95e60 | -10.71673 | -49.48021 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65184328-5042-3f5c-a990-6da788cce047 | -9.8396 | -48.37485 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 030f789b-f640-3c2b-8e32-63d81922e8f6 | -11.82313 | -48.21564 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c2b68c3b-fe9d-39d3-9bd4-a1483365671a | -10.3733 | -49.9149 | 2025-07-19 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9e682d0-05ba-3f24-ab13-94f460868565 | -12.71461 | -47.79771 | 2025-07-19 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed47694f-0802-339f-a028-7c7dad12dcf7 | -8.97436 | -61.51192 | 2025-07-19 04:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a957795-2c01-3810-8acd-06605b4bb128 | -12.42532 | -45.36657 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ddd62ee-1c24-3ff2-abd7-943b070a8f22 | -11.72618 | -48.18563 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce0a6e39-96c3-3f74-bc86-6d3af0888028 | -11.4758 | -47.3213 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04d63112-a614-3c87-8213-c1e8e59f0715 | -11.72953 | -48.18617 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b7546fe7-a834-3eab-bbb0-593a0cfde894 | -15.2362 | -47.94946 | 2025-07-19 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b237c4c0-ee74-3138-969b-b526a43b7b12 | -14.84301 | -49.12691 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b946a98a-ce5f-3146-88da-c83b485d7981 | -9.76734 | -48.74672 | 2025-07-19 04:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 907fba0f-0951-3952-b8d2-0610ee78be8e | -12.97186 | -46.9202 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bffd3718-9380-3f70-bd72-871275bfdbec | -14.75259 | -48.26505 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 343ee717-d9a7-30d1-a6c9-fabb36cdcfe8 | -12.96083 | -46.92222 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e414af6-f552-341e-ae16-6b4a19b8f56c | -10.22805 | -48.24642 | 2025-07-19 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 947a5bff-84d7-346b-8e92-73641710e341 | -11.83482 | -48.20654 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ea04a31-ca5c-33a6-bdfa-fcaa92e9ce2e | -10.63077 | -44.76504 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fce04d02-0a77-34dc-9cd2-a50026948543 | -10.64413 | -44.4868 | 2025-07-19 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cde65226-0b6e-3426-abd3-a1d76d5818ee | -10.37666 | -49.91545 | 2025-07-19 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d54e7cca-00b0-349b-8c2b-213a897d0a53 | -9.43267 | -48.85032 | 2025-07-19 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a9c70f5-3b5f-3517-ae9f-28efcd26fe2e | -8.26252 | -55.17116 | 2025-07-19 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd4d28dd-905a-3a7f-93a8-1cad8b8f0a5c | -14.8369 | -49.12224 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ef0a30f-fd39-34c6-a593-3a518beaddcf | -15.8971 | -43.4606 | 2025-07-19 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7cdc96f3-5e07-305d-8fcf-07e9d4db0476 | -8.26085 | -55.18067 | 2025-07-19 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f34c31ef-9b79-3b3c-840c-0811ebb3bd83 | -11.84512 | -63.22812 | 2025-07-19 04:36:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7127c80-b5ac-3282-9223-0979a2a86004 | -10.64798 | -44.48738 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9ea8977-93f6-3c75-9a3d-b94882229f54 | -14.78392 | -48.29245 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c41ce61e-d820-3306-ad67-6b2b6c0765cd | -9.80766 | -48.55613 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5404d329-e9a9-38c9-8b4b-b8187ab9da8a | -10.68151 | -49.6783 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77fd0411-ce86-37be-aa59-4dca965966c1 | -11.56281 | -47.09372 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71e73d8d-8786-3b1c-8e1f-fa781472733a | -14.75937 | -48.26614 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf73c146-8a20-3537-bb79-5d1c6821c44f | -14.75965 | -48.26934 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01736e98-1a5c-3a8e-ae28-263d259ec017 | -11.45864 | -48.1615 | 2025-07-19 04:36:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3391568a-e29c-3712-aa13-f2167ec19434 | -8.3102 | -55.11304 | 2025-07-19 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d3d92b2-379d-3fc4-a102-3fe4ab1fe975 | -9.80601 | -48.56662 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 606f333c-7f1e-3bc9-b57a-fbc398b27e1e | -10.98586 | -49.38672 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81cb2f7f-21e3-3c8f-8f28-0df4f1093fd7 | -12.37326 | -45.72937 | 2025-07-19 04:36:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82503e38-9353-3ee4-9c9e-7627d8cb0b46 | -14.77255 | -50.53136 | 2025-07-19 04:36:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eaeb3ce-1560-38a2-bd6e-4848c10b3565 | -9.8033 | -47.73816 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80b73cd6-0933-3766-b0a4-0f1b6c1afed9 | -9.81109 | -47.73211 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 477d0a9d-6400-3040-8f9c-f88974f6a81c | -12.13857 | -50.24076 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5700d4e5-0714-33c0-b30f-599ad8ea092f | -8.97305 | -61.5185 | 2025-07-19 04:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b146282d-c78b-3fa8-bc77-b35d0bd067bf | -12.5759 | -44.75164 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31d23336-2e01-3ed7-b30d-f643e3c40245 | -11.32285 | -55.20992 | 2025-07-19 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76eceb99-7b94-3b9f-97f3-d315d70d5620 | -11.82592 | -48.21973 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a704b05f-bb35-3f0e-bb17-5b9fb253c599 | -10.62943 | -44.76683 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed15eeb0-fbdf-3447-8fcd-41e523abfe03 | -10.81812 | -49.28711 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b5053e7-1b66-304d-9593-cf62d8fe3149 | -9.80324 | -48.56259 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6adf828-5df5-3f42-b8b0-11950bf0fc1a | -13.61272 | -45.63924 | 2025-07-19 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README23.md)
