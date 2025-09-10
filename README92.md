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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3b8aead-84c1-3784-9032-230f327fe213 | -9.09851 | -46.97342 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c328a0a3-af9f-3927-8dcf-49925ddbd973 | -11.95647 | -46.65443 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2d20cc7-2482-3cdb-ad23-66c60a5ad0e9 | -10.65833 | -48.61697 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 179c7b30-1cfe-3d81-9738-2417610f2d3b | -9.67465 | -46.89645 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 202675e2-a853-34c4-b622-60c16882da39 | -8.04348 | -48.66855 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cd0ac2a8-1419-3dc3-945e-1d5ad2a73567 | -8.52038 | -45.71485 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08616ea9-d2b6-3285-9100-0a1bf63cc466 | -11.24533 | -49.41039 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfc199d0-ea5e-3c87-a64a-05fba07eeb7d | -9.07995 | -47.05672 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a434c57f-fcb6-355e-9f7e-88839fa256c2 | -10.02827 | -51.66437 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd4dcb98-6b94-3517-a6f8-af2c9e229155 | -12.00056 | -50.97794 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| be38c953-c3aa-32e9-a4ac-ee83cb47ea83 | -9.10116 | -46.98161 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab26e2b0-29f1-3c3e-8615-268b52161132 | -11.81476 | -46.75461 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 535bcf36-b437-309c-9b5d-30045b472622 | -12.04996 | -51.05148 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 050f0150-e7d9-3710-a32f-19ed3a88e30e | -11.68254 | -46.89848 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d10ada-290f-3140-97b4-1e6ddfa88906 | -12.17504 | -50.62033 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7a487e41-d868-3d49-8300-28e5fa39ec5b | -11.10719 | -48.45889 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 966bf5d9-1408-34ef-9520-0b972a6d3d59 | -11.21417 | -54.99467 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f209a78-0a40-303b-b702-43b5bd2b49cb | -8.43105 | -49.11206 | 2025-09-10 05:04:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 939ec980-1652-3748-9cb1-609cd60dee20 | -8.0476 | -48.6739 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a6f2c8eb-def7-3f1f-95c9-c480e127b39a | -13.01145 | -48.04104 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b31659ee-54a5-3619-8272-8d07d63f25aa | -13.18156 | -47.26332 | 2025-09-10 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cf58131-1467-3425-a801-001306ae056a | -11.14165 | -48.35336 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e016425-256b-3956-b15e-93f14306a336 | -12.54706 | -49.10283 | 2025-09-10 05:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 624b3781-a8e6-3e5b-b078-cfefcbe6a742 | -8.38542 | -47.99491 | 2025-09-10 05:04:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae5c55f5-1972-3193-921f-46dbf7012380 | -10.01364 | -51.68098 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea2a7035-26a0-3fe5-8d34-b07324ce4cc8 | -9.67124 | -46.62593 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6bd1bd-ace7-365a-9edf-c993350eaf6c | -9.10312 | -46.98058 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f201ccd5-9339-3fd8-9ba7-18e2f3501297 | -9.05862 | -49.8149 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0ead3864-61dd-3777-83ba-bb2f304bbf39 | -9.68527 | -46.90097 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 4118fd3f-fd75-3590-a9a1-d59906832388 | -8.0689 | -48.66053 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a37771b-7ea5-3e8f-adff-63ab062567e8 | -10.27055 | -48.81638 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9ad578e-b30f-338b-9ec7-7b82f7a95891 | -12.00719 | -50.978 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| e86df187-76aa-316b-a02d-78ead52b93f1 | -6.84869 | -47.92292 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f1581e42-4289-30d1-9d7c-d1cdfad88a01 | -8.04554 | -48.68886 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0fba6ee6-6081-3d5c-8a4e-734311002c31 | -9.07448 | -46.97437 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bf2bd8c-d66d-32f3-8153-2aceacf35e23 | -8.07285 | -52.39022 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 791266c1-ddf9-31a8-9f17-34d9ff8c6180 | -12.02266 | -51.02662 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aecc816f-99c8-3777-b3da-f506a12e9c75 | -9.51769 | -46.54722 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39ff243c-3bfc-3467-8c8f-df58f396f595 | -12.01096 | -50.98276 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 8bb2cde2-7133-3a50-b3fc-1c6e3014a9e9 | -8.06474 | -48.65549 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 120df2f5-c528-3a92-98c4-8a67516be681 | -9.66316 | -46.644 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ea3433-ce36-3240-a02e-07acef9ff5f5 | -10.57426 | -52.03897 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9739e50-fa9d-3e3c-aa8d-6df74c786589 | -9.07401 | -46.97792 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 208cdc4d-3d2a-3d7b-936c-106dbaaa0bcb | -7.54406 | -48.21608 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4613a51-f96d-3e7a-b648-80c980a4c8fd | -7.23598 | -46.19542 | 2025-09-10 05:04:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea2ff29b-4f57-3d20-b4c6-c2960523f671 | -9.79906 | -61.52219 | 2025-09-10 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b7d0636-a9d3-33e1-888b-2dbd1e069a08 | -7.88852 | -46.27211 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45fcb97c-f3db-3e68-8cdf-5d77e51d4fa0 | -10.3053 | -48.81652 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| afe704f2-57c2-39f4-99df-71e561c6f2dd | -9.31484 | -46.72972 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b65a4c70-a17b-33df-8400-6d284f7740ed | -8.34728 | -45.04987 | 2025-09-10 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5c14c83-6fba-3b5e-8b61-357ab26f4153 | -11.15221 | -48.35191 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f464ec5-9263-3e0b-bcb8-ba293c4be90f | -9.07994 | -46.97493 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c868bce9-85bf-3e40-a410-af5c4751d4ca | -10.57175 | -52.02816 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fef78629-b513-3256-85b0-813dbc1f2060 | -9.05308 | -50.48607 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 109b2d88-6166-3840-9f01-1db6419e5903 | -13.1515 | -45.28505 | 2025-09-10 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82403c54-353d-3375-8c80-c0a398bd88bd | -8.7822 | -44.40993 | 2025-09-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16d91940-0e41-3683-94fd-9b9580b1a625 | -9.06365 | -45.71895 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e73a3e67-ba13-302f-91a7-c4706feda859 | -11.33471 | -46.52599 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26c5b2dc-9d3c-3107-805c-b092d73972f3 | -7.48498 | -48.22834 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2538244b-cd2f-3fde-9e6d-05c791522187 | -11.2136 | -54.99844 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb9e10fc-22a3-3e6d-b5f3-f4913b42b56e | -10.30958 | -48.82161 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c407e36a-68e6-31bd-84cb-c1b155e3e109 | -12.01151 | -50.97861 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7cb44eb-dc53-3114-b1c3-cb1daf697b58 | -7.7875 | -46.06235 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d31d2161-f2ba-3122-aa15-0bf91d935de9 | -11.44324 | -43.62194 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d538ef5-8e7c-3038-bbbb-3733bfd93f44 | -8.492 | -45.65903 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79a70617-fd5f-3777-8685-91fcfdbb1b5c | -13.79386 | -46.29454 | 2025-09-10 05:04:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 563bef6a-50d9-3dcf-89ac-e6809c3ac9f1 | -7.35671 | -50.81145 | 2025-09-10 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c1f438c-b40c-31bb-b32b-53fee73f0e1a | -11.19367 | -48.37611 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 588960c5-f021-3984-a6c3-e5c3a8134a77 | -9.06906 | -46.97358 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77d966e1-69c1-3c62-b690-4d579dddf871 | -11.21187 | -54.98661 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7aec732f-1d3b-3bb5-b587-6e8340496845 | -8.06834 | -48.62951 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1d5ab348-478c-3a5c-b08c-c0275f1a5932 | -9.69224 | -46.75888 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f72c9a-d1a7-3852-a1b0-b1d3b9ea7b2f | -6.3405 | -47.10079 | 2025-09-10 05:04:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b0315d8f-00f6-3861-bf3a-3a8028eaa4b3 | -10.74137 | -48.18334 | 2025-09-10 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60c3ae19-96af-3612-b2ab-5b60eb25aeda | -7.55624 | -44.65701 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde5286f-73e3-3367-8d0f-52eb07444a18 | -9.45203 | -46.70569 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 067f1ef8-58fd-3a51-ab97-d572d1a31921 | -11.21131 | -54.99038 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8927cc58-bf25-30b0-bdb8-8a855681e5a4 | -8.47979 | -47.30291 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af8b474a-e83d-3adb-9d06-dfdd71015fd5 | -7.77674 | -46.05648 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c3eb7fb-d551-317f-98b3-84023dc2d150 | -12.18552 | -53.86528 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ea3bbb6d-84a8-3faf-ba06-d3aae5b6153b | -6.81513 | -51.87914 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba46c036-03c7-34bd-a408-408562d4251e | -12.01416 | -50.99167 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c92cc793-ee0b-3ebc-b768-cc38e55f7bcb | -9.6904 | -46.81733 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c24aed1c-b8b7-328b-8b20-bdcea29d3e76 | -10.01522 | -51.66989 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ffd787e-cee3-3ad4-901c-cded32c8ee69 | -5.87841 | -52.16027 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 515319bd-b6f8-38bc-aee6-6c1d6c6fdc52 | -12.83488 | -52.94086 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 436f77e0-3b9d-3b30-9566-61935a44df56 | -5.66509 | -51.63367 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21ab47fd-bc71-3ba8-b77b-4988f97ee3a3 | -8.05834 | -52.3331 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b6e11c12-dec1-3f97-9b39-fe5cde8a51c3 | -9.71277 | -48.09053 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5698fc9a-dc74-364c-a034-72302b4b7b63 | -13.01654 | -48.0144 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbc0b78a-8051-31c2-b712-db471cd6ddca | -11.53401 | -47.31686 | 2025-09-10 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fc6e8c5-f6ad-38cc-b7e4-c1bbce2390b6 | -11.6735 | -46.90392 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0f322ca-7fe4-3fc4-aff8-897df9585d66 | -12.08254 | -45.48011 | 2025-09-10 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc98bd51-b6e4-3b43-9cb5-66f40e43496e | -6.8737 | -47.88794 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 722ff912-ca43-3d0b-8ac2-6ad648b90c03 | -10.00529 | -48.08501 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ba95832-427f-3fef-95db-32ed8d5019c5 | -9.07065 | -45.71148 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1fb02dc-6cfc-348d-b193-4cc10050f757 | -7.07608 | -45.20087 | 2025-09-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4b340873-1872-380d-9358-ae9fbe44c3a3 | -9.69543 | -46.82208 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba0f231e-2159-3c81-ada4-53f3aec9a133 | -11.20789 | -54.98983 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 505b02f2-7916-3583-805e-82d95a5014c9 | -10.01771 | -51.70966 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README93.md)
