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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35cfee20-114b-35d5-a028-13a19fb716f1 | -9.496 | -40.3337 | 2025-07-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 478.0 |
| cd7ea382-446b-3629-b7c8-b1a419b37972 | -6.1792 | -48.0494 | 2025-07-07 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 33e32873-ac1a-3030-8f9c-f59cf1a73016 | -9.4964 | -40.3088 | 2025-07-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.1 |
| ebd08f8a-14bc-3d97-8ee6-77fd85d8c860 | -9.4956 | -40.3586 | 2025-07-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.8 |
| b0c220ca-d90e-37b3-b53b-fdb1da2b9982 | -6.1604 | -48.0724 | 2025-07-07 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 244.9 |
| c7bb2c0e-c523-3849-a94b-946096906c58 | -9.4769 | -40.3365 | 2025-07-07 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 34adfd7b-9640-3317-bdeb-35b57d7a0e17 | -6.1792 | -48.0494 | 2025-07-07 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 359.7 |
| 97d7de00-bbe1-3c76-8eda-0f0eb1270089 | -7.6938 | -44.578 | 2025-07-07 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 21acbdaa-e572-3d97-ac62-65dcea21c1ad | -6.1606 | -48.0507 | 2025-07-07 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 430.9 |
| 9ed0dd45-5dbd-3c3b-81d8-0c8c17d021f8 | -9.4956 | -40.3586 | 2025-07-07 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 945e2584-7054-3fa1-9fc3-0fe933dff4e0 | -9.496 | -40.3337 | 2025-07-07 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 354.4 |
| ea603d65-2d4f-3f27-9522-2298696a2ca8 | -6.1791 | -48.0712 | 2025-07-07 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 202.6 |
| a30e6ca6-c5dd-32c4-9618-02bb0af7f793 | -9.4964 | -40.3088 | 2025-07-07 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 9fd9afc8-202a-3e4e-97b8-0523e4ee0822 | -6.1794 | -48.0277 | 2025-07-07 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e3c8db0c-3026-3130-9caa-e24835b500e5 | -7.6935 | -44.601 | 2025-07-07 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 839c4dad-f394-30db-b723-c7b2391786dc | -6.1791 | -48.0712 | 2025-07-07 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 356.5 |
| 50d6cf10-1264-3b6a-8ba1-f4327ef482e3 | -6.1604 | -48.0724 | 2025-07-07 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 38989494-7c53-3c4a-85b0-58906abf75fc | -9.496 | -40.3337 | 2025-07-07 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 179.1 |
| f9612983-cb1b-3ec7-bdd4-05184d3ecbda | -7.7126 | -44.5762 | 2025-07-07 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7ef4f363-def6-3b0b-8683-ea066daf59f6 | -6.1606 | -48.0507 | 2025-07-07 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 286.6 |
| dae70cbe-4246-3075-8288-f50a5446c26a | -7.6749 | -44.5799 | 2025-07-07 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4aad269e-606d-3bce-8bb6-a4749784ceb0 | -7.6938 | -44.578 | 2025-07-07 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 9e31a77c-1aa4-3c33-9c2a-904e4979efe0 | -9.4769 | -40.3365 | 2025-07-07 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 149.3 |
| 458380fe-202a-3d09-94c7-e20cc30ce225 | -6.1792 | -48.0494 | 2025-07-07 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 510.1 |
| ad926a5a-f6bb-3b86-8586-0a2c29c8f130 | -9.4769 | -40.3365 | 2025-07-07 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 134.7 |
| 8032a2e7-3330-3e0a-925e-b76f56b5eb0e | -6.1791 | -48.0712 | 2025-07-07 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 0440d11a-b589-38d0-bcf5-f06a13bc7165 | -12.0628 | -43.5022 | 2025-07-07 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 24b24c91-de6e-3625-b61c-70d01cb64074 | -6.1606 | -48.0507 | 2025-07-07 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0bee8976-7bb8-3bed-a30e-fe0189f2d26e | -6.1792 | -48.0494 | 2025-07-07 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| bcf94a0a-d894-39d6-9785-09b8453fe038 | -6.1604 | -48.0724 | 2025-07-07 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| b7bf3eb4-658d-3bcb-b0fe-38abf074f691 | -9.496 | -40.3337 | 2025-07-07 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 521f67a7-08e5-35fc-b0ee-4ff52ef27f7d | -7.6938 | -44.578 | 2025-07-07 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 03fca101-4d21-3031-8dde-1eff6008288f | -6.1792 | -48.0494 | 2025-07-07 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 507.6 |
| 58e0fe5d-037e-33fc-ada6-172001b46545 | -6.1606 | -48.0507 | 2025-07-07 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 18b3e96d-ddd7-3942-911b-47f176123106 | -6.1791 | -48.0712 | 2025-07-07 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 238.6 |
| de0d1e64-32f7-30de-9647-e4bf09f0e647 | -9.496 | -40.3337 | 2025-07-07 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 96e38306-141b-3dcc-913b-86b76aa23a4e | -6.1604 | -48.0724 | 2025-07-07 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 4b5f4240-5733-317f-9c80-88229f828d4f | -9.4769 | -40.3365 | 2025-07-07 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 8680ff9d-416d-3c86-9cc3-bf7b67c7e0ee | -12.0628 | -43.5022 | 2025-07-07 01:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 896d3399-2ce5-3e56-b4aa-cf6bd7779647 | -6.1606 | -48.0507 | 2025-07-07 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 310.3 |
| 2b423096-0ea7-3260-ba2e-dde29ff559b6 | -12.0628 | -43.5022 | 2025-07-07 01:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f1747b9d-d53d-36dd-9e25-d67ed9188809 | -6.1791 | -48.0712 | 2025-07-07 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| fa08557c-102c-32fd-b792-8c53a4c0e73a | -9.4769 | -40.3365 | 2025-07-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 210.4 |
| 08bdf900-c14b-33fa-b72f-91c6eb5e721d | -6.1792 | -48.0494 | 2025-07-07 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 8563d2ac-57b0-3a00-9a1d-187bc7b5d68a | -9.4765 | -40.3613 | 2025-07-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 43af385f-a2ef-37e9-9376-6eaf8935f833 | -9.4773 | -40.3116 | 2025-07-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 35799183-20f2-3a59-9ff6-f43519c18145 | -9.4956 | -40.3586 | 2025-07-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 219a04a0-a37b-33d7-b09f-f429e0ada1f0 | -9.4964 | -40.3088 | 2025-07-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 38c579b9-724b-3e83-990d-1099052d3fd2 | -6.1604 | -48.0724 | 2025-07-07 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 87ba6f8e-4759-3f8a-8f57-484ef5193c56 | -9.496 | -40.3337 | 2025-07-07 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 272.8 |
| d7887c2f-5cf8-32d1-9f44-3353c47c9a77 | -9.4956 | -40.3586 | 2025-07-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 4b2a3f3c-8d6c-3b7f-a6b1-13e63951043a | -12.0628 | -43.5022 | 2025-07-07 02:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| cf139bea-012f-31f2-86cb-64bace5c8cf6 | -6.1608 | -48.0289 | 2025-07-07 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 40629a71-6107-301d-9c61-89e31132962d | -7.6938 | -44.578 | 2025-07-07 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3bb8d7d2-18f9-35b2-88ae-e30f64177317 | -6.1792 | -48.0494 | 2025-07-07 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 324.8 |
| 8b7f78ba-ed86-305b-a519-633c8b893f79 | -6.1794 | -48.0277 | 2025-07-07 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 6d73d0c6-ec65-3a5d-a79a-e1c912715bc7 | -6.1604 | -48.0724 | 2025-07-07 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 1f30cb77-5904-32b1-8014-060f9893d8c9 | -9.496 | -40.3337 | 2025-07-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 266.5 |
| e851391b-16a3-3279-901e-3979e812ef59 | -6.1791 | -48.0712 | 2025-07-07 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 7405fe9a-b41f-30d6-8376-e9b11ab5eb4c | -6.1606 | -48.0507 | 2025-07-07 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 320.0 |
| 2f213432-2249-3ff0-ae36-a04a9bc1e56e | -9.4769 | -40.3365 | 2025-07-07 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 200.8 |
| bfa6e95d-5975-3f5a-b9a5-e7e1a065aac1 | -6.1791 | -48.0712 | 2025-07-07 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 240.3 |
| a60ecf9c-9cec-3ca6-a1ee-87058504ff06 | -12.0628 | -43.5022 | 2025-07-07 02:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 74332fc1-beb1-315e-8446-d0c2142cb611 | -6.1606 | -48.0507 | 2025-07-07 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 34682e2d-e50c-3b11-b5e9-496ea44fd28d | -7.6938 | -44.578 | 2025-07-07 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 988d4bcb-8ff6-3546-9275-3f43c6d6fa9a | -9.4769 | -40.3365 | 2025-07-07 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 187.8 |
| e524cc8a-5bf9-3fd5-be66-2f684c4d5f52 | -6.1604 | -48.0724 | 2025-07-07 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 5b1002ac-ef2a-322b-84ab-f9459f53e8c4 | -6.1792 | -48.0494 | 2025-07-07 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 338.1 |
| 96abfbd0-caea-3d2a-9828-d4b07c9e36c2 | -9.496 | -40.3337 | 2025-07-07 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 219.8 |
| 34f9c357-46d9-358a-908e-1d006b067fab | -6.1792 | -48.0494 | 2025-07-07 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 6b4b32f2-210c-3d04-a9b2-c0e8d4f6a10d | -6.1791 | -48.0712 | 2025-07-07 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 32c2a563-5dd1-31e9-89c3-36323dd93d40 | -6.1604 | -48.0724 | 2025-07-07 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 6b8e9a9f-9252-3338-91b1-51027abf87fa | -7.694 | -44.555 | 2025-07-07 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5e1349f4-8445-3fa0-8347-afb905ee9b02 | -7.6938 | -44.578 | 2025-07-07 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 190.0 |
| a6f5ede6-ddc8-30e6-ade3-cdf97fe82dd8 | -6.1606 | -48.0507 | 2025-07-07 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 302.5 |
| a7c9dde8-7dc3-300f-aae0-94a319822de1 | -6.1791 | -48.0712 | 2025-07-07 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 05fc9c4b-ac52-315c-bdbb-6a0bacb32661 | -7.6938 | -44.578 | 2025-07-07 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 096e8d1e-6efa-3cd5-a9c7-67e9c0df1c76 | -6.1604 | -48.0724 | 2025-07-07 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| fa22cacd-cd65-3bbd-a7f1-427c36ce7124 | -6.1606 | -48.0507 | 2025-07-07 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 267.8 |
| 21090615-d52d-367c-8560-f798f38c1027 | -6.1792 | -48.0494 | 2025-07-07 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 210.3 |
| e89412a7-f59c-3e5f-8b60-3cdfa65f6ac2 | -7.6938 | -44.578 | 2025-07-07 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 11caaf19-4433-395c-9854-f4423ac37919 | -6.1792 | -48.0494 | 2025-07-07 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 179.2 |
| e24f0743-f183-3973-ba3f-e9d7a2b46215 | -6.1604 | -48.0724 | 2025-07-07 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 9a5df58d-3286-3fbc-9035-482a7d30cccc | -6.1791 | -48.0712 | 2025-07-07 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| d9460174-d5a1-3631-be76-75b7d0e5f62b | -6.1606 | -48.0507 | 2025-07-07 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 255.4 |
| dd45773f-5659-3dd1-a500-c6f0bb855a50 | -6.1606 | -48.0507 | 2025-07-07 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 247.5 |
| f48764e3-1af9-322c-ade7-7c3be1dc8d37 | -6.1604 | -48.0724 | 2025-07-07 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 2f455e44-7829-364b-91c5-0b906f17e047 | -12.0628 | -43.5022 | 2025-07-07 02:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8806fb95-37dd-3b64-8a20-106df05fd915 | -6.1791 | -48.0712 | 2025-07-07 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 60f9d159-6f97-3724-bebf-e68533627d7d | -6.1792 | -48.0494 | 2025-07-07 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 5feed566-831e-3018-9d2c-b6b6fd38cb2b | -6.1606 | -48.0507 | 2025-07-07 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| d32c2beb-e073-3290-9d95-c4139996182e | -6.1792 | -48.0494 | 2025-07-07 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 18f515ac-ded1-3ca9-98db-5671c941531e | -6.1604 | -48.0724 | 2025-07-07 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 72c0497b-12fa-359a-89d7-df644ababd0e | -7.6938 | -44.578 | 2025-07-07 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ba88a622-8fa7-3de1-a04b-6a3f6dcaccf6 | -6.1791 | -48.0712 | 2025-07-07 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 27a7aa90-565a-33e6-886e-f34c637f48b3 | -7.694 | -44.555 | 2025-07-07 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 337e37fd-c42a-374b-a0a1-fba08113ce5b | -7.6935 | -44.601 | 2025-07-07 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5d7b9cbc-6dde-3800-83bc-e26682f35318 | -7.6938 | -44.578 | 2025-07-07 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| b22184d5-ae16-3abd-96e4-4c450cbd94dc | -6.1791 | -48.0712 | 2025-07-07 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 29894fa0-93ea-3def-8645-bfaeb4e291d4 | -6.1606 | -48.0507 | 2025-07-07 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 210.4 |


[Clique aqui para ver as próximas entradas](README3.md)
