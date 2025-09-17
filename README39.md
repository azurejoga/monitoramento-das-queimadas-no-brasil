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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2330f337-4676-3dc4-b00a-59445c762143 | -6.97503 | -44.4402 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 358eaa0e-ee7c-307e-aff2-8c8978c2ab7f | -6.62066 | -45.57798 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a240bf7d-ee2d-3813-bc85-4399a47e2ec7 | -9.09136 | -46.93052 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c929832-5f3d-3586-9f5b-f3012470f1ef | -7.41295 | -49.991 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a883fbc2-1749-3225-a3ba-f27cf100d7dc | -7.59187 | -44.58533 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d30fc7e-e604-36a8-b1fe-b803fbbf4a0b | -9.09458 | -44.92216 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44c064a1-413a-35c8-911b-dbf72a2a01cf | -9.06806 | -44.94962 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 811d7b45-8138-3ec8-a203-622d352e6203 | -7.76406 | -44.73106 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9c7bfe1-5b65-3afc-88a8-f8758df57800 | -6.33843 | -43.32859 | 2025-09-17 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3854af91-25b0-334b-8611-283d6fc0cb13 | -7.34765 | -46.74897 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6ec6309f-ab88-3db1-9ec3-bb1d0304a531 | -7.39284 | -50.0069 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af7c4cd-9bcd-3c3e-ad3c-1b125fadee96 | -5.95237 | -47.00993 | 2025-09-17 04:32:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc615fb9-cd3e-339f-96e1-dc1eeea5fe7f | -7.82717 | -46.15889 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01408ac3-9ba7-378b-b60f-fc8aa37f3270 | -9.06832 | -44.95107 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2780b5f6-e861-322e-bcbc-d88c04de816a | -5.87398 | -45.88221 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8136ac66-5436-3973-a38b-457231f5b099 | -7.26262 | -46.59627 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 503b6109-5065-3f3d-89a8-ea109acea7b4 | -6.77739 | -44.70935 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07b590b0-5c0d-3360-a641-ac1f552c7f9e | -8.90057 | -46.27933 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1610cdd0-acec-3834-99b1-ac0fd2e50cb0 | -5.78011 | -51.38828 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5365cc91-d044-37d7-ae89-44b205d0c6e7 | -5.25033 | -49.85688 | 2025-09-17 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29f063bf-735e-37f1-9f56-bdd0c42b7e63 | -8.61223 | -45.71904 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0f756bc-4e5a-3c48-b8af-135ab01535df | -4.34613 | -46.46993 | 2025-09-17 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca963ad8-2471-3023-b714-c56cbbb8359b | -6.52944 | -41.82182 | 2025-09-17 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fd5837a-e082-3590-a489-b1b526f05fde | -5.80353 | -45.93163 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4b925d8-c43b-3ff0-8136-c29f1f5b7ad0 | -8.29497 | -47.98771 | 2025-09-17 04:32:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7239580f-dc77-3a95-bba1-492ec8d12358 | -6.29575 | -42.38548 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5a7bba4c-f798-3964-9857-4cc242d5e68e | -5.67095 | -51.35646 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c7b0bb4-be8d-3d99-8fd3-98e262806591 | -9.24431 | -45.64914 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c71b964-6f67-3aec-b9d5-6f7a3f9e0406 | -9.09568 | -44.94035 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c75dc21e-a159-3810-b0e0-9f1ff5a43614 | -8.91957 | -46.24703 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fd3fcee-b732-329c-8803-0880f3875f5c | -4.9861 | -49.77222 | 2025-09-17 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1caab64-4cb5-38c1-941f-84be51e0bb13 | -5.77857 | -45.93523 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79f16a6b-13ec-3145-aa19-f42bee063c06 | -9.95588 | -45.91426 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15cfb588-136f-3af1-88bc-7f83a36f7e60 | -4.68151 | -50.8376 | 2025-09-17 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efc1fdae-fdeb-3d0d-868c-94d72ab25f0c | -6.68011 | -46.30724 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e96e7cd-d0bb-3b51-a4a1-4f8fd8ce5822 | -5.77833 | -43.94759 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b59cff8f-9544-31b8-95d7-f0aa501f418b | -6.86136 | -43.96888 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b61892c-970d-33d6-bfeb-e537fd3ac5a8 | -10.41311 | -50.6531 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fce2972d-5654-317e-b70e-2d6e67b0d818 | -9.14722 | -46.93505 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 573bf195-5df0-3e0f-b96b-38db584cd5da | -10.43301 | -50.66026 | 2025-09-17 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 879aa4aa-20b1-30ac-a686-f82171e52741 | -8.13785 | -43.64544 | 2025-09-17 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 120bc648-5d2a-3adf-94ec-b8f941a0a0e8 | -4.99908 | -44.87685 | 2025-09-17 04:32:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d9446e6-77a9-3cf7-b4a8-8cae0030818f | -7.02846 | -45.63251 | 2025-09-17 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf3e3818-6527-3fba-89db-06b1f3736eb7 | -8.0844 | -50.15437 | 2025-09-17 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86b6c2ce-7f2d-336b-9fdd-847736104509 | -6.96413 | -44.53605 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4b87d0a-7904-349c-80cd-15219bc8127c | -7.52779 | -46.72099 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a66c02f9-d8f2-3be5-865d-5f8a74d56eb4 | -4.81203 | -47.33144 | 2025-09-17 04:32:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a97d491-70fd-3526-8de4-0595a99c6867 | -8.53677 | -48.97244 | 2025-09-17 04:32:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d753fb8b-eeaa-3572-a8aa-cd18a7a268f9 | -8.9581 | -46.27234 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff6095ab-f0a1-36e9-b2a0-2e26b1e21e2c | -7.73882 | -44.77485 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adc6fa43-8e93-3444-8c49-39add27e832c | -9.75649 | -47.34319 | 2025-09-17 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c559c8e1-f7f1-377f-8226-93b02b16a37c | -6.88026 | -43.97159 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e75672ec-f589-3fa0-8bfb-757856d62646 | -9.16129 | -46.93361 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73aa4ec3-45c6-3c34-a930-2190bd1a7f7f | -7.9931 | -45.68174 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d31cde9-c873-332b-9f4e-c7789a647a02 | -6.87082 | -45.19006 | 2025-09-17 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 479be9b9-6b1e-3e0d-907b-c200e8e6ef51 | -7.58411 | -44.5619 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35ef4aa6-845e-3a43-83be-9a010509a7b4 | -8.0083 | -45.65203 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7107f302-1c1f-302d-a691-f9be45aeceb4 | -6.88094 | -43.96697 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfcdbe7c-5cd0-3aa2-ae8d-a16a8810039f | -5.52265 | -42.18549 | 2025-09-17 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5accd90b-a527-3be6-a2ce-633f6bb23772 | -7.41013 | -49.98673 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f76fd3c5-9794-36ae-9546-3ffb27412f5c | -6.1721 | -44.51025 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 881aefe0-65d1-3907-b48f-0c3934c32a1a | -7.84007 | -43.85136 | 2025-09-17 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b91d0e9b-6916-38c1-9cd4-463cbff1dab2 | -7.48627 | -46.12352 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0988bf4-2a5c-3467-af14-e22566f89bdb | -6.28386 | -42.38013 | 2025-09-17 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7bf82a05-0a2f-3fab-b7ae-79edffc3649e | -4.65227 | -50.99183 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29a2723d-f004-33e8-bb4f-2d604b5fbb61 | -6.86567 | -38.4402 | 2025-09-17 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 26052bc5-9016-3780-83ef-da2ef1f11026 | -8.1361 | -43.63006 | 2025-09-17 04:32:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7daefb3f-977e-3de4-a801-efbfd3cd772a | -9.07915 | -50.31404 | 2025-09-17 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 103c035f-77ae-3a4b-9900-c925375b9b59 | -10.90315 | -45.44217 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05051c1d-1c25-35d2-9cc1-947b8a982407 | -5.08148 | -44.95271 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f762c92-4208-3e3d-8693-1b8e7990bd53 | -10.17973 | -45.31124 | 2025-09-17 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c34de770-b4a7-3e4e-90e7-9b7d40bbcdaf | -7.26372 | -46.58915 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66484edb-2245-33ea-90d7-1c2fa56a113e | -5.76677 | -45.91877 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03965efd-4413-3154-bbc5-114080b997f5 | -5.47671 | -45.3466 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f968a51-274d-3f15-abaa-e0d9e476b7c3 | -7.47947 | -46.09947 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efea24d4-d016-3506-ba6c-5d4c5f45bbc4 | -6.97992 | -44.45324 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ad08715-cfe2-3ee0-9712-90c09bdfb4e9 | -5.67021 | -51.36089 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8738653-265a-3592-88ac-8d37fb7d22e9 | -9.14776 | -46.93155 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f37b79c-1f55-3bd2-903b-57f310b1089d | -8.96029 | -46.3271 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a67632b-2e7c-39e8-8218-ca8dc9d95bce | -5.78338 | -43.93926 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c94c4005-e1c5-32f6-86e8-f7a919ea7fc5 | -8.63552 | -46.43553 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d47e93a5-1b7e-37ed-b3ed-aa6c4fba748b | -6.87142 | -45.18675 | 2025-09-17 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08071e8c-e77a-389e-99dc-d42823a055cd | -8.84945 | -45.44033 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39de2f4c-95c6-39e6-be38-300ed92360d7 | -10.07384 | -48.18443 | 2025-09-17 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cd1406e-7a7c-3792-a7e4-dc2320783f0b | -5.13511 | -45.11663 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cb99c23-4b49-38cc-ab16-114bb7e52010 | -8.92818 | -46.28342 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f08a8ab-e62a-3e24-9b28-f7c4d65b557f | -8.21666 | -49.48682 | 2025-09-17 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06038660-e651-3572-b4a4-b33fbc3b4741 | -5.78763 | -43.47186 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1032b18a-b572-3421-8958-c574c5fe279d | -2.70939 | -54.95812 | 2025-09-17 04:32:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3dac9a4b-8ab6-31ee-8fdc-1b0af9268612 | -5.79603 | -43.46819 | 2025-09-17 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e20db9f-07b8-3ad9-8ef7-f7084631be30 | -6.97756 | -44.4437 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecfff453-43d1-3459-a77f-5ec1634e2e6b | -7.0771 | -44.55593 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb60bb84-9d8c-3401-bee3-85deaa50caba | -6.351 | -43.16291 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 194700e6-7bcb-3604-ab68-1cfb0ab8d2ff | -5.45517 | -50.82734 | 2025-09-17 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c74720bd-68cf-302f-8ef0-03847c0813ab | -8.56869 | -46.34502 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b57abfc8-fefb-364e-bc69-da0292a05026 | -6.42153 | -43.30849 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b6e02a1-ccb1-3816-bbb7-96c47b5b775d | -9.0877 | -44.94363 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c7a2686-cad2-3efc-813c-c2a6d0663cee | -8.6543 | -46.40398 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcd2ccfd-4c87-390f-b331-78843c785a1f | -7.21079 | -44.38082 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcd1caf1-5b93-3e69-b483-96863611e20d | -7.85693 | -46.10185 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README40.md)
