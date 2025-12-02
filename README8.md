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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bd66bc9-4031-3d59-9ec4-f08b671f5a1f | -10.76578 | -44.93805 | 2025-12-02 03:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205e997f-1ad3-3373-93be-8203418efa67 | -8.88198 | -43.92832 | 2025-12-02 03:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf66660a-329d-3735-829c-257c35006add | -10.11891 | -38.35579 | 2025-12-02 03:49:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d51e9e40-3b83-34a7-9ba5-7feaa01d0ba8 | -8.0513 | -43.1001 | 2025-12-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 257.7 |
| f844815b-e174-3ad4-b2d9-e6c9d2919483 | -8.0516 | -43.0765 | 2025-12-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| da6be62c-506b-3d3e-8f79-1a003200ca3a | -8.163 | -43.229 | 2025-12-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 83de4ffc-3539-3670-bb7d-8658ef9c1d0f | -1.4737 | -45.7907 | 2025-12-02 03:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f1d6ea14-bd5d-32e8-8383-8c9ed12f5247 | -8.1633 | -43.2055 | 2025-12-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| d8d2db0f-605d-3447-b39c-c3c6e591f41d | -11.1379 | -53.9429 | 2025-12-02 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1a839109-13a1-3d26-9aa2-5d8e1c996eda | -8.051 | -43.1237 | 2025-12-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| b140abb3-0902-334b-b440-def5830137d6 | -3.2565 | -45.5607 | 2025-12-02 03:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 96e66542-df0d-39ea-b422-9b16d3433888 | -8.0703 | -43.0981 | 2025-12-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 471ab84a-74b2-356b-a18f-75aaf1aeea51 | -3.2379 | -45.5615 | 2025-12-02 03:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 553f4780-784c-3a49-a31b-0494b5241c31 | -1.4923 | -45.7903 | 2025-12-02 03:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b0afc0c2-3e9f-38a9-a413-efd63b1f4c43 | -20.20664 | -47.4589 | 2025-12-02 03:51:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71d2034f-5a38-3d54-92cd-72a10499ad10 | -17.03193 | -40.32305 | 2025-12-02 03:51:00 | NPP-375D | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 485f90d8-ef4f-31b0-9c39-836a47f86a35 | -20.76298 | -40.67329 | 2025-12-02 03:51:00 | NPP-375D | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd946e3a-92ed-37e7-b16d-965fbf48af63 | -20.09751 | -44.82934 | 2025-12-02 03:51:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b856f086-5fc5-3d4e-be62-236343f46a06 | -17.55976 | -46.4408 | 2025-12-02 03:51:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27fd4da3-fead-3432-b140-11f8f8ce4909 | -17.55784 | -46.44791 | 2025-12-02 03:51:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2b72012-0f52-3c52-8bb6-2fca7ce76aa4 | -17.86348 | -42.24889 | 2025-12-02 03:51:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 559fbb34-3b7c-38fb-a81d-68df67fe230a | -17.55909 | -46.44192 | 2025-12-02 03:51:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3c2cc45-e3bc-398a-99a4-b9f58c004d98 | -17.85966 | -42.24809 | 2025-12-02 03:51:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| efef460e-a694-3136-a39e-e0871417b299 | -20.20732 | -47.45574 | 2025-12-02 03:51:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c91e578-8d98-3d2c-a673-392a741188ef | -17.55855 | -46.44681 | 2025-12-02 03:51:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2145af85-ef5e-37be-a816-9c79837590d4 | -17.15149 | -42.78033 | 2025-12-02 03:51:00 | NPP-375D | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba1113fb-d7ff-372b-8f2b-628d1e07a182 | -8.0516 | -43.0765 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| fb2b9ee1-64a0-3cba-aa3e-be222c6945da | -1.4923 | -45.7903 | 2025-12-02 04:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d4b76c08-634b-3ed7-a4fb-a4efa11d535b | -8.051 | -43.1237 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 36d64691-68a5-360a-839e-5c0f60cb0406 | -8.0513 | -43.1001 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.4 |
| 5494dad5-31c2-36cd-8b2e-dcf9e9312cf0 | -8.163 | -43.229 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| eb809325-bc27-3760-bb86-dd57856fecf8 | -8.0324 | -43.1022 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 5a6722e8-22a6-3db1-8db8-a19a0299365b | -8.1633 | -43.2055 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 0193c368-7516-3e0d-abae-f5078d351a28 | -1.4737 | -45.7907 | 2025-12-02 04:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 852713b3-cb0e-36ec-8256-d67a02ec7ea0 | -3.2379 | -45.5615 | 2025-12-02 04:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ce6d89d2-e1fe-3e7e-839c-06b4aa82b404 | -8.0703 | -43.0981 | 2025-12-02 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| d09307a6-6667-31e5-bea5-efe8163529e0 | -1.11006 | -47.34447 | 2025-12-02 04:06:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f08b7838-fe54-3596-8dfb-b7d7c79766ad | -1.35432 | -47.40358 | 2025-12-02 04:06:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61516e36-771c-3661-a1b0-a3aeb3d04c4f | -0.84129 | -47.41251 | 2025-12-02 04:06:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69612d6-c3c9-3e1c-8074-e9fcbd8d6629 | -3.31992 | -42.50282 | 2025-12-02 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f6c7ab2-edca-3efb-b701-222e9390bf61 | -1.35356 | -47.40829 | 2025-12-02 04:06:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23962fea-fad2-32c8-ac5b-69551f6716bc | -1.68925 | -45.79062 | 2025-12-02 04:06:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc068f2-002a-385f-be35-14f55461be1c | -2.0298 | -47.15373 | 2025-12-02 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09d0fab3-29e8-359f-8e04-b7a335944e9f | -3.24099 | -45.57081 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 00b48400-3a26-35b6-ba8a-109efc4d98c5 | -3.25824 | -45.56054 | 2025-12-02 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 90a6bb6a-86e4-37ad-9a82-e7a619c7a9ef | -3.45841 | -42.99463 | 2025-12-02 04:06:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bbab200-7e24-3319-b459-3234db574474 | -2.44291 | -47.08476 | 2025-12-02 04:06:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e80e40c-f0db-3a41-bdc6-b734fec86a68 | -3.86688 | -41.58755 | 2025-12-02 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cb471b1-4244-3edd-bf5e-b08407c7030f | -3.81592 | -40.75057 | 2025-12-02 04:06:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 34cd6b7e-f440-31f9-89d0-083170706143 | -1.14356 | -47.25418 | 2025-12-02 04:06:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd98841-3116-30d6-8a4b-445af0ffe907 | -1.68866 | -45.79423 | 2025-12-02 04:06:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c98c13d-8718-3f90-b25f-78120f14a3fc | -2.44264 | -47.08283 | 2025-12-02 04:06:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf9d033b-372f-3fa4-bcec-630b61ae470b | -3.23705 | -45.57018 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 07f44578-34e4-3851-b314-29ecf75258a9 | -2.91906 | -40.27413 | 2025-12-02 04:06:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5b39c82-abea-36df-a7b7-121ef30c9b8e | -1.4813 | -45.78771 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 233786dd-dbeb-302c-b887-571f830c196f | -2.77545 | -42.48494 | 2025-12-02 04:06:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bce1988-0783-31a2-bfa9-87c7aaea5579 | -3.3233 | -42.50335 | 2025-12-02 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abc802b3-1668-36c8-baa7-cc7f33f40ff3 | -3.58891 | -43.03409 | 2025-12-02 04:06:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 373e206d-3aef-37be-a7b7-827156b49b41 | -3.02459 | -45.0703 | 2025-12-02 04:06:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c48c8274-2632-355a-8d6c-f992f7b89fee | -1.4842 | -45.79575 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7de8d63-70b3-30e3-a94f-a527a3ccf5b1 | -3.26136 | -45.56619 | 2025-12-02 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14a55070-94f3-394b-b41f-4c73e2c10942 | -1.26333 | -47.4451 | 2025-12-02 04:06:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f88369b0-f070-3afd-a324-12929fd0fbf2 | -3.04118 | -40.27585 | 2025-12-02 04:06:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 307a2c80-6e02-3f06-b40d-02ecc7b4bda4 | -1.68807 | -45.79785 | 2025-12-02 04:06:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0451570-efbf-380b-9162-bff183ee5425 | -2.4436 | -47.08045 | 2025-12-02 04:06:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5de1586-d8dc-3ccf-8a36-686a60af4cda | -0.8359 | -47.41653 | 2025-12-02 04:06:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 883e1049-bcbc-3158-8ffe-0ec63fe8f8be | -3.04172 | -40.27239 | 2025-12-02 04:06:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4813d32-77bd-33b1-8968-0bb68a51bf90 | -3.24083 | -45.56805 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7e1a324a-b092-30f2-9927-7557f3c6a6c5 | -1.4766 | -45.79071 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| bf53f625-9fd9-361c-8c90-57602ca704cf | -1.92896 | -52.12037 | 2025-12-02 04:06:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 508f1968-53a7-3540-835f-a7c48c568401 | -1.4801 | -45.79508 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0f957f92-b4ef-3f47-9b22-af3321e9fbc0 | -1.10547 | -47.34377 | 2025-12-02 04:06:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c09afa22-c539-3841-918d-d43c67ef12d9 | -3.55368 | -38.85746 | 2025-12-02 04:06:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b7b4ab7-41f0-30a8-a29e-605d47c99aae | -2.43855 | -47.18953 | 2025-12-02 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 332b3220-7351-3ae5-b9be-44d694b3b8e8 | -1.92816 | -52.12527 | 2025-12-02 04:06:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03d5cf6d-6249-3a9a-a114-5b5a0956877c | -1.86064 | -46.36011 | 2025-12-02 04:06:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fbdd89c-a8b0-3ed9-9a33-2db7b22aa9f8 | -2.31006 | -46.04985 | 2025-12-02 04:06:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 229c4179-e3be-3a92-95e8-6cba8479027a | -1.4848 | -45.79208 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd215c5-1027-3809-9744-195d22a1b1a4 | -2.43517 | -47.1911 | 2025-12-02 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6382ac77-2f19-3c13-9a89-3d67941f5b04 | -3.41221 | -42.45376 | 2025-12-02 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c6f9df1-fb00-32d6-818f-1b75fdd26187 | -3.24 | -45.57307 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0c3d08ae-29bc-38c4-b3c8-9c282efbdc8c | -1.86937 | -44.80645 | 2025-12-02 04:06:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc46d55d-8bf1-331b-a478-f75f85c75b06 | -2.44336 | -47.07855 | 2025-12-02 04:06:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da151a8d-d4c0-38af-adeb-e30337df24ce | -3.23772 | -45.56242 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9b976598-05ad-35d0-8f1d-353f572f3313 | -3.23785 | -45.56515 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7fdcbd00-c39e-3833-a01e-e6f6907b1bc7 | -4.19371 | -38.36413 | 2025-12-02 04:06:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 31d5be98-2ee3-3d19-938b-e9e205675a86 | -3.86634 | -41.59101 | 2025-12-02 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5fbf7cb-65aa-3c48-995f-176e7bbce2af | -3.24179 | -45.56578 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 91ae91e3-ab68-3ce6-a5f7-187fbed83548 | -3.25742 | -45.56556 | 2025-12-02 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f05910be-75c7-3a26-ac40-ad6a8010ecd7 | -3.63569 | -42.23267 | 2025-12-02 04:06:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3959f7fb-b271-3d9d-97fe-f12c61b9074b | -3.86965 | -41.59153 | 2025-12-02 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b04e428-0637-3153-b488-793c168ecef7 | -1.73883 | -47.08876 | 2025-12-02 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8d1690-e89d-35c9-80c8-8c9879fd9851 | -1.47951 | -45.79874 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b358d21e-9339-3598-a331-49ddaa88971e | -1.4854 | -45.7884 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb85877f-bfd9-320a-b24c-c789327ed112 | -1.86487 | -46.3608 | 2025-12-02 04:06:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c454b7f-e9fa-3dff-93e7-b01c69e70e9a | -1.68397 | -45.79725 | 2025-12-02 04:06:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3195efc4-d068-3375-a864-accb25306721 | -3.29392 | -45.51498 | 2025-12-02 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b41d2e6-f4ee-3287-8c36-000e105f3ac1 | -3.86743 | -41.58409 | 2025-12-02 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 052f5bcf-f3ab-39e8-9edc-34d7db416a76 | -1.68516 | -45.78999 | 2025-12-02 04:06:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f2cd62-9fe1-3424-9246-649da8cc674e | -2.24158 | -45.49103 | 2025-12-02 04:06:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
