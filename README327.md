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

## Dados Diários - Página 327

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e8bcd8-b048-3cf7-af52-0071518d207e | -10.74292 | -48.5489 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83e63368-0f2e-3dfc-9624-59e29ad49c53 | -11.80428 | -43.52626 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e08ae8b7-c585-3605-b3d7-417f0e080d7b | -10.9531 | -45.38353 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 73929131-5663-3f53-bf5e-7d65838c6029 | -10.95257 | -45.38001 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ad2eee86-5c24-3332-ab87-0025086008db | -8.95182 | -45.14046 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d3f682ea-56cc-39f1-9684-905c34e99a55 | -7.11349 | -42.53215 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7bb293de-8b90-3412-a09b-366b48e4e8c3 | -8.96291 | -45.12447 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 089d8968-a580-3379-b895-226fd3b72f76 | -11.81041 | -43.52157 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f6cb1cb8-86f9-3a63-b128-8c6d238f4e6d | -7.04945 | -45.43858 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d32a1a6-1337-3ec2-ae92-2bbdb8feadb0 | -11.30068 | -44.83511 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6eaaa8fc-56fe-3f25-a702-0e127f130e89 | -9.27955 | -47.45048 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c0af4e15-4e56-3280-904c-eb8bfdb66b60 | -6.42682 | -43.82857 | 2026-10-08 16:37:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e282a38b-306b-3b9c-a163-0be2e05d5a84 | -8.94413 | -45.13451 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 104c48a7-c971-3149-88fe-b110c9d7452d | -10.50314 | -47.31277 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ab5f03ae-ad8a-331b-8854-42221fa948d5 | -6.04504 | -44.03092 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4a5bd7d0-fb35-3d47-aec8-1f8c0975b27b | -17.69314 | -39.1688 | 2026-10-08 16:37:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9f5b83ae-7d23-32e4-aa5d-eb94663349df | -7.48744 | -42.79743 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 7ce671d1-70f7-3804-8d15-a84b516bc37b | -8.34543 | -47.65894 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2548fea4-e8aa-372e-82a1-baf696d50e79 | -8.32513 | -45.03828 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ed4c3dc1-6869-3071-ad05-acaea3a05f9d | -6.32347 | -35.13029 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 47bc776f-5921-3d72-892f-bd5961335627 | -6.49282 | -43.57969 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 78781e0f-2ddf-31b4-a2b5-125e8d952328 | -11.40937 | -47.56549 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c5a8fce5-fe04-3d19-aeb0-b25622cabf75 | -6.38317 | -45.78683 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 83d2bec5-26d3-38f5-87a6-23655354c70a | -5.97098 | -43.87255 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bbe29c10-d516-3286-9e32-b51b31419641 | -5.97449 | -40.90577 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fd998e98-ec17-380f-8127-84c67db7f797 | -12.2396 | -44.7408 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c3cc8994-02b2-375f-9ed4-0254ec720f85 | -9.13785 | -45.82813 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 95f54c42-01d7-34b0-be48-212480513bcf | -13.70141 | -49.12099 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 98f04d0f-472f-34cc-860a-27f08a97e1b5 | -9.56716 | -46.84153 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 234cdb5e-4176-375c-b0fa-f2c371e3d442 | -18.24675 | -41.64027 | 2026-10-08 16:37:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f71e7b12-1332-3c79-bf4b-048919a2d62a | -12.57849 | -44.67059 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e8a4cb89-5bff-35d1-87b5-a6c55f45d243 | -6.9753 | -45.13342 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 18c83890-9c73-3838-bedd-4b8f7d0ac9a1 | -10.9014 | -45.53599 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2fdb6581-4653-3514-834f-2a4481b67ff0 | -12.641 | -45.86246 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 29a450f4-0a63-3566-a34f-c7b729fa0c83 | -7.48258 | -42.83086 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8560af93-70c8-38a2-8e29-439c8573d783 | -7.56841 | -39.04441 | 2026-10-08 16:37:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ce6a80c9-4b07-3a88-bfd2-8daea778d945 | -8.78588 | -47.59378 | 2026-10-08 16:37:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7d65b758-c344-3a4a-8ee7-1545841b7f90 | -11.62663 | -43.69225 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| dfaeaaa3-7c6d-376f-9378-4ad83b0d21cb | -8.28865 | -45.70927 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2f1212e8-9641-396d-b77b-1a644708d05f | -8.0724 | -45.62633 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| a64bdcb5-3ec1-33ba-8f59-317d18c21cfd | -5.73586 | -41.76831 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 07859f7f-a2e0-37fa-b670-999c6a097035 | -8.215 | -46.41123 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 976e9bd0-e066-3c13-bcd7-c9f0ed963bc0 | -8.29023 | -45.71969 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| dac53c93-0eea-353c-a85b-abad006d8acf | -8.52757 | -46.91122 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 67dff83c-c362-3f76-a57b-86837a1432f6 | -7.60538 | -49.55073 | 2026-10-08 16:37:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d048b4a3-27dd-3d17-8077-d0e0c4ddb7b4 | -8.06975 | -45.60896 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2186ac6a-05e4-3fa3-9945-7a5eec3d14c5 | -9.88332 | -44.86438 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 27cd319f-b271-3d0b-8f38-51adc0134746 | -12.18028 | -44.81855 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 05b72744-070f-308f-a074-a70343cc7c6d | -12.40749 | -39.07923 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a31c7d9b-7a95-3e25-a195-c72a9c51036b | -14.65765 | -54.96917 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ee7b4839-36e8-373f-889b-d8c9b00db251 | -5.97507 | -40.90932 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 2f399c59-f24e-31fd-bc12-2ce200e0cbd8 | -7.64926 | -37.66488 | 2026-10-08 16:37:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 28287d4a-c5ca-3bdf-90f9-20641734bace | -8.75533 | -45.76675 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4d974932-6703-396b-84fc-800bc0851905 | -13.65186 | -47.67692 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a8f24a7-5014-31f7-ab5b-cb3767658109 | -8.44711 | -47.9983 | 2026-10-08 16:37:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2d77ab57-78e0-39b9-b0bc-70cc008ff3b6 | -6.9532 | -44.41886 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0263c477-64c8-3237-88ab-a04e916e3207 | -12.76758 | -44.86715 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6b081a49-8978-37a2-8b73-e90c5c8c95d5 | -14.17973 | -48.67162 | 2026-10-08 16:37:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c1288378-9cd3-3614-8e41-c839997c7115 | -11.22363 | -45.24353 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 173cd8d2-3404-36ec-9cea-6a387efe8646 | -8.69252 | -39.12106 | 2026-10-08 16:37:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 72d55106-551e-3f09-805f-ed6f91206fdc | -9.75674 | -44.79218 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5e3b00ce-b35e-363e-b6c2-02e772101018 | -7.66519 | -45.38295 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8cd2ba16-42b6-3474-873a-ec6d306884ff | -7.22441 | -44.15698 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37ce8467-a943-3344-97ea-265a34915feb | -8.84017 | -45.4542 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f330406d-a770-3c41-a3fc-11e5edd5ccad | -8.01323 | -47.19074 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d48272c2-273d-3889-9965-6b96a3e01f74 | -12.24568 | -44.73624 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 49dc9512-fad1-3adf-a58d-282945a99a91 | -7.5111 | -45.77374 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 662d811f-8cbc-3343-80e7-7209e0fb328b | -5.49961 | -40.53553 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 3e3493d1-8d9a-324a-9d21-f5c62ac997b3 | -11.45632 | -43.38684 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 17bd077e-9c37-3b97-a09f-6ea883b93711 | -7.16404 | -47.78429 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bf08f37-e0ca-3382-ade0-813c9faf681e | -6.88996 | -45.90415 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 605d1fc7-f82d-3b4a-b4cf-37b47718089f | -9.92877 | -46.10295 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 384a5819-65aa-385e-a375-07324ef6fa31 | -10.67456 | -51.88752 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d795d51e-31a6-3e80-b33c-12d0668589aa | -18.04615 | -44.6032 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 56a27ba0-0d88-3c57-8977-2ad41b2f2be0 | -13.6478 | -47.67664 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 64868fda-5fd0-37fd-a8d5-8df0f9e26703 | -18.04223 | -44.6 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 121578e6-5949-31f1-a651-9dbbac78fc2d | -6.75592 | -41.53652 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| d4c91149-7d3c-3217-8e95-cb95919f1118 | -7.342 | -45.2887 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d02bd6d3-2745-3025-9ba1-9d1e1b73b07b | -6.79713 | -35.40372 | 2026-10-08 16:37:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bf729545-7e6d-369b-9a09-b40290ceabe2 | -7.47385 | -42.84479 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| a7a3b114-d09a-3e48-8145-cfe73817c61a | -7.47448 | -42.84883 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| fb13fab3-177a-36ca-ab78-2b212c71578c | -9.46118 | -44.61402 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9622e6d5-e0e5-3552-81ec-b54da2c7edd2 | -6.95469 | -45.28661 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ae7f495-7ca2-3413-9753-89ec7ea2ec70 | -6.20853 | -37.87769 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b6fb82a2-ab68-3422-8ca5-1cf46eb19a0e | -11.62774 | -43.69938 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| bc72b49f-f0c6-3078-a4bd-d6b809d84262 | -6.37153 | -45.79921 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0d0251c0-a208-32aa-bcab-0f0390ddfd55 | -11.72623 | -43.42388 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f0968767-c841-3417-8c37-c524389507b2 | -9.89458 | -44.80537 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ba6a3170-a5b1-3463-b4b2-0d1d16111b68 | -8.29129 | -45.72663 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e75565a3-2deb-3d17-b26b-3aadf292f73c | -12.19688 | -48.41372 | 2026-10-08 16:37:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a18d4b48-c1d5-3751-a246-4c6371baec99 | -12.31735 | -47.05242 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4aa08aa9-e294-30cb-83e3-3c3e5ea620b0 | -11.24235 | -46.25118 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 04e0dc47-69ec-3380-9b3a-e9b605d0bdb5 | -11.07251 | -44.03901 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 4e8c604f-23c2-3298-914d-25d2d81fd73b | -11.58648 | -43.67648 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 79e0b2e1-5f11-3902-8822-5425d4d3196f | -11.40489 | -46.68809 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6e89ab88-8aa0-327d-b3cd-fe7d821fd32c | -11.80036 | -43.52319 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 7963b0b2-9f39-3250-8443-ed0253e754e7 | -9.08459 | -45.12206 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 192e8705-4fff-317a-9470-2487d77dc846 | -12.7819 | -44.87214 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7c4eb664-ba7d-38eb-894f-5e5dcd85cd9f | -11.18252 | -47.72137 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| afa2fcc5-87a2-3a52-8497-fb27e975ed05 | -13.02112 | -47.20454 | 2026-10-08 16:37:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README328.md)
