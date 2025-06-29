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
| 5c04cd88-0e37-31f0-a164-e7e58091dda3 | -7.29666 | -55.3196 | 2025-06-29 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d75fe152-0594-3758-80b4-bf9b6eba38d9 | -10.56786 | -52.04323 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6632ad6-efd1-398a-b834-7263bb6f443f | -10.55181 | -52.04155 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e310b110-8bf3-3060-8f4a-fefce09b37ca | -9.64301 | -48.79055 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dee0ed0f-da60-305b-bd46-00d728d5403e | -10.86411 | -53.75143 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16b6b35c-4501-3ba7-af24-f383857266b5 | -9.10649 | -59.04852 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b7cae45-40f5-3e1c-820f-56cb1a25fece | -10.56192 | -52.04763 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 06232e86-8ec8-3009-b3a3-4bf40d438564 | -10.03566 | -54.33464 | 2025-06-29 04:32:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee0dd46f-dc74-3249-895e-b9d458d8f061 | -10.5705 | -52.04046 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742e1b81-62d5-3195-a504-ecc44e82c29c | -7.19314 | -43.70657 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07eae4c9-dfb9-3a37-b618-84c58c03d3fe | -10.55112 | -52.04576 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 632eba7e-7046-3c10-9cc4-53291f93daf1 | -10.56497 | -52.03841 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bf9a2dc-0096-3331-920f-d5f06be7a585 | -10.55541 | -52.04217 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 41eb2986-d0a5-35b3-bfd5-bf205fc353e9 | -10.29807 | -57.1369 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b039578-2bbc-3d72-89a0-094082d3aecf | -10.29252 | -57.13902 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c23bdeaf-b38d-3af1-8662-8a543330a34a | -7.54724 | -45.85094 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 69811fea-c2e5-3e08-89cb-408f3a11717e | -10.16064 | -53.92553 | 2025-06-29 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fb197f1-67d3-38e0-805d-0eb33c925df7 | -9.15524 | -46.3536 | 2025-06-29 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d55eee25-f08d-3b4f-8f35-c769b975b0a8 | -10.55901 | -52.04279 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 38b40589-45c1-3452-9c10-4b5729690984 | -4.09965 | -48.19911 | 2025-06-29 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3333dcf0-cf43-3200-8745-44687fbf9f32 | -12.12959 | -45.57074 | 2025-06-29 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b950beb-45e2-3792-bd72-162234493c3c | -6.51491 | -44.43163 | 2025-06-29 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4dbc3f4-0659-30d0-9e90-03f1e235a826 | -9.52507 | -54.77554 | 2025-06-29 04:32:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46914fd9-bd33-3e2b-b5b3-ab6533b7545f | -9.43521 | -47.94957 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b741520-0529-33c8-a03c-6d064c78609c | -11.49319 | -48.0773 | 2025-06-29 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2952c219-5b21-3970-aa64-c018345462f6 | -4.45776 | -48.99864 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97d72544-0408-3d5a-95ad-158fe0ecc8a0 | -10.87377 | -53.74267 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdb8443e-4253-34e3-bfe5-e562ce8fb6bd | -7.55302 | -45.83615 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da843783-b61e-385a-99df-6fb5d13afe29 | -4.47969 | -48.30915 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd5b16b4-5f79-3ee9-bc9f-a97b0c1dce65 | -8.36427 | -51.08251 | 2025-06-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 085890a3-b382-3da6-936c-6656013f5fe5 | -4.55849 | -48.0048 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf1b4958-1287-3276-ae0b-c3bc1ae4b51c | -12.18179 | -44.34091 | 2025-06-29 04:32:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e99c20be-7795-3d96-8d89-f246952d35a5 | -7.54782 | -45.8471 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ba11a43-a743-33cd-9000-f9e5fcf28607 | -10.29859 | -57.13404 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e0778e7-fd8f-3f19-b56f-8f860965b137 | -6.89668 | -43.9785 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00443a87-b757-3714-aed1-1934c72d4bcc | -9.46654 | -40.34311 | 2025-06-29 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f724deaa-5ba0-37dd-9e71-7269bb2926b6 | -11.05212 | -44.35046 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc75e9e-466b-3b8f-aa74-957537b16091 | -10.8347 | -53.75669 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa913b5a-b73d-398f-9439-cddc2a375bca | -7.22591 | -43.51545 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f40d6142-4681-32de-8081-64918ea7a957 | -10.83076 | -53.75597 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8880e02b-0cca-34af-89ae-eada42e8aebb | -8.09049 | -46.85707 | 2025-06-29 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e77ccca4-eafe-3412-a8d8-c5aebce4afed | -10.03633 | -54.33079 | 2025-06-29 04:32:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11029074-dff0-349b-9a3f-273f0dc3dd62 | -11.78869 | -48.29502 | 2025-06-29 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d75fdcc7-94f7-38a8-ae30-683b279a2f5e | -9.42802 | -47.95205 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e0676796-4505-3a98-a820-27a80832d208 | -10.55042 | -52.04997 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| af1017eb-c9e7-3ad2-a6db-cac705addfa7 | -10.80084 | -48.29503 | 2025-06-29 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e136d040-9c31-380c-8783-e36f5f1d836e | -7.55708 | -45.83283 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5726f1f3-dd90-3c69-9990-f8cf9adf3a1c | -10.5669 | -52.03983 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e80989f4-8715-393b-8f42-a6a71268d019 | -7.55767 | -45.82894 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f35579a4-df74-3731-8af9-6767790b4a3e | -7.85633 | -47.90409 | 2025-06-29 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81dafd0e-8d95-3c87-b794-cffdcbb7952a | -10.56928 | -52.03485 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f14730e-d6aa-366d-bfef-f599b639053d | -10.94871 | -49.25594 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0c92787-abea-3f9d-af35-88ff02c63c7f | -6.89738 | -43.97381 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6079462-e03a-33e6-ba64-d7dc697faa72 | -4.54197 | -48.02347 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a853965-4294-362f-a1e9-0454ac139224 | -10.79475 | -48.29044 | 2025-06-29 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f88513ab-bcd7-3062-9e5e-6cbfcbd35daa | -10.95532 | -48.15291 | 2025-06-29 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32cb6791-7790-3020-9dab-f36ab472cc24 | -10.5633 | -52.03921 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad589736-02ba-38bb-985d-eeefe69c9efe | -5.54982 | -46.29579 | 2025-06-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1c7c292-b69b-3284-9d59-933a76accace | -11.83423 | -47.52388 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b82f827-dfc3-3f9e-9e5a-c7a3e40b9649 | -10.55251 | -52.03736 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 626b9521-2ad4-3b34-8428-eb90e9a05fe0 | -7.55419 | -45.8284 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a58a994d-ec2a-312b-9a52-88e88ee39a5a | -5.79353 | -46.30322 | 2025-06-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dbef72d-d61c-3078-818b-2ee5b1487953 | -9.71625 | -56.18422 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bd306b41-0f3c-36a5-a111-dc8d6c8780f5 | -8.30812 | -49.48961 | 2025-06-29 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8f290e9-015b-39f4-9125-74df6349a693 | -10.97814 | -45.10706 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cae17012-e837-35b3-8341-a52cfd2f9825 | -9.4203 | -47.95799 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2aa1ec9c-e6e6-3b91-be4c-d2ecc4a42837 | -8.0933 | -46.86123 | 2025-06-29 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deb1f2b8-6b23-3846-88d9-047f7c9202cf | -11.57718 | -44.83165 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddfc64f9-2696-3a46-97a6-6ef9f16c3432 | -11.84272 | -47.53661 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69fa6f18-f3f7-3747-9afd-021b8cb9cedd | -9.78628 | -48.57075 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0c7a092-e176-3ddc-85b4-9d4a9efde6e4 | -7.19167 | -43.71633 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff04456b-cb0f-31be-a111-b3b7c875588b | -10.09855 | -52.19763 | 2025-06-29 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8be75915-4912-3959-96f9-4be48b890d13 | -4.81365 | -43.21951 | 2025-06-29 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d2faa86-cf6b-3136-82b5-9fca0998ae9e | -6.449 | -44.57126 | 2025-06-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2e353cc-1481-307a-a035-4693396d8790 | -10.97441 | -45.10648 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3d4baa9-0c9c-391b-a5d8-f379e328d47f | -7.21781 | -43.07581 | 2025-06-29 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f7a8bb34-ba13-3ff9-adf1-358513dee30a | -7.10094 | -44.3659 | 2025-06-29 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a4d03a-c881-325f-bada-3974d90f02c6 | -9.14657 | -46.38736 | 2025-06-29 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1160150-24e5-300c-bbf9-eb6b58703300 | -10.30015 | -57.12544 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e63ad802-b644-3d23-a56a-2f05e9a19067 | -5.4155 | -47.56814 | 2025-06-29 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d995541e-c24f-3d3d-8ed4-8d7260f4141e | -6.90876 | -43.97549 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecc09552-f84c-3d3f-b44f-a0881f449acf | -11.84279 | -43.79996 | 2025-06-29 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9288023d-7232-3c26-ab10-ea04a6df0189 | -10.54601 | -52.03192 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49207d6b-b54e-367f-a403-c7b46873a952 | -9.64246 | -48.79403 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e15ae2d9-a42b-39d2-a94d-8dbc344c8f03 | -9.98117 | -47.80059 | 2025-06-29 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 203272b4-96fb-3dff-80ba-18901be75173 | -5.18881 | -47.73722 | 2025-06-29 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40609bba-a78d-3af2-ac56-316320a19c55 | -10.29213 | -57.0288 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f7deffa-25b1-38ad-84bf-7e117cfb2cde | -9.11724 | -59.05494 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fcfe04c-d643-324d-90ec-7bbb73247203 | -5.08737 | -48.35544 | 2025-06-29 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da67d70d-45c2-3913-b0b1-b9dc32dca1d6 | -4.5392 | -48.01949 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8b8161c-2fd8-3250-971a-3c7178990117 | -9.0832 | -59.49205 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 110ef41c-7d66-3fef-8c06-5478bb547c67 | -11.57651 | -44.83646 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e3fb40e-63e3-350f-b97d-8adeddd9f4f7 | -7.0979 | -44.36091 | 2025-06-29 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 104cc8c7-5600-3bfc-b482-6c8a7f6ab695 | -8.36074 | -51.08196 | 2025-06-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a0fa56-57b1-30f1-b106-e6ac61300e49 | -10.56354 | -52.04681 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b175f40b-5432-3e4c-a621-62284cc1aac8 | -4.54251 | -48.02002 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0b4d326-c2f8-394e-8321-ae382d8ea7c0 | -7.08466 | -44.32274 | 2025-06-29 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35d85b28-f171-36b8-9d9f-8decd8414659 | -9.47225 | -57.83661 | 2025-06-29 04:32:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 301b869b-0aca-33bd-ac9d-1eee7ef333c4 | -7.40068 | -44.57579 | 2025-06-29 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c0b4283-488b-3577-80d0-c473e19a4521 | -10.56282 | -52.05101 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README19.md)
