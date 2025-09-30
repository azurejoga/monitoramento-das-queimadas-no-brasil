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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d346acff-06f5-333d-b1c1-d495d32941e5 | -8.8734 | -46.6539 | 2025-09-30 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| b52bdc26-a025-39d3-8856-4726986811ba | -13.3812 | -48.0685 | 2025-09-30 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 1f2ef24d-96eb-380e-a461-8ba6894090b8 | -8.8732 | -46.6762 | 2025-09-30 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5805258d-ea31-32be-a6d7-564f09207c04 | -7.8696 | -47.2606 | 2025-09-30 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f050a326-b359-389f-a481-6e12dd4dc4b8 | -7.9191 | -44.6245 | 2025-09-30 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 5c73b0a5-6e03-3409-b403-83996a0a821a | -8.8229 | -46.189 | 2025-09-30 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 78f5ad60-b0d9-3b17-9959-788158976151 | -14.5146 | -48.4075 | 2025-09-30 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 598089d1-071e-3f2f-9c67-7d11018a736c | -15.9273 | -46.2101 | 2025-09-30 12:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| c1c0c43c-b986-3c8a-a851-9af4c8a74bd9 | -13.4005 | -48.0657 | 2025-09-30 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 688f7ff4-5eaa-3e6e-8d65-d8afedee6c92 | -8.8546 | -46.6558 | 2025-09-30 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9f0dd027-65f4-3643-9132-6fb3257af735 | -9.0425 | -46.7032 | 2025-09-30 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e7d9b768-e2e6-323f-af81-292ef1400cb3 | -11.2711 | -47.2012 | 2025-09-30 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5bd74b3b-c4f8-3c53-9774-4cfd4dced722 | -11.2707 | -47.2236 | 2025-09-30 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| be582202-b673-3be4-8090-53b5a874c5f5 | -13.7319 | -54.7307 | 2025-09-30 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8800ebeb-49e7-3360-9477-0945872358de | -14.5517 | -48.4907 | 2025-09-30 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c353e039-d2c4-3e3e-bc43-a24333f68a41 | -8.7331 | -47.334 | 2025-09-30 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 56937421-5ee0-3ff3-847d-aa646e4cc354 | -10.1851 | -44.8939 | 2025-09-30 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| dc59241f-8b01-3150-a363-240b0190a695 | -10.0717 | -50.2173 | 2025-09-30 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a2459939-d446-3b39-9d51-b0b199071da4 | -14.5141 | -48.4299 | 2025-09-30 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 380f367b-3423-3ae8-9be8-4f0541af43a2 | -15.9268 | -46.2334 | 2025-09-30 12:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 066232da-3860-348e-aa24-5d237061ec56 | -7.0103 | -45.2116 | 2025-09-30 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f8f80ca3-e4dc-3c95-a342-ba93008add8e | -12.2344 | -47.8086 | 2025-09-30 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| ea101e39-7646-3e3c-b29e-d1b5920366f4 | -12.8774 | -45.1742 | 2025-09-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| db43295b-a257-3b16-ab33-208ff8db4232 | -10.1234 | -47.783 | 2025-09-30 12:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1bb059e2-2142-3842-87df-d1f876863f29 | -12.2153 | -47.8112 | 2025-09-30 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a70e74db-718a-3045-a6aa-5b031a7ba376 | -11.1546 | -54.126 | 2025-09-30 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a5aec750-421b-34e5-b85a-f25185d864fc | -12.7022 | -45.2715 | 2025-09-30 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e3a0ced7-6c77-30b5-8022-5ff8149b6877 | -8.2252 | -45.7772 | 2025-09-30 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| edd18164-584b-3a41-baf3-46d75063b4be | -8.8417 | -46.187 | 2025-09-30 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 99e8f882-3fc2-3009-8794-334ba2896326 | -7.835 | -46.9986 | 2025-09-30 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 97bea583-814d-3757-ae1b-55718e6edf6c | -8.8229 | -46.189 | 2025-09-30 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| b914d0cd-7508-350b-be6f-60f4b20ee9ec | -13.3812 | -48.0685 | 2025-09-30 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 3ece1ccc-8c04-324d-8710-89cf2dfe0122 | -8.541 | -44.6515 | 2025-09-30 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5058a61d-b6f4-35ae-9a50-55a12235dc86 | -12.2153 | -47.8112 | 2025-09-30 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3b6b8ee6-fe48-3de6-b4cc-c3a891033739 | -13.4005 | -48.0657 | 2025-09-30 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| e37e192b-06a4-3f4e-aacc-758300a5fe0d | -7.8696 | -47.2606 | 2025-09-30 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 341e8f8b-4b7b-3101-b409-0e8f34c3aaea | -10.1851 | -44.8939 | 2025-09-30 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7569a4f4-9cbb-3778-821a-0332e388c198 | -8.8734 | -46.6539 | 2025-09-30 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 00026499-dd90-3911-b48a-60e7ad61cff7 | -8.244 | -45.7754 | 2025-09-30 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4f0364e2-a96c-3c14-9b7b-c4d79a4aaf54 | -16.7575 | -51.3482 | 2025-09-30 12:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 5b527ca6-7cd7-3a79-b005-0b100d4b5be4 | -14.5517 | -48.4907 | 2025-09-30 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 22237d64-c860-3ab6-947b-35057d099a21 | -7.938 | -44.6226 | 2025-09-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| c145d516-fea0-3e19-a0ef-2027a746607b | -14.5141 | -48.4299 | 2025-09-30 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| e5e29c79-c6bf-36df-ae4e-d1250d721b65 | -10.0717 | -50.2173 | 2025-09-30 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4fedccf1-bb06-303b-8939-413720617659 | -12.2344 | -47.8086 | 2025-09-30 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4639caf7-81d1-3b19-8e37-7729511ea209 | -8.8732 | -46.6762 | 2025-09-30 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 04158fae-ea00-3ee5-935e-5461758b92ac | -14.7367 | -45.2255 | 2025-09-30 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 146fb4cd-a745-3ffb-89be-72676721bbca | -7.9194 | -44.6016 | 2025-09-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 384.5 |
| e12ba8ce-db58-33b3-972c-31ebf6bc8cb2 | -12.8967 | -45.1711 | 2025-09-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| f9820c81-f463-3139-b598-5bb7dc2c17ac | -9.4028 | -46.5751 | 2025-09-30 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a4558e7d-7993-3ed3-9946-bb4d8f382fc7 | -13.7319 | -54.7307 | 2025-09-30 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4ce7e95b-a158-38ab-b903-7d97bfdd45a8 | -11.2516 | -47.226 | 2025-09-30 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 500aab2a-5193-33df-b911-67b72995fe29 | -15.9268 | -46.2334 | 2025-09-30 12:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 27df74aa-9530-3789-b521-af419f6e6d02 | -10.1045 | -47.7851 | 2025-09-30 12:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 3a9b1a38-c073-394e-b0d7-2b3d5011a36d | -11.1735 | -54.1242 | 2025-09-30 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 357e88fe-657d-38ce-b20e-580dd28c8cb3 | -12.6829 | -45.2746 | 2025-09-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2b4225e7-4576-3b01-b1b0-d0ad80ec6344 | -10.8246 | -45.3611 | 2025-09-30 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b06132d9-b8a4-30d4-8913-167ddf199d07 | -12.8774 | -45.1742 | 2025-09-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| a4689e00-2e1b-39be-b3f3-358a3fefcdcf | -18.2176 | -53.3177 | 2025-09-30 12:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f9f672bf-c0da-3a24-bfb0-a599f39ce966 | -11.1546 | -54.126 | 2025-09-30 12:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 0c8b0e5c-ca41-302a-a961-52fe7cdc448b | -15.2654 | -49.7273 | 2025-09-30 12:30:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 96c08883-daf7-3869-909a-f6d70c05ea19 | -15.9273 | -46.2101 | 2025-09-30 12:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 146.0 |
| e1f53686-9369-3772-9f41-f3c3be7e250a | -9.8848 | -45.9349 | 2025-09-30 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 4a193950-6e9e-3569-9c36-8190df0e6748 | -12.8429 | -47.0063 | 2025-09-30 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 61bf20c2-3e35-38ea-96f6-e4f90a0145ec | -11.2707 | -47.2236 | 2025-09-30 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 47746fe4-1ff0-32e5-990e-b999c1ffa490 | -7.9191 | -44.6245 | 2025-09-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 489.6 |
| a09b8483-222f-3086-9610-1cdb87ef6077 | -8.8737 | -46.6315 | 2025-09-30 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8ba2d8b5-96a2-32ef-beea-cec8b16682cd | -10.9586 | -46.5016 | 2025-09-30 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0a0681aa-7078-3339-b182-6572124c2e67 | -14.5323 | -48.4938 | 2025-09-30 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c2fd5eeb-56f2-3334-8e8d-982e1641c576 | -12.8967 | -45.1711 | 2025-09-30 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 49f49111-fdc8-3d1f-9033-f785106bcb6f | -12.8774 | -45.1742 | 2025-09-30 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.1 |
| 679c0c01-65a6-383f-8c64-f86ce2d048fb | -7.5146 | -45.4385 | 2025-09-30 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a63f0bc4-39d0-300d-884a-156a1b6c45a4 | -10.1851 | -44.8939 | 2025-09-30 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 08cfe502-9865-3d67-94f2-9e2ff2f7e3eb | -12.2344 | -47.8086 | 2025-09-30 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 8ef46272-bdfb-36b7-b2d1-cae00a345519 | -10.1045 | -47.7851 | 2025-09-30 12:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e564d29c-a342-3aba-a3b9-1c0396a3858c | -7.8696 | -47.2606 | 2025-09-30 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4c64d83e-7e89-3c3e-a0d9-51903c6dc2b7 | -14.5517 | -48.4907 | 2025-09-30 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9121a482-1d0d-35e9-b9a5-6cd809b726c7 | -7.9191 | -44.6245 | 2025-09-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c6a21e09-e963-3c09-b3ee-aba792dd30d4 | -8.244 | -45.7754 | 2025-09-30 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0ec52244-8449-3c54-ae08-3c934fca7269 | -15.9273 | -46.2101 | 2025-09-30 12:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8d535972-95f6-3e86-90ba-3bf9afaecf22 | -8.8229 | -46.189 | 2025-09-30 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 54ac97b3-15f4-3975-b876-97c8a0cecf89 | -14.6603 | -46.9663 | 2025-09-30 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 05eee9ff-08f1-3b05-90d4-d673e81b9953 | -17.921 | -57.5952 | 2025-09-30 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 23724a26-d500-3501-b1bc-d70918f08fd3 | -7.835 | -46.9986 | 2025-09-30 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 219c5878-bcab-3cfa-9d3a-2bf4d1b9975b | -12.8429 | -47.0063 | 2025-09-30 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9a7a8dc4-287e-32c8-8fc5-892ae66ead10 | -6.7999 | -43.808 | 2025-09-30 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| bf1d4f06-f888-38e2-83b4-1d3906fdad1b | -9.4007 | -54.6984 | 2025-09-30 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0dbf8f2d-6974-364b-9a6f-f1f7eac42b5d | -8.6479 | -46.61 | 2025-09-30 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cceb1261-4be3-3651-ae88-b5d8a8d6f807 | -14.5327 | -48.4715 | 2025-09-30 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 836a09c3-b4ae-3cdb-9ac2-d6560e97ef6f | -13.4005 | -48.0657 | 2025-09-30 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 850d9552-eccd-35c3-9c86-df21743c5648 | -12.7022 | -45.2715 | 2025-09-30 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 31d9faa7-90b1-31ed-b226-7128ee98e53c | -14.5141 | -48.4299 | 2025-09-30 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c4fc599f-5c00-3a86-b5b5-6125217f8f63 | -15.3988 | -47.0654 | 2025-09-30 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 7fff7a32-7295-3445-a630-d67200c10a89 | -15.9268 | -46.2334 | 2025-09-30 12:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f45b1bbf-cf6d-37df-87e9-c6cb77e9f1e9 | -13.3812 | -48.0685 | 2025-09-30 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4a4280bd-64cc-3192-b792-2f66d78044f3 | -11.1546 | -54.126 | 2025-09-30 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b492d89e-73df-3e28-9573-fc975c777e31 | -16.7575 | -51.3482 | 2025-09-30 12:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 216.4 |
| a03bd43a-c283-3eae-9dd4-776c83fcb41b | -7.938 | -44.6226 | 2025-09-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 27d26283-4198-3fb6-b207-8861ea9e344e | -7.9194 | -44.6016 | 2025-09-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| aebe5d4c-08be-3aba-837b-a83c33504957 | -9.1248 | -47.6256 | 2025-09-30 12:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |


[Clique aqui para ver as próximas entradas](README110.md)
