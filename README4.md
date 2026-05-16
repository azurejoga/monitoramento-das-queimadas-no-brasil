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
| 2204932c-e0b7-34db-ad38-ab494f105234 | -7.71384 | -44.55883 | 2026-05-16 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91f23d8d-8261-3341-a0a1-cc50e0114023 | -8.0815 | -44.13124 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64a311b6-3506-3e7b-b21f-df5ad8fc3e53 | -13.02963 | -49.93742 | 2026-05-16 04:17:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 048071b1-5ceb-39d1-b9f5-6e4898c91b5d | -11.44024 | -54.09845 | 2026-05-16 04:17:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca681bb-1847-3c40-a60d-dcce089d48f2 | -15.91337 | -41.85414 | 2026-05-16 04:17:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25de2f8a-90e3-39e6-bf1c-e000d75c158b | -7.71442 | -44.55525 | 2026-05-16 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 870108ee-950d-38fd-861f-c1a55cdd8eae | -13.53635 | -43.99844 | 2026-05-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2783031-890e-3dcc-bc01-96d55b754292 | -14.65601 | -40.99539 | 2026-05-16 04:17:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1c3289e9-5dbe-3c52-807f-35529abbcee5 | -8.08314 | -44.1423 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2e4a8a6-c00f-34d7-bffd-06c3cf552090 | -9.45476 | -47.82025 | 2026-05-16 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17ae7960-de88-3839-9a18-abb3c019feef | -8.10109 | -43.15315 | 2026-05-16 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 35bc2817-0575-3180-9ea3-56850944c807 | -8.07874 | -44.1272 | 2026-05-16 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b9e2768-54df-3d51-8e0a-5afc611e5f1f | -8.10054 | -43.15662 | 2026-05-16 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fdf03ecc-40fe-39a5-b5b2-717e5002ba31 | -11.3103 | -54.03467 | 2026-05-16 04:17:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd6617a9-91c6-3dd1-b350-14a00983049d | -9.1652 | -47.71917 | 2026-05-16 04:17:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 751951ae-211b-3624-898f-1813ff1cf47d | -8.69884 | -47.97865 | 2026-05-16 04:17:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ea3461d-a11a-3178-a583-f36ddd7fe57a | -8.69965 | -47.97379 | 2026-05-16 04:17:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db8ddb13-132c-3c54-83c1-258ec46290ee | -12.02673 | -47.80197 | 2026-05-16 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d93352c5-41c1-3271-887e-35d673323472 | -12.04397 | -45.29034 | 2026-05-16 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7c7b369-c9b5-3655-ae09-e287c535c346 | -16.16713 | -58.48651 | 2026-05-16 04:19:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6a6e411f-a382-33d8-b2fc-be3e6c1c70f5 | -12.85069 | -43.75994 | 2026-05-16 04:19:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 85e29e7d-c83d-3ccb-abcf-e839bec6f4b7 | -20.29559 | -47.15336 | 2026-05-16 04:19:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2767f4f-e705-3e6d-8598-0fdd9cee188c | -12.05122 | -45.28788 | 2026-05-16 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a22294a-8cf9-3643-9a2c-dc9b544a14d4 | -11.31165 | -42.13087 | 2026-05-16 04:19:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8825f99-c20b-3a41-9365-8b7149df7399 | -18.12187 | -44.26888 | 2026-05-16 04:19:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8a4c1ac-a01d-3d4a-8286-1d0ae8caa024 | -19.67766 | -51.37876 | 2026-05-16 04:19:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f98b66f0-505a-36b9-b9bc-852fc66fe7c2 | -11.74559 | -44.5251 | 2026-05-16 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0954627e-b2a0-37c3-8344-89ef66593fb2 | -17.36104 | -42.62885 | 2026-05-16 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 193c39b2-c435-3cef-8cdc-68e08c4fa25b | -12.05064 | -45.29146 | 2026-05-16 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b61282e6-5b63-3b9d-83e0-11335005d555 | -11.55166 | -48.27597 | 2026-05-16 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b22f068-744b-310f-9507-dafe5b336888 | -13.12315 | -43.40257 | 2026-05-16 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f2a60e5-4e71-3605-9667-0d6f74827062 | -11.93341 | -46.55943 | 2026-05-16 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d69f6a1-b999-34bc-b451-e0734a09bb1a | -17.35749 | -42.6283 | 2026-05-16 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 456038fc-fb42-391e-8dd9-82bb97b705c2 | -12.12751 | -41.10251 | 2026-05-16 04:19:00 | NOAA-20 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3280eb20-d623-38e8-8b86-b1a193f18805 | -11.97656 | -47.36514 | 2026-05-16 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cadbf542-3123-3cfd-a41b-a24273050931 | -11.59824 | -48.02747 | 2026-05-16 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77aafa45-56da-3fbd-b4f3-ec7291f4774d | -12.2581 | -38.24883 | 2026-05-16 04:19:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 23e28824-4a42-3fcf-96c5-de5ee811a9b8 | -11.59 | -48.03074 | 2026-05-16 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 318c520b-436d-398b-9dde-e0cdfa8ef6f7 | -20.54088 | -41.82795 | 2026-05-16 04:19:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 71c4b1cc-46bd-3cfd-a46a-a94aea8db249 | -11.04238 | -48.91629 | 2026-05-16 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d65ad447-0cab-3f6c-a454-e30f13407901 | -17.75552 | -47.93937 | 2026-05-16 04:19:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b78a1776-9667-3fa6-b51b-1378a2379ee4 | -17.75141 | -47.94265 | 2026-05-16 04:19:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4f5995c-f99e-3f1a-8232-2da197b002ee | -10.39587 | -49.44108 | 2026-05-16 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d0ad46-e77d-3f0d-a563-e58d9faecae3 | -10.66662 | -49.70772 | 2026-05-16 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15bb1747-6806-3980-8a13-72d7807ef0e6 | -11.74727 | -44.51455 | 2026-05-16 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55423501-7ac4-33e2-949b-c56d095d91bb | -12.92997 | -43.61907 | 2026-05-16 04:19:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a76ee8d-bd4c-3cef-bb29-ea05415e831a | -10.65824 | -49.70618 | 2026-05-16 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8fc3d386-31af-39a8-857b-bd0a6b222b89 | -12.16294 | -47.52934 | 2026-05-16 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaf45046-620e-36a1-89a5-b4f30a7051a5 | -10.79353 | -44.8471 | 2026-05-16 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3926dd6-0158-3e5a-a3f8-07cc3dd9a53b | -17.61419 | -42.60123 | 2026-05-16 04:19:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72635404-50d8-3d69-a9c4-1137ea8c4b45 | -12.12621 | -38.16777 | 2026-05-16 04:19:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 49144a04-cf28-3ea5-8085-c336e31a848b | -12.02306 | -47.80137 | 2026-05-16 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c30a82f-fb2e-3040-abd2-dc9b4cf4cbf4 | -11.74283 | -44.52104 | 2026-05-16 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cf5e39c-40a5-36dc-96d3-5094388fa9b7 | -11.97844 | -47.364 | 2026-05-16 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a82e074-02d7-3125-99f8-9637de07a819 | -11.04062 | -48.92646 | 2026-05-16 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ea70ce1-8332-356a-840a-7edb78488e08 | -12.0473 | -45.2909 | 2026-05-16 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ab9d16f-262a-305a-9a52-15074cae6433 | -11.74227 | -44.52456 | 2026-05-16 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e86f5f20-e5d9-377e-97bb-9e7687627763 | -12.30579 | -47.90622 | 2026-05-16 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1e6bb4a-2940-31d8-b972-b01950f6a1c9 | -11.97586 | -47.36932 | 2026-05-16 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 740e827e-e71a-3fc0-9c30-fb5eac741cb6 | -11.08179 | -48.25052 | 2026-05-16 04:19:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a501bd1e-c0c6-375b-a8ef-b4132863143e | -11.59078 | -48.02618 | 2026-05-16 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78f0bf94-66e2-3a45-8245-0d2d171cd6ea | -17.34743 | -42.62242 | 2026-05-16 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63c585f0-6a9d-352a-8978-60b1f19014f0 | -19.98208 | -47.20077 | 2026-05-16 04:19:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6702367b-ea58-36bc-b703-58a72a04b431 | -11.74671 | -44.51807 | 2026-05-16 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3e42431-69b7-319a-a42a-ea0b522e7c18 | -17.35098 | -42.62298 | 2026-05-16 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 344492d6-578b-3889-ab3f-fef569fbeefa | -12.25867 | -38.2447 | 2026-05-16 04:19:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e248506e-38c2-3a67-9734-578b4294d492 | -10.6673 | -49.70382 | 2026-05-16 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 782dc8c7-2b12-3096-970f-84dfa7416e7c | -11.97772 | -47.36818 | 2026-05-16 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b914108c-7127-38e7-b914-3827f27b30f0 | -11.03973 | -48.93167 | 2026-05-16 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7484b6c2-2ab1-3449-905e-de7b7f3a8f2a | -17.86332 | -51.78391 | 2026-05-16 04:19:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9c2f4f2-eb0b-33ef-864b-ab53b5acf6c5 | -10.66311 | -49.70305 | 2026-05-16 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5e79809-7739-37c1-81ee-72ae04d082c3 | -10.97759 | -45.09621 | 2026-05-16 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb6fc1b-f169-312d-ac42-d6afc4f18531 | -17.25248 | -47.08046 | 2026-05-16 04:19:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 262c737a-2fde-319e-ae47-3bc70205ca0c | -20.53844 | -41.83148 | 2026-05-16 04:19:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69469757-e90c-3771-bc89-416529f7217d | -10.66243 | -49.70695 | 2026-05-16 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9b957bc-f70e-3c02-b7f2-8be2e332f21a | -11.0415 | -48.92137 | 2026-05-16 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c12d70c-992c-3dcc-b386-2d396dc760c8 | -17.6148 | -42.59703 | 2026-05-16 04:19:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8b5d58c0-710a-3b1b-9652-c63ae8627120 | -10.4 | -49.44183 | 2026-05-16 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 705be87c-ed1f-3531-b481-b90057e0b8cf | -12.61152 | -44.52646 | 2026-05-16 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b8c6b7f-2943-3c8b-a4ee-79a013aeb4c4 | -17.34803 | -42.61824 | 2026-05-16 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f843bff-d8ca-315f-ba90-2cde7fd94c16 | -12.04672 | -45.29448 | 2026-05-16 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fef449af-d31a-3674-8d5e-83b0585f620c | -12.62145 | -44.5281 | 2026-05-16 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ae38efa-9404-3648-a1b5-2c0fc67a1ffc | -11.59373 | -48.03138 | 2026-05-16 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b965ee0-6050-3c03-a132-bc65587c19b1 | -11.8333 | -46.67914 | 2026-05-16 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 49bac1e0-25f4-3416-8432-a79c733dc0fa | -11.59451 | -48.02683 | 2026-05-16 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44743417-c7ec-369f-bf7d-31231c3c7792 | -16.16847 | -58.48055 | 2026-05-16 04:19:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c1d6f97b-2fe5-3342-8ce8-c109e0b205a2 | -12.05456 | -45.28844 | 2026-05-16 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f913a2c-b0fe-3038-8fee-7b383d6b65b5 | -11.31807 | -42.29728 | 2026-05-16 04:19:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b89681c5-8b61-31ff-b2f1-b46ca4d1406f | -28.77693 | -50.12481 | 2026-05-16 04:21:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d37f9bfc-ffe0-353e-ad9d-08ae28f3bf43 | -28.99659 | -51.28223 | 2026-05-16 04:21:00 | NOAA-20 | NOVA PÁDUA | RIO GRANDE DO SUL | Brasil | 4313086 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| de5f6667-1847-3679-a5ef-309f34e949cc | -8.1068 | -43.15978 | 2026-05-16 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0623c444-cfa4-3f72-a6f1-5d83897d0d00 | -8.10004 | -43.15883 | 2026-05-16 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 713740dd-ffef-3b45-b959-a40fff996904 | -7.27625 | -46.80018 | 2026-05-16 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 900e5b82-3747-38dd-90f8-7e204c973a61 | -8.10756 | -43.15374 | 2026-05-16 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b17b81a2-c31b-3937-ba77-b3e1b5de5a18 | -8.08206 | -44.13549 | 2026-05-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 950db89c-4c04-3595-9452-74a1e5c2ab49 | -7.07493 | -52.72946 | 2026-05-16 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe1c410-e4f9-3b17-bf78-fb746e5b5f8a | -8.08138 | -44.1408 | 2026-05-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e372dfde-62f6-3145-bc2e-4cdcceca1837 | -8.08274 | -44.13016 | 2026-05-16 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f07e5f6-6e6e-3f60-bb3b-7d74e81ab258 | -9.4542 | -46.10641 | 2026-05-16 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53036434-ce46-3bab-9acb-021bdc082c69 | -12.85424 | -43.76391 | 2026-05-16 05:06:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README5.md)
