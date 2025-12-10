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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fffb0c90-7636-36fb-a740-3240e84969f7 | -1.75852 | -45.51335 | 2025-12-10 04:06:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4447983f-5444-324a-95b9-cefc36b29792 | -3.40232 | -42.46424 | 2025-12-10 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab3d6fe4-1978-3790-a0ec-55986c3490e1 | 3.38167 | -51.26393 | 2025-12-10 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5347934e-686b-372b-968e-e07d2c8c2764 | -2.51939 | -45.022 | 2025-12-10 04:06:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df172a53-8498-3a5d-b7c7-76f9752052b2 | -2.91612 | -39.93209 | 2025-12-10 04:06:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 81ff9642-b19f-3ad1-bab7-3fd15f855b22 | -0.84696 | -48.11094 | 2025-12-10 04:06:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65979f8e-d1b8-30dc-aa88-4d52a7a36071 | -3.52989 | -43.479 | 2025-12-10 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a30ce321-3ffa-3ffa-9189-8bc7f8cc432e | -2.48525 | -47.77856 | 2025-12-10 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 6f512d91-c033-3ede-b21b-1e0d53be9e35 | -2.26697 | -46.08842 | 2025-12-10 04:06:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99ca32c6-27f8-365b-95dc-9299475c8a01 | -1.08582 | -47.26602 | 2025-12-10 04:06:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6182cd13-1f2f-33ac-ac3e-09f7ad4fdda4 | -2.2942 | -46.1042 | 2025-12-10 04:06:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fb399e2-9396-3fed-b1b2-3759121a932e | -2.91813 | -40.35439 | 2025-12-10 04:06:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff926d8b-4003-3a3a-928b-b0d65b410f04 | -4.16407 | -40.6524 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 770b1df5-33b5-3c9d-87a4-0ae7de5aa9fd | -2.48603 | -47.77372 | 2025-12-10 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 57ec297c-ceb9-3eb7-bd52-5e9894fc339c | -4.16184 | -40.64498 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 480b4886-26c6-3116-93d9-0760b9f88eb8 | -3.122 | -41.09434 | 2025-12-10 04:06:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89455df9-bade-350c-955a-caa28d357985 | -1.5884 | -54.12064 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e0171c17-897f-31b3-b12e-b8236eae1bdf | -4.16738 | -40.65292 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 56e939cd-9a59-3105-9205-b8ab59c244bb | -3.4664 | -42.01729 | 2025-12-10 04:06:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d37a7e48-6241-3446-af31-fc7da7e3831c | -1.42078 | -54.28969 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ca1c409-7d2b-3466-adf9-6d4af0f459fc | -3.96624 | -41.52464 | 2025-12-10 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0914c001-23a9-3261-b816-ea4a46c028b1 | -4.15691 | -40.65485 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3b81596-9add-3b8e-83d4-8a377c723ea5 | -1.41686 | -54.28897 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90593bcd-5d29-3ec6-8a0f-77328b6eb7f3 | -3.39477 | -42.1076 | 2025-12-10 04:06:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| b06e887e-30ed-3f06-9dd9-abb1732e9360 | -2.19695 | -45.07762 | 2025-12-10 04:06:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97c9976a-4f82-375d-9d51-2cc7c8af4f9c | -2.9405 | -41.14666 | 2025-12-10 04:06:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27f031ba-c609-3c6d-8803-0601657ec9fe | -3.23648 | -42.05045 | 2025-12-10 04:06:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd62174-9c96-3db8-99ae-3b57901c00ab | -3.68496 | -42.03385 | 2025-12-10 04:06:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11cc6ffb-641f-327a-94c6-4dfe37848b7c | -2.42067 | -48.2697 | 2025-12-10 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f848ff2e-6637-3e61-9522-6d7b4a991215 | 3.37758 | -51.26794 | 2025-12-10 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05bfe187-4816-3c90-82d2-ba8870bbb48c | -2.79668 | -47.34645 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 582f0f70-e8df-3271-b7b2-a3ef77271350 | -3.43886 | -41.65424 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2a7f1436-d0d8-31f4-887d-4bb836d347b6 | -4.13106 | -38.13186 | 2025-12-10 04:06:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9375cd10-65c4-33b1-8869-e09bcbe8fbf1 | -3.58326 | -41.66602 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 356309ce-7141-3bff-8572-0163a8b66ef0 | -3.06222 | -40.08634 | 2025-12-10 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0b150d0-94ec-384a-bec2-a23774066833 | -2.35958 | -46.13348 | 2025-12-10 04:06:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 265f4c6a-4513-37e5-95c6-f6c041130660 | -1.84849 | -46.39669 | 2025-12-10 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b39f477b-12a8-3a11-a58b-655249c900c0 | -2.52014 | -45.0172 | 2025-12-10 04:06:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dadccc0-e8a1-3fb1-9116-4d55135ed7f2 | -1.01706 | -53.73243 | 2025-12-10 04:06:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8c53d88-bc46-34ab-b505-22d83ca84535 | -3.43941 | -41.65076 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 28b9ea73-1b8f-384a-a380-54855f86ab98 | -3.68162 | -42.03333 | 2025-12-10 04:06:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b02fdd0-1da3-33b7-b94f-142073af2530 | -3.43566 | -40.83059 | 2025-12-10 04:06:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b38e8f93-1d47-3095-8306-7f6a4db55522 | -2.79987 | -47.33958 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42b8fe4e-f938-3b8d-9b9f-c43b20caa8dd | -2.86232 | -46.80683 | 2025-12-10 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dafb8c21-2f94-33ac-825d-1d580b1a6849 | -2.90708 | -40.03399 | 2025-12-10 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29a88a36-201e-3535-ae05-1c9a36302fa4 | -3.43897 | -40.8311 | 2025-12-10 04:06:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c4c5a04f-8500-38bc-82ca-64536d47abb4 | -3.33625 | -40.98684 | 2025-12-10 04:06:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 41f657f8-5084-3b73-85f5-4f88799c5577 | -2.80223 | -47.35368 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f1a2c42-6af3-30f4-8aa4-a2282c8a3870 | -2.80189 | -47.34277 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e337552-e511-3d0a-854f-16b08c08c53b | -3.43166 | -41.65668 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9bb02920-764a-38c9-83fc-d1876cf57382 | -1.67444 | -45.77909 | 2025-12-10 04:06:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1df75f2a-211c-3496-a131-319470319b29 | -3.9563 | -41.5231 | 2025-12-10 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a368bccd-8fb5-369f-903b-1e816c2e7c37 | -2.50247 | -49.22314 | 2025-12-10 04:06:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c08800-310d-3770-b310-61aba351e672 | -3.58723 | -42.60497 | 2025-12-10 04:06:00 | NOAA-21 | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 814faff0-7061-35b4-83ec-1f4d3773ef87 | -4.49332 | -38.43737 | 2025-12-10 04:06:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d818e081-6c17-3d1e-bd58-d1d6b390372e | -2.46649 | -43.30254 | 2025-12-10 04:06:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefe915b-87f3-30b9-95ac-c3e3d18a2713 | -2.79846 | -47.34845 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1624474f-d224-38dd-af5c-24d258ab4e30 | -2.21822 | -45.66975 | 2025-12-10 04:06:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbaabeaf-29ac-3a73-a698-e747dcad8340 | -4.15745 | -40.65139 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f499b852-5f68-35d6-844a-1ce5d995e3e4 | -3.42834 | -41.65617 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a0d54f0-5051-3bb8-ab84-b4286daa8e16 | -2.48988 | -47.77935 | 2025-12-10 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b520feb5-f4e8-34fd-b066-ad622f77a0a5 | -3.88832 | -42.29812 | 2025-12-10 04:06:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09d62ceb-c73d-3283-80f9-7e9991848948 | -2.41991 | -45.8413 | 2025-12-10 04:06:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16f2c399-a3db-3c7b-9495-c8991bd17a8d | -3.96293 | -41.52412 | 2025-12-10 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 179c0235-2037-316a-9a3d-512c549908dc | 3.37605 | -51.27004 | 2025-12-10 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66eac053-163d-373b-b77a-d555d7be6b25 | -1.73591 | -46.50698 | 2025-12-10 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4c8b428-5e51-3da0-8cf0-dcd2052da0eb | -3.06563 | -40.3914 | 2025-12-10 04:06:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 30874252-ce67-3c2a-abe5-f2d5596b7df1 | -2.88679 | -45.2439 | 2025-12-10 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf58b532-a133-3c1b-8390-0a7f11e29171 | -2.37164 | -45.64811 | 2025-12-10 04:06:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f0a6ca8-f77b-3586-89f9-3a09e02f15b0 | -3.96016 | -41.52015 | 2025-12-10 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 868d722b-42ab-3674-9eef-e48698690bc5 | -1.73528 | -46.51105 | 2025-12-10 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d99d354-1044-3a9c-b793-ed66ac665371 | -3.66401 | -43.55145 | 2025-12-10 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f5f3132-ff7f-3baf-9759-acb3d180e789 | -2.08325 | -52.04924 | 2025-12-10 04:06:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9105fa81-50f3-3ab4-9542-934f4972cb9d | 3.37832 | -51.27314 | 2025-12-10 04:06:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36db5263-69e5-31e4-a864-ea30ed53424d | -3.42502 | -41.65566 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3bc5f2ec-7387-3d61-8466-df9d9a05f1a7 | -1.59139 | -54.11796 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84b24fd5-b73d-39c2-b32c-12ed43498892 | -2.38967 | -45.82184 | 2025-12-10 04:06:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d7a2d82-cecb-3709-802e-3a5eade86039 | -1.41584 | -54.29498 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60447c8d-4a11-3ea1-899d-6a2b384eec57 | -2.80293 | -47.34921 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fca3b2b0-26f2-3e9c-90db-bf04d72e5df5 | -4.15522 | -40.64396 | 2025-12-10 04:06:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e49c963e-c471-3a13-94b5-2a26e4e4282d | -3.44273 | -41.65127 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 69cd57f7-5b4c-349c-a088-007ff37314f0 | -2.80115 | -47.34721 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc8f8c13-8155-3f66-bc06-ec4ade650c82 | -1.47137 | -54.20407 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 450dddb2-23eb-3c5e-abce-36069c6f28aa | -2.37567 | -45.80495 | 2025-12-10 04:06:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aabacc77-fcd6-3005-a8e7-08bbcdee8875 | -1.47507 | -54.20504 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30490229-9779-35de-8ae2-7859ee5901c8 | -2.85405 | -46.83075 | 2025-12-10 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f553942-45dc-38ab-a6a5-b16fbc64f634 | -1.41982 | -54.29556 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66867fec-3f01-33e3-b299-1c85e0d9b171 | -1.40373 | -45.95379 | 2025-12-10 04:06:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e798db51-ee53-34a4-95d0-1224a82af323 | -2.19759 | -45.08 | 2025-12-10 04:06:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e97535a6-6bca-3201-8a51-196fc30c3ed1 | -1.47845 | -54.20539 | 2025-12-10 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7af677a-9365-3622-95f7-d106e18ded31 | -2.2615 | -44.61538 | 2025-12-10 04:06:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fc64bc-11d4-3915-a55d-33bcf4599b8e | -3.43996 | -41.64728 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 36612631-7592-3fa1-a68e-961ec48b39a8 | -2.15108 | -47.36684 | 2025-12-10 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1704ef37-21c1-3e8c-a6a9-b85d7e994347 | -2.79916 | -47.344 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09efa022-fadd-3350-ba8c-79272de4538f | -4.34227 | -38.50328 | 2025-12-10 04:06:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ff97a9e3-478d-33e6-af53-507136b47e22 | -3.65987 | -43.55479 | 2025-12-10 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a25a02dd-2b23-3c9f-a673-f2bf30003c2a | -2.52152 | -45.01987 | 2025-12-10 04:06:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 15bbda50-36ec-347c-b1e6-05baf3e7a961 | -1.53272 | -45.78285 | 2025-12-10 04:06:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1cba16f-ab6b-3b66-a25c-ae6e3efba11c | -2.44232 | -45.60221 | 2025-12-10 04:06:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d80c5ee-0699-34ae-8d12-1f50620d9577 | -3.58658 | -41.66654 | 2025-12-10 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README5.md)
