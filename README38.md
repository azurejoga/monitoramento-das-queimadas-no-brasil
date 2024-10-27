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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df807edb-c5fb-3f0d-82b5-1da437af7fa7 | -12.69733 | -48.84187 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40ca5018-edc9-3f85-8bbf-667d6d527102 | -12.69638 | -48.84702 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d31b462-1984-3467-aaf5-ea4d5ad4e978 | -12.6926 | -48.84096 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6de5658e-b00b-3fb2-ad34-ce235164e036 | -15.07717 | -48.94432 | 2024-10-27 04:02:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62ad2ca4-d5b6-3a1d-b86c-90ab060c7f0d | -15.76509 | -49.24444 | 2024-10-27 04:02:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c81a6dbf-580f-30a9-9566-c91a4ca395ab | -15.76416 | -49.24934 | 2024-10-27 04:02:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140c28fc-a9dd-369e-90ea-63508ed5ba4e | -15.55692 | -49.7685 | 2024-10-27 04:02:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7c3b41a-0579-3a2b-82e3-719dc95408a8 | -15.55213 | -49.7676 | 2024-10-27 04:02:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a12eb7c-9330-3b1f-836f-1512070515ad | -17.7456 | -39.32949 | 2024-10-27 04:04:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b785796-4216-386c-94fc-ee59a27f3e9b | -17.58175 | -39.46753 | 2024-10-27 04:04:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f594a82-8bad-37f0-b528-1411c6b3c643 | -17.62741 | -39.92558 | 2024-10-27 04:04:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 833b21fe-3021-3010-a307-315220b1fc4a | -18.00808 | -42.20322 | 2024-10-27 04:04:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05d29640-2d5c-3e0f-a8cd-41e301a57b3d | -17.00775 | -49.78228 | 2024-10-27 04:04:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d4a5863-998b-320d-bf2c-5cc1beb4f6a8 | -19.17847 | -51.44588 | 2024-10-27 04:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37a6f166-4764-3b69-b5b4-9db2aeae1d82 | -19.17724 | -51.4518 | 2024-10-27 04:04:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d855bc81-d8a6-381a-995f-08a148ffc948 | -16.79182 | -52.62443 | 2024-10-27 04:04:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0887262a-3d3b-3205-abd4-c51a4651bd61 | -16.79103 | -52.6282 | 2024-10-27 04:04:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0ca1aa0-5b01-3537-a3fd-e4705680b3bb | -0.9998 | -53.6989 | 2024-10-27 04:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 2aee05c2-aebb-3db3-b57c-f297a6dadc6b | -0.9998 | -53.719 | 2024-10-27 04:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 9423515a-8570-31c1-a431-2bdeab9b21c9 | -0.9815 | -53.6789 | 2024-10-27 04:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 75b9638b-2e12-3d9c-9a46-60d6dc173a2b | -0.9815 | -53.699 | 2024-10-27 04:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 1e35e992-8e5d-3f5f-834e-e8af2c9e52ac | -0.9815 | -53.7192 | 2024-10-27 04:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e2058583-7504-3259-b746-56510bb192e2 | -1.2577 | -53.0495 | 2024-10-27 04:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 47bcf13d-7824-3846-9df8-a23455ca36b3 | -2.6321 | -54.2975 | 2024-10-27 04:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b6ee68d5-5025-3c03-9a24-6db65c75964c | -2.8515 | -49.2408 | 2024-10-27 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0b2553e7-e2aa-3011-a1dc-b722c8ee856d | -2.8514 | -49.262 | 2024-10-27 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a18d0b9a-79f2-3414-b5aa-f79561c56973 | -2.8422 | -51.8148 | 2024-10-27 04:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 1beffac2-97f7-395b-bdee-89e8635925a7 | -2.833 | -49.2413 | 2024-10-27 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| fa5ed1e9-beed-354e-ba74-a28a0ed8dfb4 | -2.8329 | -49.2626 | 2024-10-27 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 4b4e9833-0e3c-37a5-838f-f11f30afa737 | -2.7034 | -49.3088 | 2024-10-27 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 9a9fb185-590d-38be-8ddb-3e8dfff5f58c | -2.7033 | -49.33 | 2024-10-27 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 569df08e-5275-3f9c-b2fe-26bfa5a9db61 | -2.9345 | -51.7505 | 2024-10-27 04:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bdf91f82-b386-3e54-837a-0734f9bb982f | -2.9345 | -51.7711 | 2024-10-27 04:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2b579af3-1fda-3596-aed9-9cb1ba47dc59 | -2.9161 | -51.751 | 2024-10-27 04:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| b79722a2-e16f-3bd6-85d3-92741486e074 | -6.0515 | -39.8243 | 2024-10-27 04:05:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 77.0 |
| f0739ff5-9788-3713-9526-e69b5039b617 | -6.0326 | -39.826 | 2024-10-27 04:05:39 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 56cfbabc-21d6-3fe7-8d65-f663d462ab9a | -29.873 | -51.15586 | 2024-10-27 04:08:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| a19d6f55-3740-3a52-9734-97472c4e58cd | -29.81437 | -51.17751 | 2024-10-27 04:08:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| f508d72e-f102-3f25-a282-1cd7becdef7f | -0.9815 | -53.7192 | 2024-10-27 04:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 00f1f39b-a58a-3099-8572-ec06fbc87125 | -0.9815 | -53.699 | 2024-10-27 04:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 23f82f2b-b971-3788-ba50-d732698cbdf0 | -0.9815 | -53.6789 | 2024-10-27 04:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 783b8319-738f-3122-9e91-c702b4586b46 | -0.9998 | -53.6989 | 2024-10-27 04:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| fb9ed59e-8315-33a6-b933-adcece2553dc | -2.7033 | -49.33 | 2024-10-27 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 8fb68518-dd03-3845-963e-5bf7b6f7fd8d | -2.7034 | -49.3088 | 2024-10-27 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 4e714c1d-8553-383a-8a86-3e0966fd2c78 | -2.8329 | -49.2626 | 2024-10-27 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 53b22c82-c804-3835-b170-5fccffaec173 | -2.833 | -49.2413 | 2024-10-27 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 69c05850-0ca4-32be-ac01-82176d6e1cbd | -2.8514 | -49.262 | 2024-10-27 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1c2e7887-f6b9-333c-879e-437d6673232f | -2.8515 | -49.2408 | 2024-10-27 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f70433cd-c0a7-396c-aab7-3845b231232a | -2.9161 | -51.751 | 2024-10-27 04:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 340c3cc4-9720-30b0-9eef-c18d5e0ec8a8 | -2.9345 | -51.7505 | 2024-10-27 04:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 53e13d2a-af4c-3272-868e-9a13fbf48d9c | -6.0326 | -39.826 | 2024-10-27 04:15:39 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 73.0 |
| d51872b9-4f67-36ff-9745-d299538b6713 | -6.0515 | -39.8243 | 2024-10-27 04:15:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 116.0 |
| dd89e134-9dc4-3f3d-a447-7904d8a6dd8a | -0.78312 | -47.1775 | 2024-10-27 04:21:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a23bf56-220b-3969-b602-8e4937d4fad9 | -0.74383 | -47.53032 | 2024-10-27 04:21:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a907cd8-8956-3632-881c-dd23209c197b | -0.23461 | -48.79653 | 2024-10-27 04:21:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8541702f-8073-3a26-a025-2dd0a5ea6093 | -0.23013 | -48.80046 | 2024-10-27 04:21:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8ff5be8-83a4-3f72-87f8-d01313a68e6f | 2.64151 | -50.88652 | 2024-10-27 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3de89642-2619-3c7c-80a8-c3a186027eef | 1.78307 | -50.45718 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48774a8b-eae6-3afc-8b1d-12270730d6ab | 1.78112 | -50.45887 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| df273aa6-8586-3d47-9bd6-076544330525 | 1.78005 | -50.46601 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 412bf585-114e-36e7-a3ec-ec780c111f5d | 1.7794 | -50.46192 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50308639-c2f5-3122-a224-6fadffc23fd0 | 1.77925 | -50.47591 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa7652ab-f130-3dd6-89a9-83e785e64dc1 | 1.77876 | -50.45784 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e325f1bd-4ed4-3130-8399-4e3ac21f1391 | 1.77864 | -50.47181 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 417d9461-c441-3440-a615-1e5badf21c04 | 1.77742 | -50.46363 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b7ce1c32-b286-3417-bdaa-94dc9df45d77 | 1.77702 | -50.47484 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5332452-7cef-35c7-943c-673ace0175e0 | 1.77574 | -50.46667 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd5ddf9c-f5f4-3858-9b9e-b01a9ef370df | 1.7751 | -50.46259 | 2024-10-27 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cde088ef-5272-3db6-b957-b6d43c05b3da | 1.39736 | -50.7212 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4235c65-1600-3486-a8af-a495887108aa | 1.39673 | -50.71701 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9b36db5-f482-3961-9151-5362098a2984 | 1.39609 | -50.71865 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 069643f4-8385-3ddb-a003-e5b6fd14a0f1 | 1.25765 | -50.86901 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec114df-6643-3731-92be-e5c6dcfbb620 | 1.24204 | -50.88454 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e870350b-aef9-3a58-963d-a3f65a0b12bc | 1.23764 | -50.88525 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1311fd19-6529-328e-8812-a33b1018e79a | 0.42878 | -50.27084 | 2024-10-27 04:21:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f718232-f4c8-32bb-bf51-8325b9adb47d | 0.33707 | -50.9405 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9659cd1d-58e8-35fd-a7ae-71bd8f9c4612 | 0.33634 | -50.94215 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b97e72df-a6e1-3c47-99b2-77f861a5a05c | 0.33517 | -50.928 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98027184-0812-3300-9a91-d2584bb39b01 | 0.33266 | -50.94705 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe1c884d-68a9-3b50-bda0-86b4beef889c | 0.33199 | -50.94285 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6139e12-3a01-3f77-ab08-1f93502f0c8c | 0.32196 | -50.93586 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e970e37b-5fea-3c9d-9666-a1563b1c43cb | 0.31762 | -50.93657 | 2024-10-27 04:21:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8e3060c-b90a-3a79-8ea8-a7cf43ca0086 | 3.62878 | -51.29192 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e415b58-c8e4-3964-824e-4fc2ecf4809e | 3.60192 | -51.28638 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e127bc7-bf80-3f3c-b1ee-4dbeeb7cbe93 | 3.46531 | -51.25419 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43007945-578f-372b-8002-fe97be57028a | 3.46064 | -51.2549 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0a05b4f-ff28-3dbb-8d0f-10dcc352c57d | 3.44413 | -51.27249 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49832761-f814-3344-98ed-56d2cc5ffa33 | 3.43946 | -51.2732 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3194f20a-6c7c-3f8d-bd7e-e6e897b79cb1 | 3.40215 | -51.29579 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b636587-ffeb-3e36-b476-c7416393f941 | 3.3999 | -51.28101 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52554cc1-2e2c-30c7-b6c2-eb4afd2f7e65 | 3.39747 | -51.2965 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22f78c5e-035c-3593-b471-af4787b7aecd | 3.39672 | -51.29158 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 687156fc-0c91-396b-b044-3defcc7979db | 3.39598 | -51.28666 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c68f6c31-e226-3c98-b772-f531cafec94d | 3.39523 | -51.28173 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fee1284-12f3-3ebb-938d-b6b89d7a94d4 | 3.3913 | -51.28738 | 2024-10-27 04:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61f92482-8e47-3821-b588-7e54f5f65a00 | 2.51246 | -51.09184 | 2024-10-27 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8604482e-de1c-3d69-8ffe-eac7a8ba92d2 | 2.51174 | -51.08722 | 2024-10-27 04:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d3d8bec-d77d-3641-8691-ba92ad77bbe4 | 1.36653 | -51.26348 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 844e8413-67c6-37fe-97bb-452a564c28fd | 1.36477 | -51.26203 | 2024-10-27 04:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 405427a6-3a16-3d5d-afc7-d4d35b2ae81f | 1.07872 | -52.21459 | 2024-10-27 04:21:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README39.md)
