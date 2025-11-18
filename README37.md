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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b87771de-b2c1-3e82-9e83-4cf8484b74da | -5.36497 | -44.86206 | 2025-11-18 04:48:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5487fc5-6f1f-3ada-9bc7-1480dc381186 | -3.25363 | -43.04066 | 2025-11-18 04:48:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 86b658d2-6009-3801-8e7c-fc7a03505c7c | -3.03174 | -44.476 | 2025-11-18 04:48:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf1a6702-c3f4-32ff-b75a-5508f02341fd | -2.95022 | -45.34818 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a310174-90f9-3b2e-9f8c-0f6d3f50fe96 | -3.51797 | -50.34299 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 404727e5-7ac9-32df-9173-1e7dd99d85d2 | -2.98201 | -51.07819 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d63636d-c604-3b59-a6ab-4881ce02512e | -5.40567 | -44.06178 | 2025-11-18 04:48:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2761652-7729-39a3-af4d-fb110a067cf8 | -3.64445 | -50.16499 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48433013-3525-35c9-bd06-d7b5b1c9455a | -3.30379 | -50.06873 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 089be497-5274-36b4-b231-01755652f96f | -3.4403 | -51.64962 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c75da6d0-7b95-3ed8-80f3-5459867d3c86 | -3.0875 | -51.2599 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d027436-1e97-3179-a360-0a1764d3f451 | -3.17454 | -50.64928 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9fd082-a540-3985-8a31-66ac5d8da1c1 | -4.193 | -44.24196 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28ff7d40-f20b-33f3-acfc-4212f08ba91e | -3.3027 | -50.07563 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e1e1791-7849-3f3b-97ad-9e20456ea579 | -2.51503 | -47.82285 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 880cd35a-1617-3073-92f2-be92214ba73a | -6.44233 | -45.73601 | 2025-11-18 04:48:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd387eb3-964d-3472-86fe-949ee1190c0c | -3.10551 | -53.14216 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf0d91bf-84b4-33f7-8393-465e4c557490 | -3.34386 | -53.76152 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83d34d2b-2fe6-32fe-b60a-a543878b96ae | -3.22964 | -51.17852 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432e7c0a-0111-3827-8f4c-021904b8d4f2 | -4.71808 | -50.94998 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57f6d53b-5a6c-31a2-a7dc-d95d38d9b53a | -3.17568 | -46.57381 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fb2208f-4b8e-3dc2-b5c1-281b17ffa6fd | -3.95039 | -50.32641 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63f97d37-e4c5-38c0-82b6-4f0c927f51b1 | -4.05102 | -47.50001 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36842552-4dc7-341d-9f1e-d346d033ee91 | -3.13368 | -50.28952 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 299319d5-b0b4-37b2-a7ba-9a2f46e14eba | -3.4939 | -54.05018 | 2025-11-18 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b1ead05-1f4a-3453-9d0e-ddb6d4c63788 | -4.13441 | -52.11974 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b87b5612-90fb-3f12-b374-6b2bae006df9 | -3.09029 | -51.26393 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b9efeb5-c4b1-3903-9d4e-4a6e9f478820 | -3.14938 | -51.48726 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76064b7b-d58d-3b20-8a17-ec846897e6a4 | -4.67538 | -50.70906 | 2025-11-18 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f27edf41-d5a7-3b50-8e5d-d2a197784102 | -3.78214 | -47.74562 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e50331b8-4df9-33de-af08-078c8ce2bc0c | -3.24932 | -50.69289 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 878434e7-1159-3419-b4b6-a0d2d09f7da7 | -1.77089 | -54.19083 | 2025-11-18 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a258d966-ba8f-31f6-95a3-d92d119b69f2 | -4.64138 | -47.94622 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6de7df50-5c43-3c39-a47e-9a1c039c10da | -6.30881 | -43.78129 | 2025-11-18 04:48:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33616296-2141-3fc4-8af5-bef92680f866 | -2.49556 | -49.33863 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3fb8ac9-7dc5-3a10-a9bc-52cae2705941 | -3.64562 | -50.84058 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae06bc8a-8c1f-3bd0-b365-34b64ae63354 | -1.19847 | -48.93336 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e243a64b-9aa7-3f1f-9e68-f0cf7a12a4e2 | -3.59848 | -40.96828 | 2025-11-18 04:48:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 026fa463-7224-318d-b9bf-f26060a59cfa | -3.7895 | -51.10559 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1114108-d2c3-326a-8aca-08e610d32bc7 | -3.99195 | -50.51315 | 2025-11-18 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27bf7e74-9986-3df5-8ce2-f45f2233d877 | -3.3863 | -51.02402 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11eb74bd-03ab-3bac-9478-474334666462 | -3.87764 | -47.17455 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a536ef12-2002-3b4b-986e-cd1fdb735f53 | -4.18986 | -44.23278 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e5a06f8-bfb3-3efd-9f69-7b41c9895154 | -5.42548 | -43.04486 | 2025-11-18 04:48:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 564dd303-7895-3f3f-b68c-a1d5566d84dc | -4.18169 | -44.22709 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1f7e8a0d-b0e6-3fe1-a139-d19dcb738d9c | -3.06179 | -49.36971 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7469534-5aea-3f72-a239-763057d20e93 | -4.27301 | -44.24929 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 221a5de4-a1b3-3402-9ef1-d5a168137c96 | -3.90028 | -47.93541 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb44c770-1788-3529-98a9-81a8cdc4654a | -4.64847 | -47.94722 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 25771887-3005-322d-ab85-dbdcd1b295cf | -3.38331 | -50.1666 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa33b8ab-8557-3459-8aa7-c6afb884037b | -3.35021 | -53.21666 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da21aa78-24f8-3508-8266-296eea176730 | -3.66668 | -50.21797 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fe0ddbe-5401-36b0-91d8-fc53158765b9 | -3.23568 | -50.49967 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870525fc-bfda-3b92-9efd-a70e25642138 | -3.65042 | -51.95523 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb0a7503-f539-35d0-868e-259b8c7db0c2 | -3.24412 | -51.08761 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f058470-7a30-3fa5-9184-61ddd24f6fd2 | -4.13218 | -52.11192 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cdd408f-c13c-3e98-8c74-e6d61bf47a41 | -4.9746 | -41.85788 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4fb8a5f-4119-37f9-ba1a-97a053798d7e | -2.83212 | -45.41746 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0629654-d8a4-3963-aa13-ed87a6cc1b38 | -4.52576 | -46.41544 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e51914f4-d0f9-3126-a83d-49b5b29a728d | -2.51745 | -47.80755 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4faae4ed-4327-3a36-8fbc-896771a8f317 | -3.17909 | -46.60155 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98168123-c14b-34c6-b085-d814d9729693 | -2.98979 | -51.07224 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d808f07-05b5-30ff-9a1a-7dc32081fb5b | -3.39609 | -50.19333 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab2f1259-17a3-3150-9933-f3716bb5ddc8 | -3.0719 | -50.23028 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810fe485-be18-3b4e-8d3c-38397c58647e | -6.20457 | -46.88203 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e37e6c2-9076-3719-ba23-4ee70fa2cadd | -3.84496 | -51.05729 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6582973c-f15d-3f19-a0dd-dd2aea9df6c0 | -3.48076 | -51.57531 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00150e84-f0b3-3c72-8123-9f02bd1e1e04 | -3.75819 | -50.9441 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe71b50-faae-3ae6-9f75-b4f19474389e | -3.98805 | -51.06878 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 554fdd03-017c-359c-ac5a-1024cc8f2031 | -3.48453 | -52.35922 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11987e84-21d6-37b6-8725-b71b3a2af0a4 | -3.23459 | -50.50657 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3278e7cd-c92a-33c3-a3e5-d04c202ea588 | -0.88431 | -52.00054 | 2025-11-18 04:48:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feac5a7d-47df-3484-b2b2-925683593aae | -0.59692 | -52.15689 | 2025-11-18 04:48:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e278bb9-848a-306b-8ca3-cb0f72899210 | -3.46965 | -50.24003 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cb8fd17-7e79-3104-ae4f-020130fd625c | -4.35292 | -46.81876 | 2025-11-18 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 606416f2-b2f6-3f2c-aecf-c89c92aa3309 | -3.89755 | -50.1059 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f6432f6-97b7-33d7-b2e5-9a6798a63f10 | -6.43821 | -45.73547 | 2025-11-18 04:48:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9256a7c5-5a89-3e0c-950e-757e828e8c8e | -2.922 | -47.85147 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2001138-56df-319d-b6b6-69071cbe8c2e | -3.15076 | -50.26748 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bae89dfb-eacb-34d1-9d87-3cb6109ef028 | -4.22595 | -53.50546 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb574490-907f-30c1-8137-23020f5f8944 | -2.52881 | -51.18337 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35d49f81-13b1-30f1-bdee-cfc716fb728f | -5.33823 | -43.75339 | 2025-11-18 04:48:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84feb639-2d5b-33aa-a26f-f9866708bb91 | -2.52969 | -58.02903 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35657c2f-bc10-3fa7-9107-591be4eb3fd4 | 0.27235 | -51.07338 | 2025-11-18 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a205369-a3fe-3676-bd1b-0ecd3952abfe | -6.21149 | -46.88789 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85616e6a-2e1b-3944-9542-a078c492e5db | -4.13101 | -52.11921 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1c87d9c-dde4-39c5-9fc7-a55c7943d299 | -4.14062 | -52.12447 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4210dfec-417b-397c-bd08-67d692cb188f | -6.93913 | -39.62467 | 2025-11-18 04:48:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6e059ca8-89eb-3a0a-bf22-9c5a9b060801 | -2.50579 | -47.81354 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88e33b3c-4ab0-38e5-808d-08f037d614aa | -4.27217 | -44.25264 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61ba1a3-1d22-3622-9cfa-3138f24b5329 | -5.43113 | -43.04017 | 2025-11-18 04:48:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cea791a3-4f42-3e5d-9ea2-259745482ddb | -3.22325 | -50.06686 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc2cf92a-d174-3e29-ad1a-2e074509657e | -3.21799 | -50.18617 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5838e95e-25bd-3642-8612-bc6a2641ba91 | -4.27279 | -44.24841 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7fb32a2-9e22-3817-98a9-8eac2c9a8992 | -0.88838 | -51.99729 | 2025-11-18 04:48:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46b43310-ea98-3538-a6c4-cb2a0b2a5ab6 | -5.75124 | -45.10322 | 2025-11-18 04:48:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e54d5d30-86fb-35ea-a221-7313459971a9 | -0.98805 | -47.07611 | 2025-11-18 04:48:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fb2d3d3b-8982-35cc-9f60-12184550f9e8 | -3.60475 | -43.61277 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78080396-d068-3d60-b3ec-f05fa7326a3f | -4.64555 | -47.94271 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 3bf6ae48-9d7f-323c-91b1-8aefba9f114c | -4.64493 | -47.94671 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |


[Clique aqui para ver as próximas entradas](README38.md)
