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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bd8c265-4463-3726-a25d-a93285ad05aa | -4.05694 | -56.24525 | 2025-10-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69422c6b-1683-3ba7-b945-b2a52600c78e | -4.07296 | -56.23247 | 2025-10-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52b9c68e-1d4d-35e5-b56e-456131e8f05e | -10.35633 | -48.70254 | 2025-10-30 05:16:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2aa3d652-1ebd-3265-a414-165ddf63d973 | -8.70445 | -47.91126 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 647f7be7-f163-3e92-a846-3fc8cad9e17c | -3.60435 | -50.62694 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1e1ebe4-2018-39e6-bb3a-25999ac6e794 | -8.43547 | -48.70213 | 2025-10-30 05:16:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77172816-ab33-3e71-af5f-15cfb0c1337e | -5.61247 | -47.12489 | 2025-10-30 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f64751f-a9a1-3160-ac41-c87691c29c4d | -6.21129 | -55.66859 | 2025-10-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39b98ce7-e3ca-3b3f-b4db-0ce8dfcc0293 | -10.35689 | -48.69794 | 2025-10-30 05:16:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5ac3048-4383-3bc3-b562-9a7396802e12 | -4.35803 | -48.19969 | 2025-10-30 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99ebb64b-57fa-3d54-b090-2500bcc7e167 | -4.25407 | -50.67475 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2228ac2-5cc3-378f-8778-d9709e82baed | -2.93432 | -54.16793 | 2025-10-30 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fd37b42-4600-3759-8582-c17c9750ec0b | -10.12756 | -48.06468 | 2025-10-30 05:16:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cbd5a64-0c80-323d-abd8-054bbc9b4599 | -9.88535 | -47.44177 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d485b48b-8f3d-39a8-b41b-4ac38f5f0256 | -9.93764 | -47.1731 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 97a7e6a4-5f80-3a77-bd62-1a8dcefdd3ca | -4.3304 | -47.89349 | 2025-10-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4c8f852-cabc-37c9-bfe9-167e0c4f6d03 | -9.89132 | -49.12041 | 2025-10-30 05:16:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56df3788-77c0-385d-834a-94669dbb8ba9 | -4.52876 | -54.9608 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eca0350a-981a-32e2-bc0c-0db7668e37d1 | -9.09152 | -47.91491 | 2025-10-30 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b538a04c-a4a8-3933-a29e-af9871691056 | -7.29542 | -45.66656 | 2025-10-30 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7165dec9-1e86-399e-840c-7be11b6c225d | -5.43814 | -45.33642 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 77e582ca-1ca8-3a25-b019-54b21ababe3b | -5.40387 | -49.42435 | 2025-10-30 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72e3dac0-9b27-38bb-bfd0-ba8a2be8c47f | -4.40879 | -48.95265 | 2025-10-30 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 047fdad0-4d01-370f-800f-e96e85b89d7f | -10.1325 | -48.07609 | 2025-10-30 05:16:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6350c4b3-edcc-3305-ac8f-471c7450092f | -5.22691 | -46.14175 | 2025-10-30 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a083067-69f2-35b1-a4f8-36b9a6b9ee43 | -4.69538 | -56.0613 | 2025-10-30 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d648e11-64ac-3186-b659-cecebe8b71c1 | -9.09212 | -47.91012 | 2025-10-30 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82a053b9-4d0a-381f-be15-ab48d63687ae | -3.20002 | -51.00521 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4144ef76-c6a5-3283-be9b-f8a500417697 | -7.29845 | -46.64392 | 2025-10-30 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18004fab-73a1-3dda-809f-aa4251eb83fc | -4.84155 | -45.42203 | 2025-10-30 05:16:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 539aae4e-2304-3749-840b-89e344a8c94e | -5.43037 | -45.34304 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f0a9792-fa47-3988-b5cd-e3be3bd28db5 | -5.61307 | -47.12038 | 2025-10-30 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fcbc5440-69b3-3d7f-bed3-e53ba4849693 | -8.70454 | -47.91404 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 402ca7c1-e0d1-3a71-9f56-fa4cc59a44c5 | -3.01253 | -51.38113 | 2025-10-30 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27177489-8e8f-3149-8acc-7e2fd76f2b91 | -3.67423 | -47.6266 | 2025-10-30 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b08724ca-86dd-3706-8110-3ac65364ce75 | -7.29638 | -45.65919 | 2025-10-30 05:16:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c597dddf-6b02-37d6-b7ca-3b8ff851bf60 | -3.09014 | -49.50213 | 2025-10-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05bda401-5059-3102-b397-9c174cf7ba44 | -4.33102 | -47.89185 | 2025-10-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 755d676d-09e8-3568-af9c-e609294c87f1 | -3.20466 | -51.00589 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97cd1a7e-4e89-3884-8026-dcebeee39b47 | -1.58121 | -60.38076 | 2025-10-30 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f79d807-f1ac-3cb6-a6c5-4e937ae20d56 | -5.44954 | -50.90205 | 2025-10-30 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6252335-c700-3dbc-8803-d6e63caf7a78 | -3.60512 | -50.62182 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da76ddd-1237-3278-9087-3b9339fdd6b8 | -5.43119 | -45.33565 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b8770f2b-9869-3327-a8d3-66e81d0ae066 | -5.59445 | -51.12403 | 2025-10-30 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e75e7bcb-86d1-3e58-85ec-d8a2ebd1ea23 | -5.84002 | -45.54087 | 2025-10-30 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9995ef7-a65e-39a7-ac2f-86b6ce3e49c6 | -3.0906 | -49.49907 | 2025-10-30 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89fcf2e4-e82f-35fa-acea-1564b6ab240b | -3.33041 | -54.08827 | 2025-10-30 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39495926-c1df-3fcb-82b3-1998ee3569ef | -7.34667 | -47.63646 | 2025-10-30 05:16:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2faa1a23-60ab-3fa1-9096-8b7c62141448 | -9.09273 | -47.90527 | 2025-10-30 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34b0e5e3-6aac-36c5-a8c6-1c1effdc6ca9 | -3.61026 | -50.79112 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63a49e8-59a4-33f7-b43a-077276f4939d | -8.33346 | -47.93176 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc1fa9cf-3c10-3f1d-b06e-71c8a17d4fbf | -2.90407 | -53.12939 | 2025-10-30 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eefefb0-2f7e-382b-adf6-dcca7a5c515e | -5.43025 | -45.34246 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e0cf1ae4-7e77-3eef-b138-9ce32730465c | -5.59355 | -51.12697 | 2025-10-30 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d45e55b9-548c-31dc-829a-1d21f95d9010 | -4.15904 | -55.15421 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd0b41d8-6fc7-3cbb-8090-9994c9fb3d6c | -1.57831 | -60.3763 | 2025-10-30 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d240f7c-9585-3998-9622-9faa7af0a60d | -5.61443 | -47.12092 | 2025-10-30 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f45f473b-2a06-3a33-aeb3-3ca0734fe284 | -2.93944 | -54.15948 | 2025-10-30 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ea85490-9c3e-3ba5-aa24-c052706d7fe4 | -8.70517 | -47.90918 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3f746c4-fb54-3023-b4c4-a28242b161e4 | -5.59698 | -49.08066 | 2025-10-30 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f9d458d-771c-3917-bd35-d2973f4c8179 | -3.69107 | -60.55411 | 2025-10-30 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97d9971d-3d75-37c0-8e08-f92b2f5f9a9b | -1.57769 | -60.38022 | 2025-10-30 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6521846-8362-3d05-94c7-4ce89f971ec5 | -3.60715 | -52.64544 | 2025-10-30 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc4738c6-b759-3d96-a0fe-35b34b6186d0 | -4.35863 | -48.19553 | 2025-10-30 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bc5bab0-1976-3018-a22c-627cfe6f8ee6 | -4.41314 | -54.85708 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6289cd39-44c3-351c-b881-a5c37b686e09 | -4.64567 | -49.48323 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba98fe1c-37dc-3037-973b-39e548ccc2fb | -5.59747 | -49.07711 | 2025-10-30 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58505c33-3819-3bb1-92bf-19b1d70e4bd8 | -5.7586 | -49.50039 | 2025-10-30 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66657a7d-7baa-3612-a538-d2b8664a47bc | -2.94988 | -51.52679 | 2025-10-30 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fa0560b-ef10-38ae-9003-1bd1f13d7c2f | -3.45173 | -52.81801 | 2025-10-30 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8024a2-ae06-36db-bc0e-66a5674fbbf9 | -4.07452 | -48.26162 | 2025-10-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4af1a5e1-5ca9-3eb9-ad84-1187039a91a5 | -3.61649 | -51.07589 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5feb7596-9af6-3394-9162-dec8c5a84058 | -3.91583 | -55.91186 | 2025-10-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27e9b5ca-f22b-3c94-9d78-50f10e787c78 | -2.05742 | -56.87426 | 2025-10-30 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80cebf21-444c-3929-97dc-3871fb8022e9 | -3.32664 | -54.08587 | 2025-10-30 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 001b9161-fda9-3a59-ab3a-b25cb7c33a90 | -3.91472 | -55.91132 | 2025-10-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ca42d8-8d6b-39c4-8374-0ae065cb7057 | -3.68005 | -47.62779 | 2025-10-30 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28703416-9f1f-3631-a05e-6c0796539a8f | -4.53541 | -54.96628 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e95c6fc7-39b0-39db-9f7a-45fb703ef688 | -5.43721 | -45.34313 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d78bf955-7ca7-396d-8d99-64b736c4eee0 | -8.2948 | -49.31746 | 2025-10-30 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c761d3-f276-3e1f-a68b-983899fcf39b | -9.82912 | -47.69318 | 2025-10-30 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| aed4a89f-0f16-388c-aca3-6b47e83707c7 | -4.07238 | -56.23621 | 2025-10-30 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 163637b2-d530-3e41-8909-b07afa8335ab | -5.43821 | -45.33697 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fed7c191-12f8-313d-bb1d-bee6c9043158 | -4.25486 | -50.6695 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0ca9188-0ce5-34d4-8984-ec41d2be2909 | -3.01186 | -51.38567 | 2025-10-30 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 436b94c8-9b9a-3100-9a9d-dea08ff0502f | -5.60819 | -47.12015 | 2025-10-30 05:16:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d32b137f-77c2-333f-bed0-fe71e6b166fd | -9.9088 | -47.91058 | 2025-10-30 05:16:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95d9ae91-a94f-3af9-8375-c4946fdc522e | -5.40433 | -49.42102 | 2025-10-30 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0866fb84-209f-3a46-be84-f5d388a9c4e9 | -3.44316 | -54.63712 | 2025-10-30 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d636f39-dbba-3dec-b826-87dbcf2cbca4 | -4.20401 | -60.00064 | 2025-10-30 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3c18db-dcea-3f9a-930f-bae4093036fa | -8.699 | -47.90826 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f39f6b8-b3b4-37b0-b941-b206047815ae | -4.33098 | -47.88929 | 2025-10-30 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a73a63a1-4e7d-3738-b5aa-8e1b478fc2c3 | -4.15966 | -55.1501 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae792e3e-38b2-3165-9197-d3f64ee95f2a | -8.32116 | -47.9303 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21129f69-3d46-33d5-958c-ce3acdd842fc | -8.33406 | -47.9271 | 2025-10-30 05:16:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e329c9a1-957b-3c88-83f2-044bfad0c3fe | -9.9331 | -47.86783 | 2025-10-30 05:16:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20213edc-1728-3527-acbf-4d32d8e8e935 | -4.52811 | -54.9651 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17485e41-43e0-36c5-91a5-644a405db3c1 | -4.16687 | -55.15116 | 2025-10-30 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 851b7f1e-ec00-3e79-aa24-395e89f8417f | -5.43732 | -45.34373 | 2025-10-30 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d13d37e4-749c-314d-88ab-891d40c73fcb | -3.06023 | -54.61831 | 2025-10-30 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README64.md)
