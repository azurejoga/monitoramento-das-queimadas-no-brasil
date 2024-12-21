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
| 961ab289-319f-3d37-ab31-a97f5d9c61a5 | -2.89825 | -54.50002 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad8605cb-4d87-319a-8793-f47d6b31b31c | -2.89958 | -54.49842 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7c2ab0e-3109-38cf-94ee-2661fc5b1466 | -2.06192 | -52.06027 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12682a99-7c7b-3e42-a5e9-03620b5fa652 | -2.89868 | -54.49709 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86a02984-4a78-3df8-8b60-2ab6fb51027d | -0.3521 | -50.08008 | 2024-12-21 05:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d487562b-49bb-3a8d-8632-72af971419f1 | -1.29201 | -53.13272 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b548f16-d04d-3efe-a226-dc4777c59adb | -1.29371 | -53.13297 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6fcf42d-c2c7-3c68-b340-18b11dffd918 | -1.29423 | -53.12952 | 2024-12-21 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e38c531-b8b8-39c2-bb63-f240f332323a | -1.34531 | -53.85117 | 2024-12-21 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdb53dc4-0ae4-3105-a42b-ca118be156a2 | -2.90375 | -54.49776 | 2024-12-21 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca415aaa-fb59-3549-ae7c-4215bf939c78 | -0.35122 | -50.08554 | 2024-12-21 05:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cd254b9-600e-34b6-9746-dca397379965 | -2.07353 | -52.05152 | 2024-12-21 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 772220eb-2c61-3098-b7c7-3076838b5dbb | -10.73932 | -62.82222 | 2024-12-21 05:33:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3798aac5-f898-3997-aadc-a4c261ec3494 | -9.93246 | -65.09885 | 2024-12-21 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d19175-7d5c-389b-b722-794e2d34ba86 | -9.94119 | -65.21267 | 2024-12-21 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 375ad553-681f-39b1-b22d-86eb755c9ab1 | -9.93523 | -65.10292 | 2024-12-21 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39c1877b-173f-35e3-a907-88383b80ea10 | -10.32297 | -63.62597 | 2024-12-21 05:33:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2aec25cf-fe28-36c7-9061-006fee650646 | -9.77001 | -64.85983 | 2024-12-21 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 518f7e73-f388-30da-9265-1c74757c9192 | -10.3263 | -63.6265 | 2024-12-21 05:33:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ada2c8f3-c20d-31fe-afdc-d9dbad3bae18 | -10.73591 | -62.82169 | 2024-12-21 05:33:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8de6bf0f-61f6-3535-bf00-8f48f6793532 | -10.73648 | -62.81797 | 2024-12-21 05:33:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3387ed99-09f1-3dec-bb5a-6f7c6c182b6b | -9.77652 | -64.86116 | 2024-12-21 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3fe1266-5926-30bd-950d-76b724a2c391 | -10.7325 | -62.82116 | 2024-12-21 05:33:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce2a6d73-f3e3-3552-9ce9-e9afe1bdc2f5 | -10.73974 | -62.82215 | 2024-12-21 05:33:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4478f938-f7b1-38a7-a0bc-bf85d70346e9 | -15.08628 | -59.62916 | 2024-12-21 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f2150a-0e0f-30bb-9980-20968b1a0511 | -11.98131 | -63.60875 | 2024-12-21 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9f08ad8-b7b8-390f-8f1a-05924d92b818 | -15.08684 | -59.62505 | 2024-12-21 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e957197d-c1a8-3e72-b059-94ff90ba5884 | -12.01286 | -62.7994 | 2024-12-21 05:35:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17093b96-2f2f-39f3-90c5-920a6c2221a2 | -14.49141 | -59.85994 | 2024-12-21 05:35:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff15f2ad-4df4-3e74-a9db-1d90567976f2 | -12.18899 | -64.06499 | 2024-12-21 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80990ca5-c2d9-34b2-8626-039e885b265c | -12.1862 | -64.06089 | 2024-12-21 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c958f05c-c5a9-33f1-b65f-2a33aca27f72 | -15.33138 | -60.01741 | 2024-12-21 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fbaba17-c160-3c01-9f60-461a728a77fd | -12.01343 | -62.79558 | 2024-12-21 05:35:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fcd9d83-045b-39f8-928d-a89fabe3ffd2 | -12.01228 | -62.80321 | 2024-12-21 05:35:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 042b3eeb-a73f-344a-9165-e80fc7b314bf | -12.01171 | -62.80703 | 2024-12-21 05:35:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c1e0a47-5ccd-3fb3-9559-4c44161dabb6 | -15.08567 | -59.62712 | 2024-12-21 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cb343c4-cd3e-3e61-beca-9f0399324a6c | -12.18674 | -64.05733 | 2024-12-21 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4655f3ab-b5e8-3dc2-9256-1eb32af0b4b4 | -12.18953 | -64.06142 | 2024-12-21 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f186986b-0596-3594-a658-fdf5a5267622 | -15.08203 | -59.62854 | 2024-12-21 05:35:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c678d4-8f02-3f01-9631-fdf5adbb0482 | -11.97794 | -63.60821 | 2024-12-21 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f22ae317-3bcb-3efc-bcf8-8d25c5afd087 | 4.45339 | -61.02581 | 2024-12-21 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc355ff8-3e4c-3efc-95e8-3b8a40cd07fb | 4.45468 | -61.03317 | 2024-12-21 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 855596e2-a755-3dfd-975c-0dfad9e7c005 | 4.44737 | -61.03151 | 2024-12-21 06:24:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c6cf101-ff5f-36af-a6ea-8390486cd79b | -2.8637 | -42.0012 | 2024-12-21 12:50:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2155a443-bf84-32d4-b924-2496837c4ecc | -2.8637 | -42.0012 | 2024-12-21 13:00:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 7f94b7aa-231d-3104-81b7-634dcd14ead9 | -7.33 | -39.97 | 2024-12-21 13:00:00 | MSG-03 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| aa1429bb-230b-39e5-897f-661a5df09030 | -3.4803 | -42.0212 | 2024-12-21 13:20:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 55f69787-295e-3b21-be0d-f34be179f085 | -3.0126 | -42.1138 | 2024-12-21 13:30:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 13cbf718-9a6d-3f45-8806-71ba5fe26a72 | -3.7053 | -41.9146 | 2024-12-21 13:50:00 | GOES-16 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| eff2375b-d0b2-3594-aefd-782467623520 | -4.9272 | -41.3358 | 2024-12-21 13:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 4527ccd9-733e-322b-9260-7098f70a2bd4 | -4.4282 | -42.89 | 2024-12-21 14:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 26f695c1-3185-3edb-b005-2a68b2f1d5f2 | -3.3144 | -41.5998 | 2024-12-21 14:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| d3ccbe53-dcb0-3925-ad80-77e278bc0285 | -4.17 | -42.41 | 2024-12-21 14:00:00 | MSG-03 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1d4b032-6041-35cd-afa0-730951380473 | -4.2 | -42.46 | 2024-12-21 14:00:00 | MSG-03 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 946ee409-a5aa-3e4c-a5ac-5817501d57bf | -4.17 | -42.46 | 2024-12-21 14:00:00 | MSG-03 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c1ab9d01-cfe9-3fdd-b92a-111d491f970a | -4.2 | -42.42 | 2024-12-21 14:00:00 | MSG-03 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee47a8c0-f37a-3e19-bb3c-eebf129164de | -4.9272 | -41.3358 | 2024-12-21 14:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 3283d497-37e1-3f3b-9179-c2f2a6ae252e | -4.4282 | -42.89 | 2024-12-21 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 771fda9b-a220-3827-bca0-9065449d1af3 | -2.4565 | -45.9236 | 2024-12-21 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a0a5cf45-ca80-375a-aa84-371270a31621 | -2.142 | -45.642 | 2024-12-21 14:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7ae7db6b-ee1c-3778-a555-7bdb3f37d2dc | -3.0311 | -42.1604 | 2024-12-21 14:30:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b0ddc1e4-6904-3144-8bf8-1f997f3ff6a6 | -3.0312 | -42.1367 | 2024-12-21 14:30:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |


