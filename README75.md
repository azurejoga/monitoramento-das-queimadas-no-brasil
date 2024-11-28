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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c306aae-44ca-3dab-be94-a8cf9498386c | -1.46206 | -54.50351 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f8b2638-35bb-37da-8c90-562454bbd908 | -1.64086 | -52.45978 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3008f3b8-c4e6-37c9-8714-6b76b58787f7 | -0.45693 | -52.01582 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e943b22f-6cdb-3511-9412-e6d6dc0ad980 | 4.37331 | -60.81934 | 2024-11-28 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb4ce436-021f-32c0-8786-73f931825eba | -1.31768 | -51.74245 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 905377c7-88eb-3698-b9fc-522c36f4a70d | 3.81576 | -59.5975 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3786bdec-3d59-3d05-8d56-2e460c590381 | -1.73984 | -52.79599 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fbc6a24-d5fd-33f1-9e41-26f8ed1e6062 | -2.31086 | -47.86068 | 2024-11-28 05:16:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9dc8e62a-92e4-3594-8b2b-3eeea487fd36 | -2.85765 | -46.86541 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b13d68e4-5dd5-37ab-a107-24aa11363764 | -1.09088 | -53.64072 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80dccb1c-5ef1-3ea0-af6d-785521cf37ab | -1.673 | -52.73632 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0f61ebd-f12d-38b1-9a27-5b08ee7686ce | -1.21616 | -54.2207 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca039432-d9f8-36d8-8faa-51e31c187150 | -1.45582 | -54.37248 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d5f11cc-ba96-3001-b6b0-da6fa88b2727 | -2.00534 | -51.17358 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e55fef0-231f-3bb3-93a8-24ca4021410c | -2.85013 | -46.84192 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e46b79eb-4ae2-3059-9bc8-d37a1139d4d1 | 0.94669 | -50.73026 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b2e27af-8b39-3f0b-a56c-92b893e799ba | -1.3421 | -51.6715 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4f59ca0-abfd-38d6-ac56-a35c18a4909b | -1.57636 | -52.25856 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f25b7a2-fdb7-32f1-acdb-2d027eab3dfa | -0.27219 | -51.50637 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6cbbca2-828a-3c17-a540-568ab73e09c3 | -1.69207 | -52.49507 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 861c39c9-d6aa-3576-8b03-a5768fd81ebd | -0.35965 | -49.953 | 2024-11-28 05:16:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cbb64984-19b5-3ed3-a19e-3d8d5ef53dc9 | -2.84518 | -46.86338 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a6633e4-5f57-383a-b6de-1359fb2be97f | -1.08915 | -53.387 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04bafbce-3854-38fa-8bf6-03ebadcb1b43 | -1.27513 | -52.16266 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dd19fa9-37f3-35ae-8c90-e6604bbc288d | -1.6896 | -52.48283 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dafb53b1-6dff-3514-be2a-cfb2c74d7169 | -1.68891 | -52.48303 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9fc0de8-d9c5-31bf-9b75-30aeaa982012 | -1.35944 | -54.65729 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd428fd1-cf26-3245-b62a-d84ec0d791c6 | -1.6595 | -52.47849 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef4c195f-30ef-3047-a51f-970045e3f3be | -1.13462 | -54.21955 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a571af2c-ccde-36f5-9b8f-82e8881154e0 | 1.44448 | -55.90648 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b92c795-d845-3ad9-88c4-cd583ed1df45 | 0.70177 | -51.44667 | 2024-11-28 05:16:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49d7b96f-43c5-372f-a7ab-3caa65f5e059 | -2.38803 | -47.16606 | 2024-11-28 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b98d767-aa27-3b77-be3a-cfbcb1a4d368 | -1.13739 | -53.6979 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf2e44d-5af8-3584-9b7d-da7094d8c32c | -0.59312 | -51.70284 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1a16aa2-4b9e-33b7-91d4-d56cd7783927 | -1.04661 | -52.41261 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18e83482-4e9e-3982-9113-cc826ac28301 | -1.16121 | -54.07106 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eec27156-9c4e-396a-b468-2fd1468d6540 | -2.01209 | -46.4002 | 2024-11-28 05:16:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02e6217a-57a0-3583-a08c-977ef65001ed | -1.88227 | -52.66 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02deb232-d935-3134-9c55-6b35936c5419 | -1.62862 | -52.00511 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2852552d-3f74-363d-a249-70385d7ff76c | -2.84379 | -46.87315 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 97819250-2267-3632-9590-ecb44baf75ff | -1.66371 | -52.47913 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d84d46c-0d33-3d5f-9ddd-7fc9c8954d4b | -2.0547 | -47.12156 | 2024-11-28 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6e0a47c-f2bb-3afd-aa02-f6a65bb37842 | -1.32949 | -51.9548 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4cddb17-f19d-3148-9145-bff39232459d | -1.70513 | -54.72416 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0a0b249-3744-3519-a792-a6ac1edad416 | -1.08467 | -54.03798 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be77d854-cf55-342b-9711-4825be319c5f | -2.00604 | -51.16881 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03c01fd6-cd7b-31ee-90ce-350ccdea35b7 | -1.7926 | -52.74604 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff66b899-6c03-3886-a45e-dc63136ed876 | -1.62434 | -52.36948 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f286c52f-7b86-3018-b0fa-ac6d0f36ae7f | -1.58062 | -52.25922 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10a54f86-c107-362f-8cfb-c86e6a25972a | -0.95254 | -51.65418 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7cf7ada-1a20-37b0-9d0f-095239c43939 | -0.5831 | -51.70988 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f46ad5b-94fb-34f4-8011-71362db087b0 | -2.02168 | -51.19081 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e419bc4f-27cb-33af-ad91-daa93dfa136d | -1.70366 | -52.53236 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64921a39-a149-3270-8e6e-aed6ecee0511 | -1.0716 | -53.63747 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb24770f-d371-3120-baba-369b50553116 | -1.56437 | -55.78175 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b41e772-4ad9-344c-b263-4968032fa78b | -1.64217 | -52.72776 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a681973d-7525-3c3d-b7f5-f5e43138a313 | -1.38867 | -53.63077 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02b0d052-599e-3093-a0ac-0790fdd79ed4 | -2.86108 | -46.85409 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5efe0f64-2045-3793-af06-a297d4d9450e | -1.19259 | -51.76451 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b51d7e53-2839-3deb-b0ec-20a29df9597f | -1.69768 | -52.62886 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19276cf4-2735-3335-9a40-19e0b1ddfb5d | -2.8729 | -46.86042 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 750fe173-be7c-3292-b44f-5f13750da068 | -1.64287 | -52.11254 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f78e13fc-e443-3a59-9cc1-138ca1542930 | -1.18609 | -51.98098 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b74ba50-2f04-3949-8c99-ee9dc789afad | -1.44831 | -54.51913 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c9d6190-0a07-371e-aaca-672b96384900 | -1.08601 | -53.38135 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80bc838f-7a50-3cc7-9cb3-eaa444db3087 | -2.01286 | -46.39507 | 2024-11-28 05:16:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 403a6a2f-d594-3986-bf45-b29cf1f6cfef | -0.15226 | -51.34737 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29357081-5980-3246-a380-aacdc835e559 | -1.62981 | -53.87095 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffdb8f7c-6122-3fb7-aed9-037e9d8317cd | -2.8582 | -46.87319 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b310645-ccb3-3fd7-b40e-e4169cac7f06 | -1.14806 | -53.67996 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2cd1330-caae-3062-b501-7642850f4b9f | 0.97549 | -50.12296 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 247c2f78-9f79-3716-994f-aa853fe3a605 | -2.84721 | -46.8614 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f87d5eee-a330-32f7-a324-161f6e34b8dd | 1.43269 | -55.89729 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb4937c-003d-3cc8-b64d-5f09a038a8a7 | -1.08911 | -53.36143 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20032a2b-71f8-37be-9f24-8547e5af367c | -2.86441 | -46.87432 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86061584-18d7-38f3-96c3-5ec5541aeceb | -1.19623 | -53.89353 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33c14a88-1064-3f71-b079-7d60912a37ca | -2.86938 | -46.87252 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 985540c2-dff9-3d39-941c-d0d9841d616a | -1.59642 | -52.26982 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cdfa1c9-c38b-32ab-bc24-af30f5d90c6a | -2.84865 | -46.83899 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ab36015-382e-356b-a58b-26ce4374d37f | -1.69685 | -52.49186 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa1896fa-fe74-3201-8a5a-7815a20a47e3 | -1.71597 | -52.47903 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b2de5e6-cc5e-3b49-ac01-a847a384d0b5 | -1.0427 | -51.74002 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fad451b1-c662-3319-a02b-d5c86ce42fd6 | -1.57846 | -52.01408 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c72743e-836f-3e00-a345-873b35cc1648 | -1.36708 | -52.12593 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36fab19d-6d28-3a40-a7f3-b7c747516f42 | -0.8837 | -51.72153 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7525146-caf5-366d-bf3d-5bbe9ce8261f | -2.86114 | -46.84103 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf734d78-61ef-382a-94df-dc2dbe0f842d | -1.36339 | -54.65673 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66ab146e-cc3d-3fb8-a344-0ce91b9850a7 | -1.44477 | -52.60363 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fc2cf4d-837c-3de8-937b-e896d68647b0 | 1.30991 | -60.40869 | 2024-11-28 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0edc9283-544f-3b0f-a726-c1fd35657d02 | -1.70579 | -54.71989 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4b21267-6c4c-3766-917f-12f8726adfa9 | -1.36646 | -52.12997 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 454903b3-4533-3bd7-bd6a-4cf6dc7c430b | -1.07027 | -53.37923 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fd807f8-2577-33f0-89d6-6c2f7805beb3 | 0.97715 | -50.1268 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 65cb70a1-3546-314d-abf0-174856d56378 | -1.58729 | -52.27247 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0d630da2-a86d-347c-8fc9-01a955c7ba36 | -1.25933 | -51.59452 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00fa9899-595d-3a0b-a024-634967dad9fe | -1.38011 | -53.63473 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a6ae6c0-c652-357a-b2c6-4bba64b2ad26 | -1.15396 | -54.21803 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4013700b-bff7-3e4b-85ee-1de6a4786a33 | -1.31394 | -51.73747 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1010498-3383-3cde-9497-4b5d8eeac4a3 | -1.66339 | -52.71577 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f96a2b80-f3a8-341c-8868-50e810c4ec37 | -1.321 | -51.92383 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README76.md)
