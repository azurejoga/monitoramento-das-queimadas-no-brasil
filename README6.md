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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a867efb1-5ba8-3f43-9ca3-7e14bf544206 | -14.85477 | -48.53459 | 2026-05-06 04:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 763aa2b1-0858-3743-b0fe-a82ed9975686 | -12.34709 | -50.01718 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1096510f-9f83-3582-98e2-fce108cd5e6d | -13.9816 | -47.21995 | 2026-05-06 04:06:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65b0ded9-4cf6-334b-8b98-cb641a6ad4d2 | -13.43808 | -43.84879 | 2026-05-06 04:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d10d7180-82fc-35b3-a13e-8d686b343d31 | -12.34257 | -50.01306 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7c0f84c-bdc7-3bf5-a182-a153dffc1eec | -12.33745 | -50.01204 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74215975-8553-35e5-9010-44d30fc7434a | -14.13571 | -45.36069 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 826f5d0e-6789-34d3-afc3-e8f4d2e8d16b | -14.08564 | -47.62951 | 2026-05-06 04:06:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a679294-c64e-38ad-812a-b625dbbde9c0 | -17.28622 | -47.78595 | 2026-05-06 04:06:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e84fa53-92d1-3196-8aa9-1901cf9fa4d4 | -14.07449 | -47.61868 | 2026-05-06 04:06:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa83e667-f33f-36bb-bcd1-9ee81f0af5ab | -14.07547 | -47.75644 | 2026-05-06 04:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7db0a2c1-6da9-35fc-bbf4-28a2d7b0abbe | -11.28888 | -54.02793 | 2026-05-06 04:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02991deb-c9fd-3943-be4b-219cc75acd04 | -13.29742 | -44.4263 | 2026-05-06 04:06:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3bc5a36-800c-3ec5-8d4c-1c94b334cbc4 | -17.49759 | -48.00086 | 2026-05-06 04:06:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 050e6cb4-6dc7-35fd-99c0-e6cbf3c7dfdd | -11.43767 | -55.10836 | 2026-05-06 04:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5271cf1-7a57-3404-8168-9508f2b05eb5 | -14.14389 | -45.35752 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fad65cb8-714c-3e25-bc75-a823c48c4fbe | -14.14837 | -45.35369 | 2026-05-06 04:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 459b182c-3ea7-3051-b645-903fe4a1a1f2 | -17.86213 | -42.57581 | 2026-05-06 04:06:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 19139b30-7a69-3021-af15-c92a053d70bc | -12.35041 | -50.02755 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 944d0a1f-366c-35a4-a9ea-47bdb0dfd1d1 | -14.85585 | -48.53648 | 2026-05-06 04:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87be049c-c0be-3a7b-b712-7fc2f2e6f366 | -12.34589 | -50.02343 | 2026-05-06 04:06:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05a87bae-8e57-32ff-8b73-c722d1b37c7e | -18.43476 | -54.70928 | 2026-05-06 04:08:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5b9281a-14cd-3c88-a164-0c55066661b7 | -18.49649 | -55.51455 | 2026-05-06 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b5ce99d4-99b1-3505-b386-2f405de9db7a | -20.20559 | -50.65007 | 2026-05-06 04:08:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| a4ebf450-b3d3-3fe0-97e5-807528292852 | -21.27832 | -48.97399 | 2026-05-06 04:08:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a303913d-d484-3c08-8a4b-532045c2e65c | -19.94571 | -54.38244 | 2026-05-06 04:08:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1d1a41e6-eeed-31e1-a578-995d0e8d7bbb | -20.20843 | -50.65248 | 2026-05-06 04:08:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| bee01894-b60c-3b54-b249-c68365578b87 | -18.77862 | -51.94419 | 2026-05-06 04:08:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 966c89e8-09bd-368d-baba-82364e34ab5f | -20.7132 | -52.08071 | 2026-05-06 04:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 185b5bfa-0aa6-3f49-91de-00a15e3d2f33 | -20.71256 | -52.08372 | 2026-05-06 04:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0593489-c45b-3013-86ed-8c556086e47f | -22.96975 | -52.69471 | 2026-05-06 04:08:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 789aa9bd-4fd0-3287-818a-a94ab7b3d33b | -21.97757 | -57.59064 | 2026-05-06 04:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44278f11-b629-3487-941b-d5e547be23b0 | -21.2776 | -48.97779 | 2026-05-06 04:08:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7a3be12-9286-34a1-8f71-5d682f2076eb | -23.08026 | -48.61939 | 2026-05-06 04:08:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f01f6ac-b0dc-3ef7-85e6-cfd812e621ae | -18.49604 | -55.51322 | 2026-05-06 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cc2cb733-2b26-3dea-a064-2152fc215c4d | -22.60573 | -49.56392 | 2026-05-06 04:08:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b45df0e-4514-32ac-b1f1-c94bd952fec9 | -21.70609 | -48.42244 | 2026-05-06 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 19e49b37-ae3a-39a5-8e63-289408562352 | -21.9694 | -57.59492 | 2026-05-06 04:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c6b199d-a7a6-3166-a56f-8c9d4399bbb7 | -20.35752 | -43.56288 | 2026-05-06 04:08:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5cdd0b6d-0f1a-3312-80d4-d1f78df46938 | -18.48473 | -51.68559 | 2026-05-06 04:08:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 086b05eb-9bd5-382b-82d6-2056e5693457 | -21.79413 | -50.7719 | 2026-05-06 04:08:00 | NOAA-20 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4a11b661-0f9e-3386-a134-c197cd6b48dd | -20.79251 | -51.65876 | 2026-05-06 04:08:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| 5aabdefc-60a7-32be-8bd4-0928032f6933 | -23.08125 | -48.61414 | 2026-05-06 04:08:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abd65d54-250f-3742-a3a3-51148a4360e8 | -23.72061 | -47.45613 | 2026-05-06 04:08:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 20cfec96-429c-3ec3-8d26-88c89e165480 | -21.7051 | -48.42768 | 2026-05-06 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebc2303b-1b42-3b86-ad67-df2d68c3aed9 | -22.80302 | -49.34458 | 2026-05-06 04:08:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d14f311d-dbea-3a16-be71-d601d65a8b5b | -21.97619 | -57.59616 | 2026-05-06 04:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a56ac38-03ca-3946-ac8e-a77efa56a975 | -20.52805 | -49.2449 | 2026-05-06 04:08:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 52ba5d39-82dc-315e-b54e-d8440a26b006 | -23.55765 | -48.5736 | 2026-05-06 04:08:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ff9b091-cb37-3d41-aa91-4aa57db6492c | -23.76447 | -49.15108 | 2026-05-06 04:08:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0862c216-2aef-320f-a72e-29b4095639ef | -23.54877 | -47.44828 | 2026-05-06 04:08:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53d2d682-42f0-36d2-ac75-418a26e9ea4f | -18.48232 | -51.68462 | 2026-05-06 04:08:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba96df36-5765-333b-b548-cdb7f3a0a63a | -22.74231 | -42.25203 | 2026-05-06 04:08:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| af7fdac0-a7a1-3e6e-89fb-2b9f2efe8f45 | -18.43369 | -54.71405 | 2026-05-06 04:08:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 742dcca5-afa3-364d-a2df-c3b58c4cc3bf | -17.94129 | -52.96836 | 2026-05-06 04:08:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e55f2944-cb66-397a-86f8-8051ade2192d | -18.48167 | -51.68782 | 2026-05-06 04:08:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1242a0ea-ed3f-379a-9442-97be2d6790ac | -20.21019 | -50.65108 | 2026-05-06 04:08:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f8bd5ec7-56f6-3737-a04f-ad0e8b59b7b4 | -20.22076 | -50.75655 | 2026-05-06 04:08:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7cb9e79a-bc0b-3f05-ad5f-8106afed40ac | -20.27337 | -45.54826 | 2026-05-06 04:08:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc818db3-6fbd-340f-8ef8-e2a9f7a679f3 | -21.70997 | -48.42339 | 2026-05-06 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2319d73b-5668-3c4a-96d9-12a5b86c6a46 | -18.93504 | -48.07327 | 2026-05-06 04:08:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 264a6547-0bad-3b4a-a351-9eabd16861f3 | -22.96984 | -52.69324 | 2026-05-06 04:08:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a287a13-d8c8-3544-8dee-ff4446135b4e | -22.16958 | -42.87552 | 2026-05-06 04:08:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa66c65d-2fc5-3460-9a96-424f661b1f5e | -20.20948 | -50.6474 | 2026-05-06 04:08:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 413d44fc-1b7e-393f-8f7d-6d7257b975fe | -22.2298 | -43.3194 | 2026-05-06 04:08:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bed73945-2637-33f3-ac54-2b3fa2c82a9a | -22.43924 | -44.51334 | 2026-05-06 04:08:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93be8ab0-c45e-3c94-8a87-ccb28d599478 | -23.55859 | -48.56853 | 2026-05-06 04:08:00 | NOAA-20 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16f66399-ce13-38cd-a613-e96eb5216093 | -12.5033 | -58.4781 | 2026-05-06 04:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d39d5635-283e-3bd4-8b98-4c84e6949c0a | -12.5033 | -58.4781 | 2026-05-06 04:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| a8ab8a88-321f-3f9b-a689-6d056eefd674 | -12.5033 | -58.4781 | 2026-05-06 04:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 4a27a09f-e70a-3e16-91fe-e953e7d8a67c | -12.5033 | -58.4781 | 2026-05-06 04:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f5e37e57-aa50-3aa2-9b05-aa481e04e85d | -12.5033 | -58.4781 | 2026-05-06 04:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b9d8f97d-0cfd-3cc3-803e-b14407da0c6d | -9.25855 | -49.26107 | 2026-05-06 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc0cfda8-2e58-309b-b22f-dcaf9feb419a | -9.6797 | -47.02247 | 2026-05-06 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b7e4b8d-25b4-34a9-9528-d4b487b554fe | -5.78859 | -45.12535 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bd6ad00-7ea1-3915-9406-ee4a6d92d43c | -8.15782 | -46.66136 | 2026-05-06 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90c78d51-ef3d-3e63-a4ca-86f001c6564b | -7.90453 | -50.37221 | 2026-05-06 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d6ebd4f-9e20-3a8f-b625-ea02eabbb923 | -8.72711 | -48.33193 | 2026-05-06 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c171735-d4ed-3cef-8b0c-f004b46d7928 | -5.78927 | -45.12046 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4af7a520-6c4d-3afd-83c2-002fc0334e3f | -5.78614 | -45.12401 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 815b0bee-16a1-3f31-bd0d-6768811d26ce | -5.78791 | -45.13023 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ebf8b86-b5b8-3c75-b26e-a1a16874e141 | -8.62181 | -49.5252 | 2026-05-06 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b863aad5-5c47-3869-97a2-c2678cfa2ed3 | -8.15644 | -46.66333 | 2026-05-06 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e861b0d-ea56-3fd0-b4a6-98af91418015 | -9.36853 | -47.67741 | 2026-05-06 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f753bf3-88c8-3451-82ca-8f25b1c12ffd | -8.36737 | -48.07773 | 2026-05-06 04:51:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 751e6fc6-1845-3d80-84d6-2215b3e1e1e0 | -5.78543 | -45.12888 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a389a8a1-51cd-319a-9edc-c50478daff06 | -8.22534 | -43.87726 | 2026-05-06 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f28361c-5a54-3f68-813d-bfc6bfee9a1d | -8.15347 | -46.66066 | 2026-05-06 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 521e3af5-f660-3158-80e6-eb5bcdc9556f | -8.62243 | -49.52085 | 2026-05-06 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2294e032-41fb-36a7-a044-9a922c34a42d | -9.46733 | -47.80248 | 2026-05-06 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cadc3416-a6b8-3409-b70e-fe62d4e04561 | -6.22466 | -55.64381 | 2026-05-06 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cdcc866-1b11-3215-9ac4-d0b9ead2a50d | -5.79011 | -45.12956 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1df62646-5bd2-366e-a46f-7c694f2f142a | -5.78686 | -45.11912 | 2026-05-06 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bfce08d-1860-37a3-9a9e-fcc674cbd7e3 | -9.47144 | -47.80312 | 2026-05-06 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 990f118e-dede-364b-9361-ff208af3950e | -8.23063 | -43.87799 | 2026-05-06 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5d09fe1-202b-3fd1-a5cc-dde4ea2cad0c | -11.13775 | -45.14315 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d4ae4bfa-2af1-31ed-9431-6c8fa8ba7321 | -12.27427 | -43.51277 | 2026-05-06 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b34d579a-fc4b-3486-86ba-f5866ca6c8e2 | -12.50602 | -58.48243 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 048e07ee-2250-341b-a69c-0305f7595481 | -13.44193 | -43.8491 | 2026-05-06 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0845edd5-546a-3f8c-b80c-6f556ab23f2e | -12.34231 | -50.01324 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README7.md)
