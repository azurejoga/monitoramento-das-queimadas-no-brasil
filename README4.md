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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 954de410-15bf-3ca1-a1fd-f39488b99fcf | -12.8741 | -44.3593 | 2026-06-23 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 5b26d242-cc34-3891-b566-f1d7c6451524 | -12.8552 | -44.3389 | 2026-06-23 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 79c6ec41-dbed-3821-bdb6-d306df88a3f4 | -12.8548 | -44.3625 | 2026-06-23 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| f2a0f5d1-f8ee-34d4-9268-cce7b0af5b55 | -12.8548 | -44.3625 | 2026-06-23 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 3c085dfc-8cd9-35b0-a484-4b74c66833a0 | -12.8746 | -44.3357 | 2026-06-23 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 37959564-3e69-39c4-bb20-737cc598f54d | -12.8741 | -44.3593 | 2026-06-23 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| f30b361d-0226-386e-9146-4d67ed8e7a62 | -12.8552 | -44.3389 | 2026-06-23 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 560844e0-6f4b-31b5-8e74-f8afd9d4ecfa | -12.8746 | -44.3357 | 2026-06-23 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7947a585-bb74-3010-936e-16b2b9414715 | -12.8741 | -44.3593 | 2026-06-23 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 5d31156f-92da-3c38-9adc-3e52ca8dd1ab | -12.4283 | -58.4048 | 2026-06-23 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 4919e676-dae6-391c-9a84-8f977884c016 | -12.8548 | -44.3625 | 2026-06-23 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| e07fe1da-0acd-359a-850a-d36e4d725800 | -12.8552 | -44.3389 | 2026-06-23 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 56688379-8791-367f-bf9b-adb35e88b3f2 | -12.8548 | -44.3625 | 2026-06-23 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| bd8e51f3-5e82-35ee-bffb-d0f773d7e416 | -12.8552 | -44.3389 | 2026-06-23 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c6044295-0662-3a62-b572-dac9329b7092 | -12.8746 | -44.3357 | 2026-06-23 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 18cf30ce-61ac-3c40-b80f-0619f79bbc47 | -12.8741 | -44.3593 | 2026-06-23 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| f0fbdf3c-6409-30e7-9b9b-97c812eb3ae0 | -12.8552 | -44.3389 | 2026-06-23 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3f42f929-b1be-3b2b-af5d-2b1b7fd9590a | -12.8741 | -44.3593 | 2026-06-23 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 26550e90-f69e-3a15-a862-5f5baccc9e1f | -12.8548 | -44.3625 | 2026-06-23 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 8e0806da-ed54-30a9-b349-4da9a7c9e6fc | -12.8746 | -44.3357 | 2026-06-23 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5cd07e02-8717-341e-9631-0088c7e2e973 | -15.44316 | -41.37219 | 2026-06-23 03:15:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 182def26-2f93-3e76-8542-50f8b8b8caa4 | -16.02862 | -43.41348 | 2026-06-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9bbd184-1e70-3771-9a93-445b765f2eb6 | -16.02706 | -43.42042 | 2026-06-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83d9fc87-7b09-3a9a-b91d-8c89ac893dd9 | -14.06674 | -39.4903 | 2026-06-23 03:15:00 | NOAA-21 | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 33337933-a89c-3b15-8ca2-f9476be3739d | -16.03348 | -43.4194 | 2026-06-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c3ac2c3-f2ca-3e22-9a15-856e6bc63c48 | -14.06819 | -39.48969 | 2026-06-23 03:15:00 | NOAA-21 | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ca230d94-728b-390a-b1da-7cc4cc7349c7 | -16.02658 | -43.41778 | 2026-06-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f39b0f6-43b7-30f4-a13d-d65996b303df | -16.03395 | -43.42208 | 2026-06-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64b9b305-d156-31a6-ad9f-df64270166a0 | -15.43698 | -41.37059 | 2026-06-23 03:15:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 74bb126c-5385-37d1-815c-5dd55b14df8c | -12.8548 | -44.3625 | 2026-06-23 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 40567b34-85dc-3558-a914-4a3eae2dd539 | -12.8552 | -44.3389 | 2026-06-23 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5ed48631-8c8d-3cf5-ae01-11cd9df22cb1 | -12.8741 | -44.3593 | 2026-06-23 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 52397726-3bd6-3fd9-8a84-9f929dd2b287 | -12.8746 | -44.3357 | 2026-06-23 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e99a6352-c2d8-3100-8f48-2414223db436 | -12.8741 | -44.3593 | 2026-06-23 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 6c461831-f4e8-3f74-a8b5-821becaa84c4 | -12.8746 | -44.3357 | 2026-06-23 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 38cb4bc7-952e-3fcf-a550-d33bb8530ddf | -12.8552 | -44.3389 | 2026-06-23 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 046d0e32-93f8-3da6-ab9f-e692e2384b5a | -12.8548 | -44.3625 | 2026-06-23 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| a1ca2b07-3472-33dd-a0b7-f2c7eaf25119 | -12.8552 | -44.3389 | 2026-06-23 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1e1bf58d-bda0-3956-8b43-fba867c2007e | -12.8548 | -44.3625 | 2026-06-23 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| dce606cd-f384-3388-a91b-d69f1df456f2 | -12.8746 | -44.3357 | 2026-06-23 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2a6fb8ff-fe4d-3d52-9f66-d3a3a411685e | -12.8741 | -44.3593 | 2026-06-23 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b9f77758-8c1b-3d15-967a-6cf37ce1be68 | -15.43979 | -41.37279 | 2026-06-23 03:47:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2b2cb474-beb8-3dfc-a6ce-185adb2ee9cc | -14.0661 | -39.49214 | 2026-06-23 03:47:00 | NPP-375D | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8ea807d7-25f0-34cb-9a12-aa5337d675d8 | -5.82261 | -45.07247 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b11c073-ab23-397f-b700-f1014a930d69 | -12.03418 | -47.80422 | 2026-06-23 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48f62ac6-7f28-35e4-a18a-5abcc4d599da | -11.81458 | -47.3479 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd3c6e15-22ef-36bb-9df7-dff70d9a3d9d | -11.80928 | -47.34111 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25f2a8a9-1b2d-3b84-b476-c2e14977b3f9 | -12.5135 | -48.29953 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2e7ad2b-da66-3d02-a47b-92ce6633429e | -12.87355 | -44.36356 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 242f72cf-176a-3fa0-992a-aa16f298baa1 | -6.18665 | -44.87119 | 2026-06-23 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73c55c98-f66e-3ba7-ae04-32c71ce1306c | -12.03535 | -47.80804 | 2026-06-23 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 491112a4-87a6-3e39-ba69-30510ee5a78e | -5.94194 | -43.47166 | 2026-06-23 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f5463057-d60c-3e24-9b5d-8f7417918699 | -12.85432 | -44.3547 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bce544c0-7aa4-355f-bce1-b46fcae9d4f7 | -12.85535 | -44.37326 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a89abe9c-9ffa-3bd2-a227-3268269822f0 | -9.22471 | -45.32909 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35e433e6-b8f0-3609-87f3-ab82947b52e6 | -6.19274 | -44.87216 | 2026-06-23 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d64ac87b-a483-3f60-982c-2bab0c7a5ad4 | -6.18715 | -44.873 | 2026-06-23 03:47:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e472444-1213-3e08-b58b-726af0a42a73 | -12.85792 | -44.36023 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 6d774047-12ec-3f9d-81e3-c0628e817063 | -12.85664 | -44.36674 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f08d87c7-9e56-3f2f-a246-c4fabca038f9 | -3.869 | -42.96895 | 2026-06-23 03:47:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f1f214fe-53ef-3867-a196-3f0d3cb38d53 | -5.82719 | -45.05717 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2d94e3f-0d07-3efe-be72-128e5fa8e2bb | -6.99541 | -42.89809 | 2026-06-23 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2c8e64d2-4f4b-3519-aea4-8a40f9317410 | -12.85857 | -44.35698 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 976908e4-49f1-37db-9867-c87142033489 | -11.80251 | -47.34279 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8e0df23-ba91-384d-bf23-1168337388b4 | -14.06216 | -39.49392 | 2026-06-23 03:47:00 | NPP-375D | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9685d3b8-9359-3e19-82b0-05f465ccb659 | -14.06299 | -39.48931 | 2026-06-23 03:47:00 | NPP-375D | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ec195b96-277d-3687-8e9a-897e3b5f41ed | -9.22312 | -45.3376 | 2026-06-23 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adfa7a09-1d2c-3703-95bd-7cd56068dff3 | -12.36413 | -45.69267 | 2026-06-23 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c59d009-c4d7-347b-b3fb-9497c5069356 | -12.8537 | -44.35796 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 80547ccc-08dd-3c17-b038-e83ac96eba72 | -12.65102 | -47.67884 | 2026-06-23 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de75970d-5d37-3521-9191-730b2b039c05 | -12.65745 | -47.68026 | 2026-06-23 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcd28fa4-c73d-3caf-9c9a-7f4dbf227733 | -11.8153 | -47.3455 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14177500-d9f8-3132-aafd-9018d2475592 | -8.873 | -46.94379 | 2026-06-23 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6caf7ca1-a753-3403-ad14-078ac0e0ab1e | -6.503 | -42.2178 | 2026-06-23 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5521368e-fa04-3b35-b853-fbeca3b603e8 | -5.82961 | -45.06907 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8598fe14-11e7-3750-a77f-283c05799a1f | -12.91514 | -49.48554 | 2026-06-23 03:47:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fde4bc98-cf59-3d3d-8699-f6b0e00008df | -8.97564 | -47.97903 | 2026-06-23 03:47:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5eb305bc-a057-39e5-bbb8-df3d4bceaa37 | -12.65632 | -47.68567 | 2026-06-23 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3606c4b0-5a62-3133-918d-37c3cb6acee8 | -12.85271 | -44.35914 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| f113abbd-3983-34b5-9bba-52872179af77 | -5.81855 | -45.06995 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cef9ca0f-5e32-36f2-9a49-34c53afa8497 | -6.36577 | -43.59721 | 2026-06-23 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b158727-da08-343b-a6ca-8531a241ec35 | -5.9364 | -43.47057 | 2026-06-23 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f428a870-551f-3f97-aac7-3b743f20d59b | -8.85841 | -46.94872 | 2026-06-23 03:47:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e287892-c893-3de5-9b68-5c6c731d5646 | -12.86962 | -44.35593 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f3926ce8-f354-360e-a079-2ed5435f1e86 | -16.02843 | -43.42291 | 2026-06-23 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f17ec57-6452-3b8e-8808-d96e3fb37325 | -12.85728 | -44.36348 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1ded6bc1-290e-38aa-87ec-f86b3fe9e514 | -4.05221 | -43.24779 | 2026-06-23 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1508e6a-54f4-3dc9-8552-0954439d1b05 | -12.87026 | -44.3527 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c54a715-b96d-3f64-89e6-749813620a0d | -12.86186 | -44.36782 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d5e00a7-7020-373f-89ea-7209b943b623 | -12.8625 | -44.36457 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 0a21aa9e-60a3-3756-bd34-6e7ae619664d | -7.722 | -44.56389 | 2026-06-23 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69f4847f-f530-3731-8154-6038abd2586e | -3.86577 | -42.96609 | 2026-06-23 03:47:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f9d59f0a-a559-3da2-a9dc-93f691883ec2 | -5.81941 | -45.06509 | 2026-06-23 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 787c483d-eff2-3d51-a577-5a48b951c8b5 | -11.80819 | -47.34652 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcf162fc-663a-3df3-904c-21d3e09fa3d2 | -8.12719 | -47.89214 | 2026-06-23 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a19c5f0-8884-33fe-9a1f-d7970ff846f8 | -11.80288 | -47.33979 | 2026-06-23 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7551b1c3-7449-3e57-b2e5-a4b68d740dce | -7.36508 | -47.02773 | 2026-06-23 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3b884e4-838b-3f3d-8dc3-2461cd00df52 | -12.86122 | -44.37107 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10078e49-3aed-34d2-ba08-31424f0d1596 | -12.51223 | -48.30548 | 2026-06-23 03:47:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 248adbff-a21e-332f-960c-898dddb67b91 | -12.86643 | -44.37217 | 2026-06-23 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
