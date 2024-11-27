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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00ff01c2-8698-3d79-8568-894d514cb23b | -4.27258 | -48.60978 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 173acb9a-46c2-31fc-90f9-f660713d3313 | -3.26796 | -50.55906 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8df5d5d-7d51-3f1e-8f0a-faa5cf748fad | -1.34632 | -51.43784 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc24c055-a353-3bf6-a618-f8a92f334006 | -2.63382 | -51.7702 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97d1aa03-5b17-31bf-b547-c39e5db61e67 | -3.03769 | -48.50994 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1730e2dc-aa25-3a70-b14c-fdc70db94df1 | -1.72817 | -52.03894 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7621789c-ca16-3e8f-b09c-d55cd418b163 | -2.84443 | -42.52658 | 2024-11-27 04:42:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83a1264c-8161-3d13-8472-6f09b0f46587 | 0.99606 | -50.25743 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8973e094-c25a-3319-bed4-818862bbcd4f | -1.30901 | -51.74291 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca9c350e-bca0-32cc-97ed-bba7f91e56c9 | -3.55063 | -50.20916 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a00e15c-37bc-3356-ac7e-221c6bfef2f2 | -3.50155 | -53.82542 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d39b44bc-97f8-3a77-80dc-1dbd9fe861e4 | -3.68383 | -50.22619 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e72090e-a1c6-37fd-be62-c581e126b226 | -2.79238 | -48.60214 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a404353-e85d-3f7c-8ca0-6654928442f5 | -4.29424 | -48.21861 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 371436b6-0a9b-3ebc-9ab9-98dd93fc83d5 | -3.34276 | -50.51432 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c72f59e-4258-3522-a09a-e7ba7c83854f | -2.6628 | -51.71908 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c633411e-283d-3d42-af4d-c239328dcadd | -3.18164 | -48.43826 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 986591f1-1a3a-3b24-b6de-d44e832fcffd | -2.59568 | -54.00402 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d63ea89a-9241-38fe-b2e0-3a21fa5c45a6 | -4.21575 | -48.66125 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a366f077-07e5-3e0c-865a-73ebecd638cd | -2.69917 | -48.6583 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24ce8fae-af6c-39c0-aec0-a4c1766e8ee9 | -4.17842 | -48.62964 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b950d29-b1c0-3c0a-b6b1-86ad25199a81 | -2.94164 | -54.78972 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a775fd3a-c3bb-3a19-99f5-0a3d92b1d313 | -2.96804 | -48.0109 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9010d37-b6e2-3362-9a08-e74355cc4e91 | -2.29959 | -48.76463 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 054c109c-3349-3db0-9c37-738a430607a1 | -2.80886 | -53.02876 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb7439c7-7f13-3816-96fb-89b746500d4f | -3.09637 | -53.24611 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c43736b2-b709-32c1-bc9e-85f90c3f61ca | -3.68714 | -50.2267 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 923427e4-b681-35f3-b423-db75724e543b | -2.46184 | -48.57787 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d765370-04f2-3297-97d3-01e390db0a43 | -1.31812 | -51.75191 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439cce91-3136-3bb9-994e-e7d55a696f7a | -4.38727 | -48.13434 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a65d2a3-c0ec-3ace-8d88-f7ad35e48f78 | -1.24335 | -51.62697 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5eb5aae4-0851-31a9-94e9-48ca3988a23d | -3.09113 | -53.27889 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb0104f1-2778-3177-a4c2-aa12048304cb | -3.59684 | -47.3422 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d4ab39b-0e0d-3f9e-9551-6f95fbb7e3b3 | -3.71708 | -47.12263 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a7f782-eefb-364f-ac3a-a8e9bd076e1d | -1.5839 | -51.26498 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7ff01f9-cdda-302c-8536-9221d7d1616d | -3.45879 | -49.97281 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8731717-d8f4-3c32-ae92-2156e4651680 | -4.14519 | -43.80261 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 46df9b31-34e5-34c7-879b-7c9babbeb8f4 | -1.31872 | -51.74771 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c068599-ca20-37a4-ab45-0dba739f6a47 | -2.16996 | -48.38226 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92903977-712d-3a03-8d04-dff2e9c2f9f6 | -2.58856 | -47.47558 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9704ec41-9d14-30aa-87a6-1910be02fb14 | -2.18043 | -53.78263 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c7e32a1-45ab-3e9f-a381-2e43457fab9e | -3.55225 | -51.50934 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10f01c35-e45c-3067-9b3e-80313187b6db | -5.19971 | -48.18485 | 2024-11-27 04:42:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35f0b5de-25ad-3e2e-b304-8519ed0bf1b4 | -2.5845 | -51.9237 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62ed4a79-61e0-3fc8-b9b8-6085148f42f1 | -1.63453 | -53.30236 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6aeb4d3-7ba9-34c9-ab1a-cb3406d86753 | -3.11365 | -53.25297 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27930879-fd11-3da2-9093-b69350b863d0 | -2.57478 | -54.05894 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d792a807-0598-392a-b3df-264c20fa1740 | -2.92998 | -48.63781 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa28159d-c1b3-3ef5-8639-1cfebd7c0255 | -3.49491 | -53.8199 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7193bbf2-ed91-3016-a418-fd2d348439a4 | -3.01692 | -48.59957 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24fb7010-b16d-3047-aa87-0277f2c6bbcf | -2.44556 | -50.40891 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4e2f922-cbc6-318c-b34c-dc6acd7fbe7d | -2.02733 | -51.18817 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc9c0425-412e-3a76-8c90-d598b08a1e02 | -3.93897 | -48.14328 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff0804ee-98e7-3130-8376-7c96e73347b1 | -2.84823 | -46.83546 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17cb2948-0a97-30e7-b475-b923d4ae2610 | -1.24958 | -51.6317 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2fbbf94-ea66-3959-a04f-2609e9a44e3d | -2.10149 | -46.56256 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab5a67a2-8ce2-365b-a8e5-8e1814c1cbac | -3.08542 | -49.21093 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fc842d3-a37a-3638-9703-aac9dad7ee23 | -4.01544 | -47.65353 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 700875ce-f706-30f8-ad0a-1aa3199c880a | -3.08305 | -54.12923 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91f8dbd8-69cd-32d6-aaa6-cf02c7bfc479 | -3.5804 | -41.96122 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c9fb43c4-6e30-3f88-94e5-719d86821f40 | -1.19355 | -51.76355 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 489093c3-e1fe-38fe-81e4-bae977b728bb | -2.17211 | -54.63005 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56c61f98-c30e-34ea-8e3b-07e9950d0f24 | -2.74601 | -51.96762 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 759eba8e-a59b-3818-bd88-836c97ea601d | -2.83238 | -54.12193 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b0903ab3-05d2-34ec-870a-20fea0e14a9c | -3.32815 | -50.21982 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f926fb-1324-369b-9231-c72e6b3aa206 | -3.9129 | -42.4137 | 2024-11-27 04:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3f01f48e-fd04-3379-987c-2e688ef18262 | -3.46511 | -51.59025 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b92cf45b-f40b-32a1-878c-11522d2cae40 | -2.64738 | -51.77232 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 784399bc-2c1b-3b9c-bcf3-f9d0c2c6f70a | -1.92628 | -53.0919 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c72b2573-1427-3649-92d6-4f23f75735f8 | -4.2034 | -50.89695 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e671326-967c-32eb-9538-bb2f81744ea3 | -4.22717 | -50.20544 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14e174e9-740d-3ed6-93ba-3543e2b8ab14 | -3.28219 | -41.77687 | 2024-11-27 04:42:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 114b7662-c5bd-3f15-ad8e-d1d0439e15a3 | -1.82355 | -52.0345 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04ed622a-bdcf-308a-80b6-8fb031fbc5b1 | -1.17589 | -54.12812 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72eddf40-5e16-3796-b9df-52cd20b20d32 | -2.7888 | -53.01733 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ec88b50-6124-3eb5-9e30-b134e630f55a | -2.6114 | -48.36722 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24fab89d-9665-364a-957f-3dfefaff32b3 | -3.10289 | -53.2513 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4ab02b89-5125-3ef1-96de-0654bf42eaaf | -3.49411 | -50.46087 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 053c9485-da92-3051-9ca9-5b1f3429f54e | -3.86025 | -40.44585 | 2024-11-27 04:42:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| daea14db-c716-3118-9006-6ddee16eba1a | -2.63302 | -48.06857 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c17d39dd-a40b-3ed3-b834-0ba7673962f6 | -2.92696 | -54.32941 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c0171ec-08f4-3d93-9667-2430c3499f05 | -4.21442 | -50.89162 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 09aabb91-d319-3ab6-a44f-70ecead46cc5 | -4.21165 | -50.88765 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abc5e2c1-75d1-3cbc-b275-24e3d32b8459 | -2.31138 | -47.3715 | 2024-11-27 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e9c2ffe-56cf-3f5f-b0a2-e4327d01e726 | -3.27961 | -50.59262 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40dddb3c-2de6-36b5-a441-5c7d3699db80 | -1.1029 | -52.11594 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6756fdff-ee66-3827-a2e7-b5ef19ff87ec | -1.89977 | -50.59557 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a146f83-584c-342c-9c5c-45888296fecc | -3.0879 | -53.25311 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e097bc4-ca47-3182-9638-4769ef003a93 | -1.72076 | -46.22222 | 2024-11-27 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fed895c-f930-3b41-b1e7-c449c420e130 | -3.04108 | -48.51046 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12df0aef-bfd5-352f-9644-45779e9cc398 | -2.64033 | -51.61234 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 069e48d7-bc68-3b2b-acc7-3f36202b4f95 | -2.97729 | -51.57632 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89fb6ae9-89c4-3021-b702-c50fcf6315aa | -1.48761 | -52.52315 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad32a5df-3a45-3a8d-99c8-b3534c535b86 | -0.97402 | -51.71078 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd708081-47fb-3a63-a270-3b526f18c302 | -2.73675 | -54.11316 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df58759-6f5b-3a30-ab5e-757350baf25e | -3.72114 | -50.18267 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2339216-b82a-3f81-910c-cd821fa5b0c6 | -5.31555 | -43.07706 | 2024-11-27 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 812439f0-9b82-330b-b368-5bc1897ed6f2 | -3.28894 | -50.27343 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e4ec006-b438-3b50-b37b-fef4aff24f25 | -3.97436 | -48.06575 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4302f19c-e28e-3121-a154-75cc3ad75fb8 | -1.95068 | -51.07106 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README66.md)
