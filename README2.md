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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b20dd0a3-c05d-3dca-9acc-607fa6ba8c7b | -2.7331 | -57.6271 | 2026-09-12 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 210672a5-17a8-3f46-91aa-0f871d3f021b | -4.3587 | -47.7853 | 2026-09-12 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 35d72579-f0bd-35cb-92c6-5e9037b20e33 | -10.7018 | -54.1458 | 2026-09-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 9a0db51f-3cfc-3801-b5dc-38edf1ad0d22 | -5.7754 | -45.1053 | 2026-09-12 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 586.2 |
| 962fc194-a31f-3bb7-afba-450a15c412fe | -13.3387 | -51.6389 | 2026-09-12 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 30721d1f-9f76-309b-9e81-e5c97f2d858f | -5.7567 | -45.1067 | 2026-09-12 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 80fc1292-57c0-3617-8311-596b9fae6048 | -6.1845 | -57.72 | 2026-09-12 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| bd9e891c-b496-3ab8-abb5-be7553104f70 | -5.7756 | -45.0826 | 2026-09-12 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 591.6 |
| d0ead54d-a4ab-3640-9770-6e0c6f476ce5 | -10.7015 | -54.1663 | 2026-09-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 200.1 |
| dbfd0474-7df7-300e-b230-bf34241b2280 | -3.2313 | -46.9596 | 2026-09-12 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 4f717d19-d209-3154-8cc2-ee1372d2a9df | -6.2243 | -51.6949 | 2026-09-12 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5262740d-07a8-3d70-8eb1-e739cbf0f0df | -6.961 | -44.5546 | 2026-09-12 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 663c91f7-2138-3e8a-8871-180e5ad1f4d6 | -9.7133 | -64.9637 | 2026-09-12 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3c3e5f6a-03fb-3b26-8d1e-996ab903a710 | -10.6824 | -54.1884 | 2026-09-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 31347d04-3df8-3dc2-823c-e0c7e1a46ad2 | -6.2427 | -51.7146 | 2026-09-12 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cf45708c-47fb-3dbf-8f5f-dc4b0ab83fe4 | -2.7148 | -57.6274 | 2026-09-12 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 58a4c7cf-4dc8-3fb6-9de4-a2f9946487e0 | -6.9612 | -44.5316 | 2026-09-12 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f28ff951-91e6-3025-bf4b-0d549b9446f6 | -2.7148 | -57.6469 | 2026-09-12 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 841ee470-cf0f-3f50-a0c0-029cd4b841a6 | -5.7569 | -45.084 | 2026-09-12 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 45b15800-d36c-36a6-b591-f10669916be0 | -3.2314 | -46.9376 | 2026-09-12 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a8fb436c-c5c3-3564-b5aa-5ad6635296d2 | -10.6829 | -54.1475 | 2026-09-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 31d84d35-6090-3db4-a9f2-0a47c87744c6 | -10.6827 | -54.1679 | 2026-09-12 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 337.8 |
| d7da3765-f248-3b6b-9455-aab598775d09 | -18.8868 | -46.9692 | 2026-09-12 00:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 51.9 |
| bfa42fb7-e05e-3f26-8f3c-693a9b2259a9 | -9.6451 | -49.6817 | 2026-09-12 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 39379b18-e1a6-3587-b108-d0751b99f452 | -6.2429 | -51.6939 | 2026-09-12 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| e5fd56d8-e1a1-382c-abfa-ea1147cabb02 | -9.7133 | -64.9637 | 2026-09-12 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5409a472-0d5a-3900-9f23-2deb3eef401f | -5.7756 | -45.0826 | 2026-09-12 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 484.9 |
| 659691f3-c285-3839-8f27-1e7ea898bdd0 | -8.9082 | -45.4342 | 2026-09-12 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 89dfbb0e-b2d5-394d-88b9-39ccf6224496 | -2.7148 | -57.6274 | 2026-09-12 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 12ad7ff3-bb07-3335-9d08-1d9f9fd167ab | -2.7331 | -57.6271 | 2026-09-12 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c82c40dc-3863-3329-9a22-e47896ed5ce5 | -18.8868 | -46.9692 | 2026-09-12 00:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f467b09c-1d39-3f75-ad12-e21e750505c4 | -10.7015 | -54.1663 | 2026-09-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 299.9 |
| aa7fab33-4962-3d6a-b386-9a7a183357f5 | -5.7567 | -45.1067 | 2026-09-12 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 283.5 |
| 10cedd71-d60f-365b-9eaa-0e9744a25509 | -10.7013 | -54.1868 | 2026-09-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 75895b21-d94d-3160-9ab7-7a202eef850f | -8.6497 | -66.491 | 2026-09-12 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| ccafd384-d1da-3b5d-97b1-cdb6ea36b18c | -8.9085 | -45.4114 | 2026-09-12 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 878532d3-df21-3e59-95bb-2903dd5fea55 | -5.7754 | -45.1053 | 2026-09-12 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 438.7 |
| 938cb6c2-afe9-3de3-a0e0-991ac0cee52a | -3.2313 | -46.9596 | 2026-09-12 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 7d1fd237-8bf3-380b-849b-24a40b8af9ae | -10.6829 | -54.1475 | 2026-09-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| aaf1e1c5-c106-3486-80a4-c04b22621761 | -20.7378 | -54.6254 | 2026-09-12 00:40:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 130.3 |
| bca800cc-c853-38d5-a579-d7ce538ea197 | -6.2832 | -59.9202 | 2026-09-12 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 648a7f44-e593-3af3-8080-b3c84af658a0 | -6.2243 | -51.6949 | 2026-09-12 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b9d879c1-5f97-3b86-ba05-129864d8567c | -2.7148 | -57.6469 | 2026-09-12 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8c72e929-5bd0-3a59-9bcc-612140a02bec | -2.7331 | -57.6465 | 2026-09-12 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1705d8b9-c8e8-3c79-9ebc-b6d4c46b0402 | -10.6827 | -54.1679 | 2026-09-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 266.6 |
| 58c69f70-d000-318f-8dd8-69473042063e | -6.2831 | -59.9394 | 2026-09-12 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8454a148-4dd0-31f3-a9ab-02b0871c06bf | -5.7569 | -45.084 | 2026-09-12 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 321.4 |
| 51de6341-6a40-370f-ac70-e1b1e613d4a6 | -8.9607 | -67.3918 | 2026-09-12 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| fc049533-b160-388d-a024-b04316df2011 | -3.2314 | -46.9376 | 2026-09-12 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2151be4a-66d9-3271-ac3d-10b96e9c7129 | -6.2429 | -51.6939 | 2026-09-12 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| e904d39f-04de-3f76-aa56-3f9dab38efaf | -10.7018 | -54.1458 | 2026-09-12 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 760f5397-1970-3e98-9ac5-3345cbcddaeb | -12.8543 | -44.386 | 2026-09-12 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 93334c85-ab54-3a3e-a2ee-78567efdb898 | -6.961 | -44.5546 | 2026-09-12 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a002cc20-7a21-3201-9c5a-bfadc68bb300 | -10.7013 | -54.1868 | 2026-09-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 81340f28-bbce-3e77-a0d9-199ec1ec15a4 | -3.2314 | -46.9376 | 2026-09-12 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| cafe5171-17c2-30a1-9748-6a7d6b6d5269 | -2.7148 | -57.6469 | 2026-09-12 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ff89dcb0-552b-378a-b12b-fdaf226cb150 | -2.7331 | -57.6465 | 2026-09-12 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 798189f2-5ca0-3b51-af1b-a40586eb3c49 | -10.7018 | -54.1458 | 2026-09-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c923ee16-c2df-3e18-bd78-ceaf24007687 | -10.7015 | -54.1663 | 2026-09-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 278.2 |
| 0abc5a76-b2a7-3203-bf54-2a00fed23b11 | -3.728 | -61.7555 | 2026-09-12 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 18fa069d-f0ea-3892-9301-7aec3d22e709 | -6.9612 | -44.5316 | 2026-09-12 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 99c61de0-3205-3af3-bb72-0e9e98b75a3f | -6.2429 | -51.6939 | 2026-09-12 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 7699312b-cb0c-3aaf-b01d-2d800dd2212e | -5.7569 | -45.084 | 2026-09-12 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 268.7 |
| d38d26f8-1dec-3f17-b35b-9804c9f69b5c | -5.7567 | -45.1067 | 2026-09-12 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 15bc5bfb-24cf-3923-8af5-0fc08a659b1c | -10.6827 | -54.1679 | 2026-09-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 311.9 |
| 531cbc20-61c9-365e-bc09-7bab4c30cd4e | -2.7148 | -57.6274 | 2026-09-12 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 58075acb-5511-36f0-a9de-4b16fe79dff8 | -5.7756 | -45.0826 | 2026-09-12 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 486.7 |
| ef51742c-4c5f-3ace-838f-e9e640556a53 | -3.7462 | -61.7552 | 2026-09-12 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3b620b15-a737-3a66-8cf1-95ede5cbc606 | -18.8868 | -46.9692 | 2026-09-12 00:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a43efab5-b914-34be-9511-f3348cec9d72 | -4.3587 | -47.7853 | 2026-09-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 02f3e58f-34e9-398b-9ffb-8612ba3be3b5 | -10.6829 | -54.1475 | 2026-09-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 204dcf5d-6a0a-31a9-9d35-f23634a80c6f | -5.7754 | -45.1053 | 2026-09-12 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 402.6 |
| 9a9d55c7-3c44-3bda-925f-721c46e29c14 | -2.7331 | -57.6271 | 2026-09-12 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1de74f3c-e101-386d-bbe4-ffc8ee3ee96b | -6.2243 | -51.6949 | 2026-09-12 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4dbf6a31-1ca4-379a-905d-1d40050c09ae | -3.2313 | -46.9596 | 2026-09-12 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| a4ae5cac-1aef-3ad9-9b88-900b1a5b98b0 | -9.6451 | -49.6817 | 2026-09-12 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7b154992-ba08-38a3-a35b-d5f635de0669 | -10.6824 | -54.1884 | 2026-09-12 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 39f9c685-783a-350e-8712-e0622e6c23c5 | -20.73158 | -54.629 | 2026-09-12 00:58:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 24747644-70da-3904-80d1-b4b35713e723 | -6.2429 | -51.6939 | 2026-09-12 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 7cd292c4-574b-3d54-991d-14e4e70a99b4 | -3.2314 | -46.9376 | 2026-09-12 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 7b1ec399-6fd5-3d4f-96b6-17c6e0574f4b | -10.6827 | -54.1679 | 2026-09-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 361.1 |
| e161254d-f2a1-380f-a30f-982fc64ff16a | -4.3587 | -47.7853 | 2026-09-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2d0abfc8-c6e8-36ae-b0c0-7b558f87602c | -9.6451 | -49.6817 | 2026-09-12 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 1d1b6df1-49a7-3dfe-a59e-860abaedb996 | -20.7378 | -54.6254 | 2026-09-12 01:00:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 6ef67bb8-3d64-3619-a4d7-c285221d91ec | -2.7148 | -57.6274 | 2026-09-12 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ff257269-c852-34fb-bf97-4a9fa7ee7d66 | -5.7567 | -45.1067 | 2026-09-12 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| b544db6f-ad66-3351-8661-90976694af21 | -6.2243 | -51.6949 | 2026-09-12 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f176d094-5cbb-36a3-93cb-41158a36b15b | -10.6829 | -54.1475 | 2026-09-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d59f8233-3695-3ca3-8d89-a3bb4487149d | -10.6824 | -54.1884 | 2026-09-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fae0cd1f-3807-3fc8-93ec-879fa34805b2 | -2.7148 | -57.6469 | 2026-09-12 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c8407b78-d20f-3212-bca3-a252faf927b9 | -6.6206 | -58.8483 | 2026-09-12 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 00b41c84-1694-3e10-8c43-6ef8a7799510 | -9.7133 | -64.9637 | 2026-09-12 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 91ec1f79-8665-32aa-aaab-3a85ddb67ab9 | -2.7331 | -57.6465 | 2026-09-12 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| f2194607-9726-3d8b-b392-0384c46b7cdd | -8.9607 | -67.3918 | 2026-09-12 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e7950857-eebb-392c-b402-f17b3878d2a1 | -12.1501 | -64.1414 | 2026-09-12 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6adf706d-1335-31cb-852b-dfa160c5f5e9 | -14.5912 | -52.6673 | 2026-09-12 01:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d0ebcbbd-0209-3a65-b483-0ab26067d3d5 | -5.7754 | -45.1053 | 2026-09-12 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 356.7 |
| fe8d1fbe-2f99-35de-9b55-8738bfc9dd71 | -2.7331 | -57.6271 | 2026-09-12 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c27c3412-32ff-3c01-9200-d5313ce01b88 | -3.7462 | -61.7552 | 2026-09-12 01:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 63342772-b629-331b-ba86-c992fed61067 | -4.3772 | -47.7844 | 2026-09-12 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |


[Clique aqui para ver as próximas entradas](README3.md)
