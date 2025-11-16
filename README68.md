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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b21fac28-6b5b-348f-a684-36e455005f33 | -4.4245 | -43.4271 | 2025-11-16 12:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f76cf9bf-37d2-3d86-9e1c-68788ec7f8ee | -6.7339 | -42.9498 | 2025-11-16 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 7a52e389-133a-3f6a-aed9-b13ca963a9a9 | -4.4246 | -43.4038 | 2025-11-16 12:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| b0085ddd-5813-34d7-a797-961cf526d5ac | -6.3705 | -41.7477 | 2025-11-16 12:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 7daacdfd-2d7d-39d4-9385-f66c79714f1f | -3.4087 | -41.4514 | 2025-11-16 12:40:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 751721ee-6652-3d0b-9c2b-cc52db8c03d2 | -2.5238 | -47.8115 | 2025-11-16 12:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 81485468-4305-3b7b-b156-3e65f798ecb6 | -6.7151 | -42.9515 | 2025-11-16 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 57cb0803-65b7-3fed-8899-3036e4635af0 | -4.4059 | -43.4049 | 2025-11-16 12:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 6679c0a8-af17-3c09-aa44-4b94e2139d99 | -11.71351 | -48.856 | 2025-11-16 12:40:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 651a2e2f-7163-3df8-921a-221e914fa7ce | -12.06763 | -48.21211 | 2025-11-16 12:40:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f41f70be-6661-3fcc-8c4d-0b8479dcfd27 | -12.46161 | -44.892 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 297d8f3b-d8a0-3d2c-bd68-ffefb2e5b8e0 | -12.69823 | -44.89013 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e2d7ba97-ec44-3d50-88f4-509cc9ba38f3 | -12.44523 | -47.90181 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 78f62a6b-def7-3a2e-8276-2b5bb471f292 | -11.01044 | -48.27645 | 2025-11-16 12:40:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2720bad6-2acb-3eb5-9d19-8058984b0318 | -10.4487 | -46.38821 | 2025-11-16 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| e469d84d-583c-3962-9607-1fa5e89a2e63 | -12.23029 | -47.51253 | 2025-11-16 12:40:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 4f7988d3-afad-3392-b10a-11b780ac1b84 | -11.06237 | -45.15603 | 2025-11-16 12:40:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7cfa4693-c1bd-3dea-abe8-31f13b030101 | -12.20473 | -55.06039 | 2025-11-16 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 028ff3dd-79ad-30ac-b825-890ea5188490 | -12.70212 | -44.85585 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 93093a2c-9578-3f68-8eae-0a1866f42ef0 | -11.80517 | -45.53973 | 2025-11-16 12:40:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b40fbe40-d756-3db1-b48c-2df79f8d8daa | -13.00822 | -44.77088 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| efc0bd38-2d71-3e97-9ed3-656912080f6f | -12.8802 | -46.45401 | 2025-11-16 12:40:00 | TERRA_M-T | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 72b55822-9e5a-3a4f-b48b-d541a9396d1d | -10.73192 | -48.26443 | 2025-11-16 12:40:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7ee1720d-b64c-3115-a576-b850d0134f6c | -11.72305 | -48.87325 | 2025-11-16 12:40:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3297fca0-852a-34dc-932d-72ff7abb8e2b | -14.50168 | -46.61813 | 2025-11-16 12:40:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 8f22bfb7-0575-38cc-a23d-c6d2187370f2 | -10.45148 | -46.36489 | 2025-11-16 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e2d53f09-9e1d-3eb9-b048-da60713a420d | -14.59685 | -45.2315 | 2025-11-16 12:40:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3f6cb84b-559f-3ef9-9655-80e3f29d1a8a | -14.49953 | -46.61115 | 2025-11-16 12:40:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 8067a2dd-aca3-31ee-9009-ab809c139842 | -13.24112 | -47.89733 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 46219c7b-69ed-3285-8c8a-8a0ee419ffd2 | -11.80666 | -45.53442 | 2025-11-16 12:40:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| e6c127ee-08d9-3938-a3ec-8a8ff4acf646 | -12.67535 | -47.17521 | 2025-11-16 12:40:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c4a9eeaf-5336-3a62-9e73-ddbd7f2dee4d | -12.77668 | -45.9203 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 4ab4aa3e-44d3-3db7-8ffb-e3612e8c957c | -13.24146 | -47.89043 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c2c26a7a-c4fa-3467-b9bf-faed94ffd34f | -13.23895 | -47.91114 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 94f0ac2c-8a32-3422-89a5-fafd45368fc1 | -12.69077 | -44.89585 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 0fa1e509-f7a9-3af5-82f5-a77afde82e0a | -12.4407 | -48.15169 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 60df29d3-83ce-38b3-9838-1e1ecc755588 | -12.81796 | -45.95422 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| d91e367f-ea21-35ac-bb5d-347238d4ace5 | -11.59376 | -44.89433 | 2025-11-16 12:40:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| f02a4389-1298-34f6-b7cf-99cb890575ab | -11.79157 | -45.53268 | 2025-11-16 12:40:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 0cc5886e-7d3d-38f6-8c6a-c880d6592d79 | -11.10221 | -55.69969 | 2025-11-16 12:40:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cd801eef-8c86-3b9b-80ee-1d658c6bc9c6 | -12.81812 | -45.95948 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 594f37b8-608c-3f41-b9d8-b59a7f41a7c2 | -12.40887 | -47.54553 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| c02abab2-a27f-3252-bce2-e86e605bbe12 | -12.8694 | -46.45929 | 2025-11-16 12:40:00 | TERRA_M-T | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 00b0cbdf-7afe-31d1-beec-45f7b2ba3e31 | -12.86597 | -46.4521 | 2025-11-16 12:40:00 | TERRA_M-T | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 811c1124-3ac3-384a-9e9d-d82009187ae9 | -12.45284 | -44.88462 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ee83b175-fff8-3d1c-badc-419acae8b547 | -11.71151 | -48.87193 | 2025-11-16 12:40:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| df3087e7-d90d-3fab-ad1a-8e660fc826c4 | -14.58875 | -45.22369 | 2025-11-16 12:40:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| f7143907-767f-3fe3-98c8-1628cb7d980f | -12.6944 | -44.86159 | 2025-11-16 12:40:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| b6807ce8-d0b1-382d-8dde-3c48b14146f1 | -12.41018 | -48.09153 | 2025-11-16 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a3a2e52f-0d9c-3356-b3c7-753524c51823 | -3.4087 | -41.4514 | 2025-11-16 12:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| f7fd2911-1f82-3705-86f7-48818a10cbb1 | -6.3705 | -41.7477 | 2025-11-16 12:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 0f132ef0-7863-32be-8f08-f6e4b78892ef | -4.4059 | -43.4049 | 2025-11-16 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.5 |
| a21c0001-bac1-33ea-b5d8-62674baee5c2 | -6.7151 | -42.9515 | 2025-11-16 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| fc0ddb5c-a814-3e42-8c2f-dd6feb9e5c05 | -6.7339 | -42.9498 | 2025-11-16 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 61534c7b-a2db-3c88-b5d1-ac6f4634e783 | -4.4246 | -43.4038 | 2025-11-16 12:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 04f74090-9464-3943-bfab-d81a70e1db89 | -6.2391 | -41.7115 | 2025-11-16 12:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 3b13bcd3-c988-3eec-bf5e-4202d1b1a457 | -3.6272 | -42.4639 | 2025-11-16 12:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| a2b73da6-3b47-372c-891a-da3f59b24ec0 | -4.4059 | -43.4049 | 2025-11-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| f32ff4c0-2768-3549-9482-3500a65fd70c | -3.2304 | -43.3486 | 2025-11-16 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| e5f171e3-bcea-34f5-a111-10ba247fc5c3 | -6.2389 | -41.7355 | 2025-11-16 13:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| f51c078a-527c-36e4-8634-0a1b621b2511 | -4.4248 | -43.3805 | 2025-11-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8c0551ad-76eb-3462-aa5e-3732b10c1ed5 | -6.7339 | -42.9498 | 2025-11-16 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| eea7795a-f3b4-3a46-8076-03dd8fb1c916 | -4.4246 | -43.4038 | 2025-11-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 531fb93a-3740-3151-9c5b-b6182904b13c | -6.6824 | -40.7981 | 2025-11-16 13:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 2e3c311e-e53e-3100-acb8-13f1df29ced5 | -4.4245 | -43.4271 | 2025-11-16 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 80da079b-5d81-34de-b433-80ef4a3b0e00 | -7.1429 | -41.7692 | 2025-11-16 13:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 9dc12c92-4dee-3ad9-9458-8f1812495d42 | -6.5411 | -43.4122 | 2025-11-16 13:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 2f75758f-7fd8-3b62-9abf-b07d8d611f48 | -3.2117 | -43.3494 | 2025-11-16 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 31c529a7-d08e-378e-b84b-61809dc63269 | -2.4201 | -45.7015 | 2025-11-16 13:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e0705879-05d8-3e69-8836-36499b34c40a | -7.1618 | -41.7673 | 2025-11-16 13:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 1ef00c27-65c3-37be-a9ff-8be4ad74c202 | -6.5411 | -43.4122 | 2025-11-16 13:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 63.2 |
| e7ec3868-bb75-38cc-87b2-817ae0c830e4 | -2.4201 | -45.7015 | 2025-11-16 13:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 762c7f64-19e2-37c5-b20b-da0ce21d9f42 | -6.258 | -41.7098 | 2025-11-16 13:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 146.3 |
| 6f5c678c-6415-3dbf-9f07-9cf7bf602acc | -6.7339 | -42.9498 | 2025-11-16 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 7ed29a67-e401-38db-8214-b1938ab659cf | -6.2391 | -41.7115 | 2025-11-16 13:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 171.5 |
| c907c558-61bf-3c79-9de3-84b36b0eba52 | -3.8436 | -40.7759 | 2025-11-16 13:10:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 92.1 |
| c1552004-0828-3bc0-9f2d-87d1c65fe778 | -3.2117 | -43.3494 | 2025-11-16 13:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| c00a8df1-a9fc-3344-baa4-3b19669d527a | -4.4246 | -43.4038 | 2025-11-16 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 16152015-9257-3a8a-849f-a2a46fa79dcf | -4.4059 | -43.4049 | 2025-11-16 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 183.0 |
| cf853e49-0dbe-3ace-a8b9-b614d0238b59 | -7.1618 | -41.7673 | 2025-11-16 13:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| c6b336f2-7e76-3004-9fb5-f718188af75d | -2.5238 | -47.8115 | 2025-11-16 13:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 19f2107a-ba72-3bb8-af5b-e3025c150be5 | -3.2304 | -43.3486 | 2025-11-16 13:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 73f2273c-4d7f-3e87-8688-a3f4850d2beb | -7.1432 | -41.7452 | 2025-11-16 13:20:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 3cd2ca34-6c90-3276-aaff-fed1bdc04844 | -7.7192 | -47.296 | 2025-11-16 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 6a518677-a45e-36bf-b96b-29098fe53067 | -4.4059 | -43.4049 | 2025-11-16 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 8815b760-d890-3f7f-9369-2ed4e90513d5 | -6.7339 | -42.9498 | 2025-11-16 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| a834bccb-e54f-3f95-8822-23a53594b007 | -3.2117 | -43.3494 | 2025-11-16 13:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 73c433d5-f997-3c96-89a7-189c1dc7fb78 | -6.2391 | -41.7115 | 2025-11-16 13:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 159.3 |
| a4387975-a472-368f-95b2-ca353f174770 | -6.2389 | -41.7355 | 2025-11-16 13:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| c558f2ae-34c7-359c-8409-94b2b28594b2 | -4.019 | -48.8147 | 2025-11-16 13:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6152aa84-5459-38a1-9409-3dc4297726e7 | -8.0573 | -45.6583 | 2025-11-16 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a042e4c2-bb46-3af2-85ba-9453a4e1304c | -3.8436 | -40.7759 | 2025-11-16 13:20:00 | GOES-19 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 120.3 |
| f03c3d36-2abc-3280-93e2-6ec00020992e | -3.3691 | -45.354 | 2025-11-16 13:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| bd197a47-1748-3897-9966-f32188cfe313 | -2.4201 | -45.7015 | 2025-11-16 13:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 717067c5-46ca-3332-8f3a-92274796e44c | -3.2304 | -43.3486 | 2025-11-16 13:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 6dcb705b-96b2-3ecb-8827-e81024f3847e | -3.4087 | -41.4514 | 2025-11-16 13:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 77ea6c3a-95af-343d-876b-1f403763b7c8 | -3.8625 | -40.7505 | 2025-11-16 13:20:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 101.2 |
| ce00bdc2-cfa4-36dd-8a62-b344f107d8dd | -7.5896 | -37.933 | 2025-11-16 13:20:00 | GOES-19 | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 2021306a-4676-3a91-830f-bfc05bdb722c | -6.5411 | -43.4122 | 2025-11-16 13:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 6af0980d-1616-3809-b8b2-13added0b523 | -2.5238 | -47.8115 | 2025-11-16 13:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |


[Clique aqui para ver as próximas entradas](README69.md)
