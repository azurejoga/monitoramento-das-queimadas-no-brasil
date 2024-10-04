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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dd286d5-84e7-3091-ba44-f9a881f414d9 | -4.45084 | -42.88629 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3713eb04-6030-364b-9812-10951e5ddcbe | -4.45025 | -42.88996 | 2024-10-04 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d713975e-6d53-3b2a-a567-738b52125e88 | -6.4506 | -42.36457 | 2024-10-04 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2f1e370b-395c-3ca2-b22c-107c129878e9 | -6.17668 | -43.2103 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 659559a6-e571-333f-859b-01b0c8ad0c63 | -6.17329 | -43.20978 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b7e6cc10-da1c-3480-8dec-b243c27b48b5 | -6.1727 | -43.21346 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3a0e1c5a-40b4-30ca-8298-afc924855de1 | -6.02725 | -43.20187 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| af1d7057-aa0e-3aac-b55d-d86b0a68c329 | -6.02046 | -43.2008 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21579bc3-bdaf-39ac-b05f-afc2a089b7b4 | -6.01987 | -43.20445 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 757e6812-dceb-38c5-ad08-146b9f07088a | -6.01647 | -43.20394 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0f13554e-801c-303b-b090-4a8fef510c2c | -5.88267 | -43.04786 | 2024-10-04 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8da07eca-cad7-39c8-8d36-cdcdb2239645 | -5.88151 | -43.0552 | 2024-10-04 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 35424f5b-95ed-3e46-9130-22ffed118add | -5.54691 | -42.77946 | 2024-10-04 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bb5fe8b6-4a23-38bf-8b0a-ff0e769cdd64 | -5.54412 | -42.77532 | 2024-10-04 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1f5132e6-d6cf-367b-8bb8-82acae921054 | -5.54355 | -42.77892 | 2024-10-04 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 65a2de34-132d-38cb-8325-d47da15f70be | -5.54297 | -42.78252 | 2024-10-04 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 308045fa-0c64-3629-9a40-de8fdc4a863e | -5.5135 | -42.78171 | 2024-10-04 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a84a2021-a856-385f-b4b4-a307400481d8 | -5.50734 | -42.77705 | 2024-10-04 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3dfbfb90-e5e3-3986-9aec-4e296a576717 | -5.3227 | -42.97071 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99f2b8ee-765d-3509-b161-0adba85d2497 | -5.32211 | -42.97435 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 34a22ecd-3ed3-3c3b-add1-6727aa5e3ce9 | -5.31931 | -42.97018 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7ec6a796-efcb-39fb-af00-a895194ae43c | -5.31873 | -42.97382 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cff1945e-da1b-357e-8892-08e854dd049a | -5.31534 | -42.97328 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a15ae064-3f5f-3479-aec5-d86aa5861cbe | -5.31476 | -42.97691 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bde63d70-7323-33d6-9637-d03388ccfadd | -5.31195 | -42.97274 | 2024-10-04 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59211dd5-4c8e-3942-b13e-154b35f30a56 | -6.32282 | -43.48328 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddd068a8-59da-3c69-9a6d-58f8bad72331 | -6.31999 | -43.47906 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e08ea6e7-f0e1-3c78-9a75-afe9e8c85e02 | -6.31742 | -43.05376 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5956e49a-d823-33bc-bc93-d2d0ca674410 | -6.31685 | -43.05738 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 358f992e-cd5c-3479-b432-4dbf1040e300 | -6.31627 | -43.061 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96eea88d-abc4-3138-86ec-c3e2c74b7cb9 | -6.31532 | -43.42113 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 539bc557-05ca-3429-b66d-ba4f465b82dd | -6.31472 | -43.42482 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb873676-755e-3dfc-8f84-33fc47864a2b | -6.3129 | -43.06046 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a57dad55-d174-385f-8a19-eb255b516011 | -6.31232 | -43.06409 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97a8cad7-c1a5-3be2-ba67-c6af7d4f4c75 | -6.3119 | -43.4206 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 584e1ce0-09f6-368e-9b39-5861027ac6e0 | -6.31131 | -43.42428 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56c12814-2c1d-32f1-aefc-062a1745f4cb | -6.29806 | -43.44118 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46813679-7a2a-39bb-9f27-bde9e93a81a4 | -6.29525 | -43.43692 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 28941c2f-2f5e-3726-9da5-fa24f8e197b0 | -6.29465 | -43.44064 | 2024-10-04 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ab5a161-d49b-38aa-bcda-385846c8f24f | -6.29171 | -43.01988 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25078f46-7828-30db-b1bb-b8e1249dc56b | -6.29111 | -43.26267 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3f5c79c-6166-35cf-9d23-3762ac75c82c | -6.28889 | -43.25477 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8b30664-f4bb-370c-9855-9d9b3f80c511 | -6.28834 | -43.01933 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99bb5fac-9c59-37d4-94bb-be952eab4307 | -6.28718 | -43.02657 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5febc933-edde-306a-b497-219834446fa6 | -6.2054 | -43.27554 | 2024-10-04 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e493ab0a-9094-3ed1-9431-5eaa5b96a10c | -5.3966 | -43.10226 | 2024-10-04 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39f61c85-6b34-35e5-a2c5-52a88096c41a | -5.39601 | -43.10593 | 2024-10-04 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a9caf0b-23d8-368c-bd9d-f867ecf4b0f7 | -6.66514 | -42.10605 | 2024-10-04 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f5a9d19d-f954-343c-9114-8401cc6ecbaf | -6.64366 | -42.11329 | 2024-10-04 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4497ed28-a883-329b-94a7-9ea51ab15343 | -6.64312 | -42.11674 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ba5542e2-dbb8-38bc-82e3-ae5a35e92567 | -6.64036 | -42.11276 | 2024-10-04 04:08:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dd56994a-3d36-338f-9149-fd1e4265d01e | -7.86478 | -43.07955 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c107fd20-c5e0-3e7d-ac66-f76d49d81769 | -7.82537 | -43.0733 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d6d83432-27ba-399b-a0a4-364f85b69f68 | -7.79344 | -43.10127 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4c1d3eee-dae2-3eb9-b7fb-e425676ed09f | -7.79286 | -43.10485 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 17c769d6-63b5-3cd7-951d-cc9ab1cfb611 | -7.76457 | -43.06727 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ae7bbdb-0756-3068-bb7e-bcbbc00815bd | -7.75788 | -43.06619 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6f47bdf1-97f3-3069-b04d-84bac6f816df | -7.7573 | -43.06977 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 40094bb5-0306-3dcb-bbc6-8d9cc3447e1e | -7.75672 | -43.07337 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f5dc7c07-8e8d-3317-9df8-06089ba865a6 | -7.75488 | -43.06945 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e5ee6c48-aa0c-3c69-8841-a82057b4f379 | -7.75431 | -43.07305 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 71f200bc-e9bd-3643-9967-110dae686775 | -7.75153 | -43.06891 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 56243103-2cb8-3a3a-a575-fd8345b29c95 | -7.75096 | -43.07251 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f9758b37-f6be-3226-88f9-73e423f3eba9 | -7.75045 | -43.05408 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3dc062e-5651-3f81-b3b0-ee1ba3079f80 | -7.74989 | -43.05765 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3ac35f2-15bb-3167-acc8-4f8a1f29fc17 | -7.74932 | -43.06122 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 749719e5-2182-3d82-b8b0-b05d44b9bbf5 | -7.74875 | -43.0648 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e11e8e83-d248-3f14-bf7a-2471ad21982e | -7.74818 | -43.06838 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 5c37f4ab-1bef-39be-9afa-f75a02f5e382 | -7.74761 | -43.07197 | 2024-10-04 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fa05e1cc-f5db-3773-ae04-2eba5fce22a7 | -7.69211 | -42.99002 | 2024-10-04 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ca082deb-f685-3c32-ac6b-cd63ff8e2a7a | -7.68934 | -42.98592 | 2024-10-04 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| daed17bb-cce9-395e-b809-4ca48c06d90e | -7.68876 | -42.98948 | 2024-10-04 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 80263b67-d180-306c-b635-9e5d55944a77 | -7.25627 | -43.37854 | 2024-10-04 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a83543e6-9fcf-3a4f-9636-a55fa8fe4c16 | -6.83969 | -42.82773 | 2024-10-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e58380a2-c2e0-399a-9d02-e7185dd32c51 | -6.83692 | -42.82366 | 2024-10-04 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8b221175-151f-3017-a773-c9f429843b23 | -6.53744 | -43.22271 | 2024-10-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 742f13d2-ecf4-35a2-9ffc-5d5eaefc0783 | -6.45214 | -43.20509 | 2024-10-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be498f0f-eae3-31fc-ba8c-5eed3274c9c6 | -6.45155 | -43.20873 | 2024-10-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa5eb8be-8816-3e80-ab9a-3929ee3a50bf | -9.25893 | -43.49581 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e9453788-0011-3c07-b12f-772b48ab47ec | -9.25835 | -43.49941 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c0f46ed-e391-3ef4-867e-bd336ebc0206 | -9.25777 | -43.50301 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e84db835-6af7-342e-9f29-dd7767d07cb2 | -9.25719 | -43.50661 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 33c36894-c231-3590-8b31-557b898546a6 | -9.25384 | -43.50608 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 70a7b443-6dad-3c38-b155-d21bbd9d49c2 | -9.25325 | -43.50968 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b1cbdcc5-c852-3d15-aa63-54dadb2f4e9b | -9.25106 | -43.50194 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 362ed4ca-80ba-3960-9aef-ca21c062159c | -9.25048 | -43.50555 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5123bbf-3448-31bb-99d5-744301358b5d | -9.2499 | -43.50915 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7861cd60-86ab-3d94-9869-31395bfe9ef0 | -9.24829 | -43.49781 | 2024-10-04 04:08:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f16da85a-21f1-36a5-83ea-740a8388d5c9 | -9.15236 | -43.16384 | 2024-10-04 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cf5f3760-7c69-3910-bfd2-384a6c7776a3 | -9.15016 | -43.1562 | 2024-10-04 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 31f1f9f2-d058-3cf5-9c94-b48d8377aa3a | -9.1496 | -43.15975 | 2024-10-04 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e7e1f549-9955-374a-a256-970854b28855 | -8.14968 | -42.89668 | 2024-10-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 361d8519-8302-3e94-8da7-61f6083f1170 | -8.14912 | -42.90019 | 2024-10-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f3b9ad8e-f0a1-3149-9427-02dad06602af | -8.1458 | -42.89965 | 2024-10-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8adfeb7d-041e-359d-adce-c5c6903f7e63 | -8.18455 | -43.70327 | 2024-10-04 04:08:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c202c188-647f-3bc3-b1be-99f8244ff3e2 | -8.18396 | -43.70695 | 2024-10-04 04:08:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 98f8c94c-2141-34b4-93bb-8e0049576954 | -7.99332 | -43.8023 | 2024-10-04 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13238a38-e2b0-3d8d-94a9-51fa881fc8b3 | -10.47722 | -43.65024 | 2024-10-04 04:08:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59388311-8614-371b-ae33-bb4e02a2b258 | -9.95037 | -44.02307 | 2024-10-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d05845b2-e071-3557-8423-78e3ea568daa | -9.94978 | -44.02674 | 2024-10-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README68.md)
