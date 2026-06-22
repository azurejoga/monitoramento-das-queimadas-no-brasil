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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a8eedbc-24c9-3272-94b3-2f61648b3861 | -6.5094 | -44.6847 | 2026-06-22 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 33f05433-eb17-3c94-964f-a24df51b6c30 | -3.5043 | -48.039 | 2026-06-22 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2891afc6-9206-3a12-a95b-53556c768730 | -14.8465 | -49.2863 | 2026-06-22 00:00:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1f2ad9e6-058d-3f13-a7c4-cf8f1ec9282e | -6.5092 | -44.7076 | 2026-06-22 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7f170a67-4c4f-3412-8985-10a9b3bad3dc | -16.02474 | -43.41154 | 2026-06-22 00:01:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 68f6b090-b47b-37fe-8cc5-b0994665fa4e | -18.24698 | -51.28238 | 2026-06-22 00:01:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 84838da4-f96f-357f-9cb1-48745749cb11 | -21.53653 | -41.14677 | 2026-06-22 00:01:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 8241c360-d8f5-33ef-8aaa-53ffa5752ada | -18.25868 | -51.28097 | 2026-06-22 00:01:00 | TERRA_M-M | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d0f8fd6f-7a47-3e39-9118-502c589f6b90 | -17.22466 | -43.6766 | 2026-06-22 00:01:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 10081619-ed92-3b0a-be06-ff3bfd9b65f4 | -16.02641 | -43.42267 | 2026-06-22 00:01:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8ba67a15-bf67-347c-9f1e-cf8a69cb94eb | -18.48646 | -51.57611 | 2026-06-22 00:01:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| fb2e3e23-5a37-365e-a11b-30ed4a66b27c | -22.13052 | -41.45375 | 2026-06-22 00:01:00 | TERRA_M-M | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| abff7421-0ea2-3916-8897-efdaf53f3455 | -18.49158 | -51.56994 | 2026-06-22 00:01:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| be76f64c-5dbc-3a2c-bad9-689ce6fc92ef | -20.28165 | -48.77399 | 2026-06-22 00:01:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d16ae012-ecd4-3c75-b9a3-d0721000e982 | -20.28309 | -48.7863 | 2026-06-22 00:01:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7c017e95-087d-39c9-a97f-9dcdf80b17f4 | -14.97736 | -45.45377 | 2026-06-22 00:03:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0459d60d-51b5-3446-b27f-7ae813cee6f2 | -14.83775 | -49.29969 | 2026-06-22 00:03:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c61635c3-6260-3826-8c54-8b1917557ecc | -12.47226 | -55.13357 | 2026-06-22 00:03:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 3ecb7eec-3bf6-3ff5-bf65-4cbd7636ed25 | -10.17323 | -51.66601 | 2026-06-22 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| d01d8271-e145-3c50-a8b2-2b8abcdfbe7f | -14.11372 | -49.87714 | 2026-06-22 00:03:00 | TERRA_M-M | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 661785a0-2106-3170-b733-d5a87a7a7ed1 | -13.30282 | -45.22011 | 2026-06-22 00:03:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a62ec759-508f-31f0-a0ae-52166dd23ac0 | -9.6896 | -47.69444 | 2026-06-22 00:03:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf298766-9e1b-32c2-84cc-ef58a7915105 | -11.11176 | -54.14541 | 2026-06-22 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 21a90cab-5af4-3bc7-945a-7c5d78ab3727 | -10.17921 | -51.67226 | 2026-06-22 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7865c60d-733c-3ed5-bf6d-b41f8f4e0689 | -10.05584 | -48.08836 | 2026-06-22 00:03:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f001a34b-41b0-301a-9249-0b3f08840c2a | -11.05682 | -52.49326 | 2026-06-22 00:03:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6562fe99-3d7c-3588-88e8-e569ff6c0148 | -11.09857 | -54.14693 | 2026-06-22 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d81c6e87-7fd5-3607-b98a-5ca61eb6d3ec | -13.30141 | -45.21041 | 2026-06-22 00:03:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1f43ee22-d35c-3a8a-b98b-1c5f21039dae | -10.17758 | -51.659 | 2026-06-22 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c9d101f7-c499-3d07-9871-02c677ce7f07 | -11.11102 | -54.16177 | 2026-06-22 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7e67acfe-9e49-3054-b01f-233fccf41f64 | -12.85141 | -44.39287 | 2026-06-22 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c7488a0a-5077-3e42-8a5f-52c233d0d7d4 | -13.28944 | -45.19238 | 2026-06-22 00:03:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2b2e6ba8-515f-3d36-880f-41a98dfbb950 | -10.54087 | -47.72699 | 2026-06-22 00:03:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b933c755-72b3-3344-b4ae-6fa8cf61c829 | -12.85297 | -44.4035 | 2026-06-22 00:03:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 32800e2d-ba52-3034-a01b-7162ad0d7828 | -10.418 | -46.3784 | 2026-06-22 00:03:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7e8d105d-0fa4-3a2c-ac53-22cbf3da834d | -10.19431 | -46.29766 | 2026-06-22 00:03:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4cbfc530-0073-3f67-9837-0b3053387632 | -13.52174 | -52.16808 | 2026-06-22 00:03:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3d45f908-b50f-36a6-bf03-152da7cb12fb | -11.09605 | -54.12575 | 2026-06-22 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 063ab070-38e7-30c3-9e48-b6d78b8e02f1 | -13.5608 | -43.51263 | 2026-06-22 00:03:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 33327d48-0380-3ed9-b322-f954fc636847 | -13.29086 | -45.20209 | 2026-06-22 00:03:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fba9745f-2456-315f-938b-74aaef2929db | -12.07133 | -48.42535 | 2026-06-22 00:03:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6c6e5131-8cf1-39f6-a160-af022ff68548 | -10.18386 | -51.66459 | 2026-06-22 00:03:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1f9fd142-10e1-3c4f-a749-e18f49787350 | -14.8364 | -49.2888 | 2026-06-22 00:03:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bb4119df-ff4f-3db0-ab33-62692d65eb79 | -12.20365 | -47.96923 | 2026-06-22 00:03:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 87c8d8c5-47cb-3d3b-9597-9b0a25f5df83 | -11.10862 | -54.14045 | 2026-06-22 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f03fc56d-5f0b-303f-890b-29f1fef4e6cc | -14.84606 | -49.28756 | 2026-06-22 00:03:00 | TERRA_M-M | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ee649b7a-614f-3748-be95-47309b2bfa18 | -13.30422 | -45.2298 | 2026-06-22 00:03:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f92bec65-09ca-3700-a9aa-72bf4a8e8151 | -11.90524 | -43.41283 | 2026-06-22 00:03:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5b110037-71e1-3c42-8d51-c70a6ecc613d | -14.15418 | -44.24437 | 2026-06-22 00:03:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fd626aa7-882a-3e5b-845b-e9a6cfb45e88 | -10.5421 | -47.73594 | 2026-06-22 00:03:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 548abccf-e18f-3dbe-b0d6-671ec629edc9 | -11.05488 | -52.47738 | 2026-06-22 00:03:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d136915e-eba2-3b22-8b9f-3271844aa6b4 | -6.50951 | -44.70984 | 2026-06-22 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8e36a305-c83d-3d36-98bd-b41a480db726 | -6.23801 | -48.52175 | 2026-06-22 00:05:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6023ab43-9f92-317f-91e5-cda8a45254e0 | -6.506 | -44.68581 | 2026-06-22 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 61ac96c0-f805-3d88-abe3-226609b7876d | -6.24925 | -48.53812 | 2026-06-22 00:05:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19dd54be-fa17-3593-ad1a-7274ef2da0ac | -6.50638 | -42.22235 | 2026-06-22 00:05:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7ba6dfb9-aea2-31d6-a434-cfa7e1788ef3 | -7.31854 | -46.55428 | 2026-06-22 00:05:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ebe2132c-4703-3759-ba69-707a638f06cf | -6.49749 | -44.69931 | 2026-06-22 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3fcc61dc-4411-341f-b702-6b82cb5f059e | -6.6952 | -47.42704 | 2026-06-22 00:05:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee483fda-53ea-352f-a5f2-479d7ab3b303 | -6.50775 | -44.69777 | 2026-06-22 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 234.0 |
| e833b671-1f44-3e01-a32d-78f0f7f7507c | -8.02036 | -49.64425 | 2026-06-22 00:05:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 909736b8-ffdf-3c98-b937-fe70815c7608 | -7.95589 | -47.42351 | 2026-06-22 00:05:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 30e913ba-aced-3456-a99e-e47ead9c76d6 | -8.61606 | -47.79436 | 2026-06-22 00:05:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 261d505b-5abf-3a43-92db-e8c6919f1611 | -6.24803 | -48.5293 | 2026-06-22 00:05:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 53d45011-9537-3fd8-969d-376bedf05f04 | -6.69647 | -47.43607 | 2026-06-22 00:05:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f63b15b7-76ac-3e69-a596-08255369f63e | -7.31989 | -46.56376 | 2026-06-22 00:05:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dfb6006f-b8b0-3804-842b-f72dac3ad20a | -3.99311 | -47.9394 | 2026-06-22 00:07:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03d9dad0-7c78-30b5-a0b3-fc3f8aa448b6 | -3.51704 | -48.03402 | 2026-06-22 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| bd18d219-a345-3d79-a6f2-31e3801b2083 | -3.51828 | -48.04295 | 2026-06-22 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 69c83251-7cac-37e8-ad96-01dff2d70d8d | -3.50812 | -48.03526 | 2026-06-22 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 1b621698-8ee8-3664-85a5-c30b6ab24b9c | -3.50936 | -48.0442 | 2026-06-22 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| b5f8d0d5-1fa2-3b30-a4cc-3dfb265ece8d | -6.5092 | -44.7076 | 2026-06-22 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 15df2acc-ebb2-3c98-b381-3c8eec45d82b | -6.5094 | -44.6847 | 2026-06-22 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 866e1079-9e43-3c50-992c-7892c326220d | -3.5043 | -48.039 | 2026-06-22 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 269ac9b9-a6ea-3fce-a1cf-117640a5ca5d | -6.5092 | -44.7076 | 2026-06-22 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4d668f71-a6db-3da4-8ec4-0b6cb643a7a7 | -6.5094 | -44.6847 | 2026-06-22 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 18e9362e-9c72-3598-9069-89aa99d3ad91 | -3.5043 | -48.039 | 2026-06-22 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 40126ec6-ca7a-3a79-adf4-70757116e9a8 | -6.5094 | -44.6847 | 2026-06-22 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7a97354c-c1e2-33d8-ab08-f105635b9083 | -6.5092 | -44.7076 | 2026-06-22 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8fe9cc92-9221-3d40-984f-b8cafb320b82 | -3.5228 | -48.0383 | 2026-06-22 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ef33bfd3-a6ef-304f-bbcc-a25cfb5d84c8 | -6.5094 | -44.6847 | 2026-06-22 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2531db75-d53b-35c1-bb06-75c6812b2319 | -6.5092 | -44.7076 | 2026-06-22 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 6e507677-7916-3470-a5e8-a2650676d3b5 | -3.5228 | -48.0383 | 2026-06-22 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 140ad47c-3c54-3e35-8cad-5476998fa653 | -6.5094 | -44.6847 | 2026-06-22 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 480aec56-a2d0-31d7-a4f1-8b0a6d6815c0 | -6.5092 | -44.7076 | 2026-06-22 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f0723843-a756-36fa-82e7-eeeef2b637a4 | -11.0528 | -52.4706 | 2026-06-22 00:56:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 852d7532-a0e7-3694-bb3e-9c6cab991c71 | -14.1222 | -58.372799 | 2026-06-22 00:56:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7fcadee-ba2a-30c9-94e9-1fedb148ef92 | -14.1238 | -58.380001 | 2026-06-22 00:56:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 021b5e85-7d25-3d28-86d9-1883b7b670b6 | -12.2174 | -57.272301 | 2026-06-22 00:56:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5764517-cdaf-3201-a7af-d05b7b6a4207 | -14.114 | -58.382301 | 2026-06-22 00:56:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49463c28-4182-3c67-a623-8343813588de | -11.0918 | -54.1231 | 2026-06-22 00:56:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea3c874-371a-3fbb-9d44-4a9ff6cf221a | -11.0947 | -54.135101 | 2026-06-22 00:56:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8598b4f-2961-319a-b029-477c55319ade | -14.8267 | -49.260201 | 2026-06-22 00:56:00 | METOP-B | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f222b235-e7de-385c-bcd2-280303275ccc | -12.4329 | -58.385399 | 2026-06-22 00:56:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3c5cdce-4a98-38b2-89db-254ac324f5e6 | -14.1124 | -58.375099 | 2026-06-22 00:56:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ecb92e2-03b6-3a08-a938-2105ba6712d2 | -12.4362 | -58.399799 | 2026-06-22 00:56:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7af677dc-b1ad-3c95-82c6-0e7a7b934a27 | -11.1142 | -54.130199 | 2026-06-22 00:56:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cafe0e6-1995-3a04-91dd-4034b3952e41 | -11.1016 | -54.120701 | 2026-06-22 00:56:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d5fcde7-b133-3559-92f0-33e9f4f5c12a | -11.0489 | -52.455101 | 2026-06-22 00:56:00 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da0f9572-8edc-3801-b1cd-057a2b9e50d4 | -11.1045 | -54.132702 | 2026-06-22 00:56:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
