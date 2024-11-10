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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afc1b220-a61e-3164-99d4-cd895ed498ec | -4.8936 | -45.43937 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e7a5056-fbe0-38b5-9b60-70aadc13150b | -2.23715 | -53.77598 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 257e0180-3ccd-32d0-a173-a32a85695287 | -3.98976 | -46.41453 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1dadff53-5707-368f-919d-e5096fc62dc5 | -2.81043 | -52.53826 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4d6f5103-7ccb-3451-b625-e71bdae3dbf0 | -2.87586 | -50.40778 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8cc0f810-ad05-327a-93d2-d638f87dce99 | -2.23084 | -46.61381 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eae8644-4840-3da4-a337-447d98298e86 | -3.95849 | -48.16413 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 44ea0e40-b628-3736-a7df-dd7f1f615687 | -2.50899 | -46.31001 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1014df6-ff3e-3f40-8048-4e648973acc2 | -4.85171 | -48.64746 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ef4ff02-fd15-3369-8eaa-a8c25d9e3a63 | -5.91349 | -44.61483 | 2024-11-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d10dd2c8-c71c-3bc0-b5f2-4f72e02d769a | -2.05724 | -46.09546 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03276a0-c1b9-3dea-a858-ff1c8c39e3d9 | -4.31245 | -48.65174 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc06f9ee-ef65-32e2-a9ec-3205aee3ca0a | -3.10587 | -49.42154 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6b59b06-60ad-37cc-af0c-48ebecfd3ecf | -3.60106 | -47.35055 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c917fd97-965c-3cc8-95f3-7d5774180174 | -2.54735 | -47.12367 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d274e7f-9cad-332f-828b-8af5f188cf9a | -4.01573 | -43.66587 | 2024-11-10 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99e04000-1fa7-32e9-bcf1-89015415e5d6 | -2.15925 | -48.75076 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13d07a7c-5384-389d-b0c4-d61f2dcefb2b | -2.87345 | -49.37474 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73e6bebf-d911-3c68-8cad-dacb2d7f4533 | -3.44699 | -51.4692 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f12d6c1d-0500-3718-a655-c256d33f9754 | -2.52478 | -46.30778 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 226ffbd5-e551-3fd7-854a-a683cf8d77b2 | -4.31839 | -45.66093 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33dcdc2a-7d83-3ae7-b107-7c35817a30f6 | -2.72806 | -51.74105 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d49f61ed-bcb0-3b2e-9c12-5f0d51873db9 | -3.23361 | -50.26069 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35d4b31e-9f32-3d48-8e8f-5d32d7053a23 | -3.0222 | -51.52918 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4bce221-367e-3dbe-921f-511ff9e71f3d | -2.11487 | -50.56845 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 612f99fe-bd9c-39ba-8dc3-f67b635a5686 | -5.51087 | -41.68314 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d71744b-f253-3d06-8cd9-6f47b0d11a80 | -2.90275 | -51.46904 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa5acc31-b0d5-34a2-8636-84207548350e | -3.94919 | -48.14326 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 902c5c06-97d6-3ac3-ae08-98359347804b | -3.24842 | -50.31418 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 26e173f8-a355-34fe-8c89-36b45c5f845d | -2.94998 | -54.68526 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79806962-48b6-3023-b31f-020c39156784 | -2.36758 | -46.86116 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43cd4f9e-553a-3c79-bf9e-6b8f3b5f7270 | -3.17639 | -51.31092 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 989e102c-f233-38e7-a2a3-a4fea08a0ed0 | -2.48429 | -48.80689 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c93d675-5736-3f7c-818b-688bd72f4144 | -2.10937 | -50.57058 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 238cb017-9769-30b0-980f-456e9d21d899 | -3.78804 | -47.46304 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d9955ed-093d-396a-b714-f6eb1bc26ea2 | -3.13832 | -50.44493 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.7 |
| fb9afa86-6090-39e2-be78-a44c5a6abca9 | -2.06494 | -46.34268 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33734e65-fd5b-3a9b-8652-beeb1d4d9946 | -3.3034 | -50.13349 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8dfc2f8-137d-3246-82bd-566114a6bdaa | -3.26568 | -46.3147 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9778b8e-cd7a-32d7-9976-b4087f0a571f | -3.8718 | -50.26456 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ded50cc9-e23d-3e5a-ab1b-ad4c8df3be84 | -2.23229 | -53.77306 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 210db61d-6a0f-3acc-a937-d42df472ed74 | -4.47022 | -45.66249 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8b9752c-b806-3024-a7c3-36e9a8812350 | -5.36577 | -48.24466 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1334f3c-086d-3a1a-998c-bb8cf88b30a8 | -1.67292 | -52.05787 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0f439e2-6b88-354b-96f9-8b1f4c98c89e | -4.0159 | -48.29378 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c3e0a4e-a1ef-3f30-97ac-066f028a8043 | -2.69178 | -51.69347 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07d3bca8-7a32-338a-91c2-27e8c9078765 | -5.563 | -43.97445 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7e8442b8-94ae-3413-8451-3d90e226741e | -3.23544 | -50.45111 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06cb25a4-47a7-3bfa-a86f-e6b2629723a1 | -0.40775 | -51.48439 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46795764-4cbf-3df6-b8b8-d9ecc81f913e | -2.61384 | -51.74734 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10be3cd8-d4b1-3e10-a0f9-646a37e36568 | -2.3153 | -46.4532 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f65a1230-cd87-32fb-8921-1dfa9256743a | -2.92335 | -51.47567 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cf036e66-300d-32f2-b6a2-d85c94e50f52 | -5.27466 | -37.94681 | 2024-11-10 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b69e3fd1-3bca-3966-badf-3279c100bfec | -2.66398 | -49.89301 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 437bba6c-df9d-34f9-9858-764743536f00 | -4.89751 | -47.47129 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fb43901-2824-3593-807e-acbb41a40087 | -3.48292 | -54.5854 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12f90f2b-0a3c-314b-8f16-381dfc458754 | -2.09612 | -48.83092 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 40102cf9-bd6c-3829-8224-f4281c16804d | -2.25298 | -46.50098 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 918ece9c-e4ce-3227-9915-40bb350a95ae | -4.43636 | -44.62256 | 2024-11-10 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e5d0a17c-eef0-3804-b215-dd579f8a8da6 | -2.15231 | -46.69757 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85f26e33-5c44-3b40-882a-45daf682c820 | -3.75128 | -49.89994 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21f67c3d-2492-304e-b4dc-421b51f4a4d9 | -3.10362 | -45.77974 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b047e21-1923-3a20-9864-c13563af0533 | -3.45382 | -47.67163 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87dcb858-7bbc-3514-9b61-18f59c601d88 | -3.26372 | -53.7081 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c77baded-8748-36b8-a0cd-2d0202f4b2fb | -2.18482 | -48.31421 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93067912-cb1e-3ec9-b519-4d8c0f2a9aae | -4.07603 | -50.0152 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 194db6d9-4946-305e-bd3d-452b1ea89ce5 | -3.23872 | -50.31261 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e59a43bf-bda6-3a76-8955-b78041c7eedf | -2.87184 | -50.4015 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12556a11-e861-3cc5-be24-2aa2486fcc07 | -2.92759 | -49.35928 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7097cad-ae47-39e5-a0cc-e2325682fe2f | -2.39302 | -46.77531 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7abb08bc-90f0-3c59-a0e5-53fe66004c2a | -4.10052 | -45.70279 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ca31511-34b3-3a87-95ec-a215261f33de | -2.56536 | -46.5387 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 972bcdab-cb8c-30f4-ace9-da51b7e9ee1a | -4.20782 | -48.12336 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad566e61-5107-3731-a632-4104d6e55c05 | -3.95863 | -48.98648 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0477bf0-a521-35a9-a079-8613777fdf55 | -2.07798 | -52.04273 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76ec7194-168b-33da-b810-625ca9332bb9 | -2.6353 | -46.80122 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc18545b-d460-3c6a-b9f8-e56822daf99a | -2.09237 | -48.82581 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 27c32c88-aa1c-34bd-9746-f99bc9e69d2d | -3.60188 | -47.34539 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3123c753-9bf8-39af-ae34-a7d9a3beec33 | -1.18007 | -52.10247 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4536364c-4d1b-3624-aaff-a4f1bdd511fc | -4.28403 | -48.19242 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38ab6ec1-adc9-391f-a5ad-6e9fd1d70279 | -3.52586 | -49.98079 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf25ea09-f67a-31b8-8cf9-2e03da03b9dd | -5.84299 | -42.48698 | 2024-11-10 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a56e268b-c5c7-3b69-bce9-3ce1cf380c95 | -1.53443 | -52.20906 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 04249894-a93e-3c1f-b89f-8c3234724169 | -3.81114 | -49.94487 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4046439-c3f0-3c3e-8781-4d00462e3ab8 | -2.56154 | -46.53812 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906d6be6-9b18-3234-9255-5d466b592209 | -3.19212 | -54.31962 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dbd998b-f914-30c8-8d26-91ba7dcc8814 | -3.22499 | -50.31395 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1a201fb-1257-3c6b-ac59-5a91806f3387 | -4.11416 | -45.70904 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e01cbd3-7942-3eff-86d8-1e1e238fa4f1 | -2.06568 | -46.33807 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bd77305-c6d2-3ec2-8bfc-8d5e3505b382 | -2.91379 | -49.24335 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 484cf545-1afc-3dec-b9b3-200365ec8641 | -3.30165 | -45.66817 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454a7b4c-0f9d-37f1-a880-dc28a4779cb1 | -3.25102 | -48.75407 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85eb1803-02a0-3535-82a5-ac5cd0001764 | -2.65405 | -48.47707 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86da7aae-8f3d-36c6-acbf-c96e1b568666 | -4.63348 | -49.08453 | 2024-11-10 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3025015c-1502-3a84-aef7-1754d31ddc22 | -2.63056 | -49.476 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f91f030b-cbbd-3b13-a1b8-7061a254ee70 | -2.93724 | -52.7765 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 04c7affe-b534-30d1-bda5-401a17ddcea6 | -1.2208 | -51.77833 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe2e2b2d-e5f3-3e1f-aa26-9669d767d586 | -5.56683 | -45.43581 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6adab0c6-bb38-33bd-a3e4-68b01cf2e463 | -4.25268 | -48.54118 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a84b3fc6-f336-3c41-9aed-9559d78ba20c | -3.14672 | -45.95962 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README36.md)
