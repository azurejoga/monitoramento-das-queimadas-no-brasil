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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5df7cb7-42ec-343b-8d07-744bf9ce42e2 | -23.8394 | -51.987 | 2024-10-31 07:17:17 | GOES-16 | FÊNIX | PARANÁ | Brasil | 4107702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.3 |
| c2297a63-7882-32a3-8e8b-08692f0c8a51 | -19.5461 | -56.7192 | 2024-10-31 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.0 |
| d67ba234-3673-3ea7-a087-8f5be6d79679 | -19.5063 | -56.7039 | 2024-10-31 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.3 |
| b3dcf3e4-9f78-3367-80bd-295ccd21ac52 | -19.526 | -56.7221 | 2024-10-31 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 29d359e7-8ee6-3fb7-851d-7a132ec9c791 | -19.5264 | -56.7011 | 2024-10-31 07:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 6a625333-60b7-3e06-b13d-b6f3473ba3f4 | -19.4859 | -56.7277 | 2024-10-31 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 69ddb5c8-52ce-38d7-9e98-547b515e23d1 | -19.4862 | -56.7067 | 2024-10-31 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| a72a3bf9-73a9-3495-a218-a2ab6d1de45d | -19.5063 | -56.7039 | 2024-10-31 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.7 |
| 50aebbcf-a70b-3e7e-9c46-4934628a79be | -19.526 | -56.7221 | 2024-10-31 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 0b4bb51c-3eb8-3efb-b3b1-98438c954c53 | -19.5264 | -56.7011 | 2024-10-31 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 89e252ec-b769-3c97-b757-efaea0dfd32a | -19.5461 | -56.7192 | 2024-10-31 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.1 |
| 6eaf7619-ae5d-3262-83a4-6c0d658661b7 | -19.5461 | -56.7192 | 2024-10-31 09:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 78d282cf-e358-34db-92a0-eccd094b5a93 | -19.526 | -56.7221 | 2024-10-31 09:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 15da7866-f425-31cb-b096-13ffafb93df0 | -19.5063 | -56.7039 | 2024-10-31 09:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 673c13d0-5a9f-319d-b30b-26eb80edc3c9 | -19.6063 | -56.7108 | 2024-10-31 09:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.3 |
| fd851183-cf6b-3753-ab24-7df6c2e14355 | -19.6059 | -56.7318 | 2024-10-31 09:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 197.6 |
| 394909d6-ed3a-3ed1-839d-e9f41b3a8bfd | -19.6056 | -56.7528 | 2024-10-31 09:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 152.5 |
| ac50d2f9-a88d-375a-bee7-78430cb703e5 | -19.5859 | -56.7346 | 2024-10-31 09:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 11b13320-eb33-31fd-b011-4025fc76898b | -19.526 | -56.7221 | 2024-10-31 09:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| c75965dd-09ea-3c69-955c-a5728bbdc944 | -19.5859 | -56.7346 | 2024-10-31 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.8 |
| a672f805-a0d9-3c0b-8e5b-f8965b7021f0 | -19.6056 | -56.7528 | 2024-10-31 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 160.2 |
| 742d5f66-5d2b-3603-a53c-8085355c2a70 | -19.6059 | -56.7318 | 2024-10-31 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 193.1 |
| 2530cfad-f251-3375-a0a5-457731f7dc3b | -19.6063 | -56.7108 | 2024-10-31 09:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 5614f889-8307-3785-b068-1c41e2042d18 | -19.5063 | -56.7039 | 2024-10-31 09:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |
| efab8ffd-02a0-364f-8507-c8f803a05474 | -19.5461 | -56.7192 | 2024-10-31 09:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 01f82f7e-5dd5-3fc0-a916-6b4442daf180 | -19.5859 | -56.7346 | 2024-10-31 09:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| 46e6a132-de64-3b9b-a548-80a57dc58744 | -19.526 | -56.7221 | 2024-10-31 09:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 5f30af0d-c87f-3659-bcb4-5cfd0effeff5 | -19.5461 | -56.7192 | 2024-10-31 09:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 60364820-42ec-34d6-a579-a7d146c190e2 | -19.6059 | -56.7318 | 2024-10-31 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 184.1 |
| 0c190076-0e47-35e7-8c6a-f5d18f8defc8 | -19.6063 | -56.7108 | 2024-10-31 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.1 |
| faad3486-cd8f-3fe3-98ec-2750c122888b | -19.5859 | -56.7346 | 2024-10-31 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| e6332d98-7204-3f32-a1d5-00208151267b | -19.6056 | -56.7528 | 2024-10-31 09:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 130.4 |
| d9841b9a-dc69-3546-b790-1006350fe4b1 | -19.5461 | -56.7192 | 2024-10-31 09:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| ba3f7acf-ee96-3a7a-a48e-46693c3e0237 | -19.526 | -56.7221 | 2024-10-31 09:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 87950c96-8025-3b6c-bbd1-9a21da932a1b | -19.6063 | -56.7108 | 2024-10-31 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 20f773b2-c34b-3c4b-8d4f-b71b4e123145 | -19.6059 | -56.7318 | 2024-10-31 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 190.5 |
| 76c90d93-b437-31dc-910c-1253ee16e61d | -19.6056 | -56.7528 | 2024-10-31 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 151.0 |
| 8826ad56-e0dc-3189-85ed-50ee89b708de | -19.5859 | -56.7346 | 2024-10-31 09:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| e8a01121-131c-3187-b6ae-9edfb0be6e77 | -19.5461 | -56.7192 | 2024-10-31 10:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 2d3c963f-4b1d-335b-b5fc-fb7139e05450 | -19.5063 | -56.7039 | 2024-10-31 10:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| 0357f12e-19f4-379b-bcf9-da6fb625f836 | -19.6056 | -56.7528 | 2024-10-31 10:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| 51883193-5a35-3720-b91c-7f7e18bbabfd | -19.5063 | -56.7039 | 2024-10-31 10:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.1 |
| b9d75a32-1554-320d-ac26-252768101f93 | -19.526 | -56.7221 | 2024-10-31 10:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| f574be83-fb43-33b7-be53-67bd019b77a2 | -19.5461 | -56.7192 | 2024-10-31 10:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| cfead015-eec3-3bbc-8127-3120c032e00d | -19.6059 | -56.7318 | 2024-10-31 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 183.3 |
| 6fe02370-227a-3b37-a701-09cbc93fd971 | -19.6063 | -56.7108 | 2024-10-31 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 207a9adc-0788-316b-8add-6abce1ed8d0c | -19.5859 | -56.7346 | 2024-10-31 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| d7d832a9-236a-350a-8d05-96398d0eac27 | -19.5862 | -56.7136 | 2024-10-31 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 1d1968e9-2210-3e0e-ab91-375e0e7d17f0 | -19.6056 | -56.7528 | 2024-10-31 10:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 151.5 |
| 79f8aef7-96a6-30be-9291-b450e3178c50 | -19.526 | -56.7221 | 2024-10-31 10:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 9cf4c8fc-850d-31d0-88c4-41b49c2092c9 | -19.5063 | -56.7039 | 2024-10-31 10:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.5 |
| b03b3980-3b17-3c7b-a4b7-e87701f3d34b | -19.5461 | -56.7192 | 2024-10-31 10:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.9 |
| b9d485c6-512e-3c62-ae0a-293495b80cd1 | -19.5859 | -56.7346 | 2024-10-31 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.8 |
| 8392e73b-a4ff-3c7c-94cc-67fadd6aab50 | -19.5862 | -56.7136 | 2024-10-31 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 261697a7-0877-35df-9bc0-8a3db9edd2b1 | -19.6056 | -56.7528 | 2024-10-31 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 0ea506f3-0d33-3cfa-9618-1ba8cd197e33 | -19.6059 | -56.7318 | 2024-10-31 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 195.7 |
| f4699b4f-517a-3139-88f0-ca1bb07f444d | -19.6063 | -56.7108 | 2024-10-31 10:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.1 |
| c8c727e8-03e3-3fd1-8713-4f12fc94df96 | -19.5063 | -56.7039 | 2024-10-31 10:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.4 |
| 0d2efcff-a0c6-3a3e-ab18-014b2864e87f | -19.526 | -56.7221 | 2024-10-31 10:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.4 |
| ca10d5a9-ab70-3387-9dea-a3f12aeb0ac3 | -19.5461 | -56.7192 | 2024-10-31 10:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 7a000a05-8df1-31e9-8c86-c86616762fd1 | -19.6059 | -56.7318 | 2024-10-31 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 190.0 |
| 245d3957-a33a-3667-95cd-e296744d0ce5 | -19.5859 | -56.7346 | 2024-10-31 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.2 |
| c1276d5c-f60e-34f6-aaed-ddfb7c261f29 | -19.5862 | -56.7136 | 2024-10-31 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.0 |
| f4947789-5bd1-3c7c-bf27-98511e8514ad | -19.6056 | -56.7528 | 2024-10-31 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 150.3 |
| acfed94e-e93d-311b-aa08-76d8568857fe | -19.6063 | -56.7108 | 2024-10-31 10:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 6ce52107-a8ac-3a26-a93d-8f3e4c6c6eee | -19.5063 | -56.7039 | 2024-10-31 10:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| bf90c157-26be-3f88-9acf-097e54427ecf | -19.526 | -56.7221 | 2024-10-31 10:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.7 |
| f9eadc82-5e59-3034-afcd-ce06578746ec | -19.5461 | -56.7192 | 2024-10-31 10:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.4 |
| 62ee274f-cf53-36dc-952f-8633c0f4ea6d | -19.6063 | -56.7108 | 2024-10-31 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 39691d30-bb64-36a1-8acb-4cadea7df6f4 | -19.5859 | -56.7346 | 2024-10-31 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.1 |
| e011e025-6209-3026-b221-90a357de72f9 | -19.5862 | -56.7136 | 2024-10-31 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 799ffa9d-3431-3cb0-aa89-7c80735620cb | -19.6056 | -56.7528 | 2024-10-31 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 152.8 |
| d4ac8c14-e009-3604-bfb0-0a82339ce9ed | -19.6059 | -56.7318 | 2024-10-31 10:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 206.7 |
| 194baeea-478e-3a5c-be3b-2739eaccf357 | -19.5662 | -56.7164 | 2024-10-31 11:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| ad818fee-f95e-382a-a58d-bce3b5d9eef4 | -19.6268 | -56.6869 | 2024-10-31 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 24d99616-de58-3500-8ee2-76a742e789a1 | -19.6063 | -56.7108 | 2024-10-31 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.4 |
| b5ff3a21-54ac-39bb-84c8-5e7a1d85ee80 | -19.6264 | -56.7079 | 2024-10-31 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| de3a459a-467e-3c79-9b96-d6b7bc05752d | -19.5862 | -56.7136 | 2024-10-31 11:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.4 |
| fde6ccf4-cbc1-33ed-a74b-52a7e4a40175 | -19.4878 | -56.6227 | 2024-10-31 11:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| d8071155-3369-35d0-8d6a-81d617002322 | -19.5087 | -56.5779 | 2024-10-31 11:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 9ba72cbb-6a60-3414-8345-186560c63505 | -19.6264 | -56.7079 | 2024-10-31 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 1e54cf7b-f500-38a7-9ca7-0c88f4b17159 | -19.6268 | -56.6869 | 2024-10-31 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 9e66bffd-745b-3921-af50-267588e1e32c | -19.6063 | -56.7108 | 2024-10-31 11:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| 696cd68c-4a53-3855-a970-38bd7616ca69 | -19.5087 | -56.5779 | 2024-10-31 11:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 005884dd-5674-304e-a41e-8779d3597b97 | -19.6264 | -56.7079 | 2024-10-31 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.1 |
| 9611a947-0016-3240-84ae-9644280a153d | -19.6268 | -56.6869 | 2024-10-31 11:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| d7f4738b-a88c-3886-925a-6efc71846dd9 | -17.2733 | -57.5085 | 2024-10-31 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 17e87241-f870-32df-aa18-0dbeebb56fb1 | -19.5067 | -56.6829 | 2024-10-31 11:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| d3d521e1-3f46-3a17-a3ff-6cd92a849770 | -19.4859 | -56.7277 | 2024-10-31 11:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.7 |
| 1c5045ba-98c5-32db-85a0-df9048438234 | -9.45741 | -36.98325 | 2024-10-31 11:57:00 | TERRA_M-M | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b07723c1-51b9-3507-967e-c04bec9e3ed7 | -8.38838 | -35.39132 | 2024-10-31 11:57:00 | TERRA_M-M | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 35be6580-9d77-3ba7-98f8-10e70321bad1 | -8.25207 | -41.88889 | 2024-10-31 11:57:00 | TERRA_M-M | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 9e2a3e6e-2e6c-30e9-8b59-778428baa750 | -8.24465 | -36.64218 | 2024-10-31 11:57:00 | TERRA_M-M | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 15.0 |
| c9b508aa-99b4-31b3-8772-f3b64a297c63 | -7.17711 | -40.14132 | 2024-10-31 11:57:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| eb1d3e3d-31c6-3e30-a2c8-acfb8b074567 | -6.74587 | -36.09525 | 2024-10-31 11:57:00 | TERRA_M-M | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 688984e2-4947-3274-8499-d80bad0bd386 | -6.74457 | -36.10415 | 2024-10-31 11:57:00 | TERRA_M-M | BARRA DE SANTA ROSA | PARAÍBA | Brasil | 2501609 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b1660366-2164-3e93-ae0e-ae2501f38f3a | -6.68251 | -37.46993 | 2024-10-31 11:57:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 19.2 |
| b31d68e7-c65d-382a-9cd9-4d7ab3b49d93 | -6.57912 | -38.16154 | 2024-10-31 11:57:00 | TERRA_M-M | LASTRO | PARAÍBA | Brasil | 2508406 | 25 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5bd0b4dc-719b-335a-8c9e-50191bb2f522 | -6.48104 | -37.71254 | 2024-10-31 11:57:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 15.3 |
| f3583ee8-e356-3496-ab9e-2e4d731d16d3 | -5.33351 | -35.659 | 2024-10-31 11:57:00 | TERRA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |


[Clique aqui para ver as próximas entradas](README54.md)
