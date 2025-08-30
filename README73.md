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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bffc9382-4392-3aa3-8912-9b2453e094ca | -13.37195 | -46.98486 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 458c4dcc-c0dc-307a-ae2c-1ad4e6bedf29 | -13.38075 | -46.9642 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 42c6b817-40b8-3395-865e-16215d0acb5f | -11.35675 | -63.25388 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8957cf8-75b1-3f73-8475-3aedd8456f51 | -13.36786 | -46.9819 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2bf5a90-29e9-3826-9e84-93e93c50d1f0 | -13.38848 | -47.03012 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6b19a97-1c7d-3ab4-a161-36379c816075 | -13.68274 | -46.91766 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef55e0e2-cd3d-34bf-8c28-4e22d6654907 | -13.37256 | -46.99836 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e05a825e-383a-369a-a6cd-c05fd8b0e54b | -10.23867 | -68.0955 | 2025-08-30 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0748f4-09f3-39ae-b150-eeba7966c021 | -13.55433 | -46.95115 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a399ebb-0d95-318d-ac6e-ddd0949182e4 | -12.62695 | -57.01284 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c12bc07f-c050-3640-82c2-678fea5af541 | -12.93758 | -48.13348 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20401e71-3424-3b49-96f0-bcc5a40376c6 | -12.92953 | -56.97802 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 294489b8-e954-332c-addc-f836e2954d90 | -13.54774 | -46.95219 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9cfdb81-4758-31d4-9e20-90ff1fd77c03 | -10.35143 | -64.46316 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0765be3-9bd0-347d-9a0b-d50088cd2d5a | -13.37447 | -47.01953 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d378b969-4af1-3e53-aa7f-262a13d0d3e1 | -13.97555 | -46.32328 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe4d7d3b-a6ef-3b94-ae0c-749b8231d077 | -11.39704 | -63.25306 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b46a8ab3-ff57-3b0c-a0b4-c647ecac4fac | -14.10388 | -51.78198 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c25b8c9e-2d09-30f3-a598-423bb36c2606 | -12.84402 | -48.18035 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eae34549-a941-3f5d-9321-cfff0aac169c | -12.84835 | -48.15598 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f86373d9-3892-3fc9-9a66-971cbd5de982 | -13.38141 | -47.01514 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 13295f6f-a14a-30a5-a6c3-b8da35d6841d | -13.36625 | -46.99704 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eafd89d5-ebe8-3335-90ec-8e7e2ae5780b | -13.38892 | -47.00579 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5109a472-a1f3-3e18-a271-bf1d1b2fbc29 | -9.72878 | -64.91274 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c3e634f-0ec1-3963-8cb7-5b57da49f685 | -13.36925 | -47.00873 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c96c6217-3ce9-3382-95c4-dbb28154b086 | -11.73224 | -51.7559 | 2025-08-30 05:12:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6be1282-0a27-375e-8398-ed9d7dac1c81 | -9.75907 | -65.08442 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d968222-4ca3-32de-b0ec-94da00e3eff5 | -12.84561 | -48.17839 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eb1e316-55b4-36ba-9549-646fbf941e17 | -12.94539 | -48.13075 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14681e8b-61b2-32af-a1be-5f45a55eb1cb | -12.92241 | -46.35527 | 2025-08-30 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bf16ea5-713a-310c-bb55-3f1e9c030548 | -13.38172 | -46.97286 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f2f18f4-2894-3038-bcfd-b4efafe2d7ad | -13.45304 | -46.97046 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f53d2f8-8c58-3131-ac13-e73e04eec27b | -13.45507 | -46.95217 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e274992-3fe0-3dc8-818a-b2109a390e18 | -12.84705 | -48.15385 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0202069f-92b8-3794-b932-5a6a299cc02f | -12.82861 | -48.12151 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d473e7a-4f4f-3ffd-98e6-b11ecd79ce51 | -12.9218 | -46.36064 | 2025-08-30 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 358681a7-cbb5-339c-9c61-27b6e7288d82 | -13.38484 | -47.00403 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56e04c08-f0c7-32d4-9c3c-24208f47b200 | -12.84295 | -48.15127 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 604fd3b5-3271-3b3c-9d57-104632baf17c | -13.38199 | -47.01006 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 02dfa593-f45e-3ae1-98b6-aaee2ac1ac19 | -9.7251 | -64.90739 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b75d44a5-6408-3c0f-a499-01b3b0dce552 | -9.76026 | -65.08272 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a958f28-deed-365f-8415-51645767bdec | -13.4559 | -46.94467 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af195f54-ee10-37ed-b984-fa46a7104dfe | -12.63092 | -57.00961 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8516acb6-4f31-337a-afbf-ff06dc8379d5 | -13.36994 | -46.88767 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 91b73fa8-fbc3-3f38-9bc0-8170de221ce9 | -9.33466 | -68.21797 | 2025-08-30 05:12:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3242a0a7-9036-3d94-b391-00a2fba3f4b4 | -12.60894 | -57.01477 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e88b977b-ff4e-313a-81fb-468b703ddf04 | -12.92896 | -56.9818 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e35022b-8d12-3033-b5d6-ef881fc8d688 | -12.8514 | -48.16797 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e89515b-62ab-3b15-862e-4a8edea2cfd3 | -13.38256 | -47.00505 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c68cab93-c81f-3db9-826b-7ac57bb4b221 | -13.50126 | -46.84086 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb57079d-86b7-3377-93d9-17baeebcb022 | -9.67506 | -65.03078 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 260dec68-b9fa-36ff-a11d-eca4ec8c61bd | -12.82229 | -48.12438 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c15c97d-8268-3219-8a81-48b95fa6014e | -12.92907 | -48.11708 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed1c0c41-2237-397f-95b3-3ee043e10a32 | -13.50873 | -46.95376 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1235ca00-0e0e-3e16-8143-e6035f65b2d0 | -13.19312 | -45.29381 | 2025-08-30 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 476bb0b0-661f-3b38-a621-5854d58edf20 | -13.38543 | -47.03633 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c1b93f40-673d-3cc5-a04b-fa8d68911c26 | -12.93304 | -48.12069 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 56495c5d-8d52-3e00-b444-9b4a9c0fd9c1 | -13.66881 | -46.92615 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c6b04c5-e8c1-3e08-8407-000ac89397c5 | -13.36232 | -47.01312 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f86918b-bf97-3ecf-bebc-3fe9a9e506b4 | -13.36751 | -47.02415 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0e7337b-5285-327c-bd4f-eee0dce66eb2 | -12.92815 | -48.1109 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cee09e6e-fc53-30fe-99be-0ec364639cf9 | -10.746 | -59.82184 | 2025-08-30 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 487d2bc1-087d-30f1-8a61-85363d1bc9ee | -9.77762 | -64.2487 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826459ab-74b8-3d8d-85d3-deead8f801e4 | -10.73926 | -59.82073 | 2025-08-30 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc67f086-bb3d-363e-844e-75911672147a | -12.93802 | -48.12957 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b0ebf3b-080e-3e54-aca9-f9340f2c4c20 | -13.35364 | -54.38494 | 2025-08-30 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04760185-ed09-3aad-9290-88503f701551 | -12.9301 | -56.97425 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e030d8ad-bf3c-3b0b-92ce-42fdbcbed819 | -9.54963 | -65.69149 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fbb99bf-c013-3568-9d12-396b337051ac | -11.35283 | -63.25316 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d907b73-e4ff-3422-abfc-9377d1959c6a | -13.38755 | -46.96118 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 549ba76c-1d9a-314d-9daa-064c910dbc72 | -12.82422 | -48.09169 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e90c967-576a-34e4-ab3e-f611b28694e9 | -13.37505 | -47.01442 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2d019624-5311-39fb-a662-3175735579df | -13.38212 | -47.02942 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69eb447d-87fc-322f-9b21-d9d2f43bcba4 | -12.63036 | -57.01338 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f13f63cd-3275-36f0-9b44-9fca1a314b58 | -12.0238 | -57.08992 | 2025-08-30 05:12:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18e87a88-8fc0-38df-8dd8-be62b3df0940 | -8.847 | -70.62844 | 2025-08-30 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d2ff2db-1861-331e-b1f4-0c0dde8a8d4f | -13.10234 | -57.13094 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aa90c96-382f-3c49-88a4-e8023a88d57c | -13.37084 | -46.99475 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6661376b-e053-3fb1-8c5a-a0b4813bf788 | -12.83136 | -48.09859 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9439a833-1cf0-3a6c-a392-58681b753b16 | -11.39375 | -63.25006 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 313e5c9b-1f0f-3fe3-a5af-28ae4b47edd9 | -13.36146 | -54.38615 | 2025-08-30 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cae6a317-6c64-3df3-a680-62a60d6805b2 | -14.23629 | -48.07232 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25d9c74a-76ba-35db-9b8c-5d2443646aba | -13.38602 | -47.03116 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1194129e-14e6-3373-8e38-2f9fd4c04c3d | -12.93295 | -56.97855 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aac234e7-97f1-3c8f-8409-9a37a6793ed4 | -13.65666 | -46.91845 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d98d3d53-c015-39b6-8025-ccef1ce0d032 | -13.62641 | -48.1928 | 2025-08-30 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9849a4f-4fee-3b75-a77b-98c586fe0c35 | -14.23953 | -48.06434 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcf49943-2361-31ce-918b-cecbe8c506db | -13.61952 | -48.25291 | 2025-08-30 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43e432a9-8803-3d99-b9b3-652628342904 | -9.77691 | -64.2528 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36502a46-b24c-3004-a841-8684638339fd | -13.59452 | -46.89175 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00e23cb4-6d3d-338f-9f0f-0d0accc811e7 | -10.35574 | -64.46391 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 978f165e-6024-3d17-bae8-6822bb77aa42 | -10.74203 | -59.82499 | 2025-08-30 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93dd1fd8-0454-3844-a83d-adf1bff62eb1 | -13.38119 | -46.97785 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec13a821-d534-335b-9e81-fd02d638bd58 | -10.83891 | -61.46603 | 2025-08-30 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c15ddac0-ed12-326a-84a6-3eaf170bf105 | -9.77904 | -64.24049 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1192e076-16cc-31ee-a762-101a513fabe7 | -12.92268 | -56.97695 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f95974-fdb4-32e8-ab5e-4cdca0422a42 | -13.37847 | -47.00335 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9b4bea1-0b9b-3548-bb17-a7194b92bd7b | -9.7712 | -64.26022 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8c913f-1df4-3e49-9cc5-37953db5bd67 | -13.97879 | -46.31878 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9aaa920d-904b-3e02-a501-5c68c9d2ea5d | -9.78191 | -64.24947 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README74.md)
