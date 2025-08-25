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
| d9a12ad9-6936-351f-b9b6-fca809bca9b6 | -9.0415 | -65.7349 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1f1489e9-aefe-39ce-8bcb-edae9ab3ce9d | -5.1181 | -43.1964 | 2025-08-25 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3757cace-6127-3c75-bd24-34b639910448 | -5.118 | -43.2198 | 2025-08-25 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e29183c3-8028-3d5f-b2e6-0bcfb3f54c10 | -9.1722 | -59.4629 | 2025-08-25 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b2728015-30e4-3d1c-8fc5-9464738b059d | -5.0992 | -43.2211 | 2025-08-25 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 832ed6df-f682-3070-8bbe-7614e5dd715a | -8.8919 | -62.4487 | 2025-08-25 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 483df413-d154-305f-9efd-d8d60ca9c6c8 | -8.9875 | -65.4006 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 27fdeb7b-7153-3bd8-b3b3-8a22ef8cadb7 | -9.006 | -65.4 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d8c13aa4-afea-34ee-9ea1-136e4273d188 | -9.0601 | -65.7157 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 160f068d-d38d-3797-b099-7e37d09ee391 | -9.0061 | -65.3813 | 2025-08-25 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 543d6833-f393-32e5-ba13-98ff6c5e8cff | -8.8734 | -62.4495 | 2025-08-25 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 188.0 |
| 2c842190-f791-3b47-b441-6e912bbeae1f | -8.8918 | -62.4677 | 2025-08-25 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b4778df2-8bd5-38d6-8379-d4c187e3d039 | -5.0994 | -43.1977 | 2025-08-25 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c1b74287-ced7-3cea-b597-229656efbed0 | -9.0601 | -65.7157 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 3e1ab29d-6569-34d4-8af6-be6e310dade7 | -9.0061 | -65.3813 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4b297302-e84d-3406-b78b-bd39a9d671fc | -6.2644 | -59.9976 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 35dedac5-423e-3fc3-a72e-c5e3f009bbf4 | -8.9689 | -65.4198 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b3b3f4cd-f406-34ec-9c35-c2b1b54841d8 | -8.2191 | -49.5758 | 2025-08-25 03:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 70c54869-bf8b-39f6-931f-64cda2006d98 | -8.0681 | -49.6951 | 2025-08-25 03:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 200dad9e-3728-395b-90df-bb86da6951ab | -8.8733 | -62.4685 | 2025-08-25 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 548d04be-7015-3f1e-989e-1d1a410cc566 | -6.2828 | -59.9969 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 55fa997b-3c08-35ea-b121-6de9a0da377a | -9.0416 | -65.7163 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| ae8bfc84-32a3-35d7-9f34-63014b7c0cae | -7.6326 | -62.7243 | 2025-08-25 03:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0a31959c-8c18-332b-843a-2121aa45c180 | -8.9874 | -65.4192 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| abfe0bf3-890f-3e5b-ace3-f5a7bddbcf78 | -9.06 | -65.7344 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| c6d4e7a7-cb2d-3c53-bd00-f9d3e5f09ccd | -8.2193 | -49.5544 | 2025-08-25 03:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| f0841aab-4fd1-3950-9b40-8407f6a4d63f | -9.0415 | -65.7349 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| f601fb26-d711-3cfc-819c-5f92ec65ddc4 | -6.2827 | -60.0161 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3d363bfb-3301-3116-bd9a-3033b4d2179d | -8.8548 | -62.4503 | 2025-08-25 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f9ab9bec-b149-35ef-8061-4a19aa930afe | -6.8229 | -58.956 | 2025-08-25 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 6baa0e1f-d151-3d8e-878f-93e1d664e379 | -6.2643 | -60.0167 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 199.2 |
| 3e1d3307-6ce2-3871-9a49-4132911f2040 | -6.246 | -59.9982 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 3c97788a-5249-34f8-9f76-7960040018bc | -8.2128 | -61.393 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b65427dd-d2a6-3b95-9d6f-2eae4d25b993 | -8.9875 | -65.4006 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ea38b4fa-452c-3d78-a3ce-eb7dceb983d7 | -6.8413 | -58.9552 | 2025-08-25 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| b953a137-6250-36fd-9f65-7c3ce1c97af8 | -11.4593 | -55.4836 | 2025-08-25 03:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 52b05dec-5067-3e6a-8278-235c0d3614a0 | -8.0683 | -49.6738 | 2025-08-25 03:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fa99a7cf-d970-39f5-ac05-45d4f672570e | -9.1722 | -59.4629 | 2025-08-25 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 518ef051-9aa8-39f7-9e73-f8b8a6ebf533 | -8.8919 | -62.4487 | 2025-08-25 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 2b91ab22-845a-3f3b-8dbe-e9c7305c81fd | -6.2459 | -60.0174 | 2025-08-25 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| c4613220-028b-3e0b-a3a7-f60ff98e4dc2 | -9.006 | -65.4 | 2025-08-25 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c533f51e-f96e-3c5d-b269-0e47628c8a5d | -11.4595 | -55.4633 | 2025-08-25 03:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c581f561-742c-35d2-a611-dd2eaa265814 | -8.8919 | -62.4487 | 2025-08-25 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| f5af938a-02e4-301a-a58a-50cac4c377d4 | -6.2459 | -60.0174 | 2025-08-25 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| ef49e7cc-bb4d-35b7-a83d-48160289cad6 | -8.0683 | -49.6738 | 2025-08-25 03:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 53c10f6e-639a-32a8-bbc1-99823d94ef01 | -8.9689 | -65.4198 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 71f45aec-1ddb-3d39-a454-b653a7ecf748 | -8.9874 | -65.4192 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 814245ba-1cc5-31a5-9243-351b02701bc9 | -8.0681 | -49.6951 | 2025-08-25 03:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 37ba8e0b-9819-3470-94e7-88719f0467f5 | -6.246 | -59.9982 | 2025-08-25 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 23de67d1-d2ef-3cea-b6ce-7903a58ccbf8 | -9.1722 | -59.4629 | 2025-08-25 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c5a2195c-44c4-39ff-ace8-2f4b81948bdf | -6.8229 | -58.956 | 2025-08-25 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 3c632672-bd3e-38b4-b167-c2dc67d8a7ff | -6.8413 | -58.9552 | 2025-08-25 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 298ef50b-d73d-3895-b7e7-6a7520cd7e00 | -8.8733 | -62.4685 | 2025-08-25 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 740bdee6-2376-30be-a028-5a6e46d3a950 | -8.8918 | -62.4677 | 2025-08-25 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b06bf101-af48-39fe-9b4f-e517b293bd79 | -8.2193 | -49.5544 | 2025-08-25 03:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 346ef567-7ece-3d02-a389-f971a288efee | -5.0994 | -43.1977 | 2025-08-25 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 985bc65a-ec92-3d91-aca1-ca5873fc853b | -9.06 | -65.7344 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 2fba4849-4dc6-363e-b3b7-36a4e5bca01c | -8.8548 | -62.4503 | 2025-08-25 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2a707269-9963-3626-a37a-6903716e99ae | -8.8734 | -62.4495 | 2025-08-25 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 155.9 |
| d0df534d-9001-31f0-b73a-b8705c17305a | -6.2643 | -60.0167 | 2025-08-25 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4da130d8-bd9d-3758-abc5-d1bfda5a5b0c | -9.0601 | -65.7157 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 78753dc6-400e-3cd1-8194-bb797f6b40e7 | -8.9875 | -65.4006 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d3287b56-3005-3402-840a-b58e133350af | -5.1181 | -43.1964 | 2025-08-25 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 5c430144-80e7-32e4-8a30-4c86016f850b | -9.006 | -65.4 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 22fd6b2e-c2b8-3c4b-a3e4-18b28422dba6 | -9.0415 | -65.7349 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 269c7078-2120-35b6-823d-7a2090fc11d5 | -5.0992 | -43.2211 | 2025-08-25 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| baf6740c-0241-33c8-add9-5cd12db44033 | -5.118 | -43.2198 | 2025-08-25 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| b2c3acbe-50ba-3015-9946-54930cd2f0a5 | -8.2191 | -49.5758 | 2025-08-25 03:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9271aefb-d046-396a-91dd-49a86f3b8189 | -9.0061 | -65.3813 | 2025-08-25 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6c1906c9-638c-3a39-8feb-89e7aca59352 | -7.6326 | -62.7243 | 2025-08-25 03:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 68522c53-394c-3c73-8c48-2787930cf641 | -6.2644 | -59.9976 | 2025-08-25 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b18ba082-8d5a-32ab-8bb0-401fe1294adb | -8.2128 | -61.393 | 2025-08-25 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e7a1dc5f-5d7c-3764-8d3c-464424b98614 | -8.2128 | -61.393 | 2025-08-25 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 08a44203-03e0-3517-8b83-9e35927de2e3 | -9.0415 | -65.7349 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 103e874a-e022-3751-ae0a-cad8420d62e1 | -6.246 | -59.9982 | 2025-08-25 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 79bf523e-582f-316e-b68e-23f02d1197e0 | -8.9875 | -65.4006 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 05bc65a2-dd99-3fc6-8093-ca8e566e3c53 | -5.3078 | -60.2008 | 2025-08-25 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 185b9e60-5337-36a5-a84b-78db62ad4f7e | -8.5758 | -62.6323 | 2025-08-25 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5ece1853-ea16-32df-b35f-4c3d35539995 | -6.2459 | -60.0174 | 2025-08-25 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| fd1ecfcd-4b6c-360d-a54d-d6fbbd548536 | -9.006 | -65.4 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0c840091-5794-3c04-8ff5-995b00abb1e9 | -8.9874 | -65.4192 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| a5d5b283-4e7e-3831-ac81-6fd2c80ca724 | -8.9689 | -65.4198 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b6daa6ad-3fcf-3ff6-a7b0-5228a5274223 | -5.118 | -43.2198 | 2025-08-25 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2b2b3ffc-100f-3b06-9fea-fda8275b82bf | -8.8918 | -62.4677 | 2025-08-25 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6f8d663f-0537-34f7-9776-528816049b92 | -9.06 | -65.7344 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 11c92150-a69c-33bf-b9bf-97cf1f36b7fd | -9.0601 | -65.7157 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| adcd3c64-00d2-3e2c-8c1c-1c7a858ddef1 | -8.0493 | -49.6967 | 2025-08-25 04:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| feffe59a-4554-382e-b0a4-2a40044f3b79 | -9.1722 | -59.4629 | 2025-08-25 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 50d6309f-12b0-32ff-9cea-10e15dab5466 | -8.0681 | -49.6951 | 2025-08-25 04:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 916dbba2-60e1-32f5-93f8-ec050df374c7 | -8.8919 | -62.4487 | 2025-08-25 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| cffb8b4f-3484-3a40-aa81-6694af948455 | -8.8734 | -62.4495 | 2025-08-25 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 500eace1-4fa3-3f57-a2dd-2f81b7a976e6 | -9.0972 | -65.7145 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 70abbb69-a5b3-3441-80f1-d2249fb70a6a | -5.0994 | -43.1977 | 2025-08-25 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 80163ed9-f294-3360-89ce-61fe522642eb | -6.8413 | -58.9552 | 2025-08-25 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 1c4337d5-113b-3c29-8647-56395dc4ae29 | -9.0416 | -65.7163 | 2025-08-25 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 5e2fd2f6-71d5-3379-83b5-274951908f87 | -8.8733 | -62.4685 | 2025-08-25 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 1258b946-2990-3762-990f-a8ad82afbf03 | -5.0992 | -43.2211 | 2025-08-25 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 1d8c1a70-9df4-3027-9716-17d7e2e2bacd | -6.8229 | -58.956 | 2025-08-25 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 5ac9c341-7d7b-3a23-9ce5-bf8cf79c5e60 | -5.1181 | -43.1964 | 2025-08-25 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9fd911f6-390c-3c66-8e95-0c91068b6eb5 | -6.8413 | -58.9552 | 2025-08-25 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |


[Clique aqui para ver as próximas entradas](README21.md)
