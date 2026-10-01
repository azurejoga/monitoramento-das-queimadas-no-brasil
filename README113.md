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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56aa46a9-eb3b-37ac-a057-37cfe00b5d3b | -16.08133 | -42.61831 | 2026-10-01 16:11:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 09642fa3-b613-37b1-a3cd-c0ad8f9c6dab | -15.36999 | -47.96021 | 2026-10-01 16:11:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ff7ed978-22e6-3301-81ab-0ac9ab6d8549 | -15.08967 | -48.40934 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2f97cf18-9be2-301b-9692-d8d9a4da7203 | -15.26382 | -40.90153 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| b93a83ed-431d-33f6-8baa-e8d256999ab4 | -14.34198 | -44.73735 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d6eca5ea-285c-3d31-90d4-4d664645a79c | -14.89396 | -44.80707 | 2026-10-01 16:11:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 18d66da1-d33b-38c1-82b4-f5f432bb7790 | -15.62751 | -49.27532 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| e44d25ac-4787-3819-bfda-707e6a16b852 | -15.79148 | -44.69146 | 2026-10-01 16:11:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5e834728-876c-3071-8fc7-79873a76d226 | -14.47564 | -40.70798 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 120.9 |
| 99e92c98-40c1-36ed-9d4f-3e2f343d7e87 | -14.67482 | -41.78868 | 2026-10-01 16:11:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d41729f5-9cae-390c-8fb0-e7e4b834b2ec | -15.09766 | -44.00429 | 2026-10-01 16:11:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6212a8e2-93a2-30fb-b7af-27bde260d992 | -14.64304 | -44.94334 | 2026-10-01 16:11:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c1dfa2f6-277c-3584-bc85-17e8ab6d72b1 | -15.26042 | -40.90204 | 2026-10-01 16:11:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b6e67960-1ffe-339b-bdb3-0abc0f68ff32 | -15.66152 | -44.71646 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 76544fc5-442b-301f-8a44-3c33cb6c935f | -13.95119 | -41.67592 | 2026-10-01 16:11:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 54.3 |
| f0f06492-2d55-3c38-9108-cf0c87910b59 | -14.43281 | -44.76689 | 2026-10-01 16:11:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 129dd764-6a3e-3e31-b0af-e055b5ba6742 | -14.82524 | -41.45063 | 2026-10-01 16:11:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 94.0 |
| f494ab8f-da7b-3420-b93e-cb971b1db991 | -15.23391 | -46.15747 | 2026-10-01 16:11:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e121172c-abce-367c-9246-797a719bd7dc | -14.53368 | -40.50406 | 2026-10-01 16:11:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 58c3ed24-bcd4-39f7-b949-95b087d9ce7e | -15.8565 | -41.71159 | 2026-10-01 16:11:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| 390681e4-af4c-30bb-8d76-069ff02fdcfb | -14.77057 | -40.33671 | 2026-10-01 16:11:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f19e3a3e-9fcc-3207-af35-1b2e3723060e | -16.17685 | -42.8849 | 2026-10-01 16:11:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a7e93cfa-46a3-3932-a468-ed2b55f098a3 | -15.10015 | -48.40543 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 996c3e43-4034-3921-a9d8-4fd839aaae90 | -14.24032 | -44.22846 | 2026-10-01 16:11:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| e4c04c55-bccd-34a5-af40-91dca02270b3 | -15.62568 | -49.27472 | 2026-10-01 16:11:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 4b37a62b-76c7-38d0-aaa6-74a73e0f6a00 | -16.0064 | -42.3724 | 2026-10-01 16:11:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| b1d831d8-fbf3-3c92-8762-14dcbf671844 | -15.09457 | -48.40526 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 03ada4c1-d7b4-37ee-9623-c550536f62d2 | -15.64393 | -44.71091 | 2026-10-01 16:11:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 57790c31-dd89-327c-bf79-90f74f26d5cf | -15.08673 | -48.38278 | 2026-10-01 16:11:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cf87867a-63cd-34b5-b28f-85ad015e72ec | -14.72185 | -41.0258 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 37927d12-6b22-3338-a121-b51bf10d6b7f | -13.66585 | -39.65264 | 2026-10-01 16:11:00 | NOAA-21 | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e228f5cc-c807-3909-abd6-3c216dcd54a2 | -14.46892 | -40.70904 | 2026-10-01 16:11:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 079df0f6-6a94-3f57-81e4-3774df54e14a | -16.2179 | -41.89345 | 2026-10-01 16:11:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| df6ad236-8cb7-38d7-8e17-8ff88d5cfd14 | -15.56796 | -41.21364 | 2026-10-01 16:11:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3b418356-a248-339f-b69e-abdd40ae013e | -16.13933 | -43.74769 | 2026-10-01 16:11:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1968519c-9259-3a1b-9452-4d94f36d2955 | -7.99 | -42.88 | 2026-10-01 16:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f6d53ed-2b58-3fb4-af5f-6a142fc96d5c | -10.19 | -49.97 | 2026-10-01 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 558b4dd1-c27d-38fa-9f76-083b6ee5cfcc | -9.8 | -44.81 | 2026-10-01 16:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99bb6b65-a4bb-3de9-962e-9e346cf58e42 | -9.83 | -44.86 | 2026-10-01 16:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b224b4a-ddb4-3bc3-891c-64932d88e749 | -11.25 | -45.2 | 2026-10-01 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 333c704e-f3a2-3da7-ae43-0b9cde41f8ce | -8.02 | -42.89 | 2026-10-01 16:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f95429d6-cd5a-3e91-955e-aa293b3c9a44 | -9.15 | -49.91 | 2026-10-01 16:15:00 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9797c904-44be-3bc2-b647-c70ee90d5bbd | -14.1 | -51.12 | 2026-10-01 16:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73aa19af-51a4-355f-93d1-8d818aad9cd9 | -8.02 | -42.93 | 2026-10-01 16:15:00 | MSG-03 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ffcdfb9-6fc5-3543-be03-905b06311dd1 | -11.15 | -44.61 | 2026-10-01 16:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8207daf-c9b6-333a-83dc-6fc845825eb7 | -9.83 | -44.82 | 2026-10-01 16:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 484d1773-a59b-32f9-a8f5-115518df57e7 | -1.4672 | -48.931 | 2026-10-01 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a0d0a3a2-7675-30df-9ff2-b0b637e29b92 | -1.4303 | -48.9316 | 2026-10-01 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 219f8126-460c-3a41-8d5c-18200963f85a | -1.4672 | -48.9097 | 2026-10-01 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 150f9fc6-185e-3851-a6e3-eeb867c7a71d | 2.1514 | -55.8172 | 2026-10-01 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| eb9c79e8-3b49-35c9-aa4f-49c5d3d263e1 | 2.1514 | -55.8172 | 2026-10-01 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| a4f76761-179c-3b84-bf45-6fa267d91b63 | -1.4672 | -48.931 | 2026-10-01 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c809393a-8a64-37b7-b697-f51e316bcce3 | -1.3193 | -49.061 | 2026-10-01 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1579c1dc-f648-399a-a6bd-ab6ea1afd812 | -1.4672 | -48.9097 | 2026-10-01 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8ec962c9-e5b8-39e1-a61c-491c446cf073 | -1.4303 | -48.9102 | 2026-10-01 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b7b33241-3e19-3d34-9b8c-e77346145a04 | -1.2818 | -49.3803 | 2026-10-01 16:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c7f98205-e1de-3dc9-a636-1815130864fc | -1.4672 | -48.9097 | 2026-10-01 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 34ddc4c7-c68e-3694-a61e-18a9b2aea7f0 | -1.4303 | -48.9102 | 2026-10-01 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b7517772-9a66-3519-9d18-125fd97fd108 | -1.4303 | -48.9316 | 2026-10-01 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c5017e32-6247-34f4-8c0d-1ff91e9207ec | -1.4303 | -48.9102 | 2026-10-01 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d76e1c7c-34f1-3b46-9bed-7ad509e56bac | -7.0238 | -47.5514 | 2026-10-01 17:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 6b83cd46-baaf-3c33-8077-80c50f22f7a4 | -1.4672 | -48.9097 | 2026-10-01 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 81a2555d-f608-318d-b430-a0a4eb49677a | -3.97 | -41.54 | 2026-10-01 17:15:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a47c71a2-ca7a-3cbf-8921-dac10319fcf8 | -9.12 | -49.96 | 2026-10-01 17:15:00 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0797960-9115-3d6c-b897-850880012138 | -9.24 | -45.82 | 2026-10-01 17:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8dacef4d-9cb7-3970-823a-75464b3d837a | -3.97 | -41.5 | 2026-10-01 17:15:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5938f68-9eca-31b8-917d-1e968037016e | -9.83 | -44.82 | 2026-10-01 17:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f20f0ca7-d56f-3b5a-8c9b-1d7303cd58f8 | -11.23 | -45.19 | 2026-10-01 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68eeacd2-0ea6-3a5e-bbec-d0745cf5ea62 | -9.24 | -45.87 | 2026-10-01 17:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0ddfdd5-6d57-3a24-bd46-4fa163709f8e | -11.12 | -44.6 | 2026-10-01 17:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b62583c-932e-33a0-93e6-8e5dab988468 | -11.2246 | -44.2654 | 2026-10-01 17:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 486b0b02-3be3-3f8e-8d25-17f3cec3afb5 | -1.4672 | -48.931 | 2026-10-01 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0f67015c-5055-345b-806b-1d336962bcf9 | -0.4319 | -52.0151 | 2026-10-01 17:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e25eeb9f-0efa-3650-ad28-b777d851d912 | -11.2438 | -44.2626 | 2026-10-01 17:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 77b28280-55f5-31b9-92b2-d2fb2bcff75b | -11.2438 | -44.2626 | 2026-10-01 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| f1f4a10c-2f3a-394b-a735-cefbc96f9fdd | -11.4503 | -43.4091 | 2026-10-01 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 228.0 |
| d254ee83-8c07-3543-bf30-9a9602159560 | -11.3543 | -43.4238 | 2026-10-01 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 947b193d-760d-3137-81ef-668e9ad55254 | -11.4119 | -43.415 | 2026-10-01 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 95b5fc12-e532-3db9-a985-245c4c4e35d7 | -11.3735 | -43.4209 | 2026-10-01 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 32e39c26-b48a-3015-b922-1afcca470d99 | -11.4503 | -43.4091 | 2026-10-01 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 83d9b268-8e09-331f-8f71-e828e44ef26f | -11.4311 | -43.4121 | 2026-10-01 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 1c1742e5-fea0-3105-a6ea-c94734607463 | -11.3935 | -43.3705 | 2026-10-01 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| cb4f3a37-b9b4-305a-92a9-77bcd89f0473 | -11.2438 | -44.2626 | 2026-10-01 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 278.8 |
| b6b73d8a-e375-3dfa-ba71-385844b96590 | -11.2434 | -44.286 | 2026-10-01 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 44ed0d91-1efe-308a-8e60-a4be3c7fad12 | -6.3215 | -51.1274 | 2026-10-01 17:50:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 29012fbd-f8bc-32b8-a308-cf73fb3c6ac3 | -12.5135 | -43.0943 | 2026-10-01 17:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 182.5 |
| 6df8a5e0-2b74-3c60-aeab-de267269a91b | -5.9151 | -53.4965 | 2026-10-01 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 305.9 |
| 4fc2b920-72de-3976-904f-762dc92a9595 | -14.4707 | -40.7074 | 2026-10-01 18:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 317.3 |
| 748e3670-c35b-3948-aa8e-afd2a02c68ad | -11.3935 | -43.3705 | 2026-10-01 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 6ab2cac8-096a-3e38-b45b-784d7bc4a288 | -11.7182 | -43.4386 | 2026-10-01 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.7 |
| 8229454d-e5a5-3313-8430-8281e87947b5 | -2.974 | -51.0247 | 2026-10-01 18:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 129e532d-185a-3cb7-a5fa-bb40d58cb59d | -6.3215 | -51.1274 | 2026-10-01 18:00:00 | GOES-19 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| acf193a3-de62-308b-984d-08113aa20aa0 | -3.1061 | -50.2686 | 2026-10-01 18:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2cb0f4a7-cefb-3ee3-9aa9-d2e49542c454 | -11.2945 | -43.551 | 2026-10-01 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 01018243-61e3-3df4-957a-3d5d5f008937 | -5.9151 | -53.4965 | 2026-10-01 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 236.9 |
| 58b129dd-a730-3fc5-a891-30d0a3412681 | -11.6784 | -43.5158 | 2026-10-01 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e7256444-dc60-38f5-b127-a81bec4c6435 | -11.3931 | -43.3942 | 2026-10-01 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 068a6530-fb26-36dc-9abe-df366889415f | -13.3292 | -43.8335 | 2026-10-01 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 90bcaf42-ce61-3310-81ca-2f0241b7f265 | -11.6011 | -43.5515 | 2026-10-01 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 87bd0210-ae4b-3106-a271-43c880a7fa9d | -3.1061 | -50.2686 | 2026-10-01 18:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |


[Clique aqui para ver as próximas entradas](README114.md)
