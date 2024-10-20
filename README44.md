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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fd3653f-79ad-34c7-b2f5-81290623d1f5 | -3.05095 | -48.01939 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 551a21e8-c409-3e1a-928f-6444bc933277 | -3.04681 | -48.01877 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3cdf2b-2f42-3660-827a-4311a53f605d | -2.97893 | -47.92031 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f508b011-5daf-36b6-8a39-4d6de62bf4dc | -2.97477 | -47.91971 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| af3fc563-ad09-3985-9a19-054dfbf9dd82 | -2.80179 | -48.68837 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8c55888-b0a2-3355-a7ae-d85fde34f9cb | -2.80143 | -48.68512 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cecfabd-cdfd-3ec2-a152-11d673ca7988 | -2.79863 | -48.68274 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 175c2f1d-5926-3bad-8475-23f7c4d6deab | -2.79824 | -48.67947 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4263b743-d309-3cb3-95bc-07016fd909c6 | -2.79784 | -48.68778 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c169866f-34bf-3981-9343-37e83240467e | -2.79748 | -48.68451 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 80c04afc-5d5a-3873-ae19-c4405592639b | -2.79547 | -48.6771 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cf418da3-3cbd-36ee-8486-e9541c1e19fb | -2.79468 | -48.68214 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fed43801-4a12-3db9-8ab2-50bbe51852c0 | -2.79429 | -48.67886 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ef3d120-8f20-3da6-9674-28b65a056833 | -2.79354 | -48.68391 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 81180b07-1177-3104-afcf-d774a2f4cc16 | -2.51771 | -47.4865 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b614c23-19ce-3bb0-acd4-db0731bf7596 | -2.51343 | -47.48597 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b7bf773a-baba-39b6-a308-a4a3c9416b50 | -2.51283 | -47.48992 | 2024-10-20 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d07bc0d-8fcb-334a-ab83-cab0048e0655 | -2.50268 | -48.31163 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a245262-d5e4-3605-bf4f-7b2521a3d41c | -2.44037 | -48.50402 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a11229c-d9c6-33b2-b947-ec266fbfe460 | -2.4364 | -48.50342 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f00c7e-9bd3-30a3-bc71-596e713ca557 | -2.43502 | -48.48575 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 498cb96a-a09b-3059-b915-9d301ac498a3 | -2.4345 | -48.48916 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231b9779-cda1-329e-95c6-da88cdf41553 | -2.43104 | -48.48515 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 867ab5e7-8f07-3a6d-93f8-edae19ad593a | -2.43053 | -48.48856 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05ac93ea-e32f-365a-9cbd-bc2a8e1dbe14 | -2.42073 | -48.52634 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67751e3f-9209-30f1-84fe-fedf4142caff | -2.41978 | -48.45189 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d93c807-31a4-3e24-b016-a599e252a29b | -2.36881 | -48.2914 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aee62e4-47c5-3d44-abc7-cd5008ebfaa4 | -2.36478 | -48.29078 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 031b2908-3a1c-37a2-b80c-561759cb37d5 | -2.36425 | -48.2943 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbdbb415-d15b-35bd-b1b9-dbfe2d158c1d | -2.34639 | -48.80609 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07cae8e5-c879-3fdf-b851-42f6876331f0 | -2.34527 | -48.80881 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be2925e6-4285-365e-a653-716948750901 | -2.31974 | -48.84485 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 645fa811-303f-32dd-8bf2-0f4462cf1285 | -2.30301 | -48.58936 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 287d3323-a776-32d1-a133-5fbdc26640f0 | -2.30225 | -48.59433 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ea12820-d08e-3dc7-835a-e939ceccdab8 | -2.29982 | -48.58376 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 31d188c2-e99f-3c32-affc-907e93aeaee7 | -2.29906 | -48.58876 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| e1353e56-fb9c-31b2-b5cb-3669a1862d11 | -2.29831 | -48.59374 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78feb998-2967-3e68-b776-b97aacdb02a4 | -2.29512 | -48.58816 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05046232-d650-3f99-bc2e-17c90430efbf | -2.29437 | -48.59314 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e30f104-0f07-3e5e-9d0e-c9047b3014f3 | -2.29043 | -48.59253 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f29e1d46-4114-3342-b441-49f95c58ffd1 | -2.1852 | -48.78196 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 275e9831-2a82-3d20-83fd-f02bc7a53920 | -2.18417 | -48.73674 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57692e51-9035-320b-9880-141e7e757065 | -4.89947 | -48.28644 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2388df44-0d06-3ae9-881f-6ecfd4092b6e | -4.89586 | -48.28206 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fdf1608-633d-37ca-ab6a-c54aef9d21e1 | -4.8953 | -48.28579 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d610b5b3-91bd-3f89-96e9-d1290d7b54c9 | -4.89448 | -48.56365 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc40d406-1929-3191-9c18-cad044d1dcd3 | -4.89037 | -48.56306 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3569263-1cdf-3991-b959-72979039487b | -4.87574 | -48.21633 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1423d948-03af-3003-a373-b7e9259901e4 | -4.87278 | -48.49059 | 2024-10-20 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6519d50d-3c36-3496-9c0c-8e2b035f5952 | -4.8721 | -48.21197 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7313c44-e98c-39a1-8ac5-b3557cf0e4dc | -4.87154 | -48.21572 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d19b24c8-6248-32c1-ad93-1f513def93a4 | -4.87098 | -48.21948 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 52c579c7-91e1-362c-8f6b-10b69180e22f | -4.83098 | -48.54485 | 2024-10-20 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a6f7e04-bfdd-3584-bf45-47561ae7bd28 | -4.83044 | -48.54849 | 2024-10-20 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac092b30-3031-3a82-90b6-e1321d48b51c | -4.57681 | -48.01936 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 37eec33b-c200-3d02-9b03-120dace5c4cb | -4.57257 | -48.01872 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6d761a32-c142-3653-a80a-fd621aa07e4b | -4.572 | -48.02261 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b793b346-c868-3d8d-8551-3f43a3a9c36e | -4.56777 | -48.02196 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12d6b8dc-6dd6-3117-a78b-df9ba3f899f9 | -4.56389 | -49.23065 | 2024-10-20 04:55:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cbdac0e-8163-3acd-8799-df122626575a | -4.5631 | -49.23309 | 2024-10-20 04:55:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 659fdcd9-0329-3888-9794-d9e89560f626 | -4.34914 | -48.56869 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc740554-6bd4-3186-b800-bfce9c8836b6 | -4.34561 | -48.56444 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddbee5dd-8c8b-31c8-bc5b-46a6337e981b | -4.34508 | -48.56804 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bb56059-b3e6-399a-b767-2ca2a471f5f1 | -4.34456 | -48.57159 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a005b123-c14f-3f5f-b387-4f4e8f7d8a13 | -4.34371 | -48.71722 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 814a5033-4990-3500-85eb-516db306ddac | -4.34154 | -48.56384 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffcf0ddb-1051-3faa-91ac-3886442d8895 | -2.77925 | -49.30003 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| aae1a8f2-4603-3f50-93cb-b98e2399b4a4 | -4.34102 | -48.56738 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4551ce66-254e-3c83-8b43-204737bb0c2a | -4.3405 | -48.57091 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed462c23-af2f-31a2-83f6-817a8065b2fb | -4.33998 | -48.57447 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b58ad143-914c-3fc9-b8b2-8fe6f5511284 | -4.33695 | -48.56674 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa28dba8-64f6-3ca4-ab71-3bc3ea78da10 | -4.33687 | -48.56791 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc92e8b-c687-311a-92c8-5457a166a6e1 | -4.33644 | -48.57026 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eddac86d-6a86-37f5-9925-6e706f10bf22 | -4.30909 | -48.64075 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55f70fb0-5b09-31c7-a95a-8e8733beeb89 | -4.30042 | -48.33833 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 617b3bdb-4b65-3e64-a653-6f881509bd28 | -4.2963 | -48.33767 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12e77baf-b7a4-3db5-8973-efa465c36e36 | -4.29372 | -48.60569 | 2024-10-20 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31186e3b-799a-3437-9384-d6ec51251a50 | -4.20002 | -48.0257 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ded2c51f-0cf0-3c16-bd1e-2afcd57b0db7 | -4.13037 | -48.28395 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c72c5e68-5be6-3234-b471-9099101a18fd | -4.1029 | -48.24169 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5818b9ec-f7e5-37d4-949f-6906606780bd | -4.10233 | -48.24548 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f178ccb7-adc7-36df-8525-4beabc256967 | -4.10177 | -48.24924 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60fa722d-bec7-394a-87d3-48cb57f73201 | -4.09878 | -48.24095 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c669b2de-5d8a-3e40-abef-0aaccea42e0d | -4.09821 | -48.24474 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d43ac341-757a-3f7c-991c-b25e925fb63e | -4.07669 | -48.27572 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 520e2272-3be7-3ae8-9d89-d3ece6f47361 | -4.01439 | -49.01921 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d6ad860-04f9-3386-80d8-a980b6db278b | -3.97357 | -49.02333 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bdb4f5a-6608-3802-8e07-47568629d989 | -3.9651 | -47.94809 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be0c32eb-8727-38de-a6e5-633b4b1251af | -3.9645 | -47.95206 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e42aa768-8654-3c3b-800e-e008d1a7dbaf | -3.96029 | -47.95137 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97e78524-ebee-3759-bfe3-3a9bc967440e | -3.9597 | -47.95528 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfed0a24-1089-397f-94a9-435bcffddb35 | -3.95609 | -47.95067 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20f5a5f-632c-32d0-8220-bd4a81820ea4 | -3.93687 | -48.92273 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7feae8df-aca3-3b1c-b400-fc59e7e69b5b | -3.93099 | -48.35903 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65394ea8-fcda-3650-8fb1-c01544ab76b8 | -3.93047 | -48.3626 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c643b14-7a62-3206-987d-99b7f3b577a2 | -3.92778 | -48.35896 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d026fe5-5d20-3d70-89ab-d17536941cae | -3.92723 | -48.36253 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b7d0370-b2b6-37b0-8518-b6f58ce9b9cf | -3.91847 | -48.36497 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db26728e-d0c3-3a92-80b6-0a888c6cb64e | -3.91792 | -48.36853 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04002c80-a799-32b9-ac15-9e52098be122 | -3.91382 | -48.36795 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README45.md)
