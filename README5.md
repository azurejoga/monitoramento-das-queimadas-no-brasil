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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8e5bc31-869f-3039-bfee-cbb84da5f394 | -11.5587 | -47.0966 | 2025-07-18 01:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 944c40cf-e110-3429-b355-76ac07e22cc5 | -3.1198 | -47.0075 | 2025-07-18 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5e1a664d-95c7-3b89-88e6-e866de75ea7d | -11.7317 | -48.1849 | 2025-07-18 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 86b8622d-baf4-3fad-a07b-31efd52a0e1e | -8.0883 | -43.1667 | 2025-07-18 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| de0f9f1a-d53c-30c2-a137-d44ea93c82e2 | -8.0693 | -43.1687 | 2025-07-18 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 1082854c-b1af-3e46-998c-260f015eb907 | -11.559 | -47.0742 | 2025-07-18 01:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 62e7c602-1d04-3d6f-be4e-e9881fbca674 | -8.0696 | -43.1452 | 2025-07-18 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 29db278e-effe-32e7-a530-4b0cd1846f4e | -5.6754 | -43.7147 | 2025-07-18 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 04e705c3-7b1d-3b1d-ad31-9538b288159f | -5.6379 | -43.7175 | 2025-07-18 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3a3dcca3-7771-3774-aefe-62fc32da471b | -3.3958 | -47.4785 | 2025-07-18 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 0e86718e-7fd2-3939-87cc-0e195afffd65 | -3.3772 | -47.4792 | 2025-07-18 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2fc5a9ce-5208-3f71-87c9-8269fa2e545d | -5.6567 | -43.7161 | 2025-07-18 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 264.4 |
| ded8f9e7-14a8-372e-bbbf-2e12aa7132cd | -8.0886 | -43.1431 | 2025-07-18 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 264.0 |
| 369f4076-1a33-3526-b50f-6e29fa7c45df | -11.559 | -47.0742 | 2025-07-18 01:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f679f693-5cd4-3bf9-bd96-114fc6f3cfa1 | -8.0883 | -43.1667 | 2025-07-18 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| a4ae4b8f-b570-334f-81ff-3f2efa05a57c | -5.6567 | -43.7161 | 2025-07-18 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 77565a6f-e3a9-37c8-b1c4-02c0106d1939 | -3.3958 | -47.4785 | 2025-07-18 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| ac7ce0fc-93fd-303d-a4a7-94532d29d6e9 | -11.7317 | -48.1849 | 2025-07-18 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6bcbfcfd-d4f4-377f-8858-d52b037fcb19 | -3.3772 | -47.4792 | 2025-07-18 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8f7f4410-77bc-3b24-936b-534c10ac8834 | -5.6569 | -43.6929 | 2025-07-18 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ac4c97ca-c8e9-3462-9cdf-9bf1646a727f | -20.038 | -41.6611 | 2025-07-18 01:50:00 | GOES-19 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| 265fd326-14e3-39a7-8796-c784d9bb5181 | -5.6379 | -43.7175 | 2025-07-18 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| d5c3910e-0667-346a-8362-0e8283772ea5 | -8.1075 | -43.1411 | 2025-07-18 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 86decf97-e14f-306b-9fde-cf7955299308 | -3.1198 | -47.0075 | 2025-07-18 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 4b938945-f23d-3e1d-b5bf-0dfe5c2f8404 | -8.0696 | -43.1452 | 2025-07-18 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| b905abc0-9269-30dd-9016-8abd25ea262b | -8.0886 | -43.1431 | 2025-07-18 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 229.6 |
| 39775a71-1c84-3901-94d3-0a501d10a1fd | -3.3957 | -47.5003 | 2025-07-18 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ba176e02-be90-3f15-9759-b39939751390 | -5.6569 | -43.6929 | 2025-07-18 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a1708fa0-bddc-3f06-aa1c-6dd0123494cf | -11.559 | -47.0742 | 2025-07-18 02:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 6cd344b0-3ad4-35d1-bd15-8942220fe5c2 | -5.6379 | -43.7175 | 2025-07-18 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 69cb1fb6-4bfa-320c-babd-7bc498f9caa2 | -5.6567 | -43.7161 | 2025-07-18 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 236.8 |
| c68ab0cb-4707-3795-9ccb-3e835bb93d46 | -8.0886 | -43.1431 | 2025-07-18 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.5 |
| 529e80a7-4392-334d-9c47-258eab81fc1e | -5.6565 | -43.7393 | 2025-07-18 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e86bd359-cc27-3ceb-9ccc-18d5afe202c6 | -8.0883 | -43.1667 | 2025-07-18 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 8e3a8c30-4908-32cf-ac90-f94754955ba1 | -11.7317 | -48.1849 | 2025-07-18 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e1ba4e93-d959-3ac2-9f88-8be8e66ff708 | -8.0696 | -43.1452 | 2025-07-18 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| aa60824a-854c-3226-95d8-3c4b5f90a1a0 | -8.1075 | -43.1411 | 2025-07-18 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| a734c016-ae3b-3709-95f5-ef42381b8d9e | -3.3958 | -47.4785 | 2025-07-18 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 95d207e1-c275-30cb-8782-e5d753a3f0d3 | -3.3772 | -47.4792 | 2025-07-18 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 0d2ff037-b018-3f52-a9ef-9ad25aa90e81 | -3.3957 | -47.5003 | 2025-07-18 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2bebb788-fa71-36c1-9a71-e683ee3ea6cd | -5.6569 | -43.6929 | 2025-07-18 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 845ab032-7a83-3224-87f4-914b3245c761 | -8.1075 | -43.1411 | 2025-07-18 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| ad9b4507-cf54-3bcf-b29b-ba2a001da832 | -5.6565 | -43.7393 | 2025-07-18 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a6b69717-3590-3597-924b-91c1b45dc3b9 | -8.0883 | -43.1667 | 2025-07-18 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 976e1b6d-8098-3e3b-9692-281963bcca55 | -11.7317 | -48.1849 | 2025-07-18 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| a95f6374-6ccf-35d0-a2cb-e188f469c3d6 | -11.7508 | -48.1825 | 2025-07-18 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| ea6e6d27-e14e-35b5-ad7f-d863aa527c4d | -5.6379 | -43.7175 | 2025-07-18 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0207970f-9f51-36d7-b340-1461b90af76f | -3.3957 | -47.5003 | 2025-07-18 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 7f9d59c6-6e72-38cc-a9da-af7af0e2379d | -3.3958 | -47.4785 | 2025-07-18 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| b3dde616-6328-36a8-8fb6-2f38261e8554 | -5.6567 | -43.7161 | 2025-07-18 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 60fb28d1-53c0-3f0c-ac7b-12fcc3567efb | -8.0696 | -43.1452 | 2025-07-18 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| 011cc042-c3e3-3dff-8fb9-31623672a348 | -8.0886 | -43.1431 | 2025-07-18 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 184.3 |
| 328babb0-3d3d-32c7-9bc3-479020649609 | -11.7508 | -48.1825 | 2025-07-18 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 91d33e25-6fb6-31fb-8dad-cbcbbe3274dc | -3.3957 | -47.5003 | 2025-07-18 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 6a0ce2ac-4733-3188-8412-a360947de950 | -8.0886 | -43.1431 | 2025-07-18 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.6 |
| 7ba94d50-ea49-3c7a-826a-20b3b79a3379 | -3.1198 | -47.0075 | 2025-07-18 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b2d9d789-2272-32ea-97ea-c5a954e7e8ca | -3.3958 | -47.4785 | 2025-07-18 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| f8b004df-07a8-322d-9857-931556c78f34 | -5.6379 | -43.7175 | 2025-07-18 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 43a76208-a474-38f7-9b07-f9602dd27db3 | -5.6567 | -43.7161 | 2025-07-18 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 20a96dda-c2d4-3041-b4f9-3ef9641a651f | -5.6569 | -43.6929 | 2025-07-18 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2b79830f-c0dd-318f-b17e-c86d626b0beb | -3.3772 | -47.4792 | 2025-07-18 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| da29735e-cdf5-33ca-9a96-2cc3c973970e | -8.0883 | -43.1667 | 2025-07-18 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 23e50be3-f7fa-3953-b57d-341b2aae1db2 | -3.3772 | -47.4792 | 2025-07-18 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4393991a-52e8-38c4-95a6-4b1d87d77efd | -5.6379 | -43.7175 | 2025-07-18 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| f682bad0-3750-3c67-a0eb-81bdcfdfed97 | -7.5988 | -46.308 | 2025-07-18 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 9b4f839c-9a19-31b9-9a2b-e93d2a770f04 | -5.6567 | -43.7161 | 2025-07-18 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 1d6ed947-b823-31f7-9898-fda880e90987 | -3.3958 | -47.4785 | 2025-07-18 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 75c517b9-2268-354f-b126-136fe560468a | -8.0886 | -43.1431 | 2025-07-18 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.7 |
| f9b9bc79-da50-33c1-86b1-5cde6540ad01 | -3.3957 | -47.5003 | 2025-07-18 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8fbdd5cd-e02c-3729-b675-4f39bec7e1b6 | -5.6569 | -43.6929 | 2025-07-18 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 84b7ab47-b805-3c95-bc68-ab868ff41f4e | -8.0883 | -43.1667 | 2025-07-18 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| f0fb79ec-2228-35cf-97bd-953391583019 | -8.0696 | -43.1452 | 2025-07-18 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.5 |
| 06ce38f5-41ce-392d-8216-07a2ab44b261 | -11.7317 | -48.1849 | 2025-07-18 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| cffd9958-51bb-3605-8609-bfc55e619eb7 | -3.3958 | -47.4785 | 2025-07-18 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| ba1f6a62-9402-3079-af59-16ec60ef5f69 | -11.7508 | -48.1825 | 2025-07-18 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 25e9ecd0-beb4-3a2d-b1e9-fb9bab520072 | -5.6567 | -43.7161 | 2025-07-18 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 9250f5ea-2463-3fb8-b4c2-5aafae6c5a58 | -11.7317 | -48.1849 | 2025-07-18 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2394f88b-1ba2-32b0-844a-c2be0ac86ba9 | -3.3772 | -47.4792 | 2025-07-18 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a37bf5b2-10d3-3726-b75b-9b2f952654d8 | -3.3957 | -47.5003 | 2025-07-18 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cdc45b15-9edf-3836-9430-f668c6d507bf | -8.0886 | -43.1431 | 2025-07-18 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| b1ca2745-a385-34c6-a346-e16705744f32 | -8.0883 | -43.1667 | 2025-07-18 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| ad499f00-96a1-3fa8-8cdf-74022d930d6b | -5.6379 | -43.7175 | 2025-07-18 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 43bcead9-1eb0-3e43-b9c7-15368fa33984 | -11.559 | -47.0742 | 2025-07-18 02:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| af5e1816-6259-3a96-a328-e14a8d4ea3c7 | -3.3958 | -47.4785 | 2025-07-18 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| c99604de-26f8-3b4f-a049-bfde03f15e5d | -5.6379 | -43.7175 | 2025-07-18 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f055e083-febb-34ad-a6e8-b5dd831a292d | -8.0886 | -43.1431 | 2025-07-18 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 3ebed972-d764-3f36-b388-35976c6f17dc | -11.7317 | -48.1849 | 2025-07-18 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 03922b40-7148-373d-a3e1-6256646090b6 | -5.6567 | -43.7161 | 2025-07-18 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 169.5 |
| a0c9025c-6c3c-3d61-b446-7f3e503d4f61 | -3.3957 | -47.5003 | 2025-07-18 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 44e380fe-4bae-3d7a-82ef-18a32f64b0c5 | -5.6569 | -43.6929 | 2025-07-18 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f4126593-32e3-38af-9ad0-88472d649ca3 | -5.6379 | -43.7175 | 2025-07-18 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 58cb0f5b-c8cf-3d56-ac4d-3d81fe609710 | -8.0886 | -43.1431 | 2025-07-18 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| b4735eef-382a-3de7-97fe-c01f9e7b4350 | -11.7508 | -48.1825 | 2025-07-18 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b4a5ea4f-b0a3-3d1c-aae4-bf25dc456597 | -9.5343 | -40.3282 | 2025-07-18 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 6292a32a-a0d0-3ba4-9625-a3966d4b220c | -3.3958 | -47.4785 | 2025-07-18 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 2c53456f-caac-3556-8a2c-a1d19f25047f | -5.6569 | -43.6929 | 2025-07-18 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c4964fbf-bc39-37c1-b067-82ee04179d4c | -3.3957 | -47.5003 | 2025-07-18 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 09e6be5e-6707-33ff-a163-e571ac6b9834 | -5.6567 | -43.7161 | 2025-07-18 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a83e8227-57fc-374d-a483-518710f67952 | -8.0886 | -43.1431 | 2025-07-18 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 805f9419-1a58-361e-ba7e-ed1b2709e037 | -3.3772 | -47.4792 | 2025-07-18 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |


[Clique aqui para ver as próximas entradas](README6.md)
