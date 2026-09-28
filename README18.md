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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a8d43a5-8efa-3c12-b8f4-2cd8002cd788 | -11.68243 | -44.54367 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ef751b2-de53-3e33-b868-616b49faaa0f | -11.7084 | -44.52751 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2c8d8a9-746c-3312-915d-f29d9a791533 | -7.34538 | -42.07544 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ce05071a-e42a-374a-9fee-caac0a0af1df | -11.69666 | -44.53649 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38de4390-1b93-3bfb-b03c-e305ca21b28e | -7.62171 | -44.60574 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81e3371b-c65d-3d2f-9597-a62bc85c0758 | -8.22569 | -45.44361 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11b7a017-366c-3d91-b0c3-560eb4a5089b | -10.12456 | -45.13409 | 2026-09-28 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1d1af8c-6edb-347f-b9b1-79818f2d45cc | -11.35321 | -47.43398 | 2026-09-28 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 340efe51-6fd4-33a2-ab4a-f2bfdd8de5b7 | -6.69247 | -45.9765 | 2026-09-28 03:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1db6643f-ecca-3c8d-be0b-a500e3cf69d7 | -11.19459 | -44.81382 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 148951fb-8549-378f-b241-a5793593cb1f | -6.72413 | -45.59885 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 05f2c3ad-6dac-3aa6-87e9-c2a3d321ad62 | -11.69797 | -44.54108 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d391600-554e-3c40-a000-1f3c272f857e | -10.11155 | -43.94306 | 2026-09-28 03:49:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26578e7b-b0c3-346b-b7af-6543911f3ac5 | -13.07469 | -47.44225 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6992cfa-6512-3173-bf24-c9ea34fc5251 | -9.14483 | -45.63396 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5badeb58-cf71-3758-be91-3f2ee47d52a2 | -11.90031 | -47.00817 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0dc1356a-d0d0-3274-b626-9e62b22e6b9c | -7.62601 | -45.52315 | 2026-09-28 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 177f5f8e-e5e0-3f99-9070-718959bbf762 | -11.85844 | -47.09972 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c67adcf2-5c5e-3cba-b237-189304e00e1c | -7.70962 | -44.93283 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6d6aca5-65ea-3e2d-80b0-09037008e492 | -13.46552 | -48.59974 | 2026-09-28 03:49:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e2813bf5-05ee-3578-93bd-91a0d7b4f703 | -11.69996 | -44.53014 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bbb884c-57cd-3336-9dc2-b25e262f1823 | -6.99722 | -42.62534 | 2026-09-28 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe8cfa92-611c-33b6-adef-7cff91421fed | -13.39228 | -44.36781 | 2026-09-28 03:49:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bae4a58a-3036-3745-bca9-20ae22c2bcbc | -7.70902 | -44.93623 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b61e751-c409-3201-b0fe-3a8b818e5f22 | -7.71392 | -39.34772 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c8f9e06-6233-39f3-b757-4c964f8c2264 | -6.69652 | -45.58952 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 392957fe-aecb-3148-8ea2-353971fc0067 | -12.6304 | -47.32256 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09b96591-9e9a-3031-98f0-156f3f2700ab | -13.31965 | -41.04686 | 2026-09-28 03:49:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7be75f4-32cc-336f-8aed-39d048502d1b | -10.7108 | -44.44184 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26f425b5-a075-3c39-bb75-eb446eab1014 | -7.52778 | -43.97865 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3400201b-aa4a-3986-92fc-400ee4e0729f | -11.18542 | -44.80757 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 9f63adea-79fe-3c59-8fd5-683fb3522050 | -12.65892 | -47.32854 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 549fbc2b-05c4-337a-b527-912b963847d8 | -9.32424 | -45.37029 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efadd3da-ab4c-33ed-926f-a456311d0a0b | -9.14894 | -45.64223 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e464723d-6f9a-318d-96c7-1a9da188d8a6 | -10.21676 | -49.98006 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9a5f8a0-74c5-33e4-a857-a8e27d89058e | -8.9662 | -44.14382 | 2026-09-28 03:49:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| abf18b90-ed89-39e4-8bc3-b45eaac57037 | -10.70801 | -44.42933 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47f6f143-b06e-3646-ad28-c022dbaee0c4 | -7.62667 | -45.5196 | 2026-09-28 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 918c8805-d839-3c54-b0ce-8a85eb53a14b | -13.45463 | -46.32292 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bb2e091-28c6-3268-9e31-4d8251282a65 | -6.72607 | -45.6 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ea0521a9-bc2e-3049-8d00-f5d5e09b6a9b | -7.71373 | -44.90969 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39560918-3fee-37f3-b074-927eb4700604 | -11.69943 | -44.54837 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8986865d-10b4-367d-9451-8357798d6bf0 | -11.69285 | -44.53009 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95de21be-ab08-37b4-9a92-56ffdf43d44a | -11.69512 | -44.52918 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d19262a-9a3f-3fc3-b746-85d9aa70b910 | -11.90445 | -50.62074 | 2026-09-28 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 471e3235-c7e1-31ab-aaac-ab529dca0c06 | -10.12855 | -45.14156 | 2026-09-28 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5e344fb0-d143-3df6-ba85-494b190e27e8 | -13.56006 | -46.36544 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe3a3636-611e-3274-ac38-a62730d04c2a | -9.77451 | -44.82958 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ca21a3a-1a59-39ff-b32d-99a65d3f1009 | -12.72788 | -47.28604 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18fe9455-659a-3363-9c72-44e64e5d8a29 | -11.44512 | -44.93567 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3703dccf-d7a4-3fd0-a5b8-f00d1585cc65 | -12.6896 | -47.32904 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6821a795-c747-3283-b4fc-ea41cf542206 | -11.1943 | -44.8147 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 7fb6ce12-b755-3cde-8e37-664ab2974081 | -6.69648 | -45.65542 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7ed4ed-8782-3b6d-ab4b-40feb292832e | -10.92257 | -50.69156 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 721aceb4-3539-3b72-b250-e42cea74a36a | -12.63511 | -47.26892 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f10e5de-04bd-332e-a1e0-7b399e94d89d | -12.73676 | -47.30089 | 2026-09-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34453e99-b753-34c7-bb58-5df608f0db42 | -11.44289 | -44.92 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64dec366-6eb5-3bf9-9e18-3c4be71db9af | -11.85923 | -47.09573 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ef2133a-da92-3430-ad4c-05ae20a00b07 | -10.20843 | -49.98531 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6bbec9de-d41e-3941-8f42-077105a2e36c | -12.87315 | -44.78854 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8638594d-0080-376d-98b0-35c7d3dfd107 | -10.12267 | -45.14427 | 2026-09-28 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2551da3d-e9c4-35c3-9c69-50c4d977ee00 | -8.10421 | -44.00901 | 2026-09-28 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05270698-2244-3f13-9ccf-e185f18caf2d | -7.70308 | -44.93863 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d25739c-24df-39b4-87f2-d0adc910e9b1 | -13.08176 | -47.44196 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab1b3311-dba3-37ec-8109-5123cf5c2e8f | -11.44181 | -44.92573 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdaaafc0-80f2-3bc1-8ef5-b9fd378efb05 | -12.62702 | -47.27983 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc82e3b3-4fe6-325f-9c00-7d4ef5a88da0 | -11.70253 | -44.53201 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d50e57a-63b9-3888-9b24-d8e218f04958 | -6.67807 | -45.62698 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabd6e33-2f19-367b-ab17-cd38ab93523c | -11.19259 | -44.79665 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 974e5715-1d8d-366a-97fe-ccaab6c45e42 | -9.07996 | -43.13118 | 2026-09-28 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc182d4a-9aa4-3448-b73b-10f051a2c8ce | -7.34168 | -42.07035 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ab99acec-4937-3e0d-aec0-7dce8f94a2b1 | -8.23766 | -45.40896 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fb741a6-e545-3821-aee9-7ef009522fd3 | -8.09927 | -44.00754 | 2026-09-28 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 540d6e65-2b40-3e11-99b0-0cf480fd3315 | -11.37134 | -43.42562 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f93868a-f307-39bd-9174-c6f8a8ff35e3 | -8.25448 | -45.4096 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 566969ae-e8e4-38df-847e-6c54f88af939 | -11.12801 | -50.06448 | 2026-09-28 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a7a2b32f-7690-3f4d-b3fd-64001ef21ac3 | -11.18044 | -44.80659 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 8eb26d41-e901-3f7e-8e15-f5b1fca17251 | -6.69722 | -45.65127 | 2026-09-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45a2006e-6120-3cbd-bd49-983f4eea74cf | -8.22891 | -45.48811 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fc29e99-2bb5-3a5a-bd5b-81590e9f2801 | -7.33725 | -42.06958 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e14cbd98-0841-3cd8-ba7f-7e838608c490 | -9.31606 | -45.38462 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1f8fee5-08bd-37ed-82f2-d7991a38ad8b | -12.67974 | -45.0191 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2705570f-4304-30e4-adcc-d00e58494996 | -11.70737 | -44.53296 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb18dbe6-537d-3acb-a401-36c82ba9dd8a | -13.10478 | -47.41638 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ffe451ab-153f-3c5d-826e-8e33886fe3af | -8.90047 | -46.19503 | 2026-09-28 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f54583b4-6dcb-3e75-9e13-702ebbe44607 | -7.9884 | -44.81707 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dca363c7-7aeb-3c3e-933c-f2d49408ee6f | -11.70459 | -44.52111 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d031c26d-5351-3f30-8963-105a375e18ff | -9.78078 | -44.82416 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a27966-6a6e-34ad-83f6-497e7c937c88 | -11.37586 | -43.42649 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1d1b2db-96b3-3fa4-8d38-a5c426387df8 | -10.37608 | -44.9731 | 2026-09-28 03:49:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89d09947-edde-3267-9678-6042e535d80a | -11.49512 | -47.38691 | 2026-09-28 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4927cf2-2737-3214-b684-ef76747d3d1a | -11.62754 | -46.77667 | 2026-09-28 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a533e4e0-c2ee-35e2-814b-6b1554f51c11 | -6.59978 | -47.16815 | 2026-09-28 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0075a85-4402-3369-b46e-4327a2a62617 | -7.34095 | -42.07465 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8453bef3-8c20-348c-abb6-9741bdda5579 | -9.16875 | -45.77958 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c464d697-dc2a-30b7-81a2-92fcc24c02ba | -8.96199 | -44.16684 | 2026-09-28 03:49:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0087d272-8574-36d3-af07-a33681ad5c7e | -6.68585 | -45.97982 | 2026-09-28 03:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35874798-5838-395f-831b-d5b1de84b3c7 | -8.2383 | -45.43653 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d60fc597-82c5-3b02-acc7-a729ebca22ba | -11.6984 | -44.55384 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05a539b0-f82c-38ef-b394-bdfaf6887bc4 | -9.81944 | -45.26572 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
