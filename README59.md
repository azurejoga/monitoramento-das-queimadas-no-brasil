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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f117fbf4-0d83-3982-b1e4-dc56707b53e3 | -7.62307 | -43.84349 | 2025-09-27 05:59:00 | AQUA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d2071bce-db75-391a-b328-fc26b18a598a | -7.77725 | -46.93576 | 2025-09-27 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 84074dd3-b766-3c20-8aa2-eae827121fb8 | -7.80096 | -46.95729 | 2025-09-27 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a567a28f-9f64-3f3e-a6d1-cdeca3227edf | -10.11693 | -45.32568 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2c3c8cff-9dd2-39b2-8c18-aea858ecfa4e | -11.23878 | -45.55093 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| aff710f7-d736-30a8-94cc-3cee5b3afd0d | -11.43588 | -44.97354 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4cfadfeb-035d-33ae-907f-5f3fda56935d | -11.42823 | -45.01155 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c3e2ec71-032d-332f-b466-a5f867c88b6d | -12.29663 | -47.21893 | 2025-09-27 05:59:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6269ae7e-1945-3ab7-9d11-1d05c5357926 | -11.34904 | -45.01157 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8809cd60-3189-3afa-8dc7-4637f214598e | -8.8267 | -46.21251 | 2025-09-27 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d92bb7c4-c0cb-3799-a8c8-8de59aa568c2 | -7.87553 | -44.01315 | 2025-09-27 05:59:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9d49bb5b-b842-3b7c-b965-7e86346b9abb | -11.23732 | -45.56114 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 538e1b78-6606-3a7c-809a-d90f918fe508 | -10.28399 | -45.20926 | 2025-09-27 05:59:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 29b9b1ee-c911-34a9-a316-2ea13796e8b4 | -11.37772 | -44.94767 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9bb8ff73-d6d8-3cc3-9f2a-5e321b4d9245 | -10.25536 | -50.24054 | 2025-09-27 05:59:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c1528015-878e-379a-95a3-1ba2b4496157 | -11.43431 | -44.98507 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7debe7eb-60f0-37fe-85cd-5ed525b401a1 | -10.39822 | -46.13086 | 2025-09-27 05:59:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 02cf194e-f2d4-37a2-9068-e46569ee8f92 | -11.97524 | -47.89447 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 91e7b8ba-72f5-377a-93ae-de5f9d4d4e61 | -11.35571 | -45.03481 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| c6d678fd-7c3a-320a-9550-fd6eb442019f | -7.8739 | -44.02442 | 2025-09-27 05:59:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 38f6f130-f139-3e08-bd21-2c4a4a552759 | -11.98403 | -47.89581 | 2025-09-27 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 32472633-4663-3961-b885-373a0e9c60d0 | -11.3793 | -44.93628 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6c95bd68-e0ba-3ff1-a7cc-cfa92fb5bfdd | -13.61347 | -47.31223 | 2025-09-27 05:59:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b58a76a8-5a96-3891-af69-131ec49286f8 | -11.35874 | -45.01296 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 6719fac2-6032-3e77-9620-e4488f2a6559 | -11.43304 | -44.97795 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 41798c29-41da-31de-88f5-b271cd50effc | -9.89301 | -49.12454 | 2025-09-27 05:59:00 | AQUA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3cecf2bc-f931-3235-83b7-064d2d5ed280 | -8.81995 | -46.25814 | 2025-09-27 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3731e1dc-e3d6-39ce-90de-fad5f2800ae4 | -11.60589 | -45.42734 | 2025-09-27 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 25119b9a-a010-34e7-9e05-201f626af572 | -11.98943 | -46.60984 | 2025-09-27 05:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2baa5dd8-bfab-37b0-9ea0-6fb83fb9b092 | -7.71276 | -47.30425 | 2025-09-27 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8aaeafe7-70c9-3f8c-bf35-9a976f80e0ed | -9.61468 | -47.55765 | 2025-09-27 05:59:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e5c9e3d2-3c95-391b-bc7b-488ff1e201c1 | -7.80975 | -46.9586 | 2025-09-27 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbf1df28-36dd-3be8-a17a-8cea5cceb6e4 | -11.35723 | -45.02391 | 2025-09-27 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d9f008fd-414e-3f62-9535-d93e9709bfb0 | -20.8787 | -56.6091 | 2025-09-27 06:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 759a041d-b8d7-33fa-bbd9-b5a4e9664bc1 | -20.899 | -56.606 | 2025-09-27 06:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 9d63565a-328e-3e72-aea9-a1895be44449 | -22.58338 | -48.59361 | 2025-09-27 06:01:00 | AQUA_M-M | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 2585e396-70c2-3ef3-8e99-a6e49183c2da | -20.88708 | -56.58908 | 2025-09-27 06:01:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a1d08b75-bc9f-39b7-80a6-ae85f8f94ed3 | -23.02501 | -46.72186 | 2025-09-27 06:01:00 | AQUA_M-M | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 60fc00d8-3cd5-3c94-91da-faacaa3c5bc1 | -20.99606 | -50.01083 | 2025-09-27 06:01:00 | AQUA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ec0fa31b-c3fa-34fc-9801-53426a932316 | -20.88339 | -56.60851 | 2025-09-27 06:01:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 12ea29f9-0502-3760-8129-3143bebc8fb3 | -22.58481 | -48.58329 | 2025-09-27 06:01:00 | AQUA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 363.7 |
| 592999ed-e1fe-3837-a726-905e501cbdc2 | -22.59541 | -48.5745 | 2025-09-27 06:01:00 | AQUA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 503e3e71-098d-399a-bf75-8c7685f0c2cf | -19.04726 | -48.13036 | 2025-09-27 06:01:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6ce0ec8b-0d46-36e8-bd78-3df81b710aac | -22.58624 | -48.57299 | 2025-09-27 06:01:00 | AQUA_M-M | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 139c0f59-75f5-3102-b629-c7bccf257b8d | -23.02669 | -46.70863 | 2025-09-27 06:01:00 | AQUA_M-M | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 43a1c4ac-4e9f-32bf-a89d-54340344c1f5 | -16.75691 | -53.34924 | 2025-09-27 06:01:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 11b365d1-5bed-30a6-9867-cd6b4fa6835d | -9.98246 | -64.98627 | 2025-09-27 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e5430ad-cb8d-3431-a137-4463c2ed28f8 | -8.88413 | -66.68404 | 2025-09-27 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43757a52-b169-3f1a-b6eb-e27b4cd9d719 | -15.83359 | -59.61433 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ec2bfca-0de0-34e7-852d-19f57d11fc99 | -11.00778 | -68.43073 | 2025-09-27 06:05:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 337d39d7-5202-3a69-8382-12ffeafc7344 | -10.55738 | -68.17278 | 2025-09-27 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 623ed33f-c5f2-3e0e-b7a8-f0031ef63ea3 | -15.92651 | -59.48797 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| febde7c1-3a2e-3836-8482-d47e110ebd4e | -10.14704 | -66.96581 | 2025-09-27 06:05:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1323f4a0-e938-3d86-9356-f5e91af9fb13 | -10.4365 | -67.6869 | 2025-09-27 06:05:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84ad898f-decb-3a11-a2ed-7d2282b48be2 | -15.82279 | -59.61377 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64a8bda5-b233-32ca-addd-52bc19111953 | -15.93314 | -59.48891 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c26082-dccd-3f0a-aa24-95201752ad84 | -12.17423 | -64.10482 | 2025-09-27 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5baab8a-bbfb-3fb2-99d2-3f64ec1333e1 | -11.79134 | -62.73967 | 2025-09-27 06:05:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3783b07-61a5-3c1a-a6c3-7678e8e94548 | -15.81985 | -59.61847 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 485e102a-ca95-3985-8032-1278af233845 | -11.71941 | -62.58826 | 2025-09-27 06:05:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda92f9d-8ce6-35c9-a491-ebf0fdeaa16e | -11.79648 | -62.74031 | 2025-09-27 06:05:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c27859d0-4a65-3370-9e3b-d7f1b669730f | -9.82049 | -67.60247 | 2025-09-27 06:05:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 641fe504-31ab-383f-847c-bb1101467331 | -15.81562 | -59.61866 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cb57d10-6330-3fc9-8013-e9ac6011c62d | -11.72459 | -62.58897 | 2025-09-27 06:05:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57456fd5-e281-3ed2-943a-6a0d4ee059b9 | -15.82938 | -59.61447 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98de8cfd-7d46-33ad-b63c-32f5b7cc455f | -10.28125 | -67.23084 | 2025-09-27 06:05:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2a8f186-8b61-3ff0-8353-124410afaf68 | -10.56096 | -68.17332 | 2025-09-27 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a1459f4-52f2-32ac-9223-bf7bf7b4f9a5 | -15.82644 | -59.61921 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30a597dc-87f1-3bda-a8c3-f458c6db9f1a | -15.82699 | -59.6136 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3703841d-a441-3bad-9caa-33fd0efa05df | -10.25409 | -64.31108 | 2025-09-27 06:05:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b6519c-f10e-31bc-8b2c-077834ba63a1 | -15.82221 | -59.61936 | 2025-09-27 06:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e6a7913-78b0-324f-8321-4e4b5119fdbb | -20.8787 | -56.6091 | 2025-09-27 06:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 52.1 |
| c068e2b3-9ef6-3139-a1af-ebdeb2dd9440 | -10.55688 | -68.1726 | 2025-09-27 06:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7ccb9ce-b440-39f3-9179-905dd3ccec8f | -10.55645 | -68.17592 | 2025-09-27 06:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 16d6cddb-a151-340a-9295-27593fd4aec1 | -9.81705 | -67.6026 | 2025-09-27 06:25:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 518083c1-f850-38ee-ad5d-4c13152fcfea | -11.9843 | -47.9088 | 2025-09-27 08:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2459bf61-c597-3074-bd32-ff3785761d55 | -11.3642 | -45.0339 | 2025-09-27 08:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 32312d6f-6e82-3da2-b55c-93f8a313ec23 | -11.3646 | -45.0108 | 2025-09-27 08:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 3dd53a40-f58f-3428-a20c-77f067f762ce | -11.3642 | -45.0339 | 2025-09-27 09:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 823972e3-b355-3b60-be7a-6e093d45c128 | -11.9843 | -47.9088 | 2025-09-27 09:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| bc36115b-b548-306e-884c-2006b343d12b | -11.9843 | -47.9088 | 2025-09-27 09:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| ed79b216-03b1-3abd-b810-4f3b3a051899 | -11.9843 | -47.9088 | 2025-09-27 09:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| c66c0fc2-a769-3afc-be3c-41cde4f9b948 | -11.9843 | -47.9088 | 2025-09-27 09:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 5b383b0c-bd12-38d2-b5cd-fda81fce2297 | -11.9843 | -47.9088 | 2025-09-27 09:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| bb948370-8afc-3952-bc40-b1a258ee45d4 | -11.9843 | -47.9088 | 2025-09-27 10:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 05747673-19e4-30c2-9061-2eb0bf4b56c5 | -11.9843 | -47.9088 | 2025-09-27 10:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 4ba0c0ca-dfe2-3b2f-89c6-ef4a6114ed0f | -11.9843 | -47.9088 | 2025-09-27 10:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 602ff579-4c57-3a03-b93b-264cff81608a | -11.3642 | -45.0339 | 2025-09-27 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e1c6fd12-5694-3574-809d-0efcac913a46 | -11.9843 | -47.9088 | 2025-09-27 10:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 1cc73ff9-71e4-3c9c-bb46-b383a7569be8 | -11.9843 | -47.9088 | 2025-09-27 10:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| ada6cb35-02e1-3310-98dd-04b5aff85987 | -15.5776 | -51.7007 | 2025-09-27 10:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e6e1fe95-6f3e-36fa-951e-affca6692e44 | -15.5772 | -51.7223 | 2025-09-27 10:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| fefe677e-0c14-3611-aa6e-627e9965614d | -11.3642 | -45.0339 | 2025-09-27 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| e1261f6a-9ef4-310f-a460-ec16032a14e7 | -11.9843 | -47.9088 | 2025-09-27 11:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1a59c69a-9c8e-3080-a553-ffa94f00082a | -12.2829 | -44.0568 | 2025-09-27 11:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d214e68b-aae2-3a8e-8243-47ac0035b56f | -11.9843 | -47.9088 | 2025-09-27 11:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ab94021b-7039-3d91-bce9-19c05f7f1c1b | -10.0062 | -46.7081 | 2025-09-27 11:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 2fa0a04e-9932-33b8-9adf-ec063b308498 | -10.0062 | -46.7081 | 2025-09-27 11:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b657a0d5-be05-3599-9c0f-4c967f41d629 | -11.9843 | -47.9088 | 2025-09-27 11:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 7445d733-ea85-36ef-80ae-f1e05444aa95 | -8.822 | -46.2564 | 2025-09-27 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |


[Clique aqui para ver as próximas entradas](README60.md)
