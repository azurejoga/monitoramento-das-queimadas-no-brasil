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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0a2eda5-f83b-3fcc-9fac-a2e4125db9bf | -12.57256 | -42.93041 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 954b6c59-165c-31a5-b7ad-e47914a9ff6e | -12.56463 | -43.10832 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 09aa907c-20ad-3d61-aded-9dd1407863e5 | -12.44288 | -42.43417 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5a83fde2-ff49-36f5-87d0-83dee564b0e4 | -12.41991 | -42.40902 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| dec22e7b-0a87-37b4-a6fa-bf29ced90b62 | -12.41712 | -42.51436 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aa8f457f-a002-3c6a-aed0-50b476a84080 | -12.37135 | -42.51386 | 2024-10-25 16:50:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fc33cd2e-0152-332e-a33c-349b3d774830 | -13.06027 | -43.34855 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b0a825f-c59a-3114-9147-b559a8539f3e | -13.05681 | -43.35314 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ce71a102-d98c-395f-8b7a-d404a643a303 | -12.96224 | -43.36192 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c5258c95-0ce8-3056-aa1a-cdbfb46cebd6 | -12.79465 | -43.32096 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 177a85d1-abb7-32e4-966d-46e72f6977ac | -12.79327 | -43.32111 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c01e24dd-0d2e-37a8-b831-5a2d03e0134d | -12.75174 | -43.28038 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06e8e6b0-4061-3409-9f71-a28f97c99b80 | -12.72736 | -43.28895 | 2024-10-25 16:50:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 52dc2a0e-f96b-3450-ad9a-e190dacb30b2 | -12.59656 | -43.18944 | 2024-10-25 16:50:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5754df9-11b5-3bff-925f-88c6ae262fbc | -12.57354 | -43.23094 | 2024-10-25 16:50:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c51e3ed6-730a-37da-a5e4-6adcd6a132d3 | -14.70426 | -42.29559 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c1e5f8e9-7ce7-37e7-8b09-734c30f9bd2d | -14.67528 | -42.33148 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7f462f75-8eaf-3b7c-a3d0-78d62751c817 | -14.67388 | -42.33506 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 623614e1-a5b6-3315-9fb7-4ca07c9fbc01 | -14.67314 | -42.33092 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 13a347e8-f2c5-3a22-a04a-8ee297c9af28 | -14.66299 | -42.32391 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0b8a3201-8256-3fa5-9ee6-80f599a5e2e8 | -14.6552 | -42.33012 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 90c2a040-c368-367f-8bda-9a86b5bb6baa | -14.65093 | -42.33109 | 2024-10-25 16:50:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 39f23e43-ca88-3a18-bfd6-b19b576d7b70 | -14.5884 | -42.33012 | 2024-10-25 16:50:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 72cf1324-2062-334a-b6ba-390176ec1d0a | -14.45356 | -42.34518 | 2024-10-25 16:50:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a670c93-6008-329b-bb15-c2e886ed796a | -14.37248 | -42.36542 | 2024-10-25 16:50:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6eb4fb19-90ca-3966-b737-edaddc12dd7b | -14.3542 | -42.39837 | 2024-10-25 16:50:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| eb22b18b-9422-36ab-80de-3893be7470c4 | -14.04446 | -42.16358 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 51621271-3f43-34d7-87d0-f06aa0e3986f | -14.02986 | -42.2077 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 325135b9-b1c4-3198-8f68-2df1cff05155 | -14.00964 | -42.14758 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f2e5f994-f469-307e-bc22-6bcbc7b9c795 | -13.90711 | -42.35749 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4a3feb5e-a9fe-312f-8441-5c721bf3b906 | -13.85733 | -42.38059 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 58.0 |
| b9e8c94e-c6e7-3f4e-ab8f-2bd58fff66b2 | -14.73973 | -42.89785 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 85ab8a20-ad6a-3c75-9f04-66f8596857de | -14.71924 | -43.04438 | 2024-10-25 16:50:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5168de8d-e67e-3d93-8397-e10ba3182c43 | -14.6288 | -42.52525 | 2024-10-25 16:50:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5233225e-5327-3739-b3a7-e7dd24cd98fb | -14.47922 | -42.44939 | 2024-10-25 16:50:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 9da467e9-ea16-3ebd-8702-c692e136e556 | -14.47737 | -42.45353 | 2024-10-25 16:50:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7af63ec5-c7e0-38d3-b4a0-6c8a2986f150 | -14.47663 | -42.44938 | 2024-10-25 16:50:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7e3c0bdd-62aa-3d44-8a33-3ed62d26ca81 | -14.34645 | -42.4789 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5a31165e-b27a-3320-a131-e64308923288 | -14.33539 | -42.90454 | 2024-10-25 16:50:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e9182860-15aa-3732-8e1f-5118c70cc08c | -14.2859 | -42.62535 | 2024-10-25 16:50:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 3fdf730b-055e-358f-99b0-091a5a820cf1 | -14.28241 | -42.63043 | 2024-10-25 16:50:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6f56cc15-df7c-386e-97b7-def1a2ef671c | -14.23802 | -42.55473 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| af213a8b-8dcb-3493-971d-75be0f4d3175 | -14.15871 | -43.03042 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a65cbf72-8e75-30d5-a275-449d896d1d26 | -14.1428 | -42.89581 | 2024-10-25 16:50:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7732e082-727a-35a7-a2af-a5c52ccd0053 | -14.0058 | -43.08217 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| cb3112da-478f-34c9-a844-a31b30aa8985 | -13.99197 | -43.21925 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 525c1720-490a-3f5d-902c-dea4c492469f | -13.97861 | -42.92968 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 34df3530-f889-3c04-a6b8-2942ee7b82b6 | -13.9779 | -42.92572 | 2024-10-25 16:50:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 1aa8d5b8-17c3-30ff-a510-49734f21754c | -13.96587 | -43.25568 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 39.4 |
| cc8a886b-34d4-38b1-af78-751997a7cd1a | -13.95535 | -42.49142 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| dddd7fe8-7952-38d4-a512-aca2e6a63855 | -13.85305 | -42.43077 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fb90487d-923a-3a2f-b443-779a493a6903 | -13.84942 | -42.69342 | 2024-10-25 16:50:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a1d89eb3-42f3-35cf-b0e6-f1f1e16cb532 | -13.8292 | -42.50533 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d21b16f0-38a8-3feb-add3-0e0a95c7deef | -13.81959 | -42.96386 | 2024-10-25 16:50:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18abfc6b-d22d-3289-96ea-036653c220e7 | -13.81886 | -42.96376 | 2024-10-25 16:50:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 665eb89f-bd90-3549-bf23-b9be7340a453 | -13.81541 | -42.96466 | 2024-10-25 16:50:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 32ca94cf-ddb9-3a45-a83c-d9e1bf8ef9d9 | -13.79495 | -43.21725 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 96d8c114-bfea-3630-97e1-eddf7f010995 | -13.78736 | -42.44637 | 2024-10-25 16:50:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 33.4 |
| 7140c8ce-03b4-3dca-b133-c1b54b11d809 | -13.75514 | -43.25615 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cca2c0f0-f578-3674-9788-3deec7f73cac | -13.75266 | -43.25663 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 9004dcfe-e9ee-3223-831e-6973347c28bf | -13.74377 | -43.25436 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 57.5 |
| e7bc206e-9bb8-3d88-b6c6-3edc52bc6edb | -13.738 | -42.97169 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 499c85ca-bdda-389c-bf76-193403db6058 | -13.71396 | -43.133 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 08677372-c2bc-35ee-8ba4-00377c99e1a0 | -13.69324 | -43.1129 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 73594dd3-64ba-3b79-bc02-4e27d553d41b | -13.68403 | -43.30085 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fdbedff6-b88b-3e1e-b8e8-6db63c209521 | -14.77262 | -42.64457 | 2024-10-25 16:50:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 160a5bfd-e5f4-3247-b05a-a14166aa023b | -13.89225 | -43.60161 | 2024-10-25 16:50:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 01a9b646-5ef6-3226-adc3-72f81544d238 | -13.89161 | -43.598 | 2024-10-25 16:50:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6df9d720-c1c9-3719-b2d2-3cfb36c2d9ad | -13.86808 | -43.5349 | 2024-10-25 16:50:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c0acd972-a48f-31d8-a6eb-9aeed5bcf3ba | -13.86789 | -43.55748 | 2024-10-25 16:50:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 226eb190-6510-3479-adb9-8335ddf3534e | -13.8633 | -43.62565 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a284d07d-bf91-3fe0-9ed9-76eb2e235842 | -13.86266 | -43.62202 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 29a59ca3-5ceb-3c63-9e75-1eadc8044aac | -13.85865 | -43.62277 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| aece21b4-6dc4-3b5a-bf43-659f488e277e | -13.82247 | -43.61128 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ccca8b53-d530-3cdf-8e3a-599593670692 | -13.81994 | -43.61509 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 52912543-2c23-30c4-95b3-a25f5244b4f1 | -13.81929 | -43.61147 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e144bcce-7324-3485-9963-b9266c562548 | -13.81908 | -43.61566 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e1777485-24d3-3f2a-baa8-031dafa4ce6d | -13.81846 | -43.61204 | 2024-10-25 16:50:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0f68e0e2-d3c7-3c28-a847-240704d81588 | -13.79331 | -43.58673 | 2024-10-25 16:50:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e8f5788-9d97-30e4-b733-8a659e5fb4bb | -13.68504 | -43.4702 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96c43f10-b0f2-3c10-888c-9b83cf5bd2d6 | -13.68435 | -43.46701 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d877ccf1-8aac-360d-be0b-010218e736b4 | -15.81837 | -43.82175 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 7d514d73-7b8f-3127-9e9a-1c0ac8af3b09 | -15.81751 | -43.81673 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 04236bb1-4705-39bf-86bf-a0bf1f99261f | -15.81586 | -43.82031 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 5c53e76f-b54c-3ad8-80e9-1f15f8899cd6 | -15.81497 | -43.8153 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 178a479e-2b4c-3b2d-8459-5c2f84a1fe9d | -15.81453 | -43.82248 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 15abd50a-502f-3118-afd0-bb9c82f5da73 | -15.81366 | -43.81747 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 22.3 |
| e27f5c4a-cfb6-32b8-a697-42c15c37ca4b | -15.8128 | -43.81244 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 5f03ca47-e3f9-33c6-96a9-77612f19c0ac | -15.81112 | -43.81601 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 9aa2cd32-0fd0-3510-bdb3-eb9dd87ff53b | -15.80981 | -43.81816 | 2024-10-25 16:50:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 440e63a9-ddbb-31e9-903b-9bbb52d2a716 | -15.78321 | -43.80229 | 2024-10-25 16:50:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 8b3ba979-830c-3878-8bab-7fe4457a9c80 | -16.21102 | -43.77828 | 2024-10-25 16:50:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bf47ad68-427c-3cd0-9f14-54f091ced480 | -16.19353 | -43.29086 | 2024-10-25 16:50:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14f3175d-9729-3d2d-b6ba-f745c37a684f | -16.18891 | -43.78765 | 2024-10-25 16:50:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7823b994-5615-356e-8426-5dcdb2f4b771 | -16.18804 | -43.78267 | 2024-10-25 16:50:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 22b89fda-8b65-382f-8000-7e55fe06ce3d | -16.17646 | -42.68769 | 2024-10-25 16:50:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b1cd93d-b56f-3185-9302-a8ec22d9c1f0 | -15.96021 | -43.54475 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0166138c-8236-3a2f-bb15-bf4964c2fd19 | -15.95091 | -43.51471 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f858d05c-2b7d-3e3e-8235-477fe696cb59 | -15.95061 | -43.53598 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2cf1948d-79e2-3714-bc93-a302891d3019 | -15.94971 | -43.53087 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README143.md)
