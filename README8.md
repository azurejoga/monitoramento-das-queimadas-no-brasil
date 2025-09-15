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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f82db46d-65d2-3dc8-8c75-7f2aad19833d | -11.7759 | -46.663 | 2025-09-15 02:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 9687a6ee-0d8f-3351-8b56-002c79c31629 | -17.3435 | -42.6581 | 2025-09-15 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 72666995-6650-3261-bd1e-6a68f9ce3cb3 | -18.0507 | -50.9129 | 2025-09-15 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 2d2c0cc1-eda4-36fb-b776-a3b84156730c | -11.8665 | -50.5362 | 2025-09-15 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4b183371-59e9-3e5a-b2d4-8ed75584dcee | -8.9262 | -45.5004 | 2025-09-15 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 89ceed6e-4e3f-3af9-9388-be6455301437 | -18.0502 | -50.935 | 2025-09-15 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c15cec32-b95d-3976-833f-081437bb8854 | -8.9076 | -45.4797 | 2025-09-15 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 39beaff0-2606-304b-b3d5-2deb3230837d | -12.9791 | -47.9713 | 2025-09-15 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b61f0d8d-babe-3898-94c5-2a993176647a | -15.7985 | -53.4582 | 2025-09-15 02:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7642c94b-27fa-3178-8544-c9bc690376d9 | -8.9073 | -45.5024 | 2025-09-15 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| d725c7e8-90d0-3e90-9147-98d7d816c578 | -17.3442 | -42.6333 | 2025-09-15 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 83dffe17-082f-35a3-a28e-04da3c6a0878 | -18.0303 | -50.9385 | 2025-09-15 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f4716869-deb2-391f-ae1f-af90319250f7 | -18.0308 | -50.9164 | 2025-09-15 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ff75ba5b-499d-3570-a9b4-6b9b1faee208 | -8.9265 | -45.4776 | 2025-09-15 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 07d2c81d-e78b-3a5f-afe2-c328ced58468 | -8.9787 | -45.8118 | 2025-09-15 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 629af4b4-f10f-3965-9dc6-eb32935693a1 | -10.9365 | -45.5063 | 2025-09-15 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 071be9bf-8253-3bd7-b0c9-db05b29bafea | -8.9787 | -45.8118 | 2025-09-15 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| eff14277-7b9a-3259-b50b-4e9544377f89 | -12.9984 | -47.9685 | 2025-09-15 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 7aee6d3f-9860-3d74-9e94-301391f02a25 | -14.8412 | -51.6336 | 2025-09-15 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cd71e398-44eb-34a0-930e-e96310ba7bdf | -14.8416 | -51.6121 | 2025-09-15 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| ac51c588-ae68-3b02-8f90-282ac52035cb | -10.7081 | -50.6425 | 2025-09-15 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| b14b5ee0-a895-3aba-a661-e2e23bfc9b69 | -11.8297 | -50.4548 | 2025-09-15 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e3a42088-940e-3ede-9c28-ab253ab1eb85 | -12.006 | -47.7505 | 2025-09-15 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 102443cf-6ea5-3c35-bd3b-3925a1da2c52 | -10.7076 | -50.6851 | 2025-09-15 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 5b53b030-4875-3b73-a267-7d3d53b27646 | -8.9073 | -45.5024 | 2025-09-15 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8014d8b2-6944-3001-accd-eca6cc4813dc | -12.9791 | -47.9713 | 2025-09-15 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fc4a3385-90ac-3047-831f-80eda96d3898 | -23.4754 | -47.37 | 2025-09-15 02:30:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.2 |
| aaac8ff6-6b61-38d7-b720-5a02c5f9a799 | -17.3442 | -42.6333 | 2025-09-15 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9abe7ee5-28b9-3d0b-b8b3-6a83be8d74d4 | -10.7078 | -50.6638 | 2025-09-15 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 4af69829-1f6e-3688-8d08-c4069d64a527 | -10.7265 | -50.6832 | 2025-09-15 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 989571e9-abf9-3f49-b8ba-40dbf796ef3f | -10.7268 | -50.6618 | 2025-09-15 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 215.3 |
| b00f7cf8-39cf-3c1b-a475-37d1d879c976 | -10.7271 | -50.6405 | 2025-09-15 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 3b730661-e01d-3dd6-96fb-c423cf0cb7b6 | -8.9262 | -45.5004 | 2025-09-15 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ced8eaf6-c039-3f49-b28b-771575f0dca5 | -8.9784 | -45.8344 | 2025-09-15 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 669f6d71-9a6e-3965-b56b-dd01f9201af2 | -7.676 | -44.4879 | 2025-09-15 02:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 37c8c6dd-e924-39e2-aca8-ef172c8ed2a8 | -10.7076 | -50.6851 | 2025-09-15 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| f4ad396b-2ffa-36b6-8033-dd93d26729bc | -10.7457 | -50.6599 | 2025-09-15 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 68ece059-3ad0-3f78-896c-7e2d77d83f58 | -8.9595 | -45.8365 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bfb68161-0deb-3dbb-8d67-d89445768522 | -8.9073 | -45.5024 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 8fe5ae42-e59e-30f2-aaba-000082c8b2fd | -8.9976 | -45.8098 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| aa0d4b95-36ee-3bae-b97b-a4f497bc05d0 | -8.9787 | -45.8118 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 57a552ee-f17b-3f02-8641-96e77c2f10d8 | -11.8475 | -50.5384 | 2025-09-15 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1325786d-94bb-3e3e-8f20-a38a4fdf6fba | -12.006 | -47.7505 | 2025-09-15 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 1599ce4e-0d62-34e2-af4a-cd4e7a4be543 | -11.7916 | -50.4592 | 2025-09-15 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e386b8bf-9b38-3576-acf0-73077ddf4e3f | -8.9784 | -45.8344 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 3bdde3a8-7374-3c23-a4ba-c2dcff9d8362 | -10.7265 | -50.6832 | 2025-09-15 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 073feed1-de8c-3e46-bc50-8d2b479a583e | -8.9598 | -45.8139 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 2131ee0f-e410-3027-954a-db303476c2f1 | -8.9076 | -45.4797 | 2025-09-15 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d1fbb57a-87a8-3cde-ae54-f164d624c5c2 | -10.7454 | -50.6812 | 2025-09-15 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 85439ee7-a107-326d-a231-f57c959da8c0 | -23.9672 | -51.9355 | 2025-09-15 02:40:00 | GOES-19 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 199.6 |
| 43aff621-26ec-3d9f-be81-aad25176a7e7 | -9.9199 | -50.2963 | 2025-09-15 02:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4bbb15f5-85d0-359f-bdb3-11fbd1334584 | -15.7985 | -53.4582 | 2025-09-15 02:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 445cfebc-d432-340d-84b2-fc56cf38ab11 | -11.7919 | -50.4378 | 2025-09-15 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e55309fe-7e32-3b9c-aa20-345406e4ca66 | -10.7268 | -50.6618 | 2025-09-15 02:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8873ce2d-7ce8-3313-b3b6-3fb560421ef6 | -14.8412 | -51.6336 | 2025-09-15 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4c3d08dc-f3c5-33e3-8ebe-9b4f665f82a4 | -23.9678 | -51.9126 | 2025-09-15 02:40:00 | GOES-19 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.4 |
| 08e6e7a4-d811-377d-a159-fd18826f6826 | -17.3442 | -42.6333 | 2025-09-15 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d7f9bc95-b1b8-30fa-84da-42df80c637e1 | -8.9784 | -45.8344 | 2025-09-15 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| dfbc5512-e277-30a2-863b-8705fc0be3e9 | -23.4754 | -47.37 | 2025-09-15 02:50:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.7 |
| bb0dae22-bef6-3636-84f9-b73514c5ca79 | -8.9787 | -45.8118 | 2025-09-15 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 98d89df3-e1c7-3008-9d3c-4fee60c977c4 | -15.7985 | -53.4582 | 2025-09-15 02:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4b2dbe40-7685-3c92-8970-419d5c9f122d | -17.3442 | -42.6333 | 2025-09-15 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 665be097-a54b-3dc6-86df-e52b697b4d2e | -23.946 | -51.9403 | 2025-09-15 02:50:00 | GOES-19 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.4 |
| 879eaf6d-1fb2-31df-8ced-1eb5bc352be7 | -8.9262 | -45.5004 | 2025-09-15 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 05cba99f-3422-339f-930d-22dc0b2aa6f2 | -23.9672 | -51.9355 | 2025-09-15 02:50:00 | GOES-19 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 156.3 |
| 0d4c97dd-ad80-38e4-a578-1e125dd73a6f | -23.9678 | -51.9126 | 2025-09-15 02:50:00 | GOES-19 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.3 |
| d8980739-103d-3ebf-addb-21e554cafe40 | -23.9466 | -51.9174 | 2025-09-15 02:50:00 | GOES-19 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| cdb29483-2e5b-3c45-afa9-67abe3bfc5df | -23.4966 | -47.3642 | 2025-09-15 02:50:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 2d1342dc-5411-3ac2-b84a-50a93e678fc4 | -11.7919 | -50.4378 | 2025-09-15 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7b6056a2-3bc5-3ba8-bd03-20d8fbeba22b | -15.7981 | -53.4793 | 2025-09-15 02:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2f54cfff-2b17-3dc2-896b-dcde166ebe88 | -15.7985 | -53.4582 | 2025-09-15 03:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9718623f-4f81-3b56-a333-65819f130df3 | -8.9073 | -45.5024 | 2025-09-15 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7cdbbd9c-148d-32be-949f-dfe580355119 | -8.9784 | -45.8344 | 2025-09-15 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7a7b80d8-fc28-3d1c-9ded-5b74031db174 | -12.006 | -47.7505 | 2025-09-15 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| c1d6428e-efbd-3d7c-a453-0e2bd089211a | -11.7919 | -50.4378 | 2025-09-15 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 093e49e7-20af-39d5-a7c3-9fa859a9187c | -8.9787 | -45.8118 | 2025-09-15 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| db379f8c-95ea-3372-a40f-1cf3da24387c | -8.9262 | -45.5004 | 2025-09-15 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 26df5500-73b9-3bc7-ad63-ba17f130fe9e | -17.3442 | -42.6333 | 2025-09-15 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d0fe11b8-20a9-3974-ac98-5eb1510bd7ec | -23.4754 | -47.37 | 2025-09-15 03:00:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.5 |
| 1b13e569-42d6-3efb-be90-11c4d1615aab | -9.42745 | -40.3143 | 2025-09-15 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3fa15bfa-c86d-337b-8532-0a6428970d4c | -9.42885 | -40.30743 | 2025-09-15 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4f61e1af-cba8-3780-9ce5-407adccfd1b1 | -9.43372 | -40.3075 | 2025-09-15 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c6459579-03d5-3b6e-b1b6-c27a4c14d7e0 | -9.42663 | -40.30597 | 2025-09-15 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dd0e7718-b9de-3323-8fb1-3dfc498aefa8 | -9.42527 | -40.31285 | 2025-09-15 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 85266ad7-f3e1-39c4-8277-82d32d16e301 | -9.43235 | -40.3144 | 2025-09-15 03:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f3dd84be-92bd-3eab-aee6-770fb2231809 | -8.9262 | -45.5004 | 2025-09-15 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e4cd0e4d-73f5-355d-9e75-ab572e9827e0 | -14.9411 | -46.5755 | 2025-09-15 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 7af18ee0-8ff1-3888-ac11-209845749bfd | -23.4754 | -47.37 | 2025-09-15 03:10:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 1300d5d3-1834-3dd9-95c6-653569d0b2cd | -10.9369 | -45.4833 | 2025-09-15 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| dc2f7a73-a58c-3ee5-9aa7-a85209878d55 | -17.3442 | -42.6333 | 2025-09-15 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e2893de4-37ab-35a8-953f-ce5cdcb5ab19 | -12.006 | -47.7505 | 2025-09-15 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1f1e61dd-f3e7-3264-a91a-424c565f9613 | -10.9365 | -45.5063 | 2025-09-15 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 18eab70f-0afc-3211-8ec5-62b133474c61 | -14.9406 | -46.5984 | 2025-09-15 03:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 55d7e758-c97a-333f-8c9a-8008ea338f9b | -14.9416 | -46.5525 | 2025-09-15 03:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 58dc1c0c-8d0a-3bf8-bd1f-3aea4720ca59 | -11.7919 | -50.4378 | 2025-09-15 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b9e504a7-8ada-3438-a1c9-056d85c3f65e | -10.9556 | -45.5037 | 2025-09-15 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 9fdfa4fe-3713-3142-90dd-bbbdf533c1bf | -8.9787 | -45.8118 | 2025-09-15 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f58dfc48-aa62-36b3-ba55-317473658260 | -8.9076 | -45.4797 | 2025-09-15 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 07b5878c-b4b7-308a-a8ec-b1228c9605a0 | -8.9073 | -45.5024 | 2025-09-15 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e1dfeea0-5245-343e-847e-b75edb2951a5 | -17.34313 | -42.64335 | 2025-09-15 03:10:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README9.md)
