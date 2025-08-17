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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0e45858-db9c-37d4-a7d9-6377428b0237 | -19.98837 | -45.51594 | 2025-08-17 03:28:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 263e4268-6da6-3490-bfc2-69290e4c75d1 | -18.06373 | -46.36179 | 2025-08-17 03:28:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78180b6c-3678-3e32-93aa-8e1171052356 | -22.80439 | -47.46788 | 2025-08-17 03:28:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5eda3103-dbac-3aee-91b3-4f0086bec95b | -20.29156 | -42.20709 | 2025-08-17 03:28:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5aa3528f-ba15-3cb5-aa40-19ea7b5ccd96 | -10.8627 | -45.356 | 2025-08-17 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 31935d93-52fb-3e7d-b6c5-69f5e8fd11bf | -9.518 | -60.5268 | 2025-08-17 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 824e58fe-96cb-3d6a-85fd-efc25d2be033 | -10.8246 | -45.3611 | 2025-08-17 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3c508f4b-32fa-3d96-808b-2e8fea116485 | -8.9709 | -61.6842 | 2025-08-17 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 71ccf33a-288a-3d44-bccf-e0b859c17ad3 | -10.844 | -45.3356 | 2025-08-17 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| aaca8a7b-2794-3dbd-9551-84ed362da885 | -8.9893 | -61.7024 | 2025-08-17 03:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7d7afc8f-bdb5-3c51-8880-583a156d4196 | -4.9118 | -43.257 | 2025-08-17 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f3ce35ab-5bde-3bce-a49c-0a74c03b0ee5 | -15.748 | -49.9586 | 2025-08-17 03:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fad1519d-3b4e-32e7-8ac6-3de75c24a628 | -10.8436 | -45.3586 | 2025-08-17 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 333.3 |
| a670a165-a773-3719-8a72-c16ae5e651ff | -9.5179 | -60.5461 | 2025-08-17 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8bc0afcd-b335-3c73-afdf-9473a2a760a9 | -8.9788 | -60.4964 | 2025-08-17 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8884e24c-c4a3-334c-abc1-85a62f074264 | -15.7484 | -49.9365 | 2025-08-17 03:30:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 2626c39a-39a2-3d2b-a1e5-4eda361cc6ab | -25.18266 | -50.08318 | 2025-08-17 03:30:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 327a85ed-196c-3b6f-aaa6-b946acfad7d0 | -24.48702 | -50.22627 | 2025-08-17 03:30:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58b77268-c06f-3a2b-a829-22b46d535a34 | -9.5179 | -60.5461 | 2025-08-17 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a3ea4654-6ce6-32f1-a495-1951c0a61563 | -8.9974 | -60.4955 | 2025-08-17 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| f27edd68-8c67-30e0-9f0a-0200100e77fc | -8.9788 | -60.4964 | 2025-08-17 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1ec3c017-f270-364a-aa27-2adc9367d2c1 | -10.8433 | -45.3815 | 2025-08-17 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 8f88bb53-d781-3b2f-9b10-162f11fbf692 | -9.1895 | -59.6364 | 2025-08-17 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 29535428-c382-34bb-ba5b-33d65b9744fe | -9.518 | -60.5268 | 2025-08-17 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6190d191-c6bf-3766-96b4-1bf13c1758ab | -10.844 | -45.3356 | 2025-08-17 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 2c35b634-337c-317e-b3e7-4a8600969ab6 | -8.9893 | -61.7024 | 2025-08-17 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8ca83dab-ed9b-3502-9673-bb6048374635 | -10.8436 | -45.3586 | 2025-08-17 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 1fb43f59-c8b2-39ee-8422-42e1ad9d4ba7 | -8.9709 | -61.6842 | 2025-08-17 03:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ac027e83-1318-3dfd-99af-20540317946c | -9.10596 | -44.70787 | 2025-08-17 03:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f1d4a3-4ca6-3ed3-bc49-cb81787dbf1b | -2.81699 | -48.61343 | 2025-08-17 03:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85fb9e5d-4023-3d9a-8377-6275f33b64a2 | -8.03836 | -47.67085 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b2dea40-16f9-3683-bd7f-736c2dc776ac | -4.92489 | -43.25806 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c238ff2e-05a1-3ee3-a344-769a9b5ca9a8 | -8.03758 | -47.66491 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c7994c5-bb3c-3bcc-8d06-d261e77563dd | -3.9768 | -42.52873 | 2025-08-17 03:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 296b01b6-0da8-34e6-a1b5-dfe823ec5056 | -7.18948 | -43.97096 | 2025-08-17 03:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8d84609-ec71-3435-9383-86241b109d9c | -5.95492 | -46.15408 | 2025-08-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f0191e0-b7ac-35e5-8205-62ae111efaa6 | -8.53699 | -37.72187 | 2025-08-17 03:49:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32f0d060-70ea-3c58-8cb2-39a20f2d045c | -8.03913 | -47.66666 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80bc943f-fd61-3996-8ec0-9abc90a9e338 | -8.76341 | -39.61028 | 2025-08-17 03:49:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91594d2f-1d77-368e-ba54-a571fc3c9bd2 | -8.04184 | -47.67448 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63fde96b-b09c-3688-b0ab-1aa13270756a | -6.19035 | -45.43944 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f30e1d3-b415-3a38-bbe6-905edecf99a3 | -8.50339 | -44.72981 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e47d8ba2-c4d5-3d08-b4bd-22197b294d68 | -9.6098 | -40.34619 | 2025-08-17 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 9cbad4d2-a27a-3090-852a-dbbceb94f16d | -6.55537 | -43.01631 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1298264-0fe3-3bf5-98ce-22bf580097f0 | -7.11097 | -46.10352 | 2025-08-17 03:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0178aaa-6241-3d2d-b9fc-0998616ace6d | -2.81023 | -48.61231 | 2025-08-17 03:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 612c6013-f382-314f-ab07-9113672f5222 | -8.5111 | -44.74211 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d85d4ce-a169-3039-b5dd-88be41f4e9b3 | -7.53311 | -36.72904 | 2025-08-17 03:49:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55cef25b-3f4f-303c-a60b-50628b1bdf91 | -4.91647 | -43.25169 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2cb2ae79-3341-38b7-a957-70a8af9217f8 | -6.07404 | -44.6245 | 2025-08-17 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 451ad400-366e-3f26-b858-171217688a06 | -8.03837 | -47.66072 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ad6266a-b26f-3e12-9ba9-367da262ec59 | -3.97162 | -42.5324 | 2025-08-17 03:49:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7f816427-c8c5-303f-875f-37f694b4d2cd | -5.75452 | -46.66905 | 2025-08-17 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c214dac-fecb-37b5-ba6a-caeb58c7ecc1 | -8.03325 | -47.6656 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 715b1fde-829c-3f52-b982-947d7afa0109 | -8.50244 | -44.7351 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1610f86e-ab6f-3895-be02-71c507c85b29 | -6.19439 | -45.44709 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ebc8136-9b4d-39c9-b7dd-93c7ea919b5e | -6.55464 | -43.02061 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1ef416c-f83c-3f00-aaf2-974dfb5a610c | -8.03402 | -47.66137 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d487c28b-cf14-372c-8911-9d6c15ac4b3b | -6.55317 | -43.02922 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1b965a3-7211-38b8-bc2a-95a842115391 | -6.60261 | -42.73862 | 2025-08-17 03:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2e5058b9-47f9-3568-a359-88a6e5ed6765 | -6.48967 | -42.98035 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1a4e6a1-e9f9-306e-a9ff-75b939dfbce7 | -6.19579 | -45.44393 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9436f9c3-9fe2-3c4e-9271-84677a50c38e | -6.18515 | -45.43834 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 33967eab-6114-32d7-8ad3-41ca0b50e312 | -7.60309 | -44.94048 | 2025-08-17 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3ceb323-2ba3-3d68-b300-97e6609640bf | -6.54802 | -43.03275 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b07d5246-05db-3941-8b52-3030f65373ea | -8.49764 | -44.73423 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e80c0e9-d23c-3d84-8b1f-5b1f226ca181 | -9.61339 | -40.3468 | 2025-08-17 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 766766bf-879a-3ee3-9fb5-ef4421d08199 | -8.04422 | -47.67206 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dedeca2d-4063-393a-8c10-6fa56cb5bc91 | -8.04264 | -47.67025 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3097d50d-6a64-308b-82df-e6d5f0595f0e | -8.0789 | -47.70383 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53d9e762-e126-3eca-9bf4-e776c53c4e93 | -7.19233 | -43.96875 | 2025-08-17 03:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ad5ef2c-2964-3b16-b39d-5c8728b79628 | -6.60763 | -42.73524 | 2025-08-17 03:49:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 462d8551-360a-3739-ac7a-392904407beb | -6.48527 | -42.97953 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18f5f6b9-91fb-3b53-b6ea-25d558ec7f6e | -6.54949 | -43.02419 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 64b46848-cc6c-381d-b302-e66facc8e0f3 | -8.74894 | -44.03812 | 2025-08-17 03:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4876dccd-2aa8-320b-b95c-cd72910a60f2 | -7.11038 | -46.10683 | 2025-08-17 03:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b9d062c-a6d8-3d5a-ae9e-7bd9f9ca5873 | -5.76023 | -46.67012 | 2025-08-17 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9593f78d-4974-3dc0-940a-93bcf3e26eb4 | -6.19524 | -45.44719 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fa7e5fb-cb98-3a76-ad56-2587aa51ff8b | -6.18572 | -45.43516 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 593653ee-59c4-304d-9307-c1e1fe929d07 | -6.61805 | -43.88135 | 2025-08-17 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 63a3e837-23df-3c5a-aeb1-f557a4c97ace | -7.09893 | -41.33459 | 2025-08-17 03:49:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| edad1bd1-34c9-3c0d-84dc-baeee1fb4ac9 | -8.50819 | -44.73066 | 2025-08-17 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4afa8221-be13-3ba6-b933-142214b700e0 | -8.07968 | -47.69966 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 416fe839-a170-37c4-828c-2048566423df | -8.03598 | -47.67336 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc16be2c-6f68-3f95-a04b-bce226021dbd | -9.29112 | -40.24064 | 2025-08-17 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c84da7f-159f-3fe5-948d-6d05c4d4713e | -6.18594 | -45.43839 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1f4420de-8542-3fc3-9218-68f0b968d5d5 | -7.04208 | -42.20732 | 2025-08-17 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 93552476-ecdb-3f88-b9ed-dd01b92ffb7e | -3.94288 | -41.83329 | 2025-08-17 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eb6f80d5-afed-3214-abe6-8e74c684ef9f | -4.92029 | -43.25722 | 2025-08-17 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2623accf-bf0e-313d-8407-7eeb72a8962f | -8.03989 | -47.66246 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a190a7fe-384c-3bf3-a696-6e16c9446ead | -3.97608 | -42.53313 | 2025-08-17 03:49:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ec68c087-ebef-3a8e-ad2e-5442c10db836 | -8.03759 | -47.67512 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3028de78-6312-30ef-bf45-cca7c7c2e42c | -8.08045 | -47.6955 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a7cf04-57ef-3223-9053-52a8bdca1311 | -8.03169 | -47.66389 | 2025-08-17 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70783911-1920-3c6d-9f41-498e030dc7bc | -6.19497 | -45.44383 | 2025-08-17 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3e81b06-a8ac-340b-916d-41316336f26f | -7.42051 | -42.02831 | 2025-08-17 03:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ce661bd-48d1-3608-9067-970079b85bf6 | -6.54875 | -43.02848 | 2025-08-17 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c81f9ea3-9596-3c23-a82e-2ace2949cf23 | -5.09564 | -42.79689 | 2025-08-17 03:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ed3f2c3-2c10-3ac3-9185-aeee2789eb4a | -7.19613 | -43.97441 | 2025-08-17 03:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3d43256-5beb-3fe7-afce-71c28fa0940b | -5.95467 | -46.1588 | 2025-08-17 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
