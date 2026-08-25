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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3535ff9-f20b-33cc-8634-f3b6d5982141 | -6.641 | -58.4987 | 2026-08-25 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7443eecc-d055-3c69-8324-f03fe6ebf803 | -6.9873 | -59.2389 | 2026-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 4563f0f7-f912-3bed-8cc7-d8f0eedd0b68 | -7.2194 | -60.6125 | 2026-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 73ae47c9-52a7-3bb2-839c-9ee5beaddc3a | -11.1256 | -44.4659 | 2026-08-25 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 220593ec-6285-3a37-b983-8a61c8ab8df3 | -11.1447 | -44.4632 | 2026-08-25 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 0990183c-ac20-3236-a06f-398fec28c09d | -3.5222 | -48.168 | 2026-08-25 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| dd70c1e9-2068-362f-80ba-ec9c67cb57f1 | -11.1443 | -44.4865 | 2026-08-25 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c3891712-27bf-3870-b7a4-7e48f7c0986e | -3.5407 | -48.1673 | 2026-08-25 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 4713b888-1833-3e88-95ab-609ad391686c | -10.9294 | -51.0654 | 2026-08-25 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| fe3cab12-7840-3fd8-8352-f7cebbdf71ef | -7.2901 | -45.3683 | 2026-08-25 05:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| cab85163-b17a-3c64-b6bf-4f5c70c502af | -7.2194 | -60.6125 | 2026-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 58c859cf-c093-3bdd-9756-e640bc5b16b6 | -6.641 | -58.4987 | 2026-08-25 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 00de2d71-1cca-3581-b415-6dce833fefb5 | -11.1447 | -44.4632 | 2026-08-25 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 850219d8-cc34-3803-8507-2818cf8a0fc3 | -7.0057 | -59.2575 | 2026-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 526b1f5a-917b-39a5-8036-77e3f4ad06e7 | -3.5222 | -48.168 | 2026-08-25 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6c1f531d-cacc-3bc2-a5e4-d58505ce380c | -3.5406 | -48.1889 | 2026-08-25 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| e7afd91a-f39c-3876-8acf-e7510fa0f417 | -11.1443 | -44.4865 | 2026-08-25 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b4ac1200-cdab-3a03-b3a2-0d66f5b8fadb | -7.2901 | -45.3683 | 2026-08-25 05:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9ea3955d-487b-3d66-aef9-68c44b304a61 | -11.9995 | -45.9059 | 2026-08-25 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| bdac0a61-59a8-3ae7-bd80-f0bd34c478d3 | -11.9991 | -45.9287 | 2026-08-25 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 23b16b39-fe95-3406-a9b0-ca7231e43ad5 | -16.8437 | -42.0114 | 2026-08-25 05:10:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 11b1f3fa-21ab-3e82-89a1-9e15a848457d | -11.9803 | -45.9086 | 2026-08-25 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 12c667e0-f2e0-3842-b68a-8a3e5a950e7a | -6.9872 | -59.2582 | 2026-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 16b11717-573d-34ae-9c58-c0bbc5b7ae59 | -3.5221 | -48.1896 | 2026-08-25 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 05dfc2b4-b372-308f-879b-255dc677e740 | -6.9873 | -59.2389 | 2026-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 522b4dcd-8ed3-3d11-be1a-73b87b3fa18e | -7.2903 | -45.3456 | 2026-08-25 05:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b1dc0c27-cef3-3206-be61-9de9103b0182 | -3.5407 | -48.1673 | 2026-08-25 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| dd6171ad-6da9-30b1-a60a-c1ba3d239170 | -7.0058 | -59.2382 | 2026-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 28a3e210-5fd4-3c19-98a5-55ca5ae9a6d1 | -7.2009 | -60.6132 | 2026-08-25 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| c79fdfad-b4a8-3ca2-9c5c-387dae25a5dc | -5.61305 | -47.00645 | 2026-08-25 05:10:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99d72174-d59a-3303-998f-527570930e51 | -6.20651 | -53.4981 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 200354d1-cb2c-3340-8d9b-d43c6293edfe | -6.18526 | -53.48554 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 879e56d7-7353-329b-90b8-7a12983166d1 | -6.21096 | -53.49407 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bfe24fd-4c1c-3df8-9bfd-485dcd502cbc | -5.78727 | -57.55821 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46ab3901-c854-3f21-8f85-e4b0ab034901 | -6.34406 | -54.77694 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6be3db90-e5ae-3f88-b999-dfac97962e5f | -1.42565 | -55.25322 | 2026-08-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5b45348-ceaa-35cf-8a8c-d99a15f3ae4b | -6.23048 | -55.47911 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 676c52bb-0243-35a2-acbb-68c3ff2714ea | -3.26738 | -49.52766 | 2026-08-25 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba739b07-ecf1-31d7-9a87-9e005d0f0426 | -6.24987 | -55.39789 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 882d20cc-8895-3838-bc1c-67f357954349 | -6.22878 | -55.49029 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5149cca6-02b1-3a7f-9148-d6842f460739 | -5.7874 | -57.60067 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9338ce07-8780-3838-a045-925e7a300f7a | -6.22934 | -55.48659 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 777432e1-d433-38c9-8da6-e314beaaf849 | -6.40833 | -51.70916 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36781355-4399-3bc3-95ae-0323f809d5d6 | -4.60774 | -55.74145 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ac9876-dd4f-34ab-ace4-03acc637cc51 | -5.78208 | -50.18803 | 2026-08-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 819b30ae-cc23-362e-a3a7-690f11a466dd | -7.25054 | -45.85641 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c772368c-68c7-3f67-a4d6-17ab87bfbd55 | -3.54486 | -48.17892 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca973cc8-165f-3383-9d68-5b263143bd8c | -3.81792 | -51.91314 | 2026-08-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b002638-73b4-3dce-afda-12ee913eae8b | -7.25966 | -45.37283 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e28ae1f8-99f6-359c-bebe-dabab6f62590 | -6.34113 | -54.77242 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c11de40-5828-31c3-bb8e-7b3b8be76892 | -5.95912 | -53.60073 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f7f8df0-df0d-30d4-8bd5-adbe5a6f1124 | -6.20342 | -53.49296 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87e3d5c9-a9c6-3ef7-816b-2a7f231487ad | -6.2322 | -55.49083 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c2f45881-413d-377d-99d3-ee10ad4c5b44 | -6.34474 | -54.74849 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 141af22e-76cf-3659-aa92-7e2337ef6cd7 | -1.42077 | -55.72371 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a896ad6-2b06-37d2-b022-eb8ed0db5165 | -4.47882 | -54.80509 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ecf730c7-2fe0-3bd7-ab9f-1a918e159d11 | -6.20568 | -55.64177 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7462b083-337c-3213-93f0-f531bbbd3bb3 | -6.19733 | -53.53398 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab650d81-4094-3b4e-bc5c-e540a1739b75 | -6.2247 | -55.42474 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf45a74f-7b16-31c5-8ef5-f1fd72b41212 | -6.60635 | -52.45049 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64bc6f29-3c41-3bec-910f-391e69930c57 | -6.34526 | -54.76896 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4e9080d-0922-38ca-9719-444472fdf607 | -5.78673 | -57.56166 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f063e90a-60f9-3e60-8d56-358c9353ecb6 | -4.93125 | -55.7724 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be9a8db1-3a0f-3bf8-b561-833a4e794f11 | -5.95672 | -53.59116 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52053500-61e3-332f-bcac-b730395c5f7e | -7.29373 | -45.36632 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 181b9254-7d7c-3c31-bf80-5cf297932f1f | -1.78472 | -55.52754 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c86888db-5157-381c-b3d8-d3ce956cd0ee | -6.14501 | -53.80943 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff07a70d-f3d4-36d2-99c8-3092a50b92fe | -3.54495 | -54.49214 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d879a67-db51-33b7-a3f2-832057ecaa2b | -3.53318 | -48.18644 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 4e0a2b77-f9a0-3d95-b912-9b67c4f1490d | -5.77843 | -57.54976 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 658c6e94-f2ef-34d2-8159-fe29b6ae63b3 | -6.20719 | -53.49352 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb53b431-04ad-3b8a-a0ea-594fdb7b33b0 | -4.49308 | -55.4666 | 2026-08-25 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 062c7645-a5b8-3c60-bedc-472a7f4621ed | -3.45555 | -56.807 | 2026-08-25 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1e29195-9f60-3401-a9b3-123a13c383cb | -6.17126 | -53.50219 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a711c9eb-2d44-33cf-9951-e5e82abdde51 | -6.18016 | -55.44078 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| db5abbe2-0b0b-31d0-ad6c-10d87ace0843 | -6.64483 | -45.16969 | 2026-08-25 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55ded531-e56e-35f8-82a7-658762efce83 | -3.01049 | -51.05353 | 2026-08-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac458839-b7f4-3cfa-a275-6aab03755f61 | -3.49179 | -59.29193 | 2026-08-25 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52f36354-7daf-364b-85ee-dea1458e80f3 | -1.42409 | -55.72422 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f742e0b0-9eb8-3712-a612-b799d5a0a5ff | -6.70386 | -52.09118 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 750fc8ac-d97b-33cd-a667-9e3a46885d06 | -6.09507 | -53.41398 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b37a94c2-ffbc-318f-a448-2a21c6705f11 | -6.34181 | -54.74396 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc24f7cd-47bd-39b4-bdd5-8a8f6b7d562f | -4.12949 | -49.45415 | 2026-08-25 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61a57c51-37c9-3d78-a2d9-9554e94f99df | -6.19279 | -53.48667 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 175ea3c7-2d61-3ceb-9ef4-111adb35a721 | -1.86955 | -47.98051 | 2026-08-25 05:10:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc411976-90ef-3f88-ba1f-418bc453f0b7 | -7.26034 | -45.36736 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9062bfda-3e5d-3632-ae2b-f4d97007861e | -5.68776 | -50.09249 | 2026-08-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 674ee721-483e-3bb9-add2-9324d27027e0 | -6.34819 | -54.77348 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5e718f1-7dab-38ad-b83a-317e63084ad8 | -4.49702 | -55.46352 | 2026-08-25 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8acb160-a6c0-39a8-8bf0-280024f28ce3 | -5.72713 | -53.72792 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 632b28da-225e-3c03-a662-28735ad006f6 | -6.17561 | -55.44772 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 695b6047-3b65-39e5-a950-f619e4fdab71 | -3.54842 | -54.49267 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b04a6dd-6339-3b72-b483-cb80a9e4d146 | -6.19357 | -53.53342 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb250b5-38ee-3ea3-854e-99d21d0b477b | -5.9554 | -53.60007 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf906536-1a76-373e-8381-4cd49a51f365 | -6.2453 | -55.42788 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd8bd5cc-f2c8-3143-a477-43cb58023129 | -6.1823 | -53.53173 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a528324-8e0d-3283-89cf-4ff384c3acbc | -7.26525 | -45.84264 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5c98407-e75a-3b89-8c38-7ccd533b7495 | -4.19481 | -54.5762 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ba41761-fa29-3508-86ba-bb78bd227a62 | -3.53455 | -48.17712 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1239b269-828e-3f77-a38f-d32714e5c541 | -6.60523 | -52.45806 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README44.md)
