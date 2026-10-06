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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df512079-a150-3ca1-9008-09bede4944ea | -3.17401 | -50.43917 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 399c1266-14dc-31f9-ad28-2ca214c77d67 | -3.27428 | -54.18361 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 058d4a2f-c622-3163-b22f-257e5a266b9e | -9.1382 | -47.98294 | 2026-10-06 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65f17941-51c3-3369-8a48-4095046a2bb3 | -11.28074 | -45.49861 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f7baa5e2-66f6-38ba-b00d-f0f4ca64fd74 | -3.09646 | -54.18073 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e87f5ff2-9984-32c9-89c1-39d47792ac30 | -7.69718 | -44.61996 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5cfd108-3e68-3a6a-ad39-306bbb3d4b36 | -6.4194 | -43.46966 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e79dbe29-a4c5-3d8a-888b-01fcb0de5c8a | -4.45453 | -47.91819 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 88dbd957-6fc9-3def-a071-e475085b1a2e | -8.6984 | -45.22384 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ebe16e1-7944-3e58-abc4-6e7c79d35f51 | -10.58173 | -44.05309 | 2026-10-06 04:19:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 980f6a8c-4f1d-385e-acb3-4481a90ea069 | -11.45818 | -43.38955 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eebc3b50-5433-327a-8d42-70f53bbf193c | -6.35894 | -42.54551 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc31c0ab-bf65-3347-8b9f-9de87e42f913 | -10.36895 | -45.03049 | 2026-10-06 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f79fa1b0-1f23-375a-a035-f0aa2d5651eb | -6.32087 | -43.81442 | 2026-10-06 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e5562cdb-84e1-3d29-aef4-0e49f3e70db2 | -4.50788 | -43.69236 | 2026-10-06 04:19:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d1815e7-2d66-3b88-9e2b-acc3149a92a6 | -6.88046 | -43.67797 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87c5853f-8cb9-3a02-a0a2-bdb8e6a5edb2 | -3.84234 | -50.31729 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 876c3cf7-619b-3219-a321-8366aeb6014f | -6.18854 | -44.85542 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb49e9e7-9586-3d90-a1f8-af49cb233efa | -3.49443 | -49.90402 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc056975-d967-344d-85cb-cd11ba8ebcde | -7.10222 | -42.54053 | 2026-10-06 04:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0edeb93-66bb-312c-915c-2e7ece2321e3 | -6.7271 | -44.28136 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49d8189a-58bf-37ba-9c14-7e8fbd416118 | -4.45374 | -47.9229 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 74abb79e-d3b1-3dda-9050-5f275f88fab5 | -9.86056 | -44.80933 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eed0d4f7-9513-3fb0-bea8-fae76ddeb2b4 | -5.4603 | -45.52272 | 2026-10-06 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aa8fcb2e-55ac-3a82-9342-c8aeea42c6da | -6.34874 | -42.5658 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6c788755-f5b6-3c72-b6bd-b7acf61eb4ef | -3.07825 | -54.17888 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e65a1d3-5813-3253-a3e5-cf0e4c320bf2 | -6.72777 | -44.27736 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3768bd1a-32d1-3363-bebe-476a4ca18cbb | -8.86768 | -45.37223 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73f75a8e-b899-3be2-b228-b817c78f546b | -3.50558 | -51.67793 | 2026-10-06 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b8fc4da9-91a5-313d-b98e-cb7431d0c664 | -6.19072 | -42.95883 | 2026-10-06 04:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9ff3608-4e5f-3eb9-a18a-f92c43f017e7 | -3.10358 | -53.74401 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b342878e-45a1-3aba-afd4-aeaf56fa75fb | -2.9543 | -54.15669 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8df6089d-44e7-3350-a20c-edffdd3f640e | -11.64962 | -43.65232 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd6db922-74e3-3701-b223-a615da623e36 | -5.96737 | -41.36005 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31d7be48-e84c-325b-bd50-e078a35a6ffc | -11.2838 | -45.51029 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2a3b3553-101e-33e6-8ce8-2b34e8043c10 | -8.70345 | -45.21594 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5276e9e-1905-31bb-a488-70dbbfe4d229 | -3.09546 | -53.7482 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9aad63cc-91e6-3562-b738-bd3d6d7ba556 | -5.94963 | -41.36435 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dad32134-d7a2-3690-bfa0-5dd09783fb17 | -3.89495 | -49.71604 | 2026-10-06 04:19:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4097f52-7d9c-397f-8e4f-c2f99db619d1 | -6.93208 | -43.67865 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 444909a1-c395-386d-b545-5868e3cb0982 | -9.2599 | -45.66111 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d282984-2d7d-35ea-ac17-3efbfc66ba83 | -3.22989 | -53.86908 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40269a30-6fcb-3be9-8405-2aaf95a3a55a | -4.9702 | -47.97393 | 2026-10-06 04:19:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cb3a31e-0e87-3517-8ef7-77c267bd9136 | -6.21104 | -41.5941 | 2026-10-06 04:19:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c3e37ba-036f-3577-bb7f-3b0423fa049a | -6.35061 | -42.54811 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53d17ab3-f05d-3a37-8b1c-73b23a7d6ba1 | -4.50703 | -42.06965 | 2026-10-06 04:19:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8b3a1f6f-619c-3791-b6e8-8288153fe6a2 | -5.40881 | -44.3498 | 2026-10-06 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a7d936-ef7b-3ddb-9d37-28ca088c8741 | -6.07506 | -43.88457 | 2026-10-06 04:19:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7862075e-1c76-33b9-b0cf-b4276e36b76c | -10.97248 | -45.41962 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c2b5f47-b0e1-36bc-b918-d03a742f1e43 | -6.34439 | -42.56543 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9f8a55f2-10d3-3ecd-8683-fd13d7c0d931 | -9.83015 | -44.79596 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 466e5766-79a8-35ee-96df-ce602d2feb42 | -6.8508 | -41.80331 | 2026-10-06 04:19:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85ff2f7b-9a78-306c-bf84-4a1f41d49c04 | -2.87224 | -54.16979 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8703e4c6-37dc-32f2-ac08-81ae7b820993 | -5.40812 | -44.35394 | 2026-10-06 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db3b6529-c30d-3974-88ef-538d550eeed9 | -7.24799 | -45.25546 | 2026-10-06 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33427ed9-8704-3107-afd5-c025aea3ba1f | -4.28413 | -50.27204 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8a04cc1-7600-37b7-b5b1-e758f7e4ea3f | -3.15615 | -50.44304 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93a3d5ba-b61a-3b48-9300-7d26c9c16f45 | -8.69981 | -45.21531 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 815f8218-55bb-35fd-825d-4ee471d559d4 | -6.92736 | -43.67398 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee5078be-2d16-3dc5-802b-609a3686bdf0 | -7.01975 | -43.44602 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da4f07f0-5e2e-3a88-bbb6-6548dc3ab77b | -5.83868 | -45.01815 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1859ac63-910c-3b11-8eb0-e7a4bcc74459 | -3.00106 | -54.13717 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3981319a-0f82-3f8d-a843-003248d42ad1 | -8.61968 | -44.91057 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4417813d-e162-32b6-8802-90f87227ec42 | -2.90414 | -54.08713 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7832ce45-0b3e-331f-a1e5-25c1a8fa3dc2 | -11.27511 | -45.51033 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1e98d4e3-42f2-39a0-87a0-d0aa0b1f7505 | -3.09672 | -53.74287 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82141c8e-4d5d-3f31-86c9-7c3309842c83 | -2.8588 | -54.14092 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc737736-37fd-346c-a7ef-6234daeafae4 | -6.72354 | -44.28078 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3850b7a-b35a-31a1-af36-b61765ca9c37 | -3.2288 | -53.87539 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 751f5c65-3640-32a9-be6f-05ac447bac52 | -4.36138 | -47.77599 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac4760ed-38eb-3218-be99-0907fc2d0fd5 | -11.28668 | -45.51503 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 875b9f01-db52-34d1-b728-814efc86ff78 | -10.50023 | -44.41752 | 2026-10-06 04:19:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59e3fcbf-0cc9-33a8-866e-c688e6e6ade9 | -2.98696 | -54.12183 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa3d5b2c-1d9f-3c08-badc-960d131cd5c7 | -2.95315 | -54.16336 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bd7ad48-d201-36f9-8885-5af458df5226 | -3.09172 | -54.16669 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6047b6d5-0258-38ac-99fc-0e1bbce28d60 | -6.2305 | -47.00134 | 2026-10-06 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 854a95c7-8088-3825-b5eb-1a0189119c75 | -5.64721 | -44.12156 | 2026-10-06 04:19:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59343f33-ce61-3cac-abe4-a56662b7f305 | -2.99518 | -54.12928 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 787d18ff-1ee4-36d1-a3fe-43fb1eda28bb | -6.35221 | -42.54442 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1735dba9-70df-3564-b6e4-d73df9a268b3 | -7.09491 | -45.57087 | 2026-10-06 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 446872d8-7c14-38fd-9815-e60107ee2f3c | -3.10177 | -53.71065 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f8b076d-cc9d-3140-ba27-f2e6d4d45e30 | -6.18909 | -44.86319 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f4b883c-85fd-3a56-bc48-f6082cba6baa | -5.81364 | -53.84194 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54bcbb71-f175-3f80-b11f-6d5dc4db3fd5 | -3.01953 | -53.89867 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| f7201106-4ba0-3d6e-a83e-6dfd9ad42c09 | -6.62098 | -37.88705 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 92a22b60-9415-3070-852e-50eed2f2e8b3 | -7.48048 | -42.79814 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a8f2f283-d95a-34b5-b752-7b9220b60a33 | -3.2347 | -53.87995 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c1880ce-0590-30e8-bce1-b1b799100fee | -11.04818 | -45.64063 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a2ead79-d190-3137-974d-8b51424873df | -4.50433 | -43.6918 | 2026-10-06 04:19:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6f810a9-2659-376c-a69b-cebb4e3f2e72 | -11.29164 | -45.50758 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9b7c43f-89d3-3e37-82d9-55519be15f9c | -8.58335 | -45.66162 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a89ce045-c4ab-3d71-ae09-1f760f97edca | -6.33399 | -46.95051 | 2026-10-06 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a0bb934-ca3f-326d-b5f9-1d78e659b2cd | -3.10217 | -53.7117 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4950b332-7018-33a2-a51a-9962b7bdda6d | -5.88592 | -43.45516 | 2026-10-06 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53e8d4d9-d058-30d2-a9fd-281a4afff56c | -3.0993 | -54.18278 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 67e544dd-fff9-3070-a4d2-e63c04308081 | -3.11401 | -53.76519 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1164752a-0312-32cb-914f-37f6268afccb | -2.92274 | -54.13005 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 139d105d-0f50-36c1-9de1-0acb6859c235 | -4.06076 | -54.04841 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ed97c95-89ee-3bfd-87e6-c0ea9010ba38 | -6.9327 | -43.67486 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d06baf7f-fab6-3f87-a187-2ee36f30d3ba | -5.96182 | -41.35205 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README29.md)
