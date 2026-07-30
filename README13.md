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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a71eda5f-efcc-394b-9304-a79ed4514290 | -11.9296 | -43.4288 | 2026-07-30 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| c9b0dea3-1371-3f30-ac11-be6a15155909 | -11.9104 | -43.4319 | 2026-07-30 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d8bb59ad-3066-366b-bacb-2d743a47232d | -14.3864 | -48.0261 | 2026-07-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 9131e787-341b-30fb-9f8f-e53cdab8b729 | -14.386 | -48.0485 | 2026-07-30 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6b663eef-19c7-3680-906b-f48ddcce052e | -11.9104 | -43.4319 | 2026-07-30 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 38b6b775-6502-381b-8d74-dc18611a92dc | -11.4169 | -50.0948 | 2026-07-30 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 526cb603-8605-32aa-ba8a-8e3ef8535172 | -11.9296 | -43.4288 | 2026-07-30 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| b9c3d651-7acf-30f2-8530-a9e2b1f9d3c5 | -14.3864 | -48.0261 | 2026-07-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 152.0 |
| dec8eee3-aab4-3d38-8c6d-7120558b84d8 | -14.386 | -48.0485 | 2026-07-30 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 7bdc9a51-5e19-3eba-bebf-452dd06630ed | -11.4297 | -46.8223 | 2026-07-30 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f337da76-8fa8-3b02-a79e-4a3e743f5091 | -11.9296 | -43.4288 | 2026-07-30 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 3e1cdc31-b792-390a-b6b5-a2cb1153ad4a | -11.4169 | -50.0948 | 2026-07-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 31d623e2-0649-36a6-b652-21434a5ba0e4 | -14.3864 | -48.0261 | 2026-07-30 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 161.3 |
| ceb3538f-f008-39bd-b2fe-b00f3f707a1f | -13.7377 | -51.8864 | 2026-07-30 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a63af9f6-d649-37bd-8d7c-5fa1bcfcad7a | -11.4293 | -46.8448 | 2026-07-30 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 0b34a039-67ef-3787-abf4-f0e9dce2212b | -14.386 | -48.0485 | 2026-07-30 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 7e8104e0-e200-3f5c-96ce-4d879c4f9c4f | -11.9104 | -43.4319 | 2026-07-30 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 13aaa17e-0188-3e3f-83ab-676aec6d753a | -11.9292 | -43.4526 | 2026-07-30 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 16c3cd67-e8ea-3a21-b790-9eee7fb76814 | -11.9104 | -43.4319 | 2026-07-30 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 64c76f33-ad7a-3bdc-826f-c60128c76729 | -11.3408 | -50.1034 | 2026-07-30 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| d609a355-2e85-3870-acf5-768f384cbe72 | -11.9296 | -43.4288 | 2026-07-30 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 388.8 |
| ec745894-2026-3417-8009-d3a9c7899d28 | -11.9301 | -43.405 | 2026-07-30 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 3e618c82-e11a-3870-8204-b50fbac9c4af | -14.386 | -48.0485 | 2026-07-30 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 1001c4fc-2469-3bcb-8ccd-33436275bddd | -14.3864 | -48.0261 | 2026-07-30 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 3fd624e0-8d25-3f1d-8117-9f33e677d099 | -11.4169 | -50.0948 | 2026-07-30 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 0b56150b-478f-3cee-88fb-79de0b7cc18b | -14.386 | -48.0485 | 2026-07-30 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b12829c2-43ee-3641-a478-1a21c37055c6 | -11.4169 | -50.0948 | 2026-07-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 5409168f-0427-3b81-9518-aa3af87e58cb | -14.3864 | -48.0261 | 2026-07-30 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c41de762-bf2f-3cae-b337-3a4ad53a060a | -11.3408 | -50.1034 | 2026-07-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 6115c965-e9b1-3037-a88d-63ed039e935e | -11.9104 | -43.4319 | 2026-07-30 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 391.3 |
| 5bf1254d-532d-3122-a031-9639337c5a84 | -11.9301 | -43.405 | 2026-07-30 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 1adbfe91-363a-3ff2-b57a-e2f6b24ebbd1 | -11.9292 | -43.4526 | 2026-07-30 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8b7e4160-0519-39cc-9f57-ae42689da206 | -11.9296 | -43.4288 | 2026-07-30 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 353.1 |
| 8fd9d2e0-340a-36cb-81c1-e169b2534e6e | -13.44 | -51.49 | 2026-07-30 14:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87eb216e-c55a-3605-b897-74400cef0fb1 | -13.47 | -51.51 | 2026-07-30 14:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7fde797-048e-39df-b33b-52bb44b3ca92 | -11.92 | -43.42 | 2026-07-30 14:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31e1de8b-1f86-32d9-a43d-cbf79e706e78 | -13.44 | -51.44 | 2026-07-30 14:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0be7cc6-3104-3976-986d-4f6442be7f20 | -11.9301 | -43.405 | 2026-07-30 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| f4206be0-2369-3333-b564-dcaa08ba189b | -11.9104 | -43.4319 | 2026-07-30 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 93b476b1-6067-320d-8b0a-b6e5698fd1ad | -11.4169 | -50.0948 | 2026-07-30 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| e7b476c4-edee-37c7-80b6-11aaafc64968 | -14.1993 | -43.9839 | 2026-07-30 14:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 2540cbcb-8a45-339a-9a61-ed5ecf0a2da7 | -11.9296 | -43.4288 | 2026-07-30 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 351.5 |
| d361a2af-134c-3c22-989b-e555be249c6c | -11.9292 | -43.4526 | 2026-07-30 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1638ecd3-3a4e-3f32-9c3a-36100f0edf40 | -11.3408 | -50.1034 | 2026-07-30 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c93bef70-64e0-390f-a80d-520c34317128 | -14.1987 | -44.0077 | 2026-07-30 14:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 1f4c5ea9-8f43-3f87-bfaf-3758b3af1c97 | -14.3864 | -48.0261 | 2026-07-30 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5171d03f-409b-305d-b4f1-c4de10a270cf | -14.386 | -48.0485 | 2026-07-30 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 530d6af9-29d7-35df-8238-ad9f07ade200 | -14.1797 | -43.9875 | 2026-07-30 14:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 29415b9f-9500-3892-bb28-0218c3a3f46c | -13.7377 | -51.8864 | 2026-07-30 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 15363bb2-d64a-3802-97f5-c75017b133e5 | -14.386 | -48.0485 | 2026-07-30 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 52ac71d7-2308-34a7-aae5-ba4620bb8028 | -14.1797 | -43.9875 | 2026-07-30 14:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 465192ed-10d1-34fd-8a4d-90e64bad8515 | -14.1993 | -43.9839 | 2026-07-30 14:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4036b3a9-abac-3172-9327-47202fd385fa | -14.3864 | -48.0261 | 2026-07-30 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 43ea4e95-fbab-3fd0-9964-4fb0fa572d29 | -11.4169 | -50.0948 | 2026-07-30 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 41f10420-23b7-38de-a70d-092c7572ccce | -14.1792 | -44.0113 | 2026-07-30 14:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 41912591-a45e-37d3-ac4e-65d5f965b21d | -11.9296 | -43.4288 | 2026-07-30 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| b71f15ed-9424-3793-a09b-6d2f412d46a8 | -11.9104 | -43.4319 | 2026-07-30 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 52a57135-8f54-33a9-ab1a-f629320976b9 | -14.1987 | -44.0077 | 2026-07-30 14:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0a788a06-e336-3aed-840c-18f73091fb73 | -11.2295 | -46.2403 | 2026-07-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1239f0db-84c6-3353-b588-31de99a1bd98 | -14.3864 | -48.0261 | 2026-07-30 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1b7c6b18-f49a-3b10-acee-7e5012222331 | -14.1993 | -43.9839 | 2026-07-30 14:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| b0fdbc48-6984-324a-b8f7-e6286c718983 | -14.1987 | -44.0077 | 2026-07-30 14:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 1fc37dcb-4057-3f44-a4e0-6cbaca828ec8 | -14.386 | -48.0485 | 2026-07-30 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a3cc043d-7332-36cd-973f-fd93911690c4 | -14.1797 | -43.9875 | 2026-07-30 14:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d81b7002-f3e5-3f6a-be48-562c1581642e | -11.3408 | -50.1034 | 2026-07-30 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b5bbf62f-bac8-30c5-8164-4e7840374a38 | -14.1792 | -44.0113 | 2026-07-30 14:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| d1a9cada-70c7-32a4-aca9-76843cdfbeba | -11.4169 | -50.0948 | 2026-07-30 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9b6d327b-36eb-396e-b660-e15c35e659c8 | -11.4293 | -46.8448 | 2026-07-30 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6414b5db-4bef-3021-ac4a-bb8005d26b6a | -11.9104 | -43.4319 | 2026-07-30 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 208.3 |
| b4770494-c153-3b16-9095-67a9cd55ac97 | -11.9296 | -43.4288 | 2026-07-30 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 04b8c350-65eb-3a64-8d84-51acda0bfec2 | -14.1987 | -44.0077 | 2026-07-30 14:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 5be10011-75a1-35c9-b646-b098bdb59f88 | -14.1993 | -43.9839 | 2026-07-30 14:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d50ec59c-d9cf-3e30-8497-4ea29bfb4c15 | -11.4169 | -50.0948 | 2026-07-30 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 3cca5e32-bff2-33a6-964b-404f332185fc | -14.3864 | -48.0261 | 2026-07-30 14:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 8df146fb-577e-3d9f-a1b4-da9813b855ed | -14.386 | -48.0485 | 2026-07-30 14:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0ed8570a-d747-3a6c-8188-fa1535a0b58a | -11.9296 | -43.4288 | 2026-07-30 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ed6148f7-59f4-332a-b6f5-61d75b4ac621 | -14.1797 | -43.9875 | 2026-07-30 14:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a914efa8-20b2-3817-a524-21720bb464ca | -14.3864 | -48.0261 | 2026-07-30 15:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 027a21af-c12c-305c-ada2-d7fb60310fce | -14.1792 | -44.0113 | 2026-07-30 15:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 205.2 |
| af4bc494-4bcf-3ca2-945e-d9563b161b56 | -14.1797 | -43.9875 | 2026-07-30 15:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a7c3532a-f798-3643-9fce-009b4804506e | -6.6559 | -59.1174 | 2026-07-30 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c1463721-d9fe-3e23-8b4f-42d04c6ab205 | -11.9296 | -43.4288 | 2026-07-30 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| dfb2e3a9-bc1a-35a2-a464-99158a1ceee4 | -11.4169 | -50.0948 | 2026-07-30 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6f7a8e29-80e6-31cd-ac1c-011766a8e8c8 | -14.1987 | -44.0077 | 2026-07-30 15:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 3c293280-1a60-32cc-aa67-e31b93800aeb | -14.386 | -48.0485 | 2026-07-30 15:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 91e992d9-10ab-3513-b653-c0f14e3e2e8e | -14.1993 | -43.9839 | 2026-07-30 15:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| e94565d5-ca25-3d55-9eb4-3f10ff766737 | -14.3861 | -53.4087 | 2026-07-30 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8f18c6d6-c5b9-3023-88d7-205e4f4236d1 | -14.1993 | -43.9839 | 2026-07-30 15:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 97254233-322a-3a47-9b7a-11e163df4dd7 | -14.1797 | -43.9875 | 2026-07-30 15:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| d0f72bd9-3991-377d-b1e0-02bd6623eb1e | -8.9152 | -65.0102 | 2026-07-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 1af0cc22-c01e-34b7-a22a-5ad4c48d825d | -14.1987 | -44.0077 | 2026-07-30 15:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| a49dbabb-9ca8-3971-ba8e-33991a67fb9f | -11.4169 | -50.0948 | 2026-07-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 97c12c07-887a-376c-be2a-49bb425bf250 | -13.47 | -51.51 | 2026-07-30 15:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 641c4ecd-1457-3bb7-a5cb-2a349c226fe6 | -13.44 | -51.49 | 2026-07-30 15:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b5fc3c4-65d1-3d76-afd8-aa8de2c89a31 | -14.1797 | -43.9875 | 2026-07-30 15:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 331.9 |
| 2cb0a9fd-1a24-382b-94b8-a22f12c31472 | -8.9152 | -65.0102 | 2026-07-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| da62e927-09d5-3c7c-88b2-461a73afe3ca | -14.1987 | -44.0077 | 2026-07-30 15:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 94d2f95f-556d-3e4a-b808-a4b1055109b1 | -8.9338 | -64.9909 | 2026-07-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a9212066-30c3-3e8d-8d80-e47b1efa0cd9 | -11.4169 | -50.0948 | 2026-07-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7e3bb88f-d03d-3fe2-867a-59c938cc60df | -14.1993 | -43.9839 | 2026-07-30 15:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 202.7 |


[Clique aqui para ver as próximas entradas](README14.md)
