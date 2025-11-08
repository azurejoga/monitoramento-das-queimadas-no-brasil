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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03b2ab8e-0235-300b-b0a6-ba8d38905e5c | -3.33683 | -50.09939 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7248c93-1fde-3939-945f-8cfa0f85603c | -5.03934 | -45.92308 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c8c247e-3162-3b31-bc00-3a17cea8f488 | -6.12893 | -41.51521 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 034058bf-1586-3161-9213-5aace6a955d6 | -4.71433 | -42.94829 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 74c4caa2-0ef3-3b22-b9b8-f190e536b3d9 | -6.69523 | -40.8302 | 2025-11-08 04:06:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f2bfa34-f5b6-3330-852a-b7b7e8358123 | -5.77212 | -43.64476 | 2025-11-08 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf904ee-1631-3023-8e61-2b7fdfdef923 | -4.69145 | -46.40391 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b103b6d-332b-385a-8d69-1eed28a39474 | -2.98043 | -48.71047 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ade187f4-a3bc-3899-84bb-80581bdef0f1 | -3.35186 | -50.17783 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a0e81b1-b044-3b18-a2f6-f190d6eb3285 | -3.58919 | -51.23443 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53457306-93de-3d95-a785-940a016c13b8 | -3.65916 | -43.91844 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a5a0536-ede6-31b1-a8a8-b031d64d7d0d | -5.9354 | -38.18264 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ea9f2081-28bf-33ed-b49e-26bca0b94f62 | -7.49009 | -40.12616 | 2025-11-08 04:06:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0986c668-7ee0-3de4-b543-92c8249110d1 | -5.03242 | -45.17672 | 2025-11-08 04:06:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05ce5054-485a-3073-bd0f-139e0776aa4c | -3.65285 | -43.93456 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c4e173-4722-30ad-963f-41200801f62d | -6.16946 | -39.32744 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57b64849-ae79-33eb-8337-045f6764d147 | -4.51861 | -41.92839 | 2025-11-08 04:06:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 410ce882-84a2-340d-8205-3ea1ace4d9d0 | -5.05557 | -43.31702 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1978434-4f55-35f6-9e17-543c01df921a | -6.19086 | -44.53146 | 2025-11-08 04:06:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72c45e44-350c-315a-a466-a9884b0124b0 | -3.91899 | -51.01551 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bfa4195f-6c32-3244-a3a1-0cf9ddb592d3 | -3.03051 | -50.27185 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a725ee33-56f7-3eec-b882-635bfaddcafe | -3.82933 | -49.8289 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ed34bd8-db66-34fd-b043-8be18a2777ff | -6.20634 | -43.26224 | 2025-11-08 04:06:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85054a65-5ef8-3b15-a7f5-13e1d0b8028a | -4.61562 | -44.38454 | 2025-11-08 04:06:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3718f8a0-e507-3734-b532-17d17bc50d79 | -4.4515 | -46.43834 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9f5b9bd-c4ba-362b-999c-6cfdad67ee5d | -4.59088 | -45.99519 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 825b6f36-2b23-36f7-8083-7eccb0c33377 | -4.40223 | -44.0802 | 2025-11-08 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6237d5f7-d70a-3647-aaff-6c784f6f22c8 | -5.61549 | -41.08089 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c48e8b1d-9523-3bea-a0fc-c4467d2b5bcd | -4.64589 | -40.79383 | 2025-11-08 04:06:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb917873-b7b8-3043-b959-74d383534e21 | -3.24876 | -50.14974 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b3d6ed4-d0f7-3ca3-b977-8f2692cb1afa | -3.67791 | -52.09441 | 2025-11-08 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 615c571d-b7ec-3faa-97c9-fa2d14f9e7fe | -4.46778 | -45.33227 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6ad08676-1c30-3fa7-a748-ddb6d1404340 | -3.34784 | -50.2023 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dcfd024-6f6a-397a-8124-4b97c48ba944 | -5.26185 | -47.16166 | 2025-11-08 04:06:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d64be08e-3219-39b8-ac4d-9aee642731c8 | -3.09003 | -50.32348 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85ec3220-4e31-3c6f-8e0b-5b9a03bb7038 | -3.34236 | -50.20143 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51c3ffaa-52d9-39e5-9b0e-2794b8a8bb65 | -4.64894 | -46.87457 | 2025-11-08 04:06:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 432e1b0f-4b37-33b2-8206-6b01cdf7394e | -4.87506 | -49.77337 | 2025-11-08 04:06:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 696c5f5b-aaba-3591-a89d-42bc3dc43d7e | -3.42992 | -50.11979 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d1e7d81-01fc-3c08-bd49-ebec01e15465 | -5.78171 | -46.55951 | 2025-11-08 04:06:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9365f774-1a44-311a-8d7c-4f15ed3ad8a3 | -4.69297 | -45.85768 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15aaf83d-0411-3222-b8c3-607aa50a3c78 | -5.75577 | -40.79227 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6ce20170-5584-3e18-9778-1a0aa2813568 | -4.3834 | -45.68081 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99c23eba-cb12-35be-97cf-ca1231596cbb | -5.37435 | -44.72621 | 2025-11-08 04:06:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d159afb-5ffd-36d0-b85e-2909a3e2b518 | -3.32188 | -53.36814 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07096963-9665-3387-9b19-f002d02bb9f8 | -5.90996 | -44.5245 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4bd2d75-2822-34d8-a272-ad0f97eb5568 | -6.22576 | -41.72148 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 661defc1-a7d3-3e26-b7f5-474d44427883 | -3.64423 | -45.88558 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86c86be5-33f4-3550-a47d-dfc013d795bc | -4.68318 | -46.40259 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| adc4e9a5-5be8-362a-9252-fe617e62727e | -5.97987 | -44.17522 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63e4ff99-a00b-3e56-9aa2-868f9e46f631 | -3.95347 | -45.45287 | 2025-11-08 04:06:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b297adb1-da30-3b16-a485-4758353a58c9 | -6.2654 | -43.6852 | 2025-11-08 04:06:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67a47a66-36da-3efa-9088-a35d667c88d7 | -5.78111 | -46.5632 | 2025-11-08 04:06:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c7aba53-e464-3859-947d-949a2ef57fbd | -5.61433 | -45.04295 | 2025-11-08 04:06:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1a8b3a4-06f3-3136-8b2d-4dbcc264841f | -6.58436 | -43.75549 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97609dd6-a16b-3d3d-831c-989b9a54aee3 | -6.36936 | -41.74117 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff66caa3-df01-3062-bcf0-66c286574d93 | -6.49235 | -41.60466 | 2025-11-08 04:06:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c52c90ba-85c4-3d4c-904d-a6db9db8d7ac | -7.88866 | -38.37156 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61ab8045-5576-35e7-8b77-6cabc5ddca51 | -4.47628 | -45.32878 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ad36995d-0ff2-3a0a-bfa7-290257c2d89b | -6.22246 | -41.72096 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a1373723-32fb-36fc-9e29-46aae144b37b | -3.58645 | -51.25076 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f2aa890-0754-3e41-9d8b-633874312c1a | -6.22684 | -47.32815 | 2025-11-08 04:06:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88b3c378-dc17-395f-a5c1-29f8d6630eb4 | -7.54496 | -41.66269 | 2025-11-08 04:06:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 23c38c28-6b39-3d94-aa15-3e091654a850 | -4.46084 | -43.21725 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8f8dbce-3f21-3c1b-b48e-8574df2ee65f | -5.77175 | -40.79832 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1482142c-1013-3e15-b529-cb567d424e40 | -3.25172 | -50.13939 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a795c61c-7dab-3f57-9458-478ce996dbe6 | -4.81456 | -45.57969 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 642d7113-f083-319d-8445-408707bfbd08 | -6.22397 | -47.01357 | 2025-11-08 04:06:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80852da6-502b-3d67-a36c-633a58c11d7e | -3.25212 | -52.91643 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea2ada27-c0a0-3ea9-b794-c7edd214bf9f | -3.25108 | -50.13559 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7d2e6ea-f420-3800-8b20-29246278aaff | -4.40425 | -44.78625 | 2025-11-08 04:06:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e1a282d-9200-3c7e-91d8-8400e732f7b5 | -3.44006 | -46.19276 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc24c4be-cad7-3ff1-8b45-96550c0bfdbc | -5.05211 | -43.31647 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 493e45e9-84d2-3e6f-a9d1-4e5c120b4dbd | -4.20239 | -46.39854 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f74ba409-062f-3c13-be9b-f0fcc129df2b | -4.46431 | -43.21779 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e06357-c682-3e0e-9317-5a8a57af9791 | -5.6309 | -41.09034 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a374cef-330d-33b8-8ee7-aeb3a87d2b52 | -4.3394 | -45.7257 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5b140ba-2b00-300d-9af5-3d57b8b33547 | -4.5345 | -45.619 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6c97b0ed-d08b-32a3-9f35-56408aed3fae | -2.98681 | -48.70282 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c022b4-a5b4-3f49-9ddb-139942e0e97c | -5.77505 | -40.79884 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f12d6ca-5df9-3b7a-88ab-f4e71c52a4ab | -3.40076 | -45.43518 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 949be912-266a-304a-8e51-864a1cedbd5e | -4.64827 | -46.87868 | 2025-11-08 04:06:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2037f1f5-509a-352e-a8ea-29ea0dccbf5e | -4.46777 | -43.21833 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9da354c6-7f9b-3409-bb10-9544c216a329 | -3.24462 | -48.75921 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d761927-ab00-3c75-934a-c62b44a9c50f | -3.58059 | -51.24993 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ee16a7c-65f5-3969-a474-1db425581d7a | -5.37364 | -44.73059 | 2025-11-08 04:06:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d37c9987-9079-3283-a2b6-86d0761c28b7 | -3.45288 | -48.83825 | 2025-11-08 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09cd6b95-a018-3661-bf1c-01cb9568c1d4 | -3.53313 | -47.53929 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac9ec3bf-8941-393c-95b6-f323365e9002 | -6.223 | -41.7175 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8126f127-5097-31f6-9391-e071da618d18 | -3.31045 | -50.12351 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e43988d1-190d-3ff4-8bf2-da914eb1762d | -5.28232 | -44.41386 | 2025-11-08 04:06:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac710e06-3123-36a2-8ec8-e58fe6e96ced | -7.38435 | -43.51682 | 2025-11-08 04:06:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42d7b73b-3af7-33f3-a819-96068910dae0 | -4.62926 | -43.25905 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 025c6a0f-a527-37f5-be3c-503fa91a016e | -5.08953 | -44.7979 | 2025-11-08 04:06:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 525b149c-2a5d-345f-a8fa-1462bcf0a340 | -4.80122 | -49.60365 | 2025-11-08 04:06:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd247cf5-4560-3eb9-9f1e-408cf8d3119e | -4.41515 | -46.28275 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6566efda-7389-3a05-b2da-7af11e7a5603 | -4.56774 | -48.48464 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db1105fc-5ad6-3640-b551-935076955958 | -3.34639 | -50.17695 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fdc3736-de5a-3981-be01-5dd9033f16dd | -3.64364 | -45.88917 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a48fbecf-ee8d-30dc-a235-e6b54afd36f1 | -6.18119 | -43.44196 | 2025-11-08 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
