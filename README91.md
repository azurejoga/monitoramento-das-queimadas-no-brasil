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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46f931ed-61a8-336a-9dcb-06f9a37e4bcf | -13.2801 | -54.2228 | 2025-09-16 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 36e1d438-6b02-3b2b-9156-c009a01804f1 | -8.0196 | -45.662 | 2025-09-16 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 853.2 |
| 59c2efe7-e428-3132-acfe-06df21a40eae | -11.4853 | -43.5929 | 2025-09-16 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 6cf41b7e-376a-38a8-b15b-f3221c4b4f2e | -3.8416 | -44.0824 | 2025-09-16 12:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 210.7 |
| d58dee40-e472-337f-9e22-268c1b28eeb8 | -8.9259 | -45.5231 | 2025-09-16 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 48e2be8a-3987-370f-a43c-a3aa26bad028 | -9.5309 | -45.523 | 2025-09-16 12:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f2b9386d-2918-3071-a4aa-283afa3ca3a9 | -11.5041 | -43.6136 | 2025-09-16 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e55831ba-d404-3826-ae9f-3ffcb1e64838 | -6.356 | -43.1476 | 2025-09-16 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 20e49ed2-0801-32aa-843b-c714e87432bc | -10.7302 | -46.5082 | 2025-09-16 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| ae4e69c6-f890-3817-874d-1a52772d0c49 | -11.4849 | -43.6166 | 2025-09-16 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8c31b78d-304e-3dbb-9f6e-20b6f8b4ad1e | -12.6356 | -45.7422 | 2025-09-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c71174ca-f71b-32d4-9f7c-380a5f8d6719 | -3.8228 | -44.1063 | 2025-09-16 12:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a00f195f-c173-3feb-93e4-a801df7f9350 | -4.5934 | -43.3239 | 2025-09-16 12:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| d819a7fe-e412-3bb5-a75b-f61bf436cf30 | -12.6356 | -45.7422 | 2025-09-16 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ef42fd1c-a90e-34c6-827b-93e198cdb707 | -3.8229 | -44.0833 | 2025-09-16 12:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 95fff96b-3116-3aa2-a40d-5a2ecb07ee7c | -8.9176 | -46.1565 | 2025-09-16 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ff306b0f-7a62-3890-b370-15f50c9e7abb | -13.2031 | -47.29 | 2025-09-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3f30fda3-f73c-313b-afd0-76606b42afb1 | -9.5309 | -45.523 | 2025-09-16 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 203ad86d-d5d8-3f31-a969-de217b2255aa | -3.8416 | -44.0824 | 2025-09-16 12:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 312.4 |
| cbcd2610-7dae-3bb9-b273-ec673efb0b34 | -11.5041 | -43.6136 | 2025-09-16 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 538353c0-ab67-33fb-a6bc-681afb353788 | -6.3558 | -43.1711 | 2025-09-16 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 40527427-1f7f-3efd-9610-da1b51f09b37 | -13.2801 | -54.2228 | 2025-09-16 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 8f8a6601-b5d3-384e-bed0-d61264d0eda2 | -8.8795 | -46.183 | 2025-09-16 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 350efbed-7eba-3732-99ba-f6dd99e98ab2 | -12.6906 | -48.0121 | 2025-09-16 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 457ee4f2-d5a8-332e-aa11-7e8adbeb25ab | -8.917 | -46.2015 | 2025-09-16 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8dcda250-1a51-31b1-a637-9c0582dd7f87 | -10.7302 | -46.5082 | 2025-09-16 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 57cc57b4-5825-3de2-851d-fbcc976af767 | -13.2027 | -47.3126 | 2025-09-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2c593a86-068a-3ed6-8d14-5b599fc95544 | -8.0196 | -45.662 | 2025-09-16 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 791.4 |
| 6085bca1-2d15-3b38-87da-7eaa7efba743 | -10.6548 | -46.4727 | 2025-09-16 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| c3d68253-e3cb-31c9-9ae8-66f2f1a95e8a | -11.4849 | -43.6166 | 2025-09-16 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f403d000-6f68-30e9-bf3b-483319e99676 | -8.6319 | -46.3881 | 2025-09-16 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 28c7813d-2abd-308a-bd59-d7d291de2f21 | -12.6352 | -45.7652 | 2025-09-16 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 329.6 |
| 76d387c6-c070-3da8-b309-ef412bdfe967 | -8.613 | -46.39 | 2025-09-16 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| aebd97f0-6122-3257-85cf-7e703af61399 | -7.6949 | -44.486 | 2025-09-16 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 612c5715-fee3-3e73-84d9-852ced7b3488 | -8.001 | -45.6412 | 2025-09-16 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ca108891-be4e-30f0-91cf-7c29f0fb2b02 | -12.8392 | -47.2093 | 2025-09-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 583b84c9-8a37-3467-a516-7bcc5e4c7e9f | -7.9822 | -45.643 | 2025-09-16 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 032d7be8-2fb0-3043-b9ff-a89c5e50a08a | -8.9592 | -45.8591 | 2025-09-16 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f24165ad-57a5-30f8-bb9c-978e2b8b65f4 | -11.4853 | -43.5929 | 2025-09-16 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 576f83a1-a905-3231-9e9d-557756389c17 | -5.8086 | -43.4956 | 2025-09-16 12:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| afd6bbed-b373-3b94-8cf7-f336eb5c0550 | -8.5939 | -46.4143 | 2025-09-16 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4b57987d-e41a-3d73-bdc9-51601dbca9fc | -13.222 | -47.3097 | 2025-09-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 93a6bae7-c6d7-34b9-b369-dcdcf8b4f72b | -8.6127 | -46.4124 | 2025-09-16 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 199.3 |
| a1a559fc-086a-36ae-b04e-e093137b9e5b | -8.0007 | -45.6638 | 2025-09-16 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 335.5 |
| 4acc0029-12e5-3cf1-a51a-8ecbf11903e5 | -7.078 | -44.153 | 2025-09-16 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 20958e80-6f5c-34ed-9892-cb2df5d2a997 | -6.3372 | -43.1492 | 2025-09-16 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6dd33d94-b05d-3410-a280-20697eab5d57 | -6.356 | -43.1476 | 2025-09-16 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 38c624b3-ff07-3485-ac12-e36146558d64 | -12.6909 | -47.9899 | 2025-09-16 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| c93c6cd9-cb36-3007-b909-1bca18543776 | -11.4853 | -43.5929 | 2025-09-16 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 38751b0b-cc87-3ab8-bdb1-37aa8c2eca09 | -4.6123 | -43.2994 | 2025-09-16 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 503e7a52-c6b7-314c-a892-abe931ef347e | -12.6356 | -45.7422 | 2025-09-16 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 88be0344-0f81-3017-b653-ad3a2fce7d37 | -8.0007 | -45.6638 | 2025-09-16 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 299.6 |
| 9af98fe7-6e3b-3cca-b0f0-8e0e3a4fb2da | -10.7299 | -46.5307 | 2025-09-16 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 244.3 |
| ce224902-190c-37d4-97de-aa1b1d0c3589 | -5.8088 | -43.4724 | 2025-09-16 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 5953d7d3-b028-3db7-8032-374f62fc7568 | -3.8416 | -44.0824 | 2025-09-16 12:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 567.2 |
| 34a5ea5e-a73c-3829-9d9d-1432010c5cde | -12.6352 | -45.7652 | 2025-09-16 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 5bf5978d-e771-39b2-a391-6162005beef6 | -10.7302 | -46.5082 | 2025-09-16 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 703ee1dc-6894-3dcf-8eec-e1b49d08aa07 | -10.6548 | -46.4727 | 2025-09-16 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 324.8 |
| bd8a1e43-6573-32e8-bbb8-f6de5ee667a2 | -8.0005 | -45.6864 | 2025-09-16 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 67be9f79-2d10-3d98-a604-8c13bedd6f89 | -9.1709 | -46.9792 | 2025-09-16 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 86e5ffd2-ce6b-3ba6-861b-6287b5c063d6 | -9.7126 | -47.4089 | 2025-09-16 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 37a1a79a-0617-339f-948b-5c218fc505d5 | -10.7493 | -46.5058 | 2025-09-16 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4a56ad9b-8999-3911-b51c-126c6de0e993 | -8.613 | -46.39 | 2025-09-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 97590384-96d2-3a79-a39d-ffc124516197 | -13.2801 | -54.2228 | 2025-09-16 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 73fd8a77-4811-3317-83e8-c54cd83233bb | -8.6319 | -46.3881 | 2025-09-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 4a83ce4d-b247-3d8a-a1e5-0a33a73f1835 | -4.5934 | -43.3239 | 2025-09-16 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a90191b3-d764-36e8-8bf8-ec25536e7712 | -6.1878 | -41.2097 | 2025-09-16 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 40c57d6b-ac5a-35b9-978f-6b09e0c649c4 | -7.9822 | -45.643 | 2025-09-16 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 5297b344-3518-3811-834d-cb9774dd883a | -8.0196 | -45.662 | 2025-09-16 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 912.4 |
| bc85d7ef-7358-3a55-9843-3755381afff8 | -10.6551 | -46.4501 | 2025-09-16 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f04c5bb2-2cb4-350a-acc8-137c62bb5c9c | -6.337 | -43.1727 | 2025-09-16 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4154ac1a-1fdd-37b6-bdc5-6585db5fcdb7 | -13.2027 | -47.3126 | 2025-09-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2a254b9b-6c26-3cf7-89bd-fa34fbb90bee | -7.4503 | -46.1647 | 2025-09-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e373cf76-96f0-30cd-a7a5-25a0533ff4bc | -7.2768 | -46.6036 | 2025-09-16 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 261a0dec-7f1d-3454-a944-848f30981145 | -8.6127 | -46.4124 | 2025-09-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 318.4 |
| 9bd7fafa-a312-357c-84ca-a7f23e319069 | -7.6949 | -44.486 | 2025-09-16 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 675b2e95-64a1-3875-81e9-030f199ec3d3 | -6.3558 | -43.1711 | 2025-09-16 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 0af84e85-f9ce-3e32-b811-75248ff9d293 | -6.3372 | -43.1492 | 2025-09-16 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| cf84cc6b-9c10-375e-8cc9-73d735fe1b87 | -10.7489 | -46.5283 | 2025-09-16 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0c0558c7-8110-3ae8-aa2b-86a7ac909e64 | -6.356 | -43.1476 | 2025-09-16 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 167.2 |
| be3ba64f-fe90-329a-a6f1-e565ac0b5bc4 | -5.8086 | -43.4956 | 2025-09-16 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 627673d2-090b-3f95-8532-7b94a628bc75 | -4.5936 | -43.3006 | 2025-09-16 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ee63bd6f-c250-3217-bf8b-deec53b1a61c | -9.7677 | -40.0698 | 2025-09-16 12:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.9 |
| e440608f-e13c-3275-a5c4-06947b5474d8 | -8.001 | -45.6412 | 2025-09-16 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 395bb3a2-7843-3407-be19-2cfb032b4f61 | -11.4849 | -43.6166 | 2025-09-16 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 06ead433-ca28-35fb-9be3-708e763306da | -3.8229 | -44.0833 | 2025-09-16 12:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| a9c6bf07-8a6f-3fa1-99a7-36ff5f49144e | -8.6124 | -46.4348 | 2025-09-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2da5c44b-cbf3-365b-8910-168d95d97d27 | -8.5939 | -46.4143 | 2025-09-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 264b9cd0-5e88-39b6-b1c3-c9a225e4fed3 | -7.1505 | -47.9786 | 2025-09-16 13:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 52dba285-08ac-3bd0-a212-158483972ebe | -9.0857 | -44.8893 | 2025-09-16 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 37d591db-ea3f-34a4-a9f6-c30f7abc15c3 | -6.4633 | -43.6749 | 2025-09-16 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 19f98d1a-7c56-3578-9a1c-0ca8f4b511a0 | -13.2801 | -54.2228 | 2025-09-16 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 161.0 |
| b04c08f5-b690-306c-86bd-f7f8f6824f45 | -8.0005 | -45.6864 | 2025-09-16 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 564ebda4-0366-31df-b5c1-7d6db7a8c0ec | -6.356 | -43.1476 | 2025-09-16 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 231.4 |
| 3e7a32c1-721d-3f2f-b7fb-d45ea1c8dabe | -6.3558 | -43.1711 | 2025-09-16 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| e9d4ba01-b87e-3a6a-8475-870f17625c5f | -8.6127 | -46.4124 | 2025-09-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 2b721e0c-7427-3d5c-8293-380999f8b798 | -11.4849 | -43.6166 | 2025-09-16 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b673fc74-1497-336b-89e1-f5bcf686dbc3 | -8.001 | -45.6412 | 2025-09-16 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b8508e30-6a1e-389b-bb21-bc26121e4b71 | -7.2771 | -46.5814 | 2025-09-16 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 33bf674e-b879-3d05-a141-7d2587d7f4fd | -3.8229 | -44.0833 | 2025-09-16 13:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 211.8 |


[Clique aqui para ver as próximas entradas](README92.md)
