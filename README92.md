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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46d80f59-73ec-355f-b1d6-99ff1a24bf0f | -8.6699 | -46.3618 | 2025-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 54849c82-7a79-37a2-af2c-809b121834b1 | -8.0007 | -45.6638 | 2025-09-16 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 7d537e41-453d-31ec-ba05-f74af812ce35 | -11.1299 | -45.3426 | 2025-09-16 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 71fb3d63-8230-3dab-a367-d5036d3d55d3 | -6.1878 | -41.2097 | 2025-09-16 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| e0ab1a7e-230a-35b5-8377-65a74d27c712 | -6.8156 | -47.8298 | 2025-09-16 13:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3a6081bb-34d5-3cb1-8d28-ef0276ca0bed | -3.8416 | -44.0824 | 2025-09-16 13:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 769.6 |
| 96278075-8bed-3198-b785-f39d54f8cbb3 | -8.613 | -46.39 | 2025-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a16ab94c-7c5c-3fe5-9d7d-fe971b26bcad | -7.6949 | -44.486 | 2025-09-16 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3b264f63-1755-3209-9bfa-224c73a7a244 | -6.3372 | -43.1492 | 2025-09-16 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| abeb1d9e-0beb-39c3-b58a-db63e57c32cf | -10.7302 | -46.5082 | 2025-09-16 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 56a82e05-27f0-324e-86d0-99346ae3ed66 | -10.7489 | -46.5283 | 2025-09-16 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 8f00042a-a1c2-375b-8a5e-3af6c1cb40e7 | -13.2798 | -54.2435 | 2025-09-16 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2e3827c3-fca1-3e0a-9f4b-f4dfdcf7ac2d | -7.2768 | -46.6036 | 2025-09-16 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a2df66ff-783f-3c12-bacb-090cdc0ef6b4 | -8.992 | -46.2385 | 2025-09-16 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a99244cb-9414-3043-a750-d632eaffd047 | -8.5939 | -46.4143 | 2025-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ac35b798-d777-3e16-96e7-94d9918463a5 | -6.1881 | -41.1855 | 2025-09-16 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| f80506e1-8339-3601-a89e-b2290044d5c6 | -4.6123 | -43.2994 | 2025-09-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 685c94bd-0f57-3758-b7d2-c03936777ef4 | -11.4853 | -43.5929 | 2025-09-16 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 52ce1c07-80d2-3539-9ad9-234d09330667 | -6.337 | -43.1727 | 2025-09-16 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| bf158a02-916d-3283-877e-cbf6744c3386 | -9.1709 | -46.9792 | 2025-09-16 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cef915fa-4e69-3bd6-975a-ddaa51560f1f | -10.6548 | -46.4727 | 2025-09-16 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f2061cc6-1ef6-3dad-953e-a0d41badd859 | -8.6885 | -46.3823 | 2025-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ea7aec76-143e-3887-b6c7-64c485d9f684 | -9.1047 | -44.8871 | 2025-09-16 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4633a32b-17af-39c3-93f7-bb21f3fd662a | -15.9998 | -59.2446 | 2025-09-16 13:00:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 07a3f749-781b-3277-b24e-368dbbf802a4 | -9.105 | -44.8641 | 2025-09-16 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 16a8f29d-0372-3e4e-9adb-9d65e293375a | -9.086 | -44.8663 | 2025-09-16 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 28324ce7-6348-3bee-b0a5-91b3aecd1501 | -10.7115 | -46.488 | 2025-09-16 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 07fb22c9-8fc1-3f0f-9771-7b3eb888d2fa | -8.0196 | -45.662 | 2025-09-16 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 449.9 |
| caf68a8e-7566-33e4-a2ae-2b6296ccfe46 | -6.8343 | -47.8284 | 2025-09-16 13:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 5961517c-64ed-3403-81d8-ff981cedff89 | -7.078 | -44.153 | 2025-09-16 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8a7f0d0d-b0c6-3f2e-9f1a-69efd19c5e2f | -4.5936 | -43.3006 | 2025-09-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e9b454a7-6827-37f5-9674-775a6fd17bf0 | -11.5041 | -43.6136 | 2025-09-16 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 916487c5-5469-3ca7-ae39-bb00ee6db4d3 | -5.8088 | -43.4724 | 2025-09-16 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 91f2e055-c4a0-3f2e-a7b2-47341be23900 | -10.7112 | -46.5106 | 2025-09-16 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 104e3d4e-c36c-3391-b57d-6926b1b16b29 | -8.9259 | -45.5231 | 2025-09-16 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4816bc65-d7bf-3b07-90fd-b7b8cf72cd69 | -8.9412 | -45.7933 | 2025-09-16 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 57e2632a-8ba4-371e-84ed-fbe39e31ae64 | -10.7299 | -46.5307 | 2025-09-16 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 17ccb246-3210-353e-8c84-8510c5164587 | -12.8087 | -44.744 | 2025-09-16 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b94f9ccd-d8ec-3e85-87f6-0b703cd8dffa | -8.6696 | -46.3842 | 2025-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fb109b20-3ff5-3ace-bc14-8c95578de772 | -9.0854 | -44.9123 | 2025-09-16 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 9140e009-05ff-3275-8c66-275420429cbe | -5.8086 | -43.4956 | 2025-09-16 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 56b22287-5bce-3cee-8569-98d706078167 | -12.6352 | -45.7652 | 2025-09-16 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| bdde6fcb-0cab-3d1e-98e5-b26a7a6d7a50 | -4.6121 | -43.3227 | 2025-09-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a95e1db2-dcf1-3ce0-9055-87e63d02052f | -5.8086 | -43.4956 | 2025-09-16 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| da8dcaf9-5e16-3918-beaa-6535e5356ee4 | -10.7299 | -46.5307 | 2025-09-16 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| b7d60964-26f5-3b25-8c9e-25d24c771496 | -7.2771 | -46.5814 | 2025-09-16 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b7ccbe70-f25e-33e3-8df1-c9236013fb38 | -6.8343 | -47.8284 | 2025-09-16 13:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a8692a5a-ea30-36ea-bfe6-a74d327dccc5 | -8.9259 | -45.5231 | 2025-09-16 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 57c6c574-4aa1-3747-9bcb-8b37ecce04b6 | -8.9731 | -46.2405 | 2025-09-16 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 294.4 |
| 8735c70b-9c80-3da0-9bcb-7a6f0350562f | -7.6763 | -44.4649 | 2025-09-16 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 039d3484-5ec6-3363-a7fa-f234404dabbb | -12.8082 | -44.7674 | 2025-09-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b684e09a-9912-35c1-8e07-c1b81501ac14 | -12.6356 | -45.7422 | 2025-09-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 45a810cb-30d1-3449-8d6d-d0275dcdd8c4 | -10.7302 | -46.5082 | 2025-09-16 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 5728f1e9-5335-3063-930e-1567fd34ce6c | -7.2768 | -46.6036 | 2025-09-16 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c83ad9a7-ef4d-336e-b3c0-d0e267c2bc78 | -7.9822 | -45.643 | 2025-09-16 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2a64a60c-bdde-3670-8968-1309d831c62b | -6.3808 | -44.4205 | 2025-09-16 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 32600d81-4ef4-322b-b2e4-b0a31984c588 | -9.0485 | -44.8477 | 2025-09-16 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 982f2f5c-0499-3536-91ff-bfd419f28041 | -8.9589 | -45.8817 | 2025-09-16 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 9f109cf9-bb2c-3dc8-b1b8-71a7247e26f4 | -5.8088 | -43.4724 | 2025-09-16 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ff66776c-aedb-30d7-bb88-972f42d7f54e | -9.1523 | -46.9589 | 2025-09-16 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8328d83a-d6d2-30b9-8fbe-f1f2e282172a | -8.9412 | -45.7933 | 2025-09-16 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c370bf3c-6baf-3064-88d3-147413eab826 | -6.1881 | -41.1855 | 2025-09-16 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| a94530ad-9487-34d1-af21-8763781075fe | -11.149 | -45.34 | 2025-09-16 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 970f5914-117c-3706-b5d1-8a49ba5c5ab1 | -5.8809 | -45.8641 | 2025-09-16 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 469a7909-7c55-3cc5-9907-cc85dbc01611 | -15.9998 | -59.2446 | 2025-09-16 13:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 42a57e58-88b0-37fa-999c-76d863dea111 | -7.676 | -44.4879 | 2025-09-16 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e0ef2c1e-5cf6-3006-8374-c4a5d91e227a | -8.992 | -46.2385 | 2025-09-16 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 342.0 |
| e063dd28-6db8-3256-afe4-55d6a185edb4 | -8.5939 | -46.4143 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b51e253b-e726-39df-9fd7-56d71c460ffb | -10.0934 | -47.2332 | 2025-09-16 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b4c42b4c-a205-3f5c-9e58-6998e148ed81 | -3.8229 | -44.0833 | 2025-09-16 13:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 03f6e12b-467b-3fb3-ad15-05bc5617eff7 | -5.994 | -43.7134 | 2025-09-16 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 88a4a00c-bc06-3773-a676-628c8c5f6458 | -6.3558 | -43.1711 | 2025-09-16 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 5fa92b99-78ea-3c16-b8e2-a6fa5851188c | -6.8156 | -47.8298 | 2025-09-16 13:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b86efa07-8d80-3d5d-838a-3d1de97c65b7 | -9.152 | -46.9812 | 2025-09-16 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 08074047-56b1-31f9-bf8f-84a022896bc0 | -8.001 | -45.6412 | 2025-09-16 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| f7a2d9d9-7632-3c07-9eeb-93ac697c9460 | -13.2801 | -54.2228 | 2025-09-16 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 034c197d-6f2a-3409-9197-b9f37dae5771 | -8.9734 | -46.218 | 2025-09-16 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0658a0f6-a341-3662-95c1-8c73b27376e3 | -11.4849 | -43.6166 | 2025-09-16 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1ac4502b-a3d1-3a36-9561-dcc146595667 | -7.6738 | -44.6717 | 2025-09-16 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 365223f5-3970-364d-a561-07b44bf7f5ff | -11.5041 | -43.6136 | 2025-09-16 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c0ddcdc7-28ff-3126-9dc0-e39ed1382c2d | -8.6124 | -46.4348 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 524fb59d-1930-3928-b069-d207d63b6993 | -9.1712 | -46.9569 | 2025-09-16 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ee1510b2-1f1c-360b-9110-eb62af1adda3 | -12.8087 | -44.744 | 2025-09-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 1ceb1f67-904a-303f-adf4-26610cdb1009 | -6.3623 | -44.399 | 2025-09-16 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e24698c2-f582-3864-a5ca-45abd20ababe | -6.3372 | -43.1492 | 2025-09-16 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 95188626-b7ff-3a76-b160-c1528f2a3670 | -8.6127 | -46.4124 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 45cf7a82-b95b-34a7-82c5-1b15d2cc1979 | -4.5936 | -43.3006 | 2025-09-16 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 45361334-1180-3bd8-90f7-cb47ae4de875 | -9.7126 | -47.4089 | 2025-09-16 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 848b4265-2dd7-3732-ab66-2c20478c673a | -3.8416 | -44.0824 | 2025-09-16 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 680.7 |
| 448bf9e6-effd-3b61-aa30-667baa8dbccd | -12.6352 | -45.7652 | 2025-09-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f39cdc34-df77-32c5-a729-3cb1704a6cb6 | -6.337 | -43.1727 | 2025-09-16 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| cec71de2-7d93-3c2b-865d-5dff9dc6498c | -8.0007 | -45.6638 | 2025-09-16 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 3db55679-5885-3acc-b8ff-29731faa2fdf | -7.1505 | -47.9786 | 2025-09-16 13:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 554307e3-9e6f-3371-b49a-317b0945b999 | -11.4853 | -43.5929 | 2025-09-16 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| fdc66d22-0978-3951-9d15-c764269acbbb | -8.6699 | -46.3618 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6f9781b0-81ea-35aa-a323-21fe23429521 | -8.613 | -46.39 | 2025-09-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 1efaf895-2aa1-3fc7-a936-649c7de50b78 | -8.8987 | -46.1585 | 2025-09-16 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c3d6a749-58df-32de-82fd-e835ca46fdb2 | -8.0005 | -45.6864 | 2025-09-16 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 82d09979-5c2a-3bdf-93c7-dac862c62203 | -9.1706 | -47.0014 | 2025-09-16 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 07603d2e-8ef7-32fb-8dfd-c421fbe99e18 | -6.1878 | -41.2097 | 2025-09-16 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |


[Clique aqui para ver as próximas entradas](README93.md)
