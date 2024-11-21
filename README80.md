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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7487e6ef-5e3c-3584-96cf-96d501c3c6e0 | 4.31101 | -61.25404 | 2024-11-21 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd82abde-2139-30a3-849a-0a5b0d65b775 | 4.31153 | -61.25708 | 2024-11-21 06:09:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29f5e915-582d-349d-9cea-6ddb46031e64 | -2.0259 | -54.5289 | 2024-11-21 06:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 638b8c2f-8823-3b9d-b973-7847199370e1 | -4.2575 | -46.1188 | 2024-11-21 06:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 36fa806a-3cf5-3f74-b921-c8a29a8c3573 | -4.2388 | -46.1197 | 2024-11-21 06:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 55768f59-a4b9-3503-9dd2-cbf4424efce4 | -4.5799 | -48.0349 | 2024-11-21 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ef0b97ef-d665-351d-bf67-8b4d9c2ec3fb | -3.2951 | -53.8395 | 2024-11-21 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6e24b7a8-8a68-3ef4-95fb-dfcf38cfe923 | -4.58 | -48.0132 | 2024-11-21 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 19109cf8-9533-3bf4-89c6-42feb21ac41a | -3.2767 | -53.84 | 2024-11-21 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7499d6be-fadf-3627-a134-be147372c43e | -3.295 | -53.8597 | 2024-11-21 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 46650162-ffd7-3ecb-b536-ba785ccc6256 | -5.14204 | -60.38324 | 2024-11-21 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4e238f8-e0ab-387a-aaf1-354bf46d0f3b | -5.1354 | -60.38242 | 2024-11-21 06:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e40bca1-1005-3588-b739-2de74cac6a3d | -3.2951 | -53.8395 | 2024-11-21 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3704db31-aafb-35a5-b04c-c28bffc6afa9 | -3.0724 | -45.1856 | 2024-11-21 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b459a0c0-f490-3e7b-bf7d-573b21ab32ef | -3.2767 | -53.84 | 2024-11-21 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9c35bbcd-9588-3103-8bde-7f17eb8cabd2 | -4.5799 | -48.0349 | 2024-11-21 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 186f8376-3df3-35e9-bd5a-db96db8cf867 | -2.0258 | -54.5489 | 2024-11-21 06:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 87f36515-1753-324f-9253-0609e0ee0342 | -4.58 | -48.0132 | 2024-11-21 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8100a24e-5974-3b66-b5ca-d12a193a4583 | -3.0538 | -45.1863 | 2024-11-21 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 1ae8e256-31e2-32b4-a112-7bbc0f392192 | -2.0259 | -54.5289 | 2024-11-21 06:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 480f7a8f-9e71-3bb5-a178-1ec31f269c34 | -4.2388 | -46.1197 | 2024-11-21 06:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 512446ba-6427-3019-af6f-80c79c8bc675 | -3.2951 | -53.8395 | 2024-11-21 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 30a05425-e1a5-38d1-9c43-b974ae16706d | -3.2767 | -53.84 | 2024-11-21 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 836990d5-5b57-3ebb-9290-3a74e5bc16f9 | -2.0259 | -54.5289 | 2024-11-21 06:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5a378b2b-97a6-3d2d-a39a-b9ab504b0695 | -3.295 | -53.8597 | 2024-11-21 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fad605e0-97e8-3498-9d28-3f4e2a2384a6 | -3.0538 | -45.1863 | 2024-11-21 06:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8c991ccd-d4f6-3599-9db1-fda3047cee6c | -4.58 | -48.0132 | 2024-11-21 06:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ca4663fe-adf5-3f4a-a50e-6de1cdb3d61d | -4.2575 | -46.1188 | 2024-11-21 06:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| b9c037f0-9468-3eba-93e0-62962f38b3da | -3.2951 | -53.8395 | 2024-11-21 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7dc13a6c-3f5e-3749-bf1d-55aad0d5d7db | -3.2767 | -53.84 | 2024-11-21 06:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ee33d40e-a167-3fbc-9a38-49da0e0ca080 | -2.0259 | -54.5289 | 2024-11-21 06:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a4c36501-5ad7-3c10-9e79-162cd1e3a7a1 | -4.58 | -48.0132 | 2024-11-21 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c9eb83b2-b267-3dd5-b488-78c7de33082d | -4.2388 | -46.1197 | 2024-11-21 06:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 5b140c15-b1b0-3b38-8b19-5c76c005c140 | -2.4768 | -45.4309 | 2024-11-21 06:50:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fd3b54db-f45f-3dcc-9f5c-006b2b511c04 | -4.58 | -48.0132 | 2024-11-21 06:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c0e1c399-efc8-3d70-ad92-a484c6f7fd54 | -3.2951 | -53.8395 | 2024-11-21 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 93035671-676d-3826-8ace-2857df625e89 | -3.295 | -53.8597 | 2024-11-21 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 94e7d56f-1cdd-3606-81ab-6a30406b6bcc | -2.0259 | -54.5289 | 2024-11-21 06:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 182ba6b9-44d2-30ca-bf0f-06b5921f8cda | -3.2767 | -53.84 | 2024-11-21 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c60e5092-44f5-39bc-819b-f62af6578977 | -3.2768 | -53.8199 | 2024-11-21 06:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d215e5e5-bc18-3eb4-b1dc-3dbd75570742 | -3.2767 | -53.84 | 2024-11-21 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2d79adee-1738-399b-9dcd-16e0d5a63a01 | -3.2951 | -53.8395 | 2024-11-21 07:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5398511b-52e8-3bbb-b9d0-bea476a94cb7 | -4.58 | -48.0132 | 2024-11-21 07:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f6c93c8e-0bb6-3f03-9670-c2cc401fa728 | -2.0259 | -54.5289 | 2024-11-21 07:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 75135221-8c50-386f-a11f-7f5280126f3b | -2.0259 | -54.5289 | 2024-11-21 07:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8352549c-5584-310c-bf57-d9a2277714b5 | -3.2951 | -53.8395 | 2024-11-21 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5456ab9b-d34c-332b-a75e-390e706dae87 | -3.2767 | -53.84 | 2024-11-21 07:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4c5168ee-7bf5-30b6-b2f2-6b9d5012e7f6 | -4.58 | -48.0132 | 2024-11-21 07:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b67262f0-1bf5-3823-b63f-70aef72f1d79 | -2.0259 | -54.5289 | 2024-11-21 07:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| dace5099-7ebc-3110-abf8-5966d682792c | -3.2767 | -53.84 | 2024-11-21 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 29572906-76da-364b-a606-ff5bd06e5778 | -3.2951 | -53.8395 | 2024-11-21 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3779bd5c-5f3d-3be0-8c55-d59f1aaadc00 | -4.58 | -48.0132 | 2024-11-21 07:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 08b8783d-b78a-3ae3-ad51-b8ef3569447b | -3.2767 | -53.84 | 2024-11-21 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f879d42e-a9f9-3fbc-9b69-e18e5672c514 | -2.0259 | -54.5289 | 2024-11-21 07:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 128a989f-5156-3cd3-80ca-51f433229bab | -3.2951 | -53.8395 | 2024-11-21 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6e1d6fa0-13c4-3ea0-aef8-055b29bc17c2 | -3.2767 | -53.84 | 2024-11-21 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| bc779498-2bfb-3394-a2ea-3744fb1867c4 | -2.0259 | -54.5289 | 2024-11-21 07:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 339b3081-49ae-3fd1-bce7-968b761232d6 | -3.2951 | -53.8395 | 2024-11-21 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b44d3419-4012-31b1-84f2-4a30b71fab4f | -3.2767 | -53.84 | 2024-11-21 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5d6aaf53-1a39-3853-a9a9-cd5aa2d27f32 | -3.2767 | -53.84 | 2024-11-21 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9181c922-b768-3231-912a-c532a198751b | -2.0259 | -54.5289 | 2024-11-21 08:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6d02e637-e088-36c4-abbf-885a203f88f3 | 0.4326 | -50.7954 | 2024-11-21 10:50:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2b2f1c93-3368-3c54-9e67-fcb2a69c11ac | -1.4699 | -47.5961 | 2024-11-21 10:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5af34b8f-bc5c-3756-a343-d1cfe6df67f1 | -1.9882 | -47.4773 | 2024-11-21 10:50:00 | GOES-16 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 889fb03b-ba5a-3373-a2a6-06ba48d8fd7b | -2.0259 | -54.5289 | 2024-11-21 11:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 9b8beb96-fdd6-3275-85d3-c4c855855afb | -2.0259 | -54.5289 | 2024-11-21 11:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 62b1fa94-5e29-3680-b0a8-9d6c44658551 | -2.0259 | -54.5289 | 2024-11-21 11:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 6ad5c464-d605-3943-a074-27e8520a27c0 | -2.0259 | -54.5289 | 2024-11-21 11:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| aef76df3-db5d-34f4-bed3-eef43e3da06b | -3.5547 | -42.0888 | 2024-11-21 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| f9faec78-8b74-31d0-ae16-c98943bd33e8 | -3.5734 | -42.0879 | 2024-11-21 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| ab1f592b-2db5-3ee6-80dc-a0a9e27d19d5 | -3.5547 | -42.0888 | 2024-11-21 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| bb066fc7-f1a1-38cf-bb99-419c9dbfb932 | -2.0259 | -54.5289 | 2024-11-21 12:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| dca34477-c86b-37dd-b5cd-5069c96b5658 | -3.2951 | -53.8395 | 2024-11-21 12:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a1d8714f-4e31-3226-b1f5-07a0bec1383f | -3.54 | -41.98 | 2024-11-21 12:00:00 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d040952b-107b-3563-8813-d0f4f0c45b70 | -2.0259 | -54.5289 | 2024-11-21 12:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 51339354-75fb-347f-94b0-caa7ef9c8c7f | -2.0259 | -54.5289 | 2024-11-21 12:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 23eef7c6-072b-3b4b-9c80-4230b4a534ca | -2.0259 | -54.5289 | 2024-11-21 12:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 48313f85-703b-38a4-8089-1880f2c71fa5 | -3.2951 | -53.8395 | 2024-11-21 12:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4acaebcc-4ce4-30e7-88d0-d31d7b1e089b | -3.2951 | -53.8395 | 2024-11-21 12:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4578b92c-ab4f-3397-b403-b525a72a802f | -2.0259 | -54.5289 | 2024-11-21 12:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| e9566857-2616-3673-935f-42b9dcab4018 | -7.7999 | -37.8542 | 2024-11-21 12:40:00 | GOES-16 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 3a061844-f9dd-31a7-acfe-812a5196ae9c | 1.34735 | -56.01626 | 2024-11-21 12:46:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| f418eaab-2b1a-380b-8d84-2245a8a6bfa9 | 0.39555 | -50.83876 | 2024-11-21 12:46:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 511ed0b5-56ea-342d-ac2e-a6777b80b2ca | -0.25592 | -48.51393 | 2024-11-21 12:46:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0435b6a8-53de-37ce-a337-7aca51d28249 | 0.40385 | -50.82609 | 2024-11-21 12:46:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7fc83e8d-3ff7-3c1c-926e-93bf632a7113 | 1.38995 | -56.00315 | 2024-11-21 12:46:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| eef7f8a0-2fd4-3257-b60b-76034ffcc739 | -1.25532 | -49.26081 | 2024-11-21 12:48:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f0ab5f34-5d39-3053-b488-f3644a057fa2 | -5.12869 | -45.17221 | 2024-11-21 12:48:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c8c3fbee-9ed2-3582-89ff-fe2e39c9bbd9 | -5.01457 | -45.40746 | 2024-11-21 12:48:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 881d2fb7-1afa-3dc7-bd57-5e4d49c20f07 | -4.66441 | -46.52739 | 2024-11-21 12:48:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 148.4 |
| ff2923ea-8242-3bd4-85d5-e29b0ee70f0e | -3.69276 | -42.1324 | 2024-11-21 12:48:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 978d3c38-dc7a-39ce-9fc3-3c1a43f1b0d5 | -5.28727 | -46.16522 | 2024-11-21 12:48:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| d7a7e45f-67ff-33bb-bcf0-6fafc87db88e | -5.56258 | -46.89502 | 2024-11-21 12:48:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 908a7224-8b0b-369f-b493-fd798d2a6a93 | -4.09338 | -48.46838 | 2024-11-21 12:48:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 779a4bd1-4a87-3afb-8478-a14f98d4b338 | -2.94898 | -48.33513 | 2024-11-21 12:48:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f04bcf12-bb1d-3157-a70c-ea5c7c2e8210 | -3.52917 | -50.7543 | 2024-11-21 12:48:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| df34754e-3b95-3286-b719-34f654778720 | -1.51156 | -54.3936 | 2024-11-21 12:48:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| d04960a2-51f4-3ad1-a40a-891c20414e57 | -2.25026 | -49.21008 | 2024-11-21 12:48:00 | TERRA_M-T | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b8d0ea85-dc17-3991-996c-0d39eb70113b | -6.51223 | -47.28223 | 2024-11-21 12:48:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 865eb204-79fb-3dbc-bbea-9c4782d03064 | -2.94588 | -44.09191 | 2024-11-21 12:48:00 | TERRA_M-T | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 32.4 |


[Clique aqui para ver as próximas entradas](README81.md)
