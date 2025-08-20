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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14f7b108-6706-3122-af3e-b3b494a6ef61 | -6.00953 | -42.83185 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4f702f4-2b57-3caf-af6d-ff14f2c8a1de | -5.6493 | -43.37231 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79d12735-5a62-39de-bb58-4b3cb850a77b | -4.87356 | -47.75502 | 2025-08-20 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f8da999-c20e-3379-8291-299a4167ff71 | -5.64697 | -37.25423 | 2025-08-20 04:08:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ad89f1d-ed81-3e0c-a204-9bf71cd29c83 | -6.57745 | -44.47371 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7ca9efb-d5be-32ac-856e-e525a329cbd5 | -2.7756 | -48.59505 | 2025-08-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 50fbaf67-ccfd-30bd-b21f-42f611cd7d78 | -6.46692 | -53.37172 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e449096d-2e68-3c2e-80bb-73774099b72f | -6.85331 | -43.61901 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0f0e22f-f1a8-3872-b1f5-dffb2635601a | -7.59632 | -44.39008 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b1ab5c-ca5f-3e9c-9aac-6b1c1797d7ab | -6.0039 | -42.84563 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6e8a242e-691a-34d0-b96c-0fd12db4146a | -5.46116 | -44.87006 | 2025-08-20 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fa7ab34-8772-3367-a46b-62bbf87be8bb | -5.99886 | -42.85577 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2d2b943c-87fb-30a1-9303-f74f6ed242e2 | -6.86191 | -43.609 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30394957-c936-3d2a-bbf3-d98d655bcd5b | -6.18474 | -44.52402 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15ebced5-2971-3437-af30-e7770ebe8097 | -5.64356 | -43.38654 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd725f72-53eb-3d45-93d0-80c34805fea2 | -6.39605 | -44.25102 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38390187-9736-314d-b471-753c050cb4d2 | -6.07131 | -44.12127 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b1ec745-829f-321b-9e1a-7baaeb0da68d | -7.02567 | -44.59604 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07e06e79-1514-3a58-9038-f8fc34dae61a | -7.03399 | -44.58946 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac2f6afa-e1c0-3cb2-9b9f-175c86db0501 | -8.29986 | -46.34741 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 20da169f-7093-3f81-a639-73e2b9ec0ff1 | -6.85828 | -44.41922 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 469631b1-1de6-3e99-ac65-7a1d4e761813 | -3.39968 | -46.90881 | 2025-08-20 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acc40594-93af-3551-aa6e-d5e179184124 | -6.62172 | -43.88062 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3b0f47e5-7ed1-341c-a92a-1babcc2554a0 | -8.80092 | -45.44205 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 528e6598-d4cd-367d-a37b-dffd55e003b3 | -7.26728 | -50.19635 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e939da0d-f440-3a61-b4b7-34bf3da2fac3 | -5.54245 | -45.37635 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0899873-dbc7-3e1e-ab0c-91e42bcef0dc | -6.62233 | -43.87684 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b60ca376-45d3-34cb-b688-134670038284 | -7.39359 | -44.27556 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 620bcff1-11d9-3f8b-9ed7-2649475a49d4 | -6.8539 | -43.61533 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ccb7d1-5c8b-38fe-971d-06130184296f | -7.57765 | -45.42068 | 2025-08-20 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c5559a0-cdff-3325-a936-7868ad385ce8 | -10.31691 | -46.6738 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24e0dd24-74bb-39fb-9de2-c269dc7c7c70 | -5.65331 | -43.37255 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0671f1a9-41d8-393a-8950-ceab6877c47f | -3.39541 | -46.90811 | 2025-08-20 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3ef0c06-d8ea-3d34-ac47-d60464aca541 | -7.02667 | -44.29369 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8cedb19-6cfb-3795-8356-a739f4c7bae4 | -4.42989 | -47.76027 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06955b08-33ea-3449-aeaf-ecc8376654e9 | -3.83857 | -47.73732 | 2025-08-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dcd62a9-0fff-3d96-b9e2-ee9317f3b1d2 | -5.69146 | -43.55009 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c61c6871-6201-3ce1-a847-d5de1aa5714a | -6.86991 | -43.60266 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f19aad66-141b-32d4-8739-6a23b14c726e | -8.79611 | -45.47941 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac2f011d-1527-3aa9-aeee-cada0c9e4e84 | -6.09873 | -44.35967 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c56e9607-30bb-374e-80bf-1b52ef1abf09 | -3.81899 | -41.55766 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d1f5be89-dddc-3913-b04b-de4d4040e72f | -8.80043 | -45.47582 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b17c9951-2602-312d-b92e-27c28323309b | -6.06083 | -44.11953 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 900b2ecd-3da1-3c84-9617-84e5bf4122fc | -5.40508 | -45.1917 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9482ab8e-10a4-3fc2-85f0-dc4df2ce5770 | -6.03279 | -44.38658 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66126099-57e6-34af-a563-8a7c512607bc | -6.19262 | -53.51803 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ac7c80b-b682-3c13-97e6-4c0eab728ea1 | -7.63856 | -45.2798 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4fe6dd0-019f-3c72-bb94-890ad6afa890 | -5.32631 | -43.92653 | 2025-08-20 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2efe098-d6da-312e-82f2-9b4c8150cfcd | -7.02882 | -44.29002 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 739edcc7-8602-32d9-b6d7-ed572aea1d8a | -5.78709 | -43.89078 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fc78719-55c5-3acc-876e-aba177513c88 | -5.64131 | -43.37864 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4d04ecd-7d37-3844-8844-c071f7fcd952 | -7.81501 | -46.88581 | 2025-08-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ef37658-2aa1-373b-87f3-7645f36a7299 | -5.6339 | -43.38128 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2619f49-62f5-3feb-907b-931354eba40c | -6.94862 | -42.87242 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 0c6de38a-c40a-3cba-925f-b242a60b8e9e | -5.68743 | -46.47057 | 2025-08-20 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4add87d-d346-3b31-8dd0-b1a7126b4822 | -6.7102 | -44.32762 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 867314f5-3503-3b5f-8979-c80318db88ce | -9.24831 | -44.49526 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fac240c-f970-3a5a-91b0-6833f21b8f34 | -7.22868 | -44.25746 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec3b1c62-7b53-358e-bd6e-01402265182b | -5.14164 | -42.90016 | 2025-08-20 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bfcd3e8-48d2-3a9c-b4f7-2b5d6f94089a | -6.05794 | -44.11521 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29f7fd13-4b8d-33a1-bc50-b41b5d66f244 | -6.13338 | -42.9539 | 2025-08-20 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ae7f4692-5e87-3c51-a092-21ed8fcc0dd1 | -4.43135 | -47.75151 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e76e18d7-ccef-388c-913d-9c1135901ff9 | -8.83459 | -52.04684 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61ac6a3e-e718-3bc9-905e-ec010465f211 | -6.5676 | -43.00478 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bbee216-a871-3c84-87be-828badf3586b | -6.85509 | -43.60795 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f6caf20-7f95-3535-a3b6-6b5b7231c1b2 | -5.32569 | -43.93041 | 2025-08-20 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f0baabc-b3b0-349a-9195-5298fabed3e6 | -9.91985 | -49.28541 | 2025-08-20 04:08:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84253da3-1848-360b-8933-438b13e8f4ef | -9.52784 | -42.93652 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b7187ca3-277e-323a-99f3-4c546974909f | -6.36874 | -43.26767 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24557a84-59bd-3c30-b53d-0e664925b36f | -6.71721 | -44.32874 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c360744-2104-3dd1-beb7-b0cce486dc2b | -8.2163 | -44.42053 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bfdfc8c-9e39-3bc5-9a55-86310b886cf2 | -5.78752 | -43.60775 | 2025-08-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d207e154-01ba-30eb-b425-bc57d2aec06e | -7.84583 | -45.11025 | 2025-08-20 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b7d1baf-cd0c-3993-bbfa-981f8bcc673b | -9.87426 | -45.97145 | 2025-08-20 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aad79362-ae4b-3aa8-8ad9-545c4dcf294e | -4.91008 | -43.23046 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 788e99fb-e19f-38e6-bc59-dfb88bc28612 | -8.07433 | -43.66966 | 2025-08-20 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a9d7048-dccb-324e-b8d9-e0566debb2e6 | -9.50487 | -43.16735 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc9b3cf4-04d4-39d5-9a2f-27a71942c388 | -6.19891 | -43.56076 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05df8bfa-e934-309c-a7a8-91edfd42007b | -7.66021 | -45.26156 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b249ead-474c-3e23-a88a-65791cfd484b | -7.22569 | -44.70488 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cdffe4e-4f39-3618-8aca-d0dad2fadfce | -2.90257 | -48.29617 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de9a2137-5bba-3a21-8b75-9e3e61d96c0b | -7.44978 | -50.27173 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 782955da-d25f-304d-9c34-4bba4d61a39f | -6.3607 | -43.64677 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 004de0f1-9e97-3093-889d-aaafdaedd866 | -7.59284 | -44.3895 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 23614162-546f-3b34-90f5-6680e4855c80 | -6.0387 | -44.34998 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e87f47f-8aaf-38e1-ae7f-adb05ad98c98 | -6.1643 | -42.71466 | 2025-08-20 04:08:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce0b71ad-b39e-3836-8d91-905f289f9ec6 | -6.23541 | -46.24125 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 942695cf-de7f-343e-bb93-d1cf83dfae3a | -7.2963 | -43.68142 | 2025-08-20 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 57dad338-776c-367c-aed7-2c0a6742e81d | -5.99162 | -44.28183 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b407c0b5-d967-33b5-aa77-dee0d3434254 | -6.46193 | -53.37581 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30297bf6-e8c2-3c91-b909-8cfa88c8ce9c | -5.98665 | -42.82456 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e23a50aa-90b8-3a40-bb73-9e3d400e2b61 | -5.28378 | -44.19412 | 2025-08-20 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd512671-b477-36f6-b53f-05f6057320ec | -5.99 | -42.82506 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65691c8e-924b-33c2-bef3-b4b24d2997f7 | -5.61288 | -45.18143 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aa2ef2d-e9fb-39ce-a46d-fb58320b9add | -9.33137 | -37.98182 | 2025-08-20 04:08:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb983774-ee7c-3fd8-8543-a5365c341677 | -6.48223 | -43.74257 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27dfc2cb-a8ab-36f5-9c70-514f5999a599 | -13.1364 | -54.9376 | 2025-08-20 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 43a20bf8-6058-3aff-9528-f09294d29373 | -13.1555 | -54.9357 | 2025-08-20 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fe91ced1-db3b-3f3e-9bdb-6ae0317a599d | -13.1558 | -54.9151 | 2025-08-20 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e8c65cd8-845b-32f3-9260-432d05dc2db0 | -14.16042 | -45.29034 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
