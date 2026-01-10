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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1311c06b-c492-3327-a5d4-405d8d028c0c | -20.26943 | -46.41972 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8c374b8-286f-3066-8b50-628bd9d59681 | -20.2247 | -46.48386 | 2026-01-10 04:59:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b088cfcc-a725-3b27-a126-e94620cccc16 | -16.10307 | -56.7543 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 576ea78e-064f-39ae-a8a7-4ad57f7075ba | -16.10712 | -56.75111 | 2026-01-10 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9294b6d-97d6-3950-9c3f-add1cfef1641 | -16.44197 | -58.16425 | 2026-01-10 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| cd95f593-ca31-321a-bf0e-41e47a4224e9 | -14.19808 | -57.25163 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 481c5979-381e-3ecb-badc-9f61b237852e | -15.26 | -59.86003 | 2026-01-10 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f7b1886-9eea-311e-b59e-e31e19ae9b30 | -18.52144 | -55.10564 | 2026-01-10 04:59:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cf43917c-10a0-3b21-aabc-406a06677a7d | -14.18818 | -57.24561 | 2026-01-10 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6373a581-fc5e-39ef-9bde-9e1418401c40 | -15.26464 | -59.85723 | 2026-01-10 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19c8078b-5a68-3bfe-a6d3-86fa2271863c | -15.26206 | -59.87155 | 2026-01-10 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03cbf032-6d95-3bcf-ab21-4c4ef12116fc | -12.4133 | -58.049 | 2026-01-10 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| cc3a054a-a040-324a-91f7-e26ffcc09f6d | -12.3943 | -58.0506 | 2026-01-10 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5134cfe1-aedc-31c0-949e-8aff6a985a00 | -12.4135 | -58.0292 | 2026-01-10 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f12d44bd-da97-3829-bd27-a9ea8c7e7131 | -7.4943 | -45.576 | 2026-01-10 05:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| a93aacd1-41ff-34e2-87c3-a9204b66c986 | -12.3756 | -58.0322 | 2026-01-10 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 429d3a96-49a2-39fc-bc16-a7f8161d7aa1 | -12.3946 | -58.0307 | 2026-01-10 05:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 0eebf34e-e5e8-38ec-85d3-c3df988f3fa1 | -22.82552 | -49.29147 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42b2f59a-8954-398f-816a-da2790a3680c | -24.85383 | -49.23212 | 2026-01-10 05:01:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b20de654-dfd4-35bf-b703-be8a7ef1165d | -22.82652 | -49.29408 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e7c1795-0709-3ece-8803-91c7549191ac | -19.79262 | -57.37951 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bf9a0825-90d4-3f2e-a899-477cc5f109ea | -19.79601 | -57.38013 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 19fadac8-254a-325c-bbef-288650492f90 | -22.82497 | -49.29655 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e7ac6f-73f7-349a-8b59-a2d652845cfe | -22.82091 | -49.29095 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0efaaf00-9eab-3430-9a92-d3719480964d | -22.82248 | -49.28856 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38f8648e-e2ac-3d8e-8a91-6038c26a9990 | -22.82191 | -49.29354 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83526359-278d-3ab3-89c2-aee8362b7d87 | -24.85446 | -49.23303 | 2026-01-10 05:01:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 837c0f7b-ce13-3efc-9caa-308925f653ac | -19.79326 | -57.37568 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bd006d6c-8c1d-3c47-899d-540fb9a85c8f | -20.54636 | -57.95054 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bcb7e7b5-a89c-3179-bb36-d6c08428eba7 | -19.79537 | -57.38395 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c04d9e63-81ff-3d9e-9194-48ca2bb5026f | -20.54979 | -57.9512 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 62030d23-a3b2-3c99-9c60-c67d87487991 | -22.97646 | -48.64724 | 2026-01-10 05:01:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 337a498d-79ef-3e5b-bf8c-9dbc0bd94556 | -21.04081 | -49.5897 | 2026-01-10 05:01:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f6634b2-b450-3362-b91f-4b07b02e72e8 | -20.5457 | -57.95447 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c0fc4b47-6d5e-3b9d-b65b-cf8fd2dceb7b | -20.63901 | -49.71349 | 2026-01-10 05:01:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a89ee6a-0df7-3e83-96aa-3aba0e8d77f8 | -21.04521 | -49.59033 | 2026-01-10 05:01:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bf29cb75-8ce1-3891-b69d-e3e098e8a4af | -19.79665 | -57.37632 | 2026-01-10 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0d65d76e-23a7-3a1e-a894-061a8b79ca67 | -21.23306 | -56.25088 | 2026-01-10 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 862a6e23-e7a2-3225-b40a-c6e99900f6a7 | -22.82145 | -49.28594 | 2026-01-10 05:01:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b455138-7da8-3643-9199-5a0f256e32d4 | -21.04469 | -49.59468 | 2026-01-10 05:01:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cb82f00a-4509-36b3-be13-e558b8d8d987 | -21.53142 | -47.14456 | 2026-01-10 05:01:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c53de0ce-a84b-3930-9c15-2dae87aa10b9 | -12.4135 | -58.0292 | 2026-01-10 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3b5c536c-a11a-3dba-814e-69c7ea6c66f3 | -12.3946 | -58.0307 | 2026-01-10 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 148.6 |
| dc4dcff5-181e-37b3-b656-98654229d0bb | -12.3756 | -58.0322 | 2026-01-10 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| ef7d48d5-3f36-360f-bd85-47ea84ef347e | -12.3943 | -58.0506 | 2026-01-10 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 418b0eb0-e10e-3df4-ba2e-cc333315474e | -12.4133 | -58.049 | 2026-01-10 05:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 883b9798-d28b-3fa0-ac88-5fd677b1d5d2 | 2.10417 | -55.76764 | 2026-01-10 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe53edef-b0d7-38c5-9f54-582c2ba7e801 | 3.15186 | -60.69682 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cd04576-5e62-3792-b9ef-36267bc260fb | -1.64439 | -53.95855 | 2026-01-10 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532fa2d6-2cdf-3825-a42b-d63d5f190b0a | -0.14278 | -60.73845 | 2026-01-10 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96afea2e-863a-3682-8bb6-9ec351bee2b5 | -0.39036 | -51.66596 | 2026-01-10 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae5d5ca8-7856-3eed-8916-eb1c038f602b | 3.31814 | -60.79003 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00f6998c-5005-31d2-b21a-d78a5dd8b094 | 4.35945 | -60.38718 | 2026-01-10 05:16:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07b81fe4-a06e-34a5-8d3f-58d59fad67c1 | 3.14926 | -60.69479 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a2038af-5cca-31a9-b963-bd85a5c6c314 | -0.08633 | -51.27698 | 2026-01-10 05:16:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eff1bfd-99d1-34e0-9072-8662cf607504 | -0.11739 | -51.45276 | 2026-01-10 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06d737b2-33e1-3d02-9612-5e0e15ad96ea | -1.70151 | -45.81666 | 2026-01-10 05:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 247c826e-dbe5-3b3b-8592-acc961341cb6 | 4.35574 | -60.3878 | 2026-01-10 05:16:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 313e4fd4-7676-3dea-b26c-e7b8ca731092 | 3.31883 | -60.79454 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adeef2ca-a226-340d-b3e8-45705f5bba31 | 0.649 | -60.32112 | 2026-01-10 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62415a72-c001-3da3-9aeb-5d12c65c4884 | -1.51113 | -55.58175 | 2026-01-10 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 965a7a66-3c2c-37bb-8cc1-18f21b85fcbb | 4.05562 | -60.23417 | 2026-01-10 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f303933-a18b-324b-b889-f9d28e44ad97 | 3.14994 | -60.6993 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 969f86f8-e5fb-3fef-bbfa-1b1bae263ede | -1.60082 | -53.99166 | 2026-01-10 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ae475ed9-677c-32b1-a643-f1eeab7343c7 | -1.70232 | -45.81127 | 2026-01-10 05:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecd47ed3-90b9-38e9-9517-723f9a1295b3 | 3.31745 | -60.78551 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d29bcf7-918b-3c5b-b650-2d2d40bae258 | -1.70886 | -45.81216 | 2026-01-10 05:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c9751be-5d94-3361-85a4-e7e8f8eb6e1c | -1.6875 | -53.19147 | 2026-01-10 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cb7f2a2-18c5-31ff-9c22-c39f8dbda2f3 | -2.57942 | -54.7275 | 2026-01-10 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aee36c51-6aad-351c-8a97-c1060cf7c165 | 3.14814 | -60.69745 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb9390b-792b-3b1a-abfc-5431d2296184 | 3.92414 | -60.27913 | 2026-01-10 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14359938-fda9-336f-a1fa-53e49f50e343 | -0.09075 | -51.2777 | 2026-01-10 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a86f10e-a06d-3703-85a8-f19036e7f0ad | -1.70177 | -45.81691 | 2026-01-10 05:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97456e31-cd49-302a-b644-7a9aacf65167 | -2.14622 | -54.39134 | 2026-01-10 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4e48488-4590-308a-85f4-a041de8ae30a | -1.8896 | -53.25821 | 2026-01-10 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97a386ca-db14-3b8c-b290-2591608cc437 | 3.3219 | -60.78946 | 2026-01-10 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27ffa04c-a348-3eba-94f1-65dcd9ed293f | -0.14637 | -60.73899 | 2026-01-10 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5db68e8e-fe81-300e-b20b-f242e3d95e67 | -0.08565 | -51.28134 | 2026-01-10 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abf14c02-17c9-36be-8da7-5c1fb3e2f174 | -0.11446 | -60.67254 | 2026-01-10 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6e29c31-62bd-3fcb-975d-a048eb257a5b | 2.1064 | -55.75996 | 2026-01-10 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a5d20b5-7570-3c47-af96-a5cc6de373bd | -0.11311 | -60.67107 | 2026-01-10 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 17fc6c7d-0abe-3314-80cf-ede0a81a1e83 | 4.3784 | -60.36213 | 2026-01-10 05:16:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90a38fda-734e-3073-9274-e29ef821ffa1 | -0.808 | -51.901 | 2026-01-10 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d60e5ff0-84c6-3461-8a20-cd22c2e38da7 | -1.59704 | -53.99105 | 2026-01-10 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f14f66e9-854d-3e2e-8126-802b9ea4db47 | 2.10696 | -55.76351 | 2026-01-10 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9fea726-df31-3fd3-9312-9c564b5de2e6 | -1.60079 | -53.98938 | 2026-01-10 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe674aaf-1e70-3618-abd7-82caed6004b2 | 3.92046 | -60.2797 | 2026-01-10 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b002369-3fdc-3368-a265-4305fee5122a | 3.92113 | -60.28403 | 2026-01-10 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd188df-b66d-3de8-9e41-db7b9cee94d1 | 2.11033 | -55.76298 | 2026-01-10 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9948c0d6-fc7d-36e2-b29b-f5970ad13d89 | -1.70261 | -45.81156 | 2026-01-10 05:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e37ac566-a2a5-33a1-858e-c810303ff6ae | -0.09008 | -51.28206 | 2026-01-10 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41437c78-f539-3b76-b66b-860d6a587e73 | -7.59629 | -45.89069 | 2026-01-10 05:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e6e2565-4744-3844-945f-54c3f5984b35 | -7.59801 | -45.8893 | 2026-01-10 05:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec5e6e74-17db-33cc-b46a-aa9b9b33a085 | -12.3946 | -58.0307 | 2026-01-10 05:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| b26e94bd-5640-3bb6-9313-5f984ffe96aa | -12.4135 | -58.0292 | 2026-01-10 05:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f6147a79-0592-3144-9ad6-2ab71cc5317e | -12.4133 | -58.049 | 2026-01-10 05:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 7e718cd7-4bc4-3988-9859-24438043515a | -12.3943 | -58.0506 | 2026-01-10 05:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8e78278c-0f17-3363-9da1-ddd5e103b27a | -12.39237 | -58.03742 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6097c844-9105-30a0-9620-c7b7b0a4c818 | -12.40284 | -58.03905 | 2026-01-10 05:20:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 184e6d2a-4cd8-329c-988d-e57fdca95a05 | -14.7333 | -57.77168 | 2026-01-10 05:20:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
