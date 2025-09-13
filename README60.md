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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66645c40-1d32-3f20-a4e7-931deefdf839 | -9.02307 | -47.07222 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b91138e2-42b8-3bc2-a0ea-b00e4757f4d5 | -10.74068 | -50.5085 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b4c8d5b1-4b0f-3562-b55b-2abb4fb6f92e | -11.48689 | -43.70098 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 184a2ab4-2abe-361a-8221-a3da57436bd4 | -14.17766 | -46.24229 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6f78d08b-d385-3e04-a5d8-64185f7b4288 | -11.15622 | -51.38551 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8783a4e6-5673-38a9-9318-acc49b6cc94c | -12.1096 | -44.85436 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe69f1f-020b-3d19-ba09-a3bfa0b4511d | -14.46071 | -47.33652 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29bb5d0d-11c6-30a7-a80a-cfbedcfdc36d | -9.44561 | -46.41251 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 411fee4a-e0dc-3951-84b4-eeaced52113b | -11.85611 | -46.75709 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9512e8af-0c3b-3b13-8d0d-246bedb11650 | -14.21663 | -46.24999 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4481bf7d-ea9f-396e-b5f1-13877b160a46 | -9.24548 | -51.2523 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56fcb156-4048-3963-8112-49dde6b40e7f | -9.49526 | -50.88997 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7095d548-1c83-3c1e-82ff-e55ddaf4e15c | -15.05864 | -47.98799 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b198946-d607-3140-9e37-5b8da764d7a0 | -14.88189 | -44.4589 | 2025-09-13 04:08:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01030113-4f92-306e-8964-6e2a1a397b15 | -9.74259 | -45.38904 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d93d9388-f161-370a-a0d4-863eeb293f4a | -10.92776 | -56.21055 | 2025-09-13 04:08:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c041733f-70ca-3d56-8816-5b8704057ce4 | -11.04794 | -51.47804 | 2025-09-13 04:08:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bcdcce6-4779-3e93-a795-cc42f4d76917 | -14.18617 | -46.2354 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f28a8a07-b35a-32eb-8825-618f38fbe236 | -12.91 | -54.75484 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2af8589-28c7-3506-9bd6-c470d9b8e1e4 | -10.15605 | -46.16208 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f73f3d9-036a-392a-bca2-545f26548329 | -13.58211 | -44.88223 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 313ccca2-d316-31b5-b10c-af7ab3cede8b | -14.19826 | -46.25031 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 26d97c0b-9ab1-39a0-94ff-01b2de5848df | -12.83444 | -47.91888 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cc1815b-36b6-3b86-804c-8948d6be7431 | -8.05356 | -44.50673 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c63cb426-b6d3-34c2-a35b-91d0e8852c48 | -12.89525 | -47.94624 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33fc688d-6a53-3978-8bff-46a42ceeb61c | -13.2421 | -43.75286 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a26381ee-9f85-3383-be92-f0c6336d131d | -12.99629 | -46.74078 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93d19a22-22f3-39e9-bfbf-c0856790d658 | -12.5663 | -44.67795 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 857dbba3-99fa-34b3-8c18-da74106fcccd | -13.9208 | -48.27583 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce4bfac6-d93d-386b-9d77-e9fa50ed2921 | -12.13219 | -44.84177 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8829ed9d-2a87-3587-8c5e-35520b6a128c | -10.23845 | -48.63559 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 26ae34cf-f2c7-39e5-bd9d-cbd998acb409 | -13.00604 | -44.11826 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c0f5661-45f1-3e21-932f-cd60e2e2a7ab | -14.74784 | -45.2605 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3063d53d-c3bb-3699-92ae-4b4bda0a8c29 | -14.70396 | -42.50694 | 2025-09-13 04:08:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f55728a9-ebe6-337a-a3d7-725d9adcc573 | -10.66156 | -46.28845 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 60f79a95-fd5b-3373-9c75-99205576b93a | -10.76892 | -50.51965 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c8ddaf62-8f00-3cdc-8e23-7243c41fa2db | -9.79868 | -48.89485 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 859eb512-8e54-375e-80f4-f926aec1fda8 | -14.20822 | -46.27785 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2c6f106-f099-3956-bedf-1443dcd0d682 | -11.377 | -50.74848 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbb6750c-2432-302f-82ec-54a2b1a30bb5 | -13.27201 | -43.75786 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc199720-cbbc-33e2-8dc4-0c86fac0bec4 | -11.82535 | -50.56015 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27acbbd0-40bf-3e5b-b468-23a6221da363 | -12.90424 | -47.95325 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d2618c2-b424-3362-8c28-1854e2921ce5 | -12.56921 | -45.67409 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4e299a1-4e25-3cac-acc6-3507087be099 | -12.91132 | -47.95955 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db2e836a-a477-336e-8e61-93273597389e | -10.62163 | -52.32658 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 289d80fa-70a6-3525-a091-e08402ce0ea8 | -11.48355 | -43.70042 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c49dece-1169-36e2-b958-0fc4f8153fa4 | -11.15879 | -45.23816 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eeeff73-9954-3678-98e1-82a300d673b1 | -13.14343 | -47.13313 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9b23f54-1cd8-32f6-ba4e-1282ff09fc5d | -11.14538 | -45.23187 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fd91bee-2f96-3f1f-aef6-d03b84a7e2f1 | -14.28324 | -46.07161 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d74b87b2-2adf-30e8-bd30-207efb9f8e04 | -12.9525 | -48.00535 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0f59c738-0dd8-3fdc-aa5a-5bd726ee8094 | -10.50028 | -51.54022 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48bd6c39-aa3e-32b3-ac27-9ab3abc96ee2 | -13.00079 | -46.74928 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8603d28-8e76-3132-a479-0d9ed7fdc922 | -10.36633 | -50.50082 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09dc612a-73f6-3e7d-83b5-ead6ffd0078e | -10.65707 | -46.29234 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d340687-ab64-313c-919d-55e0c4ef6a2f | -8.49294 | -45.13327 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b507776-c37b-3b68-8f7e-e9d99b295a14 | -11.84258 | -50.5746 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47a6b2b4-e5eb-3a36-81b1-f82f877d21c1 | -11.48899 | -43.62421 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc770e92-cf8e-3d11-b527-362b641484f7 | -10.72648 | -48.61928 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fd94f5c-5bee-39a0-85e7-0e78f4d92fa2 | -13.90123 | -48.2933 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38e83a04-a520-3c67-8a38-aba1c95a22d5 | -11.15732 | -50.70956 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 31788273-0a57-3e9a-95b0-c69e8c6ace91 | -12.79873 | -47.98098 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7a5d3cb-df7c-3656-8aff-dd3a0be2161f | -9.6378 | -45.88778 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b275106f-f1a0-377c-adbb-7817c368e8cd | -13.95157 | -48.18281 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6dc3d81-38d7-380e-a97b-ff2eac57848f | -12.08833 | -44.89809 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fafb31e-bb9d-3d7c-aaf8-30255dd2fa5d | -11.20676 | -48.41472 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 234090f2-fa0b-399d-b989-897b722e7f7a | -12.08397 | -44.8816 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a430d2b-8110-3679-af32-4b55830a4a26 | -8.24408 | -44.35969 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f5bf337-36df-36ad-a710-e9b758a83969 | -10.51627 | -51.53879 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0171f00a-481d-3acc-942b-96dde92ee4ce | -11.41104 | -50.73989 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9437ff55-31f8-3f0c-8206-864d5e52e12e | -11.77157 | -50.55516 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ecddd3d-dd68-3071-baa7-42d9ad3c3091 | -8.42945 | -47.24199 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1ee39ae-ad9f-346b-8256-cdc2297a6b5d | -12.11708 | -44.85171 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 944232fd-1dc9-3529-9a5c-43cfdbe1021b | -14.13274 | -45.37168 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a155a094-d30f-340d-a85a-76ef15e36439 | -11.17391 | -51.41375 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c21caa00-4c7f-3f1f-ae8d-cedf6d5303a8 | -11.85218 | -50.57649 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88afd9cd-a6bc-32ae-bbba-c1102e963c29 | -12.99765 | -46.75538 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aca5741a-5aab-343d-93a4-564db076bb51 | -14.22242 | -46.30226 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f86143ab-e05f-36b2-899f-df82fb5c6542 | -8.08813 | -44.51606 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61b89545-12d8-3edf-ad3f-c490e2aaefdb | -9.73868 | -46.89525 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60c25529-d995-3501-9c36-ff57fbba565b | -11.856 | -50.58278 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5a7f204-8472-341b-8313-2932ceed5925 | -12.0849 | -47.57457 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3564b90-bdac-3e46-a245-932382980017 | -13.26432 | -43.74195 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8afd4018-ff98-3a6b-aecb-ed5c5267d23f | -11.38087 | -50.75503 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 246fc2eb-ca17-3a46-9f1b-6d1067f54abd | -12.11085 | -44.89001 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 847a45f9-be74-337d-a7a9-1bff0037c592 | -14.42916 | -47.3183 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee66530e-2baa-3712-bacf-263eeb284983 | -13.28925 | -43.77554 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 350e013d-e866-3f5a-a99c-a31df9a380f0 | -8.0958 | -44.51329 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 722cd6d9-2660-3c26-8cc3-bca2c6c96f52 | -10.50931 | -51.54679 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e76deea5-4cbb-3347-a0a3-a6bc4b078388 | -12.98964 | -46.73503 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41138543-c16e-343e-ab62-aefd6b8fc1fa | -11.4271 | -45.60981 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a965635-3a2d-30e4-96df-37567a678834 | -12.91149 | -54.7535 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd0b503f-5373-369f-9141-3a432f4538be | -12.13195 | -44.82207 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39dfa2d0-2a1a-355d-9c69-3de0dcf8db86 | -11.17705 | -55.08986 | 2025-09-13 04:08:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6bdadc5-7599-38b3-8af7-587e89c7b0b0 | -11.3984 | -43.53317 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55587946-ddc6-3d00-be50-321dfd79ac33 | -9.89108 | -51.86429 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fef04aac-2848-302d-bdda-83aa7b01c693 | -11.78528 | -44.28662 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f741465c-d3be-348a-80a8-b2b9b31f8895 | -11.7668 | -51.50857 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 550cc9b5-7985-3592-a482-eed2a7a56320 | -11.18359 | -51.41889 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dc7d4411-c6f8-38cd-a60a-012a2f6416bb | -14.17483 | -46.23744 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README61.md)
