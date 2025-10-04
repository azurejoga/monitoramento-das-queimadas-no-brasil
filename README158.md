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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 927948de-8e07-38f0-b0f6-16a0f8d7295d | -8.7777 | -49.9123 | 2025-10-04 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| b3f5cf4c-692f-3978-97cb-d6e88bad4b01 | -11.4725 | -51.5157 | 2025-10-04 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d5771e61-d8b9-31d5-8220-6e80b489a468 | -5.818 | -42.4861 | 2025-10-04 14:40:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 225.9 |
| 254e0569-bbcc-3f54-9aa2-e84085c5f746 | -5.6843 | -42.7328 | 2025-10-04 14:40:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 701752f4-1c55-3193-ba78-f961d95c8920 | -12.9294 | -54.7333 | 2025-10-04 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 842549a6-a74d-3142-90ef-4d88e1e00a1d | -13.3225 | -48.1216 | 2025-10-04 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 26b93bbb-bc51-3173-8b1e-092846b301ed | -13.1329 | -47.9713 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| bc185a0b-487e-3519-a4e9-8fb5dd22c84a | -13.0968 | -47.8429 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e783f31e-f14e-352d-bf73-92ceea88be85 | -13.1784 | -50.8905 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 172.3 |
| dab6d36a-820f-3d07-84ff-2d74d9e9ac41 | -12.3162 | -45.3545 | 2025-10-04 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 325521a7-b3a4-3635-8a7c-ebb18d325382 | -16.3627 | -51.4752 | 2025-10-04 14:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 6e251e7e-e814-36db-b898-dcc88b0eacaf | -7.7746 | -42.5865 | 2025-10-04 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 1e2d0ec6-366c-3048-a234-389ee8907a10 | -5.8634 | -45.7308 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 987223dc-3cfe-374d-88a7-0eb09608d742 | -6.7167 | -42.8101 | 2025-10-04 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 6db785af-e151-3068-aabd-31886b0a0372 | -13.1164 | -47.8178 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0b5ba329-da6a-3f95-bca9-086bb9b1b0ca | -5.7698 | -45.7598 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 442ed6c7-9ece-3071-b8f9-256a6f0dcf35 | -11.8442 | -44.9408 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 287.8 |
| 541f828f-2ad3-3b0f-bec0-f77b1b333f55 | -7.8593 | -48.2037 | 2025-10-04 14:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 685c515d-e857-3383-ab09-ef0c5417d7e9 | -11.7924 | -46.8184 | 2025-10-04 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6efad75c-af44-316d-8e4e-92ed07ede05a | -6.0836 | -46.185 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 80eaa429-02e1-3674-8519-3d523ab27db6 | -5.8764 | -44.2764 | 2025-10-04 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 48916108-a47a-3fe1-8b2d-ad277e567e04 | -7.7933 | -44.1304 | 2025-10-04 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| d2d1af3a-ebbe-379f-a93f-d5f281d72ab5 | -9.1901 | -49.9604 | 2025-10-04 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 168.4 |
| b8d1143c-1096-390e-aed6-a412f868e1f6 | -10.6531 | -49.1449 | 2025-10-04 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 4709c307-9b73-392b-8026-1541628764a5 | -9.1713 | -49.9622 | 2025-10-04 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 77367808-6760-37db-8fd4-f1e88f562d8c | -15.3797 | -47.952 | 2025-10-04 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 144b3bb2-913b-39e4-aa65-356102c1b79b | -5.6658 | -42.7106 | 2025-10-04 14:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| bfb3ddd7-adca-38e9-b5e1-1974c05afa1b | 1.5286 | -55.8257 | 2025-10-04 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8fab732f-6db8-380c-9dd8-38d42080287e | -11.2024 | -54.8567 | 2025-10-04 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 0fba8d7f-90c5-3196-b636-8dfa3544f4da | -13.3233 | -48.077 | 2025-10-04 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 135.8 |
| e7a28a4c-2918-30cb-869d-f15b90db6008 | -5.7696 | -45.7822 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1084274f-47dd-3374-ba7a-6c9c023dd1ed | -14.9881 | -49.9892 | 2025-10-04 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 6b31ee70-a0fa-34aa-a278-084d80b3d028 | -12.9279 | -50.9862 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| aee09589-2ca7-3bfb-9826-5d1f48f8f3c2 | -6.1728 | -44.6203 | 2025-10-04 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 1742bdd9-4a3f-3cb4-a039-693c606cbb02 | -6.7213 | -45.9799 | 2025-10-04 14:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6be351cb-180b-30be-a25d-f0c0cf50f62f | -9.3196 | -45.7515 | 2025-10-04 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 7377a6b3-b3fd-3671-9508-ea177ce94249 | -11.5054 | -43.5426 | 2025-10-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| ad46254b-eedd-3206-9afe-dc0e48061ba1 | -13.2938 | -47.5905 | 2025-10-04 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 45986442-6a69-35a7-980a-b2d55ce0c6ce | -13.3229 | -48.0993 | 2025-10-04 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7042436b-31fa-3b76-a6ee-224c0e27d383 | -5.3228 | -43.3454 | 2025-10-04 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| ea0c3c4a-2443-330b-940e-c95dfcc60a4f | -9.3193 | -45.7741 | 2025-10-04 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3e249556-f1fe-33e2-a3b8-6609e407b557 | -9.9035 | -45.9553 | 2025-10-04 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5f71fbb2-b562-34be-8aee-5f226b7c852e | -10.759 | -49.6951 | 2025-10-04 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 16274a4a-8d5b-301a-bdb6-0695f30b1439 | -9.9225 | -45.9531 | 2025-10-04 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 59a544e9-4cb8-3bd0-abed-f0f8f02f9999 | -5.8474 | -43.3529 | 2025-10-04 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 2b72ff12-e5d9-34b7-93e3-e76b52abbe11 | -11.863 | -44.9612 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 4b6013b5-e0b4-3b95-a8fa-fbcb14f36e14 | -10.5838 | -48.696 | 2025-10-04 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 82820d38-7436-3638-92b9-0b1ede6043f2 | -10.6342 | -49.147 | 2025-10-04 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 20c8687c-a562-3928-a477-5a3ac595ffb7 | -13.2892 | -47.837 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 460d1194-a715-35fe-ad52-5db2e2f0042d | -14.3904 | -45.9369 | 2025-10-04 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| a5a0df93-311c-3ffe-9c92-11c78928ae88 | -5.8284 | -43.3777 | 2025-10-04 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 3996935b-c417-3208-a39f-7cf0cbba676f | -8.8537 | -46.7228 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.7 |
| ed6bca63-cc42-31c2-b1aa-d813860602a4 | -9.6293 | -54.3158 | 2025-10-04 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0efd015c-7553-3917-a22d-df23f95c02ef | -14.8271 | -54.7719 | 2025-10-04 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e0518212-9c43-3d23-a669-1dc9166f5e8d | -8.854 | -46.7005 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4a752f46-0ae8-3655-985b-de57426ec2fa | -5.7762 | -42.9372 | 2025-10-04 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 69da86cb-519c-3eca-abe2-4ef57568dc34 | -11.6318 | -45.0415 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a38ba5b6-c601-3c7f-8ed6-5e0e26db47e4 | -8.6322 | -54.9949 | 2025-10-04 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 5ac3564a-5920-3cad-8ed7-23d68d8b62a8 | -11.1268 | -47.9077 | 2025-10-04 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e78af315-5718-333b-8fed-5191c58b568a | -11.792 | -46.8409 | 2025-10-04 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2b197d61-37f5-370f-ab3e-6ba7f462c5c3 | -7.0604 | -45.7946 | 2025-10-04 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 560.0 |
| 6fdfb721-8da4-3401-b1ff-0898c2802038 | -5.9584 | -43.5072 | 2025-10-04 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a2ff9652-1a89-3697-a146-ed8f1db6def6 | -5.8739 | -42.5289 | 2025-10-04 14:40:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| ddfd50c3-0f3f-3aff-bc39-58f4d5213ba5 | -8.8526 | -46.812 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 86f01c81-ee7c-3e6f-abad-7f55d175af64 | -11.8438 | -44.964 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 00e7a321-06b4-33b0-807b-00b5cf0d2c46 | -14.8464 | -54.7696 | 2025-10-04 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4434dc94-235e-30d6-8cc0-d55186e632e5 | -5.8258 | -45.7559 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| cfd2ff8b-d20e-3bfd-be9a-0a693450b604 | -6.5044 | -45.1859 | 2025-10-04 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ff6554ed-f36c-37f1-b8fd-3d7cb7e882af | -13.1582 | -50.9574 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 72a558dd-e31e-3d0b-b758-9468dd4ffd9c | -8.5458 | -47.264 | 2025-10-04 14:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0360af6b-f182-34b0-944e-db65ff41b573 | -13.6717 | -51.234 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 947f56ba-7389-3c3a-be3e-68744462814d | -6.0649 | -46.1864 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 55d8cb48-cc14-374c-8878-5dec2fab73e8 | -8.1891 | -44.1357 | 2025-10-04 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 7e35fb4c-ad53-3e87-b0a1-65871e9d282f | -9.1716 | -49.9408 | 2025-10-04 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ce3817f1-8f40-3902-b587-3822cc246fa3 | -11.6845 | -45.3103 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b5ae3f17-c77f-3933-9360-e21020d8df43 | -13.996 | -48.1987 | 2025-10-04 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 24124a32-b9b2-3f65-b1e6-2dcf850cbbaa | -6.1542 | -44.5989 | 2025-10-04 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c11fbdf6-016c-3238-964b-bb0ff6153d2e | -13.3426 | -48.0742 | 2025-10-04 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9752cd23-1383-3249-bccc-c16dbac4b29d | -7.7941 | -42.5369 | 2025-10-04 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| 86dcc421-0784-3388-82c3-2acc88db4baa | -14.672 | -48.2933 | 2025-10-04 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a9dc2168-8b74-3e35-97be-3b7cae6ee92a | -12.9468 | -51.0053 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 942af401-f194-3374-9240-563b753351b9 | -7.7489 | -46.3168 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 45aebceb-278b-3f1e-9e3c-a2ef869d6f83 | -13.1333 | -47.949 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| de538540-1bae-32e8-8969-4571bc733d65 | -15.5211 | -46.838 | 2025-10-04 14:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 6351562a-5fa9-3ac2-bf13-eae733e8e2d1 | 1.7667 | -55.8228 | 2025-10-04 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0b9e86bc-ce8d-398c-8b5a-f1d9f1a5cdfe | -5.4742 | -43.1711 | 2025-10-04 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 09f08617-8930-37e2-b07d-1147e5f278c4 | -13.3032 | -48.1244 | 2025-10-04 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 176441b6-df7c-347b-b443-3a01f66a347d | -3.4542 | -43.3386 | 2025-10-04 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| de6a8c83-7f89-3058-92a9-6a073e9480fa | -14.8268 | -54.7926 | 2025-10-04 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 61d404be-7390-3a1d-b856-fdd045826470 | -12.0895 | -45.1583 | 2025-10-04 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 5e140fe2-cf3b-3b37-ab3e-92a84f9fe720 | -11.6314 | -45.0646 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 0e7023bd-4f03-3ec0-b1ac-0c6fba0069e9 | -5.8071 | -45.7572 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| c9f0cc01-b129-3c89-8fbe-645f277bf5d2 | -6.0618 | -42.5133 | 2025-10-04 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 180.3 |
| e5f69f56-fc58-3958-ba95-04c321ad0f82 | -6.6069 | -44.3098 | 2025-10-04 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 84fe9157-e500-3c56-8e68-954ddcb977a8 | -6.7626 | -45.5944 | 2025-10-04 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d7bde463-fe85-3c16-b9f3-ab6b6b62be3f | -15.3601 | -47.9554 | 2025-10-04 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a45c33b8-ede6-3ca6-bbf1-8349fe04444a | -8.8529 | -46.7897 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |


