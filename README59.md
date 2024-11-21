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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbab1738-d099-39fb-a1ff-085ebceba3b8 | -3.59404 | -43.62971 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd1bda67-c1b6-3730-99fd-284feaa637b6 | -2.9373 | -48.33325 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9154d694-b9cc-343c-b0b3-b01b93280ace | -2.21254 | -49.8749 | 2024-11-21 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2717b62-2406-3270-b28c-3e8a724ebcd0 | 0.69774 | -51.44276 | 2024-11-21 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445885a2-6add-33d0-bafa-3bfd73379fbd | -2.28376 | -51.11448 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45f6a10c-2eb6-308f-93eb-ffccbc34aa3c | -1.37554 | -52.86524 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cf36a88-e79a-3a21-8c29-ee4dbe61fca8 | -1.46969 | -51.12206 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58f11472-243a-3aeb-9853-4f8e06831670 | -1.24509 | -51.74965 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac6ed4e-a842-3a1d-a516-159ba601fd5d | -2.11027 | -50.12816 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47b99dd2-489c-3001-a994-0ddff7f87c4d | -1.2137 | -53.69915 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddb178c3-2fab-3639-9dbf-986cfcac89cd | -1.23024 | -47.35664 | 2024-11-21 04:53:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ddb289-1fb5-3bcf-94de-65b1be95b191 | -2.05386 | -53.43527 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe5d3cba-1586-38dd-b481-ec07bdae8643 | -1.20657 | -51.75457 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a1c37ea-540d-394b-a4da-c24b4d36de9e | -2.74123 | -47.54226 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fc90779-77a0-37bc-bd4a-e90b9c15cd71 | -1.34353 | -51.3946 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b4eec67-7ad3-3c7f-85f7-7499dbd4c114 | -2.01754 | -54.52873 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 82fe0a05-a27c-30d3-b889-52cf4bb048d5 | -2.14424 | -53.57267 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52e5f48-192f-3b8c-91cb-79e3ba297de7 | -1.2183 | -54.18977 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba5fcd36-6384-39a9-b41d-335a846c722c | 0.41043 | -50.81916 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bd97a21c-7c23-3214-b64d-111b5749ddf8 | 0.81959 | -50.25369 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbb88c37-161d-3c10-843c-161e771879e6 | -1.57942 | -51.27407 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cba4bcf7-8372-39d8-9cfc-d7f04997e1bc | -0.91378 | -51.73848 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a34884c-2f8b-3be7-8b6c-643e4ed482f0 | -1.62317 | -52.41325 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7bbd301-b362-3794-8a85-825d8de647b8 | -1.63979 | -52.61039 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f1c05b1-1856-318a-95eb-815859e4e0a6 | -2.92465 | -48.33496 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0164219-60ff-3c73-9ef5-390e56408eb5 | -1.70015 | -55.09781 | 2024-11-21 04:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a604e4d-03d4-39c0-808f-041a6d2bdaeb | 0.61727 | -51.77369 | 2024-11-21 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05fe3963-217b-3e6e-8e79-13c28f9d0edb | -2.35787 | -49.0722 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba221ff3-7c5f-35e4-bc01-5989c64f3c43 | -2.62627 | -48.48593 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9834b9a8-dc2a-3d67-b02f-d8d1f33c3d64 | -1.62595 | -52.59059 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 405dc756-8502-390d-9ccf-7a8cbf0c7865 | -1.96704 | -48.389 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6e1fc62-309e-3ec3-9141-d2278915deb1 | -2.20504 | -50.54494 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11343caa-4ac0-3efd-a8ab-0e1a2dcab31a | -1.32108 | -55.45819 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c52e5642-f5cd-3ee5-9e50-258ec43d96a6 | -2.25151 | -48.16199 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8706e950-7873-3270-9d3c-3e52954a97c9 | -1.6592 | -53.783 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d30e3c66-dada-3896-980a-5e8bf6d4465a | -0.92064 | -52.68866 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc80b227-e119-3cd2-bfb1-e935eeab041d | -1.83115 | -55.04561 | 2024-11-21 04:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7e0a1bd-0a66-3681-b55b-dd98125145c5 | -2.69715 | -46.24752 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 030e8fda-b173-32e5-ae75-66263848af12 | -1.21444 | -51.79198 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f168087c-92b8-3f90-9bfa-7ea34c9c1941 | -1.58093 | -50.43824 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cbd0dbf-790e-3675-83f4-0b02314eba56 | -1.19915 | -51.97684 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ff8d87-380e-3e39-9395-bbe376437a9b | -2.20172 | -50.6807 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5692ee4-edaf-3e07-a77a-8eaef00109aa | 0.85086 | -50.13538 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d859663b-f961-355d-88cf-8b2b45dd2f24 | -2.14479 | -53.56924 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f99f3cb-30e3-34bf-9bf0-ed4c5ea0fb42 | -1.81689 | -52.69474 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c36aa158-b58c-39da-9c5c-c46011bfb446 | -2.22154 | -50.39299 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a66e4fb-939d-3969-a574-849bef6d2aea | -2.02523 | -51.17911 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c24e79b2-ded4-30d2-b89f-8b945c423c9a | -1.56141 | -51.23037 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a1ff520-50cd-352d-b949-db8d29b983ae | -1.59438 | -50.44432 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b11fcdf-a87e-3308-b556-5d1340082bcf | -0.79613 | -52.42251 | 2024-11-21 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fa724ca-6545-345e-86b9-ec76de53dd75 | -1.62343 | -52.26109 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86ab08c-1763-3967-8cfb-7ccfd0c90af0 | -1.45664 | -52.34866 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c265c25-3520-3da1-a97c-f01b4bd933f1 | -1.21102 | -51.74801 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2801710e-7b23-37e0-bc8f-6952b447214c | -1.33875 | -54.63184 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f532a1d0-94e7-394c-9b09-2a013d4fbf8b | -1.58796 | -50.43932 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a67975c-ae4f-38a1-8f76-8475e09030fe | -2.44466 | -49.03462 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfb5e080-9e62-34cb-9678-bd8705ee80e1 | -1.13695 | -53.66925 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 679569e2-9732-35a5-af12-b7771c27c647 | -1.32534 | -51.68926 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a257f1-fa08-329b-9e0e-b52e604db578 | -1.57741 | -50.4377 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bb850fc-578b-3e15-a17a-62629d7c2146 | -2.24953 | -53.68116 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268ca89d-dc70-3e34-8ab4-a8386699d8bb | -1.14829 | -51.69515 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac369969-a097-3b35-9bd7-e7575cb304a7 | -1.55599 | -53.44498 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f1b6cc-abcd-33dd-992a-464e31192126 | -2.24622 | -50.51431 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a95c3bd-e910-3890-a340-4453789ce9e7 | -1.74364 | -52.05725 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50ef575a-054e-302a-9089-26f5fd6626ef | -2.62217 | -48.3259 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f27d7efb-37ce-31b1-8882-82bf1efcbaac | -1.23095 | -54.08724 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6956447f-55a0-37ba-82f0-60d2b86df7c0 | -1.14185 | -53.40167 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e34d9ba3-ff35-34e0-af4f-c8f636093825 | -1.51144 | -51.19258 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97a8e948-ffa9-3130-8caf-7b99b9f48a39 | -1.55402 | -51.23299 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7fd0d60-8e5c-3528-ad89-889e25bde5bd | -1.46087 | -52.68853 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fc5985a-3358-3036-8d22-a8fe455c89d9 | -1.34213 | -55.43779 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c57d5d6-2c1f-3093-b664-ac66e6136db6 | -0.27508 | -51.38943 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ffa4685-57dd-3c0c-823b-2833f012401b | -0.04985 | -51.2529 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2de8648c-7346-3a34-94ac-88b3ce38fe07 | -1.22448 | -51.79354 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e60c89f-43e8-3e3f-8d65-786329d1c8e5 | -1.10396 | -53.18785 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65f4d8e9-19b9-36a0-9604-39f84f69387b | -2.15595 | -50.4889 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 497b04b6-e18c-3a24-8d86-76c508cb94f6 | -0.98365 | -51.7242 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb06638-cfd8-3594-a698-4318001987ca | -1.64587 | -52.61486 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| edb8b8cb-fd95-35db-a0d6-61deab8281af | -0.9747 | -51.71557 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9567756b-6bbb-35d8-8bb9-18a8a71cf2e9 | -1.68388 | -50.19676 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9617a063-c7df-3b09-aa44-1ff9d2757a7d | -1.57475 | -54.07994 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2d5a61c-9b4c-332a-a06a-90056c31b075 | -2.17981 | -52.13586 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfd9ddaa-f49e-3a4f-ae18-d62aed4a4bbb | -1.4679 | -55.45261 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 690b7641-ab7c-3436-a01b-be44aac058d1 | -1.46415 | -51.97859 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 723d4a65-fa2b-3319-bb1d-b1a50c1f7b0a | -0.88142 | -51.72625 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e00e3eb5-e705-3628-87c1-47d9e46c4554 | -1.60672 | -52.47503 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0141f8c0-9c91-33a6-8439-67cf487b313a | -1.14676 | -51.94396 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b586c67e-4e64-3266-935f-160ec07fddb0 | -2.15258 | -50.69703 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4135e00-8aa1-3597-88ea-d82c1599341a | -1.50234 | -51.18364 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff3adfb2-1d44-33bd-b11f-c511614d2cba | -1.20992 | -51.75509 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39c004e3-fbcd-304e-9e24-7d021052af2f | -2.03532 | -51.18018 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a988c05-adc2-39c6-a807-b91c7ec8df52 | -1.2478 | -51.62275 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f972e2-998f-33d0-9d83-fed1e90ccf45 | -1.43943 | -54.50795 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d4118b1-4157-3ecc-bcd3-9c8f50b807eb | -1.47751 | -52.51828 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01683dfa-109a-3530-8b66-9417b039a41a | -2.14919 | -53.77823 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31777d0e-caf3-399d-b4ea-e05c10d30485 | -1.62824 | -52.61918 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc4109e2-5384-3505-9ab1-c83194495723 | -1.47478 | -51.13419 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3696b354-654b-3a93-a634-885293f417c7 | -1.50119 | -51.97706 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4769dc72-81c0-33c7-87b1-2fc206adf2fa | -2.26996 | -51.1354 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09cc338b-5513-3635-92da-03cd239c1c90 | -1.47143 | -51.11097 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
