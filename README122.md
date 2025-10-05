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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06efa9d4-b442-3f3a-9d23-a42abddc47f8 | -11.81961 | -46.85658 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7fcb3486-2c59-37dd-b98d-dd29d9306ceb | -10.49477 | -48.10788 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87b19172-b806-3eab-aec0-4126cce0c0df | -11.24012 | -47.78817 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bedc867f-e767-3486-89bf-9457e1cc8e02 | -8.61039 | -54.97004 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05f51e2a-b126-317e-acf3-90b9afabe090 | -11.10598 | -47.87583 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1968030f-c0f5-3b21-9eb7-ec4ca329e02c | -6.19029 | -44.60218 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f74695f-aa99-3e2d-aecd-f8ce95fe08e9 | -11.10009 | -49.85704 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e3ce2ad-0e39-37c3-95c7-23fe757c35a3 | -8.9 | -46.68323 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f5af556-a525-3520-a8e7-eef21403d363 | -6.42392 | -44.46636 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c2a0e26-fe1d-349e-acae-c813f6d836cb | -7.54646 | -47.28181 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84e1964c-9751-3969-9463-7b2903a8067f | -11.0292 | -45.575 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44dd20ed-de36-38d5-b190-14cf420118a4 | -10.0177 | -48.292 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 023076a2-cb04-3b9c-b408-6763b29a6994 | -7.15537 | -46.08705 | 2025-10-05 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bcf7dee-7504-394b-9df6-79c389f29a9b | -10.94384 | -47.0695 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb8cc42a-7772-376a-ad82-01c2fdd93b0a | -8.42753 | -70.12713 | 2025-10-05 05:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ccf43bb-3613-3f98-b785-33a59401c116 | -8.85948 | -46.09837 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e621136-733f-3f60-b32b-ef6cbfaebe7b | -7.79497 | -46.01898 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04f91c6d-7504-3c5b-8f5e-82df10ae2a85 | -11.76224 | -44.74296 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca3d5db6-6e34-32f6-a573-97fe5169dc9a | -11.77406 | -47.94369 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cdaac15-a36e-3108-b392-48a1ddf93ad5 | -6.18205 | -44.59579 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c5f7596-bbdc-3629-8e5c-bac8472f4ec5 | -5.76784 | -43.98161 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4fdb2df2-fd09-3701-8b33-38ea53a146d5 | -8.58544 | -46.33239 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0e7f964-cc9a-3425-8482-891f243cc851 | -11.53794 | -49.806 | 2025-10-05 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb80de5c-e85a-3701-87a7-9819dc894b3f | -7.54701 | -47.27765 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c7774ae-7b09-31f9-a27d-994794229176 | -10.3569 | -48.17078 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b2305978-af20-3d86-87ca-48ce12c97374 | -9.30063 | -45.99495 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3a4df5b-588d-3432-b332-82a0905f0b49 | -8.59688 | -46.29389 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 544dec73-f3e6-3dbf-9e20-eea01ead3c71 | -5.92796 | -43.33259 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c21b0a7f-8bce-3b93-94ba-3558160abad3 | -8.82058 | -64.24206 | 2025-10-05 05:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6626ecde-75da-31f5-817e-2fce7f275e22 | -10.18288 | -58.1788 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6bca8cd-7a6f-33fd-9ac8-7df98ecb1301 | -11.8075 | -46.85044 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c196021c-9805-3b13-b98c-499bd183a35a | -9.45362 | -56.65484 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c41b799-b35c-34c8-a321-292b7d72f86c | -9.97618 | -48.01641 | 2025-10-05 05:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b44993f0-8f11-3a16-92fb-d39163febde5 | -7.79109 | -44.51505 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d951cbd-9e89-3892-80f3-cf63a3325dc5 | -5.97234 | -43.51108 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b32f3d1-6442-34dc-8cba-733a948d332e | -6.1636 | -44.62997 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9e4408f9-fdd4-3eeb-85df-652a6e8896a4 | -11.93632 | -46.43536 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0060b83-f4bc-3fd1-808f-51c542b359d8 | -11.80671 | -46.82668 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f2cf3f5-7a9b-392e-acec-88586a03781f | -9.20984 | -46.92651 | 2025-10-05 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d9d2500-2e8e-3d51-ac3d-19d9ed1792ae | -9.91213 | -50.20131 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c6ada60-56ef-3176-801e-d841208b86c6 | -7.75495 | -46.31656 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6f00fa8-14c1-3c6c-9a5b-126b694c5643 | -8.89953 | -46.68248 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54f0ca87-b627-3d5f-a686-3cece077cca3 | -10.64573 | -46.34835 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 35719df4-6e5b-3df7-80a2-6d88c85f2715 | -8.58044 | -46.32179 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4e60823a-16d4-311c-a18c-2442193deedc | -11.55106 | -47.69219 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 688b6396-8b7d-3bfd-95f5-e8fbdeb70174 | -6.17356 | -44.62488 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a60280ac-e81b-3b5c-9784-d856a477c4ca | -6.15584 | -44.58583 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d5e86142-f263-350b-85f6-4dd3a398918a | -9.64567 | -54.3167 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ad0e434-dfd9-35b9-a253-fb98c78ff056 | -9.29901 | -45.95971 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b44733ff-1802-3cb7-bee2-051a2a3960b8 | -5.92274 | -43.32963 | 2025-10-05 05:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ee3b093a-3224-36d9-bceb-2b9fa84c502e | -11.52471 | -47.23811 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 823bf468-5553-3608-8bf5-c5857deedf8e | -5.78463 | -45.79937 | 2025-10-05 05:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60e6a842-d3d7-3edd-a98b-29aa94f61aca | -6.18711 | -44.60907 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29959388-b654-3d17-b839-a1d4fe913d76 | -8.93519 | -48.66145 | 2025-10-05 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1671c7d-0a2f-3c54-87a5-c7507ef4abe5 | -8.53994 | -50.16154 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83baa929-e6c0-3b8d-b0fc-e4e9375fb86a | -6.18626 | -44.61529 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f17ed7a3-bae8-32b3-9efd-324e2aab8eff | -7.01436 | -55.26567 | 2025-10-05 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc65fb64-e33d-3f08-bcec-036a78662ff1 | -11.23378 | -47.79079 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d187b907-c7f9-3675-a6b9-c294448837e0 | -8.58735 | -46.3178 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bcdc8543-5ab1-3e14-9add-f4e218bb1a25 | -10.012 | -48.29171 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c128ec45-9596-37b9-8856-22b36cb2d63b | -5.46256 | -51.0104 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8299ae83-0592-3b96-975e-7cada42df3f0 | -9.30991 | -54.53665 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d56b25c7-8e79-34ed-aa9e-bbd6138c390b | -11.09091 | -47.75322 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87963350-6eba-3eb2-891f-f8de7b060341 | -10.48904 | -48.10696 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee7ecb7b-4c79-343b-847e-14d2d6b7e76b | -8.5479 | -46.27649 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 475e9aa5-048b-361d-a596-5b551dd58138 | -5.22574 | -43.70428 | 2025-10-05 05:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 625ca861-a794-3808-b534-2d70084f1329 | -11.81595 | -45.05437 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 12f02fd4-c309-3b60-9541-96a9a2ee824e | -5.34571 | -45.30441 | 2025-10-05 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01f026d4-5481-3844-b18a-73919964b72f | -5.8884 | -43.70491 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 771ddb46-61c6-3123-8001-76c23ef08e6a | -10.45069 | -48.37679 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ce26846-ec20-3038-b09c-2b4e8ff5ec1a | -7.75309 | -46.31253 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 288edab4-1d31-38c7-a7c3-772bab9bde7a | -9.91127 | -45.9552 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf311ad-976e-3167-a8fd-12d75534e0e5 | -7.43135 | -46.49994 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49461d1b-c27e-3f6b-915a-0921f05af908 | -9.91776 | -50.18954 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e984524-2aef-3b50-ac1b-a66d043515ba | -11.59433 | -46.71182 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23531ea3-b97c-3116-aeab-810b844a05b5 | -11.78852 | -47.92388 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38e4f092-cd1f-3b39-a0bc-e421de0e4a82 | -5.23242 | -49.06971 | 2025-10-05 05:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7892721-f626-3b97-96a9-3b427838b034 | -9.29241 | -46.0108 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 816e8602-5b8f-3259-85e6-85296ba4a24b | -11.11807 | -47.21333 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85e988db-4718-3bb4-8d65-9b27115ba6f9 | -7.01495 | -55.26184 | 2025-10-05 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d99b7918-1cdd-3c7c-bada-26e0dc185771 | -11.02479 | -50.70343 | 2025-10-05 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22b181b3-bd9e-3f93-b9bc-ef6fa6f64940 | -7.79677 | -46.01964 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dbb052d-d7b3-3277-931b-7413cf933b99 | -9.6458 | -54.3147 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8142eb96-3f65-3f82-b233-2f6b54ff4c4d | -10.46155 | -47.81135 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b7d9fa4-6b23-3e7c-8326-065cb1b54bdb | -10.46767 | -57.49017 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89376236-1a59-3ba2-950c-6b4fad9174d4 | -11.06609 | -47.77727 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e3cf85d-573e-3440-8908-7b1d93e196d6 | -8.58481 | -46.33723 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e7367ce-3fa1-3a98-87f9-51010b041d35 | -8.59067 | -46.31405 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6bf12314-38bd-3969-ae79-7af8044aca78 | -6.15769 | -44.62288 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d7dde0c2-eeb7-3bc4-925c-6f613a97201d | -11.12325 | -47.17197 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ea424cd-834d-3798-8b77-89450e28b10f | -5.13685 | -60.38753 | 2025-10-05 05:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b9281e3c-1e3b-3729-93d3-3b70edf12b69 | -5.92171 | -43.32417 | 2025-10-05 05:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40bb168e-aa72-3dcd-9bc5-7659d27e73d2 | -8.62636 | -54.66158 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8292c9-562c-3dc2-827f-6e5e8ac97ffe | -7.62051 | -61.34853 | 2025-10-05 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a25837a7-3059-37c7-aac8-42a4a44ed885 | -11.45291 | -51.51932 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b615298-2095-31f6-ac60-ffad3658e2e2 | -9.29324 | -46.0044 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49cb5de7-842c-3162-9f72-a54f3c194183 | -11.78048 | -47.94025 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84fd1908-6937-367e-92e8-63031525638e | -11.01691 | -46.71217 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 213ca716-00ee-3de9-84ed-b97c357ec3dd | -6.16601 | -44.61233 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dbf220c7-906a-3cc4-b976-cbe4bdd47242 | -11.02549 | -50.69803 | 2025-10-05 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README123.md)
