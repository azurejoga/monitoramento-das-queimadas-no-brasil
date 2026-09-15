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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91c79094-9ad5-313a-971d-a485982e1729 | -11.1111 | -40.472301 | 2026-09-15 00:25:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4d9f4118-afbe-3b97-a93f-fb513401e469 | -2.8844 | -50.419201 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f842845-c1ae-3de8-874c-b4ec84b52840 | -9.4273 | -40.301601 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5ac9b8f1-f189-35cb-b4fc-8d057b26b00a | -6.7702 | -42.737598 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 576bdac7-bc01-396b-a547-e9d6b1398035 | -5.6142 | -45.241699 | 2026-09-15 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0737d158-b487-3027-88cd-3d6a5675e693 | -14.9532 | -47.512299 | 2026-09-15 00:25:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea171670-df36-3b59-8cf0-87f833c07bd5 | -6.1083 | -44.0681 | 2026-09-15 00:25:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56de2078-17f4-3683-854b-2fcd0a367942 | -5.3095 | -49.2355 | 2026-09-15 00:25:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a51363ef-54a9-33ef-a2ee-805e9b415664 | -7.5467 | -46.865799 | 2026-09-15 00:25:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82136805-5a91-3c1b-afa7-cd7213ae7d84 | -11.3276 | -47.679298 | 2026-09-15 00:25:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6325092-23f4-3402-8f2f-40b362e8fa7d | -18.003901 | -50.273998 | 2026-09-15 00:25:00 | METOP-C | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b193ef74-a93c-3028-bc0f-c8002b607882 | -7.6627 | -49.492599 | 2026-09-15 00:25:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc8eea4-ee76-3c96-896a-7732d1fc7ef9 | -2.8577 | -49.618 | 2026-09-15 00:25:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b1f506-2ecb-3226-83a6-3439f9daf172 | -5.7381 | -43.2696 | 2026-09-15 00:25:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13c12aad-1b20-3464-8b68-0aa444fd5026 | -6.9293 | -42.755901 | 2026-09-15 00:25:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9dd7411c-d6ea-3b0a-9d31-e51314328851 | -7.3294 | -47.275501 | 2026-09-15 00:25:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 222b4afa-96bf-3a81-9101-6a0dc6ce50a7 | -10.295 | -54.135799 | 2026-09-15 00:25:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8fb6f68-8063-3498-964f-7e877bbca7f8 | -11.1189 | -40.461399 | 2026-09-15 00:25:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2a34aff5-7ffc-3f61-ae1d-49fcd153e335 | -11.8905 | -43.8283 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51f0614c-209d-35e7-b0a2-8d75e6ef1e2d | -4.179 | -48.683102 | 2026-09-15 00:25:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8765d8a-1c84-3738-bbf1-f49e67b83b67 | -6.7733 | -48.660999 | 2026-09-15 00:25:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 03464ca1-cfa9-3c07-8b52-432af0f5a1dc | -12.4923 | -41.4184 | 2026-09-15 00:25:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed68c713-9845-362e-adc9-c5d32d6fd4e8 | -8.5095 | -50.148201 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b7eee6-cb39-386f-9da6-c6f8b924946a | -9.3585 | -50.1553 | 2026-09-15 00:25:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4870055e-c701-3914-8497-078031e8b2cf | -5.3252 | -47.879299 | 2026-09-15 00:25:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbe4784d-6bb1-3ea0-8b91-d06de61ea4da | -11.1784 | -42.785702 | 2026-09-15 00:25:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 27a9d211-b83d-397d-b185-510ba5498242 | -11.2315 | -43.467701 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a34ddd5-803c-37c1-8359-ce569844441f | -6.8263 | -43.5131 | 2026-09-15 00:25:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df6fdc6a-0e5c-378c-b0ab-f8cdb78fd0f6 | -13.2994 | -51.293999 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cee461a6-7d43-3ab8-a1a2-5d36877339c5 | -2.9115 | -50.402699 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f179211-0558-32aa-82fe-b8d17285353f | -4.2928 | -49.098301 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c085c2-0418-3a07-9ef5-61ac7003dfe6 | -10.9837 | -48.3237 | 2026-09-15 00:25:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecbe6caf-8c18-3bc4-bc64-46123f86b3bd | -7.56 | -44.9128 | 2026-09-15 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed0e9dd-92b6-3fa4-b269-c987208f539b | -3.2513 | -47.0858 | 2026-09-15 00:25:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecf71b13-04fa-39b2-807d-a8192e7ebed3 | -7.1694 | -43.524101 | 2026-09-15 00:25:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4e4aaed5-0e74-39c8-bed3-e26400f9734a | -14.9573 | -47.532299 | 2026-09-15 00:25:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 443f3551-e06f-309c-9813-1a61d4eb8ad4 | -15.2731 | -42.7854 | 2026-09-15 00:25:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d257d5c1-8352-35c9-b111-c5128b1a1fd9 | -13.7193 | -48.963902 | 2026-09-15 00:25:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae148f1d-a420-3ca5-86a9-c10ca591e610 | -15.2524 | -40.982101 | 2026-09-15 00:25:00 | METOP-C | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bcea6f6d-3f24-30a5-90a9-72f434cc8f8f | -8.4973 | -50.1385 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd077a49-05b8-3091-b420-f271bd94d473 | -4.6759 | -42.0769 | 2026-09-15 00:25:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3e9da3a-7691-3d5b-9810-7149d145fb24 | -7.7703 | -49.4697 | 2026-09-15 00:25:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe2333d-c2da-3384-af97-9e8970590d7e | -11.9716 | -44.9277 | 2026-09-15 00:25:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2d72af0-f487-339e-a0f6-6bc731e27b60 | -9.5141 | -40.319099 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c1de0f1a-6f68-39d4-9769-ed9ebcecf710 | -8.9966 | -39.9706 | 2026-09-15 00:25:00 | METOP-C | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 4fe3e508-d428-3954-98da-0edbc7b20a27 | -8.6293 | -44.4473 | 2026-09-15 00:25:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eb10821f-9dd6-3b66-bb40-bb3f857f3993 | -10.0472 | -44.884399 | 2026-09-15 00:25:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| de925144-6cd3-3684-a243-ac539d18a8d1 | -3.4776 | -50.363701 | 2026-09-15 00:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9720af81-6a26-304c-a920-336bfc3acded | -10.5817 | -47.736 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe9ab5a6-b944-3fb1-bcb5-4400bf90d43f | -7.0795 | -42.1175 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f1ea7c6-3179-3dad-9bea-41de174c7581 | -2.9017 | -50.4049 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 629be2d5-37ec-3df0-9c9e-4583a46496e2 | -13.2162 | -51.645199 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa73f356-4409-31c1-801f-98073e115f49 | -10.5797 | -47.727001 | 2026-09-15 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43e141d5-705b-39ee-bd62-41ff2d6a7a48 | -11.8807 | -43.830601 | 2026-09-15 00:25:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed33b52a-271e-378c-aace-8e60a72b2baf | -5.7794 | -49.875401 | 2026-09-15 00:25:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f6c7f29-b640-3bf4-a249-596ecb9b8fbf | -1.7684 | -54.455502 | 2026-09-15 00:25:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db503689-5c21-3fca-8957-11150f09c503 | -4.5008 | -54.940899 | 2026-09-15 00:25:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19dcef29-f9f3-3029-a2ac-25083eb3cf11 | -15.5359 | -48.789398 | 2026-09-15 00:25:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e0ccb04-19e7-3175-a508-126d6a394ede | -3.4799 | -50.373798 | 2026-09-15 00:25:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32021174-d335-35e8-aaf3-e4fc41a67e68 | -13.2064 | -51.647099 | 2026-09-15 00:25:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3fa8586-0884-3c3c-a06e-c1eb646bf6ca | -15.2715 | -42.778301 | 2026-09-15 00:25:00 | METOP-C | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ecd32aa1-7fb3-3b2a-ba0c-e093f46b7ba0 | -6.7135 | -48.1119 | 2026-09-15 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3fdf30cb-3827-3a4e-8ef4-388cdc860ce3 | -13.5635 | -43.5243 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b74e037-4959-373a-ad0e-a9954553e272 | -7.456 | -46.138699 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb029935-6b63-31b7-be69-3106e8522d4f | -18.163 | -51.733601 | 2026-09-15 00:25:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd1226c4-2d2d-32b8-aa03-b36ded69b66e | -6.4236 | -43.066601 | 2026-09-15 00:25:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e447b2cd-6a7c-3b52-a6f7-2ab76ae4d2de | -10.6627 | -54.112598 | 2026-09-15 00:25:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8202132-4ee5-3dcd-9832-d86aa9c058cb | -6.3268 | -44.120899 | 2026-09-15 00:25:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81980a53-ed12-3e9a-b7e3-b197aaefa6be | -8.7993 | -46.904099 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1338870c-9866-3157-ac16-7f3ae306d344 | -0.9607 | -47.571899 | 2026-09-15 00:25:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc7cfd6-40ad-3a8f-b265-034fb926c520 | -2.9137 | -50.412701 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ee05d8-eb3c-33f3-a91f-667c464932be | -4.6779 | -42.085201 | 2026-09-15 00:25:00 | METOP-C | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2b64653-80b4-3f8e-8228-6f401f9ed712 | -13.4325 | -43.813 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d36ea97-93e9-3399-9f21-9b238bd47f0e | -4.2948 | -49.107101 | 2026-09-15 00:25:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 694b14e4-061f-38c6-97a8-c144b2fbe38e | -13.5521 | -43.519501 | 2026-09-15 00:25:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8393cde1-da80-3fab-9310-df22aa040a46 | -11.2333 | -43.430599 | 2026-09-15 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb9614dc-10c4-3cc5-967b-cc058b44ab43 | -7.0197 | -44.623501 | 2026-09-15 00:25:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0d71d8d-ea10-3481-aa5c-ce4904ab0ff6 | -5.327 | -47.8871 | 2026-09-15 00:25:00 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03e7742c-7756-34ec-b3f5-a7d5e0ec9be9 | -7.4658 | -46.136501 | 2026-09-15 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20e716a5-89f4-3fc6-9fef-4e6f9daafefd | -6.7622 | -42.747299 | 2026-09-15 00:25:00 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 413da5dd-d37b-3342-847f-8c0343ec4f83 | -5.7249 | -46.181198 | 2026-09-15 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fcf531c-7ab4-3c13-a8ae-c816a30ecd91 | -7.2239 | -46.160099 | 2026-09-15 00:25:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bcda848-fdf3-3357-adcd-d46bfbf5a596 | -6.727 | -48.126598 | 2026-09-15 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7af689fa-643d-324c-b3b4-10e8f9b164be | -15.2747 | -42.7924 | 2026-09-15 00:25:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9dbc62c-5935-3ef7-9df1-090e317691e7 | -10.8563 | -46.305901 | 2026-09-15 00:25:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2251e208-6f02-33e5-b0db-38a3da1ad85c | -7.0776 | -42.1096 | 2026-09-15 00:25:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c370b026-1cb1-34f6-9212-87ae3997a9d8 | -15.9222 | -47.359798 | 2026-09-15 00:25:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2751c0d5-1189-3589-9891-5eaf32741b89 | -11.8106 | -46.587002 | 2026-09-15 00:25:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9d2021-34a7-3ea6-bd08-db6c184f9e5e | -2.9039 | -50.414902 | 2026-09-15 00:25:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6fd081d-9280-35b8-8cc1-547fd0162a9d | -11.1121 | -50.900799 | 2026-09-15 00:25:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05b41e97-0080-3a7c-879c-6cc07786119a | -16.7981 | -47.610699 | 2026-09-15 00:25:00 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae246231-fc87-32a6-9a10-81ffcd53a99e | -7.1579 | -43.519299 | 2026-09-15 00:25:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf6412a2-64a7-3ebd-ad55-a7f3185358fa | -9.5239 | -40.316799 | 2026-09-15 00:25:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed04aba6-d4fa-3feb-8f91-69f3862e48a5 | -6.7837 | -46.446098 | 2026-09-15 00:25:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38e5971a-c05a-362f-bbeb-6a3746f5d77d | -6.7251 | -48.118198 | 2026-09-15 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a4ff376f-045d-30aa-b53f-592145f0ef20 | -6.7153 | -48.1203 | 2026-09-15 00:25:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7105dcde-b32b-3ae5-93bb-8ffea28a13e9 | -6.7909 | -43.181801 | 2026-09-15 00:25:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88c94b91-862c-317a-b264-15c930851d26 | -2.0416 | -46.933601 | 2026-09-15 00:25:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c627cf1-a463-39d8-8ea1-222f9d864339 | -5.3532 | -50.173401 | 2026-09-15 00:25:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b814f3-5acd-307c-a7cd-26d117577595 | -6.96 | -44.543098 | 2026-09-15 00:25:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README11.md)
