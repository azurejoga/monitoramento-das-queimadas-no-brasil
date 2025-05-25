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
| 0c90778b-627f-303b-900c-b489712d2aa4 | -7.2025 | -43.1171 | 2025-05-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 2c86d7f1-b110-34ad-9d97-5cf39fdeea55 | -7.6386 | -46.103 | 2025-05-25 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f014e607-9741-38cd-bada-3f3962de4043 | -20.9398 | -56.5998 | 2025-05-25 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 164c58a6-6e70-3a6e-bc70-86b7d422e7be | -8.07 | -43.1216 | 2025-05-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 75672967-bed1-30a3-aff3-0a35f772ede8 | -10.8213 | -56.9604 | 2025-05-25 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e4bbc4d7-b2f4-3664-8361-e038da112e50 | -7.6574 | -46.1013 | 2025-05-25 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| fca18fa6-7ca1-3d00-b2cc-e0ca3a153cbc | -7.2025 | -43.1171 | 2025-05-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 39cacdd6-1266-3e26-b4ef-ca224428fce9 | -8.0696 | -43.1452 | 2025-05-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| f1bbf71f-5620-3033-a1b5-68dfe78c8f14 | -7.6386 | -46.103 | 2025-05-25 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 393020a3-4774-35d2-a445-5161ffec71d6 | -8.0507 | -43.1472 | 2025-05-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| dbd77fc7-a72a-3c90-bb30-7e5f3fcf7347 | -7.2214 | -43.1153 | 2025-05-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 5fcd1ca8-6dd4-3ca0-a054-0ee3137faf8c | -7.6762 | -46.0995 | 2025-05-25 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 090cd7d7-218a-35c2-bace-a9bc7b530d03 | -20.9398 | -56.5998 | 2025-05-25 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 87ae960f-ef8a-34a8-9876-68e7a12dcf15 | -7.6386 | -46.103 | 2025-05-25 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 9fa82997-b87d-3090-80f4-d20a24fe591b | -7.2214 | -43.1153 | 2025-05-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| a7acb003-fe51-368a-8341-839f11b09783 | -8.051 | -43.1237 | 2025-05-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| a854081c-a5ec-39b0-adfd-b39ee9910d77 | -8.0507 | -43.1472 | 2025-05-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 4ae06f93-8ad3-3a5b-8db7-b4c6bbae7e9f | -8.07 | -43.1216 | 2025-05-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| e5d48024-96ca-3f67-ac94-4eb8da1b7d9b | -20.9398 | -56.5998 | 2025-05-25 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c17e4613-ddce-38b2-9c56-23de82abb9e6 | -7.6574 | -46.1013 | 2025-05-25 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 42df232e-c037-3b41-82a4-e69e07f5c93a | -7.2025 | -43.1171 | 2025-05-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| b4b6a587-cf4f-34ac-abad-f5c00274a79e | -8.0696 | -43.1452 | 2025-05-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 4d22ba41-abbf-3d31-a8bc-88c3491ba8ec | -7.6577 | -46.0788 | 2025-05-25 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5d0907af-7fbf-3c40-9345-2cb03a600519 | -8.0507 | -43.1472 | 2025-05-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 94340a76-53d0-3344-aea9-e4d75a22c512 | -7.2214 | -43.1153 | 2025-05-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| eb0012d8-f582-3105-a1ab-9759751b1e04 | -8.051 | -43.1237 | 2025-05-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| c2b4dc8f-a990-30a1-bee7-2194ffb3a1fc | -7.6577 | -46.0788 | 2025-05-25 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| be9971d0-a8e6-3eb1-8960-5eccf275929c | -7.2025 | -43.1171 | 2025-05-25 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| a0907dc4-5f0e-3784-9cf6-36aa841bd56a | -20.9398 | -56.5998 | 2025-05-25 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d787004c-b056-3f22-bace-64a3c6640b7f | -8.0696 | -43.1452 | 2025-05-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| f9feef3d-a44d-3ef8-a013-1f8617a85a05 | -8.07 | -43.1216 | 2025-05-25 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 96d4eada-ea53-3176-8a1b-8c461b83905b | -7.6574 | -46.1013 | 2025-05-25 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 4671d1e4-9944-3570-8427-1aad70463e8d | -7.6574 | -46.1013 | 2025-05-25 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| a919a20a-63c7-3b5c-98ee-0cce47c70d76 | -7.2025 | -43.1171 | 2025-05-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| a6406058-df16-3339-a684-ca03ac90bade | -20.9398 | -56.5998 | 2025-05-25 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1ed7371d-b2e2-335d-ae7e-3c0b4b580698 | -7.6577 | -46.0788 | 2025-05-25 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9936c1f0-29a9-33f2-af92-b03c40e7dbbe | -8.07 | -43.1216 | 2025-05-25 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| a318cb37-7505-398e-a989-68d578c1d943 | -8.0507 | -43.1472 | 2025-05-25 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| e8d910db-6a9d-3731-adac-3c2131735dfb | -8.0696 | -43.1452 | 2025-05-25 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 753a5472-cf10-36c8-a25b-a6693c0e365d | -7.2214 | -43.1153 | 2025-05-25 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| f42df52f-bee3-3820-8c24-4f1aec07a31b | -7.6574 | -46.1013 | 2025-05-25 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 89486f9a-ab07-3a18-9e64-37a3bfd42f81 | -7.2025 | -43.1171 | 2025-05-25 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 7bb150ee-298a-3f1b-bbc6-f0175f91a34a | -7.2214 | -43.1153 | 2025-05-25 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 7c356ba1-46e2-301e-a886-7bc4990cd5e5 | -8.07 | -43.1216 | 2025-05-25 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| ea7a2c8c-2d02-38a9-8202-c2ed1cce2f25 | -7.6577 | -46.0788 | 2025-05-25 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 7f9699e2-6c25-3f57-9cb1-d36e7b23ab37 | -20.9398 | -56.5998 | 2025-05-25 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 6ba664f3-e2a1-3a02-b76c-0db6029529fb | -7.6577 | -46.0788 | 2025-05-25 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 6f725500-e857-3235-8eaf-addea7d77da7 | -7.2025 | -43.1171 | 2025-05-25 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 12e504d0-d1d2-3b73-9746-c1e14eac628e | -7.2214 | -43.1153 | 2025-05-25 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 74e7eafc-3137-36f3-900c-8d31a6e1d37e | -7.6574 | -46.1013 | 2025-05-25 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 9c8e52f6-ccbf-3d90-8c85-01735d89d22b | -7.6574 | -46.1013 | 2025-05-25 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 2285dea2-3eb0-3caa-bc65-e1a4f6af9b6b | -7.2214 | -43.1153 | 2025-05-25 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 33171564-6e67-3cba-9713-5fb14eb4b59a | -20.94603 | -56.58874 | 2025-05-25 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6edb45ff-2e0d-3ff0-a185-47ac225644d0 | -20.9365 | -56.59042 | 2025-05-25 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 9222e467-9ab7-3c85-b5d1-52587c4155d3 | -20.93822 | -56.60143 | 2025-05-25 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 3702bd52-6f2b-3f35-a2b4-533b36819bac | -19.88053 | -54.36886 | 2025-05-25 01:32:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 12724a3d-3cfe-35d7-84dd-5ac293438040 | -20.94774 | -56.59977 | 2025-05-25 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dbc4488d-2c66-3b2b-9b41-69e71c731f91 | -10.82526 | -56.94792 | 2025-05-25 01:34:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 48d849b1-29e5-3cc2-ac22-f0029af3fc64 | -14.03884 | -55.13611 | 2025-05-25 01:34:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| dbf47be0-153e-3a84-afb9-9e25f9a0fc24 | -13.15535 | -56.81835 | 2025-05-25 01:34:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3831ea3e-1726-3488-84aa-b4e98f0e3f82 | -11.99517 | -57.21118 | 2025-05-25 01:34:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 90b113d1-db9f-30ea-a692-515fe3e7622f | -10.82748 | -56.96207 | 2025-05-25 01:34:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| edc595c7-c6df-344e-b626-18090c974cda | -13.15327 | -56.80487 | 2025-05-25 01:34:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 014ee34b-f37a-32e6-b79e-5b8499775a5b | -13.00072 | -55.97864 | 2025-05-25 01:34:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| bd7abbb2-449a-3370-b7d2-7fe49cf978bd | -11.73731 | -62.72958 | 2025-05-25 01:34:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a0023d59-3390-337d-9d53-44f57d4e1bc2 | -9.58625 | -63.50402 | 2025-05-25 01:37:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b56e7fef-0900-35eb-b49a-16ad8ba39eab | -9.57708 | -63.50533 | 2025-05-25 01:37:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8b233cf-53a4-39b7-8e34-ff5a4fcb832f | -7.2214 | -43.1153 | 2025-05-25 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| d9b20db6-8571-344d-8519-8bb7828a59c7 | -20.9398 | -56.5998 | 2025-05-25 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 57.5 |
| addd2460-6437-30af-8e16-490240e3c6ba | -7.2025 | -43.1171 | 2025-05-25 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| e1145a83-fe8a-3682-92dd-e7c3749998a7 | -7.6574 | -46.1013 | 2025-05-25 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a5cefa28-9282-36ad-9534-00dbb1a83535 | -7.6574 | -46.1013 | 2025-05-25 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 875842c6-1486-36d8-af93-6aec734d509e | -20.9398 | -56.5998 | 2025-05-25 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 47.8 |
| fe450a29-efde-3692-af95-9859f9a26cb2 | -20.9356 | -56.587898 | 2025-05-25 01:55:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6431160b-e736-31f5-ae62-0d91f268ed59 | -20.945299 | -56.584999 | 2025-05-25 01:55:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb5716a3-4399-382c-92a2-f77c8cc03dab | -20.9494 | -56.600399 | 2025-05-25 01:55:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| be525836-0217-3e8d-a65a-e04461006980 | -20.9398 | -56.603401 | 2025-05-25 01:55:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 84820124-63ca-35c1-ab52-a34df5155816 | -7.2214 | -43.1153 | 2025-05-25 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 398fc808-d1ba-389f-94aa-a59647d124a6 | -7.6577 | -46.0788 | 2025-05-25 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ef2ca421-3e53-3e2d-a541-8a29782ba1b1 | -20.9398 | -56.5998 | 2025-05-25 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 080bbf2c-1c5f-3834-a75a-a3e38a562dd9 | -7.6574 | -46.1013 | 2025-05-25 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 3edd1a59-3eba-3641-843b-a34e9357598a | -19.9593 | -49.1096 | 2025-05-25 02:10:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b5663863-8dd6-3193-a58e-472304eb0064 | -7.2214 | -43.1153 | 2025-05-25 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| a426dfc7-c833-369f-aae9-518766e7c9f8 | -7.6574 | -46.1013 | 2025-05-25 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| d192dc83-6cce-334e-b342-732dc0e862d2 | -7.2214 | -43.1153 | 2025-05-25 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.8 |
| 3e53949b-5d17-3a19-a4be-a0a197a2e63f | -7.6574 | -46.1013 | 2025-05-25 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8883b8d4-5d1a-34a7-ba8b-bfcd2b8ed0f3 | -7.2025 | -43.1171 | 2025-05-25 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 5c7ec114-9c1e-3c3e-bd34-9e810ca9b371 | -7.2214 | -43.1153 | 2025-05-25 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 8bcf5539-b1a8-32eb-9b8d-054b7a4153c3 | -7.6574 | -46.1013 | 2025-05-25 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 96e1229d-79cb-312d-8358-023703e28d02 | -7.6574 | -46.1013 | 2025-05-25 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c742cdbe-128b-3cd1-9f9b-df60dd752fce | -6.56064 | -44.49588 | 2025-05-25 03:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6420351a-9104-3007-8071-1aa73a7e4e17 | -6.55603 | -44.49362 | 2025-05-25 03:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a38e11b-64a8-3a8c-a47c-2a565ef535c4 | -6.94854 | -42.80756 | 2025-05-25 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6cb8a945-dc8f-385f-92a4-ee7c3548d156 | -6.55743 | -44.4863 | 2025-05-25 03:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c013a670-f019-355e-9e0f-3b00f299f30f | -6.55374 | -44.49305 | 2025-05-25 03:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3574f03-55d3-3785-8e2a-ea878e7328d5 | -6.94876 | -42.81031 | 2025-05-25 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3dd15b21-9db1-350b-b337-d5f9400b64c3 | -5.58383 | -43.45693 | 2025-05-25 03:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f067e29-6dd8-36bc-90bc-b0aa5e361642 | -6.95521 | -42.81167 | 2025-05-25 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f96165bc-b65b-3d84-9efb-7245cca2a1cf | -6.95498 | -42.8089 | 2025-05-25 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dda5645e-8980-393b-b9eb-190cc40ee037 | -8.06775 | -43.13353 | 2025-05-25 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README3.md)
