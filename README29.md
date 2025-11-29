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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5051d36d-ad9f-3cad-8b58-6fe3a6d084dc | -1.68696 | -53.65157 | 2025-11-29 05:03:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 419740ba-8af0-3214-9ecd-a9b0ba379a13 | -11.08219 | -54.78358 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d61c066-533e-3c4f-a8ae-7c1997be86fe | -11.26926 | -53.95804 | 2025-11-29 05:05:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f981e826-2e32-393f-a573-e0f2c9595169 | -11.27058 | -53.95965 | 2025-11-29 05:05:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d761369-fa89-3c68-bfa8-a49a171b2331 | -11.07875 | -54.78302 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5723bae5-a0c4-3b4f-a523-5b931cb40e74 | -11.08277 | -54.77974 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 970a0b6a-5acb-357a-88a6-e385c80c87b9 | -11.0799 | -54.77536 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f620f833-25cb-33cf-9eb8-52453357a34f | -11.08335 | -54.77591 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d971395-c7e4-39e8-9b8f-aaa341477019 | -11.08679 | -54.77645 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7511f879-ef4c-3c28-b3f4-77bf90e02502 | -11.07703 | -54.77098 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b82d95f8-ec1b-30b9-a1a3-8b655648f760 | -11.08047 | -54.77152 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c74731a7-f755-319e-984a-8d79dcc16c36 | -11.07932 | -54.7792 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60148937-182c-3306-8dff-6cc18f843604 | -11.08621 | -54.7803 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ff17b7a-7e20-33b9-a35b-ca221201d531 | -11.07588 | -54.77865 | 2025-11-29 05:05:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eec8cdef-c2ed-347b-9db9-4ced791ea69b | -16.09445 | -59.00348 | 2025-11-29 05:08:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 049a9434-fc05-3848-bde9-e2c4357672d7 | -20.17775 | -52.37587 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6d6108b1-995c-35f7-90fa-4021dd7b1615 | -18.11897 | -47.13471 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16db9550-0b3b-3167-9fc1-5fcd1165d6b0 | -17.48876 | -57.12859 | 2025-11-29 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3ea7cf32-576c-3528-a8da-6f94851b344d | -20.1855 | -52.38605 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 24b79ab1-4078-3e95-88f5-54b4e61c276a | -22.72399 | -49.34556 | 2025-11-29 05:08:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e03fd9d-0cc6-3941-9d6d-7ac5950733da | -20.20818 | -47.54896 | 2025-11-29 05:08:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeeab426-eb28-31e2-bea1-cb84cad8f2c4 | -16.09975 | -59.76333 | 2025-11-29 05:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2483768-b58e-3840-be76-cef6116ed9b2 | -20.18659 | -52.37712 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b67a5778-b298-328d-80f2-22ee3ee67642 | -20.18217 | -52.37649 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9b02831f-2a5a-388d-8ce9-6209147f1aaf | -16.1931 | -59.33216 | 2025-11-29 05:08:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d484b4a-782d-3c4b-aff5-0f115e30e506 | -19.33683 | -54.17512 | 2025-11-29 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3efd7b0-0d5e-3f2d-80f2-93f9c1e2f06f | -16.6779 | -46.65812 | 2025-11-29 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c3f2e5c-f8d2-304e-8fef-2002dce08390 | -20.44675 | -47.51039 | 2025-11-29 05:08:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc405f54-9efe-3b34-ac21-4a178304560c | -19.11899 | -52.7127 | 2025-11-29 05:08:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e2e8a82-55ad-3324-86f1-14fa03090316 | -20.19101 | -52.37773 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 25bd344f-6ace-3172-add9-780bf35931d4 | -16.09636 | -59.76273 | 2025-11-29 05:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c252595-2b10-38ae-8588-8ba70606bfc4 | -20.18163 | -52.38097 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d0af9618-57a4-3dd4-84b1-d65c70428601 | -20.2086 | -47.54423 | 2025-11-29 05:08:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae010d1a-de75-3627-93b0-d52097b977a5 | -20.18109 | -52.38546 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 88aa5045-3f80-3d6c-b2a9-61594274822b | -15.93858 | -59.84811 | 2025-11-29 05:08:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c0b9298-5bb8-31a9-bc78-d7bb34df07df | -17.48932 | -57.12487 | 2025-11-29 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fb24c260-ef49-3791-b31a-12fccd7cd638 | -20.21549 | -47.53552 | 2025-11-29 05:08:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e42bbb44-42ec-3d58-b588-e0119beb20a7 | -20.43849 | -57.92624 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f9097374-7494-39a5-8a2f-e12e85d9c718 | -20.41096 | -47.2245 | 2025-11-29 05:08:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9e8237a-9601-305b-9b5c-1057785ff976 | -20.22197 | -47.53135 | 2025-11-29 05:08:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdad8f82-a999-3579-8362-b3744cd6354a | -19.12375 | -52.70922 | 2025-11-29 05:08:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9def00ec-ce21-30b2-a55e-ea2c52bce806 | -20.18605 | -52.38159 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 43adb3e1-1854-3f3b-b53a-1b9d1d90f1fc | -20.21592 | -47.5308 | 2025-11-29 05:08:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8edaa34-1ace-3013-976f-62e8c6f39ba2 | -19.33765 | -54.1722 | 2025-11-29 05:08:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dd558fe-740d-3197-9765-3126b9af7214 | -22.96764 | -47.03111 | 2025-11-29 05:08:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c6e8cf5-6660-3a43-bbfd-d07fe99bb138 | -16.76519 | -51.35873 | 2025-11-29 05:08:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f71a14-e37c-3701-97c5-9684dda303a9 | -23.25799 | -48.29027 | 2025-11-29 05:08:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4bc61d2-6b3b-3bc5-83e8-50e80b400b94 | -18.13804 | -47.14069 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22bc1d61-a04e-39d7-861c-08d698d2161a | -18.17083 | -47.24194 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67f95a54-7bfc-36fa-bb3c-b70421badf19 | -22.72955 | -49.34616 | 2025-11-29 05:08:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa32d18a-f30c-3e7a-9dae-c01fce56d874 | -20.41714 | -47.22506 | 2025-11-29 05:08:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ee2f5cc-d895-347c-9ee7-849204337f78 | -17.48819 | -57.13231 | 2025-11-29 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 92010a1c-d05f-329d-8abf-5c0f51d966d2 | -20.41146 | -47.21913 | 2025-11-29 05:08:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91ae4bda-7131-3e4b-9beb-98b120ce1526 | -21.68884 | -47.95873 | 2025-11-29 05:08:00 | NOAA-20 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba9e3fe-56b4-3933-a498-753998d119c9 | -17.60816 | -46.6619 | 2025-11-29 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db0d3a3b-b476-3d00-83e5-ae288c1435ef | -18.12547 | -47.14414 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 793d1583-9564-3f1d-b535-d0701d242f08 | -17.65436 | -56.46628 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| eab7ee59-84a2-3b64-bc06-cb66654513b7 | -18.12501 | -47.13551 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3e1ea4d-e913-32af-966d-d1186138d489 | -18.13018 | -47.14483 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8cf5a0b-9c99-3114-a286-abde6bb4011d | -22.96721 | -47.03646 | 2025-11-29 05:08:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d2bc3c7f-9b5a-3ab7-a955-0c88796ce10f | -19.05417 | -55.81535 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b645206b-a0f3-3145-9304-0b9a134b594a | -20.18271 | -52.37201 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 0c172f22-4bad-3a77-ad6e-540ceb9f93b9 | -17.49269 | -57.12542 | 2025-11-29 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| adf5fd8c-34d9-3de4-b2ef-02b410a0a279 | -19.89459 | -57.44223 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a7dccd7a-3212-30ce-9c40-f65342793063 | -16.76127 | -51.35338 | 2025-11-29 05:08:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53613485-0609-36d2-8b3d-4942c7a39835 | -20.21464 | -47.54492 | 2025-11-29 05:08:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8e3327b-7268-3521-96ec-6461a89fe474 | -19.79673 | -56.09806 | 2025-11-29 05:08:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3a778f49-9f04-3613-ad64-77ebf374f1af | -16.10376 | -59.76017 | 2025-11-29 05:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a3880e7-ccbf-3224-bbea-9140834d4e37 | -18.12633 | -47.13516 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d3a511c-443f-3f42-bf8a-7531888a680a | -18.13765 | -47.1447 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8fdf461-5cc9-3dfb-84b5-a540f47f5e4f | -17.49212 | -57.12914 | 2025-11-29 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c5954c99-5a77-3343-834e-8e9dba9b9078 | -17.65836 | -56.46295 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 56563f66-2802-3541-904d-f3fc2c315ee8 | -23.25203 | -48.28962 | 2025-11-29 05:08:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5e82cefd-09dc-324f-b535-cdc1d009ddab | -16.19645 | -59.33276 | 2025-11-29 05:08:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4d08ad5-96da-3529-9fb6-50082ef06499 | -20.98232 | -48.62748 | 2025-11-29 05:08:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 27d8018f-8403-3bf2-9a78-3f15546691b5 | -23.13455 | -50.14504 | 2025-11-29 05:08:00 | NOAA-20 | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81025862-6eb3-3fda-8580-d108dc65be01 | -18.13627 | -47.14506 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48a411f3-6d09-3091-bc54-d3ba14e5b3e7 | -18.13156 | -47.1444 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8576c25-5798-3e4a-b52f-95306fa38b30 | -19.89965 | -57.45483 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c7363d6b-7f0c-3bc3-8b92-1f35d1c567a9 | -17.4854 | -57.12804 | 2025-11-29 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4b0e7029-273a-3373-a523-9fdd098cb645 | -20.43905 | -57.92247 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cd49e31d-ebda-3591-803b-f59a3eea3bd6 | -16.67806 | -46.65491 | 2025-11-29 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dd65800-500e-39f0-aeae-10dc539713a5 | -20.41756 | -47.22055 | 2025-11-29 05:08:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a8f9697-7a44-3cd5-b6a2-1d3375200949 | -19.12425 | -52.70511 | 2025-11-29 05:08:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9438d19c-f8a4-329a-8d2b-85d65f3ca86b | -17.61386 | -46.66755 | 2025-11-29 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5f86c9e-6b23-3a21-b401-18df2f5f0c67 | -19.12852 | -52.70572 | 2025-11-29 05:08:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddd8d6a1-a9da-3d44-8c89-803c3c67198d | -23.25243 | -48.28485 | 2025-11-29 05:08:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 05ab4083-d091-32d3-9064-528e9cf70868 | -18.13669 | -47.14104 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 936d9911-b250-3794-a23a-8f66a3ae3427 | -20.44633 | -47.51511 | 2025-11-29 05:08:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c9766fb-de20-354e-9019-23ada18864b8 | -20.17721 | -52.38039 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 35.8 |
| aa73fde9-8f45-30d8-bea6-ac961319ccc1 | -20.44072 | -47.50928 | 2025-11-29 05:08:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 579a0bc8-5403-3b35-a527-7dcd3a1fae67 | -18.12029 | -47.13436 | 2025-11-29 05:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e075aa7-3bf4-3a82-9f95-e727070cf74d | -20.19046 | -52.38221 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| bb4414ee-9270-3860-85e6-f3e2d16d8315 | -20.4528 | -47.51125 | 2025-11-29 05:08:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83d3dca3-b18b-330b-a75e-b85520bf1896 | -19.11949 | -52.7086 | 2025-11-29 05:08:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbde993b-f121-3150-ac88-5b563a913c35 | -17.60766 | -46.6669 | 2025-11-29 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0133ac6-b333-3ec5-97cd-168e73a46122 | -20.18992 | -52.38668 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2bf44320-ae2b-340f-ab20-f7432ee91380 | -20.17666 | -52.38491 | 2025-11-29 05:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 92111002-fc82-3c60-ae29-0c8697776ec7 | -19.89402 | -57.44606 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7070e568-e5ee-35a7-9e20-9f8186f9836e | -19.0506 | -55.81479 | 2025-11-29 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
