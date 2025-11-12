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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04e53730-e5d1-3475-a8e4-06428c08fc08 | -20.20921 | -56.6198 | 2025-11-12 04:36:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 125fe215-cd76-35eb-a3f9-e019ec43a66e | -20.20994 | -56.61592 | 2025-11-12 04:36:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eff0acd9-23cd-3137-97d1-974faa97df35 | -19.79345 | -57.97663 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a4ffb6c3-c697-3ea4-a316-30e083ce61a2 | -19.74453 | -58.0107 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 19ca9bf5-e7be-301c-aef0-171af823c8d4 | -22.37253 | -47.05862 | 2025-11-12 04:36:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b61ca5d3-e382-3ca5-bdcf-1f822b552327 | -21.52258 | -42.27338 | 2025-11-12 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 99a027ab-9427-386d-aae2-915ce7f04150 | -23.59504 | -49.01342 | 2025-11-12 04:36:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa6fa48a-3275-3807-958b-a2e3bec948d3 | -20.21067 | -56.61205 | 2025-11-12 04:36:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bbe8da4b-8ee4-37f6-9e0d-1f937ca37421 | -21.06199 | -47.25861 | 2025-11-12 04:36:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e6ba336-f33e-3e7d-95ff-67e001817de0 | -18.08397 | -54.02691 | 2025-11-12 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22e9af1b-b5c2-3293-9b6c-27b26e23b2dc | -19.65919 | -43.68238 | 2025-11-12 04:36:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09be80d6-8e88-3c3b-8ef7-0bafe159d6d6 | -17.84093 | -49.35864 | 2025-11-12 04:36:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31691242-c32b-3d20-98ba-2ccb85f6b35a | -19.74794 | -58.00887 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ebca7e6b-7fef-35d5-a72a-8772b8ab0526 | -19.74902 | -58.01168 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3c977908-a08c-36bd-bbc8-c3182f6547fc | -21.41808 | -48.65187 | 2025-11-12 04:36:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 420f1459-dbee-3fd9-a80c-e6a51b87236a | -18.47817 | -53.4026 | 2025-11-12 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11348da5-a80b-3264-95ea-15209e52a306 | -19.92158 | -46.08553 | 2025-11-12 04:36:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ff1bda1-9680-3e5a-a4c8-d9bcd5030ccd | -21.17091 | -48.69035 | 2025-11-12 04:36:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2a5389ae-2504-361d-ab5a-d25929940b84 | -19.8524 | -58.0094 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 63aa1d72-0ce3-3164-93ff-d7ac52901aca | -22.36807 | -47.06303 | 2025-11-12 04:36:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85121bfa-aa94-328e-bc18-ff65b5699473 | -19.74608 | -58.01846 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b220fbff-c226-3601-bca3-14b86d75ed17 | -18.1557 | -54.55776 | 2025-11-12 04:36:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 168f80fe-b4d5-3f7e-9be4-f3a538e1a61d | -23.60207 | -49.01461 | 2025-11-12 04:36:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 305339ef-248d-3caa-a4d3-69c930d156ce | -21.30314 | -48.54609 | 2025-11-12 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 228cbce0-0f51-3b91-b0a5-3aedc35bd4d0 | -20.7382 | -55.70406 | 2025-11-12 04:36:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7e820c4-f6f7-366e-890b-673d0d5f0cc6 | -19.74887 | -58.00408 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b0c19956-18c8-312f-bf02-ae15bb8967b5 | -23.07337 | -52.42966 | 2025-11-12 04:36:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ccfa059-52da-3b4d-a145-589cac5e0f04 | -19.84792 | -58.00842 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 91a823a4-1f18-3d92-bd65-3254b5dc8cfa | -20.74022 | -55.7023 | 2025-11-12 04:36:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28a66b0c-34a7-387d-ba87-19d40cd245fd | -20.06007 | -50.37755 | 2025-11-12 04:36:00 | NOAA-21 | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95e7675a-c727-3bd6-9415-81002329fa06 | -18.47536 | -53.39775 | 2025-11-12 04:36:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a85e8369-4488-333c-9c65-fbfdef2c8bf4 | -20.88967 | -50.1058 | 2025-11-12 04:36:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 32a90292-6ba2-372a-b14f-7e30a5192263 | -21.17439 | -48.69094 | 2025-11-12 04:36:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 54c31f66-bece-3384-a4d2-d185a08d5787 | -17.95561 | -48.83485 | 2025-11-12 04:36:00 | NOAA-21 | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e5a8d34-0710-3138-b01f-1abca590d7f3 | -21.53955 | -48.7705 | 2025-11-12 04:36:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c6b59da-d097-3131-a767-11671676ec6c | -21.06571 | -47.25911 | 2025-11-12 04:36:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b92dd35-338e-3cfa-8cd1-99e404e44e08 | -19.84606 | -58.01797 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 72817296-17fb-31f6-8eec-87afba968209 | -18.39732 | -47.10834 | 2025-11-12 04:36:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1071d24a-2c06-3879-ae69-5317b151498b | -19.75094 | -58.00214 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ac18b1bc-8ce9-36ae-a639-0c1768c057d7 | -19.91698 | -46.09021 | 2025-11-12 04:36:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4346e67f-5a22-3881-8af4-8962ee6151df | -20.7323 | -50.17925 | 2025-11-12 04:36:00 | NOAA-21 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 703870e6-455c-3816-9b57-8fcc399562af | -21.30898 | -48.55548 | 2025-11-12 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 096e5fc8-48c0-3426-870e-e07afce059a7 | -19.27389 | -47.32963 | 2025-11-12 04:36:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f9e2f5a-a043-3e36-9d05-a401fd2814d3 | -18.0838 | -54.02882 | 2025-11-12 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8faf9424-fe7e-3f89-8587-11fd57a8dbdb | -21.33796 | -49.13718 | 2025-11-12 04:36:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 308ad5b5-e8c5-3f29-890c-d9bebd5981f3 | -19.805 | -57.98908 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 49934216-e289-330c-80d5-68b09fea8a36 | -20.89357 | -50.10261 | 2025-11-12 04:36:00 | NOAA-21 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e338c0ea-613b-369d-8cd1-f4e65605a691 | -20.05926 | -45.19124 | 2025-11-12 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3975554-7e5d-3a11-b47c-49b8d60c0f0f | -21.21091 | -46.49833 | 2025-11-12 04:36:00 | NOAA-21 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de39a65b-5a11-3661-a1c8-cd60889b72d0 | -22.53154 | -44.64307 | 2025-11-12 04:36:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae34d21d-2efd-37f7-9a19-5c1da78cd212 | -21.41458 | -48.65132 | 2025-11-12 04:36:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd907db9-cf8a-39bb-8c30-a3f3f675b6a5 | -19.90663 | -50.86233 | 2025-11-12 04:36:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36e2c66d-4d1c-3d0c-b04b-c5fd9fa640f2 | -21.30255 | -48.55024 | 2025-11-12 04:36:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b7ab781-e5a8-3a18-8dac-1ca7f8ed49b6 | -16.46251 | -58.15936 | 2025-11-12 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 25726728-0741-350f-bd5e-d9cce9e4bb8c | -20.31908 | -54.5871 | 2025-11-12 04:36:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 931edac8-0736-3045-a8a4-f94c674bfc00 | -18.29779 | -54.26534 | 2025-11-12 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebce2511-cab4-3538-9088-077abc1cab7c | -18.08149 | -48.52299 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 848eac7e-815d-3007-9d60-b6aec08d9929 | -20.78959 | -48.34684 | 2025-11-12 04:36:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fda5b63-469b-3057-9261-94a7b4784ebc | -21.17034 | -48.69444 | 2025-11-12 04:36:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d0e695f-ae79-3929-a83c-3493567d1a99 | -20.48954 | -45.92608 | 2025-11-12 04:36:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed3a959c-b6f3-3735-b61c-0dfbdcf1951a | -19.81489 | -57.98628 | 2025-11-12 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8e6a8aa2-b084-3b15-9983-9842b02b43ca | -24.03576 | -48.95567 | 2025-11-12 04:38:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 353ec309-d925-34c0-a4d8-440ac8b303fb | -28.14538 | -49.49267 | 2025-11-12 04:38:00 | NOAA-21 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 773f344d-5737-3dfd-9c75-c6ea2c26531a | -27.10481 | -50.82677 | 2025-11-12 04:38:00 | NOAA-21 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 019bb8cd-cd46-36ed-a920-bdbe66918eb5 | -29.14747 | -55.00491 | 2025-11-12 04:38:00 | NOAA-21 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| d8ddf6f5-1d60-3933-acca-73cf2040d298 | -25.18588 | -50.10694 | 2025-11-12 04:38:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f4731b2c-363c-3b99-ba46-8e662330c334 | -24.529 | -48.10864 | 2025-11-12 04:38:00 | NOAA-21 | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d442faf3-133b-32e2-97fb-bb33207d1f9f | -28.14273 | -49.49411 | 2025-11-12 04:38:00 | NOAA-21 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0410e005-2563-3810-8a37-77714240115f | -26.45661 | -50.66119 | 2025-11-12 04:38:00 | NOAA-21 | CANOINHAS | SANTA CATARINA | Brasil | 4203808 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f89de6e-9736-3cc0-902d-08029bb974c0 | -25.33049 | -51.48183 | 2025-11-12 04:38:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e8dc5b5d-4e83-3383-99d5-f3b130f44e17 | -24.98549 | -51.53848 | 2025-11-12 04:38:00 | NOAA-21 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a72430f7-1ed6-3ebd-be5d-afc3851326fd | -27.83048 | -50.30461 | 2025-11-12 04:38:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a95881f-36d6-388a-bcc2-efb98cb10f4c | -28.3987 | -49.03547 | 2025-11-12 04:38:00 | NOAA-21 | GRAVATAL | SANTA CATARINA | Brasil | 4206207 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9753a0d8-7da3-39bd-a50b-879bfb32ea77 | -27.44937 | -48.44558 | 2025-11-12 04:38:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81bfc5b0-5402-3fdb-b7fa-779a514bb1d2 | -24.03634 | -48.95133 | 2025-11-12 04:38:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52470935-5fbc-3685-8916-b5cc28c2ad21 | -30.4578 | -56.38431 | 2025-11-12 04:38:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 59848fb9-0b8b-37d0-a196-3f96a97fdaef | -25.17403 | -49.96645 | 2025-11-12 04:38:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2889eb94-02d5-3df5-9388-05d7edaa13e0 | -4.0976 | -48.0144 | 2025-11-12 04:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 40bce384-5f9d-3325-b020-96f05f7b5336 | -4.1161 | -48.0136 | 2025-11-12 04:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 5eb3fc95-f905-3b98-8198-0196aa24a4d7 | -4.9456 | -43.7194 | 2025-11-12 05:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| bcdd84df-0aa4-3a47-b330-24d1f849a933 | -4.9641 | -43.7413 | 2025-11-12 05:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 744660d1-03f5-3bb8-8f25-c420b710f44d | -4.9454 | -43.7425 | 2025-11-12 05:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 488bf0d1-5a85-38c7-a646-21e581688269 | -4.0974 | -48.0361 | 2025-11-12 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7eeeb4e1-b690-35b6-bf99-0bce0cc6ebc1 | -4.0976 | -48.0144 | 2025-11-12 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 7842972d-af35-371d-8269-5c5687981071 | -4.9643 | -43.7182 | 2025-11-12 05:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| f984f806-4537-31e1-9819-83f8d82fe959 | -4.7666 | -42.6808 | 2025-11-12 05:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 471943b2-e5a3-3d38-9cf6-27a0881f49b6 | -4.1161 | -48.0136 | 2025-11-12 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 058dc4bb-f60c-30d8-86cc-d25fb6a9eba4 | -4.7668 | -42.6572 | 2025-11-12 05:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| 685ec442-4644-3f58-a0a2-d51edec61bff | -4.0976 | -48.0144 | 2025-11-12 05:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0df6bbd0-2200-3f40-9bdd-e638d7d8c93e | -4.0974 | -48.0361 | 2025-11-12 05:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d60605cc-49c2-322e-960c-e37dd3c31b5d | -4.4538 | -44.5763 | 2025-11-12 05:20:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6fea49ac-1101-3475-98c4-59a25ff8e7e6 | -4.1161 | -48.0136 | 2025-11-12 05:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f4dae504-f07a-310f-9bdb-29bc86006099 | -4.0976 | -48.0144 | 2025-11-12 05:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| df0590ca-18dc-3bf2-932d-daa90fa4cfda | -4.454 | -44.5534 | 2025-11-12 05:20:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 165.6 |
| c733f8b4-39db-3210-8875-ae4f86bc2168 | 1.83326 | -60.84188 | 2025-11-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01c42b7f-ab9a-344f-a7a9-0aea44f9ae17 | 1.83266 | -60.83812 | 2025-11-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37971636-4681-3561-a4fc-ddaad3d2b543 | 3.97708 | -59.77508 | 2025-11-12 05:20:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70910434-dbe3-32c1-8a2d-1251aae3afc1 | 1.83611 | -60.83759 | 2025-11-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c085097-fc4c-3305-b2e0-e9cb18559250 | -2.63036 | -49.20179 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffc18cab-a69d-3829-877c-3eb2facd56ec | -2.7976 | -52.97517 | 2025-11-12 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README18.md)
