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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9a238f7-e405-3c08-a2ff-3741d45001fc | -9.006 | -65.4 | 2026-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 8a1f4c61-d204-327d-9e3c-e2677cd3af22 | -17.4435 | -48.8425 | 2026-08-24 01:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| d5b673e1-fe7f-3c60-88e6-0ed70b0cabb0 | -8.9876 | -65.3819 | 2026-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7ee25dfb-391d-3653-a0df-bdac37433f97 | -17.444 | -48.8199 | 2026-08-24 01:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 213.0 |
| f40067e1-2f0e-31f7-866b-f582d372b601 | -9.4578 | -40.3392 | 2026-08-24 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 149.8 |
| 1ddb56c2-6c83-35db-a11c-1634db844b97 | -22.9932 | -49.3831 | 2026-08-24 01:10:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.8 |
| cb7b6662-513a-39ad-8042-24b8bdc63c7b | -6.6048 | -58.3838 | 2026-08-24 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 483ebfbd-e752-3119-8bd1-b1fe057813bc | -9.4582 | -40.3143 | 2026-08-24 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.1 |
| 739f82dd-411d-3389-a878-281fd741ed31 | -6.8491 | -52.505 | 2026-08-24 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 65ac3fe6-d1e9-332e-bbc1-5f1d5698aa3d | -6.6233 | -58.383 | 2026-08-24 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1b96deba-0161-379a-9b2f-c1c7aa344460 | -23.0142 | -49.3779 | 2026-08-24 01:10:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| ade2dcd7-71ac-3e1e-87ae-a1e1191226cd | -9.0061 | -65.3813 | 2026-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 9e9c5b25-bb5a-304a-8fc0-f168966e85ea | -7.3791 | -45.8119 | 2026-08-24 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 8cde0102-9d94-3873-87c7-a728cc4aa12e | -3.5406 | -48.1889 | 2026-08-24 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 91d33cd7-d7b9-3e64-a0f8-46d2a0d46e67 | -17.4241 | -48.8236 | 2026-08-24 01:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 316.0 |
| 19c6a083-25c5-323b-9b75-d040ab234248 | -8.9875 | -65.4006 | 2026-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e4097406-1342-3f83-a334-ad951dbcc2e3 | -8.9876 | -65.3819 | 2026-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 48adf21b-46e5-3341-8070-0d6ac1e4a62a | -17.4435 | -48.8425 | 2026-08-24 01:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 7c57e79a-0659-36c7-b59e-b26ce88b8578 | -7.7706 | -61.1061 | 2026-08-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 6cae6c68-0bf4-37e0-9ba3-ccda200f8991 | -22.9939 | -49.3597 | 2026-08-24 01:10:00 | GOES-19 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.3 |
| d7a6eed6-11fa-317b-aca3-8e6ab72712e5 | -9.006 | -65.4 | 2026-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 487a6540-b8db-3121-83c9-baf63f751dc9 | -17.4236 | -48.8462 | 2026-08-24 01:10:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 240.4 |
| c6df9529-bf42-358c-a4ad-e688b9eef379 | -7.3605 | -45.791 | 2026-08-24 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 7f529575-b86f-3962-9fdd-68dbdd06b9b0 | -7.3603 | -45.8136 | 2026-08-24 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 28ab21cd-6f79-3a29-9b70-480463b78c1b | -7.3788 | -45.8344 | 2026-08-24 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f421b7a8-a331-3580-8a9a-2da098426d9e | -7.7707 | -61.087 | 2026-08-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 027f26e9-9531-3507-941a-06c361184e5c | -7.36 | -45.8361 | 2026-08-24 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 199.5 |
| c152c6bc-48cc-3657-b8b4-b7f85d8eb5a8 | -7.37 | -45.8 | 2026-08-24 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84959b50-aaaf-3ea4-8d00-eb9af46e941c | -7.34 | -45.8 | 2026-08-24 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 253d9059-9623-3976-a6f3-9e71649282d0 | -7.3788 | -45.8344 | 2026-08-24 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3f9c94e3-3bb4-37a3-a714-23f6d5e0e613 | -9.006 | -65.4 | 2026-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a9c35a79-ec9d-3117-8169-732be56dbe32 | -17.4236 | -48.8462 | 2026-08-24 01:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 215.3 |
| ad040532-5bdd-3a99-b45d-b27b090c2180 | -17.4247 | -48.801 | 2026-08-24 01:20:00 | GOES-19 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| bcc04c62-0c71-3ed2-9a1e-df40f6a7bd8f | -22.9939 | -49.3597 | 2026-08-24 01:20:00 | GOES-19 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 02d1c456-5b9f-3f8c-8ab5-8b21b805fc22 | -7.3603 | -45.8136 | 2026-08-24 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 233.8 |
| c33cd5a7-75e3-34d9-9f0e-011f84d49021 | -17.4435 | -48.8425 | 2026-08-24 01:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 7d8c864c-212f-3c52-ae0a-e088a9813a1e | -8.5892 | -49.9926 | 2026-08-24 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| fe2ec6ad-4b7d-3ba2-9b19-1d40101cf14f | -3.5406 | -48.1889 | 2026-08-24 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9bfc9890-9801-384d-a6f3-fe8e1448bafa | -7.3791 | -45.8119 | 2026-08-24 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| ee651fac-9419-3475-8131-4f03044f7120 | -22.9932 | -49.3831 | 2026-08-24 01:20:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| 0e14627e-fa98-38b0-ba58-bc098f550125 | -8.9875 | -65.4006 | 2026-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 141a7157-d1fa-3199-95b3-f206e6e852f4 | -7.36 | -45.8361 | 2026-08-24 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 6e6317b6-7ee6-386c-9229-f07b4d399d99 | -17.444 | -48.8199 | 2026-08-24 01:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 92535243-d977-39f9-b2d5-f0129d04162e | -7.3605 | -45.791 | 2026-08-24 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0d0f8b66-5352-3ead-b06c-8462cd40268e | -9.4582 | -40.3143 | 2026-08-24 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 270.3 |
| 75634256-5b09-3107-a286-610f3fca42d0 | -9.0061 | -65.3813 | 2026-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 8509b2af-77da-3218-967a-7508e94f941f | -6.6233 | -58.383 | 2026-08-24 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 98c2ea6b-3def-3278-a67e-86da592da9de | -6.6048 | -58.3838 | 2026-08-24 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5567c1f8-2117-3f18-8e5a-8df0db7b44dd | -6.8491 | -52.505 | 2026-08-24 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f2e10938-738e-3f21-a46a-0a6d60c9d6b6 | -17.4241 | -48.8236 | 2026-08-24 01:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 02e374ac-81d2-3213-a26d-c57139c9f274 | -23.0142 | -49.3779 | 2026-08-24 01:20:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| fd08c463-914e-3e66-9c68-07a7906fca6e | -9.4578 | -40.3392 | 2026-08-24 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 149.8 |
| 7c496cae-422d-3971-8630-3612c3f15031 | -9.4773 | -40.3116 | 2026-08-24 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 3ea53b4d-026c-3c70-af3c-c150125ed486 | -8.9876 | -65.3819 | 2026-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d734e0e7-bc4c-3f39-a8bb-c152b6a0751e | -7.3605 | -45.791 | 2026-08-24 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 83ded211-7a73-339b-8b07-9d1bfd989491 | -6.6233 | -58.383 | 2026-08-24 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0e7e451f-10dc-3ea2-a3d8-c09788a4534b | -17.4042 | -48.8274 | 2026-08-24 01:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1ba25e1e-6ca9-3a4d-b939-65cedd5fd2d9 | -9.6774 | -55.1022 | 2026-08-24 01:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| d45ad4b3-f32b-36d7-851e-b93ecdf497f1 | -7.3603 | -45.8136 | 2026-08-24 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 06892aa1-cf51-3cdc-aeb2-d89f4e6ec26d | -6.3505 | -54.7665 | 2026-08-24 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 1b419588-a8b5-3e38-b5ae-409f7ffb5bf5 | -17.4435 | -48.8425 | 2026-08-24 01:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 8f7130ea-1ea6-34c4-a927-4e5b3ff71931 | -7.2443 | -49.8654 | 2026-08-24 01:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 231f0bb4-6a38-36c4-8953-e1547e4b0441 | -17.4236 | -48.8462 | 2026-08-24 01:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 9d9ac981-35cf-305d-99e2-fa5079db3ff0 | -9.006 | -65.4 | 2026-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 88924458-7969-34a5-928f-f3f456ec8b73 | -17.444 | -48.8199 | 2026-08-24 01:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 237.6 |
| a1a8333b-e1ee-317c-abdf-a5f36decf812 | -7.3791 | -45.8119 | 2026-08-24 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| b9d48bd6-86ee-3b0d-b959-92acd0597322 | -8.9876 | -65.3819 | 2026-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| bb73989c-15fa-3afc-ba26-7a258ab76150 | -8.9875 | -65.4006 | 2026-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5e9c4d8d-1a8f-3a98-b39f-7ba61e294d63 | -22.9932 | -49.3831 | 2026-08-24 01:30:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 497f0c81-5b0d-3d87-b00e-20970c5715a1 | -6.6048 | -58.3838 | 2026-08-24 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 003dae99-cdc2-30a4-be22-2d45b0c16aba | -9.6776 | -55.082 | 2026-08-24 01:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 77f642c2-681b-370b-b8f5-7f14396ff8e0 | -23.0142 | -49.3779 | 2026-08-24 01:30:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 5286ce08-7ba3-39aa-b6d9-919f2a77b019 | -7.36 | -45.8361 | 2026-08-24 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b04e65da-b5ee-3575-9e75-3f46d77d3d32 | -17.4241 | -48.8236 | 2026-08-24 01:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 485.0 |
| bb052506-1464-3f38-8ab1-e70864bc9c63 | -7.3788 | -45.8344 | 2026-08-24 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 686e821c-e6c3-338b-a6bf-3070adbb37d2 | -3.5406 | -48.1889 | 2026-08-24 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c42d77af-12c2-3933-be81-893ad0152509 | -9.0061 | -65.3813 | 2026-08-24 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 121deb5a-6411-3e4a-bcab-1872f63474ab | -7.3605 | -45.791 | 2026-08-24 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 97e9d48e-9b98-32b3-abaa-7552c378a50b | -6.8008 | -59.5934 | 2026-08-24 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 6cd30c6e-5d89-34b8-9951-57bde111d87a | -7.2443 | -49.8654 | 2026-08-24 01:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e9c677ff-ef59-374c-a674-bee92bb333b9 | -17.4241 | -48.8236 | 2026-08-24 01:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 350.3 |
| f9b547c0-3e37-35fd-a90b-d4b551e89b51 | -7.7891 | -61.1054 | 2026-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| b8d4fa23-fcf2-3eff-823b-2f4772e62c94 | -14.9392 | -52.664 | 2026-08-24 01:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bdeb157c-82d5-3bdb-8f7a-2b87c70b4839 | -8.9876 | -65.3819 | 2026-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a05f5223-dd81-3f76-b94f-d7007fc3d68e | -9.0061 | -65.3813 | 2026-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f1741e23-a03e-33d4-94b7-50d2b0e39e78 | -7.7707 | -61.087 | 2026-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| dde9d72c-c1a3-3190-96f0-59de942d11a7 | -22.9932 | -49.3831 | 2026-08-24 01:40:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| ed8babe1-5435-39b2-8bd4-b48b74115e92 | -17.4435 | -48.8425 | 2026-08-24 01:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 349.2 |
| 971d16a6-934f-38ec-97e8-fa37758c9af5 | -17.4236 | -48.8462 | 2026-08-24 01:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 354.8 |
| b8a06356-5d9b-385e-9b0b-322c439052e0 | -4.1824 | -49.4053 | 2026-08-24 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b7ff4418-75ae-3712-ae6d-0d364cf4d913 | -7.7705 | -61.1252 | 2026-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 38967c11-05e5-3fa9-834e-b63b82054c24 | -9.0494 | -50.7589 | 2026-08-24 01:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 22c17c2c-eb42-3ad5-b45a-883927dcb075 | -17.4042 | -48.8274 | 2026-08-24 01:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e510a070-4ee1-3f16-b906-3096836591a4 | -9.0492 | -50.7801 | 2026-08-24 01:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 23f13b0a-dc42-39e2-847b-ef93242c1473 | -12.0941 | -50.5951 | 2026-08-24 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0082b5a8-2832-3c9d-bc93-28b82bbbe057 | -7.7706 | -61.1061 | 2026-08-24 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 8663938a-88b6-3b91-af10-3aa8c4361801 | -9.006 | -65.4 | 2026-08-24 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a4cb9f05-1c65-316a-8cef-e2169fc1844e | -9.4582 | -40.3143 | 2026-08-24 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.9 |
| e1bf6f80-babe-3494-85d8-cdffe9ea64fc | -23.0142 | -49.3779 | 2026-08-24 01:40:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| a6411de6-b8fa-3b6c-aa3a-efd5e3b901d8 | -7.3791 | -45.8119 | 2026-08-24 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |


[Clique aqui para ver as próximas entradas](README7.md)
