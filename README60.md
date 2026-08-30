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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f995360-f62d-31c7-8270-2cecae3afe28 | -9.71136 | -60.72825 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bef09c81-ab57-3509-bb07-5fadff9492b1 | -8.95971 | -62.39518 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa71a79a-bc8e-34c8-836b-693b3df0cd3d | -9.17339 | -59.6059 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf98091e-969a-3788-bc6e-eec340c7cf50 | -8.6056 | -70.21509 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 555c6afe-c9d4-3d2d-8303-d83c7f890af4 | -9.8474 | -60.27438 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e4cecb1-c3ad-3ee3-b8d2-c3dd3ea8a606 | -9.88878 | -60.27022 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64b854e0-b84a-3f07-8948-e2870a10d200 | -5.89301 | -57.75973 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c94b8fbb-22ef-340f-8ef0-8e5fdcb7bd32 | -10.48874 | -59.60779 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92191c15-0598-32cd-87f3-2d3d4a4d87d7 | -5.89801 | -57.74952 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b275dc9-c39b-3f4b-9351-e5e311aee55b | -5.89246 | -57.76329 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98b84e57-dd88-36b8-8aca-94b6fb75dfc0 | -6.62057 | -53.18122 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0d22659-cedd-3f04-9d77-5c9a4734667d | -9.01347 | -65.40161 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 576fadfd-0b83-378d-a874-e5459f9bfce1 | -7.55246 | -61.30308 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba1f16ad-71c0-3bae-8607-a6429443ed35 | -5.98854 | -55.73077 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8f8c90-4263-3fdd-a06c-3782b2bb4dff | -11.80439 | -51.04393 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| c2545825-d056-387b-a0fc-f1a1b952b6ff | -11.16267 | -51.30085 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dc06ebeb-d7d7-31c7-a03e-4ea64a64b6cc | -10.49482 | -59.61235 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94d7145c-fa87-33c7-95f9-97e8a4f381e2 | -7.30042 | -60.61502 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5012bd86-7663-3d3c-b9c4-2241c98489e8 | -5.96652 | -57.67621 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2799f312-d97e-308e-9834-a0e8a9d9b2ae | -11.16308 | -51.29765 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a258d063-7711-39e0-9162-374bfb999292 | -11.24058 | -54.00479 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b19700ab-eda6-3e1c-9c9d-0f9ca9e2d337 | -5.71816 | -52.28575 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cf2a5ae-3bfd-342e-9fef-8e8810edbde3 | -9.93706 | -60.52628 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c30a2a78-760e-35b0-9741-24c38c70a0ce | -6.78114 | -55.68605 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d48696b-ce8e-3440-b3a4-d9c488ab7bf3 | -6.32442 | -57.73828 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95934f67-d13c-3771-a96a-30ea28911e84 | -10.57277 | -59.6138 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 914c3de6-dade-3620-a158-b192b1f17a58 | -10.48766 | -59.61479 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b839e45d-6761-37b6-bb7b-508c3c1d9be9 | -9.89209 | -60.27075 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20bd38b8-d35b-33b7-b1da-7ffd607cdf6a | -10.99316 | -50.52216 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bba19ca5-c114-372c-b724-942cf62f5ffb | -6.95342 | -55.7085 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a7715ad-580e-3e0c-b2db-decb79f7acc4 | -6.88827 | -59.40981 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b651b68-317e-36ed-8998-1583ae74d11d | -7.55643 | -61.32241 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1d9c9875-27db-32d6-953d-7c3e28ba4978 | -6.88508 | -59.45185 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b84c34f9-fcbb-3e0b-aaf2-7d03b4b995d6 | -9.06848 | -65.48784 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ddec8ce-1d72-3515-b4a8-91a1409cce83 | -7.56509 | -61.31233 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0b92f74-491a-3992-aa5c-057dda23fc6b | -11.80524 | -51.03711 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d2d8ad14-c5f3-3171-95c9-5545c361f33a | -6.71345 | -58.56637 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e066e4d-45f0-3af7-b864-864e449e3afa | -9.12563 | -50.58968 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 403763e9-9cb4-341b-9ecd-f53fab3d0164 | -7.56388 | -61.31978 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2139eb36-a30c-38cd-a7b7-9bbf7682fa64 | -10.75248 | -54.03481 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 002e6af8-6764-3bcc-8be1-e41f1b041f7a | -6.1637 | -57.78638 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78d954ab-e80d-3665-b4f2-291cfa87981a | -11.18279 | -55.10274 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26df1b14-b047-30ef-bf24-fe8c4c746140 | -6.9064 | -58.98749 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a35b7a61-9c3a-3d25-96a8-90422283c6d7 | -7.45815 | -70.13445 | 2026-08-30 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a88ebc5-8a48-39b5-95ec-e42212cdcbbf | -6.10591 | -55.81975 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0717b494-f7a3-3003-b3fb-4a1bc44d4dc9 | -9.09444 | -65.48824 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2d3f140-382b-376e-80c3-51542026bbdb | -10.48212 | -59.60674 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a07d2a9e-4f2e-3d2d-8641-8985f0f6732c | -9.05132 | -65.41248 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 62919c88-bbd6-3e3c-a11f-967d3f688164 | -8.25123 | -62.75588 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6581bd9-9309-3c0e-99b0-7069ed91f208 | -7.23707 | -60.62336 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 555a61b1-abc4-3f73-b17d-7fd720f33218 | -7.30047 | -60.59299 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9008a71a-bbe4-3935-93cf-2347db196ba5 | -11.03702 | -57.2384 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da92d1e9-70cd-3e59-a3e5-578405ee7dc0 | -11.16439 | -51.2952 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fdddbc17-ff2e-3f93-ac99-87937ac82315 | -6.12761 | -57.69343 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2adbd0a-3461-304e-b8de-6ee98e52a65b | -6.849 | -59.46376 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d03b0b6-dc6c-32c5-ac18-4e5c257f27fc | -7.00605 | -59.65594 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaaf64db-d37a-363d-9400-35ca90e1d7e2 | -6.12461 | -53.55965 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b00a5ad3-63b0-300a-9c85-d00eb801a452 | -6.1793 | -57.77418 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f7fedf9-2598-3ef3-93fa-e142d3f364ca | -5.86264 | -57.55373 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9ebce02-4ebd-3f24-9048-e771772d51f4 | -8.96194 | -62.40374 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aca551e-37fd-3bda-b743-a17ce27a577a | -10.4882 | -59.61129 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4978cd67-a00e-39e4-b3f3-9962ec966901 | -8.50003 | -55.29401 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 780ad9f1-fbc6-30d5-94f3-36ce4d7e6dfa | -7.57005 | -55.56541 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c882d8e-037e-3b92-9858-8d887f3ca682 | -5.96933 | -57.68032 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 325632f4-d192-3fc0-83ad-bdc7db23fa5e | -11.02357 | -49.69148 | 2026-08-30 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fdc01e2-cf72-343f-a7e0-4930cd9b16ef | -9.70857 | -60.74594 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05a29b4e-5ac3-391f-81f6-7341ed5a3b44 | -10.4926 | -59.60482 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ba5c5ae-b3bb-3319-9912-7a03a7770809 | -8.23927 | -54.95751 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f521f12d-27aa-3516-aa63-d11809810796 | -7.24658 | -60.62853 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47299008-f1c2-3ea6-b9eb-dc56f861ff1f | -6.76972 | -55.66211 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca53dcda-c28d-388a-894a-45009251842e | -6.15926 | -57.79301 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5b1272f-b615-3660-b851-2365d506635f | -10.7577 | -54.06076 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3dfcd0f-2685-3cb4-8eed-37cd4c312174 | -5.98839 | -57.69059 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76a4dc69-d4d8-304f-b6eb-5ad8b5146cac | -6.94677 | -58.94775 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf6a5455-f625-33f8-b1cd-0533a7d83e55 | -11.2429 | -53.98799 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9feec78f-2e20-3dee-ab7a-a56dc07833a3 | -8.60643 | -54.77303 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5d7679a-3f6d-3d02-b014-331af153431f | -5.95816 | -57.68589 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ece7239-81ca-387a-aa99-14da1c2d70ae | -11.19084 | -55.10394 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90818d2e-3f1c-3914-8265-a9ba4dd943e4 | -9.95564 | -53.99891 | 2026-08-30 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edd54def-6a9d-3cbb-92c4-0808ccf69f8f | -5.88303 | -57.77995 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70b15c2d-284a-36cd-beea-1a4e0d4980a9 | -6.1248 | -57.68933 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d24e52-d4d1-3a7d-93b9-f7f5ac63563a | -10.48597 | -59.60378 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b337240b-8865-303b-bd53-4c632265a024 | -9.87336 | -60.3036 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9983a585-3be8-3113-85e1-b753f0a7387b | -11.8021 | -51.0343 | 2026-08-30 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 944c412e-cf7e-388e-b62f-aac11eb547e6 | -5.4876 | -57.1416 | 2026-08-30 05:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 2044ec2c-379d-3c17-b4ed-42c600be71bb | -4.9604 | -55.8424 | 2026-08-30 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 7c19a77a-ee2b-3232-b7be-c6c32559db37 | -11.8018 | -51.0556 | 2026-08-30 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 787c6742-785c-3208-af11-954ffbe550f6 | -11.8208 | -51.0535 | 2026-08-30 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 51d571b3-9e45-33dd-80bd-ff2d5a5745d9 | -11.8211 | -51.0322 | 2026-08-30 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| cda0fbd6-532e-3a3e-becb-3644aa533ecc | -9.8927 | -60.2752 | 2026-08-30 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d77e0551-1a9b-3ecf-9fd6-9955c9a87ef7 | -11.72052 | -54.52987 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcee4294-9273-3553-a414-66102c9cc515 | -11.71114 | -54.5331 | 2026-08-30 05:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f146850-0429-3a0e-9579-124bfc7aef21 | -14.78178 | -59.57104 | 2026-08-30 05:21:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c153e4e-8851-3199-b07a-4378db63ca6e | -14.41845 | -52.55583 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 472ffd79-2ac2-33d7-ac87-8f052346481e | -14.91815 | -52.63621 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa16b57f-0e96-3467-9bf3-7d097722ea6e | -15.61924 | -56.40582 | 2026-08-30 05:21:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03d92285-af5e-3357-a9f9-c6135cb4c036 | -14.15768 | -52.81336 | 2026-08-30 05:21:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8c756d7-4c3e-3fbb-b55a-526b66ceb655 | -13.17554 | -55.66378 | 2026-08-30 05:21:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 901f0296-3f5a-34e4-8070-3321283c4a94 | -14.42838 | -52.55978 | 2026-08-30 05:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2a53a50-a061-3e04-b0fc-038049dcc9b6 | -14.25208 | -54.67815 | 2026-08-30 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
