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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91e06e09-1a73-38f6-9bd0-6e01375467fe | -9.212 | -45.3321 | 2026-06-24 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 93b41942-d988-3a6e-898c-ac9e87319b97 | -6.5924 | -43.8957 | 2026-06-24 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| b51f9a2f-9a0c-3512-8c8f-5c88b8eb9c69 | -11.2407 | -43.3464 | 2026-06-24 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 02eb6f3c-919a-32b0-b4c9-a04e36bb5650 | -12.7958 | -44.4191 | 2026-06-24 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| fd083540-4a6a-3f32-b2ae-12f6b68fd5f0 | -13.0635 | -53.3546 | 2026-06-24 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 235.6 |
| c6e07cab-95c7-3efc-abd3-55ae36bdf760 | -5.8132 | -45.0573 | 2026-06-24 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1be60853-34e1-3802-ac0d-88e95431d543 | -6.5922 | -43.9189 | 2026-06-24 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9df9e6f8-d84a-3c3d-901c-72090c6e5993 | -13.0827 | -53.3524 | 2026-06-24 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7b3543e8-4712-317c-9f7d-3edbf6e9a2c4 | -12.7953 | -44.4426 | 2026-06-24 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3979a976-e662-31d7-a0e2-76d446d61002 | -12.776 | -44.4458 | 2026-06-24 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 6e826f6b-d6a6-30c5-9928-7539ab36bb3e | -6.3703 | -43.5898 | 2026-06-24 00:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2b4cacff-e521-3514-b48b-243a45e1c075 | -11.2599 | -43.3434 | 2026-06-24 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 9ce1169c-195b-33a9-970a-12bde8d2160a | -13.0638 | -53.3337 | 2026-06-24 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c77b0dd8-ae55-3fc5-992a-cea703332074 | -12.7764 | -44.4223 | 2026-06-24 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 69ebd650-d247-3e03-9e96-c1811c131815 | -11.2407 | -43.3464 | 2026-06-24 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 08613514-c029-3e0e-b3ac-7cb82eca6a9e | -5.8132 | -45.0573 | 2026-06-24 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b34646b7-14bc-3fd1-bc2d-07bdf3688893 | -11.2599 | -43.3434 | 2026-06-24 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |
| d89e57ab-6498-3f61-b00f-7fc35ecc925e | -13.0632 | -53.3754 | 2026-06-24 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 23005ff5-835c-36e5-b859-667685a7c19b | -13.0635 | -53.3546 | 2026-06-24 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 179.1 |
| eaac37ae-e0c3-3c59-ae6d-aa4b8c143557 | -11.2403 | -43.3701 | 2026-06-24 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 4635cdaa-fb00-3869-880d-87ba00ec3bf1 | -12.7953 | -44.4426 | 2026-06-24 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| bf759310-8285-31da-b330-f62962c250dd | -13.0827 | -53.3524 | 2026-06-24 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 596c0221-3120-36a6-88ae-68fa9c46b924 | -6.5922 | -43.9189 | 2026-06-24 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c50602d1-2fad-31db-9042-20594337aa65 | -6.3703 | -43.5898 | 2026-06-24 00:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2a547a4e-f1a2-393d-be52-26bf04c34f0d | -6.5924 | -43.8957 | 2026-06-24 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 14865fc2-36b9-3843-a8b2-1472236f1cfc | -12.776 | -44.4458 | 2026-06-24 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 25becb7d-4ce9-39eb-8d84-b04f27d5a4f1 | -12.7958 | -44.4191 | 2026-06-24 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 90324ab9-a87a-3737-95d7-b6be7e8fab1f | -17.2887 | -47.026299 | 2026-06-24 00:16:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1982179d-49f3-3fd1-b7a5-e3cc5ccd0f04 | -11.9455 | -46.474701 | 2026-06-24 00:16:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34e8eb8a-79f6-350a-9809-497409f4f56f | -11.9677 | -49.227699 | 2026-06-24 00:16:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2421ade-dbb1-300d-8b5e-131673cb6a76 | -17.614901 | -46.689899 | 2026-06-24 00:16:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84655a0e-5f76-314b-8e41-876ffd7f3c39 | -7.2849 | -46.239799 | 2026-06-24 00:16:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6914bb92-272f-3b56-ab75-d575338c90c6 | -11.2546 | -43.3461 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d6e61a50-8a1f-34ef-926b-81ab8e6d5673 | -9.2138 | -47.915298 | 2026-06-24 00:16:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78f64eef-7deb-3ee0-9173-d982fb9807d0 | -9.8029 | -48.909801 | 2026-06-24 00:16:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f233facb-b37a-3f5f-b95b-a65fdf7cab06 | -6.5877 | -43.877602 | 2026-06-24 00:16:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2ca909-febd-31e2-9cfd-be3a5e60cb3f | -12.5138 | -48.265598 | 2026-06-24 00:16:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2db8392-8089-3f2d-9e63-c8c3716670d6 | -12.7822 | -44.433998 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab9d22b-1ab0-3c48-b654-2e0b627e574f | -8.3331 | -50.481998 | 2026-06-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34adddd3-6454-3910-85a1-ad0a846a62c7 | -12.838 | -44.365501 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15e012fa-a0e5-351d-8122-cc8975eb34f6 | -8.5979 | -45.9879 | 2026-06-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54727f8f-7116-34c9-8c4c-50fcab7e2a6d | -9.366 | -50.5401 | 2026-06-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d406d4-7f07-3bff-9152-03ec460faa53 | -8.6077 | -45.9856 | 2026-06-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebf3d815-4c2f-3a4b-b573-f8cfa44b51ba | -7.2872 | -46.249298 | 2026-06-24 00:16:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f59109f-b69b-37d4-a612-adbff46f5901 | -8.6821 | -47.847301 | 2026-06-24 00:16:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 919075d4-a278-300c-8a9c-4d993023f1ff | -8.3505 | -47.131001 | 2026-06-24 00:16:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd1d764-d712-369b-ace7-6cb2f0aceb72 | -8.61 | -45.994999 | 2026-06-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a590924-a0e0-3d78-a653-d5eea669c3a0 | -9.5897 | -49.106602 | 2026-06-24 00:16:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f99214ef-bcde-326e-900b-7675948deff6 | -9.515 | -48.0578 | 2026-06-24 00:16:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a07e0b45-80e3-3406-a9e5-9d6c1b57f330 | -17.261299 | -46.3176 | 2026-06-24 00:16:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57f1afe0-3e5e-36e6-ba5a-9e7757aced44 | -5.831 | -43.470798 | 2026-06-24 00:16:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1caf17b-b978-3777-9bff-edf728d38503 | -11.1928 | -48.5811 | 2026-06-24 00:16:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1d7d9fc-88f6-3b4d-83db-6c1839f60597 | -15.361 | -47.354801 | 2026-06-24 00:16:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fd5a23cd-aaa2-371c-89c5-79ee5c87a218 | -11.5133 | -56.106201 | 2026-06-24 00:16:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 300cbcb1-07ba-3a10-b080-38213af4538c | -13.1256 | -53.511902 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff683b62-fb7a-3657-b554-f3557a6711fa | -6.5943 | -43.9048 | 2026-06-24 00:16:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84861abb-2a88-3018-9657-2ba255f02b4d | -10.109 | -47.5457 | 2026-06-24 00:16:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c486ed3-0af7-3b96-ae69-c2bc99dd4995 | -6.3508 | -43.5784 | 2026-06-24 00:16:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd958797-3038-3a02-929f-6815c18dc79c | -11.6223 | -48.473801 | 2026-06-24 00:16:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59946dd5-0211-378d-9050-624d0cf061b9 | -10.7007 | -49.598 | 2026-06-24 00:16:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 897b2c5b-1c73-331b-9d4f-0ed3375a3e2a | -10.7742 | -54.101501 | 2026-06-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7390db7b-a2cd-3f4d-a338-b6be3b99cab6 | -12.8283 | -44.368 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb87676c-e68a-3aa7-bd69-3b9fcda1fd8b | -9.949 | -49.281101 | 2026-06-24 00:16:00 | METOP-B | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8a0f7cb-a550-34db-bb03-70bf370a7a2c | -9.4627 | -49.821602 | 2026-06-24 00:16:00 | METOP-B | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8e88be-a8b5-3e3e-9c27-780d633e9d29 | -7.2947 | -46.237499 | 2026-06-24 00:16:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 663b59c0-8ef6-3bb1-b674-84e869e47045 | -8.3347 | -50.488899 | 2026-06-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e26415c-3c62-303e-b55f-fba8ecc61536 | -12.8258 | -44.3577 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c18770ef-e041-3210-ad2c-d17a952fc179 | -12.7286 | -49.081699 | 2026-06-24 00:16:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2bc6af0-3c2c-3dc0-b258-f004092b5e39 | -12.8305 | -44.334599 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5122eb2c-68d9-34ed-b84e-ef905c98461d | -11.2449 | -43.348598 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cbe60335-9ba5-3539-9a19-cfe5009f31a1 | -11.3084 | -54.703602 | 2026-06-24 00:16:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77d85584-e1bf-307a-972e-82903674c317 | -7.915 | -48.2798 | 2026-06-24 00:16:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e177fba8-50f0-3d52-a06c-bcaff091eccb | -9.3645 | -50.5331 | 2026-06-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cacece2e-ee65-3274-a562-04542f451b27 | -12.8478 | -44.363098 | 2026-06-24 00:16:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96eda1ae-df16-3d22-8b42-7d5c46bbe038 | -11.2418 | -43.336102 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d651eb9d-d774-308e-813c-041fc0596f27 | -6.5869 | -51.700699 | 2026-06-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5169ab00-1657-3840-aa0c-785ea4a2c991 | -17.791901 | -44.5644 | 2026-06-24 00:16:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b50cd1cf-77ab-35ef-9099-6c56acefcf81 | -9.4406 | -48.859402 | 2026-06-24 00:16:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adad9b89-9386-3f23-81a4-a8e3da093482 | -10.8045 | -48.551701 | 2026-06-24 00:16:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7950d3e-a3d7-3a71-89c5-c89bc0b625eb | -3.8624 | -42.970299 | 2026-06-24 00:16:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5be5d441-fd93-3d13-9c9d-b9f75cdea0f0 | -13.1276 | -53.521599 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d39f8bff-64c9-37e8-aaf4-7473fcbaa287 | -13.0606 | -53.345501 | 2026-06-24 00:16:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d30caf8-727e-374c-bab3-71231d7ad012 | -8.3524 | -47.139301 | 2026-06-24 00:16:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c778ff2-cf13-371c-acfa-d8ea6efd4087 | -11.2387 | -43.323502 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c02cd047-223a-3506-9b70-5337cb2ac952 | -7.364 | -47.016701 | 2026-06-24 00:16:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98c409de-a737-344b-9a86-8431319b8068 | -17.613199 | -46.682499 | 2026-06-24 00:16:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 978c737f-788b-3aae-a6ff-fcaf176ef5b2 | -11.1912 | -48.574001 | 2026-06-24 00:16:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68abd16b-726d-3ddb-8e6b-8adac6ab26e8 | -4.3474 | -47.750099 | 2026-06-24 00:16:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7661406f-a026-39cf-a143-e84f51dfb5e0 | -17.2903 | -47.0336 | 2026-06-24 00:16:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 79330fbb-7ca6-30c7-b3f0-a7efae591d75 | -11.4888 | -46.730099 | 2026-06-24 00:16:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8f0b5d6-2a6c-3af8-94e8-0ec83dfd5806 | -8.6803 | -47.839699 | 2026-06-24 00:16:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a65340d-a392-3f81-b09e-daf4b6cf340c | -11.2515 | -43.333599 | 2026-06-24 00:16:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7ce06e8d-ffce-3ffa-b637-2dcf0249415b | -5.8106 | -45.063599 | 2026-06-24 00:16:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3975c762-fa7f-389a-8064-9ccac14b6e06 | -6.3732 | -44.830299 | 2026-06-24 00:16:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d6fe465-f066-370f-8c5f-19dd53cbe2ee | -9.2171 | -45.3353 | 2026-06-24 00:16:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 776e4dd5-abd1-3ba2-9048-957311b8e3f2 | -17.2596 | -46.310001 | 2026-06-24 00:16:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a11209c3-bd01-3ca5-8d15-8d4ff219c7c4 | -7.9248 | -48.277599 | 2026-06-24 00:16:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cb9959a-2501-33d6-9064-ad402bd5da2f | -6.3076 | -44.641899 | 2026-06-24 00:16:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3910698d-fed1-3981-900c-26f1fda6f24d | -7.2827 | -46.2304 | 2026-06-24 00:16:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4160519-9ae8-3070-8750-713ca8efe730 | -10.7038 | -49.6119 | 2026-06-24 00:16:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
