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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c51ef9ec-0b37-39ee-8a3a-9ac1fb4edef2 | -11.5969 | -52.113 | 2025-09-03 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 98bde791-d975-3ace-8f70-cdaa7ab5f9d6 | -11.5776 | -52.136 | 2025-09-03 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 314.4 |
| ae12472d-4380-3ad8-98c8-7653ddb01223 | -7.5476 | -61.3437 | 2025-09-03 08:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ff9b301a-1c19-3929-8a8d-a0fa8a5b1daf | -11.5966 | -52.134 | 2025-09-03 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 254.4 |
| e1300b42-b20f-38fd-a103-6b20d2592c40 | -11.5774 | -52.157 | 2025-09-03 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| e88fac9e-b8e9-3865-ae6c-93bef03b3295 | -11.5779 | -52.115 | 2025-09-03 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| fb8bf5e2-463c-3234-9c73-c7811db16cfe | -11.5963 | -52.155 | 2025-09-03 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3a219bc2-f8d6-3958-9b35-a13dc3662dc3 | -11.5969 | -52.113 | 2025-09-03 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 11be7fc4-b10f-3326-9350-08d4e3d152e4 | -11.5963 | -52.155 | 2025-09-03 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8c62bda6-090e-3834-88ef-494aa111ec13 | -7.5477 | -61.3247 | 2025-09-03 08:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| faccda85-3125-3466-8b90-795594eef6d0 | -11.5969 | -52.113 | 2025-09-03 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 118fbc72-b3f6-32e6-9feb-cf43dd5cf478 | -11.5966 | -52.134 | 2025-09-03 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 198.9 |
| 8e00751b-1da1-3bd8-858b-72f395eff0e5 | -11.5774 | -52.157 | 2025-09-03 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 336be84f-28cc-339a-9d99-c02e41603a3c | -11.5776 | -52.136 | 2025-09-03 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 259.0 |
| d929c4da-c1ea-364f-a4bf-1bea2da47f36 | -11.5779 | -52.115 | 2025-09-03 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 1d84177b-2e79-35e0-ac84-c3798cc9cb8d | -7.5476 | -61.3437 | 2025-09-03 08:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 084da580-3359-3214-8d12-8dbc261f4495 | -10.0932 | -54.7667 | 2025-09-03 09:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 2a67ef27-6feb-30e9-a554-44ede11625f6 | -7.5476 | -61.3437 | 2025-09-03 09:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b8362a03-7cdf-3140-a4aa-d472d5af04f5 | -7.5476 | -61.3437 | 2025-09-03 09:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4e5447ee-9964-3b79-b207-fe3c53bb1561 | -7.7224 | -48.7572 | 2025-09-03 09:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 000678b7-02c0-3e41-ba7e-8ba9f1c8ed42 | -7.7226 | -48.7355 | 2025-09-03 09:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 8fdbfa15-19d3-3430-bfa1-c681b0d2a937 | -7.7036 | -48.7587 | 2025-09-03 09:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 310c2783-754f-31f5-b76f-5c15c28631a2 | -7.7036 | -48.7587 | 2025-09-03 09:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 168.0 |
| f887a32f-01d9-30d8-a574-00f5f253b3e7 | -7.7224 | -48.7572 | 2025-09-03 09:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 130.8 |
| c9420c12-070d-3d58-86c3-10f81cf29f0d | -7.7226 | -48.7355 | 2025-09-03 09:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 110.9 |
| c10583f8-2ea1-318b-91a5-fbef7de5388d | -11.5776 | -52.136 | 2025-09-03 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| d0bd8dc5-4290-31d3-b60d-c86f68ed40ce | -11.5969 | -52.113 | 2025-09-03 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 62ee8643-618d-3be4-abf2-f83923b9ed72 | -11.5966 | -52.134 | 2025-09-03 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 77db554f-912d-3ed6-95cc-adaec9b65316 | -7.7036 | -48.7587 | 2025-09-03 09:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 131.0 |
| e9e5459e-894b-366d-845f-1c1ab965f9e4 | -11.5779 | -52.115 | 2025-09-03 09:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 3c32a65d-8e1b-39a9-8735-5b4e5da45116 | -7.7224 | -48.7572 | 2025-09-03 09:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 161.8 |
| b97b6672-931c-31c4-b580-a83b1af2702b | -7.7036 | -48.7587 | 2025-09-03 09:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 431021c0-b204-3375-bbef-0d5862e49c47 | -11.5966 | -52.134 | 2025-09-03 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 5f42c3d0-bccf-34df-abbd-d421e25f1215 | -7.7226 | -48.7355 | 2025-09-03 09:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 108.0 |
| db9ffe70-6854-30ec-ae3f-9b54c2c388dc | -11.5779 | -52.115 | 2025-09-03 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| db61724e-f0b5-3179-a842-925c517f02ac | -11.5776 | -52.136 | 2025-09-03 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 8349d014-a574-3b65-9c5e-760278022fa8 | -7.7224 | -48.7572 | 2025-09-03 09:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 372bc583-07da-32bb-aad0-299476315615 | -11.5969 | -52.113 | 2025-09-03 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 7ee49e2e-428b-39ef-a817-4c6f4291ae5a | -11.5966 | -52.134 | 2025-09-03 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| f4177b62-3e33-3164-aae3-02df5b3b0bbf | -7.7224 | -48.7572 | 2025-09-03 10:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 5afa5f88-a86e-33c1-b71c-bb828e974d02 | -7.7036 | -48.7587 | 2025-09-03 10:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 3f7d3769-c986-3e41-8bdb-b7f2bdfc8688 | -5.908 | -57.7311 | 2025-09-03 10:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| e01ae5fa-c8ae-35d0-ae63-5701e96e7516 | -11.5969 | -52.113 | 2025-09-03 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f5f83c22-af44-3bca-ab26-9f5cbbdf8f26 | -11.5779 | -52.115 | 2025-09-03 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| cac1c849-d75a-3050-b2f9-97a92d30a0bd | -7.7226 | -48.7355 | 2025-09-03 10:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 255fcd23-5cef-397f-ad36-e8f73cfd9df9 | -5.9079 | -57.7506 | 2025-09-03 10:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| c749f483-bab4-3f4c-8c74-722d4ab873e4 | -11.5776 | -52.136 | 2025-09-03 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| e040df2d-50cc-365e-b657-c5609be7a6e6 | -7.7036 | -48.7587 | 2025-09-03 10:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 5f693919-8aad-3bf6-8aca-74a7afd0493f | -11.5776 | -52.136 | 2025-09-03 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 423f2d7f-3865-3171-b0e8-8bb16f6b655d | -7.7224 | -48.7572 | 2025-09-03 10:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 276.7 |
| 1b09aaef-67c5-31d3-9cb7-8ad7e09f09bd | -14.5602 | -48.0654 | 2025-09-03 10:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 291.6 |
| c6551e78-7715-3e51-96aa-83a96fa780e9 | -7.6851 | -48.7386 | 2025-09-03 10:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b2e2cd0a-7618-3eb6-a350-7b5468c7464b | -11.5966 | -52.134 | 2025-09-03 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| be21e376-2db0-34bd-af96-580d136de884 | -11.5779 | -52.115 | 2025-09-03 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 61f1c003-e333-3651-9b47-cea9530b63d8 | -7.7226 | -48.7355 | 2025-09-03 10:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 0bc6159f-d8fb-37f9-9882-93d115be4ed0 | -5.908 | -57.7311 | 2025-09-03 10:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 70ac5b1c-79be-3c46-9c79-e30ade3bda5a | -11.5969 | -52.113 | 2025-09-03 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 219453d1-458b-3bd6-a78e-9f16bd1684fc | -7.7034 | -48.7803 | 2025-09-03 10:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 99.0 |
| a3285846-1db0-3d13-83e8-db4abafa26ac | -5.9079 | -57.7506 | 2025-09-03 10:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5f7f5bba-2695-3544-ac50-2e94ab13b821 | -7.7221 | -48.7788 | 2025-09-03 10:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 114.2 |
| e3076fd5-4063-3707-a1b8-ceb218551954 | -14.5606 | -48.043 | 2025-09-03 10:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 187.8 |
| ac78659c-d64e-3e31-bcea-4f3d78a0bedf | -11.5776 | -52.136 | 2025-09-03 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d80a7bb8-2f31-3f46-9568-8566e54ccfcf | -11.5966 | -52.134 | 2025-09-03 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| cc3f59df-7096-385a-b16f-b164fcfe9cf3 | -11.5969 | -52.113 | 2025-09-03 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| aaab0d15-619a-3a45-9d80-ef6e1264c25e | -5.871 | -57.7715 | 2025-09-03 10:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 39eb3724-caba-3c99-9de4-33b7af67fd75 | -5.908 | -57.7311 | 2025-09-03 10:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 2d29ecce-b4d1-3d4f-a82e-d42a40df86e8 | -11.5779 | -52.115 | 2025-09-03 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 7b9a4d99-e52a-3250-a11d-1061f17e56c4 | -5.908 | -57.7311 | 2025-09-03 10:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| edc1e213-ff2d-3213-a836-50a6e4bc9c10 | -6.8365 | -45.7009 | 2025-09-03 10:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 242a0acc-3036-376d-9a18-ffccff680a6c | -11.5969 | -52.113 | 2025-09-03 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 01edda21-97a0-3d1b-acdf-872aa76ad2a2 | -11.5966 | -52.134 | 2025-09-03 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| dfc01ab1-979e-394e-acd5-5a1feee231a7 | -5.9079 | -57.7506 | 2025-09-03 10:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| e907fcff-7fe8-39b5-a2ba-93f4ddff1bcd | -11.5776 | -52.136 | 2025-09-03 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| b26e758a-85f6-3460-bac7-918972444b5a | -6.3689 | -45.6483 | 2025-09-03 10:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 13f6a40f-efb1-3f97-a2da-785b899a8673 | -6.3502 | -45.6498 | 2025-09-03 10:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 2115e4f8-5338-3c78-bf95-87ac7758b717 | -11.5779 | -52.115 | 2025-09-03 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 1540b777-4c88-3240-9cb7-24a9ffdeb0a2 | -5.908 | -57.7311 | 2025-09-03 10:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| a3cd5a47-f141-3d7d-b27d-be0d91e535c7 | -6.35 | -45.6723 | 2025-09-03 10:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9cf202bd-0aca-3a1e-a01e-2349a15c5de5 | -11.5966 | -52.134 | 2025-09-03 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 9541ef17-a519-3d92-ba6a-dd59568d8d5a | -11.5776 | -52.136 | 2025-09-03 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 0d20d448-83d3-3f0c-a1f8-75332442c7cf | -11.5969 | -52.113 | 2025-09-03 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 7936abb9-8ab3-3137-9e05-34bf45327c95 | -6.3687 | -45.6709 | 2025-09-03 10:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1f6402cb-bbd2-33fa-be1d-38476f09aa91 | -5.908 | -57.7311 | 2025-09-03 10:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| a8b50f7b-cae1-341d-87aa-d8d02229299b | -6.3687 | -45.6709 | 2025-09-03 10:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 289391cd-3608-3180-ac58-60a0b17e0f3b | -11.5966 | -52.134 | 2025-09-03 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 555dd717-a7e8-3866-8666-3deeaaa1cbd8 | -6.3689 | -45.6483 | 2025-09-03 10:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 084acfa5-78d9-3325-98f5-c3fe4e74443b | -11.5776 | -52.136 | 2025-09-03 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| d8871e63-ac2b-39f8-bc73-43292b6e0865 | -5.9079 | -57.7506 | 2025-09-03 10:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 9f5f0105-55b4-317a-a787-32ee2b40bf45 | -5.7677 | -43.8698 | 2025-09-03 10:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4050c0e6-5c38-310d-8396-0e1c93856e23 | -11.5969 | -52.113 | 2025-09-03 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6cd54353-702f-3b45-83d0-2e9aaf1cb312 | -6.35 | -45.6723 | 2025-09-03 10:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 319.9 |
| 593d1a9f-1fee-31a4-9241-de85fbf6afb3 | -6.3502 | -45.6498 | 2025-09-03 10:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 464.7 |
| 668d6962-d9c0-3ac6-87f0-909cb3728fe5 | -6.8365 | -45.7009 | 2025-09-03 10:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 90e48f0e-9367-37d2-a02c-80ea06f2fe29 | -11.5779 | -52.115 | 2025-09-03 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| b6bbcda5-9d53-3f20-bc22-9c59c370807d | -6.35 | -45.6723 | 2025-09-03 11:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 38b4a15e-0814-3e58-b0d4-48946026bb1f | -6.3502 | -45.6498 | 2025-09-03 11:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 86d32cbc-281d-3433-90db-ef203399088d | -5.7677 | -43.8698 | 2025-09-03 11:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 6ddd8dec-4f40-3a4d-858e-f569f341a7bc | -11.5966 | -52.134 | 2025-09-03 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| cafc66c0-80e6-302e-adfb-5e951a3cdab2 | -11.5969 | -52.113 | 2025-09-03 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 4f115665-e335-3326-927e-69e6b040e395 | -11.5776 | -52.136 | 2025-09-03 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |


[Clique aqui para ver as próximas entradas](README110.md)
