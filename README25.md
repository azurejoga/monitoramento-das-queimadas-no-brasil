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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff61404d-a075-3899-9726-9f5cc1d6cd40 | -1.68064 | -45.79169 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24984924-edf0-3952-a983-b2d8745e65ac | -1.13806 | -48.33519 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56e68d49-b024-3dfb-9a17-b86ec0921a76 | -5.85313 | -40.79834 | 2024-11-29 04:04:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 566c3c49-46bd-3b44-802d-75e03e173be7 | -1.92302 | -52.89879 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6461a08-2cbb-34bc-b4ac-068172264428 | -1.91738 | -52.89199 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c89d3806-bf72-3b58-a6e9-8e650de25fa0 | -4.40768 | -50.8261 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d344a2a8-7d78-3311-a852-f5c8156f5311 | -5.03521 | -44.17557 | 2024-11-29 04:04:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7600200-5814-3047-933c-95582de1c4f8 | -3.10863 | -53.81273 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2b0bbad-45bf-3e3d-80ae-56c6156a2cbf | -0.95591 | -51.65639 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba6271b7-ab7c-36ef-a91e-41c7da699171 | -4.66913 | -42.38257 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b91658f5-0400-3a6a-a86c-d3757902a3dd | -3.61696 | -41.64639 | 2024-11-29 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 069006e4-1e8b-3fe6-8801-9df9d7cafb33 | -2.96726 | -53.72544 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d281fa54-6980-3e2c-91f2-bd03289a4ed2 | -3.2009 | -46.56765 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3aa6a84b-975d-3cf1-81d8-6106b379281c | -2.67145 | -46.60297 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0671a615-d386-39af-a6a1-9bf1ea5ab46e | -2.31411 | -51.95753 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7361febf-53b2-332d-b1be-09b1b2f93efe | -4.72928 | -45.44918 | 2024-11-29 04:04:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5267d70-9aec-36e5-9f50-a9451eea810a | -3.46723 | -50.53922 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f0ee329-e162-377c-b566-6bd90f289827 | -1.04438 | -51.74143 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 660a4b64-88be-3edc-848c-59b8d1688352 | -4.6697 | -42.379 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 61e1c12e-a1fb-3e10-9da9-fe8b8fbcca83 | -4.08178 | -47.0312 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf7b1f47-768d-3355-92b6-7b878f2c368d | -3.05418 | -51.30417 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29bcf1c4-12ce-3c64-aecf-ba1f7be2cbd6 | -6.85918 | -39.43193 | 2024-11-29 04:04:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4fa178fa-bfbc-3675-89de-ad92143b2453 | -0.94891 | -51.66019 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9b7d945-1ec2-3b7e-9a4e-cc9835b40dfd | -3.70297 | -50.5158 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61ae750f-09dd-36cd-9df7-43ef990a0af4 | -3.86268 | -50.13091 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 203df644-484d-362b-bd44-0931a9d4a909 | -1.08818 | -53.39739 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7242bd06-e38c-3326-b635-65f826d205d2 | -5.22631 | -44.91681 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3759a375-3ecb-3382-8807-0eaff3b754bd | -6.77952 | -39.05574 | 2024-11-29 04:04:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5fcd1248-9b0c-30ac-887a-f701fd3b3a67 | -2.98656 | -53.29544 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 445edc94-6e82-39d7-a219-fe22b24256f5 | -0.26499 | -51.62485 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2f1bb61-3dcb-3528-af7e-9ebc96869d2d | -3.41086 | -50.16163 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a87307b-e328-3e47-80db-b2c25153a25a | -1.53382 | -51.62046 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 626b7f66-d6ca-3a6b-b1dd-48b52a44fc16 | -5.21811 | -44.92022 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62ae0a70-7400-3bce-bbc3-012da5fe13b0 | -3.33683 | -53.21154 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d37d0f0-4199-305c-8955-eba14686728d | -2.56625 | -51.84195 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2df1e23-a227-32d0-a7b3-bbe1b7655283 | -5.48252 | -42.0729 | 2024-11-29 04:04:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 76a01690-d5f0-3124-b242-349b4d2f8ac8 | -4.06523 | -46.68823 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbc6d852-56db-3ed3-a8ca-469fe94d0844 | -3.81574 | -46.59721 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 958c1133-8055-3266-b5c0-9eb239c34371 | -2.8262 | -46.84599 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66894ffe-5912-381c-8a2e-4a451afe8cd5 | -1.70782 | -52.63599 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8873c83f-78c0-3818-b477-ed1775a888b9 | -2.73003 | -49.87457 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ce225c-6602-38f4-8bff-7372a4e77c5c | -2.66041 | -48.79245 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 8cd80a17-3188-31d0-bab7-38e321638ae0 | -2.98182 | -53.28345 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c0d22a7b-c5ec-3fbe-a11e-19c2e71b1b48 | -3.30695 | -45.50217 | 2024-11-29 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e9ac784-0430-372c-8263-6d0f74c09253 | -1.19872 | -53.87725 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c6bfc3b-952f-310c-9278-5ea106e3482a | 0.0436 | -51.1111 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73b1cf35-c863-3b57-af4a-50d666ed37a8 | -4.07241 | -47.03399 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f96a685-9214-3a59-80c9-7c8114330d59 | -5.75215 | -43.39626 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26297e79-87d3-3afc-a320-0b617c0adb8c | -4.47478 | -44.0531 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e56f3a50-78f3-3cba-95f4-05e49faf4402 | -2.30223 | -51.9904 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35c38d16-3aba-3a15-98d1-ba8bf31676d1 | -3.85655 | -50.1489 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdfc13c3-b2f6-3c08-bf45-55649e1948ea | -2.6063 | -46.83939 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be8a39b6-5ad0-3f2d-8f69-186566cae22f | -1.59732 | -52.28811 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 730d4ba8-2a5b-3ac5-9eff-ad7923f2a490 | -3.61563 | -50.18999 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aeedcbf9-5e97-37c5-b9ba-7fea23b9c115 | -6.09788 | -43.96578 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2499f81-c642-3bbd-9e70-8315a2d81203 | -3.81751 | -44.04015 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b536fca-8689-313c-a0e7-6842df0147e5 | -5.75904 | -43.39735 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f3bf960-127d-33dd-b3fb-7b3cdcfa3ff9 | -2.01325 | -51.19339 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a3ce955-03eb-3692-bf79-88030a1625ae | -4.36565 | -47.24997 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 96a4f2cf-109d-3aa1-b668-c98e42dbe654 | -2.98104 | -53.30455 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 98934440-95c4-321b-a7b4-224c175a5c99 | -2.83548 | -49.88695 | 2024-11-29 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c883a206-fa9e-33f7-9b92-85e6f957b4ee | -3.44928 | -45.86364 | 2024-11-29 04:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acab4f4e-624d-38ac-9349-82519f7e5791 | -5.23004 | -44.9174 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d1896eb6-8cd0-3ce1-8b99-4e4677093689 | -1.91078 | -52.89089 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1994acfe-f7de-358c-880d-bcaca10623c8 | -1.53484 | -52.67199 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90ba7a05-072b-355f-b882-f6cf781d9996 | -4.4828 | -45.92352 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7de43fa9-34c5-3594-aa5f-8e7084d40ce9 | 1.32102 | -50.68585 | 2024-11-29 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9972471b-4b5e-34ce-9ede-96e1b6841181 | -2.2898 | -51.98835 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0885bdf3-1fd4-3b9f-a462-6f84f4d118a7 | -4.47493 | -45.65608 | 2024-11-29 04:04:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95cbe9f3-94e1-3651-ab49-558ee8fba23e | -3.24566 | -50.77406 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 015c854d-1068-3968-b723-3ce6865f3c16 | -4.25176 | -48.06734 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdfe0aec-9852-3a80-8710-640bb7ba5e5c | -1.69195 | -52.44933 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c9da5902-fdc7-362b-81da-e77ca7fcd074 | -3.95834 | -48.08336 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| efd165c8-f858-3c85-b5db-24edfa6149e4 | -2.89232 | -45.25665 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d04fdc2-09d9-37be-abd9-cd3df06e3170 | -2.98306 | -53.29256 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 337aedc6-7490-383b-9894-a05f3878e76e | -1.30673 | -51.96323 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30b89da2-d589-3c57-8b95-908eedd5851a | -3.69024 | -47.13279 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4fe9cb3-29fd-39fc-80a3-7112c6183e5e | -6.09723 | -43.96976 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d51509eb-da8b-36aa-8b5e-c3349c063e0a | -3.27827 | -50.04402 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c57049a-40d3-345c-a57e-9f34756e75dc | -4.18516 | -47.90398 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb87956-e06a-3c66-af6c-9a5469988166 | -2.96489 | -45.22953 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd36e6c8-a580-3688-9976-b0efcef91713 | -2.33476 | -46.8736 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d6d55694-d84c-3741-a466-0b3b721a675e | -2.65028 | -49.51894 | 2024-11-29 04:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe50a2b-5548-3de6-bf7d-89fce055d9a4 | -1.96547 | -46.44621 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b4c5180f-7350-317e-89bb-1509ef8282d2 | -3.0781 | -50.25824 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17458545-2693-3406-896b-9e8443a7a4f3 | -3.69498 | -50.22481 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d5d7912-dc98-3726-8228-55ad98d9728c | -4.23558 | -45.77005 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cee1de1-4c54-38b1-82e5-058cca18e796 | -1.93795 | -52.97195 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bce7a17-ffdf-3435-9778-d9d5f649261a | -1.95117 | -52.97437 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf6bf7f9-6d44-3db1-9228-2115d305fbf8 | -3.96542 | -48.06939 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76ed0449-3df4-35ce-9184-6efebb6d59ed | -2.88128 | -46.83761 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80af50b-489d-3a04-aece-f889e7ef8b7e | -4.33745 | -50.77654 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a06b3f7-3c72-38ab-b489-cb97decd2933 | -1.87901 | -48.54858 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cf519bd-9ad8-3785-a438-5350437e3bec | -3.34169 | -46.61042 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c288a55-0ddc-3564-aae3-4e611e43be2e | -0.83717 | -51.80766 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 086b478e-857c-3e00-b345-1f28953a19e3 | -3.276 | -50.5953 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e0d8f02-a344-38cc-8158-75e2851a52a9 | -3.89722 | -46.49579 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f3043ea-97a1-3cf7-af54-11d2baa95016 | -4.2588 | -42.60625 | 2024-11-29 04:04:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abacb982-3fe7-31ed-bac7-6d9254513655 | -2.984 | -53.28698 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 23c1e260-6495-3ad6-b1e0-6bd59315f926 | -3.05366 | -48.51725 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README26.md)
