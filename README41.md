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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1b14ef3-f3cb-305c-9913-f6ee00c0962e | -10.15249 | -44.5571 | 2025-10-12 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8808b59c-b93e-37ad-b339-5a58bc84bda8 | -10.72952 | -69.44807 | 2025-10-12 05:04:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d3f5a33-a415-3c48-960a-7118a6770dd7 | -9.08325 | -48.02892 | 2025-10-12 05:04:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba6ef8e7-d537-31e8-be97-cae03655deaa | -10.73238 | -69.44806 | 2025-10-12 05:04:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d3385d3-ea7c-30a2-94be-fe84f6bc2c63 | -11.85279 | -56.86972 | 2025-10-12 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12988843-203a-3571-aa60-f40cbc0be9ae | -10.73119 | -69.45404 | 2025-10-12 05:04:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb6699bf-9edf-301e-8469-dc1d2c48082c | -9.71149 | -61.92342 | 2025-10-12 05:04:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 426b7f34-d30c-362e-b875-a07cf8512235 | -17.40341 | -46.87365 | 2025-10-12 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 498ede4f-06c3-328d-b289-c102ab0323e5 | -15.46302 | -55.9441 | 2025-10-12 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7929e02a-e105-3696-8f64-2d88e922ba7a | -17.82544 | -57.67009 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 753642a0-2a1f-38b1-a067-b356d1bc1fcc | -15.18511 | -56.85667 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9040790c-8e26-3029-8b0a-c9f093bfcbd5 | -19.04523 | -57.54736 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 05cdf0ea-6bbb-34ff-9375-27e66e1825b3 | -17.94082 | -57.62562 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 62ca85b0-7db8-3cb0-ab12-6df60b7281ff | -17.84374 | -57.66197 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 97d2bc9c-bf2a-3556-bf03-eeba2aa638d6 | -15.46642 | -55.94464 | 2025-10-12 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85d5314b-1bbd-317b-aa31-da29470bc2cb | -15.85853 | -56.75705 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8be4353-4268-3898-95ed-4f59f8186fad | -15.0007 | -53.88088 | 2025-10-12 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f17ab72b-fd91-39b3-88c8-00fd8e9f097b | -17.826 | -57.66648 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c12624f0-a1e7-3645-bbaa-a70263c77322 | -16.11725 | -53.97702 | 2025-10-12 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24aa1aac-9d9c-32b3-ba97-4c9e930d150a | -18.55514 | -46.94613 | 2025-10-12 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1c48419-2b87-3c76-b755-0b0a2dc1c1d5 | -18.55663 | -46.94345 | 2025-10-12 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19cdf0bd-0b69-3748-9be2-2212c7cc7bb8 | -17.2567 | -52.26712 | 2025-10-12 05:06:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bc0b80b-926e-3fe2-b86b-b5ee3bbc2adc | -15.46585 | -55.94841 | 2025-10-12 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 58475330-5c22-30ef-bba1-f53ec81c5883 | -15.15468 | -56.81502 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ed5364c-3a85-3bb8-9a91-095f2ce307e6 | -18.03754 | -57.52582 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 12d6e2e1-24ab-33de-a9ce-076808d3c7ab | -17.83321 | -57.66395 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 029257ae-2d64-33b7-a111-150693f5b393 | -17.81935 | -57.66541 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ec268290-e951-3979-b57d-cd7ed54f56e2 | -18.07588 | -57.52087 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eb81f091-b51b-3c96-b3da-d4029a27b40b | -17.82267 | -57.66594 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ef4fa17e-a158-35fb-b77b-f0a71112cca2 | -15.45961 | -55.94355 | 2025-10-12 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39a8a3bf-ab66-39d0-87bb-9a4de04dee35 | -17.84042 | -57.66142 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b0ff72b7-8cad-34c8-b421-af1ce45a6754 | -15.28496 | -57.09042 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbbeadbe-defd-3f54-8771-dfa3661f6d82 | -17.8443 | -57.65835 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e41a0c66-ab87-3963-ab55-6ea379492822 | -15.23387 | -56.87226 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f8cdae5-3225-3435-abc4-9b955f521282 | -15.87525 | -56.75972 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 373c8856-aa63-359c-abc1-ad044232cc95 | -17.95581 | -57.61691 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a758874e-87b3-3226-9292-850fc69650c1 | -17.95914 | -57.61747 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6b675d3e-802b-3603-91b3-1bd50d086ba8 | -15.2311 | -56.86811 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ed5d0b-4b72-3f35-bf07-1f9fef5d1e87 | -17.82932 | -57.66702 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 556dabb5-2493-3fc0-8e0b-bd20faaab2c2 | -18.40506 | -46.39418 | 2025-10-12 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15c9ea39-7099-3ee0-afbe-27ac67e7ea18 | -17.8155 | -57.64616 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eef2b931-43ac-3a1e-8f21-33bdd25d604a | -18.04314 | -57.51161 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 512e2a0f-ccee-376b-a621-aa576c2cf69b | -15.18843 | -56.85723 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df628b75-77d5-35b8-bf28-4d7c09e77ab3 | -17.81602 | -57.66488 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e0b8f6e7-cce1-3ea6-ab54-f71203baf674 | -15.15191 | -56.81086 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e37c9c52-d210-31aa-be09-44f7270d2d41 | -15.69771 | -56.14942 | 2025-10-12 05:06:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7448a350-98ff-3c69-98a2-fc592deb3a1a | -15.85352 | -56.74498 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4eeac73-24bf-3c8b-b3eb-ec7a3742949b | -17.25618 | -52.27126 | 2025-10-12 05:06:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3ee2ff6-5506-3e17-88f6-bfa68ea25f97 | -15.17013 | -56.84311 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29371fb8-7c71-3679-b117-b177a36e0ca1 | -17.25199 | -52.27057 | 2025-10-12 05:06:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 109f98e0-a914-3d06-abff-7c96d630cb9c | -15.46245 | -55.94786 | 2025-10-12 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 484074d3-74a6-34a9-8d34-29bbe5d1967a | -17.94747 | -57.62673 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cc91cfc6-1a2a-39b7-8c37-b7af169d34f4 | -15.71499 | -56.15543 | 2025-10-12 05:06:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 761fbd65-fb28-31ea-b5eb-f16504ab8790 | -15.20395 | -56.8672 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed9a93fd-1dc3-3c66-a56c-5d39b290097c | -15.22721 | -56.87118 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 463ba781-3851-317f-a9fc-6ce2ebd26e11 | -15.00313 | -53.89048 | 2025-10-12 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54206095-5d74-3326-b33f-0aaaac1f8f63 | -17.94358 | -57.62982 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2536db6e-7bb5-3426-a754-b1973a8e0376 | -17.40994 | -46.86897 | 2025-10-12 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c3a7c75-e3ad-3f25-bffe-7e71c8f80fdd | -15.00007 | -53.88541 | 2025-10-12 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fcae8ae2-a8e9-3041-81f0-7fe91f3d612b | -19.10154 | -46.41586 | 2025-10-12 05:06:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5a10c38-8690-3eed-a56d-ebf1453313b2 | -17.94691 | -57.63038 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5f395078-b3aa-338c-a5db-0b2c54ecb902 | -17.25147 | -52.2747 | 2025-10-12 05:06:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9c57053-4efc-3234-8454-9d80812286ad | -14.71004 | -56.32421 | 2025-10-12 05:06:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1213a31-19f1-3aaa-a051-83003adaa01c | -14.16777 | -57.24414 | 2025-10-12 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5bee46e-c086-3f7d-93c6-2b9e51805ccc | -19.04857 | -57.54792 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| d39fcf41-9775-3ef5-bb27-8de6338a9aeb | -15.87246 | -56.75555 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c62dac9f-48f4-3444-a384-a8c027bbf8b6 | -17.81546 | -57.66847 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0f90b15f-dbd7-3562-8d0c-c37a79ae8251 | -19.02296 | -57.53601 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7d4ab25f-b512-3e54-bd5b-9a82beba2bac | -19.03911 | -57.54253 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| f387404b-6dfb-394a-852e-61b78e6c9bdc | -15.17346 | -56.84366 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f122fb3-6820-35ce-9d87-b0e6c3cc2393 | -15.8758 | -56.75608 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93a0c7dd-59e1-3b88-b90c-487e65a7b43d | -17.86721 | -57.57637 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3148ae8c-1b8a-338c-86c6-aa2c41c74532 | -19.04188 | -57.5468 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 4f863c22-1363-3dfa-8d6b-c08ac4f2b8b5 | -16.00264 | -56.00711 | 2025-10-12 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9e105fa4-0785-3e52-bc53-c2265f33fe8b | -15.28995 | -57.0802 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 565997f2-cf5e-390b-9451-a6d613e00380 | -19.01905 | -57.53915 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 28adf04b-c1d2-36a6-bda3-3726c5d8261a | -16.11791 | -53.9724 | 2025-10-12 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0988ed69-d736-39c7-992b-81964feb58f4 | -17.89695 | -57.66684 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c9358b0a-9032-3dc2-aa90-960dd6ef4d8a | -17.82166 | -57.62839 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fa8eb5b0-034d-3243-968d-6ed26a24ab93 | -17.88918 | -57.67299 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 21f26d79-9a69-3eb2-b45b-182584b761a1 | -19.03633 | -57.53827 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 207c3f63-a309-3070-a7d2-70861bc17872 | -19.04132 | -57.55051 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 423fba89-e76b-3775-8d84-3db6c51e681b | -15.28884 | -57.08738 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec1548c7-7ff8-3b55-9df7-1fef9617e251 | -15.28607 | -57.08324 | 2025-10-12 05:06:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4885d7c6-dd62-32e7-aca5-ede385a1604e | -15.85909 | -56.7534 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a64f002e-2d07-304e-928b-33aa5ff63bcb | -15.23663 | -56.87643 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe5b67b6-ff5d-3518-b0e3-7c65ab40d7f5 | -18.40291 | -46.39272 | 2025-10-12 05:06:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ea46baf-6635-398e-bb1a-60bdcff5ec3f | -15.87135 | -56.76283 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 225d1236-a7d7-3865-af8a-f7fb935504cd | -19.05248 | -57.54478 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 7fd0d734-8917-3576-ae2f-2b2c83b33f5a | -17.81325 | -57.66074 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| de0d245c-d02c-3d05-a930-8d6a973ee864 | -19.03854 | -57.54624 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 61fd38f6-85f1-3111-88b4-0e7e26e1cc11 | -15.21448 | -56.86532 | 2025-10-12 05:06:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e52b27d-2a45-37ae-b94b-faa33d13e90d | -15.87692 | -56.74876 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37037a5b-b48f-3105-8319-89c86d6c5fa5 | -17.95192 | -57.62001 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 31afc4b1-5d90-3311-8114-d425d1ff011c | -19.02461 | -57.54769 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1b0e105d-a9de-3894-9685-3b5b4e6d190e | -17.40774 | -46.86615 | 2025-10-12 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2165c86a-a57f-39f0-97be-25d3c227e553 | -19.05191 | -57.54849 | 2025-10-12 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| c8a045fb-0728-3ee2-b6a4-f5bd7bf22042 | -17.89582 | -57.67411 | 2025-10-12 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 17c458fc-532f-3b20-a099-d61d37aca05a | -15.8563 | -56.74919 | 2025-10-12 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 328df4ec-a0d2-30c6-a50a-91407d7c77e4 | -15.15413 | -56.8186 | 2025-10-12 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README42.md)
