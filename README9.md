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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d36500c-87d7-332a-9e78-2aedf792844b | -17.31016 | -42.64301 | 2026-06-06 04:25:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb443d0c-c6b0-3466-b900-87b0cafc395d | -14.76855 | -52.67788 | 2026-06-06 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 963509db-6d84-3d8c-bdf0-a200dfc2fd5a | -14.24537 | -58.4409 | 2026-06-06 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccd7b3aa-b328-3440-aef0-9c2da15069d1 | -12.50225 | -46.29707 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 089dacf5-221a-3fb4-9e26-55988c8ba939 | -12.52567 | -46.27885 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5788433-3427-3c3c-915e-f7eae62f5025 | -18.86803 | -47.64376 | 2026-06-06 04:25:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a82e2256-f94d-3ba2-9865-795ea00ebd2f | -15.45933 | -55.85726 | 2026-06-06 04:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd471dd9-d1d8-34f3-8d3e-9615b3f4ad1b | -11.04826 | -56.92741 | 2026-06-06 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87b89e44-bc68-34d7-916a-f19bdd8661f6 | -11.90533 | -57.03417 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b14aeca-9d13-3842-81db-9919f455a228 | -12.38223 | -48.12717 | 2026-06-06 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18441ace-f0d1-382a-a27d-97b56a9d6b65 | -17.31609 | -44.91697 | 2026-06-06 04:25:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e647fc48-fd01-316e-9626-533d11bca2b2 | -10.57205 | -57.32307 | 2026-06-06 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f4378f6-6bba-3f9a-9d19-eee830b0bc3c | -12.52679 | -46.27181 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b22e3849-c288-37c0-8646-914cd4efd373 | -11.78296 | -56.99778 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58fe5ed3-9675-3e9d-ab2c-3d6a00b0fc15 | -19.43581 | -42.56814 | 2026-06-06 04:25:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fc618d46-8c58-3eb6-b588-353e113e84f6 | -15.80699 | -41.64207 | 2026-06-06 04:25:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f10cc85e-c78f-3941-8882-a27b7cc09a78 | -14.2298 | -45.80506 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62efb901-5277-33f5-9f48-5ff8924eea51 | -11.72464 | -56.83719 | 2026-06-06 04:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ee42a1c-84c2-33e2-b93d-8a6b595a8802 | -12.4995 | -46.293 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 926a9078-99fd-33cd-9af5-372bc77b41bf | -12.79951 | -54.86694 | 2026-06-06 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a0aab39-f0fc-3f0e-9a41-7955ce508a77 | -12.50907 | -46.29779 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afd10627-66e8-338f-a56a-0a2f968fb6c7 | -12.51294 | -46.29482 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afa03400-0813-3283-b73b-9942e25b51a7 | -13.95348 | -53.96497 | 2026-06-06 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eada830f-e251-3f5c-b0d9-41ca9cf3aa8e | -12.7726 | -59.00418 | 2026-06-06 04:25:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56115eff-93b5-3bef-8353-fbb22e21c540 | -17.3024 | -42.6418 | 2026-06-06 04:25:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98edca06-e487-3732-9e2c-322e0e2a2612 | -14.39456 | -45.57415 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 815afbcf-bb6a-36b4-9357-9daeac868845 | -12.38567 | -48.12773 | 2026-06-06 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2954aa40-5a73-3320-a7b4-52539b147015 | -13.36134 | -43.20225 | 2026-06-06 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 13635469-726f-3c24-a94c-84249e2197d1 | -12.50689 | -46.2902 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 281ac62b-eb5c-3ebb-a945-81498bfcc225 | -14.77278 | -52.67881 | 2026-06-06 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c237f115-1d8b-3f8c-aaf1-d2c0186574ab | -14.37955 | -45.56061 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ff3f716-9c19-3c34-aee3-fc267eb367be | -11.55422 | -52.79625 | 2026-06-06 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f243dd5-669a-37f1-819e-2e4b213c8df9 | -12.49894 | -46.29652 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27c22968-7a26-3275-b094-1f3ece339edf | -16.59788 | -58.23315 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c5d5922c-d836-35a8-ba32-fd47554e3c6f | -19.43654 | -42.57172 | 2026-06-06 04:25:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b9285e3d-a14e-326c-a7a4-cda3087e2a31 | -14.69722 | -41.35854 | 2026-06-06 04:25:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3c17de75-0e1e-3991-8022-bf464ad6cf05 | -12.29156 | -57.38288 | 2026-06-06 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6da671c3-4e3f-3393-9f33-90f3c246779c | -12.29064 | -57.38743 | 2026-06-06 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2002cf68-33b7-3728-b9bd-0b2045d2a14b | -11.26614 | -53.9632 | 2026-06-06 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c8aebfb-7570-34b7-aa60-6405df17de88 | -12.79892 | -54.87001 | 2026-06-06 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 304fb4e9-2053-352e-9594-85ffe7cc9551 | -14.22093 | -45.79628 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df88b976-ee6a-3a12-984e-83d59b77be0b | -14.22647 | -45.80453 | 2026-06-06 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6465943d-1a2c-38ed-b96b-5fcbfa6ba35b | -16.59932 | -58.23429 | 2026-06-06 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4e3f329b-71f8-36b7-884f-fa402d18104c | -12.52348 | -46.27127 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23c4c019-3dc7-3d66-9bda-e2c480cbe906 | -18.00042 | -54.2822 | 2026-06-06 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9afac08a-ae50-35e3-b098-0697cf95e2a7 | -12.50504 | -46.27944 | 2026-06-06 04:25:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f93d23b3-6c9b-33ae-9f8c-cfecba77e6e2 | -21.52145 | -48.62173 | 2026-06-06 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34b04d98-69a3-3303-a9cd-1bbf416be9e0 | -21.34842 | -48.62121 | 2026-06-06 04:27:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 166833e8-db84-3863-95a6-0816f79da410 | -22.38402 | -49.78912 | 2026-06-06 04:27:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3462c4f3-9409-3236-906e-2589dbefb5e0 | -21.40934 | -49.22704 | 2026-06-06 04:27:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 57d063f2-bee7-3509-8b8a-2129967c1324 | -23.73384 | -54.60733 | 2026-06-06 04:27:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7af26b8d-49ed-333b-b68b-0aa085b342c0 | -23.05342 | -47.13839 | 2026-06-06 04:27:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2e01e348-4116-3e0d-a123-1d94afef62bb | -19.74594 | -53.54482 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 155786e4-488a-32be-b1d5-b9ae7cbc6bf4 | -19.74356 | -53.5447 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 41efde32-146a-30ef-a8ed-4fb2f60e7180 | -27.1944 | -50.47261 | 2026-06-06 04:27:00 | NOAA-20 | PONTE ALTA DO NORTE | SANTA CATARINA | Brasil | 4213351 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5a70dfb2-6f76-354f-8baf-942bda45316b | -22.17051 | -50.38368 | 2026-06-06 04:27:00 | NOAA-20 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0632af8d-5c16-35c7-90c3-9a4dfb38c824 | -19.75003 | -53.54576 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7215524d-7270-3161-a2d5-7b1c2fcc8e12 | -23.25542 | -55.08042 | 2026-06-06 04:27:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 274a28d1-665a-3642-9894-c3e3f9d2b721 | -22.59891 | -46.82857 | 2026-06-06 04:27:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a495bb9b-f96c-349a-bf15-45bb6cbabb25 | -19.74517 | -53.54876 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bcc47bf6-3554-3c84-9459-e8b96aef960e | -21.34783 | -48.62491 | 2026-06-06 04:27:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45da35af-91f7-3f9c-9e45-17e81a0f276a | -22.89899 | -49.18583 | 2026-06-06 04:27:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58b89c37-8990-3faa-910a-0ffc2dfd1cdb | -22.80506 | -49.34253 | 2026-06-06 04:27:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 887e0c8c-a76d-37c4-a6e4-044d75a50881 | -19.74926 | -53.54974 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 76965a61-c36d-3468-b18f-5051a981c141 | -19.74282 | -53.54865 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a2941e0-08a5-372d-b445-c749f23d4bf8 | -22.99774 | -49.55765 | 2026-06-06 04:27:00 | NOAA-20 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4a5a4a0d-5f94-3ae0-8066-4639d97cbdfd | -20.77532 | -49.21632 | 2026-06-06 04:27:00 | NOAA-20 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b8e23318-4c21-3af8-a29f-85ae77b60b42 | -19.74691 | -53.54961 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 17120a87-c147-369f-93a8-221d8287013d | -21.983 | -57.60768 | 2026-06-06 04:27:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4059224-6e72-3382-a964-3b265be4f955 | -22.17392 | -50.38437 | 2026-06-06 04:27:00 | NOAA-20 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3375a3c9-c406-302e-925e-a671f3aeedfb | -21.42302 | -48.64202 | 2026-06-06 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5637a3c6-3822-352f-89c4-d6cddef93a97 | -21.986 | -57.60668 | 2026-06-06 04:27:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8605b546-0193-3d0c-9b4b-bd59f1ae5825 | -22.79718 | -49.34879 | 2026-06-06 04:27:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 816e8884-a106-364d-a818-8570b974d4b0 | -19.74107 | -53.54784 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef7c38c5-e38d-3363-92c4-6c507097234d | -21.406 | -49.22641 | 2026-06-06 04:27:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a331e655-0731-338e-a626-164a11613e69 | -23.48416 | -46.55701 | 2026-06-06 04:27:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 64d68d98-470d-31b2-b7da-0c80fb69242b | -23.72977 | -54.60637 | 2026-06-06 04:27:00 | NOAA-20 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7d4e43d9-2c60-3e26-a223-f6f323155bba | -26.54831 | -48.85225 | 2026-06-06 04:27:00 | NOAA-20 | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f262b1cd-9ea1-3468-97ef-eeeb0b715939 | -21.52476 | -48.62234 | 2026-06-06 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5c0910e-f69c-338c-8af3-37b6bbe93b2e | -22.9386 | -43.64893 | 2026-06-06 04:27:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3dcf760e-7a71-307d-970a-2b34f2845873 | -19.74765 | -53.54563 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9263ee45-c514-3658-92a6-0104ff1770d0 | -23.82092 | -48.70875 | 2026-06-06 04:27:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab9ab093-8377-3e70-a8a3-cf434fbb3ce5 | -19.74183 | -53.54393 | 2026-06-06 04:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3839b2ea-c9ab-3bad-b00b-5aef01fedd87 | -28.61097 | -48.94936 | 2026-06-06 04:29:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c71312b-6571-3686-b756-1b1a610cd1a6 | -6.45162 | -44.56124 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64348146-f381-38ff-89f3-33db08dec672 | -5.34928 | -45.18697 | 2026-06-06 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30755e81-59f8-3eb5-944b-1b93a118ec60 | -6.44128 | -44.58902 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91ea8d99-4109-3ab2-af98-9b2d0517e971 | -6.44197 | -44.58356 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 101b501d-c5a1-39fd-87a1-6746707ec2fa | -6.72589 | -44.37421 | 2026-06-06 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b3887c46-59f8-35dc-8a91-a920933bfb49 | -6.72156 | -44.37148 | 2026-06-06 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ae878ae-c321-3d44-b1be-058e751c56d0 | -6.44698 | -44.56767 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 66c15f81-943f-3548-8fe9-2340c9675d87 | -6.72832 | -44.37265 | 2026-06-06 05:10:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f518867a-84e7-35f2-b969-10f82b55be4f | -7.24376 | -49.67109 | 2026-06-06 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59de30a2-54fb-3e54-be81-b7d4e4b265d9 | -5.92947 | -43.48384 | 2026-06-06 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0082abf-d18d-3017-9758-05cf3cd2ec59 | -5.81017 | -43.79512 | 2026-06-06 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ce42cef-6b62-397b-be6e-ae8cb0eef3f3 | -6.43607 | -44.57648 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d66164a-fc13-3415-a234-8584e53d2c4d | -5.93038 | -43.47701 | 2026-06-06 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8f618f0-1c8d-360e-9ce9-e278b25b3d97 | -6.43797 | -44.5841 | 2026-06-06 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a75e4661-5ec8-341f-9073-cc443eb4c39a | -6.04779 | -47.89294 | 2026-06-06 05:10:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e096f86d-3313-3562-9a92-b69e599e1989 | -6.05317 | -47.89378 | 2026-06-06 05:10:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README10.md)
