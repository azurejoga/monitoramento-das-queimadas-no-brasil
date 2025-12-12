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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04043371-0460-36b8-b9da-6b372c3f6135 | -7.56324 | -55.34643 | 2025-12-12 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a91dcc7-5e85-3772-95a7-412bb3559c6f | -10.3031 | -57.13676 | 2025-12-12 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ab4862b-69ca-3fed-925f-7f3565f4dc73 | -11.81078 | -56.96561 | 2025-12-12 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4752b9b2-f64b-331e-bffb-ad7c7703a357 | -12.41048 | -58.0413 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ec3299f-70ec-3f67-9da2-51182d155c2f | -10.2379 | -52.22195 | 2025-12-12 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e4fe437c-adff-3651-b62d-0657ffc22b35 | -12.4311 | -58.03773 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1a64916b-8a9c-3e26-a1f6-258618cd039d | -12.62716 | -58.09068 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b55fddb-ce16-3798-91fe-b5d25743bfa7 | -12.40105 | -58.03616 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 202997c0-9104-34c5-8dfe-701f1192c1a1 | -19.96599 | -54.80532 | 2025-12-12 05:14:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f1c87b2-c072-304c-a900-cdaf7a421cf5 | -15.95152 | -58.44832 | 2025-12-12 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ad1488c3-5b78-3e1d-917e-fae2a37e25ec | -15.97493 | -56.28217 | 2025-12-12 05:14:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4db740d6-f669-3bd4-8640-fb82d0745135 | -14.91749 | -58.14672 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| afd7379f-d0be-3b71-91de-81432204a0ca | -20.77808 | -54.41721 | 2025-12-12 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c54fae0-57bc-3b8f-afa6-5e0825ff0e09 | -14.90127 | -58.12598 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e51665ff-377c-335a-a811-2c4f3798f559 | -14.90519 | -58.12286 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8a568044-7c85-383f-84e1-ec9dcd1a0604 | -16.04148 | -58.44407 | 2025-12-12 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 73e98c46-600a-32c1-b006-256af1e3e147 | -20.87038 | -56.04944 | 2025-12-12 05:14:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 669340ad-7ec2-3719-a182-172a86af9496 | -14.91414 | -58.14616 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27636f53-8ba1-37a7-bd30-317e226e43cf | -14.89792 | -58.12543 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1867448c-7efd-3eb9-a393-b34b98bb19e0 | -14.89736 | -58.1291 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 69db61b3-3bea-300e-917b-3379895b2fb3 | -14.90575 | -58.1192 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8bc357e-742b-36eb-a371-3ee46322986b | -13.43161 | -56.83314 | 2025-12-12 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c24918b-1878-3ca0-b59b-152d1fcfe48a | -12.45084 | -63.63498 | 2025-12-12 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2b89ffe-a94c-356a-8eeb-992287e1ee72 | -14.07476 | -56.16807 | 2025-12-12 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ed55ee-7096-3e61-92de-e73d79d7ca6c | -20.46729 | -55.6037 | 2025-12-12 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00917c48-0e4d-32a6-879b-8e768b8d5478 | -13.88355 | -56.19263 | 2025-12-12 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bdb4071-70ef-366c-9fdc-05d04d4be5f8 | -12.4469 | -63.63427 | 2025-12-12 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cd0bc9d-e64d-3105-b235-549aca609a0a | -16.09901 | -56.75876 | 2025-12-12 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba242cef-da33-3432-8842-e3f135a6429b | -14.90854 | -58.12341 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2d355bee-7717-302e-a27d-979199bbbdc8 | -14.07537 | -56.16386 | 2025-12-12 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22e12508-8267-305d-af68-734565d6af7d | -14.90072 | -58.12964 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b6edbee3-ee21-3a6e-a8bd-b29e69874765 | -14.90183 | -58.12232 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9120cb2b-2985-34e8-aeea-09e98c3cf329 | -15.97554 | -56.27781 | 2025-12-12 05:14:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e4ce46bb-53e3-3e7b-b367-35bed9fab430 | -14.90407 | -58.13018 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b14a5b8-688e-33d0-a684-d35b9b304161 | -20.77377 | -54.41657 | 2025-12-12 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e51f3104-e5a7-3cd7-86b7-7faa40f2691f | -14.91469 | -58.14251 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bb2b746-c1a0-39b3-a1f2-56c65d5761e4 | -20.86648 | -56.04883 | 2025-12-12 05:14:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ae8229-a953-3104-9fc2-fcf2a57b171b | -14.07895 | -56.16439 | 2025-12-12 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a17bff2-d7f3-3f51-9d46-80eb396e9e1a | -14.90463 | -58.12653 | 2025-12-12 05:14:00 | NOAA-21 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bfb3acb0-afd9-3416-b372-dc4588bde9fe | -21.72696 | -56.58366 | 2025-12-12 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b40468bb-5b27-3191-ae80-c78191e8f51b | -22.95188 | -48.70843 | 2025-12-12 05:16:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7051e4cd-b5c2-3787-89c0-24886b31b11c | -22.95227 | -48.70301 | 2025-12-12 05:16:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15821d76-b140-3969-a541-ca269849b5e4 | -14.8941 | -58.1282 | 2025-12-12 05:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| aeafaae4-8b5d-3810-b5b0-28f6013c5672 | -2.4367 | -51.948 | 2025-12-12 05:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ca7de966-4bc8-3f5c-8a54-d5028c843880 | -2.4183 | -51.9484 | 2025-12-12 05:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8ad1ec3b-97ed-359a-abc9-24c75f9563c5 | -2.4367 | -51.9274 | 2025-12-12 05:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 03c3a9ae-4da3-3f0d-bcb2-c1a8ea016838 | -2.4923 | -51.8027 | 2025-12-12 05:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b2e2dd8a-2dbc-3cdc-afa9-54226b685e57 | -2.4183 | -51.9278 | 2025-12-12 05:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f719da0b-3f04-3010-9a14-6aaaa3f7acc0 | -14.9134 | -58.1263 | 2025-12-12 05:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3ed1c0e3-17cd-3e72-834b-7e4470633cf4 | -2.4367 | -51.948 | 2025-12-12 05:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c952534b-8a0b-33b4-81ae-e572fb6a51bc | -2.4183 | -51.9278 | 2025-12-12 05:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ed04b2cc-7b4f-3b37-8f39-7407c4b81e24 | -2.4923 | -51.8027 | 2025-12-12 05:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| b50270a8-c8bf-3f21-b0ec-a00aaaabb857 | -2.4367 | -51.9274 | 2025-12-12 05:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 60df842a-ad7e-3b2b-9795-a8329ad39690 | -14.8941 | -58.1282 | 2025-12-12 05:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5590c98c-2207-35bc-a159-741a9a6646a3 | -12.4135 | -58.0292 | 2025-12-12 05:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| a1340149-ad6d-3415-9d37-8f9731e05669 | -14.9134 | -58.1263 | 2025-12-12 05:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2fb9dcb2-29d7-3417-82d2-005b2556fc31 | -6.02194 | -43.69908 | 2025-12-12 05:37:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ddc5e98e-3be7-3c79-85f0-35b370cde816 | -3.22388 | -42.07357 | 2025-12-12 05:37:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8c608827-085d-3a51-90f7-6a8a6f0682c8 | -6.46567 | -35.16979 | 2025-12-12 05:37:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 77412e70-4351-3c83-a652-8dd57355c977 | -8.0348 | -43.09732 | 2025-12-12 05:37:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 76418992-cfb7-3c3b-a809-ca1fd5230536 | -3.23397 | -42.07516 | 2025-12-12 05:37:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bdaa214e-1ff8-3447-adaa-799f344f5e9e | -3.43463 | -41.64461 | 2025-12-12 05:37:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 52e88a16-7b8d-33b7-9ba3-34c3832a08c0 | -8.02474 | -43.09572 | 2025-12-12 05:37:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 96123ef8-cf9e-3f1a-8582-0ed4fe66d5ab | -3.30917 | -42.52913 | 2025-12-12 05:37:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 19b91ecf-bde7-32ab-baee-3dbb7683c788 | -3.22625 | -42.06715 | 2025-12-12 05:37:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9f71fbf5-6951-3ee4-ae3e-e9e3795bdfff | -6.02487 | -43.70522 | 2025-12-12 05:37:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 719a8202-c5bc-3f22-b337-a8a569af0bd9 | -3.95943 | -41.51759 | 2025-12-12 05:37:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 310bc42a-e407-30fa-bf35-0cb027f8ffcd | -3.95422 | -41.52208 | 2025-12-12 05:37:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 57173b23-23a3-31a0-9803-137496016b5d | -3.96855 | -42.50761 | 2025-12-12 05:37:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 962354d8-d781-3c35-96a2-c06ed3ed4d69 | -1.75753 | -54.04158 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68f8c395-d993-3898-ab42-e49b5ab77091 | -1.19461 | -54.17762 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88e7b453-2318-3991-aa0f-ab398bef1a07 | 4.03251 | -60.63367 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aa14b10-c966-30a5-be96-ab45c0e85df1 | 2.8777 | -60.26042 | 2025-12-12 05:37:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b7555d2-4db4-3aa6-acd7-7681bfd58ae1 | -1.28711 | -53.16518 | 2025-12-12 05:37:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bed7f5e-1559-3751-b839-7d547e9f4895 | 0.70376 | -56.87742 | 2025-12-12 05:37:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66250a74-e4e9-3bca-884d-a261ad2a4dff | 3.29763 | -60.10708 | 2025-12-12 05:37:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67fcfb02-43de-357c-918d-d6d446592274 | -1.34126 | -54.60651 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1b117da-aa48-3354-b151-fa0ec7387146 | -1.69938 | -53.9327 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7affbf9c-b189-30c0-8a0d-8eb147bd6c0f | -1.37516 | -55.38565 | 2025-12-12 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32efe44c-2422-3994-a4a1-c56c52b19301 | -1.39081 | -55.34688 | 2025-12-12 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed189b4c-5d9d-374c-8005-be591b5448c2 | 4.03752 | -60.64362 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc909eba-6aad-339d-8419-3509de8bb8e9 | 1.12806 | -60.52781 | 2025-12-12 05:37:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d43a67c-9141-3656-afaf-82c2b4fb540b | 1.12863 | -60.53142 | 2025-12-12 05:37:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4314ff0d-8025-3abc-a38b-c4a84213f5f7 | -1.29259 | -53.16611 | 2025-12-12 05:37:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 718e2741-d1ab-3604-889b-2384226316b6 | 4.29884 | -60.85923 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26f55193-e4db-30eb-9939-1b838e9ab7ae | 4.29663 | -60.86668 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f776ed96-da88-36ca-9dd9-2e0a8aa61187 | -1.76276 | -54.0423 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d3b2e8c-14f3-3f1e-9d72-db205045db54 | 4.29552 | -60.85975 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47ea5ee3-6fce-3fcb-b34a-c399e5a8d713 | 3.22245 | -61.19906 | 2025-12-12 05:37:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cb6d035-93a2-3189-a877-5e56119e2aca | -1.34626 | -54.60715 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea434494-9df8-3774-ae70-e0dc4e20e951 | 4.29607 | -60.86322 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 247dc87f-71bf-31b8-a0db-114487dff2ed | 4.29995 | -60.86618 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 818d33cd-6c73-3a4f-bca6-46169d1c9c95 | -1.11629 | -53.69009 | 2025-12-12 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81e8c38b-d739-3c4f-9f15-0fb125b6511c | 3.30497 | -60.10956 | 2025-12-12 05:37:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e7bd8e8-eb5f-3bcb-8b31-f644f7279baf | -1.7577 | -54.03995 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6463d36c-85ee-3a59-be6e-3f7d73ac83e1 | 1.12524 | -60.53196 | 2025-12-12 05:37:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 159273eb-a5f8-3f93-abfe-7d8d91808b93 | -1.11098 | -53.68941 | 2025-12-12 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5b0a19d-af0e-3463-b418-d2034f5ce101 | 4.2933 | -60.86718 | 2025-12-12 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36471676-430d-34ec-b76e-c70dbcfc39df | 2.90717 | -60.92183 | 2025-12-12 05:37:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a0c7a12-c3ce-3ffb-84bf-b51465217f1c | -1.70466 | -53.9333 | 2025-12-12 05:37:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
