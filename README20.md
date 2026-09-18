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
| 4ad3dc86-9664-36e4-a42a-0430103de9e2 | -12.3974 | -50.7088 | 2026-09-18 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c95c745c-c203-3e26-80ac-e863a2130859 | -7.0275 | -43.6247 | 2026-09-18 01:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4486569a-0e5e-3ba2-afe0-1414b580ad03 | -9.7179 | -54.796 | 2026-09-18 01:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f5f08867-b4df-31e6-a5a8-a102741babe2 | -9.699 | -54.8176 | 2026-09-18 02:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| da5efa89-6ae7-3087-8136-c754c865fa10 | -13.2485 | -46.9226 | 2026-09-18 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 9641b683-ccbe-3242-a6e4-7c97bda5c34f | -12.3782 | -50.7111 | 2026-09-18 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 41827fb8-a7d8-3590-9e91-ab8683306518 | -19.1812 | -48.7717 | 2026-09-18 02:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 7b302d29-fd7f-323e-a4fd-d07b049822e1 | -21.6286 | -50.0008 | 2026-09-18 02:00:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.1 |
| d63d2d35-3394-3cfb-a0dd-68c85d1c4329 | -2.8284 | -50.4863 | 2026-09-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 75bb76c5-7dd4-35ae-930d-ed720dd2904c | -3.0465 | -51.3755 | 2026-09-18 02:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| ffce58b3-b163-3997-9784-807cececda85 | -21.628 | -50.0237 | 2026-09-18 02:00:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| f6a5dfe6-5fdf-3168-bc3a-4a6579ffbcde | -21.6079 | -50.0054 | 2026-09-18 02:00:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 14c6ad00-4d83-31ba-b29d-b19257c2610f | -2.81 | -50.4868 | 2026-09-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a3e59c91-f98c-39ee-8986-eba3f4baca50 | -2.6125 | -54.7577 | 2026-09-18 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| fc227b71-a1f3-3972-bbfb-2f87e4c35189 | -7.0084 | -43.6497 | 2026-09-18 02:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| eb2cbfc0-03b4-39a5-8299-f0b2d65ba79f | -9.7179 | -54.796 | 2026-09-18 02:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d87e4230-9ed9-3527-a2ec-85ef7a6d43a5 | -3.3638 | -50.4492 | 2026-09-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 1814796c-b9ae-3835-9ed4-900f21576224 | -9.7175 | -54.8365 | 2026-09-18 02:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| dff89f99-afc3-3668-a6c3-f1fe12d9a58e | -12.3206 | -50.7394 | 2026-09-18 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| caf7206d-562b-3f44-880f-a29d0607cce1 | -12.3588 | -50.7348 | 2026-09-18 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 63c538d4-0b92-3521-985b-13341bf4b5b1 | -7.0086 | -43.6264 | 2026-09-18 02:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| d768abdf-935d-3189-8d87-7f987ba9f0f3 | -5.7569 | -45.084 | 2026-09-18 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8fa3012d-3418-3ab5-9232-604eda750b24 | -19.1806 | -48.7946 | 2026-09-18 02:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c95e0866-a9c6-36c4-8945-87e31462da31 | -3.3823 | -50.4486 | 2026-09-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| fbbb387e-5d1a-33ce-bb7c-2cf743d92028 | -9.7177 | -54.8162 | 2026-09-18 02:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| d9f61270-c6da-37f2-a691-3eb1266728aa | -4.5774 | -42.9512 | 2026-09-18 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 264.3 |
| 05293288-2e45-37c0-8185-94058779bb1a | -4.5589 | -42.9289 | 2026-09-18 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4fa7b6a5-bf2c-372e-b244-f1f57c15aad1 | -5.7567 | -45.1067 | 2026-09-18 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8121fd7a-d2b1-37a7-a378-de1af1492883 | -4.5587 | -42.9523 | 2026-09-18 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 244821cd-4360-3a18-9c23-35ae8119495d | -4.5772 | -42.9746 | 2026-09-18 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a27e49c8-a7ff-3af6-81c2-2757d65520cd | -11.2787 | -43.3643 | 2026-09-18 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| a7782809-f53e-3fab-bb08-7111bafcd945 | -2.8285 | -50.4653 | 2026-09-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 5775d5a0-fc78-3209-bfa2-7ea7642b0614 | -2.8101 | -50.4658 | 2026-09-18 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f4528736-5b07-3c8a-80d0-98ce8405005f | -4.5961 | -42.95 | 2026-09-18 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a5e4198b-40ec-3d68-969c-e6aabd93c274 | -19.2015 | -48.7675 | 2026-09-18 02:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 5c28827c-0ecb-3227-ab62-1d8b0d9f6a33 | -3.028 | -51.376 | 2026-09-18 02:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5dff819f-c32a-3067-9202-b35f22c531f1 | -4.5776 | -42.9277 | 2026-09-18 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| aa23e4ac-2274-3096-ba2d-a59670fb8340 | -12.3397 | -50.7371 | 2026-09-18 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f381cb29-9a17-39fb-a602-c4990af7a6cc | -12.3394 | -50.7586 | 2026-09-18 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| bcb9bab9-57e0-3961-ae6e-a6fca0fcc6c4 | -3.3823 | -50.4486 | 2026-09-18 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8240d2e6-1852-394f-b835-21db9ad8f03f | -4.5961 | -42.95 | 2026-09-18 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0ac3acee-688e-3b6d-a108-1c6865b3cc25 | -19.5539 | -47.6346 | 2026-09-18 02:10:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 44a47c49-fe83-3158-ba3f-48daa127ff30 | -2.8285 | -50.4653 | 2026-09-18 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4bfde7e3-7859-3aad-8f4e-1038b579e256 | -21.6079 | -50.0054 | 2026-09-18 02:10:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| fefe67fd-6341-320e-9352-e415ed91440a | -5.7567 | -45.1067 | 2026-09-18 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2befe8b0-0e34-35f1-b42b-2ca9a5d64ee9 | -4.5774 | -42.9512 | 2026-09-18 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 349.5 |
| 72c54887-a45a-369b-baca-820422218c84 | -4.5772 | -42.9746 | 2026-09-18 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 55e61fe4-23ed-3f57-af92-28d09f9b8d24 | -19.2009 | -48.7904 | 2026-09-18 02:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ebb7f0ff-5e89-3346-9690-4da921ccb4e7 | -12.3397 | -50.7371 | 2026-09-18 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b1b143c5-ecb9-37c6-86a2-70371156df4b | -19.1806 | -48.7946 | 2026-09-18 02:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 120.5 |
| a14bac76-6cfc-3230-be8f-ff0a341efd30 | -19.1812 | -48.7717 | 2026-09-18 02:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 401efdb9-ccf2-3d09-a1d4-60c92f84633d | -4.5585 | -42.9758 | 2026-09-18 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6253dca7-6438-395e-9ae9-c6110a124fae | -3.0465 | -51.3755 | 2026-09-18 02:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 9298796b-59ef-3980-b90a-92f76a833fc7 | -7.0086 | -43.6264 | 2026-09-18 02:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 4f559727-6db3-3d6e-b405-8dc8caca7cf9 | -11.064 | -48.2898 | 2026-09-18 02:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9f06657e-58aa-3367-babf-52b1d2c57045 | -7.0084 | -43.6497 | 2026-09-18 02:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 596d4121-db3c-3eb4-958e-a2a596d2672f | -2.6125 | -54.7577 | 2026-09-18 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 24022305-7ab8-3ce6-bca5-8a6f07cf9071 | -3.028 | -51.376 | 2026-09-18 02:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 5b58be7c-5cef-358c-bd7f-ae60e0d7c6a2 | -9.7179 | -54.796 | 2026-09-18 02:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e4e6984d-bb23-3e91-b910-75e328d8e5db | -13.2485 | -46.9226 | 2026-09-18 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 973598d4-bda8-3031-aafe-37abe1c5d801 | -9.7177 | -54.8162 | 2026-09-18 02:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 552a79a0-ea22-3d05-81a0-34eeea27a7b8 | -19.2015 | -48.7675 | 2026-09-18 02:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 72eea86b-e428-3495-bc4b-b24919d2066c | -11.6798 | -54.446 | 2026-09-18 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 0d941ab4-7dc7-337c-8712-1322beb51b2c | -4.596 | -42.9734 | 2026-09-18 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b22caeb8-60d0-334f-b8e2-96933e17d6ce | -5.7569 | -45.084 | 2026-09-18 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bc188c0a-2440-343a-a4b6-a67a6dbe8138 | -2.8284 | -50.4863 | 2026-09-18 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| d8cd0380-26a8-3f47-a97b-30b215e5201f | -21.6286 | -50.0008 | 2026-09-18 02:10:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.9 |
| 0ae480aa-ceca-363f-a03d-c4c793561999 | -9.699 | -54.8176 | 2026-09-18 02:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d5a73174-f692-3127-9417-f7c427519a5e | -3.3638 | -50.4492 | 2026-09-18 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 3f8f7f52-45a5-3c43-bcca-5347f20821f5 | -11.2787 | -43.3643 | 2026-09-18 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| b96fd61b-a7a2-3f96-a4ca-89de29b7eed5 | -4.5587 | -42.9523 | 2026-09-18 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| bdce5055-0bff-381a-8e11-e986a96292b2 | -11.6609 | -54.4478 | 2026-09-18 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| fa9b01bd-73c3-3b0b-96b1-fd82bd172779 | -12.3394 | -50.7586 | 2026-09-18 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1f1c52ed-945c-3f23-8950-0018922c5cc4 | -3.3823 | -50.4486 | 2026-09-18 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 12f8f78f-6270-37bb-a90c-81e8335ad0a0 | -11.2975 | -43.3851 | 2026-09-18 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 05ad52af-1680-3d2b-9193-141cb2143f59 | -19.2015 | -48.7675 | 2026-09-18 02:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 22513cff-1c03-3cc6-9af7-1221fdfc6034 | -12.3397 | -50.7371 | 2026-09-18 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d2901d47-eed0-36d3-a9a4-b44b446408d9 | -4.5587 | -42.9523 | 2026-09-18 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| e816618a-802b-34de-86fe-ed8b8fca9333 | -2.8284 | -50.4863 | 2026-09-18 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4a5d67fb-c92e-36bd-aab7-020235c77e2e | -9.699 | -54.8176 | 2026-09-18 02:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 648abad5-b978-3dba-8f2d-039eb55cfef9 | -3.0465 | -51.3755 | 2026-09-18 02:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 4370dbbe-b107-3ed3-80c1-81ce34bc7100 | -11.2783 | -43.388 | 2026-09-18 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 282cdc2c-64f7-3921-8c4e-59d2cd9d37dd | -4.5774 | -42.9512 | 2026-09-18 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 70c6c5e7-f256-3c35-8f23-b2050f4d00bc | -5.7569 | -45.084 | 2026-09-18 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 440004a8-230d-3424-99fe-7f2798da3846 | -9.7177 | -54.8162 | 2026-09-18 02:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| d8c124e2-e028-3d6c-a83f-7b9ab03d410d | -10.6536 | -50.4778 | 2026-09-18 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 1d9619a6-7c0f-34d4-a211-95ed1be20a5d | -11.2787 | -43.3643 | 2026-09-18 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 927b6606-e734-335b-b7ef-c53e390abb89 | -4.5772 | -42.9746 | 2026-09-18 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c0a7e882-b246-3e66-aaeb-19825d1ab879 | -11.2979 | -43.3614 | 2026-09-18 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 0e52f622-9ca8-3793-9c2f-d3401a7b00d3 | -3.028 | -51.376 | 2026-09-18 02:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 89b6f6e2-e12e-343d-b357-686e537dea19 | -19.1812 | -48.7717 | 2026-09-18 02:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 263.3 |
| 64e46345-5d5e-3eb2-889d-31e28b497ca5 | -2.6125 | -54.7577 | 2026-09-18 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b29ee000-c125-3acb-9f84-4f6bfc844ce5 | -2.8285 | -50.4653 | 2026-09-18 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 481e0961-1428-3932-8f7b-9867734659e7 | -7.0086 | -43.6264 | 2026-09-18 02:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c66db7f7-8c65-38f2-81ef-075346e61177 | -3.3638 | -50.4492 | 2026-09-18 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| d7762e9e-c992-3b82-aacf-2fa56ad42cf5 | -12.3206 | -50.7394 | 2026-09-18 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a1899bcf-0279-3ab1-a3ed-b9697006d42c | -19.1806 | -48.7946 | 2026-09-18 02:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 6574a3e5-801d-3bd0-bcdc-41ea1c7ddb18 | -5.7567 | -45.1067 | 2026-09-18 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8261793c-a158-32d6-921f-2271e6d9c9de | -12.3394 | -50.7586 | 2026-09-18 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 67192e3c-2078-3a99-9fca-b874cdf2f6ef | -9.7179 | -54.796 | 2026-09-18 02:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |


[Clique aqui para ver as próximas entradas](README21.md)
