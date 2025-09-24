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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e2edab-c62a-3bdc-8760-da175dfb0246 | -11.4037 | -44.959 | 2025-09-24 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9e26857f-5999-3189-b3f2-920ce4c53feb | -6.1992 | -45.7961 | 2025-09-24 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 75bc71bb-5484-3bb6-bb46-b9b1f669d3ca | -11.6822 | -44.361 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 1202fb7d-56ce-3c5e-b006-63987b953d9a | -11.5037 | -43.6373 | 2025-09-24 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3d480db0-db18-3474-8571-9e50385e0c4a | -11.6822 | -44.361 | 2025-09-24 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 9ae18405-41d4-3ba5-9fc3-9b15b78d84a7 | -4.7974 | -43.5435 | 2025-09-24 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4c6d8fdc-5519-3f05-aba1-98a8281defed | -20.5445 | -57.1224 | 2025-09-24 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f91383d4-243d-3588-888a-4f45ab9ad288 | -11.5032 | -43.661 | 2025-09-24 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 4f12b583-b2c9-3dfd-8631-24b11e759d0d | -6.2179 | -45.7947 | 2025-09-24 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 90fbe199-cacc-34f5-b424-631023a8bfd9 | -11.4233 | -44.9331 | 2025-09-24 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 30e5cf8a-5912-32c8-a770-f2ad9c65ee12 | -10.3755 | -46.1015 | 2025-09-24 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2b9bc249-9f7b-3daa-ae7e-e500557b5efb | -5.1651 | -42.0614 | 2025-09-24 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| 85ae95de-9f55-38e0-bc8a-e0b1b2123a14 | -3.8651 | -40.3596 | 2025-09-24 14:10:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 40d98bba-9f3e-367e-88ba-aff6f274a79d | -17.9506 | -55.8731 | 2025-09-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 0ca74928-4080-3ac0-8758-300c51ba42a4 | -11.4041 | -44.9359 | 2025-09-24 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d5984181-ad4a-320f-b348-3892566b6339 | -11.6634 | -44.3405 | 2025-09-24 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 1846624e-72e4-3670-a22d-8e4c1c022b97 | -11.6446 | -44.32 | 2025-09-24 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 689459a6-be62-382a-a8e9-fd7191bb1ebe | -17.951 | -55.8522 | 2025-09-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| dbede914-6c00-388a-8376-015cc068b09e | -9.8439 | -46.143 | 2025-09-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 68a8890f-8f2d-3610-9be5-4aa2da045913 | -11.663 | -44.3639 | 2025-09-24 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a42c49f5-e47e-370b-8378-bbc780cabdbe | -8.3139 | -46.2183 | 2025-09-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 24c67fc5-47b2-3ece-ad00-c20e8cea5b9a | -11.6461 | -45.3158 | 2025-09-24 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 8bbd1934-6b60-3439-9380-ae530657b129 | -6.1992 | -45.7961 | 2025-09-24 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1019c8d8-3aa7-3da9-9c31-55e25586bc27 | -11.4229 | -44.9563 | 2025-09-24 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 242e7a02-aaad-3ce2-b36e-f7babc699029 | -3.7814 | -41.7196 | 2025-09-24 14:10:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 240.6 |
| a4c0ee5c-ea9b-3c59-b89f-420720207c45 | -11.0253 | -45.9046 | 2025-09-24 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1db58e1a-7f34-3964-ab70-2a2fe8931f51 | -3.8001 | -41.7186 | 2025-09-24 14:10:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 559978a2-52ab-3f30-a94b-78e6c518ef44 | -11.4037 | -44.959 | 2025-09-24 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2c8664f1-76d4-36a2-bb03-bbcd12abca7c | -11.6438 | -44.3668 | 2025-09-24 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 2a884a8f-198e-3671-82e0-cf8717f1e9d3 | -5.8088 | -43.4724 | 2025-09-24 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 5159b6e8-5833-36fb-a9b4-fb3a540035d6 | -11.6442 | -44.3434 | 2025-09-24 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 29ddde02-7551-3518-8a6a-907bbea3786b | -8.8417 | -46.187 | 2025-09-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 322a2270-4377-3116-8d61-24329e4e8ff9 | -9.825 | -46.1453 | 2025-09-24 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a0f49208-8423-303a-ad8b-1db34d2719fe | -11.4233 | -44.9331 | 2025-09-24 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| fad7efb9-4f5c-3082-b1e3-fb016fe962e4 | -11.4037 | -44.959 | 2025-09-24 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 0e9de210-7855-3e49-a722-7c907637dd2d | -3.8001 | -41.7186 | 2025-09-24 14:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 200.0 |
| bab59bb4-36a5-313b-89c2-d3cb0dff3cce | -20.5445 | -57.1224 | 2025-09-24 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 194.6 |
| ce2d4741-6e3b-36e0-b9d2-ae69b779f26a | -10.3755 | -46.1015 | 2025-09-24 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1bd012de-efb9-3cfb-acf2-c81e3cceaf97 | -11.0444 | -45.9021 | 2025-09-24 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 7c648dd4-9d1e-3091-bd66-c743efc50848 | -20.5652 | -57.0984 | 2025-09-24 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 268ff2cc-759a-3fd9-b5d5-4f834673f5c0 | -11.044 | -45.9249 | 2025-09-24 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f228eeec-c27b-38b4-9f26-ad62fa514e4c | -3.6241 | -43.0042 | 2025-09-24 14:20:00 | GOES-19 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3c822532-5100-3055-9491-6c3c977feadd | -5.5243 | -43.8647 | 2025-09-24 14:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4871f227-fde3-3534-bee3-d445b4f616d0 | -9.825 | -46.1453 | 2025-09-24 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ebc0fd4a-c79b-3df6-a4b5-275bfd9cbd0c | -9.5787 | -47.534 | 2025-09-24 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 64c70506-e145-3b8a-9250-9946cf3a6b65 | -12.8879 | -44.6378 | 2025-09-24 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 2cd1c398-bfbf-32be-b737-c69368740e9e | -8.8417 | -46.187 | 2025-09-24 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 00f72537-20a8-3c1e-b469-192661595c2d | -10.9541 | -45.5953 | 2025-09-24 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 93169f31-9717-3a69-9903-222e753df271 | -10.3378 | -46.0835 | 2025-09-24 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6f6d8622-0a56-34a6-bcd8-db7f910e530f | -17.951 | -55.8522 | 2025-09-24 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 880cca10-4919-3c52-95c6-f4d13798ccc3 | -8.3139 | -46.2183 | 2025-09-24 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 38df1872-e752-30ad-9dc3-759064ac019e | -10.9732 | -45.5927 | 2025-09-24 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1538e115-a10c-3b7b-80a9-20fb54082949 | -10.3572 | -46.0585 | 2025-09-24 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ddba1cb9-50c1-3405-bf7d-7a364881098d | -11.5225 | -43.658 | 2025-09-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 87140436-ad9e-3b74-9428-87d7136e680a | -11.2306 | -46.1722 | 2025-09-24 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 430e379c-eb21-3f73-b389-6db2b9f1769b | -3.0574 | -44.4148 | 2025-09-24 14:20:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9e787cce-c473-3da0-9cc3-1e8c58e2efdf | -3.7814 | -41.7196 | 2025-09-24 14:20:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 361.5 |
| eca3ad93-2953-3a2b-8d98-2f554d20197b | -4.7337 | -42.0914 | 2025-09-24 14:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 175.5 |
| e7711390-f5b1-33d1-9bfa-cf0531be18d8 | -17.9506 | -55.8731 | 2025-09-24 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| fea48496-30f6-3fca-a529-591b04a4391e | -4.7974 | -43.5435 | 2025-09-24 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 719967d7-e3f2-3557-bd4e-4697e02bc2f8 | -11.0249 | -45.9274 | 2025-09-24 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 09a558fd-085c-3212-91d3-96a05d84cb4f | -10.3568 | -46.0812 | 2025-09-24 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ea9d4367-ba21-33c6-a9d9-2632a8bfb7fc | -8.4939 | -46.8924 | 2025-09-24 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 5a1ec22f-dd36-3559-b541-749acbee4fe9 | -9.0472 | -44.9395 | 2025-09-24 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fdbdfe0c-90f2-3848-a47a-122ec8d858df | -3.8651 | -40.3596 | 2025-09-24 14:20:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 120.4 |
| dddc571b-b329-3970-9c62-15bd2c75a7b7 | -9.5784 | -47.5561 | 2025-09-24 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| b1b8fab2-0770-3c52-b5f5-3477468489b6 | -11.5037 | -43.6373 | 2025-09-24 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 939631d3-42ac-35c2-8d6c-b5fe4df54ef5 | -20.5648 | -57.1194 | 2025-09-24 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 744fab82-f993-3b59-b712-a6844b031629 | -9.8439 | -46.143 | 2025-09-24 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| bbae7a95-3905-3782-a109-4bec4cba0979 | -12.3184 | -44.2154 | 2025-09-24 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 0c9088fb-cd65-3fbb-ab67-20989eda0048 | -11.4233 | -44.9331 | 2025-09-24 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c220f8b9-6578-3b04-a087-e841279877e0 | -4.7974 | -43.5435 | 2025-09-24 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 77f7e816-e8ec-3ab6-9e86-02545c53d67a | -3.8001 | -41.7186 | 2025-09-24 14:30:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 337.8 |
| 4b9a2e4e-ba8d-3866-8317-f95983d33fcf | -11.6446 | -44.32 | 2025-09-24 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 9de40528-ece3-3b94-bbb3-69e9bf3a6bab | -10.9541 | -45.5953 | 2025-09-24 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3f7dbbd7-530d-31ee-933a-f1f292c76a5e | -6.1415 | -45.9797 | 2025-09-24 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 49b60261-fa44-3538-bdb8-d7178d8f2630 | -11.6442 | -44.3434 | 2025-09-24 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 868da673-d6be-3af9-95aa-8219633c6325 | -9.5784 | -47.5561 | 2025-09-24 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 22b7ee30-b342-3333-a178-29c6478b37b8 | -20.5648 | -57.1194 | 2025-09-24 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c3185c1a-a6c1-36fd-8f9c-0a3d3e732760 | -8.4941 | -46.8702 | 2025-09-24 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 65768c99-1c73-37da-a18c-cd780bcc034c | -17.951 | -55.8522 | 2025-09-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 06e1e6b0-dfe4-3b66-8614-3aa5480cc69c | -17.9506 | -55.8731 | 2025-09-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 87363914-3c6a-3435-891c-44513bb8aaa2 | -3.0574 | -44.4148 | 2025-09-24 14:30:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 9e0c414a-ee3f-33d7-8220-5154b99fdd15 | -20.5445 | -57.1224 | 2025-09-24 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 128.2 |
| ba84bc4f-85d0-378c-a76d-746efe8b380e | -11.5037 | -43.6373 | 2025-09-24 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| aa77fc30-61e2-3141-9d37-007d6cef9a39 | -4.7623 | -43.2434 | 2025-09-24 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 8fe22ff2-bbb7-330c-b189-ba2b01d6c883 | -11.6438 | -44.3668 | 2025-09-24 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 271.4 |
| 65e7f3bf-e899-3010-82cb-b3f154d7aa3f | -3.1765 | -42.9313 | 2025-09-24 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| ffecc10d-345b-3900-aeb9-41d77c1a06b4 | -6.9024 | -44.7656 | 2025-09-24 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c1b53214-97f6-36fd-9798-8dfd6ead0052 | -9.9555 | -46.2876 | 2025-09-24 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 83bef326-f528-3f70-ac5a-3a3a5a305600 | -11.6634 | -44.3405 | 2025-09-24 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| ae5963f6-1dda-3107-9a91-c0e440238207 | -3.7814 | -41.7196 | 2025-09-24 14:30:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 502.1 |
| 271b3066-a068-3c44-980c-7cf093080068 | -11.663 | -44.3639 | 2025-09-24 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| f18bc976-c549-3b20-ac24-4ba9ecabbc5d | -8.8417 | -46.187 | 2025-09-24 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 84433eb0-edd7-3e66-a186-385428561747 | -3.6241 | -43.0042 | 2025-09-24 14:30:00 | GOES-19 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 091e8452-3d86-3ceb-8e51-e22581dc73c0 | -11.7014 | -44.3581 | 2025-09-24 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 2e587810-40cf-3b4c-b2e7-1f11d71e33d6 | -11.0253 | -45.9046 | 2025-09-24 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| bdc056f1-adf2-3871-8286-b63cd7870bad | -10.9732 | -45.5927 | 2025-09-24 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 93004d45-c2c4-3765-87a9-e575daf1982b | -10.0317 | -46.2561 | 2025-09-24 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9c68391d-759c-326a-bdab-65a545643c24 | -6.1415 | -45.9797 | 2025-09-24 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |


[Clique aqui para ver as próximas entradas](README25.md)
