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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccd138df-05a5-3294-aa9a-6c40a6ba2e83 | -1.18881 | -55.72226 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 064c2545-ce18-3c84-a249-5812e56ab2fa | -1.29338 | -51.73103 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cda2efe4-8143-3fae-9e1e-e34905e952f0 | -0.31855 | -51.4863 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b644077-30c1-3c41-a484-d016482db3bb | -1.2611 | -53.36079 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98388492-6a1b-3b24-bf0e-24bff8bc2cc5 | -0.93934 | -51.65508 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1dff56e-ad2e-38ec-853f-9d181b49a287 | -1.94502 | -56.82632 | 2024-11-23 05:10:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e41f70dd-fb5d-3012-b2ac-3454b76eee62 | -1.12438 | -53.39988 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85dbf1a4-17af-3172-9124-7cd3a05778ae | -2.45395 | -53.70072 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 289e73e8-c1d3-334a-9b34-3f061e9471b6 | -2.2035 | -53.75675 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6176906f-f089-35e2-b066-43b41ad446ba | -1.13448 | -53.40565 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ed3043c-d50d-3634-868d-edcee1099d46 | -2.20604 | -53.67011 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40a28653-0055-3c79-8c88-ba221f343ef9 | -2.20648 | -53.75591 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a19c117-2d5c-34db-934c-e7f36bac6ce3 | -2.08225 | -46.28298 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 230d8951-0810-3995-80ed-164dfbf39fcb | -1.50753 | -52.03918 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1295582-7235-3e80-84a9-bba1ed86492d | -2.70845 | -46.09924 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d3819be-9238-321a-8642-232b9275661c | -2.21004 | -53.75644 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91904e9d-21c3-3bab-ac44-d5612dccd69a | -3.15663 | -50.58754 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 346b295e-51fb-337c-9209-69c95f2cd49e | -1.27141 | -52.69506 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37fe8092-ba93-3fdc-8e56-7e943536066a | -2.58021 | -54.08352 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fadcf5c-4cf4-30ac-b296-57af5d39489f | -1.78817 | -53.63141 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b61b36f9-c277-31d4-8cef-df9153c2bfce | -1.20831 | -51.75912 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 786b1256-3b4f-36c4-9f14-c3a402eaebf5 | -0.91169 | -51.65074 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae781f63-3c63-3ffb-b117-669135804506 | -1.73864 | -52.71426 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6b7579b-e6db-373e-bc63-fbc5af17646e | -0.94406 | -51.65063 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8459c8a3-ee04-383f-9eb8-092443f666e3 | -2.71639 | -54.14331 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d1d7f8e-d820-3fbf-a075-87ee621ba962 | -2.26754 | -50.80882 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91fafe12-7b25-3bec-bbb8-0f0d62f75905 | -1.65011 | -53.86806 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6750c4f9-d273-35a0-8428-d5b36b961114 | -1.72809 | -52.70803 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9de2184b-88ac-39a0-a2e7-420472f7a3f7 | -2.68695 | -52.06951 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b9557cd-ff8c-332f-bc51-4ada0453be7a | -2.70337 | -46.2654 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51f84ebf-40ec-3a53-82fc-7f1ff95a71fa | -1.28396 | -54.54268 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34c62709-3b93-32bd-b8b5-5e5899e82382 | -1.24684 | -51.74448 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91b53b82-f6ab-3022-8d6c-a42d60128dcf | -2.18355 | -45.68246 | 2024-11-23 05:10:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2718b041-f990-39ac-b0d0-081bb7cec6d4 | -1.23133 | -51.79352 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60eca530-185b-31e8-8f8a-4120726af875 | -2.74563 | -54.02235 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 238c545e-de62-3b68-b961-291986d8ab82 | -2.76124 | -54.08572 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04d13bee-355a-3019-8f5a-eaa1b2cfbcb0 | -1.99171 | -53.29148 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b467ee4-1eeb-3ae3-9c82-e6af9274a84f | -2.78574 | -51.4108 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 375fb59f-d9ab-3a06-b617-3cba11c6216c | -1.63166 | -52.60297 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0039bf10-7724-3e2f-bf8c-a87e9e546fb3 | -1.73115 | -52.71311 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f9be1e9-c48e-3a06-8bb3-65cc8bf46b2a | -3.70789 | -47.61775 | 2024-11-23 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 753441d7-9dab-3df3-9059-c61e494b7c93 | -1.60722 | -52.60649 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e946aba5-595f-32ec-85d7-8a734092ec94 | -1.62687 | -52.58358 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb49f5fe-561f-3267-9197-13c5c739cccf | -2.56417 | -54.00054 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c239f21-549a-377d-8112-0a807f714908 | -2.1579 | -50.45577 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57b40511-44b1-3740-b01a-462cf979e6df | -1.41746 | -54.90541 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bf5b578-0cd5-3f67-885a-852b67c8edff | -1.47047 | -55.17744 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e36267ce-7dac-3a60-bb6a-f5facaa2e58d | -2.45752 | -53.70131 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3980e8c9-715a-398a-99bf-ff1590108639 | -2.74895 | -54.07169 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e90b03dd-8690-3dde-b4b9-4a8b299d0aa4 | -2.75953 | -54.07332 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef5aab41-9915-3949-83cb-c9e7c835704b | -1.61683 | -53.31343 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ff381eec-c3e2-3c46-9e57-87a78d939a3e | -1.23106 | -51.74205 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6cee3654-3b53-33cc-b87e-1c213c2f518a | -1.20592 | -51.75199 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 15ce8b2c-e15a-3084-9280-e16b576ca0c5 | -2.45927 | -49.03865 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36a268e6-921a-303d-96b6-96a528cc6249 | -3.15682 | -45.21411 | 2024-11-23 05:10:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1988931-9f83-3711-b7b2-7f6cf9aea91d | -1.98879 | -53.13834 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47187451-6979-3c66-8b67-4f7406767ef4 | -2.91379 | -53.06444 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6db08382-b126-3f32-be77-c6b656add26b | -0.26129 | -51.5703 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5436494e-fbdf-345d-ba59-8315fd93ebdc | -1.28511 | -54.53529 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7c88a16-f22c-3082-822f-ed8c2a143d0e | -2.19658 | -53.66032 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0b5b112-6311-30d4-a20c-0a592394b5d5 | -2.76781 | -54.06649 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e56b3f02-0899-365c-8973-15d504c78a95 | -1.63271 | -53.31417 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 323c07a9-8d8a-3555-8fa9-ca9ccd4d5632 | -1.72979 | -52.7221 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b15d1aaf-f608-36fb-a573-9088ee4b4337 | -0.24215 | -51.61618 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c275a24a-160b-3b0e-9073-ac64ff5f4901 | -2.84791 | -53.03419 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fe52c78-51c4-3d8b-8ab7-81c3fe4fb3a6 | -2.57815 | -54.02702 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a438f968-3d01-3b20-86f3-1a90d595d178 | 1.31911 | -50.61665 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03ebecb-f0b3-39b1-9f6c-c435a892e2c7 | -2.20691 | -48.92057 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 35f8942c-9341-3db9-b3bc-47322b5bffbe | -2.18023 | -55.14325 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69f4d5c6-7751-38d6-a58a-17919d2fa235 | -2.75892 | -54.07728 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 677dd364-2d49-331c-8cb0-a7c534726c80 | -1.30839 | -51.73854 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b937850-b2e5-398b-9ec8-b0963e1e8ed5 | -1.27039 | -52.06863 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4867c5f-5bd0-3c30-8286-552a9d90d15f | -2.20587 | -53.75989 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9dd9aa9-8f84-3e1d-8e05-d05ae2e5ec8b | -3.675 | -47.14056 | 2024-11-23 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30356d4a-2760-36d6-92a7-d748b0755eb0 | -2.60193 | -54.06227 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6dc37589-2599-3509-a020-eb8af450c1d1 | -2.58081 | -54.07962 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97ce0fdf-e452-3d6a-9fde-87b263f96c70 | -2.44927 | -53.6832 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19c1c6fd-c651-31b1-bce2-3c27f0ddbc0c | -1.77286 | -53.61247 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b9c64c2-3d26-3541-9cbf-f76f802bb73d | -1.30681 | -51.74866 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e59faace-4aaf-3234-b5fe-e55752a31520 | -2.85948 | -51.27551 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c1e5bd2-4574-3b94-a350-24821ffb839d | -0.26625 | -51.61712 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af6388ff-13dd-3126-8d59-7d34bbb59d64 | -1.62484 | -53.31726 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba04ba95-f351-3cc2-b9f8-65b3e456a5dd | -0.95745 | -52.78066 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 292cc01a-8e69-3e16-b4e8-b15d0ad702ff | -1.72673 | -52.71703 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c14dcf6-6381-3e90-8537-2b8296981b2b | -3.18895 | -51.35802 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7534164-51e9-3d2e-802d-aeef7c644c6e | -2.68618 | -52.07467 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5650816-54a5-3d5c-86ed-4bdae5dac30c | -1.73047 | -52.71761 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd09eedb-1a8a-36d7-8b4c-e9b947a0722b | -1.63474 | -52.6081 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfed5980-af13-3103-8a4e-9ae810600e19 | -1.75041 | -52.38491 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05115fac-9c38-3ab2-a9cf-c7a827f3d9c0 | -1.19962 | -51.76647 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f26ceaba-f8f7-382a-a8ac-9523733824b0 | -2.62151 | -51.80838 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b28659a9-3f91-3902-b0ec-6380fe8f5d41 | 0.79338 | -52.00632 | 2024-11-23 05:10:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9beff5d5-6746-36b4-92fa-6320da0877b2 | -1.73728 | -52.72326 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 85b54ff3-a2ea-3ab5-88d8-7220a51d31a8 | -1.19805 | -51.77652 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be2b3087-ff32-35f9-a4ac-b4f6f7453be1 | -1.89564 | -53.01094 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2de17221-1c6f-3baa-9b6e-41c0396e17a5 | -1.39051 | -55.19033 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d642ad3-1b2d-3e81-9a53-e8f58875961d | -0.7683 | -51.77555 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c4cc52-caa3-30ce-b3b3-c6a79b8a6cef | -1.68018 | -54.99343 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21b5e727-75d1-34f8-8d8f-033c8d5000f6 | -1.92983 | -52.08786 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a4d9009-c071-385f-882b-580415d496aa | -1.78356 | -53.61411 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README51.md)
