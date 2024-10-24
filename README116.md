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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b158a5ff-5d1d-33db-bda7-f65d80e75741 | -14.3124 | -42.86009 | 2024-10-24 12:14:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 37290979-a13c-3808-ab9b-12c70398e2d9 | -13.86056 | -42.86168 | 2024-10-24 12:14:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 4c450a03-2aa5-314c-8c69-a6a520774a85 | -13.84498 | -42.71247 | 2024-10-24 12:14:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 5a90b447-9ae9-3c50-83e6-a5b7585589d4 | -14.77746 | -42.46485 | 2024-10-24 12:14:00 | TERRA_M-T | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| af945c9a-370a-3320-b635-45fa2d62e726 | -14.40012 | -42.40459 | 2024-10-24 12:14:00 | TERRA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d5f2f0ab-95c3-363e-9d62-d77d825a0a8f | -16.44839 | -43.59543 | 2024-10-24 12:14:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ab67fff4-127a-367e-a5e7-9604f1cad459 | -16.44674 | -43.6059 | 2024-10-24 12:14:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 596eb6cb-72fe-347d-aa51-59d1765d3c4f | -16.10401 | -43.62223 | 2024-10-24 12:14:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8c197e1f-caad-3cee-ac0c-2d9b5534aff8 | -16.10234 | -43.63288 | 2024-10-24 12:14:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9c19fb23-c5f0-38e6-8384-0824b6c189b1 | -16.0945 | -43.62067 | 2024-10-24 12:14:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 13d4da20-7bab-37bd-bf66-f45644767de7 | -16.09282 | -43.63132 | 2024-10-24 12:14:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 59cffa6b-a7e7-309c-a731-3995c2439aa2 | -16.08779 | -43.66333 | 2024-10-24 12:14:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| fbe0ee75-409d-345e-9926-607a875710ef | -16.08612 | -43.67396 | 2024-10-24 12:14:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 42e8ec3b-545d-3982-b25e-5d1b3521853d | -15.95187 | -43.47641 | 2024-10-24 12:14:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8fa79dbe-fd94-31c7-a5d4-a25fb1d66280 | -15.79015 | -43.2663 | 2024-10-24 12:14:00 | TERRA_M-T | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c01a87a8-0546-3361-849c-f9a816da8b11 | -15.48953 | -43.54379 | 2024-10-24 12:14:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 844bb1f6-bde7-3591-a3be-65445f743208 | -12.91773 | -44.36975 | 2024-10-24 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 58087497-25f2-3a7b-bc7f-9fd86200687a | -12.7188 | -44.3909 | 2024-10-24 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f1d6dbff-8ade-3ee6-bf9f-40fca837518f | -12.6089 | -44.43327 | 2024-10-24 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c061f4ea-51d7-3645-82e4-f424578fc5ab | -12.60425 | -44.42654 | 2024-10-24 12:14:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9a0c3bcf-2dbd-381f-8c1e-777ed1e17eb3 | -12.53111 | -43.38397 | 2024-10-24 12:14:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6ff85a15-8995-302a-b6ef-84c6aee666e9 | -12.52659 | -43.34859 | 2024-10-24 12:14:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 316dc42d-8379-3f72-9717-5067b0c00eef | -17.22474 | -45.33721 | 2024-10-24 12:14:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bb595fe9-65bb-3905-8e9f-fa5976b8b3e2 | -12.97939 | -46.30048 | 2024-10-24 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 04c02685-b6db-3fa8-a4b3-d4ad188344d4 | -14.48076 | -45.46633 | 2024-10-24 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 468bcb77-4de0-3463-958c-f48fab681b02 | -14.47832 | -45.48087 | 2024-10-24 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 865f0039-f67e-3066-9244-054b8c150a5b | -14.47762 | -45.4749 | 2024-10-24 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e78061f7-6930-3eb7-887e-2da821c7b200 | -14.04074 | -45.54177 | 2024-10-24 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ed2a8465-1bd9-360e-878f-bdc72442b89f | -13.65024 | -46.77039 | 2024-10-24 12:14:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 781b5ea4-a07a-3948-9642-5d0ba73dc2c4 | -12.7699 | -47.14778 | 2024-10-24 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 8faa8b66-0ea0-34a9-b87f-1a71975523da | -12.50791 | -47.28537 | 2024-10-24 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 1278545a-90b3-309e-86d3-60556cafd4e4 | -11.59918 | -49.83961 | 2024-10-24 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 1b3a282d-1fb0-3d4c-a79c-a5679f105b39 | -17.0184 | -57.5178 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 20aa7995-b81e-3581-b25c-b7caef654d17 | -17.0384 | -57.495 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| bc5fce6d-ca94-3979-a4f2-fe013953c912 | -17.0387 | -57.4745 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 9e59f3e8-c80c-3b38-b037-825b594e8906 | -17.0381 | -57.5155 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 01ab7ab9-146a-350f-bd1f-d4e2553c08e8 | -16.9596 | -57.5245 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 499964d8-7aef-31c2-9150-03de069ee317 | -17.0188 | -57.4973 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| b71732b0-3dc4-3717-8e37-fe82f3f0fb3f | -16.9792 | -57.5223 | 2024-10-24 12:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.1 |
| acca4c3f-f03e-322a-a3f1-daf7f4a181d2 | -17.7062 | -57.4774 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 7d2bea28-810e-304c-a049-106672b47918 | -17.764 | -57.5526 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| f3608528-00aa-387c-924e-cecb4077750a | -17.6865 | -57.4798 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.0 |
| d949f080-ebb2-3225-af56-1e7a0b5b1e3d | -17.6868 | -57.4593 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 170.3 |
| 4fabd4cd-fd44-34fa-b723-9d0359347fd6 | -17.7644 | -57.532 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 1fae0999-41e0-34a0-882e-432d4c8ff75d | -17.7082 | -57.3539 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 2563744b-16a6-3b79-bd8a-56a180e96b0c | -17.6671 | -57.4616 | 2024-10-24 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| fb5449d3-0726-306b-b456-11f9df4f971e | -17.9268 | -57.2447 | 2024-10-24 12:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| ddea3aac-10a8-3e79-98fe-cb360b92356e | -17.8427 | -57.5636 | 2024-10-24 12:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 22a0b992-02fd-362f-8541-ce0d4a8aa8d1 | -18.0837 | -57.3076 | 2024-10-24 12:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 0ffd6d48-9fd5-35eb-8dd9-9f2cb6b20aa9 | -18.0834 | -57.3283 | 2024-10-24 12:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 93ed3524-dfe0-3aef-96e9-125c574e2e63 | -18.0438 | -57.3332 | 2024-10-24 12:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| e64a8ec4-a6f0-34a5-84a7-c5d64c235493 | -18.2637 | -56.0603 | 2024-10-24 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 310.0 |
| 1b16e603-a74e-3774-95f6-27ac7ba5544a | -18.3199 | -56.2404 | 2024-10-24 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 20fadac1-9ac3-3813-a51e-acbf04262dbb | -18.2641 | -56.0394 | 2024-10-24 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 508.6 |
| 1651141c-bbcf-3a9a-b3e7-fca938a2d0dc | -18.2836 | -56.0576 | 2024-10-24 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| f09f932d-9196-35a0-8994-2ff38ff517e5 | -18.284 | -56.0367 | 2024-10-24 12:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 252.4 |
| d67f1b67-8442-3dd9-b426-9caa80bff61d | -19.6237 | -56.8549 | 2024-10-24 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 48168297-c5ea-33b4-a557-0ddd8e04b1df | -19.6438 | -56.8521 | 2024-10-24 12:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 58f3486a-ca35-34dc-af75-d4d57a017464 | -19.7065 | -56.7176 | 2024-10-24 12:16:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 24b6e590-c8e4-3cc7-aaca-e56c25a15192 | -17.0184 | -57.5178 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 7bf8b171-9422-360d-876c-37e225693f78 | -17.0188 | -57.4973 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 4d127e1e-bb04-3f81-a157-81c4127750ce | -16.9596 | -57.5245 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| d564d8b6-e4f4-3b2a-ad0e-3853558b0103 | -16.9792 | -57.5223 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.5 |
| 8074b441-5a4b-361a-bc2b-a67810d95f55 | -17.0381 | -57.5155 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 6f2e8f22-e2c5-341d-89c4-217a5a1df4c7 | -17.0384 | -57.495 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| d5068f29-73b0-38c0-a9c8-7dea3b84bc39 | -17.0387 | -57.4745 | 2024-10-24 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| bd57902d-3e39-353b-9284-3e7e934f910f | -17.7644 | -57.532 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| d17790d8-d53a-3b92-8093-cd4d7fcc3e5e | -17.7841 | -57.5296 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 47d46375-02d2-3611-ac2d-490407f6a579 | -17.744 | -57.5756 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 4ec4efe4-46f4-3539-afd7-1ebbd4160b7e | -17.6865 | -57.4798 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.7 |
| 63eda14c-89b1-3f5e-bd22-56e7ea6c2589 | -17.6671 | -57.4616 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 89ae76f6-1e93-3403-b0d8-ce779b09ee5f | -17.7082 | -57.3539 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 221efbff-7fb6-394c-9ac0-31b6751d0c84 | -17.764 | -57.5526 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 6fdb08c9-8634-3ff5-8a5e-83674e0a8f1e | -17.7062 | -57.4774 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| b88e58dd-e94b-3e63-8424-1b049ddff823 | -17.6868 | -57.4593 | 2024-10-24 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.0 |
| 58430458-d456-3736-8ecf-fb7cb429fed6 | -17.8226 | -57.5866 | 2024-10-24 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 36ef491f-b784-33e9-8f7b-b333b9b3cab5 | -17.8229 | -57.566 | 2024-10-24 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| c234f9ba-6273-37d4-ae45-0ab79204d2b6 | -17.8427 | -57.5636 | 2024-10-24 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 1be51159-3456-3d8f-b85d-f3a389de4c09 | -17.8423 | -57.5842 | 2024-10-24 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 1fae601c-863a-3f66-b683-52cedef40143 | -17.9268 | -57.2447 | 2024-10-24 12:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 5db412c4-3ea4-35ae-8708-5443280bcdad | -18.0837 | -57.3076 | 2024-10-24 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 92247707-4d5f-361e-811a-ee12b0a022c4 | -18.0841 | -57.287 | 2024-10-24 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 94e4210c-98ca-3f07-a8d4-63d7b729d80d | -18.0834 | -57.3283 | 2024-10-24 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| a4cbb582-3c13-37bf-8b21-075199772921 | -18.083 | -57.3489 | 2024-10-24 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 64036904-c7b0-34ce-a6eb-069a1be27975 | -18.0639 | -57.3101 | 2024-10-24 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 98ce44ee-8cd1-3d11-bda1-ba69b7019a83 | -18.1802 | -56.3008 | 2024-10-24 12:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| cd83772a-4abe-3bd2-9282-22145c6bcf97 | -18.2641 | -56.0394 | 2024-10-24 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 431.1 |
| c5a49911-42c7-3643-a7fe-124fc51fb859 | -18.2637 | -56.0603 | 2024-10-24 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 266.7 |
| 5be55a2c-0a6b-3322-a7a5-96229e48c991 | -18.2836 | -56.0576 | 2024-10-24 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| e81640dd-e192-32c1-a69d-9c6e5a3f672b | -18.284 | -56.0367 | 2024-10-24 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 172.6 |
| 74317ac6-5838-3f7b-89c7-8d0c81f35e2e | -18.3199 | -56.2404 | 2024-10-24 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 3bc25c5b-0d37-3870-810c-d10d42fc6624 | -17.0184 | -57.5178 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 8e0ddb77-52af-3457-a047-bb5e92331f46 | -17.0387 | -57.4745 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 23fce751-4084-37e6-99ea-92dd50f6e990 | -16.9596 | -57.5245 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| 2535ad23-11a3-3e5c-9b45-4c1ef30220e1 | -17.0188 | -57.4973 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 31f47710-623a-3a2d-bb90-7a73a39fe2af | -17.039 | -57.454 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| f1bc1a84-d9e0-3e82-b659-739a0a1963bd | -16.9792 | -57.5223 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.5 |
| f9937d6b-a534-3051-b884-5965dece4858 | -17.0381 | -57.5155 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 4a0fdd3b-4322-30ee-89c3-670f7bcf18e0 | -17.0384 | -57.495 | 2024-10-24 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 927b4f98-62d1-398d-ab4f-a5be4ce16fda | -17.7065 | -57.4569 | 2024-10-24 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |


[Clique aqui para ver as próximas entradas](README117.md)
