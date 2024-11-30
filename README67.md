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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3ab682b-b135-3a1c-a7d3-f90e5a41b63a | -5.65412 | -45.20291 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8864764e-aebf-3d8d-b9ad-631738373f56 | -3.02288 | -54.02766 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f22f2674-8baa-3976-9718-afd7feafdfc0 | -3.40342 | -50.66103 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0137290b-224b-34a9-8d1a-eb769e1f06dd | -1.1267 | -53.18994 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a83a4505-13bc-38e6-83ae-f8cbcf873097 | -3.14034 | -53.72234 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f4416e1-e537-35eb-9525-50dd4329400d | -3.74529 | -54.68004 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 694b401e-b98f-3d85-ad08-fdf0730d8608 | -3.9387 | -49.91271 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bcf4b73-5007-39fc-b5c4-a714d40cf0b8 | -2.95821 | -53.88395 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fd70c49-d90b-3ccb-bca4-87ebe73d5e8a | -3.5124 | -53.7881 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36e086f0-5cf5-3302-951a-a0e9a75db32d | -3.42792 | -53.89251 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2141a331-462b-38c8-bb65-0f6f4d7b1be9 | -2.84338 | -52.53678 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f84bf1-084b-38a3-acfd-b71bd42329e7 | -6.9478 | -42.78067 | 2024-11-30 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d0dd6d11-1b9f-3460-b993-186d477cea63 | -3.41198 | -50.16781 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a87641-a3c4-3520-8c95-d486a63275c4 | -3.59319 | -50.37724 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbe9c06f-5e78-3bd9-8a13-01e9b05da001 | -1.68784 | -46.78823 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b7e04940-ad49-39d1-920a-2dfc25c8fdc4 | -2.4477 | -53.97022 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66f5ae5e-a2c9-3202-97e1-e6f4683b84b4 | -1.19945 | -51.74556 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9aeebaa6-0666-3453-ac48-a4b6d9d6db90 | -3.09886 | -49.4546 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc215358-9af4-3a40-b0eb-586f6bb7ea76 | -3.23424 | -50.30681 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa588cf8-9101-38c5-972e-e51c91ad6d6c | -2.51848 | -48.18266 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee086585-61a4-342b-a5bb-60ea1def895a | -2.11278 | -50.34248 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a96ef0ce-3997-3d0b-9a8c-7ee1ce308ea1 | -2.95653 | -48.3397 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6453e74-efdf-352f-964e-39ff8184f14c | -6.90695 | -43.54271 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 41505177-952c-338d-b8d9-dbff38f80717 | -1.07857 | -53.63034 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b5c7be9c-fe89-33ce-81e9-f792425d4085 | -2.86735 | -46.82893 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f972ee8-82bf-36b3-b1de-c9d2e0cae169 | -2.62685 | -46.20282 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3faafa0-929d-3a37-a18d-7b88e32ec87e | -1.75457 | -50.54544 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccc87608-6a6c-37ba-9fc5-efe4ab3c4435 | -3.53951 | -50.1802 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7310a5b4-9eb4-3dd5-85ac-a8f4af9d5ef4 | -8.84759 | -44.75216 | 2024-11-30 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19e72c5b-bd22-3349-8721-a24d9b46512f | -1.64658 | -52.40023 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3a18fc7a-adef-3721-b583-b3e955e84f3a | -3.35015 | -46.60981 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc0e8a3d-c8fa-3717-8c24-bd77408c63da | -2.86898 | -53.99617 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56384102-be32-3626-98c8-3cb5edb87713 | -2.58543 | -54.09945 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c9787c6-8857-3e94-96a4-092aafb2147f | -2.46088 | -46.52936 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efff1ade-bf02-36c3-a581-999696ba4bd6 | -4.0792 | -47.02416 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a589aec9-1e93-3cd6-9768-ab6fe4ac07f7 | -3.51829 | -50.51225 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e9d5e02-2ad0-3589-99ac-167f0056e40c | -3.25694 | -48.76772 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e550801-db0b-3875-b5bd-22f5d5b8c3dd | -2.4603 | -46.53316 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6fc7e55-b954-3088-96d8-f5ef20275f71 | -2.89205 | -54.1658 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 417f838a-f588-307b-8071-a82eb315de6b | -1.20477 | -53.88754 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7978d294-91ae-3067-a8ef-b6120d563436 | -2.69464 | -48.60207 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97053b7c-0ba0-3951-8a60-2e12882f12cf | -4.0059 | -50.3478 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68dd15b5-d5cd-390d-8b6a-8e1605ded26a | -2.42191 | -50.47561 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b359f2-f03a-396b-b36b-4e3e34817637 | -1.25224 | -54.5478 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9bed6dd4-0a00-315e-919b-b69227bc0f93 | -2.83932 | -46.8742 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e202b28-ea12-3207-bacd-49b723665771 | -1.25338 | -52.18638 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1345321-2c65-3b1c-974d-754f06eae173 | -3.10556 | -54.03439 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed47626-387f-3049-8dfb-2092f3bebfec | -1.09131 | -53.13308 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b20e4fc-64c4-389f-ba84-95c645d7871b | -3.38077 | -50.69477 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23d3fdfd-b3ab-312e-9890-c1cd84fcbf51 | -3.70822 | -45.69219 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03fb03a0-7677-38f4-915d-55f4d334ef23 | -2.46595 | -50.21666 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49892fff-716e-3078-8ef5-d3403a2ed9f5 | -3.51331 | -50.30298 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5678284c-0647-37e4-98d3-2df192a0b2b9 | -3.55178 | -50.18936 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97f1e828-ccc4-365b-ba62-d4b582b0379f | -2.8052 | -53.04654 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4c8ba0a-50bc-38f1-96dd-99c7fa531d78 | -3.85837 | -54.08078 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ecc173d-36ee-3a5d-9ffc-b4a54ebe955d | -3.25068 | -51.14085 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f5c462-baf3-3d88-9e18-19a7eac3bbdd | -2.69134 | -48.60156 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bd7744b-d238-3c49-a0f6-0975c55fd5ea | -2.20216 | -48.33479 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 434835bb-b1dc-3b5d-a726-8d0c2e967044 | -3.24995 | -50.5922 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e361895-8a2a-353b-a074-0c6127a9caa6 | -3.49078 | -53.82135 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d95a00a-ee04-35ca-8798-9fe820ab9a33 | -0.82343 | -51.60666 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ba8f905-bad6-37cd-b430-94c0b75fe507 | -4.59277 | -44.70865 | 2024-11-30 04:40:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab57ef12-30ac-32e2-b87c-aa31d45722a7 | -3.48934 | -53.80521 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| bbd868e9-ddac-3aa5-8d35-14ef8fdb5338 | -3.64895 | -51.39566 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b0cfeef-ab3b-3b58-8fe9-cc5841bafc56 | -1.21228 | -53.55424 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0041b3b-e464-31c3-8f32-478dbf5ba4ae | -3.78299 | -47.72077 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fef31f32-740d-3eb8-a120-92d2c362f78f | -1.65611 | -53.75223 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5423d08f-5059-308f-a6b2-cb1c772238e3 | -3.23431 | -54.73093 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1942d242-f084-36ce-9993-1711dddc04f3 | -1.30981 | -52.86456 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ce0df8e-01cd-3d4b-b095-c00278ec6d69 | -1.8807 | -52.65943 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd7bee7b-d218-394d-b5c5-f259bb213707 | -1.67003 | -52.51889 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9cc1137-24f0-3bec-8b9f-7471cdb164c1 | -3.34163 | -51.97813 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3d7adac-b8ee-3522-a1d5-695797ab1563 | -4.20618 | -50.69664 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90d6ecff-35b7-3ead-91b6-36bf2965652e | -2.4124 | -46.50704 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cae7a189-48c3-3164-8cae-2264a49b1741 | -2.87197 | -48.09546 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be2e31ad-f2a3-390d-a501-b58bdc30f4ea | -2.76911 | -55.33714 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3963601f-e8b5-3e66-b177-05fe7798f7dd | -1.15951 | -52.23674 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77daf226-5042-3225-8f59-53adc8f97b3b | -2.74987 | -51.66426 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36db9b60-dffc-3a97-9c19-1571c93151dc | -3.33491 | -50.50237 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9f72d9f-b169-339b-a7e0-4545c73446f5 | -1.06989 | -53.63269 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce08313e-f2d5-3962-9005-4cea24b706de | -1.28305 | -51.66058 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06cc3577-7863-3b23-95f2-6d75de16afb7 | -2.71733 | -48.63019 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f442ba9-0004-39f1-aead-c353c677c8cf | -1.17531 | -53.88691 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 867de3da-6695-39d5-bdf6-7b056ec4e408 | -1.36092 | -54.65918 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f9787c8-d473-3a4b-97f1-6cc0fdb88e0e | -1.11333 | -53.22361 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63fef235-afd5-3dcb-8534-198cddd4510d | -1.0493 | -51.81475 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6f0b23a-3e4c-3aaf-ba66-d87e854c92c8 | -7.21612 | -39.77283 | 2024-11-30 04:40:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 87439894-a4b0-3371-b87b-dad73514d5df | -4.38877 | -48.13676 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9f6ac1d-2d0e-321f-85d2-45d0e4521123 | -3.25142 | -53.85673 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e67b1940-48d3-3861-89ad-b252494cc0dd | -3.42655 | -50.42478 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d1213c3-74d0-3cb6-9ea7-9249cb243702 | -1.86077 | -50.80945 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f2bbc04f-8709-383e-a148-50c80f790f54 | -3.03387 | -54.0367 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcb92797-3c4e-356b-8528-df254073fdc9 | -3.78576 | -46.69742 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d45a6853-116b-34b1-9b85-17c62680dc16 | -8.31978 | -44.95383 | 2024-11-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fde41783-0a4b-3860-8680-73d0b9407f34 | -3.34555 | -50.52243 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2c8f841-e153-30a8-9222-1b33f199f234 | -1.11358 | -51.7421 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8667723-599a-304a-91e2-3afea1e24d0a | -2.19778 | -48.34116 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df6644b9-c51d-345d-b5c5-3075753096a3 | -1.26629 | -54.55832 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 26a4fb0a-407f-3132-b7fb-42f4eedbcee1 | -5.65028 | -45.20229 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 149d2223-98fe-3f3b-a0a1-399e6aec0243 | -3.81499 | -52.24696 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README68.md)
