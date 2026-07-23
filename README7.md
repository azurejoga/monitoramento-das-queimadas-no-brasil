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
| 10380faa-c466-39d1-b465-b9f8a477d56c | -12.0214 | -50.3679 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e3bbe62a-c370-35af-8c0f-4247340f16d6 | -11.807 | -47.0858 | 2026-07-23 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 839870f0-4fd6-34d6-9c10-2e0bc6f55b35 | -18.8205 | -51.2381 | 2026-07-23 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d783b678-55e7-34f4-a8de-1e6883c3086b | -11.7875 | -47.1108 | 2026-07-23 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 5b90e791-6f38-3fba-bd05-782bdb343722 | -11.926 | -50.3792 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f8d56c37-3f4d-3734-8500-88f51d37956d | -11.9835 | -50.351 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b3c68153-a914-31e5-876f-7f007997532a | -11.7879 | -47.0884 | 2026-07-23 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| d4cfdbb1-8626-3113-948f-6f641c40d742 | -18.7999 | -51.2638 | 2026-07-23 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f3ee70c4-df13-3dd3-bda3-abf34fa0cc23 | -18.8004 | -51.2417 | 2026-07-23 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 463.2 |
| fb96c23e-a3bb-3d95-82c1-ee66ca69a518 | -11.9832 | -50.3725 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8bb3cf61-1419-3383-abad-75d934c4acfe | -12.0023 | -50.3702 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 8971fc53-b919-3991-82ab-8e771ab25da5 | -18.8009 | -51.2196 | 2026-07-23 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 136.7 |
| ea019fcb-824b-3983-9747-6d8ab5afd24e | -11.6792 | -50.3437 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ef6d6f40-4a7c-36bb-a693-44f7fdb19e89 | -11.9645 | -50.3532 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fd0d5a33-397f-33c1-a689-aa32b5b641c7 | -18.8009 | -51.2196 | 2026-07-23 02:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 752bd219-3cad-31c0-9cff-7f04cf65f6b6 | -18.8004 | -51.2417 | 2026-07-23 02:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 812302dc-f555-344d-8027-cf55f5131b4a | -11.7875 | -47.1108 | 2026-07-23 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d15bf9e5-7f60-3817-bff8-2d20728b8f57 | -11.7879 | -47.0884 | 2026-07-23 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| bb5626d8-abc0-355e-af02-683b2ebffdc7 | -11.7875 | -47.1108 | 2026-07-23 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 30e19cb3-b009-3c00-a1c1-bdf687ac4663 | -11.9641 | -50.3747 | 2026-07-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e959c13e-96e8-3f2e-99b0-ec9485a135ee | -11.7879 | -47.0884 | 2026-07-23 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 63eb3cfb-513e-3043-89ee-c1e0af2f2e4b | -11.9832 | -50.3725 | 2026-07-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ffcc4818-76b1-393b-9f76-3820c0306b4a | -11.9835 | -50.351 | 2026-07-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 34729c75-f2e4-3135-bc08-f9c6c2550c5a | -11.8066 | -47.1082 | 2026-07-23 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 1b07fd1d-01e3-3ef6-9026-42af9826d7dd | -12.0404 | -50.3657 | 2026-07-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 15b7df90-4360-3206-9e56-cba3df715624 | -11.9645 | -50.3532 | 2026-07-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 51e9db69-b739-37c9-b77f-4a085a9270e3 | -12.0214 | -50.3679 | 2026-07-23 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f14aa64b-eac6-35a3-a999-082c7edff063 | -11.8066 | -47.1082 | 2026-07-23 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 9a86eb91-d525-38a2-b0b9-5b6ddfac8fe5 | -11.7875 | -47.1108 | 2026-07-23 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 891aa0be-ed38-312e-b1e0-83e0a92ce162 | -11.7879 | -47.0884 | 2026-07-23 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 6c2d201a-defe-3584-a3a5-1aeca270eaab | -11.926 | -50.3792 | 2026-07-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 6e710dd4-d928-3f33-bdef-f509b13eb29a | -11.7875 | -47.1108 | 2026-07-23 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6bbe41e2-767a-35f6-838d-b9d124126475 | -11.9069 | -50.3815 | 2026-07-23 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 03246259-a043-387f-a616-1b764d1266cf | -11.7879 | -47.0884 | 2026-07-23 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f660b1a2-e5b3-3279-be33-074208766738 | -16.2939 | -50.0459 | 2026-07-23 02:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| bf3c5712-b95e-31dc-94a1-cbc26595fbc1 | -11.7875 | -47.1108 | 2026-07-23 02:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 34a5eea9-a432-35b8-ae33-095280b48ef7 | -16.2934 | -50.068 | 2026-07-23 02:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 58f34d98-e7e5-30c4-a033-627f8199373d | -18.8004 | -51.2417 | 2026-07-23 02:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 25c9c6b4-be2b-398f-a41c-f7d362f5fff0 | -16.3136 | -50.0427 | 2026-07-23 02:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bf2731c3-cb64-3873-bc6c-69d236faf746 | -18.8004 | -51.2417 | 2026-07-23 03:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 9bd27c4e-9937-3e00-b759-c8a5e1a605a0 | -11.7879 | -47.0884 | 2026-07-23 03:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e7994f17-c9c3-3271-93bd-7a65630a15f1 | -11.9641 | -50.3747 | 2026-07-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7bb989de-8b4b-3e6f-919b-566f307d6dbd | -11.6792 | -50.3437 | 2026-07-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 1be0a719-7a56-3f04-bfdb-45d2a435006c | -11.7875 | -47.1108 | 2026-07-23 03:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 16517abb-bf2a-3301-9835-cc3486f72412 | -11.9451 | -50.377 | 2026-07-23 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| a6eff765-df36-3af3-b20b-133a415fef12 | -18.8004 | -51.2417 | 2026-07-23 03:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 93cb903b-962e-33fd-8217-b2033e5c90a8 | -11.7879 | -47.0884 | 2026-07-23 03:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 7cce9cc8-1f5e-379e-9535-92187494811c | -11.7875 | -47.1108 | 2026-07-23 03:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| ff43c149-62cd-343b-baad-55ddf07a88fc | -11.7879 | -47.0884 | 2026-07-23 03:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 9e7a5464-576c-3d11-8c3b-b032e55f2cfb | -11.7875 | -47.1108 | 2026-07-23 03:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 84f51a6a-44bf-34a1-9a34-e7e524e88447 | -11.7875 | -47.1108 | 2026-07-23 03:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 33b76f7a-7c8e-300d-9f47-eabf4ccf312f | -11.7879 | -47.0884 | 2026-07-23 03:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1509992b-0dae-3a49-b470-a4c427a8a13d | -11.7875 | -47.1108 | 2026-07-23 03:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6992b1e1-a201-37a7-9165-47238a14789a | -11.7879 | -47.0884 | 2026-07-23 03:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a67cb5aa-d135-3cd1-a358-c1ba75e2728f | -5.48791 | -45.12015 | 2026-07-23 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02e81265-4085-39ec-a9ec-6acb0a730920 | -5.54948 | -45.38931 | 2026-07-23 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85908ecc-d8e8-3990-aedd-5749329565cb | -5.80847 | -43.63615 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f22ef16c-d99b-39a9-b96f-6499f730b9fa | -4.03409 | -43.23209 | 2026-07-23 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 012a697d-a382-3e92-b97b-3690bcd27f5d | -5.80708 | -43.64317 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2565be5-132d-3f88-ab72-cf91487c46fa | -5.79851 | -43.63927 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25c3811d-7669-3576-a212-d69aec364659 | -5.70433 | -38.86015 | 2026-07-23 03:47:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d1ba05ec-2fca-3659-941f-679f30dca2a4 | -6.04652 | -43.87198 | 2026-07-23 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e271b66-4b19-337b-b75f-14af39357ecd | -4.03787 | -43.23513 | 2026-07-23 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ed1c74-c2a0-3f17-8776-1166f7f79ad6 | -4.03327 | -43.23439 | 2026-07-23 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 10df9db5-e748-37df-a28d-bf4ca44cc657 | -4.83645 | -44.07059 | 2026-07-23 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ffcfefb7-6276-30b4-99e2-b6a5a2b4db4c | -5.80331 | -43.63765 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc04e311-9c6c-3ca5-9fec-1b3c82dbe73b | -5.82466 | -44.13303 | 2026-07-23 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6db09750-1821-35d0-8afe-9c0251974d50 | -3.52395 | -42.69551 | 2026-07-23 03:47:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 927fdcbb-2725-38ab-bb28-3886f5b65a6e | -5.63911 | -44.12633 | 2026-07-23 03:47:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e62f06cd-1ac0-3826-96c8-8c949735a40a | -5.09943 | -41.71945 | 2026-07-23 03:47:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 036fd467-e6f5-3042-8f8e-e250de66dc2c | -7.0349 | -37.306 | 2026-07-23 03:47:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 542b9bbf-8290-3fab-afaa-1d361d2e7b9b | -4.58926 | -43.17399 | 2026-07-23 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be2718fb-e45b-3ad6-8422-02b7a1e3e0e6 | -5.10002 | -41.71584 | 2026-07-23 03:47:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7dee901c-1559-3f1b-ad4c-f9dd4f56700e | -5.83013 | -43.48309 | 2026-07-23 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3a407648-3353-333f-81c4-e570b4331bfd | -5.8238 | -44.13815 | 2026-07-23 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75b89f96-e374-382f-8406-503a916c0bc8 | -6.05117 | -43.87279 | 2026-07-23 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95631b80-8938-3823-8d8e-ed2a4b4b162a | -6.04736 | -43.86704 | 2026-07-23 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04eb04d6-63a1-333a-9947-334649598633 | -6.04188 | -43.87116 | 2026-07-23 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e14355d-c48a-3211-9c09-a934a0f9e683 | -4.16109 | -43.08663 | 2026-07-23 03:47:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae7dbf14-c0ec-358d-b0d5-164dd2b05a0d | -5.8087 | -43.63381 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e1ec3c9-3efd-3e1b-a04a-d3109ea22648 | -5.80692 | -43.64556 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44038060-1010-3bb5-ad52-03cf4c0dc0d8 | -5.55003 | -45.38615 | 2026-07-23 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01404095-6fa6-3adc-a21f-6f361dac4eb7 | -3.52322 | -42.69999 | 2026-07-23 03:47:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 766c1089-2b36-32eb-b3f1-f495209677f2 | -4.47828 | -40.8661 | 2026-07-23 03:47:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b1c8635-50fa-35ec-a2f7-b7e1eaa7eec4 | -5.80412 | -43.63297 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e23c8c84-914c-3dd4-aebe-561b09d0273a | -5.35724 | -43.14282 | 2026-07-23 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b5509ed-34b2-3538-9fa4-18aef4797985 | -5.36005 | -43.14154 | 2026-07-23 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11f946bc-ddc7-3add-804c-e7de590b59a2 | -6.20438 | -43.29116 | 2026-07-23 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b049f96-0f32-3bf9-ad61-0ce0a610455b | -5.82877 | -43.48502 | 2026-07-23 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73506013-e2e9-3949-b94c-63e394e7c71e | -5.80789 | -43.63848 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34e3cd00-8822-3eb8-8266-690abc4bbadf | -5.80389 | -43.63531 | 2026-07-23 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e85fccc2-2c62-3c0f-9374-b92476e83650 | -5.67714 | -43.57644 | 2026-07-23 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18667603-067d-35b4-a039-e5d35a9fc075 | -5.6383 | -47.10292 | 2026-07-23 03:47:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79cd7aff-7f27-36e8-b9a3-b393a59fa7e1 | -5.82494 | -44.13531 | 2026-07-23 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3a7cb5b-c2a7-372e-9b76-751d417be673 | -6.052 | -43.86787 | 2026-07-23 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce66c52b-9521-3815-8f94-5708f221f8d9 | -4.03333 | -43.23679 | 2026-07-23 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c611679a-d2f5-3153-9190-5f131f7689d4 | -4.59078 | -43.17204 | 2026-07-23 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39e872a5-704f-3a9d-b32b-76fd42c94632 | -3.42346 | -43.1629 | 2026-07-23 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7f6c3c2-d7d2-3ed1-a49e-f2217e49c6b8 | -11.74584 | -50.35202 | 2026-07-23 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a44aa941-395d-3314-ace2-7f76497170e6 | -6.41812 | -43.0639 | 2026-07-23 03:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
