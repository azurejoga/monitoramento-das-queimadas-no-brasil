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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea192759-95b6-3316-8522-9d650a195835 | -1.02569 | -53.73054 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c713a4-45b1-38ea-9f71-6257406f1c76 | -1.02524 | -53.73326 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c094e72b-46a9-3c6c-8b85-b8648bde3d4d | -1.02478 | -53.73607 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e6a882a-23a5-3a04-9df6-adc2439ec082 | -1.02463 | -53.72902 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49cb3c1a-e965-3b2b-8c98-bf5beca27609 | -1.02419 | -53.73183 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 209d45ba-026e-3850-8624-6b2d28fc2f1d | -1.02374 | -53.73467 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e9af9ff-9a73-3663-b4fc-b37f34bc5d08 | -1.02327 | -53.73768 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f43b2b5-d557-3001-a051-79cac46dcaf5 | -1.0206 | -53.72911 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 741c8e05-d3f0-30bb-9295-dcff8a5f969b | -1.0201 | -53.73215 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc144a08-8afb-34cd-a871-a63fc2afb8cd | -1.0196 | -53.73523 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e619eb19-655b-3d36-93fb-200fac3eafc4 | -1.01904 | -53.73068 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e9e8c10-10e0-3844-ae1e-22f54ddb55b2 | -1.01856 | -53.73376 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6061c04e-8dc6-3b5d-af96-f3c62f951527 | -1.56943 | -54.76302 | 2024-10-11 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca1e4e50-9498-3682-9221-ddefefdff1d4 | -1.25417 | -54.68463 | 2024-10-11 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0e78463-8863-31e0-bbf1-3be1762af8b5 | -1.25354 | -54.68858 | 2024-10-11 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fa18aa8-2205-3c95-8b72-31cca718323e | -1.19487 | -54.11215 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| abfa0740-5c40-31e2-818c-09d4983f45d6 | -1.19458 | -54.18114 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf867514-80b6-3feb-bd25-b3beb6b454eb | -1.19022 | -54.10726 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 120d4890-b5e6-3b71-a576-9a3a667d85bd | -1.13631 | -54.21548 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d623ae6-bd6a-3392-b0f3-d8f5154a2ed6 | -1.13578 | -54.2188 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f7756c-1af5-3730-890f-bfe0a6b43b6a | -1.11175 | -54.06147 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 548c4c8b-366b-30ba-acae-9d75f2b45912 | -1.11122 | -54.06472 | 2024-10-11 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b258beed-43a1-3644-820c-52476a8401ae | -2.2466 | -53.48493 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e4803bc-f122-3e85-8462-cc54053b9fe8 | -2.10508 | -54.63289 | 2024-10-11 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef266385-1973-3e2d-a8a1-bf326e74c858 | -2.10451 | -54.63636 | 2024-10-11 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f28ab4d-8734-330d-b42a-7097a98bdd07 | -3.66864 | -53.95675 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05a6b6b7-8e5e-3477-a8df-d2d3d5a2e417 | -3.64829 | -54.1611 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a002c5ba-a9b4-3f9c-bba9-d5eccec03ad4 | -3.6473 | -54.1669 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e52fcf5-8d4f-3e35-bfc2-0135915fad21 | -3.57364 | -54.53885 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d0e37a6-6ae4-3033-b869-dd3b5df65cd4 | -3.57363 | -54.53582 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c6508df-6997-3671-a244-de6fbceb9192 | -3.57311 | -54.54207 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372a671e-fa3d-32f4-a0e0-dac3a8f3d5e4 | -3.57308 | -54.53906 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc0c9ab-7192-387b-8d07-c3767fe794d1 | -3.33848 | -54.61835 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a52615ff-9de6-332f-b650-d2f0265be4ad | -3.261 | -54.18247 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a67476ac-4393-3760-a32b-7ac3cc083649 | -3.25489 | -54.18729 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bab0fff-860a-3be8-bf1c-0de9b20501b2 | -3.25439 | -54.19031 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67c28ead-3f40-324f-a3d6-676886bf2dd7 | -3.25337 | -54.19646 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6774305c-2bee-3cfa-b1e4-9c538cb7a0ca | -3.24924 | -54.1894 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bf22896-a4cc-3f5c-9f23-ed25f70f6ede | -3.24232 | -54.13572 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c7e101c-5d6e-3d8d-a74a-6e1894d3112d | -3.06599 | -54.77631 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ecef65a-e799-3d99-97fa-b09745bc27f9 | -3.04056 | -54.27739 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12fa2655-8d04-3e34-aea5-413173a8244a | -2.97243 | -54.62441 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3594e7d-e02b-3b84-a01f-0f653ee96899 | -2.79886 | -53.98823 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b4e00d1-cac1-3b00-9cd9-f3433b0ad500 | -2.79878 | -54.08286 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 263d8394-0e8f-3327-9a25-3f51d8955275 | -2.79835 | -53.99127 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fffdf2c2-4393-3b95-ba86-ddc994e4de90 | -2.79826 | -54.08594 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7206f51-4f85-31c4-86c0-3270b7aebdcf | -2.79784 | -54.07919 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c1dc30-ff76-311f-8284-07211ddc3130 | -2.79735 | -54.08227 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8dcc04d-d8a2-3bbb-89c4-dc791b02f158 | -2.79686 | -54.08535 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 951e47da-e8b0-3a5f-8115-24147a650d1f | -2.79636 | -54.08843 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 536e5e45-54f2-38dd-9417-fac06566e6a4 | -2.79436 | -54.10091 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13cffdfa-72cd-3b5d-82ae-c663cee5e9d4 | -2.79258 | -54.08819 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64eaf187-7b9e-365b-8fc0-645e0aceb1ea | -2.78969 | -54.09695 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f78d869-5bbc-3f81-8019-2867bc46be38 | -2.78583 | -54.09669 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27ef3fdf-691a-3295-8012-f391eaa0b3da | -3.11927 | -53.73575 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 017893e5-175c-3472-95b9-c3928918aab4 | -3.1188 | -53.73865 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a47bfd17-4e6b-3b4a-b2ff-f533ff337f2d | -3.11426 | -53.73493 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8050b32a-df24-3db0-9b7d-e53586eba235 | -2.94945 | -53.70798 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b89c1202-9640-38e0-a202-2cd741b2dccb | -3.11975 | -53.73285 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33dd9fcc-9313-320e-ad15-a80f8de0909e | -3.11378 | -53.73782 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11c08048-7229-3ba9-828f-92ec86bc31c9 | -2.97292 | -53.71971 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd7503a5-fff9-31b6-909a-612b837082f2 | -2.97243 | -53.72261 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fca8a99-0ecf-3e65-9d7f-0323f2eb0e4d | -2.94992 | -53.70508 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca1a13dc-4b68-3dd2-85cb-54594954ac23 | -2.5039 | -54.58851 | 2024-10-11 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 873405b4-5e9d-3647-8012-5ee3d1f35b1b | -3.64778 | -54.16409 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abaddcdc-3cfe-3bb0-947b-99a49d942c8c | -3.64682 | -54.16972 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b20c2ef0-de7e-3960-9b29-02c02cecc6a6 | -3.57417 | -54.5356 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca7b3b3e-7c64-34bc-abf9-026bdfd02b60 | -3.49614 | -54.45362 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f31706a2-98f8-3cc8-8a0d-aa4641a0c3cf | -3.33949 | -54.62177 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2cc06503-7062-390f-8ea5-fac8995f3905 | -3.33791 | -54.62165 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daaf73ad-7ae1-3453-bbc8-1a22b067ec54 | -3.33417 | -54.62093 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cbd7356f-cef3-3d30-9ba3-b961a9f74140 | -3.26051 | -54.18543 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78925c5f-1058-3876-8674-b407d92f59b2 | -3.25853 | -54.19736 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 691b729a-e51e-3eba-892a-913eafac473c | -3.25538 | -54.18436 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63465569-96f0-35fa-a209-3a3f0fa1c1c6 | -3.25388 | -54.19338 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96e2039e-92b2-38a6-ae35-66c173a5d146 | -3.25024 | -54.18338 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 483d2046-e5a4-31cd-b745-6c98f84aaabc | -3.24975 | -54.18635 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 507aa1db-7cb3-3646-a9b3-d4371d9c901a | -3.23721 | -54.13462 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8369ac78-8750-309f-ae21-6fde95f052ab | -3.07139 | -54.77718 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55770a8e-e287-3a56-87fa-e99290f75300 | -3.04109 | -54.27417 | 2024-10-11 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 240ef23a-1641-38bd-9d5b-ff237af43edd | -2.80807 | -54.09075 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e913d193-1a8d-3dce-b2f0-4ae34bbf4d1b | -2.80399 | -53.98908 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 223383b5-7e9d-312a-a946-26e41a223c57 | -2.80394 | -54.08371 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777250d6-5b21-387b-9722-aafaccfbdaa5 | -2.80139 | -53.99128 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 907b0a9e-c7ea-32f3-bfce-645b1e1b232e | -2.7993 | -54.07978 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df77c94b-08e8-3fac-b223-40a1a10262df | -2.79618 | -54.09834 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b16affc7-86ff-39df-b8e5-dce244eac400 | -2.79153 | -54.09441 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4815faeb-08a0-3103-a267-1e512d4e258f | -2.79019 | -54.09383 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eef47b74-8927-3239-b989-b88446299a5c | -2.50446 | -54.58512 | 2024-10-11 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 460835dd-de45-38a9-bbb2-19b7b7ced395 | -4.47566 | -55.09049 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 718c643b-2637-3120-b21b-93ebe53ca480 | -4.47029 | -55.08951 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 647a230c-8677-361a-a28c-1c84231be540 | -4.46971 | -55.09288 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2fb06a4-4e5e-3b6e-be48-acc4255772d1 | -4.46913 | -55.09627 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee505ca5-cd3a-395e-be7f-5df677e0ebd7 | -4.44772 | -55.48248 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd72d1a7-a894-3a69-b4da-2da3fb4a679b | -4.44711 | -55.4861 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a820651-1915-3758-8e09-36b1fe2ab992 | -4.44159 | -55.48513 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 949d1a49-b24d-3732-bbfb-826685615050 | -4.44098 | -55.48869 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32a35fd-eb23-3c14-a182-50f5d7a8deb4 | -4.42053 | -55.23925 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40597e4a-c6a5-37f0-ad61-5db5db0c0244 | -4.41993 | -55.2428 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d4ed71e-c098-3dd8-9924-b50cbedd4b1f | -4.26604 | -55.45303 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
