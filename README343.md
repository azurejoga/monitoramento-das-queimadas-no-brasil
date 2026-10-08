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

## Dados Diários - Página 343

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c40a7cb2-3485-3359-8fe2-957c4582872a | -5.72711 | -41.64098 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.1 |
| c7462c91-f929-303d-ba03-48050a2825b7 | -8.29671 | -45.74001 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 34acb030-d9b6-3d51-88b1-3e960aac383c | -18.98723 | -40.64827 | 2026-10-08 16:37:00 | NOAA-20 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 696f2ab7-1055-3bca-81ec-24ac9e369de9 | -7.46062 | -42.83034 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 414a4e1a-e7b3-3f44-a8b7-926c94088c2e | -11.59652 | -43.67489 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 7e6dd624-e110-395f-8966-963d6c9f1e19 | -6.16903 | -44.85574 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| cae581a1-2e08-3f0e-8f8c-3eed4a696841 | -10.67266 | -54.53152 | 2026-10-08 16:37:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a87eafbf-b614-3c15-9723-60193bd8ff5b | -12.62034 | -44.54501 | 2026-10-08 16:37:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fafaa23c-3628-3af7-8906-a79b44e4e0d7 | -6.97976 | -47.67439 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 20b21324-0fee-3a44-9190-ed0ea49740ff | -11.33917 | -46.6939 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| efe4589b-1707-357e-b978-31fb545b5b9a | -7.5642 | -46.70873 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a04345df-47a2-3072-a4f2-c6934a995c67 | -6.43223 | -44.82767 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f1defe7-5f23-3256-9fdb-d1f287c61ac2 | -12.13548 | -43.31868 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f31bfaa7-ff51-3343-89f9-fd36e4f0078a | -9.23081 | -45.65894 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a7d6db72-b9c8-3085-9cc2-1d0d3c3337cb | -7.40782 | -44.74732 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| bd846db9-212b-322d-9448-a3fca545df5d | -9.77722 | -45.88427 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06ab9ec9-1903-324f-a441-c75208ac2436 | -11.07751 | -44.02729 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5a62da6e-ae97-3e5d-8ee9-26513e8310bd | -11.58983 | -43.67595 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| f428661b-722c-321b-b8b4-4ec9202e4994 | -8.60194 | -45.62706 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5dc54a9c-3c85-31f9-8291-d449a982d67f | -8.94953 | -37.58985 | 2026-10-08 16:37:00 | NOAA-20 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| cb659fa4-5fc2-3e93-b672-e9694bb8a8b7 | -12.32262 | -45.26617 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19bd5557-a377-3193-ae01-7c2a9e935434 | -8.93202 | -45.19019 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| dab8d36a-25df-386e-9011-9dcdb5369844 | -8.96004 | -45.14988 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f1ba019f-db53-380e-8b20-6d9a88070143 | -9.53068 | -45.62224 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1c056913-2fb5-3ad2-b3be-5c748fb0d02d | -7.48677 | -42.79336 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 6b42b302-051f-3766-a531-fb4222f2ef66 | -12.22699 | -43.92947 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 03574e50-c6d5-3572-b92b-d684dd37428a | -10.79321 | -41.22256 | 2026-10-08 16:37:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| d55b6561-b313-3a6a-b97c-470066e41e7c | -9.51153 | -46.84649 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe98e2fb-4ea1-3f6e-9bff-2cc75ead1279 | -10.75655 | -46.60761 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 164b3278-c362-3417-9e48-7e34706c8503 | -7.76239 | -44.16751 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f0ce2752-beea-337a-8d02-4e1ba3e112ab | -11.26831 | -45.20304 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ee629bf9-55f5-36e9-8ea3-592e7b07047d | -6.45212 | -46.01675 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cee8b236-c6aa-3b4a-8b29-09e23fbc75d0 | -9.74741 | -46.95034 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d781423d-c36f-361e-9d62-ea6ec4086e08 | -6.2245 | -44.97717 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3fbef398-6c1d-39ab-9207-f183300a78d4 | -5.87172 | -38.8588 | 2026-10-08 16:37:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d98a70f2-b845-386d-bcd1-b8ccf5b0cdb3 | -7.4732 | -42.84074 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| cb5bdb6b-3340-3cfd-a9f7-3a48323d794d | -10.36369 | -42.48413 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 105c575d-f78b-3753-8686-64fdf7174a44 | -7.40168 | -45.65575 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cf45643c-2564-32f7-8c06-c68f1e35a735 | -6.834 | -39.55974 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| dabdd8ff-4db0-3783-b0d9-52df44399001 | -9.50974 | -45.61831 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e3f1dea8-b3c3-3b32-893e-87c945f257a5 | -19.36262 | -40.35136 | 2026-10-08 16:37:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 971c8960-c19e-33ea-b98a-6380a54e2183 | -8.67671 | -41.18679 | 2026-10-08 16:37:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 734d530f-448f-3dbe-9561-cf4309cd5193 | -6.95084 | -45.28363 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 717ea69e-943a-3dcf-bf94-55955cf4fcc0 | -11.0764 | -44.02019 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 05d0534d-949b-379a-bc16-3f207118a05a | -10.43381 | -47.28802 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4487fa6a-6771-340b-83bd-9b1c1f2b6369 | -10.82906 | -57.18055 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 14af6402-a7b8-38a4-afaa-50a1f8070e06 | -8.0818 | -45.62133 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6b0f082-06c4-3f9e-89ec-8957a185e1ae | -8.69386 | -45.27437 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e164cb20-11a8-3d51-9bfb-2aee30d63c07 | -12.41161 | -39.07854 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 65f7a3d9-e681-34fa-803b-4e410f38daf6 | -10.75709 | -46.61132 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 399f9189-d563-324e-988c-54d9d5162ea3 | -9.82076 | -45.67922 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 505aaf63-95dc-3c39-bb1b-951a881dec58 | -6.31675 | -35.12692 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| cd7f95ab-b1b7-3066-ad8d-a72023afad3d | -9.34474 | -37.20644 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5b5cfb0-ddb3-372d-b84d-bc01d4ef138d | -7.18568 | -44.26341 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 56284c2d-08fc-3495-a2ba-fc6ceb786d1b | -9.8882 | -46.10552 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab8c045f-e1d9-30ce-a29c-e13e1f957c09 | -13.1267 | -46.36617 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| be509924-938b-37d3-b825-124e13eaf06d | -7.10557 | -42.52907 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 89f02d2c-819d-33ee-9c7f-ef72df4189c8 | -12.21498 | -44.82391 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d2c4f319-f64c-3627-8933-30521d79699c | -5.25311 | -39.09878 | 2026-10-08 16:37:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| fd6db393-fb4b-3c41-a7ff-2159b010d9c4 | -18.05923 | -41.49826 | 2026-10-08 16:37:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0c687af9-399a-3bd4-98c5-68587013c83a | -12.19181 | -44.82755 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| cd147bcc-7409-3041-a36e-59d985647328 | -6.6764 | -45.3746 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 94ae8824-a3b9-3288-8cbe-bb2c4a2a915a | -6.53051 | -45.39743 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| d77559a2-dae8-335c-bb99-3ee56cd04428 | -6.33352 | -44.86891 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a9e5ac5c-6535-3c34-9376-830aaf82de87 | -6.67362 | -45.37858 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 15c756d6-5e95-325b-ad36-e19997871fcb | -8.93917 | -45.19265 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 4078b39e-f303-3b3a-982c-9d204a31663d | -5.71038 | -41.75754 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| b9f4416c-59fc-39d4-af3c-2b287e809e76 | -8.06525 | -45.62387 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2edf6fb-6173-36c9-aa0f-c3a4e0e2ebb7 | -8.32352 | -45.02781 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7a063424-63ed-3ae2-bc7c-cc4df73dcb25 | -9.93945 | -43.56819 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9091f14b-b21a-30e5-9ac9-ac689937f671 | -9.02922 | -44.36577 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2fb47145-86bb-3fda-ab8b-96417ac51cf9 | -11.31246 | -46.67852 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6975347d-0f13-3526-95d6-ab87ed2de96d | -8.90627 | -50.5978 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c88c78f-3b76-3774-a11e-7e2b76f99172 | -7.00011 | -43.97799 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90498010-53ce-3743-9949-4319e800aec8 | -8.60846 | -47.98756 | 2026-10-08 16:37:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa8e7485-20ae-3277-a0a1-d90ad8d6660f | -8.78578 | -47.25858 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1cfb1d5c-e050-3505-9d2c-4a994f9c29f2 | -6.45596 | -46.0197 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 93184a0f-8df6-3b9c-9cd2-08c5f42611be | -7.54342 | -42.08392 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 6f889a6b-1182-3ec5-bbaa-a4752016f4a2 | -8.29844 | -45.7291 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 8dc5d7c3-ca41-3f71-9095-f1e08e9ed999 | -8.19146 | -46.36796 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8bd5ba9e-a69a-3ec4-8189-e25305235efa | -9.36491 | -45.93887 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| de9c1905-fc30-3713-81a6-c521864b05bf | -7.76352 | -44.17475 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5ec4a9af-634c-372d-8c84-3b351459ec17 | -11.08139 | -44.03032 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| ebd624e7-232d-3003-a64c-3300122b8576 | -10.18569 | -51.59338 | 2026-10-08 16:37:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 182174de-46e4-3c1f-b8e2-772886352fef | -10.74368 | -48.54694 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 20b149b9-e28b-311e-833d-d5b025fc18a4 | -5.96707 | -43.89262 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 95b8037e-2ce3-35ed-a79f-d283e139cfe8 | -3.78407 | -41.67242 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| e6042f29-e2e5-3cad-b244-1811ae280049 | -4.63427 | -50.95667 | 2026-10-08 16:39:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 43027c03-59d5-3864-9dee-983a47d0445c | -3.74286 | -59.61615 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6b29bd93-5b8f-3051-ae7b-da7a5ab12643 | -1.52449 | -54.81455 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0faba9b7-ce9e-3855-a845-63ea580b298b | -6.16034 | -52.64416 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 94efd4ee-ab3f-3e61-9712-f4562d5ec595 | -3.00897 | -54.79167 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 369f1a52-1bb8-3f32-8d52-67330f92bfa5 | -4.35598 | -43.8028 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 75323642-c4f3-33f4-9607-fa61134cbd4c | -3.70734 | -46.02115 | 2026-10-08 16:39:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a43fe0c-6569-326f-8d96-fab25e2bdd90 | -1.20795 | -55.69521 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 88e2ab73-2536-3e0d-9ed1-abe94a46a72e | -3.24324 | -44.3735 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 22af6bdc-37f8-3db6-a0d2-02a770d94df4 | -3.29169 | -53.69912 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4f0155d7-1dba-3433-bf6a-565c5195bfbb | -3.9267 | -55.85747 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e073051e-25bc-3d11-8872-93cd84645a8b | -6.16829 | -53.27073 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 44abb59a-a1dd-3f5e-a77c-8c4bfd34f685 | -1.52165 | -54.51168 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README344.md)
