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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 564a5e0e-07cc-369f-b873-9b629d0a03db | -6.1665 | -43.3273 | 2025-08-31 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c034ef8c-c452-316c-bfbe-8ac2b47b75a0 | -10.3126 | -59.2023 | 2025-08-31 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2ea757ee-5b89-344e-ad2d-a2d79fc6a45b | -16.2221 | -52.6778 | 2025-08-31 02:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 668660f9-764a-3079-badd-9a378f155dca | -8.744 | -62.379 | 2025-08-31 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 73444cb7-8764-369e-bf23-02bcbc77b938 | -9.5913 | -40.3448 | 2025-08-31 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 26cb845a-5003-3a0b-9344-f03ecdacd723 | -11.8177 | -46.4541 | 2025-08-31 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5adf3171-1f5f-37f8-a1f8-4f0a002a7d2d | -8.6724 | -61.964 | 2025-08-31 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 033f259e-3745-3dec-a825-1207d2bad490 | -7.1139 | -44.3111 | 2025-08-31 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 8504072a-0374-33ea-959b-ef23f9de59eb | -13.3443 | -46.953 | 2025-08-31 02:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f0ffef8d-b64e-31f0-82e1-2481c06a49dc | -11.9143 | -46.3953 | 2025-08-31 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 22f3d829-4942-3637-9a1b-a6bf1073e9dd | -16.2217 | -52.6992 | 2025-08-31 02:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 309e39f2-b84e-37cd-9919-89eabb50a46d | -8.6724 | -61.964 | 2025-08-31 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4764f1c8-6bb5-38c2-9228-aaa44e17eec8 | -9.5908 | -40.3696 | 2025-08-31 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 847b47af-1924-3dd1-8df7-a03b949d1bf0 | -8.6539 | -61.9457 | 2025-08-31 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3975b763-7c55-3e3d-8447-b57d581b3872 | -9.5913 | -40.3448 | 2025-08-31 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 2b0baf33-9a22-3a00-9e20-ffcfa617c876 | -6.1665 | -43.3273 | 2025-08-31 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9abfcedb-d329-3ee7-aa7a-904640f96d56 | -16.2221 | -52.6778 | 2025-08-31 02:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 585a423e-5e50-3b85-81d3-7f213a84ecfe | -9.4432 | -60.5692 | 2025-08-31 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f52006c1-bc90-35f2-b6e3-09ed6267c2bd | -11.3312 | -43.6399 | 2025-08-31 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 029fe249-fb16-3d11-9a2b-ee38c9d5b2c6 | -11.3504 | -43.637 | 2025-08-31 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| a592b698-b724-39f0-afce-f5277d865d02 | -7.1139 | -44.3111 | 2025-08-31 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 85b8910b-4e2c-3eca-8fe6-8499f5655b87 | -8.7439 | -62.3979 | 2025-08-31 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 30c25153-6082-397f-9891-fc9ec3bc39d6 | -11.8177 | -46.4541 | 2025-08-31 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 98e46b3b-a1e5-3c56-8bc7-da4faf37a0d0 | -11.3701 | -43.6104 | 2025-08-31 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 153a8abb-780b-32b1-bfa4-ea318b5d76c3 | -3.5995 | -47.5142 | 2025-08-31 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f5598bc7-7df1-3f61-88bc-3a615dab64ac | -11.3509 | -43.6133 | 2025-08-31 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 0f32ddc0-9a92-3fd0-90cb-f481a21fe0c4 | -13.3636 | -46.95 | 2025-08-31 02:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0b04624a-44a8-3986-a4ce-cca8fde2eb1c | -8.6538 | -61.9647 | 2025-08-31 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 337b55ef-3b00-3d99-be97-c0cc8873a1cf | -8.744 | -62.379 | 2025-08-31 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| a3ac1d79-bf9c-3e3c-a2fe-c9bbcbc47c4d | -11.3112 | -43.69 | 2025-08-31 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 2dad5d05-9fac-3e37-90bf-cc7ec12314d9 | -6.1853 | -43.3257 | 2025-08-31 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 84cc1d0b-efac-3d5a-8710-4b81c2f1354c | -10.7567 | -59.8175 | 2025-08-31 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1ce2963b-9522-32de-af13-1521d3c1a61e | -10.3126 | -59.2023 | 2025-08-31 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| b863fccd-73aa-3a33-88e8-03f7ece7bc20 | -7.0951 | -44.3128 | 2025-08-31 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 92cfeb29-7f3b-37eb-83e9-7b15b89e66c9 | -10.6128 | -44.3284 | 2025-08-31 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 59c96f5f-9b6b-30a7-8233-bf8aa23b31d5 | -6.7093 | -51.4165 | 2025-08-31 02:40:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 75e9aaa8-1e9c-38d9-a659-1b8cde2ff375 | -11.8181 | -46.4314 | 2025-08-31 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 1b08cde4-8ec0-30cc-a735-b11a81d50240 | -7.0951 | -44.3128 | 2025-08-31 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c2b7692b-353e-3888-9a1d-3a58aa503118 | -11.4233 | -63.2444 | 2025-08-31 02:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1df409fc-c390-3866-a23f-5314dc111d19 | -3.5995 | -47.5142 | 2025-08-31 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 3d4a66bb-66b4-305e-940b-e14a386559f5 | -8.744 | -62.379 | 2025-08-31 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 18bc797f-5f9e-31e4-ac3c-e947a06d3650 | -11.3504 | -43.637 | 2025-08-31 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 93260e13-9564-366b-9605-21eaf1b25926 | -6.1665 | -43.3273 | 2025-08-31 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0bafc901-f8bd-399e-9d7c-6546d9c61823 | -10.7567 | -59.8175 | 2025-08-31 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| be836072-95c0-3f8c-b7f8-d770fbd066ae | -9.0614 | -65.4355 | 2025-08-31 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 21a67499-37d6-38be-ba52-428d4adc495d | -6.1853 | -43.3257 | 2025-08-31 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| da64d7e2-0ed6-393f-a570-80d8991f7e77 | -8.7439 | -62.3979 | 2025-08-31 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 0c041149-fd1f-305b-bde3-499a736b54f0 | -11.3509 | -43.6133 | 2025-08-31 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 17ec7263-baa8-33cb-af97-b8cb3a7dafb8 | -16.2221 | -52.6778 | 2025-08-31 02:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ecdaf263-53ba-317d-b62a-4be879f60f4a | -9.4684 | -62.3286 | 2025-08-31 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2f0e87a0-cd44-38fa-9522-3af10645a3a5 | -13.4793 | -46.9547 | 2025-08-31 02:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c5943170-32f2-31d3-91a2-50daee5e53ca | -11.8181 | -46.4314 | 2025-08-31 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3142f868-78d5-3f7a-a7b7-9085808541a4 | -9.0613 | -65.4542 | 2025-08-31 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 49599313-b4f6-3455-95c7-33b538556f15 | -8.6538 | -61.9647 | 2025-08-31 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cbf693d7-dfdf-3e0a-9114-8ee3704cd45b | -11.8177 | -46.4541 | 2025-08-31 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1c7d0a2e-6786-30e2-a205-a839d2728422 | -9.4498 | -62.3294 | 2025-08-31 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7f32e92e-55f1-361b-8dd7-8426141e4377 | -11.4045 | -63.2453 | 2025-08-31 02:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e1c93148-c94d-3cb2-804b-6c5c23f0ff0d | -11.3112 | -43.69 | 2025-08-31 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 423afef1-5b58-34fd-8478-dea493a7ce7a | -9.4432 | -60.5692 | 2025-08-31 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 761c6899-3cfd-3762-bfb6-e0e41ccedf88 | -9.4431 | -60.5884 | 2025-08-31 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| bb72d84c-b45b-3a7c-97cb-0ac9e7133f2a | -11.4232 | -63.2634 | 2025-08-31 02:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 3afe44e9-11f8-3e93-a57a-848b74fbbd1c | -9.4497 | -62.3485 | 2025-08-31 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 116.5 |
| adc9c309-8afc-399c-ae6e-5a8cff3c9066 | -12.0976 | -44.717 | 2025-08-31 02:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ece9dca6-ece0-3998-a01c-4c8bfec8ba2c | -9.4683 | -62.3476 | 2025-08-31 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 1871cb68-420d-3ef9-a65f-96b74607465c | -10.7567 | -59.8175 | 2025-08-31 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 82648f4a-c1d6-3887-8de8-90bf7cf25ec9 | -9.0613 | -65.4542 | 2025-08-31 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 590de59e-9dbb-34a0-bfef-ebd7d5489709 | -6.1665 | -43.3273 | 2025-08-31 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 82a08661-9bed-3282-800a-f62f6953a0a8 | -11.4233 | -63.2444 | 2025-08-31 03:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 2a0d84cf-e890-30c9-ba02-0b016982fedf | -11.3509 | -43.6133 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6b518a4a-03b2-3e1a-912d-775a347f8642 | -9.4432 | -60.5692 | 2025-08-31 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5dfc470c-19e6-32c8-bf67-8f0c33294fbf | -8.7439 | -62.3979 | 2025-08-31 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 92471725-dc30-3713-b0a0-c8d5e1679a3d | -16.2217 | -52.6992 | 2025-08-31 03:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 32cc471b-f1e9-39f5-ae3b-a0fd36f4f1a7 | -11.8177 | -46.4541 | 2025-08-31 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| be01ac16-2e06-351b-974b-36a1e9fb1d21 | -12.0976 | -44.717 | 2025-08-31 03:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 7a518e96-7d8b-393a-b217-50093f277fe2 | -11.3696 | -43.6341 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 820bb68d-d9e6-3e8d-a2d9-a496ffdcf4f6 | -11.3112 | -43.69 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| cf54281d-0a44-3853-bd0b-c191bee82665 | -11.4045 | -63.2453 | 2025-08-31 03:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2575ca5b-beba-3ac0-9c1b-4f748d3f77ab | -13.3636 | -46.95 | 2025-08-31 03:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0a8ea113-93aa-30b4-b07e-b0a6ad320d07 | -7.0951 | -44.3128 | 2025-08-31 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6e7db371-4cdc-3e17-a190-e8fcc1b6a90e | -11.3116 | -43.6664 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9c3fcd9f-8f4e-3459-87bc-8a4109f4b798 | -11.8181 | -46.4314 | 2025-08-31 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8f2159bd-e61e-338d-9d51-1e84c958b37b | -11.3108 | -43.7136 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| c9883622-347b-380f-975f-8e9a4e430030 | -11.8373 | -46.4287 | 2025-08-31 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1db2ae9f-4f79-3c39-95ae-e9ee8740acf2 | -16.2221 | -52.6778 | 2025-08-31 03:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 790cdead-5323-33e4-b5c5-b9231d60c0fd | -3.5995 | -47.5142 | 2025-08-31 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 4c546c97-8f36-3dd4-a258-6ddc829fa37a | -11.3504 | -43.637 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 1ca17fbf-68d9-33f3-bc90-7945aaed8584 | -8.744 | -62.379 | 2025-08-31 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 37748600-31cd-379f-bd40-ac7809693aa0 | -6.1853 | -43.3257 | 2025-08-31 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 877cb243-66a5-3f0b-8d40-1a7c7b4b7a15 | -9.0614 | -65.4355 | 2025-08-31 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 85e7cb7a-44eb-3f5f-940a-cb0ad56d6f02 | -11.3304 | -43.6871 | 2025-08-31 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 906149c0-7e3d-304b-980b-ded54bd64fef | -10.7567 | -59.8175 | 2025-08-31 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dc06685c-35e2-3e93-b98e-b0ae28e9cc2c | -6.1665 | -43.3273 | 2025-08-31 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c6319749-77bf-3998-9f3d-9540c56ad29f | -11.3112 | -43.69 | 2025-08-31 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 03bc3ecf-2c3e-3066-ac13-dae762eb1342 | -7.0774 | -63.1948 | 2025-08-31 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dbab96bd-c994-3844-b990-3a8d7f491f75 | -11.3504 | -43.637 | 2025-08-31 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 524cfaed-bf00-36fe-a3b6-a5f782a8c00b | -7.0951 | -44.3128 | 2025-08-31 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d17d231a-105a-32aa-bbe7-0755d4b75143 | -8.7439 | -62.3979 | 2025-08-31 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9809a9f5-c77d-3e1b-b9b1-99df8e126a9b | -11.8177 | -46.4541 | 2025-08-31 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a167cec9-0ce8-3ed1-a80f-31782b25c642 | -11.3509 | -43.6133 | 2025-08-31 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d2ddf15b-8496-361c-a373-6722be8ae287 | -9.0614 | -65.4355 | 2025-08-31 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |


[Clique aqui para ver as próximas entradas](README13.md)
