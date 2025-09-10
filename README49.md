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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 939b7439-2bff-3a7d-9ba9-fc8bc8249206 | -19.9977 | -46.83943 | 2025-09-10 04:19:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbbd8ed4-05d5-31ef-81fc-0255078d7682 | -19.64447 | -45.04857 | 2025-09-10 04:19:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 38629c7e-1a3e-3f87-a67d-23640afb23ec | -18.354 | -49.3433 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b61649d9-9e03-3a02-ba6a-448a7aaf6479 | -19.17731 | -43.06647 | 2025-09-10 04:19:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 52aeedee-a475-3ca5-9c56-301ce2b8ad23 | -27.83095 | -50.30352 | 2025-09-10 04:19:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb02a90e-cedc-3201-9931-6a14a799cf30 | -18.29357 | -49.32758 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 050d1ca1-d984-32a3-8884-44d13a5ecec4 | -20.07652 | -47.53727 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59bc5796-6005-32dd-be32-9dd85e72eb51 | -19.49107 | -45.30201 | 2025-09-10 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 249ea5d7-de1d-303c-ab63-95e9d57fbdad | -19.99219 | -44.27591 | 2025-09-10 04:19:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a2b301fa-bfc1-34cd-90d1-1353bda51bb3 | -20.0848 | -47.35876 | 2025-09-10 04:19:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 221d27b0-e1fd-359e-93ec-1196ad9c42f3 | -19.34374 | -47.45184 | 2025-09-10 04:19:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80e08658-c5b0-3f61-a7eb-ede6be0bbac7 | -20.45862 | -43.99734 | 2025-09-10 04:19:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6527f3e0-dfaa-3060-acd8-b54e8422025a | -19.22994 | -44.43803 | 2025-09-10 04:19:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebb205e2-cff0-3acc-96d6-6ddaa84718a0 | -20.07258 | -47.54036 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3daf179-b9a4-3348-9ed0-01be4202a718 | -19.75044 | -45.71949 | 2025-09-10 04:19:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d0cc2f-a9da-30ae-bfb5-836f537e88c2 | -20.15619 | -43.65859 | 2025-09-10 04:19:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6fe80317-ebd0-3791-a518-84b290de5b3a | -19.49441 | -45.30257 | 2025-09-10 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2e7486e-3eb7-341b-9662-dbf791477a47 | -18.01759 | -47.12689 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 624de930-a1e0-3837-bc2d-21fbaa3a473d | -18.34392 | -49.33715 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a67078ee-2160-387d-ae8b-9565de9dee07 | -18.33884 | -49.34507 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2f278d9-ab9a-3c4e-8c5a-1a0900c0dc61 | -18.02857 | -47.14392 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1a8f28cb-7849-319d-bbd9-d10e7ef8a85c | -18.52667 | -43.27778 | 2025-09-10 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d0f6983-267e-3415-94cf-08b990ccc6e4 | -17.95619 | -46.91866 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a348f31-1805-39ae-b46f-f3675b0e8521 | -23.50447 | -51.73022 | 2025-09-10 04:19:00 | NOAA-21 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 31cf14ae-2a93-33f8-8c58-48f954713f5d | -20.01126 | -47.62159 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1118f51-e372-3fe4-a341-00f1aa60b548 | -20.46079 | -43.95686 | 2025-09-10 04:19:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fd35b411-f385-3564-9a0a-47cebec0cd2f | -19.03743 | -47.91458 | 2025-09-10 04:19:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2cfd01c-2368-3d94-9e77-04e6d5048a74 | -19.17372 | -43.06592 | 2025-09-10 04:19:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 20567a48-7ade-39b9-aad7-ed0d699fe28d | -18.01424 | -47.12634 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbbb45bc-46a1-3166-8184-3db8b3a0b548 | -19.53593 | -46.09663 | 2025-09-10 04:19:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c43f2d23-3013-3a04-9005-2a65703857e0 | -18.52251 | -46.18385 | 2025-09-10 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa3bc453-c80a-391c-b91a-6eee8602a131 | -17.5858 | -49.82283 | 2025-09-10 04:19:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aa18c17-40a8-3cfd-b600-998cbec2ddc8 | -18.46629 | -46.47547 | 2025-09-10 04:19:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8df42753-5d6d-37f5-9378-0a2146b31aed | -18.13685 | -51.72452 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0e01e00-2b13-3c64-82f6-dd4df6fe56e2 | -18.66687 | -47.54768 | 2025-09-10 04:19:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a691076e-2869-3de8-b73c-084d2862144e | -20.02126 | -47.62353 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f75123d4-a2e4-3961-ba93-f4e855fdd942 | -17.20726 | -50.15778 | 2025-09-10 04:19:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5907128-4d4c-3c27-aa96-88b519899606 | -19.89718 | -43.85894 | 2025-09-10 04:19:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 70c0c42e-665a-3213-a3f8-13452e65affa | -20.16329 | -43.65924 | 2025-09-10 04:19:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32a79853-6c78-373c-ac19-0c52f2352f82 | -19.35042 | -47.45303 | 2025-09-10 04:19:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19461bb7-2df2-36db-bef4-e868112a363f | -20.00639 | -47.60922 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9375a20-d12c-3479-9654-5064a741e478 | -20.01276 | -47.63345 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| feb1573d-40cc-3656-9fd0-18fc508776f9 | -19.35104 | -47.44928 | 2025-09-10 04:19:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66ed16b7-d33d-3438-9419-553006e3d62e | -18.51815 | -46.38385 | 2025-09-10 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 245addda-7e2b-3393-8594-24e4c5eadca3 | -20.46774 | -43.95814 | 2025-09-10 04:19:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| c68f8eb1-b6e4-3718-89bc-60e25c605e1b | -18.93384 | -46.95739 | 2025-09-10 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dcdd67a-8bc5-3ae7-898e-3d7eb765ef19 | -19.59917 | -46.0846 | 2025-09-10 04:19:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e89e082a-55b7-364d-9bd3-ea4e2504e909 | -19.29333 | -47.98727 | 2025-09-10 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c569e879-e67d-3304-b687-19ee2c066324 | -18.00664 | -47.10976 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 170a3915-c275-301d-903c-314de0888941 | -20.06864 | -47.5435 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63438c5-d0f0-34a6-868e-63d2f6c8982a | -18.00542 | -47.11721 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3bfc600-ecb4-30da-a85a-61a20f03a26b | -18.34678 | -49.34207 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a903f16-511b-3540-ba36-6d8f87114ca0 | -20.00245 | -47.6123 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d5ae980-38c0-3c9c-964f-c822c3037899 | -20.20381 | -41.54608 | 2025-09-10 04:19:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9f14ff00-574a-3d64-8678-23cd1e56ffdf | -17.76602 | -48.61259 | 2025-09-10 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93897530-8d63-3271-8ea8-1136ccb54ac0 | -19.99911 | -47.61172 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f9570c3-8365-3a06-a9a2-c223950273a4 | -17.57384 | -51.06351 | 2025-09-10 04:19:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e449d71-05a1-3cba-8c2e-e6781ea9f3f2 | -18.00329 | -47.10922 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deaae8df-a4f9-3e25-ab45-f3d24bb2d5b7 | -19.17284 | -48.78679 | 2025-09-10 04:19:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb0e1176-2ed8-36ac-af11-868508a1231c | -20.00126 | -47.61965 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e36cf786-9994-3f32-9352-a583b3924b31 | -16.51426 | -55.1377 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a84ce909-0aa6-3289-828e-e78f63b7b597 | -18.14511 | -51.72612 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9e58d991-4940-3f18-9067-b015f8557fc9 | -28.06224 | -48.67109 | 2025-09-10 04:19:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 96e74c5d-3662-3eaa-b82d-3f81c87b4656 | -18.34752 | -49.33776 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43f0a607-9065-30dd-a587-b9eca8a9dbf4 | -18.132 | -51.72762 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47d355d7-fda5-339f-bf72-579fbafb6d2d | -18.9604 | -42.38976 | 2025-09-10 04:19:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 387917d6-a856-3d9b-825e-1b963c7d1b38 | -20.00579 | -47.61291 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f52225d2-519f-3638-ad85-5a7e374d2fd8 | -20.07319 | -47.53661 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb04fc0-1fc8-3e26-b650-140284c68b33 | -19.30633 | -43.25625 | 2025-09-10 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73193459-e7b9-3b2d-b42c-03a1a3cb0e8a | -18.03132 | -47.14813 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2a319d30-2198-31b3-97bc-4722ded6d7ff | -19.5365 | -46.09299 | 2025-09-10 04:19:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0962112b-2a6e-3483-bfba-97b2e271ce4f | -20.15265 | -43.6582 | 2025-09-10 04:19:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5dc57ca7-e6e2-3aab-9296-5ba336318efd | -20.00942 | -47.63279 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 62b6b619-5821-38c8-8e81-0f6e385856c0 | -20.06318 | -47.53481 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1df67956-54fa-3abe-b7f4-7b549cb4f22c | -29.72046 | -51.10339 | 2025-09-10 04:19:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| add71d40-3c38-36cc-b813-7a6c18cc37e1 | -18.00878 | -47.11773 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd3aa319-b463-33f0-821a-1d11398998bb | -19.9973 | -47.62278 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5b82296-89e3-3179-a1f6-8a3798b58a50 | -20.00305 | -47.60862 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d785ebc3-3cc5-3f33-9778-d9a8410f37a5 | -18.14308 | -51.72608 | 2025-09-10 04:19:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2ed02ad3-1492-379c-826c-639314987b88 | -19.48774 | -45.30144 | 2025-09-10 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e923f343-d4fc-397b-bb7c-24dc186e450f | -18.00816 | -47.12149 | 2025-09-10 04:19:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a3fbb46-dc8f-3cf2-b6bd-13632726bccc | -18.53664 | -43.28359 | 2025-09-10 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5c6c7337-3c1a-3755-babc-22c86afff56f | -16.12315 | -55.86598 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fbe6fdd7-4271-3e65-9318-5910daa8be88 | -20.0046 | -47.62024 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eead8c7e-40f7-312f-be1c-c095388d37d3 | -19.68721 | -46.17425 | 2025-09-10 04:19:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7105d139-b9d3-3ba2-8e16-7bf6794a69ca | -19.99971 | -47.60802 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6533cb31-7698-3c99-912a-6442a4851181 | -19.64224 | -45.04047 | 2025-09-10 04:19:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2658d2ee-c065-31a7-a9cb-35245fe16510 | -16.12695 | -55.86596 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0b996c10-9c25-354f-a8be-f0782b43dac9 | -19.99791 | -47.61908 | 2025-09-10 04:19:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4909dd4d-3150-3b9e-89c8-b12d79a3900b | -20.77294 | -42.8851 | 2025-09-10 04:19:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59b0bdb0-0192-3cbf-8862-31e9ce69e194 | -20.28393 | -46.25066 | 2025-09-10 04:19:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8fdba913-7636-3929-905d-c547a5ea4314 | -16.54678 | -55.14053 | 2025-09-10 04:19:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6c44fdd4-b861-3ae7-a1ff-a6b97c7a4ded | -19.64168 | -45.04424 | 2025-09-10 04:19:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 097e6e69-044a-3fa4-9865-261cb0c91881 | -18.43891 | -45.93535 | 2025-09-10 04:19:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc3f1216-4fff-3f6d-b463-566a341bff2f | -19.67022 | -44.89835 | 2025-09-10 04:19:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84beadb0-139c-3119-92f4-b54c43c777d7 | -19.75432 | -45.71638 | 2025-09-10 04:19:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60f3846f-a87e-327c-b8ed-654be1cfe037 | -20.02137 | -47.77051 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1169d854-9c0c-3b33-a360-872b6ff69e67 | -19.51787 | -45.00807 | 2025-09-10 04:19:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1094f459-53c4-3017-8537-fabfe27dd807 | -20.06257 | -47.53856 | 2025-09-10 04:19:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03db5f0d-7db5-33fc-be97-24c48f578ca4 | -18.3576 | -49.34395 | 2025-09-10 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
