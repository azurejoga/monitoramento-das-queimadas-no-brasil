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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 654271c2-7117-3977-8334-9fffd14f3941 | -18.33363 | -44.03918 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac218905-243e-3b03-9e43-c1fa03961c96 | -18.33101 | -44.03783 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c8fd9e3-6d49-3c85-a9be-03d4400b881c | -18.32754 | -44.03694 | 2024-10-04 03:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a6955ba-e902-3bcb-9f22-e66a34251c8a | -18.21438 | -43.29866 | 2024-10-04 03:17:00 | NOAA-20 | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c1d2e26-d4c5-317f-88e3-ea7505ec7b32 | -13.66136 | -43.73176 | 2024-10-04 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fc180d7-ebef-30aa-b47f-c113b62b8525 | -13.66006 | -43.73792 | 2024-10-04 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5ff0d2c-08ff-3e98-80e1-c7ebf92b4416 | -13.48057 | -43.77884 | 2024-10-04 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f61a9a9-d3f8-3674-b159-28f5f8d484da | -13.47379 | -43.77752 | 2024-10-04 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dc95304-3b69-395e-93a0-932b331397f9 | -14.16542 | -44.65381 | 2024-10-04 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56f97828-9c6c-39a0-9b75-d71df23bc4ae | -14.1585 | -44.65189 | 2024-10-04 03:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3de6de88-f296-3198-9eaa-3db5fffc021b | -13.99382 | -44.03067 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 59bc8901-2e56-31f0-92d0-76a1b09971eb | -13.99311 | -44.02832 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b1dbf03f-43a2-37a7-81bf-e171ce095294 | -13.99242 | -44.03698 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 80d358f9-061b-3088-8052-84e4057c2877 | -13.99174 | -44.03466 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e4e232cb-817a-33db-a8cf-91fba8dd5fdf | -13.99038 | -44.04103 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| efe1d683-cef5-3ce4-a5d4-ddf6aecd7540 | -13.98705 | -44.02911 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8a442b24-371d-3f3a-b61f-45590ceaea21 | -13.98564 | -44.03545 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3187e730-c824-3fb7-958e-444a4ce05e63 | -13.98498 | -44.0331 | 2024-10-04 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23a8c578-87af-3f0c-abd4-9deff2e82e62 | -16.8945 | -40.61126 | 2024-10-04 03:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| df4305a2-0e56-37f9-a3b7-766cc9d52323 | -16.89385 | -40.61028 | 2024-10-04 03:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d247ec0-a9a7-3228-a84d-5647840faef5 | -16.89381 | -40.61466 | 2024-10-04 03:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c73e5804-88d0-3158-8ae5-7367150cbd5e | -16.89315 | -40.61366 | 2024-10-04 03:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d24fa5d-c27b-381e-890f-a17427e4a054 | -16.89314 | -40.61803 | 2024-10-04 03:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d61ba5b2-ed44-3262-95c1-7838d05646a2 | -16.89244 | -40.61702 | 2024-10-04 03:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b63aa542-ece9-373a-8294-c88aee894b54 | -19.44246 | -41.36192 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1013afd3-0e43-353d-a1fa-c61d3825cb84 | -19.4418 | -41.36505 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 75f3fe73-f9c3-32c7-9d39-a8f63bc751f5 | -19.44115 | -41.36815 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f2bf975-bc37-3003-aba7-8729206b10ef | -19.44043 | -41.37159 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6f00c389-5d55-3d29-99bc-73ba8e89ddcf | -19.43731 | -41.36027 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e5803d5-2df9-3ef3-a42d-b4088e73d903 | -19.42831 | -41.35088 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d2e4a47-afff-3efe-9f9b-2d78398e04d3 | -19.4277 | -41.35378 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 520ff73f-f10f-3a24-995e-c9ad7ae9a608 | -19.42417 | -41.34453 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 07d27d19-95d0-368f-aa29-29732b1a931f | -19.42349 | -41.34773 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c51717b2-6f3a-3c24-af51-62b0a466dfbc | -19.42285 | -41.35079 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4664ad1f-0271-3ecd-b623-efef7e57d8c2 | -19.42218 | -41.35394 | 2024-10-04 03:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a6e133ac-a307-3aaa-8ff3-9e4a2676a6f5 | -18.57124 | -41.28456 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| cb61c0ed-a283-3fdc-a882-0ff9c2f54060 | -18.57056 | -41.28775 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 20f62977-3346-39f2-932b-19fa0e3cc0ea | -18.56985 | -41.29118 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d48f501c-b16a-35f3-ab23-eb3acc26d888 | -18.56603 | -41.28289 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4f67fc2d-17ad-3bf1-a9b7-36aaf4dc6ec3 | -18.50899 | -41.30075 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ea4b7ab6-e1db-3790-a9b2-c58e4c4a9151 | -18.50825 | -41.30431 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| ab433632-95df-33a5-a46b-f12386c8c10a | -18.5066 | -41.30093 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 1e544c07-52b2-3d4e-96a8-771d6d1230a0 | -18.50583 | -41.30452 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5395c8f0-93ce-3b0a-9dcd-46a0e83ef4b8 | -18.50364 | -41.29973 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 83a0a84a-6c82-3f81-89a0-2d42a5459e4f | -18.50289 | -41.30336 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 5f529324-9a78-3d7f-9e7a-a43b1b6be871 | -18.50047 | -41.30355 | 2024-10-04 03:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9e89a4fc-6a1f-369c-b8c8-e8b35e082268 | -13.87555 | -42.02273 | 2024-10-04 03:17:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1f56bfe9-ce2b-3eec-a4ad-14d65d7a2080 | -15.51758 | -42.23598 | 2024-10-04 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10df0c34-42e7-3b84-9550-3b740067ea74 | -15.51653 | -42.24094 | 2024-10-04 03:17:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c569d20e-c51f-3c00-bf15-7b552021830d | -15.43327 | -41.14123 | 2024-10-04 03:17:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 808da1a3-fe47-30bb-9e79-7d28fd339248 | -15.43246 | -41.14519 | 2024-10-04 03:17:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b34369d0-2841-3e1d-bb6c-0233b8703031 | -15.2263 | -42.16512 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0a6bb819-6b07-32b1-ad44-5445bb054ab2 | -17.93484 | -42.20713 | 2024-10-04 03:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| af67c14b-2344-3fe2-870a-da449674ffad | -17.92933 | -42.20505 | 2024-10-04 03:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5c3efb52-c15e-3d95-8684-eebd5b24b3b8 | -17.92851 | -42.20887 | 2024-10-04 03:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| baf4eb1d-50b1-38dc-9bad-d70c77a667e2 | -17.92358 | -42.20411 | 2024-10-04 03:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f2fe1b0-5e3c-3c29-93ad-94e9787f7486 | -17.90842 | -42.19155 | 2024-10-04 03:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| efd87cd0-d2e6-30c2-adb6-2ecc7bbb904b | -17.62514 | -42.01992 | 2024-10-04 03:17:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 542f0671-40c5-3434-bebe-34bcc7174a6a | -17.61952 | -42.01854 | 2024-10-04 03:17:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 98ea0d66-22ce-3906-bb83-ee6dc102dc4b | -17.37888 | -42.62837 | 2024-10-04 03:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| efc78c6a-7ddf-3380-9193-7e6c80e037f6 | -17.37399 | -42.62249 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5796d052-6174-30b9-92b6-19889274e9e9 | -17.37301 | -42.62696 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1c56eee-190e-350d-bcef-c3ac9fd4b0d7 | -17.37204 | -42.63143 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d1b331a-b6a9-3502-9858-2fe24e46e93f | -17.36713 | -42.62562 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 68153dd9-8d29-3b28-9616-248e17f7bbed | -17.36616 | -42.63007 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fcf4bd69-26f3-3caa-956d-41a1fb2781d6 | -17.36342 | -42.62585 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1aedc2ad-03c1-3de0-9d22-f50a514aa6e3 | -17.36248 | -42.6303 | 2024-10-04 03:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d2214c30-9e04-3cc5-8326-8c19a6984d45 | -19.03474 | -43.19933 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e38e7f34-7efa-35c9-be0d-8b7de9d3e180 | -19.03021 | -43.19177 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 341b2236-da7b-3c8f-b38a-9155723f6d2c | -19.02912 | -43.19672 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8510581d-943d-3ce6-9ea6-a53bf99148bf | -19.02441 | -43.18998 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 91876228-b1aa-3e6a-95f5-3494c42abd06 | -19.02333 | -43.19485 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 95b819cb-1ad9-3851-a550-59935366c006 | -19.02225 | -43.1997 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3936583d-5d70-35dc-a18e-77bfba162957 | -21.7773 | -48.3976 | 2024-10-04 03:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e2aade2e-6599-336e-9c64-43f6d2ab9b0f | -21.778 | -48.3741 | 2024-10-04 03:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 85d10f05-fb6e-38c2-91ca-04d4c5e3f08b | -21.7981 | -48.3926 | 2024-10-04 03:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 545e9267-e288-32b2-8ea8-b02f97d28a24 | -21.7988 | -48.3691 | 2024-10-04 03:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b9b6147b-ba57-3373-b118-548c3c2f0e9b | -21.839 | -48.4061 | 2024-10-04 03:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 28965722-6359-34c7-a48e-afa655242023 | -21.8397 | -48.3826 | 2024-10-04 03:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 5d8e87a8-0a3a-3c4e-98b7-319917fea698 | -20.28766 | -43.51632 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7529a688-1d54-3d0f-9c3c-a808431f6ddd | -20.28574 | -43.51402 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ba7aaf39-30bf-3102-b7f4-1ec71009d566 | -20.28244 | -43.51209 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 27984a5e-6416-36a7-a6e8-d4cdd685d25e | -20.28172 | -43.51526 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f5cda8f5-4ff5-30d3-b021-411d67e38a61 | -20.27635 | -43.51172 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9012207f-f6c5-3ace-81ba-0922f85a79d6 | -20.27565 | -43.51478 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f6148e7a-37c2-32b9-9711-72f25d41c3ee | -20.26953 | -43.51458 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31749c14-8983-348f-b3ea-cf819ec46ccc | -20.26884 | -43.51761 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ca6e317-67cb-3db1-a7d9-b0b33cad461d | -20.26731 | -43.52438 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5220766c-39f0-373a-be92-d926fdf6402a | -20.26648 | -43.52805 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7561ec6e-70f8-33d4-a4e4-1ec2dc50753a | -20.26545 | -43.53263 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 188daeb7-9373-367d-a779-36498dc7309d | -20.26107 | -43.52462 | 2024-10-04 03:19:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b8ffcadd-6847-3ebb-aaff-5c1de76ac981 | -20.50479 | -42.37421 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7e49f3c1-49c4-335e-9ca4-5c1ec22055e3 | -20.50418 | -42.377 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| db0224ba-7d2c-3d88-be01-67069cde9032 | -20.50351 | -42.38005 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 54c9d9f7-e236-336a-8990-9632c247fe46 | -20.4999 | -42.37038 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 510c3b49-e8d2-36e2-a26e-4653e362d8a4 | -20.49919 | -42.37358 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 744a7d9a-7d84-3055-afb9-9a3651367765 | -20.49854 | -42.37654 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cfcb1713-45ca-3331-8ee1-abd181204428 | -20.49788 | -42.37956 | 2024-10-04 03:19:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 48616b63-96a6-3222-a0b9-1596d1ea71f3 | -20.43758 | -42.52199 | 2024-10-04 03:19:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2965cb7a-6c26-3ae6-bc7a-3058c59f7c02 | -20.43679 | -42.52556 | 2024-10-04 03:19:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README53.md)
