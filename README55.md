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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5ffb5d7-bf81-36f0-85fa-34b15043a65c | -15.24443 | -53.8679 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 579d08c1-287f-3fd2-988c-4cc10594eb67 | -15.91434 | -56.22221 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 33997909-8260-3df1-b65f-927b8acd53d6 | -15.67792 | -56.27834 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77ba7006-8637-35da-a3d2-956d71f67f2d | -18.28516 | -52.68808 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 71d67520-1e01-3c13-ba58-1848f74d7552 | -15.23585 | -56.38847 | 2026-08-31 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74842e8f-f1f2-34a7-869e-a22633f578b6 | -18.28572 | -52.69593 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bf79977-f0a7-347e-884e-a5c67f211e58 | -16.00987 | -54.40259 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8090e47-79c1-3d63-bcc3-8d358c248145 | -15.87212 | -56.49397 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4d8d893-e780-3864-82a8-08f9fe7d2c44 | -22.04549 | -56.08941 | 2026-08-31 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 143fd49e-9080-3f42-a96d-b5e6861a95eb | -18.27088 | -52.71894 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc57ff27-3e4b-30e9-8fe8-7475befdae5f | -15.23628 | -53.87487 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfbc8846-bba9-32a9-a7e4-a9b29409799b | -16.01332 | -54.40308 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be566182-e328-3590-8416-f27d23398616 | -18.28842 | -52.67602 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2ba643e5-a4ad-3aa8-8727-fbf5aff42534 | -15.24035 | -53.8714 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d989ac8-1a88-3458-bbbd-87c75eac02ac | -18.2794 | -52.70244 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba639461-6f60-3234-b383-0ed9e9d063b9 | -15.55147 | -56.28329 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f553644-5b15-393f-9aa9-01838ac261a7 | -18.28008 | -52.67984 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cd35b50-57da-317d-8fdd-dae3161224a7 | -15.91821 | -56.21918 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5b3d0d11-1c32-3244-bcb4-501cce31218c | -19.09712 | -57.37401 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c3b94365-fb40-3005-8763-eb87d2b3d765 | -14.51281 | -59.83323 | 2026-08-31 05:01:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24763647-37c0-3ecf-9aa9-073a15d6fb2d | -18.28709 | -52.67315 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 342f037c-2c2b-38b8-8919-af0978a0c499 | -17.31406 | -54.93932 | 2026-08-31 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe7af979-350b-38c2-8b61-37d1daed6df7 | -15.45747 | -53.96828 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6da2a0f-4bea-3228-a55a-cc42c87dd637 | -19.3262 | -46.06471 | 2026-08-31 05:01:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02939a90-a48b-3531-9e9c-d1abeb58819a | -15.41867 | -52.71418 | 2026-08-31 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abb5f8b5-ef15-3232-8e5f-8deeaaeecad9 | -14.68169 | -54.90654 | 2026-08-31 05:01:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d67817b-bdce-3386-bd8e-1924d6d57606 | -15.63098 | -50.0975 | 2026-08-31 05:01:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3349b228-5eb5-3896-96e0-dbf29b187672 | -15.51604 | -56.02863 | 2026-08-31 05:01:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79e1d76b-eb31-3f91-9c7f-4af1536f2801 | -15.12621 | -53.58345 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f8d08fd-e7c1-3eae-87ba-55bd4cabd2a9 | -15.55533 | -56.28027 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 261703b7-9f21-342e-bd74-b02146c8e946 | -18.22934 | -51.65288 | 2026-08-31 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5d88c29-a4fa-3ce3-b9ba-0af3dff85033 | -16.00642 | -54.40207 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eb4d6ba-a706-32fe-8d52-042b5869908d | -15.87986 | -56.48792 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e602c155-8d4c-36c9-9aee-0f78ab68d580 | -15.63697 | -56.38879 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0aaa75c2-ba6e-3d74-ae62-b459657004b3 | -20.25264 | -58.1544 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 02901062-de86-3afa-9a51-6c39d05b794e | -18.28459 | -52.67545 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c1b7d0f-b253-323a-a1c1-852aa289fb6c | -15.87268 | -56.4904 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdf7f666-0303-3c9b-a6c9-229fc21e9fa9 | -18.27366 | -52.71674 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 615d1d7a-ea4d-3a81-be7b-e9f5ca4089c1 | -20.25538 | -58.15868 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| afb5a11b-9192-3d29-b2ff-dd2c965d24cf | -21.89624 | -55.37185 | 2026-08-31 05:01:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 326d08bd-157b-3324-aaaf-0e77b587d6e6 | -14.42501 | -56.26934 | 2026-08-31 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e9e57700-e4d7-3f0b-9b35-54c910fef2f4 | -18.28005 | -52.69746 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b97e68f0-7071-36a4-a5ab-68f427013f9c | -16.35585 | -51.00916 | 2026-08-31 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63ba248e-2c32-3460-80fc-7fa936674e1d | -15.23978 | -53.8754 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf36fb13-57da-371e-9d6c-ce1ce569f4a7 | -15.62479 | -56.4234 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c82ab4ed-80fc-394a-8ee2-a85f4fc19ab4 | -18.27739 | -52.69972 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6853a7f4-288b-3cec-b444-5e174031d91f | -15.64084 | -56.38577 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2985a051-39e8-3350-bfba-7c32838e569f | -18.22525 | -51.65235 | 2026-08-31 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3ea5ef8-9ef8-3f0f-9984-f7a36fc2333f | -14.6845 | -54.91073 | 2026-08-31 05:01:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 483d9d7a-faf4-3472-a54c-db5adbb6c3a2 | -18.27558 | -52.70184 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 09166b7c-c53f-3838-8468-59cbfba2d429 | -15.91765 | -56.22276 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| acb68b63-f99e-3886-90a2-421fda50bedb | -15.56306 | -56.27422 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d48412-cbff-3348-a77b-86fd37075385 | -17.99469 | -44.31191 | 2026-08-31 05:01:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46489466-2aae-3a79-8fcc-3f32f014f26d | -15.96338 | -52.209 | 2026-08-31 05:01:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a37f91f-33bf-3d39-baaa-5fd5e6742aa5 | -15.62204 | -56.41928 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e183c68f-1112-32f3-90fd-f2c911a5a91f | -18.28189 | -52.69534 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d0b0335-e3ed-362a-b1d8-d78e473ae455 | -20.36699 | -47.45953 | 2026-08-31 05:01:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16135358-ee7f-390e-879b-ac95d41690fa | -15.62593 | -56.39429 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f3e1006-f7bd-3a94-84f4-eaf720c8370c | -15.56362 | -56.27065 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd227606-c26b-39b5-a451-56752bb211c8 | -15.77231 | -48.52772 | 2026-08-31 05:01:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1d1c3ff-b87b-38a5-985f-d4761b0c8224 | -14.42777 | -56.27344 | 2026-08-31 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b7bd3f8-c419-3760-941c-8b2224a55b77 | -15.41928 | -52.70976 | 2026-08-31 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6603823-221e-3d7b-b41e-036f23de9080 | -19.13452 | -57.39519 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 450a8ecd-8921-301b-8311-ffa98db8441a | -18.22886 | -51.65672 | 2026-08-31 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95213cd8-0adb-3c1d-a95a-8e942d0bb2f8 | -15.92041 | -56.22688 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d50c5a45-8eea-3dbc-8305-d4a31f04102f | -15.61984 | -56.41159 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f4a73f-c5a4-3a57-949e-5b15f5207c75 | -18.2864 | -52.69094 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95c767f8-5830-3619-9951-89990819deac | -15.24269 | -53.87993 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f40dda53-155e-3984-9426-47eb2f11eb1e | -15.55422 | -56.28741 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f268a1ac-f0d2-3ebd-8b22-45ac185cca62 | -20.25206 | -58.15809 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f7d5b8da-cd32-35d3-b695-42260b40e05f | -15.24619 | -53.88046 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3508634e-8260-31aa-ac87-db6971b71022 | -15.55202 | -56.27972 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de7776a8-d5df-3ed5-8a1d-691800897088 | -15.91379 | -56.22579 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 87b68483-8a7c-308f-bc31-e77c3a5c187e | -18.27306 | -52.67383 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c7ddf44-ab9d-3692-ba90-59ea3693dd4b | -15.61928 | -56.41516 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0720c73d-bdd9-392e-b622-bc39668dacfc | -18.27877 | -52.67698 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9b533a3-41f0-3c34-8374-50388e39b6d0 | -19.15656 | -57.40649 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3fd18f26-1edc-38a2-8ecf-ad4aae9af0e5 | -15.23863 | -56.37066 | 2026-08-31 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a160c0fb-3e39-3aeb-9916-ac138a5fa67f | -14.4245 | -56.27283 | 2026-08-31 05:01:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| afe536d7-efdd-3c7a-99e0-f4628b9e6407 | -16.35633 | -51.00538 | 2026-08-31 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3c42e03-c8f1-32e0-a58e-d4c87523500a | -15.55589 | -56.2767 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a9c884a-c2c7-37c0-9153-2f86a0313a84 | -18.28387 | -52.69806 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 81c97680-8ce6-3376-a50c-7585fd9643b9 | -15.24677 | -53.87645 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dacff57-5665-3aed-a421-e90400cb80f6 | -15.91489 | -56.21864 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0abbcbfe-a9b2-3c21-b37a-d89ba47785db | -20.25928 | -58.15558 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| cd6bb498-c38e-30f1-b3b9-3ac733dc0eb4 | -16.0162 | -54.40749 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99b913d5-3030-3a95-8f28-e31ebdf6f08b | -17.45372 | -52.4137 | 2026-08-31 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5ef369d-02c8-3a8c-a1ea-d9da7f6a17f2 | -18.22477 | -51.6562 | 2026-08-31 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9841503-f352-374f-a469-398aace8952d | -17.30149 | -54.92969 | 2026-08-31 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 903814a6-45b3-3818-883b-a89de233d2e5 | -17.30093 | -54.93344 | 2026-08-31 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d44f362-6a8e-3b28-be8d-b50ad777a0b2 | -15.61433 | -56.40336 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9c40969-c5d6-3aa3-9b55-f2920c7d9391 | -18.28075 | -52.67488 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3470168c-8208-36e2-b0d5-97840626b87b | -15.41184 | -52.70901 | 2026-08-31 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aef7a98e-f0c3-34ae-b91f-2cc84de8cced | -18.28964 | -52.68369 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e2fb0fe-0ebf-3a46-ae4f-c06f983770fc | -18.28645 | -52.67812 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3830bcfe-a67a-3954-8839-451ad370e638 | -15.55975 | -56.27367 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d0818a5-7642-3e7d-93bc-58c3d37e39c0 | -18.28122 | -52.70031 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9c0f4f1a-bc6f-3d89-96ee-821976c1ada7 | -15.88317 | -56.48847 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6063045e-dca7-3063-9521-69d2676c56d7 | -15.61157 | -56.39924 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3571f780-76f8-3e6b-9af1-bfe9ff7506a1 | -16.01275 | -54.407 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README56.md)
