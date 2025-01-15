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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbd5fef7-4d13-3e49-bf59-42d979cb2a00 | 0.86593 | -59.29986 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fed721a-0b5c-3e9b-bc8a-a8c2daf58de1 | 1.32362 | -60.03333 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8aeb52f-b7f8-3d8d-9dca-7a6c1dce663d | -2.49203 | -54.13259 | 2025-01-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45026c33-c5f2-3817-a411-9cfa1c8a8d1e | -3.32362 | -53.86138 | 2025-01-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55ace94c-4ac1-3968-b2e2-e9333015452b | -3.31127 | -53.86446 | 2025-01-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7f72225-046f-301b-8ea1-69a5f410a534 | 2.09703 | -61.81713 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8c2c09df-52be-30af-9285-f520aa3b9c8c | 1.32486 | -60.04131 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c2ad7ef-e591-3c0d-96c6-d0f2820cccd6 | 1.32716 | -60.03279 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e23a0916-c8c1-3635-aea4-6c7d24631911 | 1.16974 | -60.49154 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 328091f6-aea0-3ffa-9083-c6a4f390bcc6 | 2.09291 | -61.8437 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dac65eb3-5dba-3dcc-8d3e-53f1bf05206f | 2.09633 | -61.83491 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d91bd735-9deb-3f0c-a251-3c6dffea47e1 | 2.36319 | -60.93773 | 2025-01-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b2ed49-cbc7-38d6-b4e0-2505ce549bf9 | 1.32027 | -60.42759 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1c0f781-7eba-3b03-870f-e03abad21be7 | -3.02677 | -54.58811 | 2025-01-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daf565ca-1850-3a3a-8c44-c45de0ff8282 | 1.11881 | -59.45938 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9f0778-44fd-3578-834d-5d138fa1f472 | 1.18122 | -60.49408 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98079271-702a-300f-91ce-d13865514a7c | -3.5611 | -53.30315 | 2025-01-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89b29495-ea68-312f-b954-f5433890f367 | 0.96095 | -59.54881 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf852fbf-587c-3666-ba48-c63ac8d9e8f0 | 0.64638 | -60.50317 | 2025-01-15 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b33a65c-d14d-3b6a-9bce-14c6bc2d3e54 | 1.04763 | -59.54299 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92744d3a-c881-306c-bd0e-52683c4dce93 | -1.53343 | -53.98726 | 2025-01-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c72f3d-ff6e-371e-ab7f-7d986ada1261 | 2.10645 | -61.82609 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 92cbae34-72e7-3100-9096-11947437c282 | 2.28099 | -60.21827 | 2025-01-15 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15a145c2-eaf4-3a8d-b107-9a2742c160bf | 1.0126 | -59.56765 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bf415d8-251c-3442-8bcf-38796a1d7451 | 2.09001 | -61.84625 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da9953de-c6d9-3c2a-a326-40cc1e848d73 | 2.08922 | -61.84119 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ba18919-ee67-3eac-8e80-e5f7491b9b77 | 0.63649 | -59.94963 | 2025-01-15 05:16:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ed6dd26-1c8c-3014-92bc-1327092d0907 | 2.52013 | -60.99751 | 2025-01-15 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 84e1e75b-b4ba-31f8-81d8-de2bdcd57cf1 | -0.11737 | -60.67611 | 2025-01-15 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3eb25488-e221-3b75-83ab-5a404b76d0f8 | 1.31601 | -60.42397 | 2025-01-15 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c98cb486-a173-339c-9da6-5572a50d2737 | 2.09367 | -61.84874 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d8a4421-bae9-3456-8641-580e4d1ac396 | 2.09611 | -61.83801 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e8429991-61f4-3ef1-a698-dffc7e70ac1e | 1.12389 | -59.42409 | 2025-01-15 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f418af22-43f5-3f4c-9b19-edeaf373b0d9 | 2.09626 | -61.81201 | 2025-01-15 05:16:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ba9072ab-def9-34c4-a5b2-3a3865a78c12 | -9.26352 | -60.31777 | 2025-01-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51a9d0bc-1599-35df-80b2-c4f1ac78f422 | -9.25965 | -60.32075 | 2025-01-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fd30418-cf40-36eb-b224-78d2529508d3 | -9.26021 | -60.31724 | 2025-01-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6060bef-0b01-3e14-9321-4706934208e0 | 2.2889 | -60.2076 | 2025-01-15 05:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 98f14d42-cf01-3294-9885-5a0bb31ce3d9 | 2.1039 | -61.8166 | 2025-01-15 05:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 28dbd624-ea20-3652-b03b-b6f942fdb967 | -22.10831 | -49.62944 | 2025-01-15 05:22:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d26597da-2d2c-3cfd-bd43-ce66b0067ee4 | -21.45179 | -48.60685 | 2025-01-15 05:22:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 421d8965-c700-3148-a4ea-056798e9ff98 | -21.88258 | -56.11385 | 2025-01-15 05:22:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d334bdb0-b90b-3865-92cb-7580cb7553de | 2.1039 | -61.8166 | 2025-01-15 05:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 068882aa-8b53-33d1-b407-1b18ad104cba | 1.3217 | -60.4262 | 2025-01-15 05:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| fbf6d5ae-665b-3f61-ad99-767d344c5d04 | -8.9505 | -35.1752 | 2025-01-15 05:40:00 | GOES-16 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| 766cfc64-d78f-3297-9e17-f229476fd2c4 | -8.9313 | -35.1784 | 2025-01-15 05:40:00 | GOES-16 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 124.8 |
| b3f0e855-32c1-35af-9f28-7f47cc54b03a | 2.1039 | -61.8166 | 2025-01-15 05:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e55572ca-f189-31ed-8d5e-764a965e24cf | 2.2889 | -60.2076 | 2025-01-15 05:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| bfeaa522-8706-3a65-b07b-88788d08e2b9 | 2.10956 | -61.82534 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f9412a89-b08c-34ab-9ae1-3badceb61b07 | 2.10192 | -61.81842 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 458c708e-3bd8-3a66-9e25-127d90da8219 | 3.04692 | -60.24031 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ead6a4e-aeab-359b-804b-2f0e58870a52 | 3.04434 | -60.24147 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1ef28e-0049-3ec5-8775-e3476484afa6 | 2.28305 | -60.22029 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a48fdabc-e170-305c-ba79-0282f37ac878 | 1.32896 | -60.03477 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e28cc8ce-c746-3355-a1c5-9f1eb56fd1c2 | -1.55627 | -54.43895 | 2025-01-15 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e85ca6ba-4170-3a54-9887-4b0b976a0df9 | 0.66626 | -59.59632 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 921ccdbb-8d6e-35b9-8375-e9cf75ab2d68 | 2.09509 | -61.81948 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744e349f-d35b-3f8e-a83e-5924efb66caa | 2.10706 | -61.82888 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f8c19617-9fe6-3822-be47-7345fdb5b51f | 1.32654 | -60.44113 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc0fa41-43a1-338b-86cf-9ba5acda39c6 | 3.03903 | -60.2373 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f5472e3-72c4-369d-9f01-02917d17c96e | 2.09451 | -61.81582 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cec93cff-bdff-3851-8283-e8b34f83ad0a | 3.04298 | -60.23318 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a4a0a1a-dff8-344c-b090-9ebf7f17a533 | 2.51635 | -60.98849 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6446a58-1301-30d5-aac3-fc5de825da31 | 1.1234 | -59.42553 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdebe3d7-f125-345f-aef2-ad554fcfe95d | 2.09912 | -61.84515 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d3b6e89-b1d3-3968-8d52-0eef3b6f60b9 | 3.01618 | -61.29168 | 2025-01-15 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bab9aed-7f41-30b0-a121-e9a3df74cfb9 | 2.51698 | -60.99239 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e8b3946a-614c-3350-9165-c70f7fa9cafd | 2.09114 | -61.83886 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e3e8cbb-9f5e-3089-be2d-31e69bf0c10f | 2.08772 | -61.83938 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6647b248-15de-3a65-ab91-2e3471546a9e | 2.67344 | -61.18152 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79981cc9-9d28-3aec-a769-a71970ea999b | 2.09455 | -61.83833 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd8c6ee3-d6b4-31cc-9b68-996c900d4172 | 3.04366 | -60.23734 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1407cd8-f620-323c-8c85-6991dd70ae5a | 1.32219 | -60.04029 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f0429d9-05ec-32dd-b1ec-41b6dfff3fa9 | 2.09793 | -61.8153 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7fc3a44e-ba2c-3030-b14a-0583ff5f7f20 | 0.66673 | -59.59437 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb65e333-20a5-3382-8385-12b5e49d6e83 | 2.28966 | -60.2149 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cb61cd74-2f42-3748-ba58-0a6ad2c66bdd | -1.46901 | -54.19302 | 2025-01-15 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64eb4e0c-0577-36a3-bbda-7230d4606e3e | 0.50604 | -59.33902 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5710e0e-a5db-3094-9ba4-bc9ba85613c5 | 2.94868 | -60.18342 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 198913ba-1117-3d1e-a019-a0a74976a541 | 2.09394 | -61.81216 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e55f3262-083f-3f5c-9fc1-21f56d3361e0 | 1.31857 | -60.43805 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2a831b89-8259-3169-9609-40020a7ba351 | 2.28337 | -60.21843 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ec61611-d55a-3c15-b64b-6d1bacf1ed31 | 2.52112 | -60.99572 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| b4803331-be38-32f0-bb37-34b28c93a135 | 1.31658 | -60.42538 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b3e53d00-2b4b-3e90-acbb-6ce234a5cee0 | 1.32522 | -60.03532 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1545e3ae-e986-3494-aabd-5638d1727441 | -1.47503 | -54.19161 | 2025-01-15 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a5e7cc-b550-3588-82ba-f58b19d9ffa1 | 1.32452 | -60.0309 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7c3cf38-7185-3aa9-bfc7-6e77bf854580 | 1.11329 | -59.46172 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b99d6c23-0204-35aa-b7df-829991655463 | 2.09398 | -61.83466 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8790f16-0557-3975-bf01-5b6b021137b8 | 1.31559 | -60.44285 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5abbf158-6f61-36fd-b991-0b14eb1846ff | 2.10135 | -61.81477 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 64b568b1-2257-3dfc-a0d2-043405a723d7 | 0.72424 | -60.11726 | 2025-01-15 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596b1a07-5bc9-3776-ba1b-fd51b016e521 | 2.0923 | -61.84619 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e3b7de4-7181-32af-824b-eb4522716cb5 | 2.10648 | -61.82521 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 16026d0f-8037-3dcd-9bec-c385931339fb | 2.10476 | -61.81424 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 20782e17-62e9-35fc-90a2-1323435dc229 | 2.10139 | -61.8373 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd9e24fb-211e-3a05-8cb6-06d986daae63 | 2.09571 | -61.84568 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b44f612-dc81-3f7e-87d0-b6fe3ae5a796 | 2.10839 | -61.81802 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06ea8b9a-1cc1-320b-9df7-5f7d872f6c92 | 1.18204 | -60.49308 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f53ec0-581a-36f5-b7da-f3286e3c94f2 | 1.31791 | -60.43383 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README6.md)
