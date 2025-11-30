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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abf71084-87cd-33dc-9ba0-cb90e15092bd | -2.05921 | -48.26177 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93cd57d1-552d-39d0-99f2-bd16b69bb87a | -2.14149 | -48.52378 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3deb48a-538a-3135-a3b8-7885a8d1e7aa | -3.24779 | -50.69574 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95a21be7-a463-30e7-b607-9175dd2199ec | -3.62655 | -42.75742 | 2025-11-30 04:44:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b05aa6b9-f683-31c3-ae87-333c20a100c9 | -1.88082 | -47.92638 | 2025-11-30 04:44:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b264d2c-2e50-344d-99c0-a91d4f7d0444 | -2.96508 | -49.21332 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e79033d-36fb-3841-b2e7-b486324a070a | -1.67638 | -51.24272 | 2025-11-30 04:44:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6445dc7c-67c7-3571-a8d2-5374364b05f1 | -2.96842 | -49.21384 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f65fe0a-a0c5-3673-bca1-b0236f90e237 | -2.38371 | -47.61172 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa6eba71-9876-339b-9aa0-7d9f69a85575 | -2.51054 | -49.09916 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83334af6-37f9-3a40-95b8-33e0b2c8b87f | -0.95854 | -46.79624 | 2025-11-30 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 245137a5-bb7e-352f-ba07-1962b6ebfc92 | -2.47137 | -48.13752 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d538e8ab-a278-3435-868b-3486fed31047 | -2.63444 | -48.55059 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07af6dbb-c426-3bdd-b024-6c8c18e289c4 | -2.21299 | -47.99878 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 292bf35b-437d-3ed9-bc79-60d029d8bf1e | -2.17482 | -48.42113 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee697115-8c49-3b26-9cdd-55fa16ce0fbe | -2.17143 | -48.42062 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9166093-bdad-3ed0-bae0-17545765b24f | -2.22509 | -49.8342 | 2025-11-30 04:44:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d5e41b0-b2e2-3b0b-933a-30474683fdd9 | -1.88682 | -48.39982 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efbd778e-b394-368f-abc2-9782c1ab1e5c | -3.5873 | -45.62144 | 2025-11-30 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5fbc57b-95e7-3bb9-a0ba-97272d9e2333 | -1.79206 | -48.06581 | 2025-11-30 04:44:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9d52ad5-37d8-3e31-ad5e-18703e34eebc | -3.07674 | -46.64565 | 2025-11-30 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5aa017a1-0e8a-388b-803c-95e3c0baf31f | -1.47687 | -47.75425 | 2025-11-30 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6bd6e29-eba9-3c69-bf90-3cf96dbc955b | -2.50999 | -49.10268 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 941d8bb4-3863-3bff-9f87-e02d8ce37b19 | -2.21226 | -49.76523 | 2025-11-30 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74ed1044-1b23-34d4-bb03-d5d2de225cc3 | -3.72459 | -46.06756 | 2025-11-30 04:44:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832f012c-35e7-34ac-b4e5-0db608d4bf9e | -2.60254 | -47.34409 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f709bb-c705-3a3a-bf21-cc7415e31f90 | -2.70434 | -48.3507 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3f7f685-7584-3b9e-a7af-f6328438675e | -2.38707 | -47.60913 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a22927a3-b37b-3475-9741-bdf03533af4b | -2.21514 | -48.00269 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c538ac7-00fc-3905-baa7-9a6090a371fa | -2.1669 | -48.42735 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d828547-6b42-3c3e-b8d7-44e809c5b471 | -2.92405 | -48.22443 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eafe8671-ca82-3189-968f-f7d26bee2a09 | -2.13867 | -48.51964 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3baba00e-d19e-3132-8c7d-2b8b8c84ace8 | -2.70232 | -49.52309 | 2025-11-30 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d0edd2b-fd7e-346d-8fde-fca7e37bc5ba | -2.54265 | -48.35333 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474de111-74b9-38fc-82ac-b5883a948dba | -2.46216 | -48.15143 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 731b617c-2ebc-34d3-8316-4c9bd78e9028 | -2.39755 | -49.38666 | 2025-11-30 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcface3e-9a24-3488-8ed5-845d99054837 | -2.05862 | -48.26545 | 2025-11-30 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4de46c15-c8ea-3a6d-9dcf-c0d52777d7ca | -2.44813 | -47.08424 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f692e011-4d16-3e69-86bb-1cca03eb892d | -4.52168 | -44.75237 | 2025-11-30 04:44:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a327c834-9cb1-30b4-804a-437b562a40ad | -0.96213 | -46.79679 | 2025-11-30 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2230b2e8-09ec-3739-986d-02d331bd79a4 | -2.44518 | -47.07955 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b7f713c-78f5-3c2a-ab63-a9aa5bd18643 | -2.83902 | -48.8299 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1c1e03b-a489-32fa-b8c8-50e3210038b7 | 0.61602 | -51.57194 | 2025-11-30 04:44:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab6da86c-d758-399b-be1d-369ca6b037aa | -0.86185 | -48.65319 | 2025-11-30 04:44:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e7b4f91-d713-31ba-88a4-1ca87dc6378e | -3.59087 | -41.66884 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36777a88-0137-3292-8f49-25e49aedd25c | -2.32151 | -45.84342 | 2025-11-30 04:44:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf7718ce-d114-37e8-8592-6211c81dfbb6 | -1.88427 | -47.9269 | 2025-11-30 04:44:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 904e759a-d888-354f-946d-9e635e77b0f1 | -2.85291 | -49.49343 | 2025-11-30 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 043bec78-1f90-357e-8e10-642276a41dd2 | -3.58088 | -41.66422 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 227e9e39-e371-3e6d-83ed-87a75810c5aa | -2.64745 | -48.55632 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c363d90a-37f1-380a-b172-e592ae705890 | -2.60317 | -47.34007 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa17bfd9-0640-372e-92ae-7a55e90c60aa | -2.92346 | -48.22818 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2bbfac35-643b-3029-9b27-c7912d034570 | -2.57239 | -49.09792 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d6fe52bc-1d5f-339f-9d8f-27dbcd1e6ba0 | -3.4438 | -45.41159 | 2025-11-30 04:44:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77948500-499b-3d18-8a13-d00a0942aa49 | -2.38999 | -45.84675 | 2025-11-30 04:44:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f515bfd-b8e9-3e1b-801e-a7eee69d186d | -2.29864 | -47.73863 | 2025-11-30 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f13512f-d3e8-3db0-ac46-126718eae3f5 | -5.11249 | -43.29188 | 2025-11-30 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12f4bca6-f9aa-3c8b-b169-f7c447a12d97 | -4.3633 | -43.163 | 2025-11-30 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eaa2cf18-d786-3606-b7eb-9608088cdcc5 | -2.44453 | -47.08368 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7067e4c5-a7e3-3934-9fee-3f3f94ae2a40 | -2.69973 | -49.32284 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7980aeee-7568-3ecb-b5e6-1603f853df43 | -1.88486 | -47.92315 | 2025-11-30 04:44:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e62df342-778a-3cc6-9fd6-b1cbe3405b75 | -2.89076 | -48.02987 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 803fd589-3211-3849-a714-98f642877896 | -3.22868 | -45.5353 | 2025-11-30 04:44:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a708c27-d280-3e02-9218-48a2b2d0d1ef | -3.35744 | -50.49786 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5036e9f9-6a61-312f-b185-5e34b2d1f458 | -4.36408 | -43.15788 | 2025-11-30 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e683a4a2-24d2-36c2-bcac-c4cd31f4ecc2 | -2.53872 | -47.79812 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aaf4ed3-8e78-340d-b940-97439c5021b5 | -2.68245 | -47.3635 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 702c64e7-96bf-3ebc-a22d-0ec0e686017b | -2.24389 | -46.52004 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d079224a-e4b1-3f0d-8d6d-6b0775c52c8c | -2.74664 | -49.86655 | 2025-11-30 04:44:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 857826da-3669-3427-91f4-d93ee444a48f | -2.63529 | -45.91753 | 2025-11-30 04:44:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3d2124b-fa54-3927-81af-8eeada9acbb6 | -3.2225 | -50.57547 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92b0df37-b93f-3f7e-9402-b6ac4193d9a9 | -2.44991 | -49.01065 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c45ba7d6-648f-382e-b361-a2b07031b7d1 | -1.53271 | -47.21838 | 2025-11-30 04:44:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d690ead9-d942-3efe-b378-53dacd879e0e | -0.93258 | -47.48955 | 2025-11-30 04:44:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 539d16c3-fed1-39da-b6ac-30332395dfac | -2.63892 | -48.03187 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb81878b-9a5f-3c4b-bc64-8f2d7258e011 | -1.57556 | -48.6465 | 2025-11-30 04:44:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7030ca0d-39f8-34f6-a9d0-bea3546a8935 | -2.51389 | -49.09967 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 533846a9-fb46-3b29-90c9-238b475ee256 | -2.70028 | -49.31934 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f82ac71-131c-3180-9eb8-86318e55b7ba | -2.01298 | -46.92495 | 2025-11-30 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 851ce717-77d0-3ffc-b685-46d2ed53957e | -2.69945 | -47.39487 | 2025-11-30 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3ec55d-6b79-3761-bfe4-a7bef463fb83 | -2.45047 | -49.00711 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88521a71-54c3-3b9d-9a54-abc83346bbf7 | -2.19357 | -51.3672 | 2025-11-30 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ca93118-646a-350a-a0df-c7397ddfb321 | -2.50944 | -49.1062 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31fdfcb9-2297-3b0a-a6c0-bd3d8c8034fa | -2.60737 | -49.26162 | 2025-11-30 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dcb9d91-48ff-3adb-88de-49043c7853d9 | -4.36403 | -43.15958 | 2025-11-30 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c86603af-108a-3d76-87a9-2b836d06c18e | -4.41499 | -44.44685 | 2025-11-30 04:44:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8a1b630-d964-30d7-8b96-cd720036c12d | -2.45514 | -50.25003 | 2025-11-30 04:44:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 005988a4-194d-33f8-9ffb-7fdb69c0296f | -3.59182 | -41.66254 | 2025-11-30 04:44:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 210510e8-a938-36f1-8e08-7df5756176b2 | -2.44158 | -47.07898 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a5d7a6c-e2b0-3e8d-91f0-ce071cf09310 | -2.21239 | -48.00254 | 2025-11-30 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 91b42136-3782-3ea9-8f75-aa492d6f6511 | -2.6418 | -48.54799 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 47ec08c7-9ead-373d-af97-4705985ce092 | 0.85197 | -50.18924 | 2025-11-30 04:44:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 069785b0-3a50-3a9c-9003-48ee4dad4a62 | -2.45459 | -50.25346 | 2025-11-30 04:44:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca2aaee6-5b05-3822-917f-7d6430e74812 | -3.62169 | -42.75672 | 2025-11-30 04:44:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 131077dd-ca93-38db-b048-1f9f1519a619 | -2.63219 | -48.54279 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33ef118-ff81-3cc7-a241-ad3576b51c1c | -4.35778 | -43.16916 | 2025-11-30 04:44:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6755ce7a-2b27-39a0-b781-d9e759361d0c | -2.44878 | -47.08011 | 2025-11-30 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c42ce6df-06e9-3052-92a0-5f2dd2bb49b7 | -1.1569 | -48.82838 | 2025-11-30 04:44:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7123a47-0669-3a11-bd1a-5b6203814e9f | -2.63915 | -45.91812 | 2025-11-30 04:44:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 559ba66b-a156-3d1c-ba55-66431c454f67 | -2.63841 | -48.54747 | 2025-11-30 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
