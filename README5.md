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
| 6dfbc477-566e-38f3-8a0b-ce9e7c6927b6 | -14.66696 | -51.84962 | 2025-03-07 12:44:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3b33c3f2-09f8-3846-bd90-026ad74aabc6 | -14.66837 | -51.84016 | 2025-03-07 12:44:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 88c87bca-96f4-3b62-ba42-39616e034bfa | -30.36972 | -51.9697 | 2025-03-07 12:46:00 | TERRA_M-T | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 11.3 |
| 0f9cc922-aa5e-357a-b469-1aa300d1e2bf | -24.89678 | -50.10509 | 2025-03-07 12:46:00 | TERRA_M-T | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 57aedd62-d7ff-38c4-9d26-c5062191f62b | -29.30024 | -52.16191 | 2025-03-07 12:46:00 | TERRA_M-T | MARQUES DE SOUZA | RIO GRANDE DO SUL | Brasil | 4312054 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| f12e5d52-58d5-3342-a384-9763777aa0ef | -29.52144 | -51.5721 | 2025-03-07 12:46:00 | TERRA_M-T | MARATÁ | RIO GRANDE DO SUL | Brasil | 4311791 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0237359d-a0e5-3c10-be15-94c7b2ea119f | -31.66432 | -53.39088 | 2025-03-07 12:46:00 | TERRA_M-T | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| 0dd42d1b-c0d1-3cd4-a2a7-12fc38883349 | -31.67333 | -53.39244 | 2025-03-07 12:46:00 | TERRA_M-T | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 7.3 |
| de2650a8-3515-3e9c-b8b0-1ed37c7373f6 | -12.9179 | -45.075 | 2025-03-07 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 04062b85-72ef-3c15-9fe3-25665fc2871e | -11.5971 | -44.8385 | 2025-03-07 13:10:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| d377f973-755b-33ea-aebb-de8a036a2b7e | -12.9179 | -45.075 | 2025-03-07 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 821d74f6-5b5c-3738-8e9b-ace1962df1df | -11.5971 | -44.8385 | 2025-03-07 13:20:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 73644f35-ef08-3326-99cb-673c7e54286b | -12.9179 | -45.075 | 2025-03-07 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 60a6f7d0-721c-3d8d-94ea-ebab1e21314a | -11.5971 | -44.8385 | 2025-03-07 13:40:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e08c1afe-55be-3389-8ba5-23b252252da5 | -16.0101 | -43.5966 | 2025-03-07 13:40:00 | GOES-16 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| ccd47e5f-b61b-3149-b647-209a7e8966a6 | -12.9179 | -45.075 | 2025-03-07 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1c01e28d-e31e-32f1-bd6a-dd7b1d117511 | -11.5779 | -44.8413 | 2025-03-07 13:50:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 201a558a-0410-3119-bdca-f47582398f27 | -11.5971 | -44.8385 | 2025-03-07 13:50:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 0c8a4436-022c-3e92-95d3-019f8cc20136 | -11.5971 | -44.8385 | 2025-03-07 14:10:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| ec04b50b-5f7d-3e9c-9d1d-42121ca87646 | -20.723 | -49.4242 | 2025-03-07 14:10:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 1ba3c011-8996-328b-b2d4-81d5e3370046 | -11.5779 | -44.8413 | 2025-03-07 14:10:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| dda017df-aa3a-34f7-ac66-8268f65299e7 | -16.0443 | -43.8059 | 2025-03-07 14:10:00 | GOES-16 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 35716070-bab3-30af-8b07-3a13135fc410 | -20.723 | -49.4242 | 2025-03-07 14:20:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| ebb37d50-47e6-3a53-9bdd-17c9aa420373 | -20.7223 | -49.4471 | 2025-03-07 14:20:00 | GOES-16 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ff213b1a-976c-3c1d-95e3-40ee99e5e287 | -12.9179 | -45.075 | 2025-03-07 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e564a076-6591-3775-a9fd-9e9c691a448d | -12.8985 | -45.0781 | 2025-03-07 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 46200d28-8448-372a-86d3-c0b156ee8e63 | -20.723 | -49.4242 | 2025-03-07 14:30:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 5f6bd666-a6bd-31d7-be52-294ed19ff3d9 | -20.7223 | -49.4471 | 2025-03-07 14:30:00 | GOES-16 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c5123d3a-3911-3dbc-b3f9-9e21b19ee020 | -12.9179 | -45.075 | 2025-03-07 14:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |


