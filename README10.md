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
| c432f0d6-cf47-3a4f-af0e-8e6e3baddb82 | -11.45936 | -47.31587 | 2025-08-08 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e959689-0561-3b01-93fb-94a20b525c5c | -13.29564 | -40.35658 | 2025-08-08 03:45:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c1a602a-0ce4-3e11-93b3-325c81da9c49 | -11.7617 | -47.50705 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca67b366-b44a-36d1-bf14-d00d6f5e1fe0 | -11.76807 | -47.39168 | 2025-08-08 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c2290ff-bf69-3968-bc57-27a068b11d83 | -15.83814 | -41.8484 | 2025-08-08 03:45:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76ceec4a-991d-37ce-afda-1e21d6b2dae8 | -11.44113 | -45.13483 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6fa7726-cb0b-3f1e-a939-90eae892712b | -11.80569 | -44.9328 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1b9ef0a3-245a-3334-a432-1004c83efc07 | -11.45757 | -47.31576 | 2025-08-08 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18ca26dd-7ee4-3bf8-a437-ba00cbd04c65 | -11.77455 | -44.96113 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c26c3994-62f0-3cee-835d-059085496521 | -11.80014 | -44.93356 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c001fc1b-f775-33ee-9e4f-f4dd4da9cabb | -17.57325 | -49.08613 | 2025-08-08 03:45:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2715496-3aa1-35c9-9911-1a93306c6257 | -12.6176 | -48.11044 | 2025-08-08 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c68bc1-297e-3f51-8da3-20be46316dc3 | -11.76724 | -47.39594 | 2025-08-08 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7ecc6aa-a55e-3ee9-bf75-91f01383d771 | -15.83727 | -41.85338 | 2025-08-08 03:45:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7643224c-cfc1-35d5-8d0c-1a5d808ed9ba | -11.43756 | -45.13996 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42358af4-59c0-3871-9e1b-32a53bbe8700 | -11.02476 | -45.07203 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6aecabc3-bdc4-3fa0-b9af-17c26eae249c | -14.48823 | -42.18031 | 2025-08-08 03:45:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b3a6cc55-d665-395e-8fa5-d97abdbb8955 | -12.35458 | -38.27794 | 2025-08-08 03:45:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0ce3d031-1717-3100-b6d3-a7ce24f48400 | -16.72266 | -49.13284 | 2025-08-08 03:45:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ac0f64d-b363-3d77-91b4-3a4536c52f09 | -12.51778 | -47.11813 | 2025-08-08 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b016801e-7065-37ac-87c6-4ae5cfb6ea46 | -12.70199 | -46.38229 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d13d1f9-0ff7-3f58-a86d-435203cd1235 | -12.71541 | -46.3789 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75b0a461-b9e9-3baf-a335-ad7687ecf915 | -15.04329 | -42.46369 | 2025-08-08 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95b0384e-8ff3-3f2d-bcd3-32507a0d6c51 | -17.65638 | -42.51366 | 2025-08-08 03:45:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a268f539-2186-3441-afab-c21e26fe4ff6 | -12.89358 | -43.77732 | 2025-08-08 03:45:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c127858a-2cf6-3e11-bc74-40914663f273 | -11.75003 | -44.95351 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2750763-39fe-34e7-95d3-1940c8f0cc6b | -13.29855 | -40.36152 | 2025-08-08 03:45:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3635c20e-ee5b-392c-a604-ade8683ce304 | -18.61477 | -44.26321 | 2025-08-08 03:45:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78909cff-860d-37b0-9e38-5cf3e23a6b29 | -15.90063 | -40.02687 | 2025-08-08 03:45:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6f3015c-a531-3395-aaf8-102a00dacc8f | -11.43481 | -45.14019 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6acf62f6-1bf5-3f43-a629-eb6882ca0b2f | -11.02419 | -45.07506 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b5e9cd0-8eaa-351a-9208-08f6486283c5 | -11.02534 | -45.069 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40ab999f-9087-3919-869c-b960eef68751 | -13.03038 | -44.08811 | 2025-08-08 03:45:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4cfbc45-fd00-3efa-a951-8dc7fd03b344 | -18.22065 | -45.627 | 2025-08-08 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2565aded-7f04-3ac4-ac31-c4eb35a783dc | -11.8057 | -44.93161 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d391cdd3-f878-3636-88b0-e2b98b3c4366 | -14.87811 | -46.85658 | 2025-08-08 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b82afd6-2ada-3ed5-b857-b5de2c3bf935 | -15.89714 | -40.02623 | 2025-08-08 03:45:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d01c021e-cdfe-32eb-9937-d5aa6fffa3c7 | -10.82911 | -49.37699 | 2025-08-08 03:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e396c6b2-f627-31ef-9c21-f928b829800d | -18.91287 | -40.61213 | 2025-08-08 03:45:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6df81ff8-5f33-304b-892e-eef43a798fef | -11.78394 | -47.51861 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8389952-f7ed-32c5-a0d8-6a6fdb3d764f | -12.48842 | -47.50356 | 2025-08-08 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef0ff17c-388e-3e3f-8af1-0580b6af8827 | -12.72151 | -46.37651 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7237965c-a9a2-3afb-9124-5098b3ef7ab4 | -14.87881 | -46.85305 | 2025-08-08 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e7ca9954-34ed-32e8-b1a8-f9446f01774e | -11.76757 | -47.50839 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5b1906d-b4bf-359e-8806-b8686486308f | -11.75269 | -47.5025 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d3ddaab-0177-3d73-a4f0-5b8e6fa3fd42 | -18.61901 | -44.26405 | 2025-08-08 03:45:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c25ca04-1e67-32f3-ab30-e5d76fb69371 | -11.77895 | -47.51287 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11b99c4-23d5-333b-bbef-9042dbb727fb | -12.70129 | -46.38592 | 2025-08-08 03:45:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60f8a8d1-aca6-33fd-9f89-5da7aacd8d3e | -18.29043 | -42.86816 | 2025-08-08 03:45:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4f1573e2-1f6e-3629-aa70-2f6e1c5cc914 | -11.73542 | -45.00352 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d3a4d99-5c00-3bf7-8110-65b7a56eba8b | -12.09628 | -44.73375 | 2025-08-08 03:45:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d31184d5-d988-3d6e-bd70-4a251cbbc76d | -17.57439 | -49.0888 | 2025-08-08 03:45:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2162b1e9-445d-3e17-9c3c-26db0edaa278 | -11.75058 | -44.95058 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7d2bb0-9725-3df8-99e3-2a2fe23ae1ae | -11.80124 | -44.92887 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bbc6c6d1-6061-32b8-a735-a6991af9fcd9 | -16.4712 | -43.42442 | 2025-08-08 03:45:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c3ab010-78b1-3be2-a99d-abb5a41080ab | -11.8007 | -44.9318 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ee82206-6d48-3934-a471-4b9684828086 | -11.44054 | -45.13791 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 693f0803-d6e9-3beb-81c2-b189086c42f2 | -11.56756 | -44.85322 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adc19d26-e433-3a6a-a25d-39ff45f37a64 | -11.43815 | -45.13681 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12bd9d63-cfb4-3d9e-a9d0-6ee39ecf2ff0 | -18.76229 | -40.9983 | 2025-08-08 03:45:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 70071abd-0c88-3c6e-a14c-b1e266201730 | -13.35961 | -43.76493 | 2025-08-08 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b0e33e6-a9e6-3f55-a3e8-b0292c80a8bd | -11.77824 | -47.51638 | 2025-08-08 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ea4e6cf-0fdb-3fd9-924d-89a3a8c07cd0 | -11.43994 | -45.14103 | 2025-08-08 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6da2fd3e-8ebe-3c2d-a009-a9ecc1dd2336 | -11.0289 | -45.06602 | 2025-08-08 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9634c8f-04bd-311e-9186-1c403f7a7214 | -19.18383 | -45.05532 | 2025-08-08 03:47:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503877bc-9503-38db-9f76-43f2fc41f1ae | -22.8157 | -46.42111 | 2025-08-08 03:47:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5207613a-6635-354f-a8d1-2178b0982dd3 | -20.0623 | -47.58211 | 2025-08-08 03:47:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c8081ad8-6608-3129-822e-259909924e24 | -22.12866 | -44.3476 | 2025-08-08 03:47:00 | NOAA-20 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef90812a-ebf4-306a-b69b-42ca7b7528dd | -22.17574 | -47.12443 | 2025-08-08 03:47:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11a4a67d-dc85-3088-aaaf-c302c8737291 | -19.97092 | -44.96273 | 2025-08-08 03:47:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 641fe481-dac3-373d-8ba3-39841b709d1a | -21.7868 | -43.33706 | 2025-08-08 03:47:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8934703a-509a-3a66-aaf7-abcbef97af9a | -22.21873 | -44.73186 | 2025-08-08 03:47:00 | NOAA-20 | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5e8560b4-70ab-3ce0-84e5-29d493f3e29f | -24.54626 | -49.05359 | 2025-08-08 03:47:00 | NOAA-20 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01b20fb1-aab6-3851-a770-55a02776d855 | -22.04201 | -47.02613 | 2025-08-08 03:47:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aab72bea-8024-3ccf-b842-1359d0ee092d | -20.05658 | -47.58407 | 2025-08-08 03:47:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff10380d-2238-3616-80e1-fd91cebac574 | -19.30294 | -47.43758 | 2025-08-08 03:47:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17202fde-8e6d-34b4-a7cb-62fd4079669d | -19.90122 | -41.3638 | 2025-08-08 03:47:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2626952a-67df-38af-966f-7ff21c5e9162 | -19.65754 | -43.69519 | 2025-08-08 03:47:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17789180-a6b2-3769-a048-69dd81a820c7 | -22.92425 | -45.4994 | 2025-08-08 03:47:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 747f8627-d8c6-3b26-8955-db3132a145e2 | -19.18514 | -45.05252 | 2025-08-08 03:47:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9726fc0e-6f14-35b5-b686-842cf1d5fc9a | -19.76935 | -46.56911 | 2025-08-08 03:47:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6f96979-5309-3583-b074-d973bb093d55 | -19.18914 | -45.05164 | 2025-08-08 03:47:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bed5c00-b235-3f1d-a178-3b67f946a626 | -20.33418 | -41.44388 | 2025-08-08 03:47:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4172a496-2a20-3e92-8480-58af6eebd58b | -18.91367 | -47.55542 | 2025-08-08 03:47:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 751d29f9-b1ef-3b20-ba84-8f5383bfb41e | -22.24253 | -48.5398 | 2025-08-08 03:47:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4250b7c2-9356-3261-a07a-6b3626dbc68a | -20.38959 | -41.91809 | 2025-08-08 03:47:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ddb60a16-6626-3a32-a12a-d54b89197f11 | -21.00266 | -43.27558 | 2025-08-08 03:47:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| e511b4e3-c89d-3a85-9556-f532aee44924 | -19.22491 | -46.5877 | 2025-08-08 03:47:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 95fc336c-62fc-3291-8652-faf9e080fb83 | -19.18824 | -45.05621 | 2025-08-08 03:47:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d95767a9-f761-3e32-980d-96406158e2e7 | -23.0297 | -47.5307 | 2025-08-08 03:47:00 | NOAA-20 | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ed916b50-e2ab-361a-9c12-189ea059a0b9 | -18.91296 | -47.55874 | 2025-08-08 03:47:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 81acf931-1e3b-3d14-a857-2bef912eccbb | -20.14519 | -41.75147 | 2025-08-08 03:47:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b115d5ad-3a3f-3129-bba2-bda4f5fef71f | -20.12455 | -43.80317 | 2025-08-08 03:47:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 74d3df10-bb1a-3661-b481-bd0c8bcf947b | -19.95073 | -45.17917 | 2025-08-08 03:47:00 | NOAA-20 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa2cacf3-1835-3554-8d4a-560089898e25 | -19.75879 | -45.23139 | 2025-08-08 03:47:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce1b5cc-7260-3504-b0c2-086c391ca456 | -20.21331 | -41.3861 | 2025-08-08 03:47:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2eaab1c2-f5bd-385a-a7ab-7d0522a1cbe5 | -22.18044 | -47.12564 | 2025-08-08 03:47:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90b4c7be-704f-3345-93a8-3c803c03cb23 | -21.74452 | -45.81674 | 2025-08-08 03:47:00 | NOAA-20 | CARVALHÓPOLIS | MINAS GERAIS | Brasil | 3114709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0d873b6-68e0-33eb-829a-d501caa57088 | -20.14676 | -41.52106 | 2025-08-08 03:47:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb5b1d83-784e-34f2-8403-924a04fe5066 | -20.06294 | -47.57905 | 2025-08-08 03:47:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README11.md)
