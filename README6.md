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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69b27a69-d8da-360f-9213-b0b1b0f803d2 | -3.0108 | -48.5093 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5957c75a-10fe-3249-828e-2f134c473622 | -3.5575 | -41.872601 | 2024-11-27 00:21:00 | METOP-C | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 259d6022-0bf8-3d81-a117-2c761f163460 | -2.5044 | -47.317001 | 2024-11-27 00:21:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc37e24-f7d8-3e31-8aa4-47da29a698eb | -4.6712 | -44.9725 | 2024-11-27 00:21:00 | METOP-C | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5517f32c-f297-31eb-967e-726d254c1304 | -5.6704 | -46.851299 | 2024-11-27 00:21:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a97f271-a8ab-31a4-9929-408ef3d21518 | -3.9402 | -48.074501 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca86e173-c4e8-3da5-917e-8780ab3a0a5d | -2.856 | -45.3755 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa7e3f12-cd0c-3b5e-ac0f-ae1b27afb2b0 | -3.7928 | -44.330101 | 2024-11-27 00:21:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5854ffc-5a2d-3162-8fb8-2ecbe3c06d20 | -3.3485 | -50.104099 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b77a0520-4698-3ce0-8083-8e55a305baff | 1.3994 | -50.6166 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 74f8c33e-d877-3759-b4f2-b6bb2f0fac51 | -3.9381 | -48.064999 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9526e848-2154-3ad0-bdec-21a640e35ffe | -4.8242 | -40.752899 | 2024-11-27 00:21:00 | METOP-C | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5e964e5a-ec8f-32d3-ac32-eb1d56a36afd | -5.8825 | -43.410198 | 2024-11-27 00:21:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5e0f60a-70a3-33d1-88ba-b10e705691d7 | -3.0722 | -53.2575 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c78930cd-a1d7-3f4f-a36f-c59857ba0635 | -3.9115 | -46.895199 | 2024-11-27 00:21:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc6b322-0dd1-3561-bf0d-76a970b6612a | -3.2566 | -41.776402 | 2024-11-27 00:21:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b68b037b-46ae-3918-b70b-aa79785a4bf2 | -6.0672 | -39.411598 | 2024-11-27 00:21:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6a9e1b15-8da0-32e8-b2a1-6c0f6072db82 | -1.6342 | -52.4384 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d14daa5-acde-3169-81f2-eb492b062130 | -3.88 | -50.6063 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4318e2f-397a-3cf1-be0d-4b4948ba1cc0 | -3.6919 | -50.175098 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42e1dae1-0236-3ccb-b1c9-410a9a08e58e | -3.0819 | -53.255402 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a027665-0eef-3fb9-a6da-0221b61916d4 | -4.6238 | -43.814301 | 2024-11-27 00:21:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d88ff88-4222-3ce6-92a0-6e7cea190311 | -7.1231 | -40.255299 | 2024-11-27 00:21:00 | METOP-C | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d9033451-132d-325b-a0ce-516e44bea0ca | -2.8197 | -45.487499 | 2024-11-27 00:21:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4304416e-1102-3780-bc69-942bead57ed9 | -2.8762 | -45.238201 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccd3c9c-083a-3a29-88f0-11fe07e0a808 | -3.9906 | -47.658001 | 2024-11-27 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f13125fd-1683-365a-9743-017b31594335 | -5.5555 | -43.153301 | 2024-11-27 00:21:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 123194e3-22fa-3cd8-8ddd-de43e2094425 | -5.5915 | -43.942799 | 2024-11-27 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c6a0e06-b36b-3298-82e0-3d73b7abab1d | -3.7912 | -44.3232 | 2024-11-27 00:21:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf5d0f1a-3087-3d04-a866-e7bd38314570 | -3.936 | -48.055599 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dba9ca6-077b-3819-83db-cbe7bb14433b | -3.8739 | -50.578899 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3caedf8c-0396-3356-8ce2-66250065ae8f | -3.2575 | -50.612701 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1ff8a0a-fdeb-3cf5-a403-ad616d4cbfbb | -9.3823 | -35.923698 | 2024-11-27 00:21:00 | METOP-C | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33cb87c6-4253-32fb-a8ba-26fc6e685aa6 | -4.185 | -48.663502 | 2024-11-27 00:21:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6317d654-f538-37c8-aa8b-5e268590eb40 | -3.9951 | -45.535301 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b51c8cc2-07ce-3cb2-8374-36ccb2bc38a8 | -2.6608 | -45.649799 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afbb4ae2-a373-3b3f-a5b3-e1196e2ddfb7 | -9.3789 | -35.910301 | 2024-11-27 00:21:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bb1efc0-d220-3598-9d83-64f39818e1fb | -2.7674 | -54.1227 | 2024-11-27 00:21:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a897eca0-554e-32ed-90f2-03a43bd05f3a | -1.6109 | -52.425701 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa07c6d-2f07-3f9c-949e-82002bd2f944 | -3.2485 | -43.036499 | 2024-11-27 00:21:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d720644-36cc-3453-8e62-61b428fd9d21 | -3.9488 | -46.649899 | 2024-11-27 00:21:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd224414-4dc5-3fb8-b4a3-ecb83e5dd4ec | -2.2953 | -46.126099 | 2024-11-27 00:21:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2eb454-4169-3eba-acb1-18a80bc26d77 | -3.2545 | -50.5993 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a982a93e-6387-38e2-8bb7-c7d5d37c5abd | -3.947 | -46.641899 | 2024-11-27 00:21:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6ee114e-1200-3989-9dbd-ea1bd97dddb2 | -3.7837 | -46.602901 | 2024-11-27 00:21:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b4ce738-87c4-3574-b742-0923ba30f5b7 | -3.4846 | -50.300701 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cecd2bd0-6453-3fe4-b22f-436a217b947f | -3.4961 | -52.141499 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31693e0e-f37d-3541-abeb-f4089809dae5 | -2.9767 | -45.452702 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3730c8d2-7d3c-3a0a-adba-aa9ab4d0f4b3 | -3.1997 | -50.308701 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab2d2a68-b5cc-3458-aa66-3b5bc11da9d1 | -5.5931 | -43.949699 | 2024-11-27 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 700c9d0d-c166-31ef-851e-98ca53463f6a | -3.0226 | -48.5168 | 2024-11-27 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3247de07-eea5-3392-b0db-012ea7beaa03 | -3.6827 | -47.659801 | 2024-11-27 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 817ad365-4436-30b9-b3ee-5c885d189bbb | -1.6497 | -46.91 | 2024-11-27 00:21:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8090a949-e061-30ad-8262-b45cb17a97d0 | -3.823 | -45.9119 | 2024-11-27 00:21:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4f903c6-0f0a-30ab-8b69-60e6fe082980 | -5.7235 | -46.2603 | 2024-11-27 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c1fac0e-a099-3954-8de0-ebf87b146371 | -2.7964 | -54.116402 | 2024-11-27 00:21:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c487f842-78f3-3e05-b146-b594d78ff976 | -3.2056 | -44.152901 | 2024-11-27 00:21:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d19ce903-ec0e-30b7-a5f9-63242b767a76 | -3.1175 | -48.526798 | 2024-11-27 00:21:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3198ea28-0a1a-382f-a141-27c0daa38623 | 1.3896 | -50.614399 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5f59693e-ffc5-35f3-90f1-ad2d974a6fe1 | -3.073 | -48.010799 | 2024-11-27 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 077a47ae-4f3a-3a0f-84bc-7dd097eecb58 | -7.6712 | -42.9785 | 2024-11-27 00:21:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 003dbbb8-0094-369b-b467-bce8a46afb8f | -1.9946 | -48.651199 | 2024-11-27 00:21:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c947bae7-2a08-317d-9b29-a351d321a79e | -1.6381 | -52.455399 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53f0df8a-dad1-3312-9894-f5187a28ec87 | -2.9056 | -48.635201 | 2024-11-27 00:21:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eeee7be-adff-3013-b38c-8a9ac815338e | -2.6739 | -45.6619 | 2024-11-27 00:21:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c634cde-4c51-3a53-a921-7ec18fa48acf | -3.0535 | -53.218899 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8182de24-1ba5-3bfe-a29d-0542db4909fe | -3.8337 | -40.443802 | 2024-11-27 00:21:00 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 138a9b90-b024-353e-bcfa-30a827bdf47e | -5.0093 | -43.606098 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d614def0-bb00-3d9c-80bb-88f626e39e7e | -5.6235 | -46.640999 | 2024-11-27 00:21:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bb81a17-5af8-38cf-9ef7-2b5adf30da1f | -3.0625 | -53.259602 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7587a5e3-f104-3bfa-80a5-7ce18b5a3029 | -3.2496 | -45.429298 | 2024-11-27 00:21:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2e6d506-5c1e-3cc8-8ee9-2b0c7b834cf0 | -4.1144 | -43.8424 | 2024-11-27 00:21:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2348359f-e4da-346e-ac2c-35337406919a | -4.6253 | -43.821201 | 2024-11-27 00:21:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14d43b35-dee0-3aa9-909f-6c2e6281350e | -4.515 | -46.788399 | 2024-11-27 00:21:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f46eaa17-3fa0-347b-8465-2422c13de997 | -3.4231 | -50.300499 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3ab9c8-5bc4-35cb-8e0e-1418256a3acc | 1.3851 | -50.589401 | 2024-11-27 00:21:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d86c497a-8572-3f4e-b4a8-79e85229f69a | -2.8068 | -46.8349 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e33e726b-ee50-3828-abea-d16dab1ceb43 | -5.2322 | -40.599998 | 2024-11-27 00:21:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 18ca0328-fbe8-3cd0-beae-a884f7f2d671 | -4.1912 | -46.447102 | 2024-11-27 00:21:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20c90996-b14d-312c-a17c-14f898664fd1 | -3.0677 | -53.237099 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8d4f284-e433-3be7-8bab-609d1c7241e9 | -5.8964 | -42.9757 | 2024-11-27 00:21:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3666f373-b5df-31ff-9690-a8f7bc25f311 | -1.8688 | -50.586102 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47769a4a-3031-3e7e-b8f2-6625bfa54a10 | -5.3 | -43.0741 | 2024-11-27 00:21:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c379692b-2a79-331c-8fe9-4191bce1edad | -3.9445 | -48.093399 | 2024-11-27 00:21:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6060293c-929e-3b8f-b8b1-96e834cd7b9a | -3.058 | -53.239201 | 2024-11-27 00:21:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac2e4d7e-d2d6-361c-9118-db8c2a30c910 | -1.6303 | -52.421398 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb76dcf8-ede9-335e-895b-27d103ed3467 | -4.1883 | -47.211102 | 2024-11-27 00:21:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcdd20a1-dbd2-3339-99a6-60d1179bf836 | -3.2041 | -44.146099 | 2024-11-27 00:21:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| afdcff9c-a6b7-3569-8900-9230be6e4a4c | -1.4884 | -46.068298 | 2024-11-27 00:21:00 | METOP-C | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e165c693-6ed4-3a3f-acdb-3f5c71c4eda8 | -2.8061 | -54.1143 | 2024-11-27 00:21:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a019175-e03f-30ea-b78e-26d8867c4d46 | -1.64 | -52.4193 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ccc08ce-a762-3f6c-89cd-3e8bb047b33e | -2.5136 | -46.405701 | 2024-11-27 00:21:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c4f13ae-995e-3abd-87a3-9d3b1f603bbb | -2.818 | -45.4804 | 2024-11-27 00:21:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72051f8c-7d41-3912-aa06-4c4fd2d4a817 | -2.8521 | -45.177502 | 2024-11-27 00:21:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21c0a030-9875-3a66-ad6b-e26ea814ab7f | -4.384 | -44.118999 | 2024-11-27 00:21:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c325f92-fb4a-396c-b973-4e0fa321956b | -2.7913 | -54.093201 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c07ef86-9a37-3767-89ff-3e84256a41bc | -3.8672 | -50.5947 | 2024-11-27 00:21:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5680085f-ac31-3e35-a5a5-13ee98893c80 | -3.1968 | -50.295898 | 2024-11-27 00:21:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9abcaf2a-2d65-36d0-b6e4-e59126fcfbc4 | -1.3734 | -46.737701 | 2024-11-27 00:21:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d40558-03ce-31b1-b8bb-70c68616741d | -1.6127 | -52.478901 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
