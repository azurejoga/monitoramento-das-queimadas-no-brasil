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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 417f2c81-f4d3-369b-b277-9108895c5d0c | -7.48977 | -45.57241 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01b69f6f-d8af-3843-b5ce-7a37c4c7cff1 | -11.13323 | -46.57978 | 2026-01-10 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7765c4f7-cb49-3492-9424-9c25f3338668 | -7.32469 | -34.9073 | 2026-01-10 03:38:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f13c6d19-3141-3542-8b5a-19431b041995 | -8.6921 | -40.76207 | 2026-01-10 03:38:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 77b66f94-1e35-332a-8cee-0b788ad6c804 | -7.49322 | -45.58842 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8764a8ac-99af-3608-84be-d0dade3e69c6 | -12.12276 | -40.46009 | 2026-01-10 03:38:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cbe2d71-6031-33ab-922b-da1ae8db5b8f | -7.7494 | -35.24853 | 2026-01-10 03:38:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b5b793b1-b9a8-331d-973f-6926810e28b0 | -10.66121 | -38.37428 | 2026-01-10 03:38:00 | NOAA-20 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5a4a9f5d-39b3-374e-a82b-ee4ac45be5c9 | -10.65872 | -38.37547 | 2026-01-10 03:38:00 | NOAA-20 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dba800bc-a1a2-367d-911f-9b8c4621d6f5 | -10.4861 | -44.93422 | 2026-01-10 03:38:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 818340a8-148c-3319-a5c5-a95c3c510138 | -9.8517 | -41.59479 | 2026-01-10 03:38:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f099e4b-fbae-374f-9b8f-21f88ae8ebff | -7.42239 | -35.18868 | 2026-01-10 03:38:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eab25ce0-9f2f-381b-b503-355237ec7769 | -9.6874 | -37.10322 | 2026-01-10 03:38:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3d50eb23-8598-3715-981e-30b7e08df83d | -11.1322 | -46.58491 | 2026-01-10 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 360db159-ea68-31ad-b763-d747453b3ed4 | -7.48703 | -45.58719 | 2026-01-10 03:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6f7e07a-0b21-387b-a8fd-00498a8962ca | -8.2536 | -37.48814 | 2026-01-10 03:38:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fb5cbce5-2509-3c5b-b7f6-d5a289fe9965 | -12.3754 | -58.0521 | 2026-01-10 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 433a3eab-c6b9-3cde-b710-5afe081f3235 | -12.3943 | -58.0506 | 2026-01-10 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 867ca6b2-1f5e-35d1-8a61-95604a12b6e3 | -12.4133 | -58.049 | 2026-01-10 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 39f914ed-50f0-312a-b893-67599994e5f6 | -12.4135 | -58.0292 | 2026-01-10 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 5f0a492b-8090-3fb4-9f12-0f3a307a841f | -12.3946 | -58.0307 | 2026-01-10 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 234.2 |
| bf1aace9-922b-3025-8d6f-8ebe5ba71622 | -12.3756 | -58.0322 | 2026-01-10 03:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5f26d9f1-0308-3800-a92e-519d1b09b833 | -20.22209 | -46.48885 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2662ae4-0b80-3fa3-96f4-60a0343344d4 | -13.78653 | -43.24026 | 2026-01-10 03:40:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 011489af-9846-375e-8179-e19977119251 | -20.22226 | -46.4878 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeb0ce5b-0932-39d4-8158-b080fd7681e7 | -20.13831 | -46.85853 | 2026-01-10 03:40:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b05c0d42-f76c-397f-a8d0-4894ce582f1f | -14.97497 | -43.42739 | 2026-01-10 03:40:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c9faf1b-ce56-3e86-a544-3da1f6a30583 | -20.14056 | -46.81047 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1505427-922a-38a6-a090-410708ddc8c7 | -13.78077 | -43.24458 | 2026-01-10 03:40:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b77b327-95d2-36d6-b5e5-3243b4e67be3 | -20.13774 | -46.8088 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 639122eb-7008-3102-a8c0-7e403a305bf8 | -20.22285 | -46.48535 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e431202b-4308-3147-b64b-ed0a229ef574 | -20.13697 | -46.81239 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01dd2b2c-0032-344d-ba1c-5b3c716f9d84 | -20.13907 | -46.85495 | 2026-01-10 03:40:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 87fcbf0e-c642-355c-af6a-c1a31a4c255c | -14.97622 | -43.42471 | 2026-01-10 03:40:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e193eea-612c-338c-953f-91e0dfba6fa5 | -14.97145 | -43.42398 | 2026-01-10 03:40:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee58fc45-eabb-30ae-a45a-72d36f524e34 | -20.13978 | -46.81403 | 2026-01-10 03:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb706f77-8b78-3e2f-856e-fef49d6d7d51 | -21.04181 | -49.594 | 2026-01-10 03:42:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| def3efdd-557c-3a51-b5bb-3e58d9c7f7ff | -22.82296 | -49.3 | 2026-01-10 03:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0df2814-0816-381f-ac0a-387108121c2c | -21.04643 | -49.59592 | 2026-01-10 03:42:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 345e1fa0-b0d6-33b4-9388-2d88e970e8ae | -23.58119 | -47.03415 | 2026-01-10 03:42:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bcda93aa-a0be-373d-b26e-fd64fc5f8269 | -20.70651 | -47.28783 | 2026-01-10 03:42:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 932dc4b7-b0ef-362f-b45c-e25e113478a8 | -22.81927 | -49.2894 | 2026-01-10 03:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c50e3f37-40b4-385b-b458-1c71cf6fb07a | -22.81718 | -49.29831 | 2026-01-10 03:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8adf5537-70b2-3ee8-a077-af913a9cdaf2 | -21.04033 | -49.59425 | 2026-01-10 03:42:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f6488c63-e18f-3633-adb7-40217e3dca24 | -22.82396 | -49.29573 | 2026-01-10 03:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca4f97cc-f749-3bbb-b8a9-616d7a590ea7 | -22.8182 | -49.29395 | 2026-01-10 03:42:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 59bca952-fe6d-309c-a10f-47bdbf4f4d7e | -20.70555 | -47.28735 | 2026-01-10 03:42:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7739555c-9023-3374-82e0-ebbe73d8fa2f | -12.3756 | -58.0322 | 2026-01-10 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 20addd83-a4e3-3643-a518-50906e986925 | -12.3943 | -58.0506 | 2026-01-10 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 6f623fa8-ee9e-35d2-9689-b477c92b2abf | -12.4135 | -58.0292 | 2026-01-10 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ab6b996e-67d8-3bba-b206-01236d97aa2c | -12.4133 | -58.049 | 2026-01-10 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 27de94fb-03f7-3c4a-8f27-5b467858c438 | -12.3754 | -58.0521 | 2026-01-10 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a7834ac9-1789-369a-973c-d5c910ec9092 | -12.3946 | -58.0307 | 2026-01-10 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 213.2 |
| e07efdda-e5ee-3f80-ba1c-62107bf98fd6 | -15.2574 | -59.8521 | 2026-01-10 03:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f16743c5-7b33-354b-8764-f71dbd34d2c1 | -12.4133 | -58.049 | 2026-01-10 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d07cd925-7fe2-3025-a641-0d2bb586a80d | -12.3946 | -58.0307 | 2026-01-10 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 0ea3d981-6e80-3e5f-bc7c-51380c48640c | -12.4135 | -58.0292 | 2026-01-10 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f628c2ad-9f69-3114-8727-795688c8aff4 | -12.3943 | -58.0506 | 2026-01-10 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 03595604-4738-362c-8415-c80b6de00e7d | -12.3756 | -58.0322 | 2026-01-10 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1e14d8ed-fedb-36b4-8ac7-0a4213ea0912 | -12.3754 | -58.0521 | 2026-01-10 04:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4de0994c-564b-3a14-94c2-524b6451428b | -15.2574 | -59.8521 | 2026-01-10 04:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1bfb4656-9125-3345-85af-d8c48a8e4b2a | -12.3754 | -58.0521 | 2026-01-10 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 6ead2995-d125-34ea-a70a-9ebfac893d07 | -12.3756 | -58.0322 | 2026-01-10 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 18b29e85-55f5-34b5-ac05-ea6e74d18d42 | -12.3943 | -58.0506 | 2026-01-10 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 9e582b22-3b4f-3264-987d-43f22362e54c | -12.4133 | -58.049 | 2026-01-10 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c753bab0-6892-3249-b3f7-ca68db3780ce | -12.4135 | -58.0292 | 2026-01-10 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e2defdd5-a2c8-3595-bff1-c7175d7409ca | -12.3946 | -58.0307 | 2026-01-10 04:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 5b5e15cb-1ddb-371a-8e8c-6d9cdf9c353d | -12.4135 | -58.0292 | 2026-01-10 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| da0d082d-6115-36b9-b8e7-5ccbe8f3cc47 | -12.3943 | -58.0506 | 2026-01-10 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 5c3febc9-d9d6-306d-b519-6ce20144bdf7 | -12.3754 | -58.0521 | 2026-01-10 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1e255db3-e11f-3da7-8205-d45a664efb47 | -12.4133 | -58.049 | 2026-01-10 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| cb6a3336-50a2-328c-9cef-016ca076a32e | -12.3756 | -58.0322 | 2026-01-10 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c56e49fa-f0a4-35f2-a311-c2afb3ca56db | -12.3946 | -58.0307 | 2026-01-10 04:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 02504059-cc84-368b-9791-cb501bd6ad34 | -2.58122 | -54.7274 | 2026-01-10 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecb8e8d0-4232-3ab9-8e40-0ea9034c51c6 | -5.47837 | -39.65297 | 2026-01-10 04:25:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| add4fbf7-7caf-3a5c-a6ad-07754fde46c5 | -3.78541 | -40.97167 | 2026-01-10 04:25:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f1a59b4-c3cd-3d28-92d9-83122a7f3557 | -2.90114 | -49.37928 | 2026-01-10 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 258563f1-16a2-33c9-baff-faf1f5479db8 | -6.06255 | -43.25299 | 2026-01-10 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eeb75a99-4162-391a-95b3-5a0d46348060 | -3.60579 | -41.59304 | 2026-01-10 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e545c87b-b4ba-3cdc-baee-bd0432382ab7 | -1.70393 | -45.81216 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 898d0cb5-2eb1-3885-a343-7fc3136da072 | -2.14543 | -54.39347 | 2026-01-10 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05149f2c-233c-38a3-b6bf-6c3ca0859be1 | -3.64441 | -42.02259 | 2026-01-10 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 068ccf47-e09f-31ea-b8d8-c9bf406a38f7 | -3.57329 | -43.40505 | 2026-01-10 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dab56cbe-f16f-313c-8065-539ddf743dab | -3.49657 | -43.31171 | 2026-01-10 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd3f0668-67ad-3e2a-98c7-2523096fbe68 | -0.08988 | -51.28244 | 2026-01-10 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5a7cbfa8-8c4e-370a-85a1-1fa2d77ad2a0 | -2.86954 | -45.23582 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3a06535-6794-3d83-9125-79a11c201ebf | -2.88875 | -45.22117 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43817254-067a-3b88-981e-ab6f2be4972d | -2.14587 | -54.39265 | 2026-01-10 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f2432e6-c7d4-3247-b9aa-15af3bba89e2 | -2.2485 | -46.4161 | 2026-01-10 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae1dd4df-0690-3472-acaf-9959db4b4343 | -2.88437 | -45.22755 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0001f86e-5749-3f4a-87d7-c730099d9b35 | -0.74512 | -47.86316 | 2026-01-10 04:25:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ae9c173-3a9c-3562-abeb-0da9759bc3fe | -6.66525 | -39.64991 | 2026-01-10 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ef2034e9-9906-3850-a6a7-2f7ca3410b58 | -4.33957 | -44.12912 | 2026-01-10 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6670641-84af-3827-90c4-7a7c17918dd2 | -2.86946 | -45.21467 | 2026-01-10 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7a0fcc3-e03d-3347-a316-40afdb9dd217 | -3.70973 | -45.38901 | 2026-01-10 04:25:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31b003b4-bfd3-3627-9781-e1f059183752 | -3.08094 | -44.88283 | 2026-01-10 04:25:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3f64dd2-8d5a-3cc8-95b4-a6063af5db82 | -4.21812 | -46.44205 | 2026-01-10 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eeb10952-4409-3cab-a3f4-e41af67d2b2d | -0.11738 | -51.45424 | 2026-01-10 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 304cb16f-7a9b-3331-9c63-98dc581f882b | -1.57196 | -46.84682 | 2026-01-10 04:25:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4b5d932-e1e8-3844-833f-d1d8ced2eef8 | -3.25397 | -41.83738 | 2026-01-10 04:25:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README6.md)
