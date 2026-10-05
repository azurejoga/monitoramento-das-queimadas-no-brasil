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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 863aa07f-951e-3b4b-bf0e-144adb621180 | -10.48424 | -47.25037 | 2026-10-05 16:37:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f02ac3f-523c-37a8-abea-665bded469a0 | -14.09068 | -45.60389 | 2026-10-05 16:37:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 12c88720-167e-36c0-a284-32734158a902 | -17.92128 | -39.42125 | 2026-10-05 16:37:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 0824dc87-8f17-3b7b-bd15-85b8801bdbf6 | -5.90976 | -38.04841 | 2026-10-05 16:37:00 | NOAA-21 | TABOLEIRO GRANDE | RIO GRANDE DO NORTE | Brasil | 2413805 | 24 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 20bf60f6-fdd9-3c6a-aaf1-df22f4d8c001 | -11.66495 | -43.65764 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f931d726-ae43-3761-a801-0322fae94967 | -14.08142 | -43.7688 | 2026-10-05 16:37:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| dae7db50-5261-3d2e-87ee-3b3c0300636e | -7.25296 | -37.2569 | 2026-10-05 16:37:00 | NOAA-21 | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a8ccd603-fc1a-3373-af76-84f4a3a17d10 | -6.70755 | -45.23734 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 6a6addf5-da31-330e-86b3-47f6b480bd60 | -11.39954 | -50.84669 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 529b07f3-2649-3658-ab5f-0aaab704afd9 | -6.80152 | -39.30001 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 1114f3e2-2ca4-36d9-a7e6-8c4117c21297 | -18.30951 | -41.00086 | 2026-10-05 16:37:00 | NOAA-21 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 584764da-eba9-3475-951a-f74562c5373b | -8.3058 | -39.14877 | 2026-10-05 16:37:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 4a36b879-2f24-3923-9155-88e401f334cf | -7.18606 | -42.00371 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 342da38d-48d3-3d54-bd07-0056509ed3e1 | -11.35227 | -46.67726 | 2026-10-05 16:37:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bfc20b83-b46b-3bda-8453-01c5b51d2597 | -7.17901 | -42.01225 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4b7dbadb-a5cf-372a-83a0-3793ff9fb1d8 | -11.6643 | -43.65363 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1deb489e-5c3b-32cf-b4f0-c2d92c23aa42 | -6.69371 | -45.23956 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4bb4aa10-8530-34e7-902e-bc1955b3c368 | -12.05012 | -43.43747 | 2026-10-05 16:37:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5425f465-9151-3093-ac43-35e1a3e0785a | -6.28604 | -43.08436 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4736fd94-344f-3ba0-acec-b48f4cc6ac74 | -11.00675 | -47.86163 | 2026-10-05 16:37:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 675ca32b-48eb-365d-bc81-d1e229ff2eb3 | -10.95106 | -45.4393 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7858f74f-a26a-352c-95a3-90385d01847c | -10.97831 | -45.43836 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 92507322-6056-3ffa-b996-cf46a4f11231 | -11.08226 | -41.26043 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d45aad44-3bfb-3a44-bb1b-71868a55ad7c | -12.69971 | -40.54119 | 2026-10-05 16:37:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8c82e43c-2500-3de7-8b62-df2ffeb82857 | -8.53639 | -54.58859 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 36237cd9-7692-33c8-8e14-ba231bba970c | -6.99978 | -41.47951 | 2026-10-05 16:37:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| e5a03453-c609-3080-a97f-fcc6d570719c | -11.64559 | -43.62749 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 74b6be9c-2529-3aab-adb4-8721b5b5d834 | -7.06336 | -42.88633 | 2026-10-05 16:37:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 01d6dad3-7d67-3890-be4a-4ef87cc02964 | -6.8576 | -38.67985 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7ddac9b8-a6f8-3b49-9df0-f374edac68ae | -7.18672 | -44.32178 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2d81cd9c-34e6-36a3-9a7b-476406c3fc20 | -10.3459 | -40.06949 | 2026-10-05 16:37:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b293294a-5332-34c6-a1c5-9287feeed160 | -8.78358 | -47.55129 | 2026-10-05 16:37:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3a5f5bdf-4d02-30c0-9e15-440e6c5c7ac2 | -6.5981 | -41.56976 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1c5f3a97-fab6-39e8-b0e4-8c9338db5817 | -9.82818 | -44.79594 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77f484c8-9c53-3b05-8301-fa8ebfc4a33e | -9.02217 | -45.15887 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| baf07bab-cd07-3324-9b76-a7f6b9a2571c | -8.58873 | -45.66343 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7239b1be-6137-39de-bbfe-0b8b1d426cde | -8.60218 | -45.6613 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69c0096f-c7c8-3536-8372-6128563889ed | -11.37396 | -42.54672 | 2026-10-05 16:37:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 158e3bc0-d15b-3905-be98-db82ebba5b86 | -10.75331 | -45.30276 | 2026-10-05 16:37:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1da0991d-24dd-3a2d-b32b-07bdac1954dd | -7.94605 | -43.84001 | 2026-10-05 16:37:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a0374604-2f47-33b3-b3ed-3ada57406055 | -10.9935 | -47.24955 | 2026-10-05 16:37:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 13458b8b-eae1-3a5e-a2f5-516eae866471 | -6.59674 | -41.5617 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 0fb08dc2-f4f9-30db-a88c-cf87f06b139f | -7.03253 | -44.78791 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 82d94b60-019c-33c0-95d7-96ee5edfae85 | -10.96773 | -45.41441 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f3fcfe60-08d9-34da-b19a-2ad4cfd4e6c7 | -12.75504 | -40.03697 | 2026-10-05 16:37:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 04e20b76-eb93-3525-aef2-fbf1e5eee2ba | -9.78208 | -45.90299 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| aa317ac3-b43e-3a23-83ec-d4068a334ef4 | -6.60798 | -41.57635 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 27fd3114-069f-3a76-b0ff-a1249a8b26a2 | -7.48478 | -39.72587 | 2026-10-05 16:37:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9640306d-4318-3328-b95d-186efc0bd0a7 | -11.02262 | -41.27769 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 037ad9b9-2438-3677-bb48-087503ae2b82 | -10.40062 | -47.53114 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3be10ede-823a-3fc9-9b38-1390068778e4 | -8.54932 | -54.57644 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 17557bc7-1dc3-3a53-87bb-fd6d261c3d67 | -6.34341 | -42.54694 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9a1ef78f-80c2-378d-a44b-d1f6f3a212b3 | -6.7188 | -44.27866 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5b9ed33b-f2da-3117-a09b-1cd39e38129f | -9.04214 | -46.88335 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 60f73a12-dc51-312e-98e8-aa279055591e | -9.38045 | -41.14078 | 2026-10-05 16:37:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 4478cabe-d2c8-3974-8fae-ec985d4c1e4b | -8.65821 | -54.54966 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 980f9339-987c-3ad1-aa82-4bc18c4ac6dc | -9.03192 | -45.17633 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 00d6ef82-77cc-361f-9549-f0a4e264d1c3 | -11.26255 | -45.23372 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bc9a9af0-1e94-3f8a-a007-762cc3779e11 | -8.55444 | -54.58423 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 5cf35513-dc10-3057-9792-007f19747fed | -10.49928 | -46.03293 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 06c611ae-9588-31e8-baee-0da1dccb95b9 | -13.45112 | -40.05748 | 2026-10-05 16:37:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| b432ba59-abae-33b7-aa49-5501f6410471 | -11.09522 | -41.26149 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7912f619-76f3-3230-a343-19bc1fd3d9eb | -6.71506 | -45.24006 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0ee14cf9-c320-3d5b-92ec-50ded95d9e96 | -9.02897 | -45.15779 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f6c65420-c35b-39c6-9d7e-5dedc9c8424a | -7.76396 | -40.27502 | 2026-10-05 16:37:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9ba2bb02-cc6c-3378-9b58-0979df6893de | -8.28222 | -45.92223 | 2026-10-05 16:37:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 933e054d-7b24-3e3b-abc1-4d02031ed6bc | -9.87702 | -44.83815 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1dd13a50-227f-37b2-b2c4-1bcbb3108303 | -12.50697 | -41.21411 | 2026-10-05 16:37:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 88be8628-7a49-3072-801f-35fb4fa57188 | -8.65753 | -54.54455 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 28656f50-0e20-3c75-bfb0-91f95268e433 | -11.20074 | -47.13678 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 00d6d723-364c-3c9d-af91-69a05dc531e5 | -8.15051 | -47.09615 | 2026-10-05 16:37:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b27bc3aa-3c53-3fa6-b31c-ed1a8dffa6e7 | -11.63281 | -43.63799 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| eaae248c-84fc-329e-87b3-c08c10b0ea70 | -5.98607 | -40.91188 | 2026-10-05 16:37:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 562db83d-911b-30a8-9d1e-1f79efad753e | -8.73779 | -47.0706 | 2026-10-05 16:37:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 552b6256-10b9-380e-8bf2-4b08f508ce28 | -10.40168 | -47.53824 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e0b04bcd-d8ec-3717-a175-ff86fd60b878 | -6.31896 | -43.34205 | 2026-10-05 16:37:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 976bee0c-b362-37d9-b35b-7973e9bea5b6 | -11.38336 | -47.72598 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cf05ae7-eb37-3c74-b36e-4a6f8ae37789 | -11.63634 | -43.63742 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 11ed1253-c5c8-397e-8dd4-7b2990987551 | -7.17842 | -42.0086 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| dca27e64-9adf-3993-a7c8-8cccc040b764 | -13.51371 | -40.76884 | 2026-10-05 16:37:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9ba478f1-eb4f-34c4-ba48-a453cd17be63 | -7.23119 | -45.73882 | 2026-10-05 16:37:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bedb6f4-d451-3723-964e-691001e32968 | -6.70789 | -45.55404 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7d38a4e-c759-392f-aa72-53bdd6990c0a | -6.89794 | -43.68772 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| aaa2619d-ff0f-3c4f-ad4a-6d687bc40664 | -7.48957 | -45.05903 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 362a2e26-82fe-3712-b321-19e0f421f782 | -10.95939 | -45.42687 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d6c1560b-de79-3045-ae66-5cbd28d5b3ac | -13.26582 | -40.36237 | 2026-10-05 16:37:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 14e902fa-cc9c-33a3-9fdd-d72b355dd9c9 | -11.09586 | -41.26514 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 07b1cf28-bff8-3c1a-a83d-2141e6e1937f | -13.75237 | -43.62181 | 2026-10-05 16:37:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 4815fbce-0231-3f78-acf9-5313809da0cc | -6.73425 | -39.11955 | 2026-10-05 16:37:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fc18e96c-6381-31a7-8b8d-e6c912974529 | -12.0716 | -41.39668 | 2026-10-05 16:37:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 78beec4f-9ae4-3f75-bd2e-3fd89397529f | -17.89691 | -39.42612 | 2026-10-05 16:37:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 8bfb0a42-4521-3323-bb7d-303ffb9d1788 | -8.53063 | -54.58731 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 20981cec-c8f3-3e47-8110-e6c98f70b6f1 | -11.37611 | -47.72336 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5b145850-b6fc-3cc2-8587-18bafce342b9 | -10.97942 | -45.44551 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 8898e8cb-f288-3285-8c70-8f6417fd7b42 | -9.41834 | -47.30098 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44ce83a4-7c30-37a5-a141-56f6ba703f1a | -8.59935 | -44.49115 | 2026-10-05 16:37:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0ee5a5a-ee1a-3704-ab4c-962c93de59ae | -11.3777 | -42.54613 | 2026-10-05 16:37:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 03c943ff-d718-33c9-b2aa-99b63253e60e | -10.50808 | -46.04595 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3493eba4-06c7-308a-8620-0eebb8e0ae26 | -6.36285 | -43.59498 | 2026-10-05 16:37:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 957d1589-e30c-3529-8082-a2255a9c0029 | -11.35439 | -46.69128 | 2026-10-05 16:37:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README81.md)
