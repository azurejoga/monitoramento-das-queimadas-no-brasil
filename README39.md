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
| c6f890b5-1c86-3ac2-93c0-04bed25ba08c | -3.2994 | -42.26929 | 2024-10-15 04:23:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8bce44e-8f48-3437-a3a2-bf6ac84db32d | -5.03105 | -42.42082 | 2024-10-15 04:23:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 89eb6781-b1de-3dae-b3da-bdbf3f787860 | -5.02991 | -42.41938 | 2024-10-15 04:23:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04459739-d585-33c5-bc72-5ed7a74569ea | -5.02927 | -42.42368 | 2024-10-15 04:23:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58b51b66-5326-3eba-85b0-05b318ef0af3 | -5.02738 | -42.42026 | 2024-10-15 04:23:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 174da92f-119b-3518-b3ca-09be4f918ec8 | -4.9708 | -41.80861 | 2024-10-15 04:23:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e8ac138-9714-3432-ac36-67e82e272fb1 | -4.09423 | -42.28334 | 2024-10-15 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75fb04df-8fd7-3e88-acd1-680338686c81 | -3.92572 | -42.41161 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97bcf4d1-4c56-3a7c-9d15-ccb8057b2771 | -3.92507 | -42.41578 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5508e9d0-b795-38a3-b096-484596b25082 | -3.92273 | -42.40688 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| e7bd5da0-2eb1-3f17-81c4-a99aed256e47 | -3.92144 | -42.41523 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 81ff9f12-e61d-3d31-af17-5df864ae0672 | -3.91975 | -42.40216 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 620f1d1f-5efd-3561-b615-a9ef77d9ad8f | -3.9191 | -42.40633 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| efb0e525-b2ac-32cb-904a-24e8d579f5d5 | -3.91846 | -42.4105 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 2f5504a1-29ad-3d31-9010-ed05e07e3374 | -3.91781 | -42.41467 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| e66045f6-bc6c-3017-a836-21c199ac4f60 | -3.91547 | -42.40577 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 29c1d491-fb2d-35a0-aefc-d18d0d0505c2 | -3.91483 | -42.40994 | 2024-10-15 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7458ab1e-42fd-3448-919a-19f3d2129ad2 | -4.51944 | -42.88381 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73dcfc3a-a754-3aeb-b7ba-bf0d1dfd858e | -4.51462 | -42.89136 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ed859f5-f256-3c59-965f-7ae722f55d93 | -4.03167 | -43.03011 | 2024-10-15 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6715007f-a555-3591-ad06-5aa6783b8183 | -4.03107 | -43.03401 | 2024-10-15 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2b81b47-4211-3e2f-86e3-3dd2df4efaf7 | -5.86953 | -42.46228 | 2024-10-15 04:23:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5bf1fb59-01b2-3216-adb2-f1ea0d3d05a0 | -5.47631 | -42.79141 | 2024-10-15 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bed543a4-8a3c-38af-b86a-04e0819722e6 | -5.47458 | -42.77843 | 2024-10-15 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0407284d-4929-3adf-bd7c-3a10a43c5889 | -5.47394 | -42.78259 | 2024-10-15 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 34f398a7-a351-3f79-b052-6891b222666b | -3.51909 | -43.24776 | 2024-10-15 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44573b90-fe04-3f68-8a49-c9822b60e5ba | -3.51851 | -43.25157 | 2024-10-15 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44acd63d-438a-3667-b4fa-a4c4f0668e56 | -3.42341 | -43.34969 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a8ebe1c-fea6-3158-b9d5-81d84c5051fa | -3.41995 | -43.34915 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf9c272-30a4-30d5-800c-cd4de69172f9 | -3.41879 | -43.35669 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c60d5b0b-7b89-3474-954b-0ff441709a30 | -3.3986 | -43.34974 | 2024-10-15 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d791eef-58bc-3fd9-b838-83010b4cdedc | -2.9188 | -44.35453 | 2024-10-15 04:23:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab976555-bb83-323a-abaf-34bfd99ad28d | -3.96349 | -44.05383 | 2024-10-15 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49c63094-48a2-3b30-83bf-4f586b5ad0e9 | -3.93448 | -43.1434 | 2024-10-15 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 863bfef0-06ec-30a3-9040-07fa88d60f7b | -3.93097 | -43.14286 | 2024-10-15 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae0fa3b7-34db-36f6-a064-51deb50ac0ae | -5.32272 | -43.37236 | 2024-10-15 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a5dd0ac-f332-3f7b-bcc1-2e457055c7c0 | -5.32267 | -43.3712 | 2024-10-15 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5be1604b-17f5-3f22-adfc-845647c02b71 | -5.31856 | -43.37457 | 2024-10-15 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdab45e9-0d21-3f53-9436-02072030206d | -5.21442 | -43.7258 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 186d83e0-9c0f-3bbf-92e1-6d97fc230a69 | -5.21383 | -43.72958 | 2024-10-15 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1adaee6-0fab-3e04-acec-3029346bac89 | -3.60871 | -44.78719 | 2024-10-15 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce82dbd7-9417-3873-98ac-e95e8bd5bd84 | -3.60538 | -44.78667 | 2024-10-15 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecb8cdf8-50a7-3350-9c55-769f1c3810e5 | -2.81397 | -45.28463 | 2024-10-15 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4aab9504-3f8c-3106-97c4-bf87c7ce5e62 | -2.81342 | -45.28808 | 2024-10-15 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 05c60ada-e804-3671-a6b7-b1c6403ff634 | -2.81065 | -45.28411 | 2024-10-15 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bf194f8-8e06-3d32-8b39-2489b8402a16 | -4.71222 | -46.16249 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40551caf-08ce-32f1-b50c-4def30f6b47b | -4.70558 | -46.16145 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f85b2a8c-1cba-3de3-b3c8-871cc11e3956 | -4.70225 | -46.16092 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c72701d0-6cca-320c-8da4-ff361b1fb1fa | -4.78334 | -45.79791 | 2024-10-15 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36df7195-8fd8-3d64-a82c-7bd9fba48bca | -4.71555 | -46.16302 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9dae121-f7f0-30c7-8a5a-5dc34ad5228c | -4.71277 | -46.15903 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45391107-d041-3181-83e0-3a564a74eb9c | -4.7089 | -46.16197 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744b42a7-f11b-3597-b959-8bbc7cf36ec1 | -4.68624 | -45.79362 | 2024-10-15 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99d86f00-7170-3d1c-82b6-809f8eb250bd | -4.68291 | -45.79311 | 2024-10-15 04:23:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02150ed6-73be-3a1f-bc58-e6a2bedcdf1a | -4.51269 | -45.92581 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b507887-070d-37fb-ba33-20b170417188 | -4.50937 | -45.92529 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbb467b2-2b73-3c70-a5c9-75581507b01d | -4.47156 | -45.93316 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf37ffe6-4049-34a4-9d71-86110b5e326e | -4.46824 | -45.93263 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6894f64d-c85b-3fd2-9e30-a60ce6895eda | -4.46482 | -45.88963 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dd64376-5d56-3c18-a841-c29e89661f91 | -4.46204 | -45.88565 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f29b4a51-ea8a-3c89-b275-52f878aadca6 | -4.46149 | -45.88911 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4d3eeda-90da-36a9-8f3c-17850b604804 | -4.13286 | -45.39825 | 2024-10-15 04:23:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 247b183b-23aa-3c49-945b-8408415b1cc2 | -4.0528 | -46.07331 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e30e398-5163-3780-a6d7-02f1070d2e72 | -4.04947 | -46.07279 | 2024-10-15 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ee667f7-5ddf-3409-88e1-5dbee9b7ed53 | -5.18969 | -46.2912 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d64d0832-9bd9-3fde-b28f-c3120feafc48 | -5.18636 | -46.29067 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f8558b3-37c4-33ab-a8be-f7c30bb8f01f | -5.27405 | -46.37924 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f8d4e0c-5925-378d-8c85-7e8cb17f81a8 | -5.24079 | -45.4903 | 2024-10-15 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fbf309b-2353-321e-ac9f-be9bb1d16f79 | -2.14698 | -45.86386 | 2024-10-15 04:23:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82acca7e-127e-3e67-9610-15da98eec0c6 | -2.11995 | -46.05631 | 2024-10-15 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0170aa67-0da6-3eca-90b0-6ff97da67b36 | -2.1194 | -46.05981 | 2024-10-15 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc491bfb-1405-3e6b-b32b-b68107d0324b | -2.06391 | -46.56271 | 2024-10-15 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 198ed239-e3c8-301f-9b7c-f49607d69c9c | -1.66207 | -46.21229 | 2024-10-15 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 775937d7-5ad6-3260-9ce4-4a6dc6d0094d | -3.58781 | -46.33938 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab62866b-e238-39fa-9b4d-1f39f529a5d7 | -3.58725 | -46.34288 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e6e6e25-99b2-3881-874a-095d5a80614b | -3.5867 | -46.34639 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d96ca16-41e8-3e50-a861-06f1da1bc2f5 | -3.3675 | -46.49177 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 305ca6fc-d93a-3dd2-bde1-9a5dfe700ca5 | -3.35463 | -46.48622 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68a2c28f-0175-31ff-9a4b-43da19f344b8 | -3.31294 | -47.0108 | 2024-10-15 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8132d40f-75d8-3d2f-8b60-ca01de345fbe | -2.97058 | -46.94686 | 2024-10-15 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7c797ec-195f-359a-95d8-4ce5383a3193 | -2.97001 | -46.95049 | 2024-10-15 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f02d773-46c2-338b-a6d9-6442fe948423 | -3.07102 | -45.9511 | 2024-10-15 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae715840-4fd3-3f10-9c86-d40f4d919c4d | -3.06381 | -45.95353 | 2024-10-15 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55117c22-199f-30b1-898f-54c64c40c059 | -3.06048 | -45.95301 | 2024-10-15 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184635f1-de56-3efc-ad37-055eeb88e84e | -3.05994 | -45.95648 | 2024-10-15 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81782b9c-6444-33bf-8098-eb02f719c472 | -3.05715 | -45.95249 | 2024-10-15 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c322dc7b-0440-3c85-958f-b3855f461551 | -2.5944 | -46.11961 | 2024-10-15 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e49adce-a991-33ec-bf85-879e155fd265 | -2.59105 | -46.11909 | 2024-10-15 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5d63ae-1e88-3c1f-ade0-ba311f5d9aac | -2.45495 | -46.03656 | 2024-10-15 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01fd013b-edba-3277-9890-f833e319af02 | -2.33766 | -46.46221 | 2024-10-15 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2d25452-4e96-3844-890d-335f5bafd085 | -2.33139 | -46.68461 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68e8ce7c-9e67-3a67-86ab-8b9384e98c2e | -2.33094 | -46.48302 | 2024-10-15 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e66b1179-be97-32ef-940e-bd7e043fafe8 | -2.32858 | -46.68049 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb4f9a91-2a63-3220-afca-be9c0bbbc263 | -2.2541 | -46.75045 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce6acd7-8f6f-35c0-a0f6-cb55f81ffbe9 | -2.25356 | -46.73184 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e81037c-94c1-3c0b-9a81-aa57c442d71c | -2.25353 | -46.75407 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f62e884e-d1e7-3211-b2e1-5bb456608bef | -2.25295 | -46.75768 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d9be7f-4728-3b14-a197-71548d51c895 | -2.25242 | -46.73906 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b656011-21e4-31a0-8c67-1dcc81623b2e | -2.2507 | -46.74992 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4456d47a-ee9a-34a1-9a96-6d8bcbd85956 | -2.24956 | -46.75715 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
