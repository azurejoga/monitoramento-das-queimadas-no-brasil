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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cc898f8-f660-344e-8ef9-1c8eed893060 | -12.8359 | -44.3422 | 2026-06-24 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 5a353ccb-5138-3639-aea2-f4018bab4f92 | -12.8552 | -44.3389 | 2026-06-24 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 6843e9e6-a02d-3500-9382-cbaa0e11eec7 | -12.8354 | -44.3657 | 2026-06-24 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.9 |
| d208ea11-6279-3b4e-a69f-f66d2256f34a | -12.8548 | -44.3625 | 2026-06-24 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 5f821dba-52d7-3e07-8ddb-9d89ceef7f48 | -12.8354 | -44.3657 | 2026-06-24 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| fe952749-cd9d-302b-a563-9b685c3efa3c | -12.8359 | -44.3422 | 2026-06-24 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 36792ff1-57b7-3d19-8df0-7e477c1266b2 | -12.8552 | -44.3389 | 2026-06-24 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f188294b-9f15-3607-bd0f-00dc977026af | -12.8359 | -44.3422 | 2026-06-24 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 38c645ff-fd61-3b36-b003-0b39f6826192 | -12.8548 | -44.3625 | 2026-06-24 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| d036ec00-efb7-3ccd-8d1f-180117a28e31 | -12.8354 | -44.3657 | 2026-06-24 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| d761ed76-e932-3dd9-8b9b-baf29e5c5174 | -12.8552 | -44.3389 | 2026-06-24 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 1391aa25-045c-3c46-86b9-42d2272787e2 | -12.8548 | -44.3625 | 2026-06-24 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| a1807d43-ed8d-3201-8c34-152bb733fb0a | -12.8354 | -44.3657 | 2026-06-24 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 4e79a584-5029-3ed1-b08d-36b7f02b4e78 | -12.8359 | -44.3422 | 2026-06-24 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d9b95473-5440-3cbf-9f58-ffd067e1670c | -12.8552 | -44.3389 | 2026-06-24 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1957237a-b05e-3228-b090-31bd90900f9b | -12.8548 | -44.3625 | 2026-06-24 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 4148dee4-10d6-362c-9f50-fc1a87b052f4 | -12.8354 | -44.3657 | 2026-06-24 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 8c045eb6-4d63-3756-a8f1-8ba932284763 | -12.8359 | -44.3422 | 2026-06-24 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 43df20f6-2040-3c58-814f-d7edbb0720ef | -12.8552 | -44.3389 | 2026-06-24 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bebead4b-216e-335b-bcc3-30c38bd846ee | -12.8548 | -44.3625 | 2026-06-24 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ad81f5dc-399e-36c5-9a4d-1817203bda17 | -12.8359 | -44.3422 | 2026-06-24 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 68f3a869-8b94-3f65-b6c9-d76ba649ccd4 | -12.8354 | -44.3657 | 2026-06-24 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 6bf781e6-63a7-35bb-aef8-6bf4e0f02b46 | -12.8552 | -44.3389 | 2026-06-24 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b3b30660-b9f0-3885-b4c7-a67283340f83 | -12.8359 | -44.3422 | 2026-06-24 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 7ecb21e9-1b62-3ed4-8a53-78ec836e38e4 | -12.8354 | -44.3657 | 2026-06-24 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 10e14a75-db99-31e8-8eac-4f8ea2f5e5e6 | -12.8548 | -44.3625 | 2026-06-24 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 5cec3c39-bf60-3acf-b4f9-6b15e8492df4 | -12.8552 | -44.3389 | 2026-06-24 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 45063700-197e-32ab-a44d-2863ebf4476f | -12.8354 | -44.3657 | 2026-06-24 09:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| dd60ca00-fdf8-3fdd-a8c5-95ccfbe1cbba | -12.8359 | -44.3422 | 2026-06-24 09:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 652208ed-c23a-3070-b694-3889e7ecf4a6 | -12.8354 | -44.3657 | 2026-06-24 09:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 03aa5a54-3590-3228-96b4-fca9768a1689 | -12.8354 | -44.3657 | 2026-06-24 09:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| d77fc58c-8c3f-3050-ab68-b28fb195d1a7 | -12.8548 | -44.3625 | 2026-06-24 09:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| b10a69ee-07bd-3475-99be-5d814cef2f68 | -12.8548 | -44.3625 | 2026-06-24 09:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 68f0869e-8425-32f0-8668-8615b1559b01 | -12.8354 | -44.3657 | 2026-06-24 09:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| bfef8566-df73-3b70-9a9d-bbc67a0a561c | -12.8354 | -44.3657 | 2026-06-24 10:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 2baa9eb2-eba3-3f3a-b086-4a888d46f4bd | -12.8548 | -44.3625 | 2026-06-24 10:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 388f2761-dfc3-37a9-8c42-30a5d2870a2d | -12.8359 | -44.3422 | 2026-06-24 10:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 18edda24-408e-35d6-a040-5ff988b2409c | -12.8354 | -44.3657 | 2026-06-24 10:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| d9ded331-379e-3300-a24e-bf53794cc0ae | -12.8548 | -44.3625 | 2026-06-24 10:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| dd9429d0-aff8-3607-86b7-304981d6cc14 | -12.8354 | -44.3657 | 2026-06-24 10:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 44f944c7-af73-3853-a5ce-205193f9d20e | -12.8359 | -44.3422 | 2026-06-24 10:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 38555051-f355-3ebb-ad65-752bde1698ce | -12.8548 | -44.3625 | 2026-06-24 10:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 3e1bb7b0-d1e3-3792-b0ec-c8f69ba4d442 | -12.8354 | -44.3657 | 2026-06-24 10:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 6d170058-e80b-36e5-8fe9-41cf0e966cb6 | -12.8548 | -44.3625 | 2026-06-24 10:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 938af94a-87cc-38ba-afca-d4a3a2cba886 | -12.8354 | -44.3657 | 2026-06-24 10:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 99677fd4-5bed-32bb-b15b-33c2435c2587 | -12.8354 | -44.3657 | 2026-06-24 10:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| e0a875be-fc8e-3434-ac2a-86af904c787b | -12.8548 | -44.3625 | 2026-06-24 10:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 4b8575cf-c20c-389a-8615-561c62fe9cdc | -12.8354 | -44.3657 | 2026-06-24 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 4e59ec2a-0c92-3829-b9e7-4042e7d8b353 | -12.8359 | -44.3422 | 2026-06-24 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6b30f6f4-a7a6-3d7b-ae51-fc0f81f2e8b0 | -12.8548 | -44.3625 | 2026-06-24 11:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1f853ff5-f396-3139-ab24-14d8fb457f77 | -12.8548 | -44.3625 | 2026-06-24 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| eb0959f8-d11a-3724-8e3d-dd89fe228ced | -12.8354 | -44.3657 | 2026-06-24 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| f1b69c29-bdf3-3586-b6b3-2e07abefaa28 | -12.7764 | -44.4223 | 2026-06-24 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 213.2 |
| db0339d2-84c9-3d4c-8803-8ebbeba58329 | -12.776 | -44.4458 | 2026-06-24 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 8dac34e5-7f31-346b-b5e7-8079d8a3dd03 | -12.7958 | -44.4191 | 2026-06-24 11:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| d7e23f32-5678-3989-8507-2dec9d2b15b5 | -12.776 | -44.4458 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 364.8 |
| 88ea27bb-6f81-3d1e-b2ae-850574124717 | -12.7764 | -44.4223 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 515.8 |
| 466aae15-39c1-33b8-9fec-14a2b2ba654e | -12.8548 | -44.3625 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 70d3565c-4545-3b8a-8a17-def98c8d5d28 | -12.8354 | -44.3657 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 7abaa546-c58a-36d3-abc7-dc6693bb3fb8 | -12.7953 | -44.4426 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 66cfe662-544f-3ee9-ab03-065d1efef176 | -12.7958 | -44.4191 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 312.5 |
| ed015d4c-2013-3973-bb70-87dd49fece2f | -12.8359 | -44.3422 | 2026-06-24 11:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| af34e7eb-5130-33d7-a7a8-ed5e377967c3 | -12.7764 | -44.4223 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 874.5 |
| bca29930-80ec-342d-b511-67fce9aa3588 | -12.8354 | -44.3657 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 4b23aa97-abd2-30ea-a9ce-fb1191c95441 | -12.8359 | -44.3422 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4df391a0-5532-3cea-a6d7-c16f600405b3 | -12.7953 | -44.4426 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 88ed3e29-86cd-3c2b-bf4a-b4b8418931ba | -12.776 | -44.4458 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 519.6 |
| 84023a75-6fbc-3376-a759-9b314848990b | -12.7958 | -44.4191 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 324.5 |
| 193136fe-ed66-39ce-bb50-957165586586 | -12.8548 | -44.3625 | 2026-06-24 11:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7407c1bc-9e88-3dff-8bc0-a4bacc3f8375 | -12.8359 | -44.3422 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8b5088df-296e-3a7a-8ba3-5d2bfd2637e4 | -12.7958 | -44.4191 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 348.8 |
| 1bf30cf3-26aa-3b63-92b4-1acf70075ea0 | -12.7764 | -44.4223 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 727.6 |
| 6513b9b9-6c63-3297-a0b6-111b57f1fee9 | -12.8354 | -44.3657 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 4a10f923-3b73-3a8b-b923-92db3e3fff36 | -12.8548 | -44.3625 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 9e2c13c3-2c33-3458-8a94-a864f965a9e6 | -12.7953 | -44.4426 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 219.6 |
| e0018cae-214e-3e7f-a322-4c6250fd645a | -12.776 | -44.4458 | 2026-06-24 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 412.8 |
| 58c3fe08-a275-3362-99c5-1a6471281c00 | -12.7764 | -44.4223 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 619.8 |
| 22826d3f-c724-3205-98e1-b1d15c48fdf1 | -12.8359 | -44.3422 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 152ced56-b2ee-35c0-89ad-37e3302bf165 | -12.8548 | -44.3625 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| fe2dbb14-9f37-3f09-87d1-d0661c507e28 | -12.7953 | -44.4426 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 23ff4e87-6b79-3230-9bde-6471171f7187 | -12.8552 | -44.3389 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 669859c6-08ff-381d-86e8-e6f0aed69b6d | -12.8354 | -44.3657 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 8485152e-635f-3e59-b1e2-600702d4736f | -12.776 | -44.4458 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 402.6 |
| 291660c8-5957-36ad-9c13-625ccf6c820c | -12.7958 | -44.4191 | 2026-06-24 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 920489d5-af3c-383d-b140-c03d16a8916f | -12.8354 | -44.3657 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| a6369218-666e-3a45-89fb-2641ae81f3f1 | -12.8359 | -44.3422 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| df2a3cb5-a71d-38b3-9137-c61454a9af69 | -12.7958 | -44.4191 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 3bc1ad96-02c8-3cac-983c-b64201555293 | -12.8548 | -44.3625 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 2697ffed-d7f0-3fcd-8ecd-91f946d325e6 | -12.8552 | -44.3389 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a1046d65-41d7-3c6b-862f-76d3a74fb0b3 | -12.7764 | -44.4223 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 513.8 |
| 5b2e0683-5125-33a0-bad6-9c2bc5f09c16 | -12.776 | -44.4458 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 382.5 |
| cd024734-db3a-3d8c-880c-09dd31300c5f | -12.7953 | -44.4426 | 2026-06-24 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 7e6a1225-f60b-301b-bd80-99b7f3fa6332 | -5.79893 | -45.12659 | 2026-06-24 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 57c73970-708c-3bcf-ae8d-cf9be93e9e5f | -5.8201 | -45.05845 | 2026-06-24 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| edd3f277-cfff-3ad0-8d55-92424391ee04 | -10.15895 | -56.62325 | 2026-06-24 12:08:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4c62b258-0c83-37d7-9d8a-847753f39146 | -11.30434 | -51.40933 | 2026-06-24 12:08:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 04898678-1e88-348c-8ba0-50f11dd5ddcc | -8.61257 | -45.98837 | 2026-06-24 12:08:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 934e3122-8e34-3956-bfda-764805a09914 | -12.77062 | -44.44453 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 360ccc29-07c7-3d0d-8036-3d624bdf985f | -6.93588 | -51.939 | 2026-06-24 12:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ca88b062-cb56-3d66-806c-89f81dd98349 | -11.21034 | -54.33274 | 2026-06-24 12:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README21.md)
