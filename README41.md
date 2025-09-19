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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2682f400-c860-3a42-bcfa-623a72fc7b15 | -8.9161 | -46.269 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| c4a5b2fa-da36-36d5-b367-595542240441 | -9.1461 | -44.6295 | 2025-09-19 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d9d430e3-1d0a-312e-a96d-590dd7c8363e | -9.01 | -46.3039 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| f6db79f0-706d-3c00-86eb-6386ef61185d | -8.8801 | -46.138 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 91b460d3-0dd7-32a3-acd5-296d938db68d | -7.6389 | -44.4455 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 12150950-4676-38ac-8299-8e0407541614 | -8.9892 | -45.0376 | 2025-09-19 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 8af59742-de27-3b02-8e6c-281349ea3f65 | -8.9908 | -46.3284 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| bef749e3-1f1e-39ba-8f74-799596ae449c | -8.6265 | -45.3282 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 27aad5cd-0c91-3a53-aedc-2b33b89d53fc | -8.899 | -46.136 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| add86faf-0bc5-3164-aec2-abb8b249639e | -7.6951 | -44.463 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 74b9c3bb-cc6e-367d-aa4b-75052581738d | -9.1744 | -45.3135 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 773d00ad-076b-3f82-a5a4-c2ecd1095330 | -6.1881 | -41.1855 | 2025-09-19 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 221.3 |
| 41431c2b-1fee-3ea5-ade3-2d6944af2c9d | -6.1876 | -41.234 | 2025-09-19 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| f56caaf2-daa3-3f98-84f6-8dc86cbb2033 | -7.1878 | -44.4193 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b2cbf1a3-d19c-3b63-95ac-fa7b94c2c434 | -8.9179 | -46.134 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c2c9aa29-3dc9-3965-97cb-49abd3adb311 | -7.7148 | -44.392 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 4e5027a4-491e-31bc-ac8a-f4f51526523b | -8.9344 | -46.3119 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 255.6 |
| d1d0dea3-fc58-3524-be0c-b741ddf5deb5 | -6.9207 | -44.8097 | 2025-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6e3a45e5-8d4d-3ceb-83dd-b5b51797a83c | -6.169 | -41.2114 | 2025-09-19 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| f081b1db-5907-386a-9bbd-859b1abfc13c | -5.8073 | -43.6352 | 2025-09-19 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f82fd761-e9d5-3dd4-8f97-79940970d5e7 | -7.3366 | -44.5663 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| eeaa0698-4583-312d-bbc4-0d6f9b73d126 | -9.1747 | -45.2907 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 08d0e717-41b9-35e1-9335-2c63f87d4e30 | -8.9347 | -46.2894 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 85a3a707-7d50-3606-afcc-083ea967e8c4 | -7.5818 | -44.4971 | 2025-09-19 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 55e385f9-21cc-391f-ba10-a663572431da | -9.1933 | -45.3114 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 22c4f1de-acf5-353e-b042-dfd77c7e15fe | -6.1878 | -41.2097 | 2025-09-19 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 340.0 |
| 0a258e22-de7c-3ab0-a3be-31f16f53e852 | -8.9911 | -46.3059 | 2025-09-19 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 8c30340a-eeb5-3c9e-92bf-8954d58ddd1f | -6.921 | -44.7869 | 2025-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 874ddf6b-9b2a-3590-8c52-d039a9f937ba | -8.9895 | -45.0147 | 2025-09-19 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dd1f0598-4785-33c0-887d-ee63afe6b294 | -8.9985 | -45.7418 | 2025-09-19 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 9a2140d7-330a-322c-9c5b-fdb6fa47da02 | -6.4239 | -43.8638 | 2025-09-19 13:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e152be92-8700-3232-ba8c-2ee93eafcca8 | -8.9796 | -45.7439 | 2025-09-19 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| dc067350-14c7-34d0-a39a-bc1bddc45009 | -5.9253 | -45.0718 | 2025-09-19 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2710f5b1-c037-3174-93a1-a0a0e433a670 | -6.9212 | -44.764 | 2025-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c9c2ff61-3ef6-382a-b07e-07768537364b | -6.9022 | -44.7885 | 2025-09-19 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2c290099-cd6c-3f69-88fd-6989420ca26f | -9.1937 | -45.2886 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 226.9 |
| ff297436-b788-3a1a-82ae-9957cff830cd | -8.6076 | -45.3302 | 2025-09-19 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| acc86ddc-d1e9-3515-833b-76fcbe71a501 | -14.8603 | -51.6523 | 2025-09-19 13:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 8b11260f-0e30-3fa1-b745-838cebcef0c1 | -7.3363 | -44.5892 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8d678d5d-bcd1-31ac-a4d2-9a22178e54ec | -7.7148 | -44.392 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6d08f304-023a-3134-b57b-c6e8300de71d | -8.9179 | -46.134 | 2025-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f7236fff-5c6c-3c46-90ef-172df857fc78 | -3.1562 | -43.2587 | 2025-09-19 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 57a4dfa8-0f94-3a47-8edb-aeed4bcb80b9 | -8.6265 | -45.3282 | 2025-09-19 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 34f0815d-1b11-3b01-84c4-1a7274c70545 | -7.6949 | -44.486 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 7ea14819-b1b5-3aa6-b9db-3a9001ab8c87 | -9.1933 | -45.3114 | 2025-09-19 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 231.1 |
| ab916a49-5345-3491-b950-9eea8dacfeb8 | -9.01 | -46.3039 | 2025-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 22e792fc-71ab-325f-bf11-ab0c9ff5e6ca | -6.921 | -44.7869 | 2025-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a4dc1cc6-fdde-3a15-886a-fc54b1fa1832 | -8.3146 | -44.6527 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 3847ef45-a3a2-3ff1-bc20-6981410e1576 | -7.5598 | -44.7743 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5a1d3cd8-76d7-3204-92f2-716dee91592d | -7.2609 | -46.3376 | 2025-09-19 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 4005298a-ba2a-36e6-a609-ce6d6848436d | -6.9022 | -44.7885 | 2025-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ddf20caa-06ed-3d28-af74-a1169956efdb | -6.9212 | -44.764 | 2025-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 4500fb7c-4a58-323f-b2c5-24131b8c8584 | -7.3366 | -44.5663 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| eca52ae5-7f17-3277-98de-e04bc885ce57 | -8.899 | -46.136 | 2025-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| ba15dc4a-5f57-3d55-bc03-f743cf77b862 | -9.1747 | -45.2907 | 2025-09-19 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 57f3eaf4-d5bc-3d51-866f-a5526fe0b797 | -6.9207 | -44.8097 | 2025-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3ffc6280-b41b-3f24-91f3-ea7878872639 | -6.9024 | -44.7656 | 2025-09-19 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d0cb95da-639d-3c8f-9aae-8e091415bee2 | -8.9911 | -46.3059 | 2025-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 47d289e0-eac7-3803-aa4b-7f537e9d7730 | -8.0188 | -45.7298 | 2025-09-19 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 8ef5c955-572c-31b6-a757-ec844584017a | -6.1881 | -41.1855 | 2025-09-19 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 163.3 |
| dfc9ca95-ae4a-30bf-b2c7-220353bf09f6 | -7.6951 | -44.463 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 4952ed50-e8f5-316d-b161-709b3f197a4e | -6.6508 | -45.5359 | 2025-09-19 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e0d08787-3b43-3ba2-9df1-7060b2c576b2 | -9.1937 | -45.2886 | 2025-09-19 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 702044c8-36ed-3036-917c-cc27da3002ee | -8.8801 | -46.138 | 2025-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 6713a6d7-191a-3e39-bc14-e2cb66df4f2a | -8.3334 | -44.6507 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f099d05b-d835-3d48-bfaf-2ed622f6cdb9 | -8.0281 | -44.957 | 2025-09-19 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 04e8a3b7-41a7-3821-b4e0-206c0b3d34fe | -8.9344 | -46.3119 | 2025-09-19 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| c393208e-7fe9-3f12-9ca4-bac36a5f84ad | -9.1744 | -45.3135 | 2025-09-19 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 60f9cae5-ff4c-3af3-a0d4-d3a09ca4c03c | -7.1878 | -44.4193 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3d09d0d0-a144-3a38-b19e-49c6c2c0e376 | -7.5818 | -44.4971 | 2025-09-19 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| db6653ae-0cb1-3ab5-b394-7faf55a69f6a | -6.1878 | -41.2097 | 2025-09-19 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 223.3 |
| 4125685e-e067-3849-b3e2-89898402931d | -7.6574 | -44.4667 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6ef92aa9-3468-3f0d-9bb8-c05f928ebb24 | -9.165 | -44.6273 | 2025-09-19 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| cad517d2-efaa-3472-a914-5decb2148172 | -7.4531 | -42.644 | 2025-09-19 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| f5e2e808-0455-3eb7-8b73-ed09df772fc1 | -5.5393 | -42.176 | 2025-09-19 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| cfa567bb-bb40-3cc2-a190-e59e6df3fc94 | -8.9895 | -45.0147 | 2025-09-19 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 72c22d59-26c2-39c5-9fc9-1908353c002c | -8.0092 | -44.9589 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a8307652-40da-35c1-be97-0d4744f05d06 | -9.1747 | -45.2907 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 204ca508-68c3-3291-9c69-b4e3e4e6d02c | -7.1878 | -44.4193 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| af4f5b2e-c169-358e-8281-14f2e838fe83 | -8.6265 | -45.3282 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 200.4 |
| da8e9b4a-cdb8-3af0-9167-547a7bd91a82 | -9.2123 | -45.3092 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 4545e8f2-cff8-35cb-925d-befe2186e052 | -3.1562 | -43.2587 | 2025-09-19 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e52d9439-a747-3dc6-b2b4-7fa902e0e630 | -4.6762 | -37.6106 | 2025-09-19 13:40:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 5fc48365-88cb-322d-b481-8f0dd2db18ec | -8.9344 | -46.3119 | 2025-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 8101ed56-90ce-370e-86d0-731480b21c18 | -8.9892 | -45.0376 | 2025-09-19 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| eb87cb37-1f58-302c-ad9f-784472f8df39 | -6.6319 | -45.56 | 2025-09-19 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 6c573a47-4c73-31ec-8b2e-52aeb5ea8506 | -9.1458 | -44.6526 | 2025-09-19 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 185c4bf1-c8f0-3b82-b7b7-59148edcd741 | -6.1881 | -41.1855 | 2025-09-19 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 91dba86f-8c89-3109-a71b-66fb0e628275 | -7.6386 | -44.4686 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 1c2419b8-2233-32c9-aae2-a9979e8e5c37 | -9.01 | -46.3039 | 2025-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| a983e1d5-45f9-3a93-9efd-293cbd7be624 | -8.9796 | -45.7439 | 2025-09-19 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.4 |
| e3ba6206-68c3-314e-96c5-976b68c39b70 | -6.9022 | -44.7885 | 2025-09-19 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8a960244-7d5a-3fbe-9720-352be318fe34 | -8.899 | -46.136 | 2025-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| bda70eab-15c4-355a-8598-8523cc33218d | -7.3366 | -44.5663 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4749543c-2834-3cd6-b1bb-ef1f94d2fae9 | -8.9985 | -45.7418 | 2025-09-19 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| e4c5b4b5-d9b8-3cfc-a215-cb8a4d986432 | -7.3363 | -44.5892 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 154e02cf-8ba3-346c-b890-845e8a2873f8 | -6.6321 | -45.5374 | 2025-09-19 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 242122b9-e045-37c7-932f-96d02d8df87d | -7.5818 | -44.4971 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 68908c49-4905-33c4-bcc0-3f8aced532a6 | -9.1461 | -44.6295 | 2025-09-19 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 873e199c-e134-306e-a63d-ebcb0a998e86 | -5.8073 | -43.6352 | 2025-09-19 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |


[Clique aqui para ver as próximas entradas](README42.md)
