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
| 5b34893e-13c4-3105-8f74-290967db665f | -3.347 | -53.3279 | 2024-12-18 00:27:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb7f866a-df82-3dbc-924c-27423536724f | -3.0563 | -40.040901 | 2024-12-18 00:27:00 | METOP-B | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7846adfc-3848-3ea8-9598-18dde82a67b5 | -1.9821 | -46.5364 | 2024-12-18 00:27:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03950cdd-905b-31a6-8563-976b162a0a2c | -4.9643 | -43.7182 | 2024-12-18 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8df46998-ac48-3459-95b0-37581ad6033f | -3.5153 | -53.9542 | 2024-12-18 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5dba12eb-9852-37a9-8e4f-8ecde53e3bab | -11.8648 | -43.8172 | 2024-12-18 00:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 22c74095-8fdd-3d91-901e-ebcf6bfc1b35 | -4.9832 | -43.6938 | 2024-12-18 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3fef2024-4d63-3318-ba23-ef4747d700fc | -1.6963 | -45.7864 | 2024-12-18 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 2c3dc513-8ab3-3651-922f-df820b7fb22a | -4.1049 | -46.7467 | 2024-12-18 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3b9cc3ab-a2c5-3ba1-b1fd-53fa4aa519e9 | -6.9715 | -43.5833 | 2024-12-18 00:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 18aa1643-2770-3bec-be81-1a89a12282f3 | -11.8643 | -43.8408 | 2024-12-18 00:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| a2116c73-de41-315c-9689-d6e5ad55ead1 | -11.8455 | -43.8202 | 2024-12-18 00:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a2545079-d5ba-3388-89ed-7d3113e1918e | -6.9718 | -43.56 | 2024-12-18 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 33d34e66-d988-36dc-9e78-d8eaa040aba1 | -2.0816 | -54.2278 | 2024-12-18 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ccda449e-bf57-35e5-85b7-5ab1e0450948 | -4.9645 | -43.695 | 2024-12-18 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 144e7930-fc78-3ace-8c85-faf3ec6dc0c8 | -20.7425 | -54.409 | 2024-12-18 00:30:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 01f20f24-7e0c-363e-9f53-aa54e2dcafe7 | -4.983 | -43.7169 | 2024-12-18 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 49239230-e503-3868-9dc8-2c9bd08ac44d | -1.6219 | -45.8548 | 2024-12-18 00:30:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fcbb85f3-bd85-39ac-9d4b-1f029666eeb9 | -3.4969 | -53.9547 | 2024-12-18 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| bdd07ddd-50f2-3a4e-adb9-ab4c8c0ec78d | -3.8619 | -47.0218 | 2024-12-18 00:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eef163c2-091a-37cc-9b13-688f3341125e | -1.7148 | -45.786 | 2024-12-18 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 9c604c8e-a877-3a2a-8a13-6448eff835ee | -6.3898 | -35.0729 | 2024-12-18 00:30:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 67aadb42-11aa-3798-8b8a-a4549f1d3ecb | -11.884 | -43.8142 | 2024-12-18 00:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ae2c25a4-3212-3a4e-af6b-d4952bd18256 | -5.9369 | -48.0654 | 2024-12-18 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0723f58d-28a0-3842-90cb-65c749ad6b10 | -4.105 | -46.7246 | 2024-12-18 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| f0a4c192-3774-306c-93db-a35ecc561f0f | -6.9718 | -43.56 | 2024-12-18 00:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 917c47b3-17e7-3f22-af6c-9a78ca4df882 | -5.9183 | -48.0667 | 2024-12-18 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 20f016e9-c2e1-3b10-8acd-8b906ed95adb | -5.3523 | -44.2913 | 2024-12-18 00:40:00 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 88330f42-39b4-3693-83f6-b86825391a70 | -11.8455 | -43.8202 | 2024-12-18 00:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d511b526-321a-33bc-ab92-418e180d02de | -1.7148 | -45.786 | 2024-12-18 00:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 5f7da4a9-8a28-39c4-b87a-3c8338fedc09 | -11.884 | -43.8142 | 2024-12-18 00:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4824863a-2cce-31b9-8c6e-02e397d9e641 | -20.7222 | -54.4124 | 2024-12-18 00:40:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0aa75298-8e9f-3f5b-bc05-811c3a3d583a | -5.9369 | -48.0654 | 2024-12-18 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| eed9dc99-d05a-3995-8514-c9fa7e066c02 | -9.9328 | -59.9247 | 2024-12-18 00:40:00 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6519d9cf-268f-39b7-94f0-b4a150fb8625 | -11.8648 | -43.8172 | 2024-12-18 00:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 409f99c4-5dd4-3808-b354-083f12629373 | -3.8619 | -47.0218 | 2024-12-18 00:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 34ebb9ff-8a34-325d-958f-6074cbf22374 | -4.105 | -46.7246 | 2024-12-18 00:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 6f85f304-058e-3ecf-ad60-fdcc91e0345c | -11.8643 | -43.8408 | 2024-12-18 00:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 4f80c895-3fa3-31dd-a3b7-e3fa22a26870 | -6.3898 | -35.0729 | 2024-12-18 00:40:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| a6e9c9e4-8480-3e09-8ec5-e926e11f706f | -6.3898 | -35.0729 | 2024-12-18 00:50:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| e21de64f-7350-3bb5-b133-b1ea1180e1dd | -5.9369 | -48.0654 | 2024-12-18 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 22a61dc9-b9e6-3984-b89b-951d7ed6441a | -4.5375 | -43.304 | 2024-12-18 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 68bbfd70-d14a-353d-aaa6-efd09e33dfd8 | -11.8643 | -43.8408 | 2024-12-18 00:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 523996b6-0f0e-35a6-9a9f-72f7f009759f | -4.5376 | -43.2807 | 2024-12-18 00:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7cf9e054-9e33-35f8-979c-1fd6c87ae9aa | -1.6963 | -45.7864 | 2024-12-18 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 858538d3-c9c7-3e7f-9b74-778fe5f44a2e | -10.0484 | -36.1581 | 2024-12-18 00:50:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 128.2 |
| 0a9f73c5-59df-3230-b99c-8922960356f6 | -5.9183 | -48.0667 | 2024-12-18 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| eeb4148d-aff1-345b-8636-21f0a12b5cee | -1.7148 | -45.786 | 2024-12-18 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7c94b9fd-4c18-3875-bafa-67bc6b7174c4 | -4.9643 | -43.7182 | 2024-12-18 00:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 03950cf3-8ed0-354b-b27a-faa90f4e9514 | -11.8648 | -43.8172 | 2024-12-18 00:50:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 426e4f9e-561c-39d2-80b0-a4f1e4e139c1 | -4.105 | -46.7246 | 2024-12-18 00:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5ed61e66-4cf0-371e-bbe3-96a9475cfd44 | -3.4969 | -53.9547 | 2024-12-18 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c612458a-7a5a-329d-bacc-9c42190e1445 | -6.9906 | -43.5582 | 2024-12-18 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 7125e96e-3727-3c5d-b549-a22ff704b906 | -4.5563 | -43.2795 | 2024-12-18 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 71716c88-9175-3972-ba3a-794638a70ec2 | -4.9643 | -43.7182 | 2024-12-18 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 378.2 |
| 1994ccdb-96d1-31b5-a385-1be1e9b0547b | -6.3898 | -35.0729 | 2024-12-18 01:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| d9edc81e-2065-3cb0-a061-3820ba6a9de2 | -5.9369 | -48.0654 | 2024-12-18 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 186c33db-b3ca-3750-9c92-cdc44ded678a | -4.983 | -43.7169 | 2024-12-18 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 434.1 |
| 0f636bac-4ef1-3ba6-b769-ac25c5802a3c | -6.3902 | -35.0454 | 2024-12-18 01:00:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| f840d1a4-5b93-39a9-af67-b5b36d1ede00 | -4.9645 | -43.695 | 2024-12-18 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b7fe7507-91df-38bd-a74c-e5e03bb14e1f | -6.9903 | -43.5815 | 2024-12-18 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b39876b9-a16e-3d4a-8a17-b414c9ae7bfa | -6.9718 | -43.56 | 2024-12-18 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e0540163-1846-3047-a989-fb0639800fb5 | -4.9832 | -43.6938 | 2024-12-18 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 9a795485-25dd-3e31-96f8-c72ca4a370f6 | -3.8619 | -47.0218 | 2024-12-18 01:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| eac26e26-6221-3a24-9d3a-0c175d3d8bba | -11.8643 | -43.8408 | 2024-12-18 01:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9958620c-1160-3dcf-b71d-fd2775281019 | -11.8648 | -43.8172 | 2024-12-18 01:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 1b73a869-72eb-3f7a-b8af-3c9b2c46d375 | -1.7148 | -45.786 | 2024-12-18 01:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 27f0c6e2-4a32-35c1-a3eb-757f915433cf | -4.105 | -46.7246 | 2024-12-18 01:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 21aa3600-c6b2-37ca-aa6d-b0bcd8b9e1d5 | -3.1504 | -53.1559 | 2024-12-18 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9e75e4cc-dfa6-3ce2-96a3-84afe24661cc | -4.5562 | -43.3028 | 2024-12-18 01:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ae3f48b4-6292-350b-bde8-492fbc8e07b9 | -4.9828 | -43.7401 | 2024-12-18 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 6732b8eb-7195-3151-ae60-919eedd770b6 | -4.9641 | -43.7413 | 2024-12-18 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 894fa04f-4135-3b03-86a7-2033d89b1db3 | -5.9183 | -48.0667 | 2024-12-18 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f8cbea2b-565d-3a6b-a75d-3cd4a28a0f93 | -4.96 | -43.68 | 2024-12-18 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fabc374-207f-35a5-83ea-c584119219b6 | -4.99 | -43.72 | 2024-12-18 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ffde633-7e4f-3ca1-a48f-bff81e0be5a5 | -4.96 | -43.72 | 2024-12-18 01:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 021cc9af-809b-3457-9914-6b7b3094bef0 | -6.38 | -35.06 | 2024-12-18 01:00:00 | MSG-03 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ed31ac7-5cc5-31e2-bb18-705a657d56c5 | -3.0164 | -45.2328 | 2024-12-18 01:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 686cdf6d-e9e8-3fdf-ad0e-95fa141cf1f4 | -4.9828 | -43.7401 | 2024-12-18 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d4b3a920-de77-3047-a564-35a6ef98657b | -1.7148 | -45.786 | 2024-12-18 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d26ce77f-11c6-3ded-9e5c-2d3781410cf2 | -3.035 | -45.2321 | 2024-12-18 01:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f5124a88-a8a3-3ea1-8476-b2f26ab674e6 | -1.6963 | -45.7864 | 2024-12-18 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| dd6e887f-2e78-3936-b237-bd8f6d3eab79 | -4.9832 | -43.6938 | 2024-12-18 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| dc177a51-83de-31f4-bec1-3494226a7d15 | -4.5376 | -43.2807 | 2024-12-18 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 56754461-fd8f-3ce4-a813-2dd587e23a14 | -6.236 | -35.2004 | 2024-12-18 01:10:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| ca5fb286-b3fb-3de9-828a-dad861125452 | -4.9641 | -43.7413 | 2024-12-18 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 6be03d60-5c53-306a-a1f7-a55898747276 | -4.5375 | -43.304 | 2024-12-18 01:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b6aca874-9e49-3919-9070-a2e68a637287 | -4.105 | -46.7246 | 2024-12-18 01:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d1a5c731-4581-316d-b0c4-b5481cfd4511 | -4.983 | -43.7169 | 2024-12-18 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 8759baf8-d506-3c9f-935c-692aeb63a5f3 | -4.9645 | -43.695 | 2024-12-18 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c534925e-b8cd-3e42-9ced-885280c967c8 | -4.9643 | -43.7182 | 2024-12-18 01:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 304.2 |
| f7727ffb-85b6-3e52-bf9c-324cf317b3f7 | -3.8619 | -47.0218 | 2024-12-18 01:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 50cf36e3-c076-399f-b15e-563ee89b604c | -4.5562 | -43.3028 | 2024-12-18 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 093e0d90-980a-3887-8c52-9c9c943d4fd9 | -4.5375 | -43.304 | 2024-12-18 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| fc9e46ad-4b51-316f-8e46-d4d90a197ca2 | -4.105 | -46.7246 | 2024-12-18 01:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6228628b-a8a4-37be-aa67-cc1623af1d77 | -4.1049 | -46.7467 | 2024-12-18 01:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f0d7ff62-b5ed-3407-b6ad-7f5eee7e52af | -3.035 | -45.2321 | 2024-12-18 01:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 34610ff5-8348-3e19-8cca-b7b933a6db39 | -10.4975 | -36.8553 | 2024-12-18 01:20:00 | GOES-16 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 3649e087-c800-3d6d-a639-95ffc20a2754 | -4.9643 | -43.7182 | 2024-12-18 01:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| bbd9b866-9569-3a26-a9f3-0f40ed784f16 | -3.0164 | -45.2328 | 2024-12-18 01:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |


[Clique aqui para ver as próximas entradas](README6.md)
