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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b891671-52ea-3c08-8fe6-fc4f32c0c1e7 | -15.8037 | -51.0844 | 2026-09-01 00:30:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |
| c83144b2-f990-3598-879c-c3c728b63fef | -11.258 | -50.5836 | 2026-09-01 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 91f1e7db-6a6f-3fe0-8b82-22a78aeb23bf | -6.9552 | -55.635 | 2026-09-01 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 2213f1c8-0079-3d64-acb8-64d4a7ac9e7b | -16.0547 | -54.3908 | 2026-09-01 00:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d6fb3c5d-6e7c-3730-ab66-64f8c88edc8d | -14.1263 | -52.8106 | 2026-09-01 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| d0654a5e-e960-35e3-85a2-bc63a975944c | -4.7734 | -41.8026 | 2026-09-01 00:30:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| a64ecca1-bbdf-3343-a1f0-825529e16c69 | -10.0173 | -44.6849 | 2026-09-01 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d470f819-0a61-3ee8-b295-d73814d16384 | -6.9551 | -55.655 | 2026-09-01 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 25259620-13b0-3d6f-878d-51b551d785b1 | -6.9367 | -55.636 | 2026-09-01 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 2c24b6dc-02ca-34fb-b6c8-0ff36f3fe92c | -18.5089 | -50.8974 | 2026-09-01 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 8d16e0fb-3237-3be8-9d72-a5d2c664502a | -7.182 | -60.6904 | 2026-09-01 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 652bcd6a-0280-36ce-8494-c6c030d130e2 | -6.1183 | -53.5472 | 2026-09-01 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 8887da0d-bf58-3bde-8f90-78679548eb55 | -17.4122 | -42.3445 | 2026-09-01 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c4333e2f-d11c-3c7c-9a4c-241adcbc1cf3 | -10.0364 | -44.6825 | 2026-09-01 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| d8df321e-0768-3888-a592-aa26c5e07a17 | -7.2006 | -60.6706 | 2026-09-01 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 01cef007-9ed0-3f66-8099-ad59457ddbe4 | -14.1459 | -52.7871 | 2026-09-01 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 39d7f8a6-20b5-329d-9dea-b3588fba9e4d | -16.4773 | -47.9381 | 2026-09-01 00:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1196d292-3432-3295-ad5e-a67ed1f7af37 | -6.9551 | -55.655 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 64724c1b-2493-3cf1-a3b6-9a974e2fcca1 | -11.3232 | -45.2009 | 2026-09-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 0783bf63-680e-3f39-bc23-b15106b9de26 | -15.6762 | -48.7085 | 2026-09-01 00:40:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a508c2b4-0189-32be-a543-11e0b74c4a80 | -11.258 | -50.5836 | 2026-09-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 267.9 |
| 5afbff52-9334-3c0c-890d-a23c0f6fa1be | -17.4122 | -42.3445 | 2026-09-01 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 150472cc-ce57-31c5-95a1-4b0532fe68c0 | -17.3921 | -42.3495 | 2026-09-01 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 31f605dd-86ab-323b-bd57-74c25dab1825 | -15.7841 | -51.0874 | 2026-09-01 00:40:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 124ca238-f0e0-3441-a504-7ddd9b4d6021 | -9.4578 | -40.3392 | 2026-09-01 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.8 |
| ddb0998a-3353-334d-abe3-2b541b340b6a | -11.2577 | -50.605 | 2026-09-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 283.8 |
| c7bbf9ad-b4c5-3f15-8b9f-9aa98ae1226d | -12.1122 | -44.9699 | 2026-09-01 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| a97f9ee4-d699-3bcc-bf31-c03c67561985 | -10.0173 | -44.6849 | 2026-09-01 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5914ad27-8ed0-3b92-ae52-68a3b584923e | -11.304 | -45.2036 | 2026-09-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| b7dea173-9615-389f-a517-a7944350d099 | -16.4971 | -47.9344 | 2026-09-01 00:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 1fffbc2f-0075-384c-aeaf-862baa0ba377 | -7.3487 | -60.5883 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7bb68248-b90c-3c6b-9dd1-d9bb61d82872 | -6.8193 | -59.5734 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d54cfffd-671f-3a31-a59b-674371b8d44e | -6.6975 | -55.429 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 2d98d4de-442c-3afe-806a-e92c8ff880ae | -10.8627 | -45.356 | 2026-09-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a5de4e66-7751-30b4-8de6-7e91cfe9548c | -7.2005 | -60.6897 | 2026-09-01 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 5295702d-62f3-39e0-8e66-d90995fafa71 | -6.1183 | -53.5472 | 2026-09-01 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d0315f4c-346c-3902-b7dd-bfde36eb6be8 | -7.571 | -60.4643 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| c3eb2cce-26d3-329c-a030-67b93a7a2d53 | -15.7845 | -51.0657 | 2026-09-01 00:40:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e7428e50-ad1b-36b6-82cb-ba227f8ffcf3 | -10.0364 | -44.6825 | 2026-09-01 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 9c122322-b37a-360d-ba70-5435016af03d | -6.9552 | -55.635 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| d4c79e12-868c-31f3-853d-f9e1a4a3bed6 | -11.2767 | -50.6029 | 2026-09-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 0d350486-4096-32fb-91bc-84331154c61b | -10.3574 | -50.0171 | 2026-09-01 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2625dc24-d77d-3e42-874d-9524c610fd32 | -7.3488 | -60.5691 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 67cedc07-1e35-35dc-b6cf-90b0d8567ff1 | -11.277 | -50.5815 | 2026-09-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0ef95d3b-8ed1-3f47-a2ec-fdae66be7c03 | -15.8041 | -51.0627 | 2026-09-01 00:40:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fa9ae930-c890-30dc-a839-6c09bc459ea1 | -16.0547 | -54.3908 | 2026-09-01 00:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2f0025be-a6a6-3703-a824-412e9db57fce | -7.182 | -60.6904 | 2026-09-01 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3aa95fc8-191d-32e8-bf51-b0376e0e0a2c | -3.0425 | -39.9355 | 2026-09-01 00:40:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 334947f6-dbc5-305e-a831-dadf63a0fc12 | -6.9367 | -55.636 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3bc6c931-b2da-3dab-906a-82be2fc5a243 | -14.1266 | -52.7895 | 2026-09-01 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b0ee8a46-bbeb-360d-81b8-382cbbedad5f | -16.4773 | -47.9381 | 2026-09-01 00:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ea197c82-0beb-3b43-a421-514cc6cbf60d | -10.8818 | -45.3534 | 2026-09-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| afea148d-0f36-395e-8a2f-116f5b7e078c | -14.1459 | -52.7871 | 2026-09-01 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c260cc89-0b5f-3772-b236-fbc75a24ef84 | -7.3302 | -60.589 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1932a7f2-a2d9-3628-8139-9681585dc9df | -16.4768 | -47.9608 | 2026-09-01 00:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 76850390-3a87-35b7-8737-37958237e6ed | -6.6976 | -55.4091 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 507.6 |
| 1de33995-3ee2-31cf-9f48-0115acc56488 | -12.1117 | -44.9931 | 2026-09-01 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| db83c5b3-e454-39aa-b7b6-3b4dab2e89e2 | -6.6978 | -55.3891 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d82bd0ca-8232-3eac-843d-8bd66db18c46 | -6.1844 | -57.7395 | 2026-09-01 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e767bca2-1d31-3798-94e1-8672764657ac | -6.7162 | -55.4082 | 2026-09-01 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| ea520c8f-2a00-3d3c-b352-0703f17bf752 | -17.372 | -42.3544 | 2026-09-01 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 137.3 |
| e3f0c8fd-d739-3cf6-b50e-f89020b2035b | -7.5709 | -60.4835 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 11c0f2e2-8309-3841-8233-6991c65f73ba | -6.8009 | -59.5742 | 2026-09-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 27b25fe8-fc84-36a4-bbf9-9ec9111543d2 | -15.8037 | -51.0844 | 2026-09-01 00:40:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 307.5 |
| 01b812cb-c5a4-3b91-a85b-bba18650d26a | -11.2391 | -50.5857 | 2026-09-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 8e6b050d-a3ee-3cb8-a2d2-38b26fdb027e | -15.6566 | -48.7118 | 2026-09-01 00:40:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c1ad41bc-74c9-31df-a14c-8c444ea599bd | -6.6036 | -58.5972 | 2026-09-01 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 6d2d9150-f3f4-3ea4-bd1f-af99c8977fa7 | -17.3713 | -42.3794 | 2026-09-01 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c267a32f-19d6-3799-a345-8205dfe64c77 | -17.3914 | -42.3744 | 2026-09-01 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| a312f99f-ecd8-3ced-8a5b-c7839c341195 | -9.4574 | -40.3641 | 2026-09-01 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 4e5f3a0b-846a-3c91-b8b0-27738f0ebe25 | -15.8041 | -51.0627 | 2026-09-01 00:50:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 635fceb0-c82b-3bb8-be66-33167feeceb7 | -17.372 | -42.3544 | 2026-09-01 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| dc5eb6d9-4716-315b-9494-9132ab7bccbb | -16.0547 | -54.3908 | 2026-09-01 00:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 23cf6b70-4cfd-34d9-80d5-e2ea67c4b64b | -10.3574 | -50.0171 | 2026-09-01 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 09b07eb9-6965-3dfb-85d5-8eb14c3567cf | -10.7456 | -47.9978 | 2026-09-01 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 01b13df5-ee55-3dfe-a05e-e8b45f6c8d69 | -10.0364 | -44.6825 | 2026-09-01 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| ccd7a298-c654-3cfb-b5bf-4f4ed4c5c0d5 | -7.571 | -60.4643 | 2026-09-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0462a108-2193-35e2-8c06-1ee9dac0e7e2 | -7.182 | -60.6904 | 2026-09-01 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fe4e0923-ac5d-3704-8e93-f7c1b21feb7c | -6.1844 | -57.7395 | 2026-09-01 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4b05c79d-eaf4-3a54-abc3-811d256b6696 | -17.3921 | -42.3495 | 2026-09-01 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 5634dab8-0a56-398b-b6e8-256bd4c049a4 | -10.036 | -44.7056 | 2026-09-01 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 423a44f6-04c5-3b5f-b6af-6dc4db1fa54e | -6.9551 | -55.655 | 2026-09-01 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 92c1ec3d-1886-3beb-a21f-64f6f37b9bcd | -15.8037 | -51.0844 | 2026-09-01 00:50:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 227.9 |
| ab3fa871-ba9b-343f-8ddc-3e8c43ffe7ea | -6.9552 | -55.635 | 2026-09-01 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| f1ae7855-2f39-32d8-9922-9d42e933fbbe | -18.5089 | -50.8974 | 2026-09-01 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| f335249e-dc53-30e6-8848-059c5ac39c8b | -7.3302 | -60.589 | 2026-09-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 40c8ecc3-3210-3a17-8bfe-13ad002fe67b | -7.5895 | -60.4636 | 2026-09-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 7fb07b34-15e8-3c94-8551-5f984534eb96 | -10.7459 | -47.9757 | 2026-09-01 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bac76345-7e23-3d25-ae4d-be632828cbf2 | -10.8624 | -45.3789 | 2026-09-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f4437743-8afe-3aa2-b389-ea74b17234c0 | -6.7162 | -55.4082 | 2026-09-01 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c4386026-5592-3838-a3d2-9b9a4b49293b | -10.8818 | -45.3534 | 2026-09-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 467b6ac3-ad78-3518-9ba8-57d3fa7ec1fc | -10.8627 | -45.356 | 2026-09-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.8 |
| ed8d56fb-b62b-3f3d-a665-13b0172137e0 | -17.4122 | -42.3445 | 2026-09-01 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 96ee69d8-3ae4-38fc-8d41-82f0bf238610 | -7.013 | -52.9057 | 2026-09-01 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ff3e814c-645d-38ff-9cf8-49738cd15915 | -10.0173 | -44.6849 | 2026-09-01 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 88e0aa0a-f9f9-35c3-b3b5-5f76152a868b | -6.6036 | -58.5972 | 2026-09-01 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2a4d053d-25b6-3053-9853-8fb0e9d89167 | -17.3914 | -42.3744 | 2026-09-01 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 90741c16-99cc-3de1-9af1-44dd0177585f | -6.9367 | -55.636 | 2026-09-01 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 29245f76-bffb-3588-bd09-a61d8d5cdaf9 | -7.3487 | -60.5883 | 2026-09-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e43b8416-81d6-3652-b9aa-dd96d1ed9633 | -6.6035 | -58.6166 | 2026-09-01 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |


[Clique aqui para ver as próximas entradas](README12.md)
