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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28e67f1e-7ac3-30ff-b471-58f5f5d302e2 | -7.3603 | -42.44603 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f99c49fe-3acf-3f7c-be8c-71eb613682d5 | -4.86948 | -48.52755 | 2025-10-27 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 25ce1d05-b9e5-394b-9052-3f9783bc0de5 | -7.84467 | -46.42138 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d93da1d4-6245-35f1-8535-49a691a41267 | -3.4261 | -52.43624 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 536f24ef-db8f-34a9-946b-9be8e269f656 | -7.86987 | -45.72462 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c75738f9-762a-3323-8b0d-499ec4540b78 | -5.57262 | -40.91747 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a2445b07-1441-342e-84cd-1c44dee13b96 | -4.43577 | -43.42867 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdfe03df-c5b4-35a0-8a90-13b7592976a8 | -3.14814 | -50.33401 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d637ff69-4150-344b-b719-1c3bb1c441e8 | -7.25276 | -44.96405 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d85e78a4-20dc-3015-b3ba-2944309a88f7 | -4.38638 | -43.32373 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef6adc3-43cb-323d-86c8-449a79c6b551 | -9.99109 | -47.16378 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e66ebce-6abf-309e-adfe-ae160122a90f | -2.81604 | -49.12997 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b84073de-e464-3c07-927a-0f6d2ceed2ab | -7.83692 | -46.47223 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 48414b14-57d8-3be6-a9bf-459ffac40ae9 | -2.77486 | -54.57479 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e6805b9-8153-35f6-9490-bf1a036944cc | -7.86581 | -42.86302 | 2025-10-27 04:32:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e71582c-9d96-38f9-b7fc-60ac0f95dec0 | -9.82671 | -46.92718 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cc86900-3fcd-3b90-830c-c40b7f30ecc9 | -3.24385 | -50.6469 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 876259e5-1d0a-3fbb-8238-eec69e845367 | -3.11867 | -51.20887 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53083c24-04bf-3091-ac19-d10b664f09a9 | -9.99116 | -47.18596 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3145606-3b38-3783-9928-63c25a4f1607 | -3.75696 | -51.75485 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a370d355-d6b4-3309-b2a0-884b214f0adb | -4.39015 | -43.32432 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7fb31db7-b6e9-3e02-bc6b-be95b3464c4b | -1.34931 | -53.48685 | 2025-10-27 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01f0410b-8675-3ba0-acfa-309af9bde18b | -7.97723 | -45.47281 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d7b1f083-df59-3b64-95c0-9eaad0a9d0f3 | -4.34309 | -49.88244 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9d491d5-e024-35ff-a524-0034b367e907 | -3.05246 | -53.02498 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c0babc7-2d65-3972-a5a0-3abe73de7fbb | -4.46928 | -43.41745 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98ac55a2-62fe-3b40-b74c-2017ca344269 | -4.22346 | -48.35291 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e57fd65-c8f9-33f1-a5ae-b8a64c7f4e20 | -7.68454 | -46.34081 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3ef0cb0-f3c0-38e5-8f01-998a62d84eb6 | -7.06583 | -46.75749 | 2025-10-27 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7fcb398e-bd11-3b05-9bba-d9eab4d30c0b | -4.72733 | -46.8119 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f28ebc73-70a7-31db-b465-b2cf6ce81e9f | -4.47542 | -43.4277 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5191b47f-28a9-3651-810b-094f2ced0d61 | -8.11611 | -48.8122 | 2025-10-27 04:32:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae622d79-88c8-359e-b046-ff82e47db346 | -6.4436 | -42.34461 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d9720d72-4489-33d0-ac20-3899231de2fe | -7.78161 | -45.37655 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfe3ae88-24ad-358c-a850-8923eb18113b | -2.81303 | -49.14882 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d90cffde-5542-3f93-a3cd-81bc8f0c4009 | -7.85265 | -46.45976 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 868d1834-6aba-3e42-9643-eabda8de8e28 | -4.89048 | -48.65404 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaeb01a5-a273-3c63-b04b-01b27f898d5b | -5.77233 | -39.62755 | 2025-10-27 04:32:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f20adb9-9239-3c42-a9c0-cc1dbe90ec36 | -3.57145 | -49.01736 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f6a448-ffcb-32f9-8fc8-238f15da96ab | -7.92065 | -45.66072 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36965c88-1019-3197-bbcb-b46009cd1457 | -8.12876 | -47.03122 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08113ad3-19f4-3551-bc97-153bcebea1eb | -4.60386 | -48.78394 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c6dc89c-9cab-3bb8-8f57-67d875952581 | -9.26154 | -45.5739 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9fe0052c-326a-3e42-aab0-03b326ae390f | -4.45069 | -45.46348 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53a97f45-6211-3bae-8166-b58e2a3c8b9e | -7.2498 | -44.95938 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db9fa713-951e-38c0-9270-1c7bf0755667 | -7.83243 | -46.47897 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a1c2decb-bcd4-3847-9a63-8a68bae39ba8 | -9.52553 | -40.30405 | 2025-10-27 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6b470eb4-4121-332d-9925-21bf258a3782 | -9.52699 | -45.81092 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af68f65a-4118-34e9-b7e6-8494f9f7a527 | -8.09686 | -46.94993 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdb8cb34-7449-3e78-b9cf-415cfcb2ca55 | -3.14775 | -50.45135 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f2eb306-cbe3-3560-9e1a-b2537e818f7c | -5.81913 | -40.82887 | 2025-10-27 04:32:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c03ff02-0613-3128-a831-674563022511 | -4.36784 | -46.80515 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2942a61e-8ebb-3886-bf05-7d24348de03e | -4.32006 | -48.08538 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d606f07-e206-361f-a986-a994239ae125 | -6.3096 | -44.74163 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0c197f0-2458-34f8-8600-3a8399969b9d | -8.04635 | -45.15537 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 622e45d6-c492-34c5-b498-c331c5742a84 | -4.44677 | -43.41408 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e0f5ebe-dae1-380b-96e4-712303f5139d | -5.01605 | -41.03702 | 2025-10-27 04:32:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3fc0200d-303e-3dd5-a716-5373303500f5 | -4.87376 | -48.6514 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf10930-eec2-377b-ba74-2e4239f64175 | -4.21347 | -48.3513 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc8a83d0-de74-30b7-a09a-2a004cb67eff | -7.76813 | -45.39453 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a330ec87-164c-31c9-9928-bbedc2ff1e8b | -8.87946 | -44.83665 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a012cad8-28c0-324e-8b5f-ae78540be536 | -6.45057 | -42.34585 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49ad8188-3e28-3c25-b81c-7543d73f7b83 | -9.71865 | -48.92356 | 2025-10-27 04:32:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f06cb0c3-2288-39da-b832-2d4b9364d0ee | -7.8986 | -47.24398 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0b4f72d-6c06-33f5-a3b4-7ddc022eb122 | -2.90209 | -53.134 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ddf0ac5f-1912-3e3b-b99a-4babc58ebc25 | -3.79469 | -51.34885 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4270fb6-b022-3909-8814-d180562f289a | -7.05428 | -47.03006 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 490240eb-4a84-393b-a040-51d18f4a3931 | -3.98203 | -49.28606 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b06e9ec-15b4-3e28-b8bf-a9ba0285cd0d | -3.04671 | -53.01668 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 086ed9e8-ce30-3db7-b050-ca164aea175f | -7.24826 | -46.96318 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a49d3fcf-bd1a-358a-9072-891965b5af8a | -6.09894 | -41.78093 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9bea75f-625d-3ea4-88b0-e1c31897173e | -6.12037 | -41.71768 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 906d8f39-c849-316e-8205-faa7f67cec59 | -6.69101 | -42.04871 | 2025-10-27 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9fcbc910-8566-3711-8c2d-2e67eb399a4d | -7.68779 | -42.18114 | 2025-10-27 04:32:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 79fabd60-f8e5-3a06-827f-15fecd47101e | -3.55527 | -49.49598 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2871adc-06cc-3d42-a5c3-4425b05af23c | -6.88858 | -45.1485 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2669a7ea-cd80-3e66-b9fb-37a15aeab8a9 | -2.69191 | -48.4553 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 703f20de-cc02-31f1-864e-837a85c0c78f | -4.45183 | -43.66098 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f03bd8bb-5775-3326-ba53-a5d7e48e6428 | -5.72035 | -49.31607 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ad4ca1a-42c5-3228-8048-3e617a8c6725 | -2.97523 | -51.03563 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 439eb4ce-fe1a-3c5d-bbbc-6574f5739c77 | -9.97737 | -45.67427 | 2025-10-27 04:32:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ca9ee54-746b-30eb-a570-0e9bf5b1c693 | -3.09982 | -49.44239 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77b8e8d4-d890-3922-9d90-3f630b027477 | -7.33485 | -42.44609 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9fae1e0-0ebd-3ea6-a7a3-e1ffd438ee29 | -6.26004 | -41.83075 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 094e6d6b-e3ad-3b64-83ab-856d175d5d0a | -7.86036 | -45.38312 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42207100-4e43-375f-b878-e8e49f105dba | -2.27361 | -47.85229 | 2025-10-27 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aedc89e8-ddea-3115-9f08-6c59e5ce86f4 | -4.45807 | -45.46087 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85a4493a-7031-335f-bf1a-d41f0632d969 | -3.07761 | -51.2702 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abb1fdcc-7bb7-3805-9290-af854ec2f1a2 | -2.4442 | -48.99556 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f3a321-45c4-347b-b14a-f040f550bb84 | -6.15778 | -43.12965 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f8c7859-0ec4-345c-9b3d-0c1fbfa19216 | -8.02766 | -46.75969 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7ba5bfb3-4590-3e74-aad3-d95b84bf00d3 | -8.14229 | -43.41018 | 2025-10-27 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 44f4251e-1bdd-3cce-98a8-ad2fdec38d02 | -6.17583 | -43.74224 | 2025-10-27 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 245dbe1f-b32a-39bc-a2dc-6d4f74734423 | -4.20958 | -48.35429 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db3ddbf2-0541-3658-9b07-ebd06eb32d4e | -7.85479 | -46.40043 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff52b3c1-d0fc-3746-99e5-22ebf4a9c677 | -4.35311 | -50.70243 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045eb19e-42bb-3191-819c-eeca912245ef | -7.94618 | -47.24419 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6e61c1e-07dd-3d0f-88f1-c8a8c6bc258a | -7.43302 | -41.87818 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 88d38b5f-f283-3af7-990b-a7e212030838 | -9.99054 | -47.1674 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78751317-8b19-3bc4-880f-5218ed51a6d4 | -10.29984 | -44.11073 | 2025-10-27 04:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
