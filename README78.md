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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de5cc906-55d1-3bab-946f-b857f78e9fe0 | -19.46147 | -43.58691 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8481cce6-8a8a-32b1-934e-aacd30ce988b | -19.68561 | -43.09516 | 2025-10-29 04:49:00 | NOAA-20 | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6524675b-e01f-3e6f-b3c3-6191dc13d920 | -19.6855 | -43.09411 | 2025-10-29 04:49:00 | NOAA-20 | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 78391a96-6105-327e-8454-580261b91272 | -19.42416 | -48.06314 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8754414-00b4-3fd5-b3d5-45085bc7f2c4 | -17.53712 | -44.61821 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88198dbf-2ebe-3f97-8bcb-5a7e323b73d0 | -18.33008 | -45.88563 | 2025-10-29 04:49:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80bbe724-8268-3f3e-a176-1cc72bd1991f | -19.45195 | -49.32843 | 2025-10-29 04:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6c3d76c-7d8d-3b22-9a32-02ca0313fed0 | -19.38524 | -43.62973 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfddd255-c274-3968-b931-5d1c5338f4c9 | -19.67791 | -44.19944 | 2025-10-29 04:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a47ee51c-4372-3f84-b3ec-72fc26a447ec | -19.24134 | -43.99874 | 2025-10-29 04:49:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 132a634f-46cc-3747-b7c6-06c2cc0b4709 | -19.33688 | -43.05881 | 2025-10-29 04:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fc71d227-e028-3842-a975-bfa657ab01cb | -18.92118 | -45.04581 | 2025-10-29 04:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9200475-c10c-35f0-8087-968948c972a9 | -20.80054 | -42.75912 | 2025-10-29 04:49:00 | NOAA-20 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 39bc5225-acdb-30e1-b980-2b621cf4d09b | -17.20306 | -44.45254 | 2025-10-29 04:49:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c3b09cb-0074-337c-9a6d-e50c7e5a0940 | -19.45436 | -43.60127 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 69b9ff26-058c-3fa4-bdcc-a1b596f66492 | -17.53681 | -44.62103 | 2025-10-29 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38030294-4f72-39c6-ab7c-a1bead4636fa | -20.99965 | -42.79652 | 2025-10-29 04:49:00 | NOAA-20 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5c18ec3c-06f6-31be-8e1e-b03da9c1e6c0 | -19.43206 | -48.06824 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a683f51-b4c2-321e-ba96-55c56fe3808b | -19.42316 | -48.07105 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14a0a96a-3dc0-35ce-a27f-6ee686454fdc | -17.48531 | -44.07101 | 2025-10-29 04:49:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64815211-3dec-3887-8d2a-498408dbedf7 | -17.04106 | -47.0568 | 2025-10-29 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5f5ea32-e35f-3cc8-8491-7ce0d100b8c8 | -17.26358 | -45.28522 | 2025-10-29 04:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb403703-49bc-3abb-9621-f8d5eafd4d9c | -17.20379 | -47.0051 | 2025-10-29 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f985ce1-f14a-35d0-b670-1e25d7eb38ce | -18.20073 | -44.33688 | 2025-10-29 04:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3379f573-d3d6-3562-95fc-3775fe49f899 | -19.86856 | -48.32927 | 2025-10-29 04:49:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 445d394e-b0d8-3d1f-abe2-75d963339468 | -19.45514 | -43.5934 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27d4a572-b00a-3f5f-993f-0258dbfc774e | -17.04158 | -47.05259 | 2025-10-29 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b2af42f-c297-3f0e-a277-820c6e66aab8 | -18.50655 | -45.07913 | 2025-10-29 04:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f176df6-cd0c-3592-ae47-c362c588e64e | -19.24172 | -43.99511 | 2025-10-29 04:49:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e284437-61ff-31ef-9115-a9f256ba814e | -19.45546 | -43.59015 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 214a401c-bff2-3d69-8698-944a8026286c | -19.45478 | -43.59702 | 2025-10-29 04:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d77364be-94d6-3b9b-b27a-7e03dbc1055c | -19.6783 | -44.19577 | 2025-10-29 04:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4975aea4-28ff-3ce8-ab90-c710d043d209 | -19.41946 | -48.0665 | 2025-10-29 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c84a14f-e325-3666-a64b-0b165ac4d106 | -4.2157 | -50.0812 | 2025-10-29 04:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 5c40d719-93c7-34ee-ac85-60e0981a5f72 | -12.7021 | -46.303 | 2025-10-29 04:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| e177d551-9dde-38c7-8e0d-2c1aa864c0bd | -6.0999 | -42.4628 | 2025-10-29 04:50:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 379108de-017b-33a9-826e-5302bf7849b6 | -3.777 | -45.5833 | 2025-10-29 04:50:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1142071e-16d6-3f0e-bdd6-9d99c3e51d8f | -10.8671 | -50.0916 | 2025-10-29 04:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c0b63ec9-d2cb-33ae-9163-6e042ac1944b | -4.2159 | -50.0601 | 2025-10-29 04:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 060b2243-cfd1-3de8-b7e5-ee22010777d4 | -3.7769 | -45.6058 | 2025-10-29 04:50:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 8b1957e8-0eeb-3f91-a238-b4f3e76bbb77 | -4.2156 | -50.1022 | 2025-10-29 04:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 06be8830-14ed-35f2-8f55-37fcf38ca86d | -10.8481 | -50.0937 | 2025-10-29 04:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7985e77e-8334-385f-b811-ec8e3f11acb1 | -7.8037 | -46.4458 | 2025-10-29 04:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f38484b1-a248-3d8d-93a2-801a473385ab | -4.1972 | -50.0819 | 2025-10-29 04:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 9bfa4b70-2413-3059-812e-9f027c27ef2f | -4.2157 | -50.0812 | 2025-10-29 05:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 181.0 |
| d7c55d4f-d218-3d11-9873-97ecdba54090 | -4.2156 | -50.1022 | 2025-10-29 05:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c5f10c11-dba4-3617-9f90-010995492fcc | -3.777 | -45.5833 | 2025-10-29 05:00:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 78f26150-7ccd-3ae2-a16d-529f61ab97bc | -12.1958 | -46.717 | 2025-10-29 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f93fda3d-8a5d-31e8-8d54-8ed6de0f4256 | -7.8037 | -46.4458 | 2025-10-29 05:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 412446af-cec0-37b9-8b16-344337a7a9d1 | -4.1972 | -50.0819 | 2025-10-29 05:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 73105242-62c4-3b07-91af-4356438443f9 | -3.7956 | -45.5825 | 2025-10-29 05:00:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 19295e1e-0747-351b-9c9d-fec787d8c162 | -10.8671 | -50.0916 | 2025-10-29 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 26922171-ad95-36ab-939b-b31d3f853e08 | -4.2159 | -50.0601 | 2025-10-29 05:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| f3a74383-06ae-3ec4-b8c7-2da4b991f54e | -4.2156 | -50.1022 | 2025-10-29 05:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 6b9520af-4226-3e1f-a1f5-90d197c089a8 | -3.7956 | -45.5825 | 2025-10-29 05:10:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 032f712b-e3ef-386c-8f73-e3ce78dc5e31 | -4.2157 | -50.0812 | 2025-10-29 05:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 796b413b-e045-3102-9994-52f814787198 | -7.8037 | -46.4458 | 2025-10-29 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| aa4f008b-bd2a-33fe-9d8f-55201c5c2ba9 | -7.8035 | -46.4681 | 2025-10-29 05:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| a8271bd9-b805-3ea7-9334-f885b18a4afd | -12.1958 | -46.717 | 2025-10-29 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 391e2315-b408-388b-a471-275690b3ad45 | -4.1972 | -50.0819 | 2025-10-29 05:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 923a2a8f-3fd2-362f-84c2-bbd00ce5f9d5 | -12.0036 | -46.7667 | 2025-10-29 05:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e9d0f102-8e4d-3366-a787-10812efef982 | -10.8671 | -50.0916 | 2025-10-29 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| b3d772d6-7f6b-39ec-a3db-963a50e92edf | -4.47795 | -43.42336 | 2025-10-29 05:14:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4430bf34-049e-362a-834c-92c226d91e53 | -6.29616 | -41.87299 | 2025-10-29 05:14:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| a219f556-c25d-324e-a7f9-f2f86305f5ac | -4.47305 | -43.45326 | 2025-10-29 05:14:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 467e4f72-a913-3227-a8f4-d28628d4a294 | -6.13183 | -41.83345 | 2025-10-29 05:14:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 234b3a13-3006-3587-9de7-3c8a7fba7461 | -6.09138 | -42.46509 | 2025-10-29 05:14:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 57cf5181-e2e6-3d7a-a91a-dd3fda11c790 | -7.34058 | -42.4573 | 2025-10-29 05:14:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| bb2000cb-e672-3c61-9064-c2e130db0b96 | -6.10513 | -42.4672 | 2025-10-29 05:14:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 2d317948-070e-3c15-96d9-8634c9eaa64e | -12.00194 | -46.75483 | 2025-10-29 05:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1363e88f-73d2-3ba7-bf32-734993374904 | -10.4265 | -44.96853 | 2025-10-29 05:16:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 7c97841d-270a-380c-a662-f208df0637ec | -13.63792 | -46.50126 | 2025-10-29 05:16:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| c5859c95-c53b-3d78-985d-19d4657537c2 | -10.42096 | -44.99883 | 2025-10-29 05:16:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 0d90d4c0-6d7b-3f7e-a30c-6e70aa9ad3b6 | -15.09244 | -43.8369 | 2025-10-29 05:16:00 | AQUA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 31.3 |
| bba6587d-771f-30f0-a86d-50a350c51e1d | -12.0064 | -46.76044 | 2025-10-29 05:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 733f218d-9a4a-3917-bdc5-62518a703918 | -10.42666 | -44.99216 | 2025-10-29 05:16:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 23164a93-a8de-306a-b7e2-c360a26f9f4d | -13.81591 | -41.69479 | 2025-10-29 05:16:00 | AQUA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0ecece40-dfa7-3a21-a04d-0b68d86471f4 | -19.78445 | -44.50753 | 2025-10-29 05:18:00 | AQUA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9ab50d9d-f1ed-355f-8de3-a7cca6d5f89c | -19.79671 | -44.50975 | 2025-10-29 05:18:00 | AQUA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b447ccb8-d908-31ab-acca-a4786b55c6dc | -18.92091 | -45.02514 | 2025-10-29 05:18:00 | AQUA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 110c63df-5fed-397a-bb99-95aca3bef587 | -7.8035 | -46.4681 | 2025-10-29 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 2b59de43-e150-3df2-9a79-dcf6def74a0e | -4.2157 | -50.0812 | 2025-10-29 05:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6d49aaff-cc3e-369e-bcd8-d63033075e6b | -4.1972 | -50.0819 | 2025-10-29 05:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 5efbd067-a604-3c54-8c63-db85438c32bb | -7.8037 | -46.4458 | 2025-10-29 05:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d0f2a424-7788-3503-b556-e50098e844e8 | -4.2157 | -50.0812 | 2025-10-29 05:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 583fa499-9b91-34e9-8632-4f44ca63b813 | -6.0997 | -42.4865 | 2025-10-29 05:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 50e25391-d333-32f3-9bec-b6e13648d892 | -6.0999 | -42.4628 | 2025-10-29 05:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 211fabc4-d2ec-3765-9b3b-43a44e132b17 | 3.95063 | -59.63317 | 2025-10-29 05:31:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f0637ae-d7d6-3e7d-b8ab-a97517e1ea16 | 2.45772 | -60.91415 | 2025-10-29 05:31:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f9d92141-78d3-31e1-a0ed-cffd7a04318b | 3.29628 | -60.6828 | 2025-10-29 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca467b91-2be6-3ffb-9d56-384472e7ac39 | 1.60153 | -55.70481 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae297476-6f50-38eb-9fd9-c8874c2c6905 | 1.60087 | -55.70072 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d6fe7fd-8d36-3f95-947a-07ed7b949434 | 1.60518 | -55.70001 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1abbcfff-9987-3307-93ce-03bd6fb72068 | 1.59058 | -55.7192 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf55871-790f-37a3-87c8-82b33b7a56c9 | 2.68221 | -60.4152 | 2025-10-29 05:31:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd1ae345-5722-3936-a767-3e32efcfd48c | 1.58628 | -55.71995 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19899e69-debe-31f1-a542-06874f51b1e1 | 2.67893 | -60.19867 | 2025-10-29 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c3ac9ab-5d1d-3f4a-8ec8-909feeb8ca6d | 1.57898 | -55.72946 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509ebd70-03d4-35c4-851e-07dbb38c3cb0 | 1.63642 | -55.67375 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74a7e4c2-6faa-3d2b-a366-d3e4734eadc7 | 1.64009 | -55.66889 | 2025-10-29 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
