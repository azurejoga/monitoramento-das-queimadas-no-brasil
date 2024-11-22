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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99ed6e0c-603a-350a-9112-a11104c12308 | -2.52705 | -46.40365 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9e3e77e-1970-3c51-9ae1-3c2a88500180 | -2.91869 | -50.31938 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55b4b964-b756-3377-8dc4-1596fcb407a2 | -5.94351 | -46.19214 | 2024-11-22 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18903a60-5b73-3bd3-8aff-9e1017ea1a38 | -2.76362 | -54.07393 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7e71815-3c6a-3297-936e-eabb8df4f756 | -3.23051 | -54.23683 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c43afd75-a182-3cf5-baac-35618b2b0cac | -2.09896 | -48.88803 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5df41622-f299-3328-a033-edcfc2e29583 | -4.07243 | -46.83324 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0997095-0d4a-3784-b726-b1cfd627c5c0 | -3.05002 | -51.33178 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b5032e6-8f6e-37ed-a32a-036d8f85b0b3 | -2.84071 | -54.01729 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74f4fe2d-4829-306a-a52e-eb8838aead1b | -1.64111 | -52.76725 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28575737-52a7-399b-a598-35b39937bacb | -2.14792 | -50.4914 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79020fee-e8e9-3785-a6ad-d7140f31d9b2 | -3.11604 | -53.70334 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6d7fc9-2c21-316d-a827-d493d2d7f7c7 | -1.19036 | -51.94925 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b77f63dc-4bb4-385b-a568-1f1e5e66b7d9 | -3.57479 | -54.68323 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20132d4e-861d-30ed-abdd-37f7332a215b | -4.98952 | -50.72381 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0276f4a-51cc-3214-aa11-642bd06a5101 | -1.81151 | -52.16353 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7e8c663e-40c3-3eba-8caf-cf15cc03865b | -0.9574 | -51.64302 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46eda770-fdf9-3f6a-93e8-a6763e028276 | -1.63584 | -52.41841 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f55c298c-abc5-3cd0-8155-8bcdcb6a5800 | -3.46739 | -45.90637 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8db058da-9d7c-35fa-83c9-923e7c046c2b | -1.4714 | -51.12407 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d18549f4-e96c-3765-96b0-00a5eb1786a1 | -3.25342 | -50.39729 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 619031b4-3ce7-3da6-92b3-91b2fc08350b | -1.28643 | -52.47013 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97b9a386-f585-325f-8efd-d75901a0263e | -3.50729 | -53.80653 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 91c630aa-11cb-385f-bdb5-143c4d940760 | -3.23824 | -54.24203 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 29afa927-9edc-3a51-b3bc-313b4237f86e | -1.07257 | -53.36836 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1b4126d6-ece0-3b15-aeb3-d8ad20fc5234 | -2.0871 | -46.28448 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d8de589-882b-3f24-afb6-4277e1776b4d | -3.55007 | -51.53624 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fc00f48-abf8-38d6-a0ca-f8e0452219b8 | -2.9019 | -48.32094 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfa75bbb-76a4-3b10-bd41-974db295686d | -2.08789 | -53.33197 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85c4ac62-4dc7-3791-853f-af68792439ad | -3.6281 | -51.25349 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f76c5f55-4179-32d0-97d3-94c0d59cb56a | -2.95425 | -48.3326 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8525b694-9fe5-3378-829f-d83dc7c18d89 | -3.19281 | -48.58798 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bdb7b507-833d-396a-88b6-5bbfaadd6c20 | -3.68606 | -51.36246 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec599ca1-a2cc-3ecd-9040-f771bb174c6a | -1.62518 | -52.41196 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21072560-9b64-3865-845a-bd9157f7de96 | -2.56407 | -46.55079 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70784466-7c4d-3133-a551-80872bac75c6 | -3.79018 | -44.0163 | 2024-11-22 04:36:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9653124d-9938-3e0a-b596-c9ac7189f5dd | -1.20455 | -51.95604 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b8bd5f79-72ed-37a5-a2bd-30427193dce7 | -3.56387 | -54.22275 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 823d7dd6-ac04-3731-b94a-19feaa618e8b | -2.28254 | -46.55742 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77a638ee-e5ca-3398-b505-8294add5c2f6 | -1.09551 | -53.16954 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a42f8cb8-d8d0-3a0b-aca3-ff19e8dfeb32 | -5.81668 | -44.75005 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f2445b-a7e3-38bc-a3f2-369f3f265c19 | -3.65722 | -51.31785 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5acd8035-3426-37a9-88dd-aa3a6a3cb56e | -2.40161 | -48.608 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2920117b-e17f-3ec8-aa07-d7d31f10a412 | -3.0965 | -53.21044 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89e1fd43-ab1d-3a70-bdd5-dc7094e2f3f9 | -2.49648 | -48.99621 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fce889d-e46a-331a-a80d-b1a18fc63f2b | -5.95134 | -44.46687 | 2024-11-22 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12d96801-b02a-3f41-b702-0c5d9ac002f4 | -3.26765 | -45.37005 | 2024-11-22 04:36:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90fa6390-6d69-3b70-91e9-219f0d4b95c1 | -1.84537 | -53.69514 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2469ba05-a1a3-36eb-a848-d99ae46f7af5 | -1.7171 | -52.49092 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b5f8159-64bd-3576-b2da-66aeee16c12a | -2.55873 | -47.32372 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05db14f1-8be0-32cb-b8e5-5c956ced3263 | -2.78498 | -51.71756 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53b4a76e-04f4-3ea6-ada5-073bafc9a38d | -2.54558 | -47.12154 | 2024-11-22 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 165cb587-366c-3ccf-9fa8-8dbd67c1e6dc | -2.24681 | -49.00691 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eefe5f5c-8860-3d7b-a9fa-a69351526f8e | -4.08441 | -46.84652 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 629c95af-3adf-30fc-b56b-792a5cde205f | -3.59261 | -43.63951 | 2024-11-22 04:36:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbdee9ed-bc10-359a-88b7-4cbde83cd526 | -1.60089 | -53.2177 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 656d4b5b-e279-3883-9b15-b5906999c58f | -3.46618 | -45.91439 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48242ad6-dc78-3c03-9b7a-438860626b95 | -2.01794 | -51.17262 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8460fe4-41ea-3a8e-b706-c54a811b7255 | -0.77013 | -51.76423 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59114bbf-8dd0-35b5-8ba7-35f8c20ddb51 | -0.81306 | -51.79573 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60b4b6dd-1a1f-3044-b4ad-f85c27af9fbf | -5.06159 | -44.22141 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90feba47-eb91-3fca-b0e4-790b11560b43 | -2.95072 | -53.71753 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a56193b3-e5ac-3802-ba4c-180eaa875aa8 | -3.18739 | -46.55198 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48d45fa3-07e3-3faf-8c3d-ad84e5b466e1 | -3.2905 | -53.85924 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 339f0c32-854a-334f-9a44-3bb45fec5331 | -3.71192 | -53.75368 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaac31ab-3304-3ed0-b1fd-aad924d6df41 | -3.28993 | -53.86283 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 891601e1-693b-3efd-8c31-4f0b04975230 | -2.86961 | -50.4056 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 60d27bee-be63-35d1-8de7-2ccf09cf3958 | -2.62019 | -48.18824 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b95dd0d0-df41-3320-9f8d-47ed8626ece4 | -1.04613 | -51.74414 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c20406c3-8abe-3a4e-a740-fca08e705565 | -2.85806 | -53.97806 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 242f2873-446d-3897-93e9-da95d658100f | -3.02843 | -53.72726 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d54b86c6-c840-3f89-983d-06d561c87e0c | -1.73322 | -52.71246 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e2bea922-fb09-34d4-90b6-2750b414004f | -1.13775 | -53.40313 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e794bef8-bda3-3cb8-b5e9-980ad42edfb0 | -3.46706 | -45.91113 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9e5bce3-2ce1-3299-b4fe-0cf1ee916dbc | -3.09568 | -53.21544 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c575a866-bee3-361e-aeb5-c8cf8cbf89c3 | -2.72463 | -46.10181 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2008160b-85ca-3172-be3a-b3dd1f04f418 | -0.27215 | -51.55222 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb101825-4c5d-3aff-a6fe-7bfce7a59cd3 | -1.61286 | -52.58813 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ea1b0efd-2521-3dbd-aa93-0c4b1ef8cc85 | -3.46643 | -45.91513 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1135d3d6-25d1-3fac-ab1e-47095c075dea | -1.93696 | -49.52551 | 2024-11-22 04:36:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b486c613-d10a-3aa8-90a5-41d5d1a5b6fd | -2.57319 | -46.55976 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72d84362-c929-3ae6-810a-5abe8ced1eb9 | -2.22725 | -48.37709 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df307aa8-0a4f-3f69-87a2-8a5835bfae2e | -3.19823 | -54.25126 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61fa1126-42bd-3265-bd9b-127d978ad9fd | -3.58909 | -43.63537 | 2024-11-22 04:36:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 655bd2ce-a497-338f-8848-fce571f8dfed | -3.11192 | -53.75356 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf928b07-e1f3-3712-800a-449bc9344c90 | -4.96487 | -49.84618 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5431c042-38e1-3c9b-b4ca-fb6f9306af0c | -3.19063 | -54.32517 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 618aea97-060d-3beb-a5a0-493617da50be | -2.16663 | -50.13225 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c40424c-d35a-309a-bec9-faf723bee032 | -2.58237 | -46.54597 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 649dbae7-2c09-32b0-adc0-4b871d901682 | -2.86811 | -46.66782 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6da0004f-c1e6-3e40-b0de-62615f88c1dc | -6.10852 | -43.97283 | 2024-11-22 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 400e6d79-e82b-3aeb-aa3d-59e827d4b1db | -4.43975 | -45.8451 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b96ddd54-feab-374d-8dd9-a1456a31004e | -1.13788 | -53.6688 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7369df7-e2da-324d-add2-b42b6d625b44 | -1.60164 | -52.41298 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcd11f96-a591-3069-8185-713565bb4c35 | -3.893 | -50.07362 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39765fe4-8836-39a4-bfea-c8fb026fe095 | -3.24128 | -54.25814 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac9a3ee7-4675-32e8-a2c1-e2099a50be47 | -2.26396 | -50.80315 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52b80de1-f228-3c57-a4c5-6837929edcdd | -3.02265 | -45.14073 | 2024-11-22 04:36:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 93718f78-eb6e-3499-870e-32c7ceedb711 | -1.25722 | -53.36005 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d573209-3028-36cd-a884-fc16486b8494 | -1.5524 | -52.28419 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
