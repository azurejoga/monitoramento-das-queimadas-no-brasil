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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 807a80f9-7542-324d-b9fd-5b02662e1fed | -1.72775 | -52.52808 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c2d383-907c-3974-b9d4-38f27f8ff9cd | -1.69976 | -52.16169 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12b67ef8-9dd8-38d2-aabf-0c6dd120016f | -1.69698 | -52.15769 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ecdaf0-5664-3905-888a-a6540c34e78d | -1.67695 | -52.13315 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c6a0e5c-3cfb-392b-877e-5abe7585e06c | -1.60474 | -51.96366 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a25f0598-1905-3e8a-9f32-49d1b203c35c | -1.59955 | -52.49695 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5348ea66-5222-3583-8674-ff6185f8f2c0 | -1.59901 | -52.5004 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb6c662f-ebca-39d3-834a-7da477ba7631 | -1.57738 | -52.05308 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8044b5-53d3-34ff-83fe-92290ed8a730 | -1.56293 | -52.03651 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4404e1-9f48-31fe-86f2-e214c9d0baeb | -1.56015 | -52.0325 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fda4b739-d648-392a-9473-72ca11ecd283 | -1.55682 | -52.03199 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93b311ca-4daf-39a6-a3ba-e2957da8ea99 | -1.55319 | -52.64135 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1eca9c9-1a8a-3362-83ca-eb09fe9ed9ab | -1.5514 | -52.10987 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7063b7c6-e343-3d67-8e8f-6e1a0bc763ef | -1.54917 | -52.10238 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29e12dde-51bb-3831-972a-8b6575ba56fd | -1.54863 | -52.10587 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4cb83f8-543d-37e7-9c5e-5f2a73e7a845 | -1.54804 | -52.0879 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61364fc8-e428-3156-9549-c29fabbc3222 | -1.54647 | -52.14124 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c13d2e86-4860-3eb1-9a20-8d74a6133a48 | -1.54593 | -52.14473 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c4b34eb-bcb5-3910-8ef4-b0ecdd283436 | -1.54471 | -52.08739 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ee04f40-856c-3a4f-ad51-1aac8b22ee7a | -1.54417 | -52.09088 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30da2ead-3a68-3a1f-9123-909d9c4f7cb6 | -1.5426 | -52.14421 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6064484-fc84-3832-8c44-f860eb4abf89 | -1.54193 | -52.08338 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a982d25f-1ab8-3f79-bae9-cd5e816d7a09 | -1.54139 | -52.08688 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 234394b2-35ac-3a73-aed4-df0a1f9ef53f | -1.54029 | -52.09386 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02357ae1-7757-37e9-90b9-a631624ff475 | -1.53915 | -52.07938 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd4bb1b0-49da-3dc8-8ac3-3cf3a6958b9f | -1.53861 | -52.08287 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d483e2d-b76a-347a-868d-548f08752cee | -1.53806 | -52.08636 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445f1554-8e68-3bd8-8434-beb899abd9e5 | -1.53364 | -52.09282 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 424b3d97-e96c-3fb8-82c3-07ee90524977 | -1.52397 | -51.98026 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb4fcc51-b085-3d23-aed1-6740cbe3cb19 | -1.52342 | -51.98376 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1beff34-385b-34a5-b80c-c9b796988c64 | -1.51279 | -52.57523 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b7c19f4-2d52-3ee1-a87f-4c81a2503b4a | -1.47234 | -52.52682 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d332ee-ded4-365d-86b2-99f714d0e5b8 | -1.46904 | -52.52633 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1f86037-f88c-39af-9d47-faf5380df4ff | -1.46778 | -52.03613 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8967f603-d9fb-34d7-877e-d16fb271425d | -1.46723 | -52.03962 | 2024-10-28 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec91ea2a-a5ca-316c-872f-c069191216b3 | -1.40786 | -52.02685 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dee6512-d0bf-39df-9f5a-9b4aba59815d | -1.40732 | -52.03035 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95d6ea33-27ae-38ea-a582-53528080ef67 | -1.40283 | -52.2329 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55d61fb1-c9d0-31aa-b0ba-406e7a7be4af | -1.40251 | -52.10464 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aacf28fe-c329-3dbc-b45c-594b13275ea9 | -1.40006 | -52.22892 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f04c6291-5438-3566-a889-0fc0316c4aa8 | -1.39946 | -52.21104 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8ceb6c9-f0fa-3faa-9aaf-95cbb4abf246 | -1.39919 | -52.10413 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f21312ca-a449-3bc6-ab61-fd0b7aaeb140 | -1.39632 | -52.49027 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f241d25-855b-3627-8fcb-fb67f7072769 | -1.39301 | -52.48976 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 424f473c-305a-39b7-951b-064c30836c5d | -1.38913 | -52.27693 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7801096-7561-32e6-b831-e88b71ca95bf | -1.37307 | -51.96724 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e52fc785-439c-32a7-802f-ba64c2eb52a5 | -1.3441 | -52.52098 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13b18da1-7f09-39e4-97d5-6c22aef19187 | -1.34356 | -52.52442 | 2024-10-28 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fa2a5c0-8b42-3f7c-a3ff-95eeffe3c3ff | -3.52702 | -53.24807 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5319b247-08ee-304e-8f4b-01cb7f7e962f | -3.52372 | -53.24756 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0470a6b2-c00e-3b8e-a4d5-8d3778c14d1a | -3.45955 | -52.96213 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd67fe8-8139-3c0d-8565-6848ce4767cf | -3.45625 | -52.96162 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d1fa990-3d68-3d6a-9c21-97bba461a1f4 | -3.40039 | -53.68872 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d664b53d-b639-3a71-91db-e114fda78dff | -3.39985 | -53.69216 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547184cf-5f5a-313b-9e55-dde13481f17c | -3.39709 | -53.68821 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e5f2308-4278-3363-9f5f-bbdc58878cb5 | -3.23214 | -53.28233 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e848c01-5997-3e92-a9c6-aa8fd823b841 | -3.21868 | -53.36806 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68d04afe-7bc1-30fb-88cc-0663d7ddaa99 | -3.21592 | -53.36412 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3163f734-c76c-3f46-bc54-204dab5a12e1 | -3.21538 | -53.36755 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95e4819e-d80b-369d-beda-19871f728674 | -3.21263 | -53.36361 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c77eca75-bf65-3e3b-8428-6d5ad3e76400 | -3.2067 | -53.40133 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a6907c-c260-3df0-bb45-061c93d5b94e | -3.2034 | -53.40082 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 346e46c7-1d01-35d2-b63e-a67d5895fefb | -2.88896 | -53.04214 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ff43017-0f23-3041-a383-8049fd76124b | -2.88842 | -53.04558 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f0d4cca-1025-32c0-ae4a-46974885f928 | -2.86027 | -53.33278 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72efb55a-6e62-3d9c-b813-7c95a3b554d8 | -2.85751 | -53.32883 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4f1990a-5609-372d-b37f-797981b562b2 | -2.85697 | -53.33226 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4063047b-474e-3d78-a31e-e6cd4436b188 | -2.85643 | -53.33569 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e65c36d1-b8db-30c6-a0c8-5cd7c1f882cf | -2.85421 | -53.32832 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63fce62-a12d-3952-89fd-e82e488ef4a6 | -2.85367 | -53.33175 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 018242c6-4431-360d-9079-f8b9916bd3bb | -2.85145 | -53.32439 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fd6b51-07a7-34ef-adb9-4c6fdcb4edc7 | -2.85091 | -53.32782 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 550ba8cb-e7d7-3bd9-9d04-9f13fc6c6179 | -2.85037 | -53.33124 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f2d280-5ddb-3709-95e0-a3c02ffb1c42 | -2.84876 | -53.34152 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a31684-b4dc-386f-b57c-ec60a606adf1 | -2.84822 | -53.34495 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8a7726e-1121-3a3b-93c0-69e3fb30bfa0 | -2.84815 | -53.32388 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74290fee-84a4-3e9b-97d0-d7ee72b3a513 | -2.84761 | -53.3273 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f232fd-44f7-3f9a-bf0f-593e29f34969 | -2.84708 | -53.33073 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edda50dc-7a83-3c79-b4ff-ffa575a3fb8a | -2.84654 | -53.33416 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f89ea7f-aa2b-3bb1-8e3a-39ed9d1f09cb | -2.84485 | -53.32336 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd4862cc-d0f4-32df-b947-b86f070c66a4 | -2.84432 | -53.32679 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bedbdee-7b76-3789-8058-6672b63bc061 | -2.84378 | -53.33022 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7975f9e5-1fa8-37d2-a93e-dd83a0f42e1d | -2.84352 | -52.55018 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7a2a2f89-c6c6-3055-924f-44bab5338860 | -2.84298 | -52.55364 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d7510e6-69ea-395f-81ef-1a8d46384bd3 | -2.84216 | -53.3405 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f4a302-0bff-3226-820b-08fddf5513cc | -2.8402 | -52.54968 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81b1224c-1e41-341a-85f7-2b620803aa6d | -2.83688 | -52.54918 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a152dc6-a753-3739-92fd-63dfd86b164c | -3.6816 | -52.39062 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 825adcc0-0049-3e71-b756-d907f72fc924 | -3.63182 | -52.2925 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19c714be-296f-38b6-ac57-f4e5de5f26ef | -3.59525 | -52.70357 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9bec6ae-d1c3-39e6-9f00-7f01ac67b9f9 | -2.7857 | -52.89866 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6ca54f8-ee1c-39a2-a55f-88ce112396ae | -2.78516 | -52.9021 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ee8a799-2912-3af4-a011-fcc771ea033c | -2.78186 | -52.9016 | 2024-10-28 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07064778-bd71-33a5-a100-81ab70dc4efa | -2.75992 | -52.06332 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03263ccd-35a2-3aa0-bf68-69e2d4e7f025 | -2.70653 | -52.44706 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b29ef3bb-c4ac-34fd-aa05-60f6155eb724 | -2.70585 | -52.90737 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73cfc28-2dea-3091-b583-934150f8d3ab | -2.70321 | -52.44654 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e590b3a0-059b-31c6-ac64-aadd8c24f7b8 | -2.62411 | -52.45211 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d252e8d-7b48-3232-a89d-bfdf42355e17 | -2.60807 | -52.94482 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60b0ab3a-6e1e-3a5b-855e-278b44e6095d | -3.16765 | -53.06841 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README64.md)
