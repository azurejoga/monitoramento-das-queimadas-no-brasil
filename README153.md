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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42543fd8-25a2-3d14-84c7-e937df6786a4 | -11.8225 | -45.0827 | 2025-10-05 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 1ec086b6-b7c5-3baa-882f-440efc429fc4 | -17.986 | -51.144 | 2025-10-05 12:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5ad149d7-fb73-3e47-9105-62a8265790fc | -13.7473 | -51.3097 | 2025-10-05 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 312.4 |
| e5fecc1e-96de-38dc-bff0-89cf3f243c82 | -10.9303 | -47.0882 | 2025-10-05 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 025d0481-403f-314b-bc67-1abca89c61b7 | -10.4054 | -45.3931 | 2025-10-05 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 184dbb37-15c9-3cb7-85d9-b2069c33d8ba | -9.9556 | -43.7632 | 2025-10-05 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 3cb6194f-4715-3551-998f-9d57658d5acf | -10.9497 | -47.0634 | 2025-10-05 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 3d63d5be-d663-3c05-bbb6-63dd88768271 | -8.1888 | -44.1588 | 2025-10-05 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| e751ff0f-a310-3bc7-a1ac-a7f2e6ac0184 | -13.728 | -51.3122 | 2025-10-05 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| dbeed746-ad37-3e02-bee4-4691fed02447 | -10.0504 | -50.4113 | 2025-10-05 12:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 79f1af43-a911-3df1-b2f0-a5c049cc198a | -11.9327 | -46.438 | 2025-10-05 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 14560b77-7505-3b42-8a06-f763a0c4e342 | -13.7476 | -51.2883 | 2025-10-05 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 8e68071e-bcb2-38e0-a8b5-c8f3cbc7dc8a | -10.93 | -47.1106 | 2025-10-05 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0410141d-6e6b-3267-ab97-aface6f17c46 | -8.1891 | -44.1357 | 2025-10-05 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 6e874287-fdf7-3870-b59c-497bd220d105 | -8.5393 | -46.2631 | 2025-10-05 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 20da8c76-400d-3a53-ae08-66b63a5a8ed8 | -7.7118 | -46.2754 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 235.2 |
| a1941e94-1ccf-3e3c-a4db-7044a487d81a | -8.5578 | -46.2836 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 34c23727-d9f4-3899-8e78-151b413f1f17 | -7.7743 | -42.6103 | 2025-10-05 12:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 1a222f0b-8125-3471-80e4-7d78bbaea9aa | -11.823 | -45.0596 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 81b42d52-bd12-322a-9632-6b6d1b026d88 | -11.0313 | -46.7171 | 2025-10-05 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 0f14583d-6803-3f81-abd6-ad06490b8540 | -7.7935 | -42.5845 | 2025-10-05 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 9d9c32f4-eb1d-3417-9a7b-6e526236a4e2 | -10.8093 | -48.8229 | 2025-10-05 12:50:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 05e74fa8-b47a-3dfb-8b83-c07de538dd79 | -17.9408 | -57.5928 | 2025-10-05 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| d033967d-f37c-3c6c-b958-1964f254b6d2 | -8.5407 | -47.6831 | 2025-10-05 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| fae13647-21b7-3947-9424-a06c103bef44 | -13.7284 | -51.2908 | 2025-10-05 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 4eaf4c0a-a045-3595-af44-6a3f1f0d63c4 | -11.1168 | -49.8492 | 2025-10-05 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| bee1245a-41a5-3c2e-9aa4-1a2a16af1ef6 | -11.8234 | -45.0364 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 1c831873-39b3-3915-8cac-d7550eb8ca80 | -10.6568 | -46.3372 | 2025-10-05 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 9fb92707-33ec-38de-a247-54b2b4bf0aa5 | -12.5487 | -54.7307 | 2025-10-05 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| fa41cb33-61da-3e45-98b0-07f18241bea0 | -15.6015 | -52.5102 | 2025-10-05 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b29215e4-53da-3aa5-9409-ba03b3674460 | -13.728 | -51.3122 | 2025-10-05 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 266.9 |
| c18a57a7-67cb-31f8-8467-ff84da7240a5 | -11.8225 | -45.0827 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 9412b9cb-365e-38fa-9568-1f44d695b293 | -11.8038 | -45.0624 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| e47ddea5-bc7d-3a8b-b5eb-26df7ff680d2 | -11.8635 | -44.938 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b771f3e8-403b-360d-be4a-74d5b3ba1e7a | -7.712 | -46.2531 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 553.5 |
| e0b97674-6e7e-3452-9f22-956cd6666722 | -8.1888 | -44.1588 | 2025-10-05 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 955e3ea8-95fd-35fd-8a61-6d5e4c273d79 | -11.0911 | -47.7573 | 2025-10-05 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0398ab24-0e0d-30dc-b65f-fb0e6fce8b1c | -9.3941 | -45.8336 | 2025-10-05 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3d1e6635-2680-3d1e-b81d-9251b599372c | -12.2688 | -49.1907 | 2025-10-05 12:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 0516b99f-62e8-38d3-822e-df0c04a5d5f1 | -11.0978 | -49.8513 | 2025-10-05 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 22dca86c-c942-3e4b-82a0-d1c69bed9cc5 | -10.0504 | -50.4113 | 2025-10-05 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 8c5bcf20-f45a-3d56-83ae-e7083d54e058 | -8.4683 | -45.9106 | 2025-10-05 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| e6497602-4a4c-36bb-b4c5-6e268bf85f49 | -7.7123 | -46.2307 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 79d7b26d-5cc3-3556-b52c-93550efc29a2 | -7.7932 | -42.6082 | 2025-10-05 12:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 88172fae-33b1-368b-8e4d-aba7944e2231 | -11.0316 | -46.6946 | 2025-10-05 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 353893b8-2fd7-363c-a072-a76e3be9ed77 | -16.0966 | -51.0829 | 2025-10-05 12:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 21542db8-dc5a-3626-866d-418e07b98f05 | -7.8127 | -42.5587 | 2025-10-05 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| af665863-1b75-3cec-9a2b-251fd0c5f2a8 | -7.7308 | -46.2513 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 191.8 |
| eb9ec347-4218-3b44-acd7-71862e14fb37 | -8.1891 | -44.1357 | 2025-10-05 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| d585a2ee-e06a-3cb3-954a-9b89862d1fbb | -13.7473 | -51.3097 | 2025-10-05 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 270.9 |
| ee699338-ae93-3532-96e8-d829fee5d48c | -17.9612 | -57.5492 | 2025-10-05 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 2066d3fa-cbdd-3932-bd60-c866fb373992 | -17.9661 | -51.1474 | 2025-10-05 12:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ef6d7cf7-dfd6-36e7-9023-360d15a23634 | -11.8422 | -45.0567 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2c43c632-0de3-3284-b05f-9c3b7c9dcd49 | -15.582 | -52.5129 | 2025-10-05 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| bf5c19cf-d07e-3b76-bfea-64b8163827c9 | -12.5863 | -54.7679 | 2025-10-05 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| e0206bc6-8772-350b-b7b3-9716d8b724e1 | -16.077 | -51.0859 | 2025-10-05 12:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| bbca553d-703f-3635-b479-fab984dd5623 | -7.6993 | -42.5708 | 2025-10-05 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| c9f54312-bf7d-31dc-9d77-a8a40b8e9e9b | -8.4872 | -45.9087 | 2025-10-05 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0b43ecd0-70ea-3a2b-a63a-03f8d0b3a059 | -17.9605 | -57.5904 | 2025-10-05 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 42d7cb37-6ebd-3821-959a-cad0e3d8a3f8 | -7.7885 | -44.5228 | 2025-10-05 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 36c61655-5377-3088-bce5-36533cc62855 | -8.9188 | -46.0664 | 2025-10-05 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7321e87d-23c4-3731-a290-2310d444df9f | -19.0155 | -50.6045 | 2025-10-05 12:50:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 179.7 |
| e6e2b9b9-54f9-3887-9de3-ddf912decdb5 | -8.539 | -46.2855 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a3ba4962-6477-3bed-bbdb-6d5071ac8b52 | -17.986 | -51.144 | 2025-10-05 12:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e73cc18f-4b99-3b65-80a6-67c4569d3e03 | -7.7938 | -42.5607 | 2025-10-05 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 5cc1994b-a91e-382f-a6c4-38f068118542 | -10.6378 | -46.3396 | 2025-10-05 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 48811f4c-f133-3f83-9988-e2a6528ea562 | -8.5581 | -46.2611 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 7d2b5882-6827-3ab6-bd54-365f4d3fc199 | -18.1968 | -53.3638 | 2025-10-05 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c8dbddfa-bc58-354a-8ac0-c25c71b16c4f | -12.6913 | -45.8482 | 2025-10-05 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8fcb6fbc-88b0-3723-ab78-478509eb4572 | -8.595 | -46.3246 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f9785879-ec7a-3b52-afc7-e8f9631523d6 | -8.5393 | -46.2631 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 877409a5-0f9b-33bd-b6de-8e21b8bed51a | -11.8418 | -45.0799 | 2025-10-05 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e45df87c-cdb7-3f00-b7a3-474b3a8bbd8f | -8.5953 | -46.3022 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6975b624-27e6-3c41-881d-f1f5a6e21317 | -9.2973 | -46.0026 | 2025-10-05 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f2bf5ec0-9df6-3e06-8da9-f8d9a80991c3 | -12.5485 | -54.7512 | 2025-10-05 12:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 547262be-df80-3f9e-9026-095884b196a9 | -15.5824 | -52.4916 | 2025-10-05 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 01031b0c-709a-3a1c-8ea5-2647555475e4 | -12.7106 | -45.8452 | 2025-10-05 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.9 |
| dbfeff10-bce3-3ac0-8d61-2c4b5330b564 | -7.7306 | -46.2737 | 2025-10-05 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fbc614c2-9543-307f-a766-a55ef0aa7a26 | -8.468 | -45.9332 | 2025-10-05 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 282.6 |
| 28c2a5d0-c7cf-3350-89f3-a5b6ce55fa93 | -1.15642 | -48.99742 | 2025-10-05 12:55:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9138354b-e361-3d04-83aa-907c8260e749 | -2.68977 | -48.39918 | 2025-10-05 12:55:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 1286217d-584a-311b-9c08-ff8a80561344 | -1.38916 | -49.38614 | 2025-10-05 12:55:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e60c5bab-6752-310f-9531-431c32a9f8e9 | -2.33564 | -56.0161 | 2025-10-05 12:55:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1d9e534-9a4c-3dd4-99a7-a5d08ad6ba57 | -9.64432 | -54.315 | 2025-10-05 12:57:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8bf36165-2a7b-3eb5-a829-444fee4abad1 | -10.41229 | -50.37645 | 2025-10-05 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.8 |
| ff636cf3-1faf-38b6-becf-f472c84a34a3 | -7.00531 | -47.46685 | 2025-10-05 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| a75e2f52-ddc8-39d0-bac5-2ed834d97ad6 | -9.83907 | -59.47168 | 2025-10-05 12:57:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bd5cacdd-1461-3602-b291-3a74557c1431 | -9.25493 | -51.80565 | 2025-10-05 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 15505933-dfdf-37f9-97b2-589d686f7248 | -9.45587 | -56.64943 | 2025-10-05 12:57:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6c74ef53-0ec6-3170-aa75-6d743534bc02 | -6.99471 | -47.4963 | 2025-10-05 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 0cb3f1f7-83ff-3ee4-add5-22c3a655837c | -10.4682 | -57.5007 | 2025-10-05 12:57:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 16e9eaf0-0409-3a76-90ad-30f75b159900 | -9.6209 | -51.80445 | 2025-10-05 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 33688f6f-b75d-304f-a65b-664adc976380 | -10.44009 | -50.43451 | 2025-10-05 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 986cb754-bdab-3d6c-a157-990f4375c561 | -9.41401 | -60.5077 | 2025-10-05 12:57:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c2ffe796-ac4b-3016-b205-408396345171 | -10.46948 | -57.49175 | 2025-10-05 12:57:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| af346eae-a4a1-3624-948c-a917090245b6 | -10.38523 | -58.71341 | 2025-10-05 12:57:00 | TERRA_M-T | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4f2f8b43-648a-366e-802a-d979ba4b1adf | -10.80921 | -48.82507 | 2025-10-05 12:57:00 | TERRA_M-T | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 02bc053c-93c2-3e2a-8e0e-ad211d018129 | -11.0918 | -47.7565 | 2025-10-05 12:57:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 63bf19e7-ccf0-37b4-a769-f00b3492bf4f | -9.25277 | -51.82285 | 2025-10-05 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4c733539-ebaf-3e15-aaa2-a3ee342ee3c5 | -11.11246 | -49.86227 | 2025-10-05 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |


[Clique aqui para ver as próximas entradas](README154.md)
