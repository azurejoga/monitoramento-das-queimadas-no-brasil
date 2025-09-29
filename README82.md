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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bd6b234-7752-3b5e-abe4-23838e86c391 | -10.823 | -46.6538 | 2025-09-29 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3016000c-3f48-3eae-8353-7f1c06bfc8c3 | -7.4488 | -46.299 | 2025-09-29 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3adfbbe1-a054-3f25-a853-acca923345c7 | -11.925 | -48.0273 | 2025-09-29 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 8c66fd95-60e1-3e27-8585-785a5b485ee8 | -13.2154 | -50.9715 | 2025-09-29 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 4c418417-4bca-331b-85b8-5a886b5c3483 | -13.235 | -50.9476 | 2025-09-29 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 82cc5e03-7f4c-3d31-95cf-2c34d560c40e | -14.6049 | -45.0161 | 2025-09-29 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3a4e9634-422f-3a31-9b4f-f4fe6860baa7 | -7.2214 | -44.783 | 2025-09-29 12:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 485d81de-b8a0-30b2-898f-ad6746892db2 | -11.3634 | -45.0801 | 2025-09-29 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| e9aca7b2-fe2c-3bd7-beb7-748e9a5da686 | -11.3638 | -45.057 | 2025-09-29 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 470b050d-9d9f-3eb5-ae40-73225ad9adcc | -10.6239 | -48.5386 | 2025-09-29 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 585c7c25-109b-3f47-8596-725c64d3652b | -8.2659 | -45.5244 | 2025-09-29 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 969a8a9b-b6da-37f5-81d8-193855196455 | -7.4676 | -46.2974 | 2025-09-29 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 55d18399-2da0-3a1d-94e6-6bffabc15c29 | -7.8163 | -47.0003 | 2025-09-29 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 66caf484-0ffd-3e78-af5b-64a48e1c4c14 | -7.2402 | -44.7812 | 2025-09-29 12:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f611c558-fe2a-36ad-91f8-6e45c1cc7703 | -11.4409 | -45.0229 | 2025-09-29 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| efdfbb07-7415-3d06-8490-b448e2c6bed4 | -7.8566 | -46.7527 | 2025-09-29 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5d48ba0b-1b4e-39f9-8e69-879e86e4d083 | -13.2158 | -50.95 | 2025-09-29 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ea9ca968-8d81-34c8-895a-0d8842e29858 | -8.2848 | -45.5225 | 2025-09-29 12:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| ce11508e-0828-306f-bc23-80750813dcb8 | -12.9435 | -46.7655 | 2025-09-29 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7261ed9a-c777-3017-b549-34f779af76b8 | -11.3826 | -45.0774 | 2025-09-29 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b7cf7c96-4292-3efa-ba31-bfd8aa7233d3 | -13.2346 | -50.9691 | 2025-09-29 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 444.8 |
| b279c043-18fc-3fe7-8cc0-023421781117 | -7.2402 | -44.7812 | 2025-09-29 12:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 90996ac4-7537-3510-a5ef-b25a7a68b6b1 | -8.2848 | -45.5225 | 2025-09-29 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 65734170-72db-34da-ae78-398b578f9424 | -14.6049 | -45.0161 | 2025-09-29 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 1031d474-945e-389d-8b25-0cbfa7c395fa | -11.3634 | -45.0801 | 2025-09-29 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2131d60f-73a2-3967-b38d-da38ef523da8 | -15.219 | -50.1071 | 2025-09-29 12:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 65887a62-ecbf-3112-a26a-f844523a9fcb | -7.4676 | -46.2974 | 2025-09-29 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 040f3ac0-9f58-3b6e-913e-4118197f0e6e | -7.8163 | -47.0003 | 2025-09-29 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 94d846fe-e203-333b-9a07-ff337f97f55a | -7.2214 | -44.783 | 2025-09-29 12:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 58e69277-975b-3f24-8f4e-66ac8b96d90f | -8.2659 | -45.5244 | 2025-09-29 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8c508e79-2f6f-33d1-935c-7c9a41bab385 | -11.3638 | -45.057 | 2025-09-29 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 538bd7a2-5af3-3c51-9e34-4d55c8584d35 | -13.235 | -50.9476 | 2025-09-29 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 199d59ba-5398-367f-b17b-c2d4acf8c515 | -13.2154 | -50.9715 | 2025-09-29 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 149d77b1-5835-3696-ba42-75d92f395ee8 | -7.8378 | -46.7544 | 2025-09-29 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e351d265-768b-37e0-8582-99b1c6918915 | -7.8566 | -46.7527 | 2025-09-29 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| efde4deb-5318-3f24-a091-691c36abe491 | -14.698 | -45.2093 | 2025-09-29 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| acf6a171-e6fe-3246-9977-922774a167f3 | -7.85433 | -46.76911 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| b83d4e1e-8807-3c4b-99f9-9b304e4e333c | -6.00413 | -43.79238 | 2025-09-29 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b360ce41-dded-3e8d-89fb-5661a362717c | -6.03941 | -36.52488 | 2025-09-29 12:17:00 | TERRA_M-T | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 9be1cc31-5224-3b5c-b652-005ae8ea3c24 | -6.97819 | -43.76564 | 2025-09-29 12:17:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 176067e0-357c-38a2-950f-f03806fee4bd | -6.08293 | -42.44183 | 2025-09-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 404a48dc-fa9f-3d60-bef6-b0129ac0f489 | -9.05388 | -46.69846 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c03cf5cc-3c19-351c-ab5f-1dcac8972871 | -8.72099 | -50.04472 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2a79b7f9-acd6-3ac3-8e9d-db7a23a33f2c | -6.38997 | -45.13737 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b0b90ec9-c304-369c-90ce-9da7810998df | -2.25301 | -47.88265 | 2025-09-29 12:17:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 39cdc263-7b89-3ccc-bd75-6ca2e1e97391 | -9.30992 | -47.36133 | 2025-09-29 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a60d4c2b-1958-3c47-b110-cfc21dd4cdd0 | -4.55523 | -46.68634 | 2025-09-29 12:17:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 01cb5528-45ab-3950-899a-5f16e8087985 | -9.32328 | -45.69426 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c0ff4613-940f-3636-a046-3e5537450481 | -7.28057 | -45.81628 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 188e4140-ffd8-3a29-81e7-52f5d70b824c | -6.66049 | -41.38146 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 6accddbc-9a14-3071-ae56-6864f80ddc9c | -6.89642 | -44.52708 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a74a51cc-d46c-3cfd-aef6-d6fff4339047 | -4.19837 | -46.47703 | 2025-09-29 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a3f317bb-ee88-3ee8-b050-8ac1f1549073 | -4.40075 | -44.07723 | 2025-09-29 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46f3d025-21e6-3edc-938c-9e4494dd302d | -7.45918 | -46.30865 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4c04c28d-366a-301a-b7e2-0ecc4d712402 | -7.84674 | -46.75897 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6835a248-7df1-3ead-9b3e-27cf814bc3a7 | -8.38862 | -47.99252 | 2025-09-29 12:17:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fbfe1190-58e7-31f9-9d4a-34211942f4c1 | -3.45446 | -44.12244 | 2025-09-29 12:17:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 591903dd-6767-32ab-bfe8-d3440fa80c0d | -5.46115 | -41.07718 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 3dd30875-4ba1-38fa-849f-5828d19b49c6 | -9.10738 | -45.85804 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 23189a81-8f2a-3535-b2f5-1d370c4ae8ac | -7.46047 | -46.29963 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ef97476d-8fbb-3e88-8417-9489ff3d4916 | -6.2896 | -45.26272 | 2025-09-29 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c270ee8e-7330-39d7-bc95-38532b39f833 | -2.69188 | -43.71569 | 2025-09-29 12:17:00 | TERRA_M-T | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e1e877f2-b2f4-3196-ac91-5bf9fb3603e1 | -9.09997 | -45.85101 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| cb88b767-c866-37b2-b950-78cf556040e3 | -9.06629 | -44.94847 | 2025-09-29 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0629d449-21a2-36cb-91f0-89d6e505e04b | -8.87236 | -46.61459 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 6266cf35-dcb7-3f97-b354-5cfbe628e91c | -6.0666 | -42.48191 | 2025-09-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| c6e01a23-bb7f-3f7b-8920-cf1f4b24c9d1 | -7.55542 | -45.29842 | 2025-09-29 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 35847e00-7814-3c03-a370-f6418e4bc83b | -7.44547 | -46.98524 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1a2eecd9-f80a-3c5b-adee-1d87118fb09b | -8.28462 | -45.4875 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 80f7a55b-60cd-39f9-920e-c3e6e2e8d0c5 | -6.4403 | -43.07621 | 2025-09-29 12:17:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fae080c3-3c4c-32a7-9d8b-03021e8769c3 | -8.44174 | -46.92229 | 2025-09-29 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a532fc20-0d5a-385d-b814-b1ffb1b71bf1 | -6.43164 | -43.06196 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 52731367-53ff-3ebd-9644-0c4b009be444 | -8.86601 | -46.59529 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c0a3ebdd-d6eb-3889-af4c-ea2ad0b80852 | -5.86576 | -43.89623 | 2025-09-29 12:17:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8c76802a-60fe-3ccc-a9f0-d5048340c258 | -7.84929 | -46.74117 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 22ac8cb2-5cac-3edd-a10d-d4598df25c68 | -9.32196 | -45.7039 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.1 |
| a7b6f3b1-d45d-3529-858a-65c3a4d53db4 | -6.65823 | -41.39828 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 3af45eb9-6872-3231-b799-28a5c8402516 | -6.39129 | -45.12795 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 40427c9e-3c3a-396f-9676-1c78c9e80179 | -6.29874 | -45.26391 | 2025-09-29 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| bfdc3a03-d9f9-3510-a172-d1eb6cae2c46 | -9.31407 | -45.69296 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 30682fd1-e2ea-3bba-b9ef-4cc1be8190e0 | -7.84547 | -46.76787 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 01b9d8ff-f520-308b-a35e-c42599869843 | -6.46503 | -44.21788 | 2025-09-29 12:17:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 53d0d217-b718-34ae-ab47-d23edcbad56e | -6.7453 | -43.37912 | 2025-09-29 12:17:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e39d4390-0b7d-3067-8a47-74b1f1561d60 | -8.27789 | -45.53575 | 2025-09-29 12:17:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| bc420385-64e4-3238-9e1c-045ee6736722 | -8.88526 | -51.66741 | 2025-09-29 12:17:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9d21c335-0a60-3ad2-a308-2e70a8e41820 | -4.97599 | -44.50685 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 307d1141-bbad-33b8-a0ec-1d1414c53d10 | -8.1784 | -44.10605 | 2025-09-29 12:17:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f04f6515-aeef-3cf4-af4f-d64e9f624f94 | -9.05261 | -46.70742 | 2025-09-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2ac016f6-1051-373a-9a35-53049cb57023 | -7.85815 | -46.74241 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a98be40b-ff4e-36f2-9a05-8b841b95dfcb | -4.97736 | -44.49694 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f9054a12-b79d-3420-ab08-a569d6977fd0 | -6.21273 | -44.21425 | 2025-09-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c7f9016d-e915-3d59-b700-3e8524a3192d | -4.12131 | -44.23687 | 2025-09-29 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b65cdb24-3e62-3258-94b0-e4d608b81797 | -4.29022 | -48.26456 | 2025-09-29 12:17:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d4078e2b-3e0d-36f5-b5ab-96e9b2aa38cc | -8.83057 | -46.19323 | 2025-09-29 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 62af83a3-ef9d-3154-8e29-8ac65c94b977 | -6.76569 | -47.09819 | 2025-09-29 12:17:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 70c565e4-526e-3119-a418-3060a3eb1b29 | -9.46217 | -45.48971 | 2025-09-29 12:17:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| dc9cd58d-69de-3c35-b0a2-c1648f267cf5 | -7.82522 | -46.78316 | 2025-09-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 837293ae-3931-3a80-862c-165c8a40c3a2 | -7.22321 | -44.78838 | 2025-09-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 87e27301-fb00-3a44-8505-ec7e5e82af26 | -9.31274 | -45.70269 | 2025-09-29 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7389dec6-48e3-3df7-9dbe-34df0fa90368 | -9.06487 | -44.95896 | 2025-09-29 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |


[Clique aqui para ver as próximas entradas](README83.md)
