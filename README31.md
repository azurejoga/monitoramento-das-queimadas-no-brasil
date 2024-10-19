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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4c24b5b-cceb-3cf7-9d91-7c636bcb054a | -3.27808 | -50.66195 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 09f2bb40-0fd9-3ed0-aa2c-6399f1c6f4be | -3.27753 | -50.66549 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 479fbd6e-e9d4-3c71-9318-c9744b336159 | -3.27472 | -50.66142 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80b6c835-5fc8-39ca-b6c1-c59fbc2309d3 | -3.27081 | -50.66443 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9b652cf-fe96-36ed-a046-37b95ad8f293 | -3.24756 | -50.94551 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a481d3f-2c5f-3ff5-aabd-eab01054bf49 | -3.24422 | -50.945 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18bfd9ae-46e1-3ba2-8ea5-4a48501083e5 | -3.23892 | -50.84723 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97c49059-fc4c-343d-8801-5c7797d385a7 | -3.23837 | -50.85074 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 956b0c7f-a1f3-3a24-bc53-9fd9cd088d57 | -3.23503 | -50.85023 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcf7791c-17c6-39f6-8988-eda0435bbd39 | -3.21954 | -51.2551 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c525b1-f4d2-3e84-9159-8f734c9c37db | -3.2089 | -51.03971 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e5cbb3a-7de6-3c8d-85fb-59441bdc2263 | -3.20835 | -51.0432 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ab92b8-f099-3f8b-800d-86f297cc7ded | -3.20828 | -51.02176 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee253117-90e2-3dca-905a-6e801a17e4ff | -3.20611 | -51.03571 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc938b81-7ea5-3d9d-97af-821b5174818b | -3.20556 | -51.03919 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0182d67-a813-33fe-bb3a-a1b17966449e | -3.20502 | -51.04268 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4b80339-e4a4-3d5f-bc14-cab2b7481082 | -3.20494 | -51.02125 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1abca73-dacc-3dc1-b8b2-9a8cd7c926ce | -3.1864 | -51.29256 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85d2df10-9a77-39a5-815f-2641fd5c21fa | -3.18585 | -51.29603 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3f898b6-80b0-3c5b-8796-ff67be75f491 | -3.18307 | -51.29205 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63b7639d-fbbe-3a95-9534-12557b54ecf5 | -3.18253 | -51.29552 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4eb175b-850f-3844-9504-2f5a43474465 | -3.16908 | -51.25082 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58bf0157-e9d7-34b5-be33-9a920f5691eb | -3.16575 | -51.2503 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d24b350e-f2a0-3428-835f-0980b212ea4c | -3.15801 | -51.25621 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d6be5b-ff69-3a50-bb51-9c8282655c56 | -3.15003 | -51.35074 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76c4642a-9fe0-3a5d-a98a-fb50760ab528 | -3.14948 | -51.3542 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8658706d-12ec-32b1-b633-24b4c24036cc | -3.14942 | -51.14109 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 160bbe5a-cf93-3031-a7ee-6515431951c2 | -3.14888 | -51.14457 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca78915c-fd41-3ff4-a10e-a35495837d4d | -3.1467 | -51.35022 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 936cb429-3aaf-3529-aab8-2203da263e0d | -3.14616 | -51.35369 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35a590a5-9d6b-3f04-bc1c-7997ac233f2c | -3.14609 | -51.14058 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c9ed8d8-d282-3bb3-9d93-bbb7e02e0fff | -3.14554 | -51.14406 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad005b16-b1b5-30fa-8a7e-39b807a1667c | -3.12162 | -51.31796 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d09cb153-a937-375e-b841-e0aef3891445 | -3.10336 | -51.32577 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d101069-1aa4-34a6-9af5-2d72692c451b | -3.10282 | -51.32923 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee27361-7f53-375d-85d1-b38081c52096 | -3.09251 | -51.2212 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c657b46-126b-378c-adbd-bfc609ee958c | -3.09197 | -51.22466 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4980ce1-0518-32af-9884-38672e348b89 | -3.08973 | -51.21721 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 353cdf09-7da3-3104-b559-232cd1d28c3d | -3.08918 | -51.22068 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ec1786b-f197-35d9-aefa-0a4564774ce6 | -3.08749 | -51.20975 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9de27270-f615-3b1b-b3b9-8ac02b4f6f34 | -3.08694 | -51.21322 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbb8848b-6697-3c7a-848b-06fc319061fa | -3.0864 | -51.21669 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ddf6e417-5861-3f38-9f15-c1ca68db2a76 | -3.08585 | -51.22017 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e30f86a-181f-3b73-b95f-cad81a41b677 | -3.08416 | -51.20923 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d81b9c12-6edd-3ab9-a976-0b7686eb71ff | -3.08361 | -51.2127 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4116e756-18a6-31ef-b2a5-fe3f297ec7f2 | -3.08307 | -51.21618 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3954dc23-8584-37f5-ac9d-775da6f218fd | -3.07974 | -51.21566 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c64c6ed8-edfb-3aae-9f54-562522a41866 | -3.0792 | -51.21914 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfaea4a2-07d4-36e2-9f54-b14b903c3619 | -3.07818 | -51.24738 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bfd9856-252c-37e8-8d6d-9fe72dee854f | -3.07641 | -51.21515 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e517241-132e-3dba-8fd5-c331a654ad51 | -3.07486 | -51.24686 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56484f1b-57e3-3499-a649-323dbe86de10 | -3.07431 | -51.25033 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd1392d0-69f3-36b2-a2fb-f8a114a63f45 | -3.06888 | -51.05336 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e0c8be-066d-3bb1-97fc-2dc599e58d10 | -3.06554 | -51.05284 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cc4ed8a-c564-3f18-b969-50c2bed89b19 | -3.06495 | -51.26662 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 309ae3f2-7668-397e-a862-f11b0d879761 | -3.0533 | -51.04381 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99b45e31-5bf5-38ff-9993-2973f21bcbb8 | -3.05275 | -51.04729 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f78ecdc5-e2f4-3c21-ad0f-464c2c76b71e | -3.0522 | -51.05078 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c582f28-7ab0-32e9-9f7a-09524557b061 | -3.04981 | -50.97898 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 170d4aeb-3203-3beb-bd05-20eafe3c801b | -3.04942 | -51.04678 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f66dcaa-c3ae-3e84-8072-b2d7f33e465b | -3.04926 | -50.98247 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4427223e-e97e-306f-b2f3-42cd41ad4b39 | -3.04871 | -50.98596 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b678b2b-f455-3448-9964-390f12c16950 | -3.04413 | -51.33429 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e0be4a0-e440-3be4-a976-d79f55a644be | -3.31122 | -51.64114 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baef878b-be46-332f-b7a9-dfbaafa99057 | -3.14495 | -51.49162 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dba74fc-23d6-3171-8285-cc912525d44c | -3.14441 | -51.49508 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb498d64-a83f-3f8c-8e78-f785eb960c2f | -3.14163 | -51.4911 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8401e2e-91d7-3341-90b4-3b3716858a39 | -3.01475 | -51.35406 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79db23af-76c1-3101-8378-00e0ecd6ef3f | -3.01037 | -50.99074 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b759e87d-6ef5-3d28-b93d-d41f68a75cb7 | -3.00703 | -50.99022 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dbaa6ac-3786-33fa-922d-3c87ffdc4891 | -2.99375 | -51.00958 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57d8f8b1-6a87-3569-8920-30691eb3cfbc | -2.99042 | -51.00906 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89ffb93b-ba8d-3b4c-a1b9-4e966e78986f | -2.9894 | -51.03741 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d83ec49e-2a78-32de-b4fa-03cd3532a9b1 | -2.98661 | -51.03341 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| edb2f2a8-a23e-3473-be70-2e69d8b6d51a | -2.98607 | -51.03689 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e04c8063-e28f-39d7-8e4f-41f522c451f2 | -2.98328 | -51.03289 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b783fb5-ec0f-3707-a9fd-b3c131344654 | -2.98274 | -51.03637 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b16e7cd9-361b-3253-b1c0-ba0fa5239d9c | -2.97132 | -51.10946 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb4b32a4-828c-371f-b25c-f543ccda25b8 | -2.94908 | -51.03836 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 605b761a-2441-3315-92fd-937396fb35ad | -2.94853 | -51.04185 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60793a5d-628b-32d2-9528-16ab0d505271 | -2.86637 | -51.3912 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cfc5512-5ba0-30f6-8c9c-e7d9a099cf72 | -2.86583 | -51.39465 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b7fd70-bcdb-3cb9-a6af-56c255d5d7d3 | -2.86325 | -51.28094 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 969399c6-63bf-30a7-9a30-04dd9717a4c9 | -2.86271 | -51.2844 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56f67fa-c836-3937-a654-52da8645e106 | -2.86217 | -51.28786 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dba4855-9ce1-3060-8e43-38c32f9209cd | -2.86136 | -51.01785 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d1d9b66-58d9-3891-8977-f52d7d2d31d6 | -2.85993 | -51.28042 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e11b12-ace6-340e-9c69-a2d8ab5412f0 | -2.85939 | -51.28388 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecdc6893-bac5-3075-9787-f09a7a42875a | -2.85884 | -51.28734 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b355e60-f77f-3f70-85c5-2b779a67ba5a | -2.83951 | -51.30205 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15babf06-6631-3c27-a07e-23ade00e3326 | -2.83897 | -51.3055 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d1fe1fba-cc92-3d5b-91d9-79320e9b91f3 | -2.83619 | -51.30153 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4b8a012a-45e5-3e55-b52e-710da2ebb6d7 | -2.83565 | -51.30499 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c7ad695-31d0-3082-8b2e-29521cfe137c | -2.83286 | -51.30101 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 33fbdcff-4a17-3a6d-b827-7a3b37732b83 | -2.83232 | -51.30447 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 76577950-1b0c-3da6-9982-b989192e0eb6 | -2.82358 | -51.33853 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b7fa74-a5cb-396a-a48b-2a3eb530edd0 | -2.8225 | -51.34544 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 572ba251-cfbc-36f9-b794-939ac334f40f | -2.81971 | -51.34147 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8775452a-6c08-31b6-9806-87aed396a419 | -2.81917 | -51.34493 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89303fdc-0c2b-32ea-b0fa-635e44793f30 | -2.81863 | -51.34838 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README32.md)
