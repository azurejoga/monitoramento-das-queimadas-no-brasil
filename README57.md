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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a582d31-7142-30c9-905d-c760d4056992 | -9.9779 | -44.7821 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 2e6e9241-7b32-318f-91f9-f81ddd127790 | -8.3049 | -43.9377 | 2025-11-17 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 0457dd39-be2f-35ba-9046-21249ab60c9c | -8.3046 | -43.961 | 2025-11-17 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 6a1a7d6f-5783-3694-9c98-993fad1a3fda | -9.9758 | -44.9204 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 064b5e47-626b-3b05-a5eb-e7e5240df53b | -9.9775 | -44.8052 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 86a995bc-45e7-379b-ab9e-917581d7a784 | -3.3552 | -44.4255 | 2025-11-17 14:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 91c4c679-3fb2-3cc7-abc4-b1961ceefb8f | -3.7652 | -47.7468 | 2025-11-17 14:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 0fffc813-1474-329a-8eb0-1530c58ed74a | -11.6755 | -44.7342 | 2025-11-17 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 358.9 |
| b737255a-fd78-3bfa-86d5-e85ed700cf3e | -2.4015 | -45.7243 | 2025-11-17 14:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 5b733d24-b466-378f-bdd2-e8df51e1bf51 | -7.491 | -45.8693 | 2025-11-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d85270f2-964d-322b-b011-a587ecda1a7f | -9.0211 | -45.4672 | 2025-11-17 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| c2ff2946-6ce6-36b6-b22e-1055937ea70f | -11.6947 | -44.7314 | 2025-11-17 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 484.8 |
| 307ab0f6-0197-3426-8876-b2ebbd58dc86 | -10.3535 | -48.9174 | 2025-11-17 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 1882e9a4-367e-3f69-b603-e286af280537 | -1.3932 | -49.0387 | 2025-11-17 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 656e4c94-ac1c-385c-8b9a-c144495c3312 | -2.4201 | -45.7015 | 2025-11-17 14:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d26aa4a0-3cdd-3d71-8fca-0e1b9289c9a9 | -9.9754 | -44.9435 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| f8778ed4-194b-31fd-9ecd-a708429598dc | -8.2827 | -44.1951 | 2025-11-17 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 84af7c80-dab1-3b3d-b485-e3fc9c438266 | -1.3961 | -47.5103 | 2025-11-17 14:20:00 | GOES-19 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 2c3db6e0-fd30-36d8-8956-581bb3d50023 | -9.0825 | -51.1566 | 2025-11-17 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6d206551-0f09-3cb8-844c-ba94a679621a | -10.7889 | -47.6392 | 2025-11-17 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f5a71be8-0ba1-3725-98b2-e831ddc649d0 | -10.6708 | -44.2739 | 2025-11-17 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ab687b9f-7d34-372e-9176-4a66819c0ea0 | -3.8229 | -44.0833 | 2025-11-17 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 865d45eb-b372-358d-9dd7-8251990b0a19 | -8.3016 | -44.1931 | 2025-11-17 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 0fae4cf1-4223-3450-94a9-36f71d628a90 | -3.9895 | -44.2813 | 2025-11-17 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 20735d69-e93e-34ba-bb24-ea9963544a60 | -10.8456 | -44.0862 | 2025-11-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 224d4f63-38df-3c33-8396-a6b10f4449ea | -10.0917 | -44.7907 | 2025-11-17 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 55b3ca4d-7c4e-3cc7-976c-fe293cf458ec | -7.7169 | -45.8262 | 2025-11-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 71ed895c-f467-3ddf-82ba-38cd8411cf87 | -10.1111 | -44.7652 | 2025-11-17 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 09d9c458-0e5d-3b02-98f9-c5ad9cd49ec4 | -10.3939 | -44.9129 | 2025-11-17 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 147.6 |
| ccaa9dde-c178-3dc4-b5e9-79ed04f0175b | -12.8525 | -46.4847 | 2025-11-17 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 0d70d299-3845-3140-88c4-7300413cbce7 | -3.4654 | -44.7168 | 2025-11-17 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| d5eaee03-cd4c-32fe-873d-c15760d23ca3 | -3.3602 | -43.4821 | 2025-11-17 14:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5b0b3379-6956-3e4a-a52b-133dace7254f | -3.4468 | -44.7176 | 2025-11-17 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4f9d2837-8552-315f-843d-f4a34b7645d0 | -3.6021 | -43.5868 | 2025-11-17 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 05caabf4-dfa6-3ade-815c-9c0952b5a35e | -8.1212 | -43.5382 | 2025-11-17 14:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 8ad39cd0-295d-390c-afda-98af4c09e430 | -11.7996 | -45.2935 | 2025-11-17 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| aeb07733-04c7-357e-b1ee-c75ddc361be9 | -11.9784 | -44.9439 | 2025-11-17 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 223.3 |
| a0e8a963-0ff9-3437-a2c3-616ef6dd0eda | -5.0588 | -37.0843 | 2025-11-17 14:20:00 | GOES-19 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 109.3 |
| f757bc36-f357-3a3d-9bde-0909a7955ae4 | -9.6232 | -44.3876 | 2025-11-17 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 88d6bf93-44a1-3b57-ab34-d68eb19cd387 | -3.4036 | -42.3567 | 2025-11-17 14:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 686cbe54-63c9-3eca-a5a4-b2a145bcc902 | -3.6701 | -44.7303 | 2025-11-17 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| b06ba9c5-a0ae-3e0c-9b35-d3e6265fa510 | -3.7838 | -47.746 | 2025-11-17 14:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 8ec9aeb4-185d-3236-8450-94068f3f8c64 | -3.4281 | -44.7412 | 2025-11-17 14:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 862d6118-02a9-342c-baf8-bd10903b91b2 | -10.3936 | -44.936 | 2025-11-17 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a1b6eb5f-256d-3f9e-bcec-2e72e7e3d109 | -8.3019 | -44.1699 | 2025-11-17 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 0574dbe4-dfe7-3733-abc1-e19a571bd9c9 | -3.3601 | -43.5053 | 2025-11-17 14:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a78f5510-044a-3915-881e-b434c02ccb50 | -3.7292 | -44.1797 | 2025-11-17 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 49bde59a-7910-3ae9-a53b-da4159f08cc6 | -9.9972 | -44.7566 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4e8b2c68-9b92-35b1-9eb4-7f9262370fd3 | -7.7135 | -42.9478 | 2025-11-17 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 69fd2dc8-71b2-34ee-8535-b0624d7300cf | -9.4645 | -44.868 | 2025-11-17 14:20:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| de939cd9-ea6e-3b0a-9669-036f86155b78 | -3.2116 | -43.3726 | 2025-11-17 14:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 2fad637e-0c9c-3168-aaeb-9d04ee4992b3 | -12.6672 | -47.167 | 2025-11-17 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cc62a1fe-68f5-31b4-9c51-dd4f828dc3cb | -12.7189 | -45.4074 | 2025-11-17 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| fd702d94-9836-3635-a614-bd6fd9af121e | -11.4136 | -43.32 | 2025-11-17 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 65b909d7-86ae-3280-924d-f6e0b44864ed | -4.54 | -48.4689 | 2025-11-17 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6ffcf0de-2f1d-31d7-8b86-bf7f0c44f1af | -2.5053 | -47.812 | 2025-11-17 14:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 924d4d3c-cf07-3005-9b31-07127de9450d | -9.6236 | -44.3644 | 2025-11-17 14:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 0e34890b-8943-3615-9726-db674691470c | -3.3602 | -43.4821 | 2025-11-17 14:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4a08849b-202f-3e0f-a122-bd4a01242aff | -5.3444 | -43.0167 | 2025-11-17 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 65.8 |
| aa0c45f2-110e-37fd-a89d-fe674b2cff93 | -3.6701 | -44.7303 | 2025-11-17 14:30:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 5de740a7-15e5-3782-832e-24c88f019064 | -2.4201 | -45.7015 | 2025-11-17 14:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 384dca9b-07fc-31a2-b781-a2de9e09289f | -10.1111 | -44.7652 | 2025-11-17 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 05dd6196-071f-3547-be96-09ab3f524475 | -4.2673 | -44.5866 | 2025-11-17 14:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a804e98c-db8b-3404-b8fe-b50cf6c00dfb | -11.6947 | -44.7314 | 2025-11-17 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 490.1 |
| 132e2c72-31ae-3e4c-94a4-a989340e9d50 | -3.9897 | -44.2584 | 2025-11-17 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 20a16328-553a-3e1d-ba52-cff147ee05c2 | -11.6755 | -44.7342 | 2025-11-17 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 381.4 |
| 19d40a95-7b58-3f07-b399-7e8098abd216 | -10.3037 | -44.6017 | 2025-11-17 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1e56bafb-9a63-3c40-8472-08a7a9879bf7 | -9.0825 | -51.1566 | 2025-11-17 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b947d197-0884-3281-8c4e-a4999542b572 | -9.9567 | -44.9228 | 2025-11-17 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5e4966a5-12e2-3cbc-8994-87c258ff1c86 | -1.4116 | -49.0384 | 2025-11-17 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 44b62e47-b36c-3c1d-90ed-1ebe17fbca11 | -9.0211 | -45.4672 | 2025-11-17 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 404.3 |
| e52fcfcb-dd86-3a5b-9387-e76da39235aa | -12.88 | -46.0478 | 2025-11-17 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1c4b1294-fbca-35f3-ab34-f3ac26753317 | -0.8399 | -48.6608 | 2025-11-17 14:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8fe7a9d0-8fb5-3b2b-950c-58084eee7ddf | -10.1107 | -44.7883 | 2025-11-17 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e29ecc84-cea5-32f6-a90e-ff843e0200e2 | -9.9972 | -44.7566 | 2025-11-17 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| eb2d4d4d-17de-37f6-88e2-9b21fea34d7a | -8.5129 | -45.3629 | 2025-11-17 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d622db80-ce0e-33be-987c-acbf5999c241 | -3.6021 | -43.5868 | 2025-11-17 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6184d5f0-e2b8-3a6b-b55b-ead80491e1c3 | -11.792 | -44.6472 | 2025-11-17 14:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| af5cce4e-da51-3a4a-b96e-7e2ebcfa6646 | -3.9904 | -47.2791 | 2025-11-17 14:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c966a463-f108-3ccc-bef5-82568ea87d93 | -4.5585 | -48.4895 | 2025-11-17 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| dd6bad1f-b53f-3d48-9e36-83a1bb14e45b | -3.3842 | -46.0472 | 2025-11-17 14:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a65f9edb-2d91-3090-bb6e-9efca8f3dcaa | -3.5834 | -43.5877 | 2025-11-17 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b4992d12-0bf2-3a49-bc64-098950f1de39 | -3.2159 | -50.4958 | 2025-11-17 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ccb3eba1-41a5-3f69-b443-b02920ece7fc | -2.4015 | -45.7243 | 2025-11-17 14:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 5b26e863-b167-3714-8505-4006a32a2ded | -11.676 | -44.711 | 2025-11-17 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 375.1 |
| cffb34ed-b987-389e-8ffb-093b5be1d96c | -9.4645 | -44.868 | 2025-11-17 14:30:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 1475fe86-64cf-32da-802d-6ea0fefa83c5 | -10.3749 | -44.9154 | 2025-11-17 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| dd6e0228-c608-3956-84d2-cea6d33d805a | -13.2938 | -43.6737 | 2025-11-17 14:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 7d7096a0-e42f-38f9-910f-a7ba7f6ad95e | -9.9754 | -44.9435 | 2025-11-17 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3978a3fa-48f0-3dd4-80c8-c4f88606792b | -3.3841 | -46.0694 | 2025-11-17 14:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 62008ee0-bc2c-3911-8fee-3d3a9dfcd031 | -9.9775 | -44.8052 | 2025-11-17 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| f3ef6e83-c83c-39ab-a20e-7e64760d2f94 | -11.152 | -44.0423 | 2025-11-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 35855d39-d613-33e2-92a5-1fd28fbd2a83 | -11.9784 | -44.9439 | 2025-11-17 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| d9413816-ec27-3446-a7a9-f4636a97e5e2 | -7.442 | -45.2184 | 2025-11-17 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 768c08e3-b0f5-36c8-a235-cbc8cc54e7d5 | -8.5607 | -46.0588 | 2025-11-17 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 395bb3bb-b937-3838-9a49-b05eac1c2eb7 | -9.1387 | -45.1579 | 2025-11-17 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 5d7b829c-79b2-3663-b49f-512033e7a80f | -4.5586 | -48.468 | 2025-11-17 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 0124eb6c-087b-3edd-b818-a1d35ab14271 | -3.7293 | -44.1568 | 2025-11-17 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 8b38e8df-a41a-3f46-a5ad-be22cc98b4da | -3.6515 | -44.7312 | 2025-11-17 14:30:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d8908ec1-8c30-3361-a11e-50f787538c02 | -11.1332 | -44.0216 | 2025-11-17 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README58.md)
