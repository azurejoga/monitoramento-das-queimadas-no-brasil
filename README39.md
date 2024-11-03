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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b0cd7cc-8570-379d-ae1f-f500527c675b | -2.73767 | -48.73701 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aedf87b2-4bee-3b9a-b4b7-e8ca9782f524 | -2.73711 | -48.7406 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7af3357c-38f7-3841-9591-d58c74f742a3 | -2.73656 | -48.74419 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf3f799-7e51-3fda-a673-5c4d6e47f1b3 | -2.73545 | -48.75134 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c93c56fe-ea4f-345b-a6b8-b9931badfa1c | -2.7343 | -48.73649 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d661b0b0-90fa-38b0-b366-f218f2062c00 | -2.73375 | -48.74008 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e80b12-5741-3fb2-ab62-ce66918b65b2 | -2.73263 | -48.74725 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edfc2eb6-3c98-3718-b65d-57859559e23d | -2.73208 | -48.75083 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21588ee7-06c4-3462-a394-1faeed5ec03a | -2.72871 | -48.75031 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 588f22ef-604e-388d-8353-3a6750ea8bb4 | -2.72816 | -48.75388 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08590466-4108-3717-8d77-15b194744938 | -2.72535 | -48.74979 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83cea59c-72fd-3918-8554-d5b4c9901535 | -2.72531 | -48.72777 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68dfa023-4ef2-3225-a98c-79d9f997b38c | -2.72479 | -48.75336 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ea12d0-573a-3f3c-8ac1-4bbbef739373 | -2.72198 | -48.74927 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c9b5047-1dc2-32fe-891b-0920018a3eb7 | -2.72194 | -48.72725 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80942efb-b28f-3a4e-86ae-6f6cd9992336 | -2.72028 | -48.73801 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 210a786d-143c-3c2a-b4c8-433d9c4af84b | -2.71861 | -48.74875 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 634aa8b4-0da8-3961-9e34-c5f869fbc0d7 | -2.71691 | -48.73749 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 591d82f9-e988-3233-bbf5-f4b6f6e38ea3 | -2.71635 | -48.74108 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86fdbbdd-8267-34a5-beaa-c4e59eaee307 | -2.7158 | -48.74466 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2f0c05c-e83c-350c-9465-4df281f2b519 | -2.71525 | -48.74823 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc89157f-fa31-3bc2-aa0a-97f037f2e9d7 | -2.71299 | -48.74056 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb135231-f1aa-336d-be40-4acafbbaa58c | -2.33764 | -48.50994 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 793def96-a738-3670-922b-d09919f62711 | -2.30881 | -48.4499 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ccb5d11-755d-3e09-add4-6722bc3b9648 | -2.30487 | -48.45301 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb4d652-651d-34fd-94f6-0ce9b5196a08 | -2.30204 | -48.44886 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c980fb0-5de6-3b16-b9b3-4741cd5b8738 | -2.29698 | -48.45922 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95a12bdb-0f66-31db-98e0-25e149c3bb60 | -2.29642 | -48.46284 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b10abf-0da4-38b6-83e4-16e3b92b7ca5 | -2.29304 | -48.46232 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74cccac9-c978-3637-8382-a2551a4a0714 | -2.51303 | -48.55899 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61b0f9ec-337c-378e-96e2-ed367f6315bf | -2.51247 | -48.56261 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab3d8394-2efd-31ed-aa53-04f4f1ca5298 | -2.47099 | -48.48615 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8c09409-73c7-3cd3-8708-9fef08289da0 | -2.46929 | -48.49702 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9827025-22e3-35fa-8b64-6e9000f9729b | -2.46873 | -48.50064 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa75cb66-450b-39f8-bfd5-7a84380a27cb | -2.46816 | -48.50427 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 283752b1-aa43-3f3e-9f8d-287c7edabe73 | -2.46309 | -48.49231 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f6664db-8d31-3991-b387-047441e540e2 | -2.46196 | -48.49961 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3c38851-026d-3d70-9112-2f67dbca6906 | -2.45971 | -48.49179 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4095e2da-b1ed-39f1-9596-a3b4f7f4a2bc | -2.45914 | -48.49541 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5dcd92d-f165-352e-a918-e6f471df7e5f | -2.45689 | -48.48764 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 862c117d-6183-347c-867e-c731d746d4ca | -2.45067 | -48.48298 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b3d563f-5611-3981-bce0-5a2e963cd029 | -2.44448 | -48.50057 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 298a9793-0d9e-303c-9747-a695d211d045 | -2.42585 | -48.48658 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a870804-687f-3bcf-b96d-6aa5cbe808c3 | -2.42317 | -48.59342 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa3ab182-1267-3449-866d-d68548ec3adc | -2.42252 | -48.53054 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a8ee029-7aa3-364d-a5a3-c533c38d8f81 | -2.41914 | -48.53002 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ee924c-04aa-3182-9635-3b12c987e65e | -2.41858 | -48.53363 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 155f638a-c78d-3ef2-936b-2a1423126f25 | -2.41576 | -48.5295 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cb12499-40af-3547-b78c-29a243038ffa | -2.4157 | -48.86285 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea661733-a4ed-3772-8b3f-368673cfe9ae | -2.41404 | -48.87347 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55e03ec8-9167-3c24-b87e-505e2ad933ff | -2.41397 | -48.8299 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b95088b-23ac-329b-a582-f3439453b145 | -2.41339 | -48.81161 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71e79f5f-15e1-3a35-a4be-012394089bb2 | -2.41293 | -48.52536 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb473330-3e10-319c-9706-7db84100ee43 | -2.41235 | -48.86233 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e95bd043-c35b-33b0-825f-86fa7c54b4d8 | -2.41062 | -48.82938 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2912c7a8-4656-3116-a31c-222ad4339542 | -2.41014 | -48.8765 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a83e391a-72f0-3697-bcc8-0d99ea9ef63a | -2.40796 | -48.58003 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55b97640-181a-3723-9a35-7c32bdb1107e | -2.40176 | -48.57539 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1dbb65f-c4ac-34c6-a8a0-b8858eba3949 | -2.39954 | -48.58979 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f88a7c-89c2-3d1c-b491-47df74787bce | -2.39898 | -48.59339 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba59a547-3801-34e5-88cf-cb9b7b3a9aba | -2.39501 | -48.57435 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 738c0656-2758-3fbb-923a-82f6a2271fe5 | -2.38825 | -48.57331 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b71f0eb-03dc-3e7e-a6b8-63ad2d6a383a | -2.38432 | -48.5764 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41f239a6-f334-345e-945f-9cb0ea26103e | -2.36131 | -48.55791 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4302d3f-2f16-3d9a-af9f-20f229ba9e48 | -2.33937 | -48.5656 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc7904cb-619f-3ae1-b6dd-58b46204bff0 | -2.33826 | -48.5949 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d21148e-2417-3bd0-9c11-b67bda356b5a | -2.3382 | -48.50632 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04ece3ea-3127-3647-9647-43377d8372ac | -2.33489 | -48.59438 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01a721a7-ca81-3aac-9083-67b75af176c7 | -2.33433 | -48.59797 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8ce20e0-b472-3110-88f2-2fb06677db4c | -2.33431 | -48.57588 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b47f7b-aeaf-3231-91c9-ab7b87227962 | -2.33375 | -48.57948 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5282d7a3-b071-3759-8c03-0919a4a1e8c2 | -2.33096 | -48.59745 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69906cd2-563b-386a-b422-38606a2a7f94 | -2.32761 | -48.61901 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbd61da7-0542-3b1a-90ee-24b1686851e3 | -2.32105 | -48.77164 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45b489cf-e49f-33e0-ad63-21ae5fd596c3 | -2.31632 | -48.58049 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c81e37d-a8cc-3729-8034-95264dcc794f | -2.31295 | -48.57997 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 236ee9a7-567d-354a-a41f-885a90a9b77d | -2.30164 | -48.54136 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b777d4d2-e649-3c6c-b2b3-b52e94bf005d | -2.30108 | -48.54497 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13404c39-e0db-3053-974b-5a540e64f9e1 | -2.30053 | -48.54857 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 534655e7-018b-352e-81ac-0580f6ae70dd | -2.29203 | -48.80355 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f3e50391-1d15-397a-83bc-94e4629c65c5 | -2.29148 | -48.80711 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3e55ba8b-c4ce-37e9-9ada-586d00e2e683 | -2.28868 | -48.80304 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d93de579-b5b4-339e-8cad-bf4de49bbdc5 | -2.28812 | -48.80659 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a223e1cd-a4ad-3e35-a7a2-f4895d66e3f4 | -2.27971 | -48.54906 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39755f2f-29bc-3905-bb95-c7a5cee931e1 | -2.26191 | -48.82073 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17759ee6-5f46-35ab-9287-4134c1c44fbf | -2.66166 | -48.50344 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30f9fca6-e746-32ad-9ccf-06b135eba8b2 | -2.6611 | -48.50708 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b912745e-61b3-36c3-9489-6ec7cafd5cea | -2.65827 | -48.50293 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e007a6c7-d520-3dc6-a9ad-395cf284e7c5 | -2.65771 | -48.50655 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cede9cf7-e1d9-316c-9b8f-5ffc295c628a | -2.65715 | -48.51017 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57aa8e8a-5856-3db1-a0df-d524a6ba11a2 | -2.65432 | -48.50603 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4136105-89a0-3011-baaa-96cbc1ebd976 | -2.63617 | -48.44361 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06a33460-e7a7-3139-b0a9-1f1c94022d51 | -2.6356 | -48.44725 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 70f08abc-34be-37e3-a6ca-6889f38ab8b1 | -2.62125 | -48.33636 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37d6a6d9-0371-3d29-a78f-3d984dc1a9e6 | -2.62008 | -48.32114 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4af5a1e7-7c93-3fc9-9c51-90855149ac23 | -2.61934 | -48.32168 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43ff35a4-0b63-39f8-8fe1-5ea3836b044a | -2.6184 | -48.33217 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9074efb-a643-3160-b6af-8aaedd0dd195 | -2.61784 | -48.33585 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56a0dfd8-b71e-3fb0-a12e-102775b2238f | -2.61761 | -48.33269 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a37ca137-d7d6-31f8-bbcd-3fd8a35fb4af | -2.61708 | -48.3138 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README40.md)
