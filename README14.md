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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f6afcb9-5980-36df-a50e-692af33d5d27 | -24.18589 | -54.01803 | 2026-03-01 12:33:00 | TERRA_M-T | TERRA ROXA | PARANÁ | Brasil | 4127403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5a4ab2f0-bba8-3646-937f-aaf0bfaf8d36 | -23.79424 | -53.20241 | 2026-03-01 12:33:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e75a93af-71a9-3d01-a4ac-1eafc3dea587 | -21.71084 | -56.30938 | 2026-03-01 12:33:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f78038b9-f829-35ce-a7e1-7c51382db762 | -23.73062 | -53.20753 | 2026-03-01 12:33:00 | TERRA_M-T | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 68b39e8d-d7fc-3d35-bb71-319da3f08b09 | -29.22161 | -51.3241 | 2026-03-01 12:36:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| bfae1d34-21a4-338f-a435-5c71c19b5469 | -27.94714 | -52.92535 | 2026-03-01 12:36:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| fb5719db-a362-3ea5-9bd6-1bb78e988feb | -26.62719 | -52.58425 | 2026-03-01 12:36:00 | TERRA_M-T | SÃO DOMINGOS | SANTA CATARINA | Brasil | 4216107 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 23a6df73-e57a-3345-b524-a6dff5e6c44c | -29.39649 | -56.63054 | 2026-03-01 12:36:00 | TERRA_M-T | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 8.8 |
| 374e66a6-8408-3ba0-a880-f26735f54148 | -26.57818 | -53.55742 | 2026-03-01 12:36:00 | TERRA_M-T | GUARACIABA | SANTA CATARINA | Brasil | 4206405 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 91bfe723-2d22-3881-a9db-a5f908c12c58 | -27.9489 | -52.90882 | 2026-03-01 12:36:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 45e6a918-e3c4-3d56-b6c7-93ea78365bf1 | 1.5047 | -59.9116 | 2026-03-01 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 213f5c52-662d-309a-b43a-2aa9e8653822 | 1.4864 | -59.9117 | 2026-03-01 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 51473fba-584f-33d1-8400-ac9c59e1944c | 3.4381 | -60.8161 | 2026-03-01 12:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5b11cbd8-2158-30e8-bd22-1b946710571e | 1.5046 | -59.9306 | 2026-03-01 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0c54fe8d-75e3-3856-a321-07532e52a22a | 1.4864 | -59.9308 | 2026-03-01 12:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3323ece0-be5d-3996-b2b4-0416d2e659c0 | 1.5047 | -59.9116 | 2026-03-01 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 2a89904f-4cf0-3b8f-8b75-5a3515a6a482 | 3.4381 | -60.8161 | 2026-03-01 12:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9fbb0b94-0c16-39c0-9ce8-c00d9c8a894c | 1.5046 | -59.9306 | 2026-03-01 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 99ccfef9-9738-30a7-8261-f1d0eb56ae6c | 1.4864 | -59.9117 | 2026-03-01 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.8 |
| d015ee18-ce4b-3b6c-a64b-5e62e1c305de | 1.4864 | -59.9308 | 2026-03-01 12:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 430139ab-5d32-3458-a47e-feea6e1a8ea9 | 1.5047 | -59.9116 | 2026-03-01 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 5e5e8b4a-a0f0-3c4e-8259-63e36b150521 | 3.4381 | -60.8161 | 2026-03-01 13:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 56af52b9-07e2-3455-9826-8109c3ea87fe | 1.5046 | -59.9306 | 2026-03-01 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.2 |
| dbe74c5c-d161-365c-986d-a45d3e0bef65 | 1.4864 | -59.9117 | 2026-03-01 13:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 013171d7-91c3-3d26-8f49-649045ead889 | 3.0548 | -60.6901 | 2026-03-01 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a0191f32-21c1-3374-b9db-7057fa325827 | 1.5046 | -59.9306 | 2026-03-01 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ad74acfb-8954-30e4-805d-d6d9a14c8ea3 | 1.4864 | -59.9117 | 2026-03-01 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 153.5 |
| bd517ff8-2044-3f8e-a64e-309a2c83e855 | 1.5047 | -59.9116 | 2026-03-01 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 49b76c17-460e-3311-a30c-a93fd5ebd4a8 | 1.4864 | -59.9308 | 2026-03-01 13:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c5e24eb4-5749-3807-a416-fae25063ea47 | 3.4381 | -60.8161 | 2026-03-01 13:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4dc36c7e-1323-34ad-9b5d-50a801aefd7e | 1.4864 | -59.9308 | 2026-03-01 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| adcf50b2-d170-336e-90c5-384d1a6b5f65 | 1.5047 | -59.9116 | 2026-03-01 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.8 |
| d7f97c8b-06aa-3d20-acf4-ce0973c550ca | 1.4864 | -59.9117 | 2026-03-01 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 154.4 |
| ff3f86e5-5dd0-3717-8830-af3f95438c4a | 1.5046 | -59.9306 | 2026-03-01 13:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 90bc26e1-d184-3787-b0d0-ef3efdd5d506 | 1.5047 | -59.9116 | 2026-03-01 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 67e8bf43-92c1-3a42-8d8f-30cec58b98c6 | 1.5046 | -59.9306 | 2026-03-01 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 56c10664-ec4d-3f26-ab70-d86265f1f0af | 1.4864 | -59.9308 | 2026-03-01 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 47385b4b-5593-38dd-99ff-20a128cb5c7a | 1.4864 | -59.9117 | 2026-03-01 13:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 20d1715b-6120-3c3c-990a-225e9fcb03df | -21.659 | -56.3175 | 2026-03-01 13:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 92bcb215-efab-38f7-8e9e-e9e890026afd | 1.5046 | -59.9306 | 2026-03-01 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.8 |
| c130289f-81c5-37d9-bd93-e7eb1357aa2c | 1.5047 | -59.9116 | 2026-03-01 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 141.1 |
| c2625341-d6dd-3476-8356-c812a1714492 | 1.4864 | -59.9308 | 2026-03-01 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7ebc7157-2ce6-33e8-943f-58cda736ff98 | 1.4864 | -59.9117 | 2026-03-01 13:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.4 |
| b5188551-fdc3-3cc0-aa95-ec1a509a7aec | 1.4864 | -59.9308 | 2026-03-01 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 6d700b2b-9b70-3ddc-9c96-d46840911da5 | 1.4864 | -59.9117 | 2026-03-01 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 658f2ae9-adc9-339d-863a-320fb2161125 | 1.5047 | -59.9116 | 2026-03-01 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.6 |
| c3bdf4dd-4129-3371-8d42-ac138ad25b8c | -21.659 | -56.3175 | 2026-03-01 13:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 89caf340-80fe-33b6-9b08-e1a43fbc43c9 | 1.5046 | -59.9306 | 2026-03-01 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9610b907-e4ba-31e4-ba06-ff81305e57a3 | 1.5047 | -59.9116 | 2026-03-01 14:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 139.6 |
| de6feef3-2923-3a27-9393-21beec19b094 | 3.6589 | -60.2801 | 2026-03-01 14:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 971cfeb8-9c6b-3ff4-8b19-76e4cd03ea33 | 1.4864 | -59.9117 | 2026-03-01 14:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 921bf5f0-2817-3af0-87e8-d4b3d5c97f7d | 1.4864 | -59.9308 | 2026-03-01 14:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.4 |
| d5915e8c-a1ac-34e4-926f-1f7d5704a63e | 1.5046 | -59.9306 | 2026-03-01 14:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| f9f24ba1-13a0-3b14-81da-6c5b8642b441 | 1.4864 | -59.9117 | 2026-03-01 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 97d5e189-4ebb-3993-af0c-81425acf350f | 0.647 | -60.6572 | 2026-03-01 14:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 44acfaf6-4570-3261-9ce0-2e412b31b51e | 1.5046 | -59.9306 | 2026-03-01 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 3df713e7-d85b-3b99-b1fe-05eccbb767ad | 1.4864 | -59.9308 | 2026-03-01 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 98b0d01c-4bdb-37e2-865d-41c47970c6b8 | 1.5047 | -59.9116 | 2026-03-01 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 6f83869b-3955-3543-869f-73784e17b7dd | 3.493 | -60.7772 | 2026-03-01 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b85c3e93-6f2e-39ce-b186-e48eb7732dc9 | 0.647 | -60.6572 | 2026-03-01 14:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| dddd5a35-db7a-3345-a87d-88cf31b27412 | 1.4864 | -59.9308 | 2026-03-01 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 768d47ae-6791-3a90-94dd-836fe5f16484 | 1.5046 | -59.9306 | 2026-03-01 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 37d64c24-0ea5-3033-baa1-c503b02c18bc | 1.5047 | -59.9116 | 2026-03-01 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 7bb8afde-7ae2-3d29-a222-4c9f86abdb03 | 1.4864 | -59.9117 | 2026-03-01 14:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.7 |
| eb964501-5371-3836-925e-b158d7dec437 | 1.5047 | -59.9116 | 2026-03-01 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 159.8 |
| ec7eeab1-4bbe-31ad-b927-2eb802b8c332 | 1.4864 | -59.9308 | 2026-03-01 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 103004ae-3a89-3071-8836-5f2f1ad95087 | 1.4864 | -59.9117 | 2026-03-01 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 379bb962-5c87-367d-84ad-a370e1761333 | 1.5046 | -59.9306 | 2026-03-01 14:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.0 |
| de34696e-2d16-32af-a622-ee96ee7a203c | 0.647 | -60.6572 | 2026-03-01 14:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |


