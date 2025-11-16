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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e72b50be-ae0e-3bef-987c-730b47db0b90 | -10.92665 | -43.98375 | 2025-11-16 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da14b167-7600-375a-950a-d22417ce21e6 | -7.81099 | -41.67579 | 2025-11-16 04:08:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47e754c8-7590-3b4c-8540-9858c70db868 | -9.06076 | -44.75905 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16e49da8-9241-3431-a617-24397e208f4b | -9.83089 | -47.08352 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d140b13c-78d7-3790-9c3d-5e03ecc5e3a7 | -9.81201 | -48.17284 | 2025-11-16 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6061accc-42fa-3b44-b6d8-98e512765158 | -9.84238 | -44.18053 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8808013f-8b70-3fff-bea4-7b633306def2 | -7.04411 | -42.24943 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3fc2862-81af-3b30-bf58-355c7926342e | -9.73375 | -43.96145 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1575a64c-5e53-39e2-9ae2-b31c831843b8 | -7.35128 | -43.33821 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ca19f1a-405d-3889-9198-c063d9f7e725 | -10.54851 | -47.938 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6907787b-44c3-3b33-aa8f-8ed89b31569d | -8.06193 | -43.10867 | 2025-11-16 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ff2bab11-c5ac-38f5-af48-a3ee4d695ec5 | -9.73553 | -43.95039 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0cc65f4a-c51f-31f1-afb2-ce263f9f2b5d | -6.30046 | -43.79812 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27f1b7e8-ce93-31ed-85ef-f9018c87d7df | -8.25994 | -41.08587 | 2025-11-16 04:08:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4cf345ad-1973-3731-a411-37b03d96d113 | -6.44441 | -43.93141 | 2025-11-16 04:08:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a31eb95-efce-3969-9d6d-e884d4042115 | -9.72274 | -48.90252 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90b9163d-b440-33f8-b69c-b22d31281323 | -10.80147 | -47.99289 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b386e6dd-25e7-381f-b477-0eb73f2d2576 | -7.05521 | -43.94769 | 2025-11-16 04:08:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b04bd6e8-826c-32d9-823f-4411b8dcff7a | -8.33972 | -41.24945 | 2025-11-16 04:08:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d6311061-bfc8-3f42-b6ba-3266d3fd59be | -10.18153 | -44.38166 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 460c9267-5d02-3fda-b018-0252cde31d29 | -6.28082 | -41.72656 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf86a822-ef3c-32fa-b4b6-a5014e458ead | -6.37515 | -42.28892 | 2025-11-16 04:08:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2ee96ce-3dff-3333-9d2a-b640049b7e35 | -10.32688 | -44.28573 | 2025-11-16 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64075115-a5b3-332c-9d83-11b62eab2bcb | -6.08842 | -41.61073 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 331f1c8d-41fe-3c66-9ade-145409017589 | -11.10185 | -44.80497 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cdf8c7c-a5dc-3aac-bd30-f6ef23533c0f | -7.36061 | -46.58637 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a54c2a7-cda1-3397-a9cb-7da301300278 | -6.87867 | -44.47115 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1aff2f1-58b9-3e93-8a51-850171f8f30a | -6.30657 | -41.80088 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8b263126-d2af-3f26-ad05-1b46c68e7471 | -5.58645 | -44.89579 | 2025-11-16 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f09d92bc-730c-3cab-8824-e9de3a8454fe | -9.83965 | -47.61619 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0bd4bb7-468b-322c-9118-ccec63cb15f5 | -10.40471 | -47.70821 | 2025-11-16 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 313b0a88-111e-3f06-8850-2ffa7bd3d2b8 | -10.62214 | -44.58563 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cd64338-8e2d-39ec-9371-3c8083eaf415 | -7.52812 | -42.62418 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b3751e2a-029f-3bcb-8215-83822799dab6 | -7.51531 | -41.24446 | 2025-11-16 04:08:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4904ea2d-e947-3119-81b8-add8bf8ea2a1 | -11.97366 | -44.96359 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96141c7d-760c-375b-95cd-2e4f4c667bb3 | -11.67627 | -43.90687 | 2025-11-16 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 865dcbf1-f4f8-3416-8a49-4c9f86f01be7 | -9.02048 | -45.46423 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36495828-7462-3131-8b03-18ec369a0d0d | -13.0037 | -43.21523 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7c30db08-370d-3c6f-a8fd-6da3ce96fd7c | -7.40399 | -40.06457 | 2025-11-16 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac963374-e72f-346b-bf3a-3cda1fd69c00 | -9.7453 | -43.98215 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2c12b66-e01d-3c4c-b171-235076422afb | -7.06838 | -48.36461 | 2025-11-16 04:08:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02d7b6af-72b4-3097-96fe-14048fad7538 | -12.42446 | -48.16176 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a4c6cfa-97dc-3cb8-8d09-a6d82dc25615 | -6.90248 | -38.88248 | 2025-11-16 04:08:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 69d7dfd2-86af-3f16-9b08-669e76b5cacc | -8.20448 | -43.57164 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0e4b2fd-ff06-3139-84ee-e1091b54fce2 | -12.64968 | -46.7486 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b6ae8c-d180-3b1f-8954-0fedc449fa06 | -10.18495 | -44.38227 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ec99796-84d4-358b-b09c-a5ba890adb1f | -6.56034 | -39.76728 | 2025-11-16 04:08:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55ede0d3-73c0-36eb-b722-fe2492592aa0 | -7.72562 | -42.34443 | 2025-11-16 04:08:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7cba3208-978d-3c60-be68-a5418d076fca | -7.84263 | -47.17681 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef6a19bb-140f-3f11-b17c-f2094688f1b7 | -5.73285 | -42.73283 | 2025-11-16 04:08:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a279aa0e-50bd-31cf-86b8-004e005a3040 | -10.38875 | -49.05188 | 2025-11-16 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36a2d8a3-b02f-3790-bc14-79ef544fdb0f | -11.99546 | -49.27572 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d91fb2-5325-3faa-9921-6e70ba4386d1 | -10.12131 | -43.91217 | 2025-11-16 04:08:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39f7048c-9b3a-3273-a387-8303224dc3df | -7.05405 | -42.25099 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5c3221ec-3c0f-3db8-8055-b564cb21f0c4 | -9.73434 | -43.95777 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0443a426-7bcd-38f8-afae-00b7774ebb0f | -7.97053 | -38.63891 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28dba75c-c57f-3484-be18-2cf427d2ca65 | -6.71545 | -41.74955 | 2025-11-16 04:08:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a75ba1aa-790b-3de2-b100-55ffcd86e01e | -6.87563 | -41.59775 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70978dd8-7214-3d29-8e64-83d8d92abc5c | -11.96877 | -44.95504 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5603bd28-b9ff-3246-98e9-bfa35207f603 | -12.20113 | -49.61285 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a9874ab1-2894-399e-96f1-50fccd0cd1fa | -9.72578 | -43.96766 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b910999f-99b4-3f12-a712-f35d8e96b9ad | -8.09786 | -46.03656 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f20b0c57-d606-3e32-87e7-ebea1b2dc9c6 | -8.09865 | -46.03192 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 242d50e3-0ea1-3da1-b56c-2ed7e3fae17a | -10.00546 | -44.77 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5727040c-cf49-3f22-83aa-22c645de6ae4 | -6.00063 | -41.90858 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab7610c2-5540-3b0a-a1a3-03ae983c2d50 | -7.15013 | -41.75138 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12c84665-df01-30b9-9bd5-47c5052c9d2e | -5.75932 | -42.50391 | 2025-11-16 04:08:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 408144e2-1671-3be4-8eae-e605c01775ca | -12.40886 | -47.54766 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06b965e5-7ffe-395d-9b6c-bc56666711bc | -6.14308 | -42.23079 | 2025-11-16 04:08:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3fe509ce-82d2-3a98-b27a-c94dffc10c83 | -11.01087 | -45.24769 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a3c3e3d-a8fc-3fea-a19d-7ea57eb0c040 | -6.81958 | -39.81367 | 2025-11-16 04:08:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd44837f-8bd6-3464-a7fa-e5896112e11c | -6.93069 | -39.61406 | 2025-11-16 04:08:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b8db2959-cfe3-3e46-ad6c-6504f60909cf | -10.6953 | -44.5227 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 591b52ff-b565-3636-aba0-f7d6d8cab429 | -10.50137 | -44.91013 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08a7bef0-db2c-3780-8ac0-a0799935d594 | -6.13854 | -48.04632 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06418e59-d0a3-35ff-a3a8-f4eac69a8eba | -6.35816 | -46.1539 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c400b75-156c-3653-8c69-eec433a58be0 | -8.20169 | -43.56744 | 2025-11-16 04:08:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9ad4e2d-48c6-3c60-9529-74b1c8f4eb1d | -4.30807 | -50.87933 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fed6a748-8a03-3835-8a7c-60c3ec5ded0e | -6.4161 | -42.33124 | 2025-11-16 04:08:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60f7b615-6d3b-35ee-8d56-5ef5d7f2fdc3 | -8.26298 | -40.97805 | 2025-11-16 04:08:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 144ca2b2-51f4-3335-b8e2-e3d0aa933bde | -9.847 | -44.17368 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50e11100-b718-3999-b489-8e06b57fb6bd | -6.94379 | -41.5306 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dd4d4de-b535-3ff3-8ce1-b23f64444ab6 | -6.13552 | -48.04801 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f139eb3-0505-3c48-b169-1c00c3ca52c0 | -9.02883 | -46.87845 | 2025-11-16 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcbf6e0b-759d-35d0-9463-6c24c1288244 | -10.00354 | -44.78164 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0a87a6-9fca-3932-80b0-1946af124ad3 | -11.97219 | -44.95578 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 63ca2d5d-35c2-3939-88da-886e023ce3a4 | -11.71217 | -48.85806 | 2025-11-16 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e982116e-196b-3573-ad33-d23377fb7a25 | -7.61768 | -42.57413 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d8a389b4-f0c5-3bfe-9e1c-57e02c913b4c | -7.36379 | -43.32529 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58781dd5-aacd-3c87-bcaa-5e018779bc8e | -6.4118 | -43.76043 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bea1aa48-99f2-373f-be96-53baf82d831f | -12.05591 | -48.21292 | 2025-11-16 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 703ac1e1-5d50-3ab8-a354-a75a89116287 | -10.86266 | -44.50784 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6f24472-7750-3f40-998f-5173d70edb00 | -6.72295 | -42.94218 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| eebb2b02-6c10-3a5b-a226-93250b3809a8 | -9.74391 | -43.96314 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| edd1c628-d779-3477-ac06-8986612d147b | -12.39828 | -48.0962 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1163585-b625-3654-9362-cf7bd3a3d77e | -13.38738 | -40.65572 | 2025-11-16 04:08:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47398880-d859-3db0-bfc2-31c137c7390b | -12.20741 | -49.55319 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7c962c0-0590-3ccd-8ff0-cbae4ccb5835 | -11.035 | -45.21102 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28881614-2aca-3416-b1f0-2153e384db96 | -10.71507 | -44.44487 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ac5fdc1-3f9d-3e91-b409-73424d94021b | -9.71906 | -48.89741 | 2025-11-16 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README39.md)
