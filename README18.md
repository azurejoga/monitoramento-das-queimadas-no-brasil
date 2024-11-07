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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b3885ef-6823-3db4-8e90-5f17bd1f5bec | -2.6094 | -51.2939 | 2024-11-07 01:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a727b7e9-0275-302e-9e9c-aacc59bc450e | -3.4564 | -50.3832 | 2024-11-07 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 0821df0a-1342-3b3f-8ff2-67372534a57e | -4.5033 | -42.862 | 2024-11-07 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 1658446f-d36c-3a2f-bf97-2dde94edaafb | -5.9975 | -45.3607 | 2024-11-07 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 354e56c3-dcc5-3f47-ab31-a95a69f0639c | -2.4319 | -53.6584 | 2024-11-07 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| df22066d-7b45-3d88-9851-ae268cf36bed | -2.82 | -52.9613 | 2024-11-07 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 66f9cfa3-e24a-3a19-a266-6d03a01bb78c | -5.1395 | -47.7008 | 2024-11-07 01:20:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 369499d7-7245-3e3a-b769-19df9f184a51 | -1.2014 | -53.8983 | 2024-11-07 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5711bebe-c43f-32bc-90b3-a32b7a2ddb7f | -1.1831 | -53.8985 | 2024-11-07 01:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 164abbb9-632a-3e7a-bfdc-936b8f0e822f | -5.0154 | -46.8531 | 2024-11-07 01:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| adfd5707-aa29-340e-a4ac-263f48563cf9 | -6.3323 | -35.1071 | 2024-11-07 01:20:00 | GOES-16 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 30f23af2-1c76-37fd-971b-03b4e8c79902 | -2.82 | -52.9409 | 2024-11-07 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| c0fadd5f-bb0b-3c52-81eb-0dd5f6e65fcd | -4.522 | -42.8608 | 2024-11-07 01:20:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e4154f60-3669-3cea-b6e4-9e72640f6baf | -5.1581 | -47.6997 | 2024-11-07 01:20:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9c0681bf-701d-376d-a349-1e834cfe83ff | -2.6044 | -51.3043 | 2024-11-07 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8b974635-fe10-38b0-9e1f-7738d903de63 | -3.967 | -48.15 | 2024-11-07 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 25a08567-1ea1-3944-a49b-a3b505aa061b | -2.8537 | -48.6642 | 2024-11-07 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 4780e087-bc6a-384f-9859-41cb8a6a734a | -3.1617 | -50.2038 | 2024-11-07 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f5e07f2c-474e-317e-a7fc-3b7f35eb1df1 | -5.034 | -46.8521 | 2024-11-07 01:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 188.5 |
| bdb4f154-8b85-3401-830f-db7cc6cde2eb | -5.0155 | -46.8311 | 2024-11-07 01:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d65cca9c-1d32-3a6a-9289-fe27c56ccd01 | -5.9788 | -45.3621 | 2024-11-07 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| d269d6a2-0100-35f3-af53-42364315c70e | -3.0207 | -53.443 | 2024-11-07 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| aeab1ab3-2317-361c-86da-dec55ab8cf1b | -2.8536 | -48.6856 | 2024-11-07 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6eb03b4a-5879-3216-a7b0-f9c97a13d66f | -5.0342 | -46.83 | 2024-11-07 01:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 0ce9ba39-4298-308a-8627-d7b84ae641b2 | -3.9669 | -48.1716 | 2024-11-07 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a27a569d-5ae9-30f7-9399-3e64bf63b18f | -1.7148 | -45.786 | 2024-11-07 01:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 44bb3240-6077-3eaf-b569-36125c3ab480 | -3.0396 | -53.2805 | 2024-11-07 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ecf7780d-a3ff-3910-a441-0f6db45ece1e | -2.6229 | -51.2831 | 2024-11-07 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f351cc27-a37e-3540-b6e7-18b805a297e8 | -3.0397 | -53.2603 | 2024-11-07 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 26115ecd-9d60-3826-8040-973cbaad64a4 | -5.0526 | -46.851 | 2024-11-07 01:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 0e27cc43-417c-33ab-897c-6708cf774cab | -2.6228 | -51.3038 | 2024-11-07 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| b08fddd1-987a-36cb-9130-220453274182 | -2.924 | -49.5994 | 2024-11-07 01:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ad2f453d-5a76-38fc-b752-8a00cd40d371 | -2.8688 | -49.5375 | 2024-11-07 01:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5b5c895f-21dc-3c93-8a63-28dcebafd324 | -5.9786 | -45.3847 | 2024-11-07 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8c7c2749-cf93-38bb-a1d3-625489a1bca0 | -1.1466 | -53.7177 | 2024-11-07 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 81f85355-6a66-3717-a172-7dce9592d45c | -4.5218 | -42.8843 | 2024-11-07 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2eadec8c-3af1-3d9e-a8f8-1a8682859d11 | -4.5031 | -42.8854 | 2024-11-07 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a36a7b72-2748-3e65-a33d-bf3a9dccc649 | -6.3323 | -35.1071 | 2024-11-07 01:30:00 | GOES-16 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 222.4 |
| 99206b89-7c36-3274-aa23-db04a8912abc | -5.0526 | -46.851 | 2024-11-07 01:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3db89b3b-599e-3651-832b-a90ba1368039 | -6.3326 | -35.0796 | 2024-11-07 01:30:00 | GOES-16 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 129.6 |
| 8bdde191-5f75-3920-88ea-b45b897a749d | -2.6229 | -51.2831 | 2024-11-07 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| fed3e4fd-e4a3-3277-9a15-99c15631570a | -5.9788 | -45.3621 | 2024-11-07 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 7a762c0a-043c-33d3-abf0-f9dff78becd3 | -5.9975 | -45.3607 | 2024-11-07 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0b62b768-1012-3169-9848-d7232c1fc636 | -3.967 | -48.15 | 2024-11-07 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9a1fab02-1e3d-30bf-84bc-7cc77dff585e | -3.4564 | -50.3832 | 2024-11-07 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8176a376-bf57-3a91-a353-497b328dca2b | -3.2346 | -50.4533 | 2024-11-07 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| fce3be6a-c301-31ff-977a-eb44a03f1329 | -3.0396 | -53.2805 | 2024-11-07 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 57916f6c-2bbb-3f62-a708-bdae2b4d9e14 | -5.979 | -45.3395 | 2024-11-07 01:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 0affce11-31e5-3e1e-9349-5d4404ac0461 | -5.034 | -46.8521 | 2024-11-07 01:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 144.5 |
| fc8fab84-7aed-3f5d-b82b-84f51a50177e | -5.1395 | -47.7008 | 2024-11-07 01:30:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e60371a4-303e-317c-849e-878efc94c66b | -5.0155 | -46.8311 | 2024-11-07 01:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6034b223-0a87-3014-8d20-c6728b1111e8 | -2.8536 | -48.6856 | 2024-11-07 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6e51e0c4-796d-33a5-8136-9d15c9ea8d64 | -1.1831 | -53.8985 | 2024-11-07 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a14f059b-e386-3f89-9686-7989bf8c5928 | -2.8537 | -48.6642 | 2024-11-07 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| f02bb740-e4b2-37b9-b983-bb52d16cd11d | -1.2014 | -53.8983 | 2024-11-07 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| c8d554c0-9ce9-32d7-82d9-b4cdd99645c2 | -4.5033 | -42.862 | 2024-11-07 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2b999af7-e488-383a-9930-f42aad8d5c83 | -3.0397 | -53.2603 | 2024-11-07 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 99d9e779-2dab-3691-96ba-5e73869aecde | -3.1617 | -50.2038 | 2024-11-07 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f29d7ace-a06f-3acf-ae3f-ee15ddc88ddc | -5.0154 | -46.8531 | 2024-11-07 01:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 738de975-58d5-3861-bbca-480319c134bb | -2.8688 | -49.5375 | 2024-11-07 01:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 87c82cd9-a4b7-35f8-b9ba-975fd876ab61 | -2.6044 | -51.3043 | 2024-11-07 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c3f843c3-8204-39a9-b270-6951413d96ae | -2.82 | -52.9613 | 2024-11-07 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 1d90a7c3-87e1-329e-aa4a-9ebab4d437c9 | -2.5009 | -49.1228 | 2024-11-07 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 386c4a24-84c0-3f49-8f85-406368ab4eb5 | -3.0207 | -53.443 | 2024-11-07 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| dc0bbdc0-3349-3919-ad3d-8ea88b03ff8a | -4.522 | -42.8608 | 2024-11-07 01:30:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6045a6f4-161f-3c56-9da3-e1485f626bad | -5.1581 | -47.6997 | 2024-11-07 01:30:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d5fd6639-9ff5-3b58-9686-5c659bdb2bc8 | -3.7218 | -48.9979 | 2024-11-07 01:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| da2eabb4-0dda-3aa9-9c1e-2ff432f1af08 | -6.3513 | -35.1048 | 2024-11-07 01:30:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 16571fee-3f98-31f6-bb77-3263214c599d | -3.7033 | -48.9986 | 2024-11-07 01:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 04c73817-8b48-3a80-966c-7971de4bfc4c | -2.6228 | -51.3038 | 2024-11-07 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 3958a07b-9ae3-3f2e-a014-b3559a0baa8e | -5.0342 | -46.83 | 2024-11-07 01:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 9ca38e8c-83f4-3d2f-91f3-813fb8e27e0a | -2.8352 | -48.6648 | 2024-11-07 01:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 63d470be-7fe1-38be-be6a-b8040181ca8d | -4.5218 | -42.8843 | 2024-11-07 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| a42796d1-d482-3a04-96e6-674579300cdb | -2.82 | -52.9409 | 2024-11-07 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 74e89e1e-10c6-3205-a526-24ede6c06274 | -3.9669 | -48.1716 | 2024-11-07 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 34a825ec-0ac0-3003-925d-6e105aa67522 | -1.1466 | -53.7177 | 2024-11-07 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1cb9326d-1156-34d5-9113-a5cd8a1ed346 | -6.3517 | -35.0774 | 2024-11-07 01:30:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| e0f6fb27-c72d-31b9-a762-571ad62c0b68 | -2.924 | -49.5994 | 2024-11-07 01:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 00a28023-1fe9-3465-9b95-cd0ea661b84a | -2.8688 | -49.5587 | 2024-11-07 01:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 52723d09-0fa1-3e1d-a5d2-77fc4de1df8d | -3.0396 | -53.2805 | 2024-11-07 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 563deeb5-9fb3-3755-9759-95071dd754ff | -17.7055 | -57.5186 | 2024-11-07 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| d5de83fd-54f4-3270-8282-4f677831d804 | -2.8536 | -48.6856 | 2024-11-07 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f46e9d58-729c-3a40-93a3-0d37e451f2a0 | -2.82 | -52.9409 | 2024-11-07 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 1aca841e-e632-371f-9027-c9e4024602d9 | -4.5218 | -42.8843 | 2024-11-07 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 25163c6d-575f-3b1f-b554-faef29113234 | -5.0342 | -46.83 | 2024-11-07 01:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6e5c770d-0032-3e3c-a43d-a1c2fb149382 | -3.0207 | -53.443 | 2024-11-07 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| b6d170f3-29ee-3be0-8cb4-c1e3877d5930 | -4.5033 | -42.862 | 2024-11-07 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 94956ca1-bc5a-39a4-ac72-99fcb84837aa | -6.3323 | -35.1071 | 2024-11-07 01:40:00 | GOES-16 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| a2a7f5f7-efd5-3fbd-a6d2-961a1ff86382 | -1.1466 | -53.7177 | 2024-11-07 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2d72ee2c-5878-3627-a6ff-92e682e84bb5 | -3.0397 | -53.2603 | 2024-11-07 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b5a90338-c1e4-3b11-843b-583740ddbf8f | -2.6044 | -51.3043 | 2024-11-07 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 76f54d81-9d09-372c-b67d-f26bcb7c2ded | -6.3326 | -35.0796 | 2024-11-07 01:40:00 | GOES-16 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| d956a779-2b75-395a-9df2-3e55c4aa9f00 | -5.034 | -46.8521 | 2024-11-07 01:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3a8a19f4-ed1e-3acb-bf35-3cb2be72f248 | -2.8351 | -48.6862 | 2024-11-07 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c917bea3-47ac-3daa-9f5a-2e7b811e7a9e | -3.967 | -48.15 | 2024-11-07 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 26ebfb9a-b374-32bf-baf8-427d00cad0d8 | -5.9788 | -45.3621 | 2024-11-07 01:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 1f4c33e3-0184-3a5f-a480-67eed7feb888 | -3.7218 | -48.9979 | 2024-11-07 01:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 87d9cdd4-21a2-3190-97c2-deee326d8357 | -2.8352 | -48.6648 | 2024-11-07 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 196e8af1-ecf9-3c37-83a7-9b7ee1911c18 | -2.8537 | -48.6642 | 2024-11-07 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 57c23ca6-dbb0-3cdc-9dc0-08c884104adb | -2.5009 | -49.1228 | 2024-11-07 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |


[Clique aqui para ver as próximas entradas](README19.md)
