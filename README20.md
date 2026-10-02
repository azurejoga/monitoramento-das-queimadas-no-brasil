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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6fda434-681d-3f3c-8019-4ad7906d5fc6 | -11.7541 | -43.5749 | 2026-10-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| ab970ac3-fac4-3d8f-9fec-16d8747ea673 | -2.0394 | -56.8593 | 2026-10-02 02:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 57d4cf83-95be-356f-be9a-7b6ddd831de4 | -11.6959 | -43.6077 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 51e5aa5f-ca48-34c2-9963-5761e54ed991 | -11.3102 | -50.9187 | 2026-10-02 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 205c014c-bd7c-346b-ad02-00b3ca2aaeec | -11.6579 | -43.5899 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 369.9 |
| 64005fab-8ec6-3b09-b5a1-b540af432245 | -10.8005 | -53.7682 | 2026-10-02 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 2636a043-d79b-3961-80a9-ca962a668ea4 | -3.1299 | -53.7633 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d9f1f2cc-59eb-3b33-a268-a38acdf56057 | -5.7563 | -45.152 | 2026-10-02 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4380552d-79f2-30dd-a9b5-01e51a866717 | -3.2766 | -53.8602 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 61d82922-c099-3c54-a7be-06c4b0cb5033 | -12.9998 | -51.2763 | 2026-10-02 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1dd51523-afdd-33aa-a129-0943c3a949ed | -3.1838 | -54.104 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 09c47fce-cd27-33a2-8062-9c1169995328 | -3.1299 | -53.7431 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 6a646582-d9ce-34d0-94e1-e9f6cd064241 | -3.295 | -53.8597 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| f2b5425a-8920-3c35-818e-35460b0f59d2 | -10.7818 | -53.7493 | 2026-10-02 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 194.5 |
| a690da57-b444-38fc-bf6c-a689b94d402f | -3.1483 | -53.7426 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0c7a5309-9b3b-3ae5-832f-211c5b794960 | -13.3481 | -43.8538 | 2026-10-02 02:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 29c84fac-47af-3ba4-b17d-6ee9886963cb | -11.6771 | -43.587 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 371542ad-6c6c-3eb7-9350-9b284b2d900f | -11.1611 | -44.6234 | 2026-10-02 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| fc564962-b09f-395d-8736-1b7210480221 | -2.0577 | -56.8591 | 2026-10-02 02:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 35c3a0d2-442a-3f9c-b10a-cbeda9aa9ca4 | -3.1655 | -54.0844 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3ff8a414-ad5a-3e2f-ae3a-9b2ef040973b | -11.7926 | -43.5689 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 38dc2705-2586-35b6-9522-dc18961bd306 | -6.858 | -59.2636 | 2026-10-02 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e5fffb3b-dfe9-3cc3-acd2-8c482191d93e | -11.142 | -44.6261 | 2026-10-02 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 60394fd7-baea-33af-aa35-67fcb7800ae6 | -11.6767 | -43.6106 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 2d03921c-e73c-3678-8ee1-dd1e13bfe1b3 | -4.4693 | -47.9103 | 2026-10-02 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f10c7f14-0531-371d-9e87-ff9fafd2609a | -4.4691 | -47.932 | 2026-10-02 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 02d9c4b5-d12e-3ab1-8444-d2eb0c84e763 | -4.2676 | -50.7506 | 2026-10-02 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c04cc599-dcaf-3d1d-835b-962841d5cb2f | -12.9995 | -51.2976 | 2026-10-02 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 2c10059e-019b-3850-8a7f-7f77cd44f660 | -3.2767 | -53.84 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 947c1b5d-e28f-33b5-a72b-32e0612794d2 | -4.2953 | -49.1021 | 2026-10-02 02:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 156eee5f-cd0c-3a6b-ac98-c90da64b71b4 | -11.1424 | -44.6029 | 2026-10-02 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f6e0e57c-6a8b-3e11-aaf1-10c04a56e383 | -6.2091 | -60.0187 | 2026-10-02 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 98adc13b-9aba-305a-8577-9dfc5df73660 | -10.8007 | -53.7476 | 2026-10-02 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 12004b8b-ccd9-3b88-bd5f-500f8ef1af03 | -11.7541 | -43.5749 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 7bd8d316-1fef-3e17-a893-c23a85cec4ab | -3.1839 | -54.0839 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 49d69ea4-6196-385d-925a-18385acfa501 | -13.0187 | -51.2953 | 2026-10-02 02:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f5afbed1-0884-31ab-91a6-3567e119d493 | -11.4691 | -43.4299 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7c798bc3-7e1e-382f-af7c-b754068362b5 | -7.2704 | -55.5983 | 2026-10-02 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9ceb67d9-3684-3fba-aab8-45d9c32bcfab | -11.3099 | -50.94 | 2026-10-02 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b3f29d02-1de3-3e5e-94c3-c72d337793bd | -3.2951 | -53.8395 | 2026-10-02 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| ae268a02-cb49-3f23-b05c-b4dec3d6976c | -6.0626 | -59.8897 | 2026-10-02 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9f444405-95fd-3780-849e-b99ab2eb1f0e | -10.7816 | -53.7699 | 2026-10-02 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 194.4 |
| f28d04ab-c9d1-35db-a3cb-965083d103b6 | -4.4506 | -47.9329 | 2026-10-02 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 9f38d854-e7d8-3151-a0b7-503903afece2 | -6.2274 | -60.0372 | 2026-10-02 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8fd26db2-3c75-3c40-9f7e-d6dcffbd3dbc | -11.6575 | -43.6136 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.9 |
| dff190ac-e35f-38fc-bd83-54f93da75115 | -4.4507 | -47.9112 | 2026-10-02 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 5362cbd6-33ef-38de-905f-1ad4aed5d683 | -2.0576 | -56.8786 | 2026-10-02 02:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5777ac0f-a67f-3e24-ad10-776399adb6f5 | -11.7733 | -43.5719 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 25c5cf28-6ada-32f1-808e-52cd0c0e0465 | -6.209 | -60.0378 | 2026-10-02 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 54e1795c-c06e-3887-ac2b-8e6c0dd88be8 | -6.9317 | -59.2798 | 2026-10-02 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 639379c6-2ac2-38ae-9a06-33ac4e369c0c | -2.0393 | -56.8789 | 2026-10-02 02:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1f419f2f-fb6f-3015-976c-202c88a8ad61 | -2.0394 | -56.8593 | 2026-10-02 02:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 78e6bd6f-5da8-3f7b-aff5-f9b3f1a78826 | -11.6583 | -43.5662 | 2026-10-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f1364f7c-c742-32f9-9d2e-713166788a07 | -6.3952 | -56.4158 | 2026-10-02 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1c8325fd-8207-3df4-934e-323a58d1c575 | -11.1615 | -44.6002 | 2026-10-02 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3350cc66-7d20-3c77-8bf4-6ac5f1215121 | -7.7658 | -58.8946 | 2026-10-02 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| dcca5436-7c93-3465-a440-8ad173f6c8e1 | -5.7563 | -45.152 | 2026-10-02 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4dd0e7e2-dace-31ad-8505-9321db71d070 | -11.7348 | -43.578 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 165f708f-887b-3962-b0ae-8eff73759081 | -11.6771 | -43.587 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.6 |
| 671bf255-d0d8-3e44-b054-fa9b4c68a3fc | -10.7818 | -53.7493 | 2026-10-02 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 6f5428dc-75dd-3530-a204-8a62bd10f63a | -12.825 | -51.4466 | 2026-10-02 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6a59bea3-45ac-3da4-940a-0912d8a5d0a4 | -12.8449 | -51.4017 | 2026-10-02 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7ba5a81d-d1e6-3014-a7ff-14545ba93646 | -7.7657 | -58.914 | 2026-10-02 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0ac626da-b68d-3775-9b3d-4ca30c5cacaf | -11.6579 | -43.5899 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 419.4 |
| ef5988cb-75c0-3bde-a5d7-b6f3cfd1bc85 | -12.8442 | -51.4443 | 2026-10-02 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ff3125a9-5c42-3654-91f4-4fb3d456b207 | -9.1528 | -49.9425 | 2026-10-02 02:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 5af7c201-5698-3c8a-9745-3b617049bd20 | -11.1424 | -44.6029 | 2026-10-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| dfbbf655-8ec4-39f7-842b-5e5110ffede8 | -12.8445 | -51.423 | 2026-10-02 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 7083727a-9902-3106-a097-1af317908ffb | -6.2274 | -60.0372 | 2026-10-02 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7ee5abd2-0d7f-3c20-b8e6-c466f32721ec | -11.6575 | -43.6136 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 309.4 |
| 99464003-07ed-3afb-aff1-1da72a5e2cf0 | -3.1299 | -53.7431 | 2026-10-02 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| eaccd2e1-f9aa-36f4-9df2-1af5b4e6b242 | -11.1611 | -44.6234 | 2026-10-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d1b7fdfa-b73c-3bea-a093-aad6e8fa00c5 | -3.1838 | -54.104 | 2026-10-02 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 196eeea4-7b5d-3b09-93e9-c389950f3c9a | -11.6583 | -43.5662 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 0280694d-be3a-3b66-8106-757ae1530ff8 | -7.4188 | -55.5902 | 2026-10-02 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 48713354-b250-3071-94df-adf06da08d56 | -13.3481 | -43.8538 | 2026-10-02 02:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| a36ab9ee-4b18-35d9-9bd3-73713da1dc38 | -11.7926 | -43.5689 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4568ac08-22ff-3636-a877-553bfaf230eb | -11.7729 | -43.5956 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3b0ea421-a437-3df9-9bcc-97821d2f73a3 | -11.7733 | -43.5719 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| a410ae94-195d-31b8-a930-54b900da6463 | -9.1716 | -49.9408 | 2026-10-02 02:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c2e50c8f-d2e6-3b17-ba11-05b24e8bab9e | -3.1299 | -53.7633 | 2026-10-02 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2adb60ed-0097-3504-8415-ed1c46fa8715 | -11.142 | -44.6261 | 2026-10-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a4448c48-fbdd-34d7-9fd1-593df64f4c3c | -11.6767 | -43.6106 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 271.1 |
| ea9f1b66-64ea-3289-80d9-822e959a0b3c | -12.8247 | -51.4679 | 2026-10-02 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 812456eb-8685-34a6-b171-5c1dec30b911 | -7.2704 | -55.5983 | 2026-10-02 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| dda3b7ad-9139-3d5b-b2b1-ee762137b72d | -2.0576 | -56.8786 | 2026-10-02 02:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8d6efdad-6b35-3701-a617-b1cbc90c7532 | -4.4507 | -47.9112 | 2026-10-02 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f818582b-c017-3916-96a9-fb28db8c0199 | -4.4691 | -47.932 | 2026-10-02 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 25c1c65e-c09f-3e36-ae09-d1d956346c01 | -7.7551 | -49.2067 | 2026-10-02 02:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 42.8 |
| da654f63-15b0-30e2-9403-efc9cff4610c | -12.8254 | -51.4253 | 2026-10-02 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 62233fc8-22e5-30d1-ab19-d14b94f064f7 | -3.1839 | -54.0839 | 2026-10-02 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| dc0044f5-0547-3076-92f1-eac9c1c38363 | -10.7816 | -53.7699 | 2026-10-02 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 730f63c7-7b19-368b-adf0-873a8a46d26e | -4.2676 | -50.7506 | 2026-10-02 02:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e4b27525-6b63-382d-a73c-611f48fc7fcf | -11.7541 | -43.5749 | 2026-10-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 6719f23b-6112-3c2b-88a8-44c39c3b278c | -4.4506 | -47.9329 | 2026-10-02 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c583d647-71a8-3339-a052-b6d6afea038d | -13.3476 | -43.8776 | 2026-10-02 02:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 454222c8-eef4-3e12-a740-d19ceb1730ed | -3.1655 | -54.0844 | 2026-10-02 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2df4ef05-ab68-3603-a955-6c2eb669a305 | -2.0577 | -56.8591 | 2026-10-02 02:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ebde7f91-e966-3d62-822b-2df214bcefb0 | -4.4693 | -47.9103 | 2026-10-02 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 852e47fe-1ae7-38da-98e9-03a60486f383 | -2.0393 | -56.8789 | 2026-10-02 02:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |


[Clique aqui para ver as próximas entradas](README21.md)
