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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d006aae-dd00-3c5d-8d9d-3b921126cfe6 | -11.64249 | -44.04536 | 2025-10-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06dd6d6c-d9a9-30f4-ad92-ae16e558d8b3 | -9.93582 | -47.19222 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbd296ae-19d8-3cf6-8068-74246424c151 | -6.11675 | -41.71136 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a09f6905-3f51-35f4-864f-83d5c9be63c9 | -7.06288 | -44.94973 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3330713-b9e3-3e2e-8539-c6556c5cba76 | -10.96087 | -47.83986 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a3b6cda-29c0-38b9-ac9d-47305d8e1aac | -10.98621 | -47.87282 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6629911-9783-38a6-83e5-6b89103a06a7 | -6.13816 | -41.6748 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a43ccae-ac15-3322-a812-d28c325f6e49 | -9.00797 | -47.99932 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 228d2cbe-dc78-3485-93de-d68481b41748 | -7.87757 | -46.73679 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a6c9827-801f-3027-923a-5f0e79b7408b | -4.35684 | -48.19542 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09d91fa4-5230-35ae-b66a-6a386ac78f99 | -6.13825 | -41.56938 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c2d72544-3234-3877-af55-d5f68fb2c609 | -4.46425 | -45.75999 | 2025-10-30 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6152f89-1e76-3a2d-af68-38418ed65b22 | -7.32671 | -47.25244 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f36af3d1-0b31-3377-860c-045bc2479e25 | -5.65592 | -45.98 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a43d9bd-1a3d-3b6e-bfae-f57a322844b2 | -8.29284 | -49.31409 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2b90016-2c9e-35b3-9256-0fd1b0b8b0ce | -6.12401 | -41.86087 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b70e6d1-1d0b-39ad-b9e2-142f3e238a68 | -9.85914 | -40.59242 | 2025-10-30 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91be6536-17d4-36fe-bd35-b8775a643cbd | -5.29077 | -44.21357 | 2025-10-30 04:25:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0571a843-3570-36f8-91f0-8de0e87aa080 | -7.3003 | -47.43985 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7d9cc7b-0135-398f-b1a8-6eb9a61e7034 | -6.1352 | -41.69421 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ddb48bc3-c248-3970-b3c4-f829493888bb | -6.53454 | -43.56905 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2f67e57-a157-33e6-8b3d-e8442810018b | -4.8375 | -45.35241 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e83187a-4b70-317f-b8f8-584c67f64a73 | -11.03218 | -47.84066 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 736fe296-05e8-369d-9e3c-8f552360ad52 | -5.68135 | -49.14882 | 2025-10-30 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1705a77c-06a1-3ab5-9e50-b401d8c10f06 | -8.62706 | -51.59364 | 2025-10-30 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6690bf83-a22f-322b-8205-62b6b5b476a0 | -10.65073 | -47.76083 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88089017-95fe-321b-9ad7-ce2afb0603c6 | -5.51542 | -41.23341 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa451dfe-78c7-38c3-89f7-2f37504f6802 | -7.5958 | -45.84981 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59b3531c-4fc6-3657-9001-3c8bc4977c08 | -5.92989 | -44.72852 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43fa7ae1-df02-3422-86b8-7ebfb4b37517 | -7.14699 | -40.24858 | 2025-10-30 04:25:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0167b7d-152b-3ae0-89d5-78bf4739d8fc | -7.06678 | -44.94672 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7decff7d-6e68-309c-a705-f3caa6d5b2c2 | -6.14507 | -41.71726 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0283014a-e8fc-34a9-a5de-d2308eb6738b | -6.14854 | -41.58058 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e0dc4877-6a82-3e1b-a5c0-2e367f83c130 | -5.42738 | -45.3385 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9324587-5aba-3feb-a81f-8a3b32714b63 | -10.73905 | -44.74067 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dabaa05-321b-3649-be49-e74e62d06135 | -6.1369 | -41.70903 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3b6823e9-18e7-3126-a369-92ea7011f7c8 | -5.4174 | -44.83848 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3761a72a-12f3-3ee6-bee8-3705402bd995 | -7.13389 | -44.71245 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcdc2c3e-5bf0-38a2-a29c-2ea9469c7b0d | -6.13908 | -41.69478 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5693a35-c79a-3f64-b373-3b89f2f9cfe9 | -6.53043 | -43.57241 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2287d626-402f-3f76-bffa-68ed171903d0 | -3.66395 | -51.71546 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42ab5d7e-70fc-353d-9132-ce4da4f71f97 | -5.96405 | -44.73012 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b6ca302-ab31-300f-a9f1-f287c1ec3b23 | -10.3509 | -44.07071 | 2025-10-30 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b775cba5-e630-3fcf-a918-9144f77fe293 | -8.70247 | -47.91314 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1fbe2e5-a594-3834-8689-caf8f7a873bb | -10.95898 | -48.04264 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9732bac7-1a2d-3a9f-9b21-0663b78049af | -5.81088 | -43.59175 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a391108-bc79-3192-9faf-1e8444c86131 | -11.14423 | -51.0685 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2034bb8a-ce39-334c-a7cb-86844c3bc227 | -10.59598 | -49.62004 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44e476a8-9787-3685-a286-3056777b2c58 | -7.14224 | -40.46361 | 2025-10-30 04:25:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2994efae-f609-3edd-a0c3-c6706cfe727b | -5.41254 | -46.01546 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0224fa7e-01d9-3040-a530-717219a0803c | -5.59196 | -42.77677 | 2025-10-30 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3644cb8a-332c-310b-9c01-09fbc9815d06 | -4.84637 | -45.59765 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75058ce3-1dbc-3c60-8dd8-19d6b298e752 | -11.03549 | -47.84123 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9e2cc50-5b3f-3bb2-a6d7-2879029d7156 | -5.0268 | -44.81456 | 2025-10-30 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2989fc79-3c2a-3812-9088-9429ce85461f | -10.77261 | -47.82708 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cf9ce8a-75d4-3622-91e0-c729c972b64e | -10.84597 | -50.12149 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca510650-d5ab-3777-8766-77901cbf7637 | -9.73357 | -47.69415 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b70e09-f1ab-35aa-86c4-e3932aa37b85 | -7.70195 | -46.98612 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48e9e36d-1372-391c-84a4-2326944dcd6e | -9.9032 | -44.89671 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac0a4986-ee22-3a33-809c-1451b8af8732 | -6.85308 | -46.29686 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea6d67a0-1915-3212-8f18-e02548aa069c | -7.79243 | -46.41404 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c30575fb-75ca-3fe1-bca9-93390568ccbb | -5.9253 | -47.31904 | 2025-10-30 04:25:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f52f7a30-b622-35f1-b660-c42ddc1dfd15 | -4.96276 | -48.26057 | 2025-10-30 04:25:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f689cc6-4116-3b1f-85ab-132127bcd9ef | -10.33623 | -47.08866 | 2025-10-30 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0758532b-68e9-34e6-860b-9961516ca39f | -6.14937 | -41.60128 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 784ea195-bc3a-32bd-8c2f-ec88ff2041fb | -9.85959 | -47.69324 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c217f2e-484c-3b14-b09b-4ab30e6e51c1 | -7.33979 | -39.71684 | 2025-10-30 04:25:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 29ea2f4b-79ae-3851-9c96-8d4d74c171ae | -7.28832 | -45.66614 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b91ebb15-81d6-3d2a-8739-cad5d2ee1957 | -11.13603 | -51.07172 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 89f7f33a-a2f7-3b00-b3b8-f6e23bd0c69a | -11.07851 | -45.29607 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 612cc182-c79a-3b49-b8cc-0de5a9a5a48a | -7.37786 | -46.22062 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6639eb8-78af-35a3-b27e-646f6f8df704 | -7.26617 | -46.9056 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 873f268e-5505-3026-9884-245a1596d38e | -7.30302 | -44.97969 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a04e7396-e251-3879-836d-72f4d379eb88 | -11.04543 | -47.84295 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2120cec-81f6-39cb-a305-24beb119b9dd | -9.60622 | -47.76823 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b482af1c-8741-322d-97a8-7d0eed9aeae6 | -4.83696 | -45.35585 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b30d23c-3783-35ec-9284-764e304a80a2 | -7.79024 | -46.42789 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04f60937-4481-3541-978c-d3c6b218dc8a | -6.01737 | -41.98167 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 41fb2245-fafe-30e1-b228-7b4bdf744aa6 | -5.02735 | -44.81105 | 2025-10-30 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12daf675-c402-3c4a-8dc0-0a0be3d6a486 | -6.91401 | -45.21168 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2a096d1-71ab-3aab-ac26-89d9cdc89e37 | -9.81283 | -47.58104 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59dbf91d-608d-302e-9ab7-06b98fff4ac2 | -7.32248 | -42.49104 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f30eff3a-6875-34d9-b43b-af62b6588b4f | -8.23903 | -49.77923 | 2025-10-30 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56710490-51b2-3a9a-8b5a-0c088b59d74d | -5.79366 | -40.81965 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4765b0f-72f1-38c9-9d69-775d73d1d42a | -10.48338 | -44.00494 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 625ac696-acc0-34c2-af90-e141fd9112e0 | -6.00917 | -45.87328 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 75191d8e-d1ed-3a6d-9bb6-881bebd8d799 | -9.84687 | -47.68754 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fcad13c-53ef-3cd4-9c86-94f0c774f8f9 | -6.12897 | -41.57796 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c7a625c-f06e-3a47-915a-82cf7b34f3d1 | -5.60109 | -51.13373 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29dbd6ff-4180-3370-88b0-69a2a2f55cda | -7.13445 | -44.70883 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86e3ad24-0575-3c1f-91bd-f2dd11dea906 | -10.74482 | -44.74966 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca50cbb4-474b-328d-88d7-91219b7601c7 | -9.0112 | -48.65005 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d0ff873-183f-31ef-a402-e6cf864e50e7 | -10.27864 | -44.58533 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 527a6b95-5b19-34a5-a4cd-6024ecd21ae3 | -8.19737 | -44.44698 | 2025-10-30 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 465b73f4-9280-3208-a5d4-9dd3219d1546 | -4.55935 | -46.33987 | 2025-10-30 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 202ec2a3-6ea1-3eb2-8a21-c4f1a91bf227 | -4.86926 | -45.79917 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 170bffed-60b3-3ecf-8872-88919630a50a | -7.38246 | -47.62749 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca30c486-bbd7-325b-80fe-a7e55dab8014 | -7.78694 | -46.42737 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0eb4372-fe4d-3330-8a96-78c8829db314 | -9.39779 | -44.55648 | 2025-10-30 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d6727fd-fb62-3289-9aa3-0767b3726cad | -5.66002 | -41.10042 | 2025-10-30 04:25:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README43.md)
