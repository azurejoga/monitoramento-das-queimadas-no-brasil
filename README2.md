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
| 673b6dfd-445d-3f4c-b740-a0baacf320e7 | 1.5047 | -59.9116 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f0fb3bd5-247e-3ace-84c0-fee7dcfa0b6c | 1.4864 | -59.9308 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 90ad97e7-1e5f-3039-96e0-3eeb2de4ef6a | 1.4864 | -59.9117 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| fd5e7f6e-0c15-38bf-a550-be4d665398b0 | 1.5046 | -59.9306 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 42201a0d-8b8a-3c7b-ab62-fc0e2bf09ca6 | 1.4682 | -59.9119 | 2026-02-28 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b1abd415-633a-3ca1-a18d-bb96fd221379 | -20.5228 | -50.8458 | 2026-02-28 02:30:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| ada2e076-16fa-328f-8e50-ec19d39c3cfe | 1.8681 | -60.914 | 2026-02-28 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 6c1adc72-0d1b-3293-85f8-4336faa5217a | -20.5228 | -50.8458 | 2026-02-28 02:40:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |
| 848d3aef-de8f-36b9-a1c0-e17f032995e0 | -20.5234 | -50.8232 | 2026-02-28 02:40:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| b85908b3-9b56-3b81-9c18-be916b42cfc5 | 1.4864 | -59.9117 | 2026-02-28 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 79408c57-1ad8-3839-a088-a99d7f4ca171 | 1.5047 | -59.9116 | 2026-02-28 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.4 |
| c64578e6-dcb3-3efb-9132-297f1ec74298 | 1.4864 | -59.9308 | 2026-02-28 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 67b7d3ce-01b6-3ce1-bdfd-ed66327d1f14 | -20.5228 | -50.8458 | 2026-02-28 02:50:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| 0be1a123-fd74-3281-bf5a-d6948c496712 | 1.5046 | -59.9306 | 2026-02-28 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 8293fe66-dee7-3b1f-a688-0b5bf401afdb | 1.4681 | -59.9309 | 2026-02-28 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 7ca7fa36-b399-388f-b19e-c5b58d045dba | 1.5046 | -59.9306 | 2026-02-28 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e14299d3-3bde-3d80-850b-ad97e53a035b | 1.4681 | -59.9309 | 2026-02-28 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 989e0e29-c7ae-360c-a842-97d2dac262bc | -20.5228 | -50.8458 | 2026-02-28 03:00:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 4fe27f20-e15f-3f90-9752-2ed5b604bbd1 | 1.4864 | -59.9117 | 2026-02-28 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.1 |
| faf7ed2f-3ba7-39b4-a8ac-c3631e6aca2b | 1.4864 | -59.9308 | 2026-02-28 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 72eb4ec7-2c00-3e3c-acf5-4ad643e35453 | 1.4864 | -59.9308 | 2026-02-28 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| abd59632-2100-3256-83a0-87e56e4e99c3 | 1.5046 | -59.9306 | 2026-02-28 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 3391b2c8-128c-3bb6-99f1-c82c70491723 | 3.1663 | -59.9085 | 2026-02-28 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 666bf4e8-bcb7-3532-8a42-61ff0825fa90 | -20.5228 | -50.8458 | 2026-02-28 03:20:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 1a0549c9-9c20-37bb-90be-7da51b854d86 | 1.5046 | -59.9306 | 2026-02-28 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5f11e954-10af-30c6-875d-322e4d9b9ee1 | 1.4864 | -59.9308 | 2026-02-28 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 34d5238f-6180-32b6-b1b5-3d5def9e0e6b | 1.4681 | -59.9309 | 2026-02-28 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| def12c74-65a3-3118-8770-c59b9294a9f3 | 1.4864 | -59.9117 | 2026-02-28 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 2862749a-cb92-33cf-9dbd-c72f91ba76f7 | 1.5046 | -59.9306 | 2026-02-28 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 8a9ebf6f-4152-32b4-8259-95bb8d6ac6e4 | 1.4864 | -59.9308 | 2026-02-28 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8ed71a8f-669a-3d2e-b47c-95b91f87355d | 1.4681 | -59.9309 | 2026-02-28 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| dba2f408-a317-3b55-8627-bbaafeea135e | -20.5228 | -50.8458 | 2026-02-28 03:30:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.3 |
| ae55395d-a16a-32a8-b7e3-85b633642fc4 | 1.4864 | -59.9117 | 2026-02-28 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 5c3ffa1d-ac01-3dc9-9287-b777e89bb534 | 1.5046 | -59.9306 | 2026-02-28 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.3 |
| be116d8b-9354-3fa2-b402-58a3168141f7 | 1.4682 | -59.9119 | 2026-02-28 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 5ea209a5-272c-3886-b225-1c2f4f240007 | 1.4681 | -59.9309 | 2026-02-28 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 92f671a4-b70e-3faf-a66e-d84e2f626ca9 | 1.5047 | -59.9116 | 2026-02-28 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 69a6ef86-bf0a-319d-a8cc-b553704a030f | -20.5234 | -50.8232 | 2026-02-28 03:40:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 9d41f883-5b85-3d77-97ce-fff8d72730ab | 1.4864 | -59.9117 | 2026-02-28 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 0cef1482-7b8c-3b17-9448-45a801073e9f | 1.4864 | -59.9308 | 2026-02-28 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 8445008c-124b-34db-a109-8d5e43373c75 | -20.5228 | -50.8458 | 2026-02-28 03:40:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| ca756d6b-b95f-3e33-a193-7114479f70a2 | -20.5228 | -50.8458 | 2026-02-28 03:50:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 799ac5a3-492d-3bba-95cc-52e7ca40e7c3 | 1.5046 | -59.9306 | 2026-02-28 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 09e1b12d-c5ac-3ab6-9375-e2581d8c8e91 | -20.5228 | -50.8458 | 2026-02-28 04:00:00 | GOES-19 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 5ffd5649-aee6-33ec-8356-5d14e51d66bb | -6.77361 | -35.19937 | 2026-02-28 04:08:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad7539a0-c120-3442-82d5-6c8ea895dd5d | -19.79994 | -49.53148 | 2026-02-28 04:12:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ab91353-f2a7-33e5-9ede-d9daf1b83dfe | -20.5203 | -50.83786 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| a05632b7-e6e5-3838-8597-99646531f8aa | -20.52105 | -50.83389 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| df981e58-d7f7-3c31-813e-693b79afbed8 | -19.7965 | -49.53271 | 2026-02-28 04:12:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80af42d6-9ea9-355e-a1c9-e58856c80698 | -20.51203 | -50.83606 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 52bebdeb-1343-34d0-aacd-fc4d931863c6 | -20.51692 | -50.83298 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| 33315285-89fc-3d6b-aa9e-9b62e2ad6401 | -20.51954 | -50.84184 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 97ae2fed-f055-361f-9225-e10009c0d3fd | -20.51616 | -50.83696 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 3f460b85-9828-3da9-aaf9-2b4d3b7331d6 | -20.52443 | -50.83878 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a5314b27-4166-3300-8e70-ea0644a5e349 | -20.52518 | -50.83481 | 2026-02-28 04:12:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| be802038-df83-3be5-a2a3-718bc96c7f04 | -19.79607 | -49.53064 | 2026-02-28 04:12:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3dafe06-f3ff-38ba-a621-a69d04f97fa5 | -23.63818 | -53.21551 | 2026-02-28 04:14:00 | NOAA-21 | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6ee9d930-be60-3970-ad89-6bc8ee5ee670 | -21.68647 | -56.32286 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0684c52c-d667-3cbe-88fc-adf4e8047b40 | -21.68549 | -56.32721 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5fa139e8-f9ac-3546-97b0-0503d8c6d342 | -21.68744 | -56.31855 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1458c050-bd3a-3970-919b-839f8c02e26c | -21.80137 | -52.72319 | 2026-02-28 04:14:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6501bd79-469d-384e-90c1-88531e3fe6f8 | -21.68274 | -56.32064 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61f9bb0e-5872-3c20-90cc-49617bf5a295 | -21.8006 | -52.72584 | 2026-02-28 04:14:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57820a42-b7a1-30ee-84f1-9c0f341e0273 | -21.17991 | -56.49739 | 2026-02-28 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a4d727d-ff58-30d5-bd02-39d3a9eed97d | -23.63922 | -53.21051 | 2026-02-28 04:14:00 | NOAA-21 | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f4627847-249e-399c-950a-f5e3e3bc0082 | -23.64269 | -53.21663 | 2026-02-28 04:14:00 | NOAA-21 | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 82bf9d96-7353-3c2c-9125-9a9bd02d00c8 | -21.22963 | -56.25139 | 2026-02-28 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 993b622e-bbb1-368a-ab34-cdc0ac622510 | -22.02462 | -49.50793 | 2026-02-28 04:14:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c1e07d0d-644e-3574-8b77-ac683aaebba8 | -21.33439 | -49.11806 | 2026-02-28 04:14:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2ee5e38-9c49-3ab1-85a3-d9721c61f14e | -25.17446 | -49.39914 | 2026-02-28 04:14:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ae7f5b83-371c-3a65-b678-e9e6a70392b8 | -21.68173 | -56.32499 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68b2336f-6734-37d9-a35d-33bd226bea16 | -21.80158 | -52.72097 | 2026-02-28 04:14:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7124fadc-a1da-3b1d-acc2-f3d67e84cf9f | -24.68213 | -51.04569 | 2026-02-28 04:14:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 10746bee-d67d-312b-9d9e-90e04578a7c0 | -21.68741 | -56.32632 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aeb53c86-f23e-38ce-9278-82adf0dc1553 | -21.17414 | -56.4959 | 2026-02-28 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db23c288-8d64-3090-ab9f-17cb6c18d0c1 | -26.01526 | -52.70234 | 2026-02-28 04:14:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a29ec25a-43d3-30ac-ae5d-e05de87e1a37 | -21.69206 | -56.3246 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 54ec6d34-0fbf-3bf5-923f-8f147fa7ed37 | -26.02622 | -52.69152 | 2026-02-28 04:14:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 87153d69-e00f-3004-8a1e-61edf737fb42 | -21.6808 | -56.32151 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2da6fa5f-3efb-3636-9f0b-0debd4eefab1 | -21.6884 | -56.32205 | 2026-02-28 04:14:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1051b881-7b44-3619-b4ad-b718a75a6a46 | -29.97988 | -51.20422 | 2026-02-28 04:16:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| fa411be7-e46b-3f46-99f7-20788385b606 | -19.80399 | -55.0653 | 2026-02-28 04:42:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 918d52c2-ec6b-35bd-b9ba-5e2dc1f17a75 | -20.52717 | -50.83505 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| af9f85e6-8a28-33e2-b0d1-0d27da424fdf | -20.51326 | -50.83641 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9bc2e4b9-3537-37d6-9eb2-220b99c64684 | -20.52384 | -50.83447 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 89f93685-262d-3e54-85c0-326bbeb3a952 | -20.52441 | -50.83076 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 19c48e01-91f1-31d8-8e56-936ce41f5dbd | -20.5205 | -50.83388 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| abdabe61-2e16-3679-8b29-8a3b5ea55350 | -20.51717 | -50.8333 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 696ce40e-8517-362a-a9bc-68d8c4665782 | -19.80014 | -49.52963 | 2026-02-28 04:42:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b67db5c5-918a-3d94-a0a4-ccbd9b278073 | -20.5166 | -50.83699 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| 85a120e5-6f73-3057-be87-db41602bdae8 | -20.52108 | -50.83018 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 1736390d-5dfc-3e64-bbc3-c6dd17432e5c | -20.51993 | -50.83758 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| edcc9b7d-bed3-3655-8321-eb5b04a671f1 | -20.52326 | -50.83817 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7adbaf77-e3d5-3b18-b3b9-264b13274dc5 | -16.5869 | -58.21959 | 2026-02-28 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 43f84e79-ea57-3844-ab88-fa1e1de2e5ee | -19.79957 | -49.53346 | 2026-02-28 04:42:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 822e0c12-fb9f-3a30-94ff-d9f04583809c | -18.80906 | -51.61143 | 2026-02-28 04:42:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6bba1ec-68eb-34a8-a7b2-aed2b4e7c881 | -20.51775 | -50.82959 | 2026-02-28 04:42:00 | NPP-375D | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| b8d20069-08d4-3875-9475-8daf8abfe401 | -21.22996 | -56.25179 | 2026-02-28 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81729ea3-830b-3297-9a5e-8abff194f471 | -26.02555 | -52.69237 | 2026-02-28 04:44:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 20d2b7fa-f5e5-3a9c-b65d-b07c667f4c78 | -26.01374 | -52.70197 | 2026-02-28 04:44:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
