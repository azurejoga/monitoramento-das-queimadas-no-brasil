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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55a82fd1-9550-3e34-a72c-72f35910a589 | -12.6909 | -47.9899 | 2025-09-16 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b6988233-ce21-3970-8cad-a20817b162ac | -12.6729 | -47.9258 | 2025-09-16 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 06046abb-cc01-3167-9eb2-79e517fd63f4 | -12.6356 | -45.7422 | 2025-09-16 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| ad26f67f-2d30-3dbd-92ae-36a8043f2ab2 | -9.086 | -44.8663 | 2025-09-16 11:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d785e6f8-b057-34e8-8867-16df449aa0d7 | -12.6352 | -45.7652 | 2025-09-16 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 41b6a90a-0063-3891-ab97-f7ad5752bcf2 | -12.6906 | -48.0121 | 2025-09-16 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 353.7 |
| 6adda7ca-359a-320e-bd2b-2fa5cae2b3e4 | -12.6729 | -47.9258 | 2025-09-16 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 40e5fd13-1fb8-3eb3-8f45-8ea1abd08339 | -12.6909 | -47.9899 | 2025-09-16 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f4b7575d-5a61-378b-beba-d521c1001aac | -10.7302 | -46.5082 | 2025-09-16 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 16c6233e-6b7c-38db-ada5-d6f1368981cf | -8.9568 | -46.0398 | 2025-09-16 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 3b500c74-b8d3-3108-b68a-07602f8dfec2 | -12.6713 | -48.0148 | 2025-09-16 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 81a77309-b3b0-3951-acc2-e933747879f7 | -9.0857 | -44.8893 | 2025-09-16 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 78f7d4ff-8df6-3ef0-829b-c99cac154463 | -12.6352 | -45.7652 | 2025-09-16 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 33437fdf-1f6e-395a-a5ca-20d9d3c98ba3 | -9.086 | -44.8663 | 2025-09-16 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0a4fb4df-7c4b-3654-9dc5-7058494cabfc | -6.7569 | -48.1173 | 2025-09-16 11:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 162.6 |
| b3d1aa1d-dbf1-3a9e-acbf-99eceb5ba5e9 | -4.5934 | -43.3239 | 2025-09-16 11:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9634b420-3fd8-3864-a327-5db5f7f93248 | -8.0196 | -45.662 | 2025-09-16 11:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 226.7 |
| f617a540-6dfc-3815-b7bf-8beea2a7f6d0 | -12.6725 | -47.948 | 2025-09-16 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| ca71a8f6-0bca-3bfc-9eca-8de4c09fdb15 | -7.1505 | -47.9786 | 2025-09-16 11:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9f1b2df6-9487-3292-b2ab-ad9668c2e8d8 | -8.0007 | -45.6638 | 2025-09-16 11:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 21dd7095-5d09-3928-bf87-4d98f656cd32 | -12.6917 | -47.9454 | 2025-09-16 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 47b02a54-9471-3a5b-a827-163b05bc148e | -9.5309 | -45.523 | 2025-09-16 11:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 871cfe38-a793-32fd-9122-fec6bc07cb9f | -15.9998 | -59.2446 | 2025-09-16 11:50:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 9405ed13-ef74-3543-b629-9632265548ef | -7.9822 | -45.643 | 2025-09-16 11:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0f94f1d6-1595-317a-94b6-09bfab3a523e | -12.6356 | -45.7422 | 2025-09-16 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 6780b415-11ef-3815-bb2b-1be125f50cd7 | -8.9757 | -46.0378 | 2025-09-16 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 14a0049c-ecec-3643-b5de-374b8628dbee | -3.37245 | -42.31923 | 2025-09-16 11:55:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 02408c70-6ac2-392a-b251-7d28a9f2db85 | -3.3711 | -42.32857 | 2025-09-16 11:55:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 2c9801f6-5d4e-3c05-b813-62b973f18dea | -3.02147 | -43.06903 | 2025-09-16 11:55:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 482e2a66-c4c7-3189-953e-54ffc5967cf1 | -3.25875 | -40.03417 | 2025-09-16 11:55:00 | TERRA_M-M | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 63c8fb32-a1e0-30a1-a019-9431be0e7fff | -3.41223 | -39.54401 | 2025-09-16 11:55:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c7febda9-379e-3c48-bb8b-b114ce053472 | -6.73174 | -38.1375 | 2025-09-16 11:57:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 6dc43ac8-7aa2-3f14-81b2-c3b2a072c208 | -9.76008 | -40.05755 | 2025-09-16 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bb623b62-3424-3324-8729-34e3a0eee03a | -8.62049 | -46.40471 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 956756c4-22a5-35db-9c99-5fff364140d2 | -8.91223 | -45.52868 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| bc144500-4d08-378f-a6a7-256ae8301755 | -9.16934 | -47.01286 | 2025-09-16 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| fd4e1b4d-85a4-3d09-a613-43bc3f6bc8ee | -6.68964 | -45.31853 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 816fcf54-da62-3365-b044-7877ad9a96b6 | -3.42647 | -43.15134 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c6d555ba-c28b-3fd4-b586-0a24b44f42e1 | -6.4437 | -42.63715 | 2025-09-16 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| becf31cf-c149-3312-8b37-7ebd1e7bf266 | -8.67939 | -46.38494 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5ed506bc-089f-388a-a520-3fd408912272 | -9.09125 | -44.88304 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9cceb26f-d19e-38eb-9cf1-87901e7da14b | -5.81391 | -43.48125 | 2025-09-16 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| cdf3e0c6-d6ad-35a0-a938-fc8a0c907a45 | -6.54722 | -44.00797 | 2025-09-16 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 48ae3c31-b7f7-3d1b-a02c-408d19e2adb6 | -8.88227 | -46.19155 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a5c8fd0a-ace2-30fd-a915-404c0792deee | -10.7221 | -46.53048 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 51804aee-05e0-354b-a44e-3d3fed0bd9bd | -5.569 | -43.56666 | 2025-09-16 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1acca966-6922-3ce3-8012-13f7d9abf137 | -10.64161 | -46.45664 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9a4feef0-d372-38a0-abe2-792cc309eaf7 | -3.81327 | -41.5718 | 2025-09-16 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 04b3e62a-d165-3311-8176-a4da7302651b | -8.00932 | -45.66299 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2d3b4a12-f310-39a8-833e-b0dc51c3fc5e | -9.04771 | -44.84223 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| aa9d2cbe-dc59-3fcb-a966-ece92bcc153c | -9.05742 | -44.8437 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3e8198a9-165a-3f29-aa42-c20a1c6caf44 | -9.17177 | -46.99768 | 2025-09-16 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 39737f69-2b97-3a54-b356-60bcde7d847c | -8.59015 | -46.3657 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 684dedd4-37dc-3f04-8ede-45c9fbd16ca5 | -7.70647 | -45.30119 | 2025-09-16 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f163b5ce-656e-30cd-9958-863bd8d1b270 | -10.7371 | -46.50451 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c77c65a9-2c32-3370-b57b-2d8bbc4b7332 | -9.06224 | -47.03394 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b078a1c1-815a-30e0-8ee6-2f9cae719fc6 | -7.44927 | -46.15823 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1ce20114-21a5-358b-a85b-d2ec95b1c1f6 | -6.97066 | -44.54601 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 30818c22-ae63-32d3-ba1d-39982717069d | -7.4412 | -45.83068 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c8f575b2-e349-3994-b48e-3956efd5cdef | -4.52717 | -42.05128 | 2025-09-16 11:57:00 | TERRA_M-M | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 508d193f-df9d-31ca-921a-d35607e26195 | -9.76806 | -40.06884 | 2025-09-16 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| c8796fe2-4059-3ef3-9615-a573881d67dd | -7.98194 | -45.6333 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b9638568-7a9c-3716-9ec2-6afa62e76c74 | -7.46236 | -46.14608 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bc9f4856-90fc-3a2e-83a4-6e1025392552 | -9.16286 | -46.98085 | 2025-09-16 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0afba402-c100-3399-b5c9-b1513adf92d3 | -9.32506 | -43.24326 | 2025-09-16 11:57:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9577876b-647d-3f2f-a0ad-d21c0cea5cdd | -6.73336 | -38.12569 | 2025-09-16 11:57:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 14.5 |
| dbde8186-a6dc-3b18-861d-ba2afacefb76 | -10.48183 | -45.18349 | 2025-09-16 11:57:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bcd256b3-f015-302c-8bff-765fde7072e9 | -8.97784 | -46.24063 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 7d08b91c-04d5-3dc4-b9d2-d340d1026910 | -8.96139 | -45.8845 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 753edd69-0392-3efd-be46-a7cad2744227 | -10.73189 | -44.75533 | 2025-09-16 11:57:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5aaad104-9e78-357b-a902-d5a64f5e0288 | -8.89494 | -46.18028 | 2025-09-16 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1a4ca80d-339c-386c-b4f4-3022ee86a914 | -5.75467 | -43.68923 | 2025-09-16 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4ddfd41e-9c5c-35aa-a960-45841684e200 | -9.53784 | -45.52211 | 2025-09-16 11:57:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a0629b8f-8383-3b79-b699-c8e4891ffab5 | -9.08319 | -44.87046 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0062bc94-c535-3f67-acff-483c0c401700 | -10.72239 | -44.75415 | 2025-09-16 11:57:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9266e52e-6b43-3d45-8c5f-2828dd2b4566 | -7.48849 | -46.12153 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 40ce834b-e0ed-3b31-a4d7-59451ba5171b | -5.26331 | -43.5663 | 2025-09-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f9ee08bd-d92b-3b6c-90bb-44ad16e5eb50 | -9.07987 | -44.89248 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| fd40b2dc-7698-3a41-917c-b5bc6f5f0a47 | -5.49252 | -39.42483 | 2025-09-16 11:57:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 5f46acf6-6375-3ad5-9919-37242512a799 | -7.7269 | -45.3042 | 2025-09-16 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ddc43ad9-c03d-3520-8999-a6ec0279df0c | -10.4835 | -45.17261 | 2025-09-16 11:57:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2391d704-6eb5-3793-8153-a8bc106002a7 | -10.73487 | -46.51865 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| c56b7f6e-4524-3832-81f7-a34bd08d4f39 | -10.73274 | -46.53207 | 2025-09-16 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bb8ee315-1bb0-39c0-a267-af3c50c7cee8 | -8.01789 | -45.67673 | 2025-09-16 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| a763deee-b048-350c-bb2c-00729d99c17b | -5.2618 | -43.57645 | 2025-09-16 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 285a2d37-1631-3d9c-a888-f5fbcbe27751 | -9.07823 | -44.9034 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 8fd37661-2524-3f07-a7ca-fe4606a205e4 | -6.40504 | -42.65025 | 2025-09-16 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 7d1fcf55-d170-3e40-a5e4-1ad22f1baa29 | -7.69717 | -44.49192 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 492e9b03-a471-3f78-8fff-0f5d1ddb0252 | -7.6785 | -44.679 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 47c8a673-3c10-3ea8-a010-c59a323a9515 | -6.16831 | -44.49633 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2a4930b4-0c96-354f-b7b3-30a5b196a494 | -6.76973 | -44.72157 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a51484d9-8c24-31f6-b14d-45d8a36b8d0b | -4.60076 | -43.31784 | 2025-09-16 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 50f5d018-f85a-3ebf-8fb7-bfe92c8860e0 | -9.08151 | -44.88161 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a30f6f20-5fc3-3d48-9eab-138e41cb8bc6 | -7.44574 | -46.16522 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 76bc1c40-00a5-302b-83ef-b3e1f85fef9b | -8.93384 | -45.51373 | 2025-09-16 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a69b8198-06d5-316f-a8fc-8c72d7886645 | -6.34714 | -43.16716 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1425a380-c076-3ce6-8f3d-a1acfbe85baf | -7.15662 | -47.9956 | 2025-09-16 11:57:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 52fc7826-ae8b-39e7-9278-70b77f3a2f03 | -6.77145 | -44.71019 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8862a4a9-bdf4-3260-9821-58de3a88ab47 | -9.52593 | -45.53254 | 2025-09-16 11:57:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 0f23ff64-5ddd-3479-ba8e-d9e9caa3ca8a | -9.75952 | -47.14451 | 2025-09-16 11:57:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README87.md)
