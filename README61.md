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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e30b0ce6-5c31-3806-b480-c57bc6bf4a60 | -3.1114 | -53.7839 | 2026-10-08 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 57f80753-4b21-3b6e-b51f-990ecfd283ed | -5.7117 | -53.4862 | 2026-10-08 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e359a810-45db-3aae-946e-2e87902c4a54 | -6.1431 | -47.9214 | 2026-10-08 04:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| e2d3e7f2-a9ad-3d50-9456-ce01156283a9 | -2.499 | -56.0675 | 2026-10-08 04:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 01de816d-ddd3-3bd6-9747-12c50bc96d13 | -6.1617 | -47.9201 | 2026-10-08 04:00:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e51107e1-2ced-3563-bb6f-c3fa27fd6e37 | -8.6291 | -67.0296 | 2026-10-08 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 384cc495-58cc-3bbf-9aea-459385d49fdd | -2.7797 | -54.0736 | 2026-10-08 04:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 272c2f06-96cb-3a96-93ab-a61f569d0acf | -5.7376 | -45.1533 | 2026-10-08 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b54055f3-6fe4-33a1-8395-8302cf85516b | -6.1429 | -47.9432 | 2026-10-08 04:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ed0a29a0-6955-395c-b3fd-19f1d385b1aa | -8.6107 | -67.0116 | 2026-10-08 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 44ba01b7-5f7d-3b95-80bd-3ccdf99638e2 | -3.531 | -54.6757 | 2026-10-08 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 24f40905-bfa9-3a4b-ad1a-1dc0104ade2a | -3.11 | -54.1862 | 2026-10-08 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2857a5b3-6363-300c-a92b-a838a1521d51 | -3.586 | -54.6941 | 2026-10-08 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7c3da243-3300-3dda-bad0-d56af74ab4ba | -8.7231 | -45.1583 | 2026-10-08 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 22bfc9f9-90f6-3dd0-af85-b5da5d49b19a | -3.5861 | -54.6741 | 2026-10-08 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 744b92f4-9fe0-3a56-9723-8483fad378ed | -1.41107 | -48.93553 | 2026-10-08 04:00:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7b9bc13-4ae2-33f3-b3b9-f2dc87adae46 | -2.46734 | -46.02238 | 2026-10-08 04:00:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d4a55e5-6b71-3690-863d-6d3580b1b5cf | -3.16954 | -48.61609 | 2026-10-08 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbe3d730-0495-314b-b776-bfec21c3ea6c | -2.46655 | -46.01788 | 2026-10-08 04:00:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f28bdfc7-16d6-31d2-b23e-d0095ca0d507 | -2.47111 | -46.02172 | 2026-10-08 04:00:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02c77b6-f1db-3a18-b8bf-fb440994430e | -3.47475 | -44.24083 | 2026-10-08 04:00:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b640915-fd62-3709-8808-0e88419524a8 | -3.85078 | -44.89835 | 2026-10-08 04:00:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0136d604-e0b2-3ea6-8019-19806e829fb8 | -2.37407 | -45.71137 | 2026-10-08 04:00:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 969e4664-dfd1-3dd4-8627-85c4e392a3e4 | -2.46605 | -46.02085 | 2026-10-08 04:00:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 542c3cda-a186-31f7-90a6-4447454fed52 | -4.49384 | -38.23422 | 2026-10-08 04:00:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c3c011a-e8f9-34d9-901e-f130cc933fc0 | -3.23869 | -46.96539 | 2026-10-08 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4acd8e30-4304-3e44-a829-f865df5495dd | -3.43602 | -44.33739 | 2026-10-08 04:00:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99f9a6a7-f436-3e81-bef9-26fdc1097cea | -3.81545 | -44.60309 | 2026-10-08 04:00:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb2a1e00-4272-3e19-9558-6deb132e28e5 | -2.25792 | -47.00804 | 2026-10-08 04:00:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98af684f-ecb1-3b31-838d-9911554ac4d9 | -4.72563 | -37.84392 | 2026-10-08 04:00:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9f411a66-04f7-3b4a-9137-a59294b1f79d | -1.40565 | -48.92952 | 2026-10-08 04:00:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cecbd83-90c6-314c-8ad9-34620b0025ea | -2.69312 | -49.05083 | 2026-10-08 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 055e391d-471a-38b9-9d4f-5405792e3315 | -2.85621 | -49.54722 | 2026-10-08 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf61b450-68c1-3063-bcd4-db1b54ac6a0d | -3.23924 | -46.96214 | 2026-10-08 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b320086d-005f-36bb-80f7-45b23573959f | -2.32025 | -44.80558 | 2026-10-08 04:00:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22d3e314-5496-334a-806e-e4bf73aa9bdd | -2.46782 | -46.01941 | 2026-10-08 04:00:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6439df80-c7d7-3288-bfb4-0634dac7d873 | -2.26958 | -47.87669 | 2026-10-08 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceefaf7c-94b0-3cb4-9648-6ddcfe103ca9 | -3.29194 | -42.28612 | 2026-10-08 04:00:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61eaa7de-a394-3c1f-ac67-29b517413b66 | -2.36206 | -48.88516 | 2026-10-08 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e031b8-1636-3b91-a4ae-beb7b3a0954d | -3.2923 | -42.28877 | 2026-10-08 04:00:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cea512f-09ce-3fb3-b4ee-1d381d124946 | -3.13215 | -49.24885 | 2026-10-08 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6acee3d8-ee5f-3116-a232-3972f4e225e0 | -0.08232 | -49.48485 | 2026-10-08 04:00:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f2656be-82cf-37a7-8ecd-b3b53890eaf9 | -3.51033 | -41.93562 | 2026-10-08 04:00:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cbdef9ae-ed02-3f87-9e40-c5d26f7dbe9f | -2.35592 | -48.88417 | 2026-10-08 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29656e4a-6a98-3ce3-a1ef-5bc8eb06fb02 | -2.85775 | -49.55164 | 2026-10-08 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abf92223-ed3a-3b53-b221-e597a7ab7a54 | -2.85535 | -49.55242 | 2026-10-08 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 218d75a1-3805-321e-8b39-70ea881a4cdf | -4.01515 | -38.2538 | 2026-10-08 04:00:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f3f2737-0dc6-3914-bfee-e3a16982d57e | -3.24455 | -46.96322 | 2026-10-08 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0fab052-5e24-3672-905c-94817b677a90 | -3.7067 | -40.8404 | 2026-10-08 04:00:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 44adb8bd-4f4a-3302-a597-65986c1ef10d | -3.46962 | -44.24441 | 2026-10-08 04:00:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f526bf3d-166c-3880-98f6-2bb7cec55e75 | -0.0833 | -49.48994 | 2026-10-08 04:00:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da46492e-7ec0-364d-8a31-96b1440c0b6e | -4.10123 | -42.50026 | 2026-10-08 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 70b4a0ca-54ef-318c-8fb3-9b08a4a0443f | -2.68617 | -49.0545 | 2026-10-08 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9167f177-7227-3758-9d34-d12e9c7358de | -3.70378 | -40.83579 | 2026-10-08 04:00:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40c38736-3107-34dd-ba6b-7d184f8cdfaa | -3.70735 | -40.83635 | 2026-10-08 04:00:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3255d544-7933-31a5-bf24-627e9a9687ec | -3.13296 | -49.24398 | 2026-10-08 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d0f4fc7-5790-376a-8989-94d7946be9d0 | -0.08418 | -49.4843 | 2026-10-08 04:00:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecbeb7e3-16b0-322a-af84-0b1775e113fc | -3.47404 | -44.24514 | 2026-10-08 04:00:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07d308a6-cf02-3877-89c0-7865995f9429 | -1.41188 | -48.93058 | 2026-10-08 04:00:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebc01899-a50e-34a9-b86a-8b3c726dc4a5 | -3.23977 | -46.95894 | 2026-10-08 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| af2b8a9c-2226-37a0-970d-44459cb4cb4f | -0.0889 | -49.48594 | 2026-10-08 04:00:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ca41b0d-80a4-37c3-bc9c-f51aefa32679 | -3.20028 | -42.96412 | 2026-10-08 04:00:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e6d8de4-8b0d-3ad1-b715-b5eeda4f7dd2 | -2.85865 | -49.54644 | 2026-10-08 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9dd869e-91ac-3f2e-965e-7726d6617fe0 | -3.47033 | -44.24009 | 2026-10-08 04:00:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f375a28f-16de-39fa-a417-0be9dbc2caf6 | -3.16358 | -48.61511 | 2026-10-08 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fa66530-55c9-388c-bf79-1aae7d7cec57 | -4.01846 | -38.25432 | 2026-10-08 04:00:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 796ba8c4-87ad-307f-866e-f9a0bee398a1 | -1.40484 | -48.93445 | 2026-10-08 04:00:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba241179-049c-3671-a51a-9d7045e75257 | -2.26386 | -47.87555 | 2026-10-08 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03685937-3a1f-368d-aa55-28e19f9c4df2 | -3.24509 | -46.95995 | 2026-10-08 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73b45a22-ebdf-3adf-825f-d2a50d5e17fe | -4.31659 | -41.23818 | 2026-10-08 04:00:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76562d1e-4edb-3af5-9e2e-b66d72f6bf84 | -3.23443 | -46.95807 | 2026-10-08 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dcc013f0-0613-344e-b56f-e5bb9168d389 | -3.19852 | -50.56102 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9c217ccd-c5d2-3412-9f7d-276cc3a75d9a | -6.15481 | -39.43134 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 852b19fd-9272-35db-9f4d-37f59626631c | -9.91986 | -44.80351 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46e886a6-5ec0-3817-a7f0-682d75dd1feb | -9.40087 | -49.00957 | 2026-10-08 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11cc0462-6e7c-3513-9827-169bef162878 | -5.4833 | -42.84966 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 633b3ac4-f52b-3dec-825d-b62455587787 | -6.6023 | -37.89793 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e6f6aa3-5d7a-3749-ac17-4be30c539037 | -11.85958 | -40.20136 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25de46fe-8617-3ef7-a5c4-ea368543e9cb | -6.83151 | -39.55764 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18727db8-025b-32ed-98f1-cdb0d3d8f02a | -3.25953 | -50.40304 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf3be9cc-922d-3dd6-80ef-0de286a97bf6 | -4.35448 | -43.79208 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 32ca995f-737a-3da4-87c9-4c40df0b6204 | -5.73476 | -41.75742 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0d30b274-d4e6-3689-aba6-c36fe88b5745 | -4.77422 | -45.79062 | 2026-10-08 04:02:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ecacaf8-3828-3bbf-a6d8-c2e29a62bc9b | -7.60523 | -46.76189 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88d9cc2a-173f-335f-9744-b94dd9a136ee | -5.51171 | -42.82376 | 2026-10-08 04:02:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1386044-78f8-3d85-8126-fd7fb7a7e225 | -3.1872 | -50.56454 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95b8570e-b1c2-38c4-b6e2-82ebe03abc12 | -7.70375 | -45.44001 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f3fa318-c81a-33a9-9e70-ea506a9cac51 | -11.22713 | -44.87735 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da0cea1c-14ec-3077-a555-21f118143676 | -5.47923 | -42.87327 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 42fee2c6-b6d8-3ce1-9eba-4eeba333870f | -7.77119 | -43.81076 | 2026-10-08 04:02:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04baf74e-9066-372c-89ae-ef2dfb548095 | -5.49975 | -42.84724 | 2026-10-08 04:02:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4ec69d7-78e8-396e-92ce-d2ca2d328c02 | -7.39753 | -44.47523 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc70f87-13de-3459-a5f6-96dc1d0d0902 | -5.87341 | -50.10177 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9446e0b7-e536-3d35-8f54-3ac130d3f176 | -3.86062 | -50.41767 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc97453a-d265-30b1-a0a4-c73985a0a797 | -7.27751 | -46.80936 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bdcd6073-a156-31f1-b0c5-24f0f67ca1d4 | -6.64722 | -43.76501 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 423be3ca-3f66-3c6e-a953-3eca6613559d | -7.8855 | -44.24055 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63b2a67b-dcb8-3bdc-b3be-afc8e3d0aa5f | -4.80929 | -46.82628 | 2026-10-08 04:02:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 597640fc-c4c5-3805-abbc-7e7085ec68df | -9.14339 | -45.83573 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8240cff-fb42-30ff-9a8c-cf4fa0f90f7f | -8.71097 | -45.21213 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README62.md)
