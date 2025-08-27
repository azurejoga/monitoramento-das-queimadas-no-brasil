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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5be5a938-8e4e-3142-9c44-4cf39209e70a | -9.94875 | -46.37512 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f20b3ee8-fa87-3706-b1e2-ff5a15b8970f | -9.49166 | -46.71603 | 2025-08-27 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bce38b80-550b-3628-8502-a6f4745b7988 | -7.12432 | -43.69266 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e809de70-f9f7-324f-84d4-7a87816a165f | -4.79343 | -47.27213 | 2025-08-27 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbe020ed-6d60-3653-bd1a-7e39d2d06941 | -9.58386 | -55.38126 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 288f7573-5bf0-3f64-a38b-8ef60160a598 | -8.55982 | -51.35505 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a5e31e7d-453a-3550-a415-45bb8499b65f | -9.58777 | -55.38828 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bc02d39-46e4-3225-8e78-b439d24a1f88 | -9.86643 | -44.70674 | 2025-08-27 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1b89f4c2-a553-31dc-8912-1e5b74fe4ddd | -8.15554 | -45.05191 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea1f2dc9-d9f0-3df3-acb4-4a4250893b1f | -11.25088 | -44.9915 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 530c9c3e-3f90-344c-90c6-77de5a1389c4 | -8.90094 | -45.71404 | 2025-08-27 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd24690e-43f8-3347-acc5-001900556981 | -11.58798 | -47.18377 | 2025-08-27 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db82a8ab-4075-378d-834b-cc032cd616ca | -5.622 | -45.7312 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15dc62f6-d821-32da-95aa-c0408ad8f722 | -7.16936 | -59.74387 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a784dcdf-1245-3ec0-8743-15dd43ade3a5 | -7.22207 | -44.40613 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8c9a351-a8d8-30c8-88c3-55016b35919d | -10.31798 | -46.77277 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f439fee-ebb7-3313-8e87-3726a1cfa6e6 | -5.48174 | -41.41075 | 2025-08-27 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99c168a3-ef89-3601-839f-c3cf70e73b45 | -11.32401 | -43.29626 | 2025-08-27 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37ace5a5-fa14-3a27-a520-59cff7985e0c | -7.16396 | -43.50332 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7758a9af-ed29-3d00-ac0c-9fe68f918cad | -8.49707 | -49.41528 | 2025-08-27 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 870f823b-9cd2-36b0-8d0b-84a3890ad874 | -7.16038 | -43.50277 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6c8e14bd-873f-3454-80e1-8a95aef25199 | -10.78747 | -47.07003 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f44faa36-b38d-3d65-b91d-93033c700bc2 | -8.293 | -46.32567 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8f70fb1-64e4-3f58-b163-29cfa79590b2 | -6.91793 | -52.8563 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a99cccb-6eb4-3da4-838d-8e810e522876 | -8.89791 | -60.77702 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efb980b9-642c-3c09-8f62-a84eb8129064 | -6.23557 | -44.78331 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 718177a9-b170-3570-b9c5-9f28cf675693 | -8.68877 | -47.19798 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8582fb6c-fa5c-3b09-88f3-aa8210e47781 | -8.00478 | -49.71856 | 2025-08-27 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20064f85-cec7-3d87-8890-a812b1ed8e0f | -7.35478 | -59.66799 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d93d1ac-d359-313a-8479-acebc1294470 | -9.15657 | -59.54713 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adefc4fc-2a73-327b-918e-5aa39dfe0283 | -11.25378 | -44.97198 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1976bf4b-b450-3e7d-b915-f35d3ebb9c44 | -6.95529 | -44.09039 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 551190fd-abaa-34d0-b91c-aef46bae4ebc | -6.25575 | -60.02258 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a742c127-c99f-3023-a324-a1101bc17096 | -5.75472 | -53.77182 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adadf1e5-590b-3584-98ef-63520af130e0 | -9.09574 | -49.56661 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 38d2e25f-9c17-3586-8686-2a53a84ad594 | -9.0986 | -49.57114 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9d151b70-bc3a-39da-8374-caa04618cf3c | -7.76189 | -43.632 | 2025-08-27 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e207a3e7-1b48-33d0-ac10-69141aac7c72 | -9.18601 | -59.53543 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3315766d-b81d-322d-b257-b4058b8b1676 | -5.61977 | -45.72376 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 922ce761-2013-3248-958f-13d3d44c5a24 | -7.7471 | -50.28114 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8546e48-d771-3b47-a21d-0bcbec2b2e85 | -8.45782 | -43.67022 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4419bf7-7a24-3303-82b8-b5c07ff1142e | -10.31252 | -46.80775 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01595455-e61b-3a5d-8bc1-930375138d0a | -11.61367 | -46.4063 | 2025-08-27 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db16c2f0-1630-38ec-9056-20a6e0fc82df | -5.78157 | -46.14181 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2de16af-0ffc-3f00-b00d-6aa537e34c06 | -7.71077 | -45.77254 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f53a2306-9596-3312-b912-1bb460c6a2bb | -6.78401 | -59.63502 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03e37755-c93d-31bd-adf1-997444ca1603 | -5.09994 | -43.79055 | 2025-08-27 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a93836bd-6aaa-34db-8f2f-55074ae4f0d7 | -7.16 | -44.17079 | 2025-08-27 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b42269-7048-3738-b535-038a8c7c6423 | -9.9493 | -46.3716 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d47cecf7-8ac2-3851-b51f-6ec94c9fc1f6 | -10.78262 | -46.37944 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 494e2dc9-e603-3f84-be1a-bb91d11fbbb8 | -4.55105 | -55.96095 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8bb7a39-724f-3bd6-ba53-af81ca21198c | -9.85736 | -44.59382 | 2025-08-27 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e31a0093-86db-38da-93bb-9add048ba7e2 | -8.9025 | -47.32882 | 2025-08-27 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7014327-6c69-304a-8e83-8d09d8ae32d7 | -7.65936 | -42.65386 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 95548a2f-d6de-3303-87f6-96c607bb0d84 | -10.74282 | -47.07366 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14cd49f0-63f0-39ec-804c-1234bdc3c3f1 | -6.80047 | -44.3247 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1aed593-4f26-358a-89a4-0074b610c900 | -6.67935 | -44.40638 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d90e203-8898-333c-83cb-2b26e2dfdeb3 | -7.08361 | -43.64938 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd16c1dd-a418-300e-871f-2df5b90bf8d7 | -8.26195 | -45.11667 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cb0bf16-3e74-3af7-9bfa-74e851ec931b | -3.98076 | -51.06362 | 2025-08-27 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b74fa37a-dcb4-3bdd-a830-8f202c06c0f1 | -4.09915 | -47.72903 | 2025-08-27 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd7c6215-5c60-3f84-8425-2e933eac7b7f | -6.88885 | -44.98292 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cd47cd7-d107-3370-96cd-a427cf68b949 | -9.42079 | -48.24942 | 2025-08-27 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9d76936-45e2-3bfb-9d53-bbf6e0d40ce6 | -6.32029 | -43.60767 | 2025-08-27 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 085bb61b-4870-3439-b0a7-0187582a38c1 | -8.86771 | -47.16212 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9588bb1f-d30d-3bc1-9a1f-47cfbde4aae9 | -9.1098 | -49.63445 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abf47ded-5266-3146-a870-3ff733e3417c | -8.15157 | -45.05509 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c979108-d016-38ae-8969-aff4826f217a | -7.16807 | -43.85712 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae7da11e-074e-3aa8-a1a2-4c414ba251ff | -9.07152 | -49.6034 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4010e8b7-2f29-3680-bfe9-ed94acd0e346 | -5.75997 | -53.77156 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32178c59-a9c5-3ec7-9924-5dd64776485f | -11.6454 | -44.86238 | 2025-08-27 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb7cfe9c-9592-3fa3-99b5-ad9f9309c012 | -9.07219 | -49.59942 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4e7a725-7c95-3a66-8518-f0186877b131 | -9.56282 | -55.38341 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1e89efc-c844-3c7c-bdc0-5cb491e85920 | -4.56237 | -55.9628 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0980de11-6861-3269-8483-ef7835ca1931 | -9.6033 | -40.57822 | 2025-08-27 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4734d2e0-beb1-397a-bb00-b8788867992d | -9.30443 | -48.27456 | 2025-08-27 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c1a4abf-2685-3ecf-bdfa-553d5ef482a9 | -8.88665 | -60.76023 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04f4d005-225d-3017-ad03-55298595d7e9 | -5.63026 | -45.72184 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef5cd0a7-9508-3ad9-83e8-2fb3df55a97f | -11.10205 | -44.75237 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e30f2889-48da-3a05-af8c-e9e5d0a2d966 | -8.15214 | -45.0514 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 426d64a9-6376-3f67-8c10-2e27fe86d8c4 | -11.58574 | -46.38721 | 2025-08-27 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2846bbbe-a81d-34ad-8750-ea098ac7856f | -10.31361 | -46.80079 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7500d9a-c5c7-39c8-abf9-ec8c4596d6e7 | -9.08673 | -49.57733 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e0d2072-1f47-3e40-8887-35229ef6c628 | -5.1167 | -43.20168 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b85f01a-e6d5-3d78-a04c-7bbc00391de4 | -9.55829 | -55.37989 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe9fc51c-7923-36bc-9324-96e32cbfaeef | -10.08168 | -47.26115 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ee1ad80-6a42-3291-8664-b9e4d5268dcd | -8.45891 | -43.68738 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15abc809-be4b-3e10-8672-c6cfbe2ea3d2 | -6.05519 | -43.68606 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e87dfb0b-76b0-3726-b4b5-40103f98af5b | -6.71141 | -58.56307 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daaa76ca-6f92-3824-b2b6-af01f909c91c | -9.16209 | -59.51905 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17d90c8b-988d-302b-9d76-4ccac2dcc05b | -8.69153 | -47.202 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 893c6a82-05cf-370e-800a-9f330a8da1cc | -9.16095 | -59.55941 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1d03daeb-bfe3-3e38-b2e0-6496f18b1014 | -9.15885 | -59.57012 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 323373ed-5741-3134-af91-51ba6a121ba3 | -6.51821 | -42.97894 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e240016-4e07-3991-a81b-1470de9b4968 | -8.26958 | -45.06212 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa256aa3-3104-322b-9b1c-28ffaa51b597 | -8.08533 | -45.011 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7f37ef5-1f36-3347-b799-e30d5eeff4bb | -7.73979 | -51.13563 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beefed69-24c4-3a0b-b75e-2c1c8d760215 | -9.08607 | -49.58129 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5010f18-f64a-3eb1-8db9-c5be361c06a1 | -9.58488 | -55.37552 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01e19c46-d613-390a-a73a-adc23ea75ed3 | -8.25318 | -45.12316 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README37.md)
