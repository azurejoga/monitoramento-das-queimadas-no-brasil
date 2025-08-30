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
| b2fbcf41-bc7e-3c2c-bcc3-93b77319d338 | -9.33491 | -68.21964 | 2025-08-30 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11968117-0762-3b38-a322-16d17b55a362 | -8.959 | -65.96136 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f468627e-185c-3269-aef5-2a318c8a67ad | -9.43954 | -62.31984 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f160568-42c0-3ce7-8e26-6e91b802aad6 | -8.88073 | -60.7298 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5bb6cf2-7913-313a-aa7d-21e0a11b70e2 | -8.67729 | -62.43716 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61a829f5-2c0c-3678-b733-d9871a4b43cc | -8.87407 | -60.73669 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cd71635-98c9-3aae-91a4-5f10998ad9d0 | -8.18139 | -61.36836 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c835b72e-a898-31df-97fe-56505ca076e6 | -9.44221 | -62.32003 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0adcca5f-e279-30c6-a1fe-ec638b549713 | -9.73099 | -64.91467 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32489340-130c-36ce-9daa-bd4dffe319e2 | -9.44954 | -60.54844 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2f2ca8db-168d-3063-a022-f490bdb0fba8 | -9.15132 | -59.56463 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d442bc36-50e9-3053-84c4-213ba0a70459 | -11.39551 | -63.24679 | 2025-08-30 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ea4d1c9-5065-3051-90c6-b7798bb6c421 | -10.4607 | -67.74245 | 2025-08-30 06:01:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3462faa6-bc7a-3baa-80fe-c5bac4ed5e94 | -9.45618 | -60.54868 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e556294b-16c4-3b19-bc40-79dfcc52beb5 | -9.44419 | -62.34532 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aedd6d20-c913-36dd-b4a9-ba00b4aea0dd | -8.75102 | -69.44733 | 2025-08-30 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83c283df-a3b4-361a-bef5-e6eea3c187d1 | -9.11464 | -65.76901 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b4993ca-94d8-31fe-9f47-e553a1d1ec83 | -8.52775 | -64.01138 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca2cb58-81b1-3a35-9c6e-e6cf4a905e5f | -9.90006 | -67.01437 | 2025-08-30 06:01:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c6e7da0-afcc-3a78-b602-e224c9382ed2 | -8.56892 | -70.06084 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea4dcf71-6441-304a-b4da-f10efd8dd4f6 | -9.44989 | -60.5521 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f7f29e4-30d4-367f-9739-30c199ece4b3 | -8.98935 | -69.37702 | 2025-08-30 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d02cbb-1fd5-31be-a8ab-39b56253cb9a | -9.44175 | -62.34198 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8945a5ef-ad68-3d4d-9d25-d7d108c37166 | -9.45953 | -60.5618 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d898e8-59cb-381c-9bff-3dc7f74ab083 | -9.43631 | -62.32543 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df0b80b3-9615-33a9-a700-13a30a4cbb0a | -8.18919 | -61.37529 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91cb5e2a-86a3-3133-950b-736696031462 | -8.17934 | -61.36691 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56e50746-6ca1-303c-b14f-8af6dca7c715 | -9.45321 | -60.57277 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e66abc3e-682d-315e-bd44-cd18ba06161d | -9.43909 | -60.53852 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5f719f0c-bfc8-362e-ab20-eee27c774624 | -8.03771 | -70.0664 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4536e21-c92e-35b6-bce6-d5914a3a29d9 | -9.13575 | -65.82294 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d77eda2a-2777-3686-96c1-31be1fba5064 | -8.92786 | -72.82412 | 2025-08-30 06:01:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ac47ed8-aa97-31d7-a6a4-df4585992b40 | -8.63675 | -67.25276 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3c49e3a-fa3d-3982-957d-cea2c53864ed | -8.67747 | -62.4371 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a230373-f511-3a81-b8cc-a6f1e62c9d09 | -8.17557 | -61.37099 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67ed61ea-740b-3b37-951d-19b0f6222287 | -9.44265 | -60.56339 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96736a37-1021-36fd-a08a-0b8ba7a23363 | -9.46083 | -65.42915 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ee4639e-f13a-3713-af3c-8fb796da9f48 | -9.46266 | -62.36354 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c168ad1-735d-391e-a78d-4b4c5dc5e73e | -9.45008 | -60.54431 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cbca559d-eaf8-3879-b46e-8492696f3000 | -9.03125 | -63.55428 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59cfb15c-04af-359a-952e-0e72761cfb2e | -9.43939 | -60.54208 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 98abf302-8bda-31a8-bc1a-ed83e94d056f | -9.43989 | -60.538 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 972d1108-e3cc-3d19-aa08-c6eb0c2fad3d | -8.66349 | -70.04318 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 434329de-c209-3cd0-bf6c-6e6f8688ea85 | -9.45477 | -60.55336 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5cbdb5c-2933-37ca-9dde-86302eee614f | -9.44534 | -62.33632 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bdaf8b1b-0196-3ebc-a9df-7ef836504e77 | -8.61438 | -72.38969 | 2025-08-30 06:01:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ae67628-de61-3b8f-ba6f-ebd7bf932af7 | -9.46424 | -62.35136 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 299c33be-4534-37a5-a005-98c6627da002 | -9.82279 | -63.85298 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71604e31-c725-3040-a12c-ea48de513ceb | -9.46344 | -62.3575 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f85fcce-44f8-316b-a113-e7c35db839a3 | -9.45402 | -62.34988 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 186b8141-d54f-30ce-b1a4-62dad6c69fe7 | -9.44094 | -62.34798 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8e73e8e-7cba-370c-b6ca-dfd0e678edbf | -8.59369 | -60.58524 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c34df56d-dcc8-3dbb-a65f-b53996ab1fc7 | -9.43747 | -62.33514 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04063df7-0422-3553-b6da-ce2652863894 | -9.27766 | -60.46085 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5aa7a08d-0719-361b-b238-0b2869f784ca | -9.11312 | -65.77974 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75d70609-2274-33b1-a5e5-2f4dd0823b63 | -9.77787 | -64.25375 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a16facc-b801-3291-8ac9-a5da9f93da39 | -11.39128 | -63.24039 | 2025-08-30 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb437c1-328d-3d60-98f7-e23d70a1a0bf | -9.41713 | -60.57257 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 789314a7-216f-3fb5-a532-1c15350b4944 | -10.36933 | -59.20766 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef6207bf-f1ec-3079-9f44-13f5f706c878 | -9.11817 | -65.77315 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1e2237d-c864-36e6-bc8f-08cb626566d0 | -9.44812 | -62.35524 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 237116aa-077e-3a20-824c-f8cd1fa18295 | -9.4615 | -62.33226 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 755b44fb-7501-340b-96a0-fcdd8ccf59ea | -8.55565 | -63.03061 | 2025-08-30 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da1adf94-7206-3112-bdf5-80550c3d475c | -8.88981 | -60.72874 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35870b59-f6e7-30de-9fa4-597afa5d9069 | -8.02943 | -69.92218 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df58b87f-f610-3c67-8468-3ffe3587d194 | -9.17772 | -65.79601 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc9ba3db-a40b-3a44-ac71-a832b1450242 | -8.0444 | -70.08885 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbcb9954-c78d-3cc1-9d59-54c534f3d0a2 | -10.36582 | -59.20689 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99c6dfaf-6741-31b4-98a0-5d42a8ed0154 | -9.44457 | -62.34233 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7daf5b71-c015-3aa8-ab3b-32d28bf68026 | -9.82215 | -63.85771 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 64462c2b-e3d3-3b31-8491-a5261b50281e | -11.68696 | -63.90768 | 2025-08-30 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a284c381-01f1-3267-b1fe-ac14936fc25b | -9.1247 | -65.81407 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d24ad12e-64a0-30d9-b4d4-039bc8773e80 | -9.23728 | -59.78226 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 137569c3-687e-3871-824d-af0a75ccc37d | -9.44485 | -60.53943 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| eeada45a-53f6-3848-ba14-4d719432701d | -9.45113 | -60.53621 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f988637e-d471-3146-9eb9-cb0869ee610e | -8.62704 | -67.24246 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5b4e7e8-d136-3cd5-9fdb-dc6811368f37 | -8.90074 | -62.10643 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c463a30b-ce00-3adc-a447-a2836a96e5ad | -8.84787 | -70.62925 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ab63bac-04a8-36b6-b894-553bcc42b91c | -10.35422 | -64.46501 | 2025-08-30 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4d14c43-35a3-3014-a9fa-68eb80cc8097 | -8.34909 | -62.9333 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3a92b94-90ab-39ff-8557-2bceb4084645 | -9.43474 | -62.33778 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c9f4e163-5741-3c17-8f0b-38b950d51cce | -9.43699 | -60.55482 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5be03902-a42d-3cdd-92fe-6ae84b6b97b9 | -8.44712 | -70.14552 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d70175f0-8966-3dd9-95ed-1aaf93ec6b4a | -9.43872 | -62.32591 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 36519b5d-7311-317f-a2a2-510a95869a7a | -9.12372 | -65.763 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30874085-3597-3f0e-a73f-98c6bc336a5e | -9.11514 | -65.7654 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aa640845-a97d-3b55-8784-db5e97e86a95 | -8.18338 | -61.37793 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f9837ca-39c5-368c-93f2-33d3e780c5ba | -11.39972 | -63.25316 | 2025-08-30 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe21858-2119-3493-9160-df9631624e3f | -9.44793 | -60.5681 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f6e2a169-a009-3153-9886-050c320b3c1a | -10.36233 | -59.21214 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9afdf7a4-eba1-3899-8436-5c3b6d6401f1 | -9.44341 | -62.32977 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b0edd74c-6a89-3817-97f7-f69065a40c09 | -9.10653 | -65.73869 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9692319-7f8f-366a-a858-72f7c7aeb752 | -9.4379 | -60.55435 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d31ef6c1-2ce6-341f-9cfc-330fd87b6a93 | -8.18382 | -61.37453 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cecedd4-487f-3bf0-b7e1-4763a1adc3ea | -9.43804 | -60.54668 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 791ce422-913a-3109-ba6e-0a99fac457f9 | -8.88638 | -60.73061 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5871efc9-f812-33c5-984d-6d4f78802cf4 | -9.22533 | -71.94839 | 2025-08-30 06:01:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d658de84-3644-392b-ad4a-fc3a8813e724 | -8.88587 | -60.73442 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fa175c0-5186-326d-8f00-c4dd45e99ff7 | -7.3558 | -70.12254 | 2025-08-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92a83da2-3de2-37bf-a17f-263a5173fb02 | -9.17516 | -59.5731 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README83.md)
