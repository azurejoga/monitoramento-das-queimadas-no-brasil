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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed72b4ef-e974-3313-93e7-6ac4378871c7 | -10.45509 | -44.94206 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e275b6e-6f12-3732-b24d-de84ad35da81 | -10.65705 | -44.4987 | 2024-11-30 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ab64758-76a7-340f-b5ca-3b9f75aab0ea | -9.0851 | -49.58228 | 2024-11-30 03:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d2b8ab-18d4-3115-9c4d-c5dc4e454025 | -10.46275 | -45.08898 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f85168e-077c-37e6-a85a-80d0c02bf5b7 | -10.65786 | -44.49409 | 2024-11-30 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e95a7b3e-78fb-3e7d-bf93-302978c58819 | -9.0788 | -49.58223 | 2024-11-30 03:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91e00cc0-0130-3e62-9402-f861707f62fa | -10.69601 | -40.33377 | 2024-11-30 03:49:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0ecc563b-ec46-34a8-a788-05e538b3d7bc | -10.42317 | -44.90542 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9f1ea92-ca36-3a8b-b29f-8d1313bf403d | -18.36056 | -40.0738 | 2024-11-30 03:49:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 26fbf7bb-9220-3040-9cf9-80ba857cb408 | -10.69667 | -40.3298 | 2024-11-30 03:49:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 62011cf6-0f36-33cb-aedb-bef8c3115de8 | -16.75706 | -41.05658 | 2024-11-30 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16e6bf72-0c9d-3903-a7af-ba902dada4cf | -17.67618 | -42.74548 | 2024-11-30 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc5359fd-5c8a-37fd-bb70-eccd06a6e952 | -11.4119 | -45.1026 | 2024-11-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 592c1bc8-2995-3e4d-a2d4-f8d47b112001 | -10.46359 | -45.09178 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32935289-2a2f-358b-8293-4371a3111124 | -20.41608 | -43.55373 | 2024-11-30 03:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 872a1e2b-240e-3370-8632-607030ff218f | -10.66156 | -44.49954 | 2024-11-30 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdbab933-ec05-3f11-b9d1-730a1812e4d5 | -20.49658 | -42.35514 | 2024-11-30 03:49:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6b599d0-cff3-3fcb-9423-3eed97a0cfc8 | -19.16817 | -40.14221 | 2024-11-30 03:49:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9ec0a6e7-2750-3d16-97b6-86fa3bbd695a | -11.07296 | -44.31766 | 2024-11-30 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09dfe1f2-9a0f-39dd-ba01-7db8854019ad | -10.5391 | -44.68478 | 2024-11-30 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1da8a24e-1683-399e-99f7-d805dc522d1c | -19.17207 | -40.13914 | 2024-11-30 03:49:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f7c0cf9b-28de-3e26-a897-06b3c2736b44 | -10.66237 | -44.49494 | 2024-11-30 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3389fd9b-49be-3c5a-a635-666cf69489ef | -10.74641 | -37.51567 | 2024-11-30 03:49:00 | NOAA-20 | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2033a1ae-fa1f-38ae-a99f-d5c531f413d6 | -20.24417 | -41.17867 | 2024-11-30 03:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 78f0d0de-4295-3154-8ea0-418f2214f866 | -10.59068 | -36.99092 | 2024-11-30 03:49:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa4d3647-0b3f-32e9-bcf2-5beb55c32e6c | -11.4128 | -45.09764 | 2024-11-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 474f1954-abc5-3054-a037-a89a3c2a7c14 | -20.2469 | -41.18306 | 2024-11-30 03:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 72e4980c-196d-3e2b-a582-a760a8310eac | -11.06233 | -38.43717 | 2024-11-30 03:49:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 69608178-a58b-3b52-a06e-cff16ac5e64f | -11.56339 | -38.12858 | 2024-11-30 03:49:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e19c5728-7d91-39dd-ad63-515bd76889fa | -10.42782 | -44.90635 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0df80bae-9372-3501-b82f-cc4a81fe818d | -10.75698 | -40.44607 | 2024-11-30 03:49:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9350df6d-b7b0-30c7-914c-c55c1c2928f1 | -10.53833 | -44.68751 | 2024-11-30 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cc60d4c-b2c5-3835-8309-bae99c48054a | -9.08523 | -49.58347 | 2024-11-30 03:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86f7b165-28d1-3881-aeff-259edad3d6c9 | -10.45419 | -44.94707 | 2024-11-30 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07e3968e-a9bf-3ca5-9cbf-5cbc9e41a20d | -10.65868 | -44.48951 | 2024-11-30 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ed49d93-279a-35d6-9033-1a0aa85e333b | -19.17149 | -40.1428 | 2024-11-30 03:49:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6a4b0c2b-bb64-30ab-a855-1341c6905358 | -20.50073 | -42.35175 | 2024-11-30 03:49:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e582d3e-804b-3296-8e75-a55fda9a0c02 | -9.04176 | -50.01115 | 2024-11-30 03:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7e94452-da2a-30eb-a9ef-b9bdc2ce75df | -16.68155 | -43.88366 | 2024-11-30 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d15218a0-2547-31ee-bd09-dfc4189c22a7 | -11.40816 | -45.09676 | 2024-11-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e206157-3dfc-3529-81a8-ca8dd66557e5 | -17.39476 | -42.65699 | 2024-11-30 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44912ae7-cda3-3de2-a867-08e79472a316 | -11.41654 | -45.10349 | 2024-11-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe86e169-f95a-3309-a873-4ab7888009db | -3.2591 | -53.6186 | 2024-11-30 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 79193924-a755-3034-b5e1-a797022f2aaa | -6.9344 | -43.5401 | 2024-11-30 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5f162873-a60c-3296-95e6-bd9d3c0dc544 | -6.8967 | -43.5436 | 2024-11-30 03:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| d8830c0e-c3c8-3448-9181-57a4c1862013 | -3.4975 | -53.8137 | 2024-11-30 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 51870663-aae3-3a49-ac95-1f0875d3f416 | -3.4791 | -53.8142 | 2024-11-30 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8a55d7d9-e143-3206-9a7c-f4843c231be1 | -3.259 | -53.6388 | 2024-11-30 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 35aadfbe-1a77-32b2-98e9-665d39be2462 | -3.2406 | -53.6393 | 2024-11-30 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 7c3b5715-ac08-3ffb-9635-723a42ac4cdf | -6.8965 | -43.5669 | 2024-11-30 03:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 1974d758-5945-30f8-928d-536d1f4b60cf | -3.6757 | -47.1395 | 2024-11-30 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1d822e8f-a6ce-3bb5-9892-0c1aa334b18e | -6.9153 | -43.5652 | 2024-11-30 03:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a3127e98-673d-316d-ad13-a11857154d4f | -1.6938 | -46.7833 | 2024-11-30 03:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| f41ea710-28e8-398e-bebb-fdec8d8c0733 | -6.9158 | -43.5185 | 2024-11-30 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| dd2e4f79-627c-35fc-b18c-cb34e753d822 | -1.6419 | -53.8731 | 2024-11-30 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0c0c859c-80b8-3919-8b92-a07e9126565a | -4.8713 | -41.2915 | 2024-11-30 03:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 555ac7c1-3d05-36c6-a937-f0499599ffeb | -3.6758 | -47.1176 | 2024-11-30 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a65fbb3d-f7e3-3d04-96df-9d80cfe8d916 | -6.9156 | -43.5418 | 2024-11-30 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 255.6 |
| 408b3a83-df92-3874-be33-23c81eb8495f | -17.6654 | -57.5645 | 2024-11-30 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 8e63fc22-9782-3b2a-9b89-3a035eabbbd2 | -1.0733 | -53.6378 | 2024-11-30 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8279aeca-41e9-35cf-9282-0471eaf412c4 | -3.4975 | -53.8137 | 2024-11-30 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0c725c1e-305c-34ed-bbfc-fabb6bdc6785 | -4.8713 | -41.2915 | 2024-11-30 04:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 9a63c686-9b9d-3e70-9da3-7aa4ec74fa1c | -6.9156 | -43.5418 | 2024-11-30 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 169d445f-2e7d-3d08-8483-e6ae44e7aad0 | -3.2591 | -53.6186 | 2024-11-30 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5d209e55-15d1-317d-bda8-5ea0a28157ce | -3.6061 | -49.9784 | 2024-11-30 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4a219945-fbfd-3ab5-a349-67514265bf68 | -6.9344 | -43.5401 | 2024-11-30 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 63b469bd-388d-364e-84cb-6155eb1abecf | -3.606 | -49.9995 | 2024-11-30 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ba3f7089-d624-3b23-a8c7-06c8a15eef8f | -3.259 | -53.6388 | 2024-11-30 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 54c482df-6a21-3040-a030-4e9e479b43ca | -3.2406 | -53.6393 | 2024-11-30 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f86bfe18-4ae5-3223-b665-0e4ea8c8bcb4 | -1.6938 | -46.7833 | 2024-11-30 04:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 39c65c7f-39c8-352d-971e-c75f55b832c7 | -1.6419 | -53.8731 | 2024-11-30 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 655b0f59-3116-32fb-b48a-1e4c66fda109 | -17.6654 | -57.5645 | 2024-11-30 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 54e029c1-0d92-365a-9659-2941298463c7 | -3.4791 | -53.8142 | 2024-11-30 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ae1dd3b2-efd4-3677-abb3-f73aa8210ce7 | -6.9344 | -43.5401 | 2024-11-30 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 9ee5016a-514d-3f0d-b422-fc3d4280b27f | -3.4975 | -53.8137 | 2024-11-30 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0b605d13-79c1-3fc7-a227-818b0c0502de | -3.606 | -49.9995 | 2024-11-30 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 5935f481-b843-34a2-9c6f-baa24ee6ed5d | -1.6419 | -53.8731 | 2024-11-30 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ed094e1a-d0cd-3f69-9a54-0cf4307f1a80 | -3.2591 | -53.6186 | 2024-11-30 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 791b4cbf-d1fe-33a2-8d73-bda56459d9d5 | -3.6061 | -49.9784 | 2024-11-30 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| c5b94de4-ec37-397a-a352-8667e32d3d08 | -6.9158 | -43.5185 | 2024-11-30 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 0c8e3bca-24b4-3774-8791-019f0a9bbe4c | -1.5868 | -53.8537 | 2024-11-30 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7a485842-f1e3-3a8c-9cc7-8de3fbf4854e | -6.9156 | -43.5418 | 2024-11-30 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 3407ffef-079d-369b-8f1f-7e1e117ea4a5 | -1.6938 | -46.7833 | 2024-11-30 04:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e6cbdb55-98ee-3f4e-aaf4-fdfcf7892f5b | -1.0733 | -53.6378 | 2024-11-30 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d6fbffa8-cc5f-32fb-95eb-713481b0c89e | -3.259 | -53.6388 | 2024-11-30 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 4e2736ed-7008-37fb-b5d0-4bb4f8556b28 | -6.9153 | -43.5652 | 2024-11-30 04:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 6f691dcb-2275-3b73-aa0b-b532913141e0 | -1.6419 | -53.8731 | 2024-11-30 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 2f75945e-8b42-36aa-90f6-1a1b67a86cab | -6.9341 | -43.5634 | 2024-11-30 04:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 25a167b9-ae3f-3386-a927-ace826452f25 | -6.9153 | -43.5652 | 2024-11-30 04:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 406d8530-8137-310e-9d0b-5e035d7c315e | -6.9344 | -43.5401 | 2024-11-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 571e52ab-7eba-39ef-97d4-b2319f317747 | -1.6419 | -53.8529 | 2024-11-30 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 905753cf-4082-394d-af73-ccbeda6c0f69 | -3.2591 | -53.6186 | 2024-11-30 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 05b2e141-232d-3fa4-9280-3569a2bcec68 | -3.2406 | -53.6393 | 2024-11-30 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 05ff7cf1-7a17-3c68-969b-a0667e6a0d40 | -3.259 | -53.6388 | 2024-11-30 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| b23b3501-9682-3ead-afb1-8cef47e95af8 | -6.9158 | -43.5185 | 2024-11-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 4507f1a1-77e4-3265-8aad-fb2aa8d6ae5c | -1.6938 | -46.7833 | 2024-11-30 04:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 8787a99e-3371-38a2-9fec-dd9e1e3eb633 | -3.5876 | -49.9791 | 2024-11-30 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6b2011d9-5dce-3e92-b738-afa6665530c8 | -3.6061 | -49.9784 | 2024-11-30 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 525d7ae0-0f9d-3ccf-a4da-2f1ebf62b1e7 | -6.9156 | -43.5418 | 2024-11-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 9c1f86c3-3902-30ba-8bac-69e0c6a35db8 | -3.606 | -49.9995 | 2024-11-30 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |


[Clique aqui para ver as próximas entradas](README24.md)
