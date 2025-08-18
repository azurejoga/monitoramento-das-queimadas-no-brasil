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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5d6f788-8ee6-3b20-af81-eb9bde5eacfd | -6.4335 | -44.7822 | 2025-08-18 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| df8cfef0-cd8e-3ae5-947a-0ee1bc0bc194 | -12.9968 | -56.8597 | 2025-08-18 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e52189ff-ee8e-314a-9c93-d76fbfe061a5 | -3.9819 | -42.5396 | 2025-08-18 01:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 6252b6dd-462c-35c3-8980-e27addb9afa5 | -3.982 | -42.516 | 2025-08-18 01:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 381c6221-d1f0-37ab-90df-909fe46d3e61 | -17.3844 | -42.6235 | 2025-08-18 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 5131ccd6-cf80-316c-bbac-b56ca31f201a | -17.104 | -49.8642 | 2025-08-18 02:00:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 78845499-d5f3-373e-8cae-8cfdd2ae52e4 | -12.9968 | -56.8597 | 2025-08-18 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5c38423d-0497-3c8b-9db5-72be873a75b4 | -3.9819 | -42.5396 | 2025-08-18 02:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 7978e580-c858-3391-b023-86a5c8850086 | -13.1746 | -54.9337 | 2025-08-18 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b17717f4-bd0f-3149-80df-82ebff4571fa | -3.982 | -42.516 | 2025-08-18 02:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| c498d1f9-9504-3cfa-8e9d-a3a988bb4a7b | -17.4045 | -42.6186 | 2025-08-18 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 665e2d29-cd99-34fc-aa59-9403963ed0e8 | -6.4335 | -44.7822 | 2025-08-18 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| dc9fe7f8-2021-3701-b8d9-46371003f7c0 | -12.9971 | -56.8395 | 2025-08-18 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 70f61d59-6e33-3466-9741-1391820ff188 | -3.9819 | -42.5396 | 2025-08-18 02:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 5c827015-8adf-37dc-9e42-f8491a7ec1ba | -12.9968 | -56.8597 | 2025-08-18 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b357c92d-92ff-353c-90b7-f91c51b1b44a | -17.4045 | -42.6186 | 2025-08-18 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8782730e-d869-3876-ab53-a8d50c666762 | -12.9971 | -56.8395 | 2025-08-18 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c5bd2522-962e-3707-a68a-7701b541edf3 | -17.3844 | -42.6235 | 2025-08-18 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 54487255-22cb-3e10-a174-5d191b4eae8e | -13.2186 | -50.7781 | 2025-08-18 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 3da54f32-1f5d-30d6-9852-2e33ff4be28f | -6.4335 | -44.7822 | 2025-08-18 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8acab381-0626-3ac2-bfe8-e7556292f47d | -6.5678 | -44.4738 | 2025-08-18 02:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| ec91eba5-57d3-3cb8-91ef-86e2d3100e02 | -3.982 | -42.516 | 2025-08-18 02:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| 73120e3c-5115-3258-94ef-a7a82b093281 | -12.9971 | -56.8395 | 2025-08-18 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8dd15a67-e34a-32f3-907f-f5fa0b134f0a | -17.4045 | -42.6186 | 2025-08-18 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 472c9510-f7d3-3172-b3a6-f8f46c1605cf | -6.4335 | -44.7822 | 2025-08-18 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 37b6bcd3-6b80-3980-baae-fe2206655190 | -17.3844 | -42.6235 | 2025-08-18 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 68b809a4-fd91-333c-beed-b642afe00a17 | -12.9968 | -56.8597 | 2025-08-18 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a6a09e48-4b94-3d2f-b991-2593c3dfd893 | -9.518 | -60.5268 | 2025-08-18 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fc178ba7-d271-39d3-9442-159956ea5fbb | -3.9819 | -42.5396 | 2025-08-18 02:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 0bae07fe-8cc8-378d-a0c1-5a5ef8f29d70 | -12.9971 | -56.8395 | 2025-08-18 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6acdd10f-9194-354c-9264-61d4e847f94a | -13.1746 | -54.9337 | 2025-08-18 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2077dddc-673b-3153-9a7e-a485bb49fc65 | -9.518 | -60.5268 | 2025-08-18 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d43f2d1a-c4ff-3bca-8f79-9d004cf41e1a | -13.257 | -50.7732 | 2025-08-18 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8f149bc1-4c9b-35de-872b-245640da99e5 | -3.9819 | -42.5396 | 2025-08-18 02:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| c5b65576-fd6d-321a-b793-c5a3c7bc9b37 | -6.4335 | -44.7822 | 2025-08-18 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fd074ae1-927e-3fea-8ea1-1d4791176a08 | -17.3844 | -42.6235 | 2025-08-18 02:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 3ad81b4c-739b-31e8-9d74-2d0bb0fd94ad | -3.982 | -42.516 | 2025-08-18 02:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 857893c5-2dbd-311a-80e3-04dd8687bd61 | -13.2574 | -50.7516 | 2025-08-18 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ab25d932-9edb-3456-a2c6-71c0bf3061c8 | -17.4045 | -42.6186 | 2025-08-18 02:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ee7b4ec9-6ba5-383e-9a07-61737985fb9d | -13.2574 | -50.7516 | 2025-08-18 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f2a1339b-c14d-3571-9f6c-df7e9e67aae3 | -17.104 | -49.8642 | 2025-08-18 02:40:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e54b66db-0c3e-3a71-b550-554fe494e197 | -3.982 | -42.516 | 2025-08-18 02:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 1e182486-f81d-355a-9e9f-a0236170b936 | -11.8512 | -51.5801 | 2025-08-18 02:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a51025d0-909b-3a9f-9486-0aab0716ea9d | -3.9819 | -42.5396 | 2025-08-18 02:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 58f2db70-bef4-3747-ab9e-dffd3e93742b | -12.9971 | -56.8395 | 2025-08-18 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| abcbcc55-c7c6-3a2f-9489-b4e97ddaf649 | -6.4335 | -44.7822 | 2025-08-18 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 42f52d6e-c57d-3607-b0a5-03287994dc82 | -17.3844 | -42.6235 | 2025-08-18 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 54b47212-240e-38f2-a7ba-6254d1d34b09 | -13.257 | -50.7732 | 2025-08-18 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1af06356-79fc-375f-9500-e6c40e7ab498 | -17.4045 | -42.6186 | 2025-08-18 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 92df8bad-061d-3a1d-8dfc-5c6a4c885250 | -9.518 | -60.5268 | 2025-08-18 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| feb23ce6-2f30-3a90-83bf-3fe92f12c453 | -14.9815 | -54.7743 | 2025-08-18 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b0f61e2f-451d-3275-92e7-f6c4ead120bc | -17.3844 | -42.6235 | 2025-08-18 02:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3014e995-dbb7-39fe-a6d3-41f5be1913d5 | -17.104 | -49.8642 | 2025-08-18 02:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| fc85fa87-6ee8-3199-8c07-246ea84d1a07 | -9.4956 | -40.3586 | 2025-08-18 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| b61766ac-d921-325e-9323-ad0a69c72b5d | -9.4952 | -40.3834 | 2025-08-18 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| a22642c6-ef01-391f-ba08-da5b1f2bf8b8 | -17.0842 | -49.8677 | 2025-08-18 02:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 22de0038-6b4d-3b97-848d-cc36d94cad93 | -17.1036 | -49.8865 | 2025-08-18 02:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bdf59b9e-6817-3854-9b3f-f95e1798bc3e | -9.4765 | -40.3613 | 2025-08-18 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.2 |
| e6ac7ac1-ebcc-3eb7-9976-15659301f99c | -3.982 | -42.516 | 2025-08-18 02:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 61e00c33-5554-393e-9e28-21899d56be4d | -17.4045 | -42.6186 | 2025-08-18 02:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 5305874f-fed1-36ca-80ee-adf3c342b756 | -17.0838 | -49.8899 | 2025-08-18 02:50:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 305d85e7-e2fa-35e9-8ec8-e0057ed29fc0 | -9.4761 | -40.3862 | 2025-08-18 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 4201d070-f2b0-3641-9441-60230e6ea535 | -9.518 | -60.5268 | 2025-08-18 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e2b98060-6134-362c-b991-1a12717f8225 | -6.4335 | -44.7822 | 2025-08-18 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 55526da6-7ec9-3f2e-a303-2f76e7a9ba3d | -6.4335 | -44.7822 | 2025-08-18 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e2555edc-4150-3472-ae00-cbbf8558166f | -17.1036 | -49.8865 | 2025-08-18 03:00:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7da0deb8-938b-3ded-98ab-350bbcf3569e | -17.104 | -49.8642 | 2025-08-18 03:00:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3cc211d1-1b77-3804-9e80-d0bba5aae1a0 | -17.4045 | -42.6186 | 2025-08-18 03:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e35a77d4-6d6b-32ee-bd3a-55ee7fcf806d | -9.518 | -60.5268 | 2025-08-18 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9ea4a60c-3809-3e9b-a126-d76427ea55fb | -14.9815 | -54.7743 | 2025-08-18 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e729c57b-c3a2-3ee0-82e4-98b1e28c889b | -6.94151 | -34.8888 | 2025-08-18 03:04:00 | NOAA-21 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4ce983e-03bf-3071-abd4-05cf3b33581b | -6.94131 | -34.89269 | 2025-08-18 03:04:00 | NOAA-21 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a39d02c6-1bd6-34af-bb16-450b2b662e8e | -5.07229 | -37.71641 | 2025-08-18 03:04:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c020c720-110b-3d77-b0ec-472410693f85 | -6.94095 | -34.89202 | 2025-08-18 03:04:00 | NOAA-21 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a10e0181-f010-3560-9f14-b07ae7788d4a | -6.94189 | -34.88949 | 2025-08-18 03:04:00 | NOAA-21 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65d7593a-6a1c-3941-9efd-01c20650364f | -5.52039 | -37.48462 | 2025-08-18 03:04:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7a698e31-899f-3d02-80a9-7ddc9d064c69 | -5.52334 | -37.48457 | 2025-08-18 03:04:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca5d5d17-b6d4-3066-b086-45af4050b36c | -6.90733 | -39.55167 | 2025-08-18 03:04:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e0b98527-07f8-36c3-bbf5-ea07272bbc6f | -9.49087 | -40.37469 | 2025-08-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f16da4ee-e70c-33fe-ab8f-d41b144231cf | -7.83084 | -38.41904 | 2025-08-18 03:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d18fb592-c184-36be-9007-1175475245b9 | -9.4861 | -40.37348 | 2025-08-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 07a1a83f-e7b0-3bc4-8dcc-f00dbb775bcb | -7.83187 | -38.41367 | 2025-08-18 03:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 752569ea-6fdc-3e27-9574-507e8e0b71fd | -20.25299 | -41.95675 | 2025-08-18 03:08:00 | NOAA-21 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dce7c25d-bc87-3d05-9337-56b810a9e70e | -17.39434 | -42.6223 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7feba462-d36b-306e-b516-0ed83ab8b136 | -18.61537 | -42.44495 | 2025-08-18 03:08:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4e018d7d-0abe-3c12-a87e-a23a8d77048a | -18.61313 | -42.44409 | 2025-08-18 03:08:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8d666f17-360d-338b-a676-6b79097d1844 | -17.39271 | -42.62919 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2d58fa11-6984-3045-b057-b519b755cf40 | -17.38801 | -42.62403 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| c0536d38-70ce-3494-99fc-626fd2ca9aab | -17.62502 | -39.92915 | 2025-08-18 03:08:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4815b34f-e920-3dd4-ac5f-34dfaeba4372 | -17.38579 | -42.62755 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| aa2b407a-4389-3105-b4f2-d670c18efbaa | -17.38741 | -42.6207 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 648ff8fb-fbbc-34f2-be53-4587dca05c1d | -17.39495 | -42.62559 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 24f07f19-761e-3131-a92d-8f9b5316767c | -17.39652 | -42.61877 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a1fa8e92-d398-3f97-b8e8-d82ddf359ace | -17.38961 | -42.6171 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 98af12cc-18e3-352a-9fe6-03af3fc250de | -17.38643 | -42.63093 | 2025-08-18 03:08:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 849a4f7e-b3a6-33ca-9b46-8b4bbc1a29df | -20.42255 | -43.6793 | 2025-08-18 03:08:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2981c329-b197-32dc-a677-9fb3c2046482 | -13.1998 | -50.7591 | 2025-08-18 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 67d49fbc-04bb-36dd-836e-05514d64253d | -17.4045 | -42.6186 | 2025-08-18 03:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 20517fb1-9818-3a27-86f6-06201793397f | -13.219 | -50.7566 | 2025-08-18 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 9eb2b923-ffe1-3b9c-ad2b-4ad569fb7f6d | -17.104 | -49.8642 | 2025-08-18 03:10:00 | GOES-19 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |


[Clique aqui para ver as próximas entradas](README8.md)
