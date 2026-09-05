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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abd99097-01f0-3e2d-b0e5-8184fc3eeb43 | -14.91313 | -44.67654 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 91613843-b2ec-3df1-9609-706e4f09631c | -16.81953 | -49.17945 | 2026-09-05 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e63b77f7-4579-3ec6-a18d-4db7b98e944d | -14.73982 | -47.14712 | 2026-09-05 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57c2a7c5-db8b-303d-a59f-535fb2f41ca0 | -18.04233 | -47.28098 | 2026-09-05 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 145c1a37-c5e2-360f-b999-3e79d7928853 | -15.0113 | -48.62886 | 2026-09-05 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c44bae66-0b34-3094-aed2-b466cf29fbbf | -15.07396 | -52.52729 | 2026-09-05 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a940e19-d81e-34eb-abad-519eb4314510 | -15.06938 | -52.52638 | 2026-09-05 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bad13bc0-fd05-3be7-af75-93895cb3ccea | -12.44326 | -43.27354 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6da45e27-7efe-39cd-9dfd-b9dcd5c277b8 | -12.43933 | -43.27666 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e652c3af-3d94-3ceb-a944-b115da9878cd | -12.44214 | -43.28086 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5123d06a-576d-3f0b-8149-4b4235cc6db1 | -18.50664 | -46.34873 | 2026-09-05 04:21:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b872e53-bfe6-3b95-bd25-ce1b9b2adeda | -13.302 | -48.30978 | 2026-09-05 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85a8c400-e658-3b39-a8ce-e5011ab64e59 | -12.43776 | -43.41094 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dc7a0b0-9743-3221-aa5d-890dcec941a8 | -15.80768 | -56.76313 | 2026-09-05 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de522914-f9eb-3d45-a17f-ca0416e87727 | -14.90593 | -44.67902 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2370c092-5072-3fc7-9dd7-bd1cb7836b12 | -16.85159 | -49.03645 | 2026-09-05 04:21:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdb7bd83-2dcf-3229-8cdb-ff406f429336 | -16.22917 | -57.43559 | 2026-09-05 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 937b9c28-c14c-3c93-8bb4-cafc1ed64c12 | -14.90648 | -44.67545 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b096acd7-ecad-35ee-972b-b13117b10320 | -15.80668 | -56.76776 | 2026-09-05 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 075fb843-d2b2-3f6b-bc00-8f9fec0c0d81 | -15.32518 | -43.6549 | 2026-09-05 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6211834c-c554-3372-9acc-05ec9a6bdf6c | -12.4427 | -43.2772 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 750aab0b-f7cb-3dd3-99b7-0c1e5c86a859 | -14.9098 | -44.67599 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f7472884-0f8a-3604-832e-33c43f54d7e6 | -17.20552 | -53.82444 | 2026-09-05 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c09d8b6-145e-3c89-8fc7-7c37ce1d555b | -18.50606 | -46.35235 | 2026-09-05 04:21:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55df519e-fe78-31bc-acdf-97c16441b05f | -17.21077 | -53.84825 | 2026-09-05 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f5d91a5-e72a-3494-8432-35e9dc2ebf17 | -17.22773 | -53.86352 | 2026-09-05 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e71a0d07-472a-3fa7-81bb-323e21708d10 | -12.44057 | -43.4151 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 841bb844-ee1a-3e45-a536-f825ceff5ce3 | -14.85042 | -47.95894 | 2026-09-05 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc263fca-5db2-3e0c-a282-e47bea077b41 | -16.85267 | -49.03485 | 2026-09-05 04:21:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b4f1265-25f2-3848-95fd-f78b0182f0fa | -18.58347 | -46.42192 | 2026-09-05 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 277e3252-1905-3cec-b19c-fb6f36c1f48b | -12.4399 | -43.273 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0fa3fe4-80f6-382f-8ba2-4f87d478b270 | -12.43831 | -43.40731 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19caea06-cd8a-3f70-9cd0-50a5f19190ea | -17.45139 | -52.40501 | 2026-09-05 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c696641-f55b-3d1d-b81f-1e76fb5070c3 | -12.43596 | -43.27613 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 41243aef-d653-3acd-a5a2-cdb5e4ac75db | -12.43877 | -43.28033 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d063a82c-f4f9-33d6-8524-f8712af716be | -13.41569 | -41.8862 | 2026-09-05 04:21:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a319a6b6-d921-3561-97bf-ae38574d9efd | -17.2325 | -53.86466 | 2026-09-05 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7062292a-037e-380c-8051-d86c87814d17 | -11.86495 | -42.54632 | 2026-09-05 04:21:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4a39922-f77e-3057-9a12-f4d1bf318db9 | -15.64157 | -44.13167 | 2026-09-05 04:21:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e01f395-f647-341d-958f-b8d170f11ec2 | -14.9026 | -44.67848 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 413bbdf3-3dc6-302f-a7f0-c158fe1f037a | -12.43645 | -43.407 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2ecce5e0-dd3e-38f9-ad2f-bf038a58a466 | -16.77292 | -50.61545 | 2026-09-05 04:21:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 37418e64-e8ad-3ecc-a2b4-624c39cdf4db | -15.64307 | -46.82248 | 2026-09-05 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd3bc783-3120-3c9b-8cbb-921a8def887b | -12.92665 | -42.43468 | 2026-09-05 04:21:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ef933cdf-3791-33e1-b7ca-3948d7efcd16 | -14.91036 | -44.67241 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 07debe88-717f-3954-ad18-9fe3bb45a8f6 | -12.92317 | -42.43413 | 2026-09-05 04:21:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fe903a58-8c08-32da-8b56-378704f7217e | -14.74387 | -47.14391 | 2026-09-05 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac371141-3926-3d93-abdf-c7f82c4ab971 | -14.49684 | -47.1092 | 2026-09-05 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5c30360-7e1b-3395-b5bd-d370279e7fa9 | -17.76216 | -42.42658 | 2026-09-05 04:21:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0eb36ef4-a851-398c-981b-0c788398dcea | -14.98849 | -41.35767 | 2026-09-05 04:21:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8188df70-49cd-3b3c-ba42-bb6cd070fdb4 | -17.20966 | -53.85384 | 2026-09-05 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fbb925f-1bb2-3572-ada5-31d88f23856d | -18.58678 | -46.4225 | 2026-09-05 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a241d3a-09e5-351c-b4ce-91abb70b5473 | -12.43253 | -43.4101 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3a465e7e-ea0a-33cd-bc0a-0ac7aebd6c3a | -21.39219 | -45.50625 | 2026-09-05 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4dcf96c-de18-3efd-b99e-df2d3b269aed | -19.75183 | -46.67672 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c591ccfc-9223-3cfa-bd6f-5892930f2879 | -17.10687 | -56.83302 | 2026-09-05 04:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| e27c872c-19cd-37a6-873a-edd15338fdfc | -20.14323 | -46.32751 | 2026-09-05 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 02afb282-cb5d-3562-a207-104ee98b4ec5 | -21.51203 | -49.95874 | 2026-09-05 04:23:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 49ffd945-3c33-32e3-99e8-ae6c4a48de41 | -21.5183 | -50.02719 | 2026-09-05 04:23:00 | NOAA-20 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 15eede0f-d581-36bd-b311-8a9d67115e55 | -19.32519 | -46.37011 | 2026-09-05 04:23:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b473afd9-cdc2-339a-934e-64302f10ce5e | -19.74948 | -46.69138 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 328c19d9-a847-3dbb-ba2e-5943bcf76017 | -21.41587 | -45.46351 | 2026-09-05 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 555aea3f-09b5-3b3d-94ce-bf6fc97b2533 | -21.1084 | -46.27814 | 2026-09-05 04:23:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4c99f319-e01d-3e78-9657-015cf9ef0569 | -17.11263 | -56.83442 | 2026-09-05 04:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| e8dc885e-c171-3caf-9fd3-a6ae5aa04111 | -20.4827 | -47.53506 | 2026-09-05 04:23:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 645e7362-3921-3c01-bae7-d064bc3ab75f | -20.82457 | -46.31216 | 2026-09-05 04:23:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf417e9a-304c-35aa-805a-438f6f3107dc | -20.47937 | -47.53443 | 2026-09-05 04:23:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33ea90f1-103e-34ed-afd6-6f2465a86062 | -21.55271 | -44.05761 | 2026-09-05 04:23:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d93944dc-8c95-34d4-9b24-c3a5c8f40f57 | -21.04308 | -43.86118 | 2026-09-05 04:23:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0498cc95-6d64-30b3-8729-3b8a4cd584a4 | -19.75514 | -46.6773 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5a9a97f-7443-3a3c-984a-a562e5e49ee5 | -20.17454 | -47.38795 | 2026-09-05 04:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ca8a1b-b186-3022-a382-8d752795a56b | -20.29524 | -46.31207 | 2026-09-05 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 818e35ec-2a01-34fa-a57a-aa93c0644c76 | -19.15987 | -57.35694 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b0ec3731-e1f0-349c-9516-466a9a92fc07 | -20.35676 | -47.07779 | 2026-09-05 04:23:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3977e11e-d5d0-39bc-a995-6db7b9eec164 | -21.57979 | -48.6582 | 2026-09-05 04:23:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5794d0e3-111f-3f61-8d85-f6448de133d4 | -20.08845 | -47.45286 | 2026-09-05 04:23:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34dc75c0-4d12-38cc-b179-494f6adf5052 | -19.09654 | -48.49201 | 2026-09-05 04:23:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a7e826b-52b6-36d4-a6c3-33fa8418c70d | -21.45705 | -45.77307 | 2026-09-05 04:23:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1c9bd35-bf51-3bd9-b9f0-0a53ed753c2e | -19.23718 | -46.72963 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83662cd7-1b0c-36de-b807-3de3be996792 | -19.76058 | -46.62188 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72a7e20f-bf08-36e9-a387-4bf725adba1b | -19.76117 | -46.61823 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff1dac4e-4eee-3c81-b0e4-3d91ec0ca0bc | -19.01744 | -47.061 | 2026-09-05 04:23:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8332be0-11af-3345-845c-ec072ef08ad1 | -21.39162 | -45.51003 | 2026-09-05 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7c7195b-e61f-3ec2-bb8f-e2f94291a1aa | -19.81305 | -49.41669 | 2026-09-05 04:23:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ad59934-8812-3627-828a-26f546994f88 | -20.60463 | -46.37317 | 2026-09-05 04:23:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45729f74-faa3-3c92-b15c-0381661c2d57 | -21.29489 | -51.67027 | 2026-09-05 04:23:00 | NOAA-20 | SÃO JOÃO DO PAU D'ALHO | SÃO PAULO | Brasil | 3549300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6aecc156-77e3-3511-a1a5-570f9b566cba | -20.78825 | -57.76033 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| af1265cc-02a1-32c0-8d41-9e9a11480480 | -21.04579 | -46.97644 | 2026-09-05 04:23:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8aeaa3cd-12d6-3f2e-b582-41ba6ee98035 | -20.60131 | -46.3726 | 2026-09-05 04:23:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b50c702-b56b-38ca-8e18-510a6572072f | -20.82788 | -46.31275 | 2026-09-05 04:23:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af65f401-d118-3f9f-9501-4ce614905274 | -21.53648 | -43.19341 | 2026-09-05 04:23:00 | NOAA-20 | GOIANÁ | MINAS GERAIS | Brasil | 3127388 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8c4a45c-5ff7-3538-b983-e488f4eceab6 | -19.7489 | -46.69503 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0308585a-3750-3551-aa05-fb19edeaaa10 | -19.23328 | -46.73269 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc1e32e6-2328-3ca7-8394-344a1cfe7154 | -19.06651 | -48.35571 | 2026-09-05 04:23:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f7aa679-9e9b-3f35-984a-1133ad78f96a | -17.10594 | -56.8373 | 2026-09-05 04:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 95488362-0727-3fec-9229-b5d43576827d | -18.89727 | -47.04739 | 2026-09-05 04:23:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e449780-d3bd-36cc-94af-c141046f55f8 | -19.16365 | -57.33998 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6da37d95-eb81-3e69-b99d-52e3834a71f4 | -18.9006 | -47.04798 | 2026-09-05 04:23:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08a58701-0ab9-33ff-8006-6560bd022b7a | -19.8897 | -44.74932 | 2026-09-05 04:23:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d93c32c7-3d7d-33ef-8589-f997cba49ed7 | -21.58045 | -48.65427 | 2026-09-05 04:23:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
