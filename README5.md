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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6eecc1a-bdc7-3ab4-82fc-baeb79b33a70 | -4.96482 | -44.42901 | 2025-09-07 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e35f703-69ea-3ea5-94c5-b263d12fa866 | -5.95607 | -43.80694 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3820906f-1066-331b-a650-d64a896a2e29 | -5.95731 | -45.75991 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f7b8a8b8-6d86-34d6-91e3-0a4221169faf | -8.67777 | -47.44981 | 2025-09-07 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 03ccabae-e76d-398f-9991-366739043e05 | -6.15699 | -44.25609 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 635cdc09-d04e-3e78-9ea7-0d7c01241831 | -6.21124 | -42.45695 | 2025-09-07 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dae6cab7-3802-324e-8cab-fafee5f9b412 | -5.98731 | -44.16439 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| abbdc09a-53d3-31b4-8d8f-5ae9aef20e4c | -5.70083 | -49.19944 | 2025-09-07 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6988c516-f112-34a4-9a98-fe44efc7c07c | -6.72897 | -50.45771 | 2025-09-07 00:11:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| be00173f-7a4e-3d2d-9fe7-c2ba68f22ad7 | -6.34179 | -43.80019 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 21fe3448-c73d-3dd0-9216-fdd5b8171d2e | -5.63789 | -44.97641 | 2025-09-07 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bc29cd36-d5a2-3ac6-b279-72a187fad45f | -8.01906 | -45.49554 | 2025-09-07 00:11:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 99981a97-030a-3036-bebf-4f86ff9001f1 | -5.84439 | -46.10863 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3accd4f1-a165-3d2f-a508-68f171845961 | -6.22818 | -43.30386 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| edcddd59-5ea7-3f39-ae04-f58a7a0b3227 | -7.92961 | -49.32077 | 2025-09-07 00:11:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 86c7e92d-c9ae-3105-88a2-bd63ea07fe5f | -5.88154 | -45.07743 | 2025-09-07 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 234fbd6d-3e6e-3334-a5dd-94cb5dc6c569 | -9.77522 | -46.88801 | 2025-09-07 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c03c88f2-de29-31b0-97d9-ca3dd84883b2 | -4.26571 | -48.1884 | 2025-09-07 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 16aaf29a-7c15-3e3f-8ea8-4ed16b3d3cb3 | -6.18904 | -45.43517 | 2025-09-07 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d2c20219-5857-3864-bcd5-fba713187776 | -5.97342 | -44.7352 | 2025-09-07 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79a1d9b0-9ade-30a4-adf5-41e261cf6456 | -6.22574 | -43.28623 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 455f03cf-aa1b-3906-accc-09dccea1c58f | -5.97844 | -44.16563 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 982d16ff-7d66-3829-b0ac-80d618048ccd | -6.20436 | -43.53757 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee730326-653c-3c5a-a87d-118b9623bfbd | -6.21032 | -43.36926 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc2f3ec6-0c33-3cb8-a664-c7045ccef2f7 | -2.89933 | -40.24744 | 2025-09-07 00:11:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 33.4 |
| c43be7db-1f72-35c9-a860-56e8ad8c7ae7 | -6.2073 | -42.62268 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 57b9c5a8-6cf0-3e28-b705-17c8060b1fa6 | -8.94839 | -44.26249 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 826b763b-f06e-32f6-8e2c-39d839545d5c | -7.8432 | -44.94203 | 2025-09-07 00:11:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8518a058-00ea-33e7-adec-ba17a51d6998 | -6.21176 | -44.19336 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc59a047-d0e1-3623-9665-81857550efbd | -5.95728 | -43.81577 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c08b347e-f9c2-38e8-a879-bfac6fae88d1 | -11.87473 | -50.73096 | 2025-09-07 00:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 2615d908-e35e-3258-b728-aa15f04e8c69 | -6.51193 | -44.09055 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 404b4f2f-90f8-386c-9d7d-479dbe0f27fa | -6.10664 | -44.76736 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 048aa216-d40f-3b3e-adbc-80985bf9a1ff | -9.59433 | -43.3292 | 2025-09-07 00:11:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| cccf513b-e9f8-3394-8d09-a262419f5b78 | -6.13921 | -44.25858 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 70485ca5-836e-396e-acbb-a35a2ecdebf4 | -5.47051 | -44.16454 | 2025-09-07 00:11:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 98b1dbee-a682-360a-85e2-0c3274856a5a | -5.74983 | -43.71334 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c4f692d-aa04-3ef6-a30f-b2884e214119 | -4.16783 | -42.02707 | 2025-09-07 00:11:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 07d5b863-692e-3747-bcbf-9cb8351d06e9 | -6.30284 | -44.04111 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50de37de-ce4f-3f46-92af-c2346c562521 | -10.60623 | -44.34108 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 8e0fe168-593e-3258-997e-3c25e801b298 | -11.85169 | -50.52494 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b0080160-1326-3932-a937-a8d2e702945e | -6.21869 | -42.63932 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| de3e78c4-4f9e-3618-acdd-be6e8c30ae3d | -6.01753 | -45.88102 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 08dbe4c3-101a-31e9-bc7c-248fdee3af9a | -6.21041 | -53.29637 | 2025-09-07 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a5a63a5a-e717-33d2-9bf6-b166a06c4330 | -7.23526 | -43.85815 | 2025-09-07 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 600baf13-7954-3963-8371-6b7bf5eba666 | -8.33646 | -48.27717 | 2025-09-07 00:11:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 59a7c2ca-4722-3907-82ef-63cbe591bb6a | -10.15699 | -48.75132 | 2025-09-07 00:11:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 332b9444-4df6-3ae2-b875-299e36102a0e | -6.48839 | -43.9846 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 66441ef8-cfec-3016-97e8-8d42bc0f622e | -8.34816 | -48.27555 | 2025-09-07 00:11:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| c6bcac57-259e-3e4f-8d8a-303755fe7a73 | -6.23016 | -42.59196 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| fff386c9-3725-3b69-befa-e53a11f929a3 | -5.03112 | -45.32352 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 229bd7ad-15ad-3079-9cad-c0e470a1df0c | -6.16435 | -43.18404 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 761b6636-b5f5-3bdb-9efc-199b64d3ed7a | -6.17999 | -41.8446 | 2025-09-07 00:11:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9416c437-d5c6-3415-a765-f45639fe9832 | -5.71478 | -43.93102 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b7ae7768-f160-36f0-8d18-f20e2c4c98f2 | -6.85132 | -45.92509 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 074ed807-23fa-33c5-8d91-5a1a496955c9 | -5.04013 | -45.4586 | 2025-09-07 00:11:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5298c4ea-e91a-3840-ae50-bd8355b65293 | -5.99495 | -44.15422 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 7d2bfe79-aafe-3559-aef8-ff894f346171 | -5.99741 | -44.1721 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e8e6afb-3c42-3163-b54c-1853da0592b0 | -5.21289 | -43.70014 | 2025-09-07 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 580a983d-3e3b-3a0b-9f39-fa664f920110 | -6.91964 | -45.19925 | 2025-09-07 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 673c9147-6fe0-3182-a3aa-ed28a757fd42 | -6.92094 | -45.20899 | 2025-09-07 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25aa067d-3bed-3dc7-a5dc-d3708279e28b | -7.01622 | -44.95416 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 58784be5-36e7-30c6-8109-82163954ebae | -10.38382 | -44.96566 | 2025-09-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 237.1 |
| a3a4fac6-6097-3147-8bd6-df5c2be8227e | -11.60847 | -47.1538 | 2025-09-07 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 759b898c-0438-3cb9-a117-117c85fc9266 | -6.24213 | -43.27493 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 26a4050d-a991-301a-bbe4-f595302982e9 | -7.40324 | -44.95438 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb73d90b-7f49-378b-8716-4da8d4b39382 | -7.84189 | -44.93227 | 2025-09-07 00:11:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6ab7ee78-6dfb-35a7-ac6a-8c761ed21f60 | -6.48716 | -43.97564 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dcbc2c54-abf1-398e-bbb7-2b05778cd134 | -4.26382 | -48.17471 | 2025-09-07 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bce4f94e-4e3d-3a5c-93c7-5e0323b2c06c | -7.01882 | -44.97337 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f413a130-958b-3d3f-98b1-888c0091674a | -2.92064 | -48.67698 | 2025-09-07 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 405163cb-2e04-3dfc-b587-46623dd7ecc6 | -3.23759 | -50.81349 | 2025-09-07 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 91a2b7bd-7c19-3596-9bb9-7e5296bf5c84 | -3.59033 | -47.51863 | 2025-09-07 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 8d894fcf-0eef-359c-b1dd-bcd41a3a4358 | -2.43289 | -49.31246 | 2025-09-07 00:13:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 15fee50d-7b1c-39ee-ac5a-984d2669b50a | -3.41533 | -50.29475 | 2025-09-07 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4ebc5a9b-446e-3717-b11e-7fea3a29678b | -2.43078 | -49.29682 | 2025-09-07 00:13:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e7926440-ce50-3daf-aacd-136fa3c86122 | -3.24726 | -50.80569 | 2025-09-07 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 10845acf-3f5b-3a2b-b3bb-cd421f2f933d | -3.59891 | -47.5052 | 2025-09-07 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b93417fa-643e-3c27-a7f7-712f306557c9 | -3.53519 | -49.05821 | 2025-09-07 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 453945ee-838b-39b4-8dba-685f90027aed | -3.60055 | -47.51722 | 2025-09-07 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 13684cf8-4e5b-3edd-b544-c220cb6db883 | -2.78675 | -49.62539 | 2025-09-07 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 7142bd5e-0134-3ead-804a-69538a57985c | -2.62902 | -46.83328 | 2025-09-07 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b2fac9e9-cce0-3328-a776-ef2eee82001d | -2.82052 | -49.20335 | 2025-09-07 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cea7edcd-cafd-3b7a-928a-9d93859e4fc7 | -3.53731 | -49.07381 | 2025-09-07 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| f6a2414a-1c1c-39d8-a771-9c41372213fe | -2.51886 | -47.60551 | 2025-09-07 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6bf24b32-cfa1-3044-a2f1-d0ec33cfe358 | -2.85052 | -49.50946 | 2025-09-07 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b51b6f39-41d5-3140-adc7-8c134206a2ad | -2.07563 | -47.13807 | 2025-09-07 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 239c4bc6-fbfc-3135-addf-846caac5396b | -3.42239 | -46.96214 | 2025-09-07 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ae2bb74d-24b2-3649-9695-a7fcb4ef18e1 | -3.5887 | -47.50659 | 2025-09-07 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 37015796-4f3f-3bf9-9855-1bea6cb125c6 | -3.25084 | -50.81178 | 2025-09-07 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 6b87f8bd-8206-3a75-85b0-cfe2eadc77d1 | -2.07715 | -47.14898 | 2025-09-07 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64b12eab-e825-3239-b17d-0b850102ecdc | -3.5995 | -47.5142 | 2025-09-07 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 732dc4c3-661d-33a5-9abd-cb3651aaf167 | -17.6986 | -43.5286 | 2025-09-07 00:20:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| bc418a86-af55-3542-ad00-19949e861852 | -11.4076 | -43.6519 | 2025-09-07 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 592863b8-6ed3-3ecf-96ed-a38505061ff6 | -9.4495 | -62.3675 | 2025-09-07 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a285dd24-3cbe-3619-afdf-b43aae4fa941 | -6.0086 | -44.1513 | 2025-09-07 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 08abf592-8af7-38c9-88d1-ce38aaba79c6 | -11.408 | -43.6283 | 2025-09-07 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 2e21bfc9-9656-3a26-bbd3-95604107211f | -11.4961 | -55.5613 | 2025-09-07 00:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 007aea5b-8a85-3783-bf96-aabcfbaa509a | -11.4085 | -43.6046 | 2025-09-07 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 56f5e6a5-982e-30a4-a639-4804f001165a | -5.9899 | -44.1528 | 2025-09-07 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 211.8 |


[Clique aqui para ver as próximas entradas](README6.md)
