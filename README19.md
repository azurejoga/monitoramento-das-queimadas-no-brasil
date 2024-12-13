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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90f79659-130b-311b-8223-e3088ebd48ef | -7.80504 | -46.22147 | 2024-12-13 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6042d2d9-1146-3d49-a034-40d401d826ae | -5.97544 | -45.36466 | 2024-12-13 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd65939-d7f0-32bb-a7ac-3df983ac8c64 | -9.16059 | -49.47567 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e17338e9-0b28-3ffe-b615-d7cfd7572a3c | -6.32179 | -44.76001 | 2024-12-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4d2a813-ce2a-3a94-9ddd-87d349cc2144 | -9.16819 | -49.47707 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9dbd46d4-416b-3069-b01f-94b54d74d876 | -2.50435 | -51.80137 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d4c6288-189a-3597-a0fc-705d45e348b0 | -8.26955 | -48.03024 | 2024-12-13 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e9f8ece-029c-37b9-9567-01c694802338 | -6.13325 | -43.95703 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aaeed79-d088-34fc-9f9c-e026d708c8a0 | -10.32362 | -42.39307 | 2024-12-13 04:21:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2fa5b83-a849-3524-87e6-9a273f801b43 | -2.51199 | -51.7925 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4ebf0eea-4e40-321d-af7b-72a635d648eb | -2.80788 | -53.07247 | 2024-12-13 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b23d3f9c-97df-391c-b948-b34d43798d45 | -7.57766 | -47.11291 | 2024-12-13 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57b95956-b868-3fa6-a361-23d338c35002 | -9.9633 | -49.82466 | 2024-12-13 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54e5a642-ba73-3a77-b4d1-b9a01192daac | -9.46879 | -37.06882 | 2024-12-13 04:21:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 802489f6-b0b2-3652-8da8-0d29472fa19d | -9.72781 | -48.02918 | 2024-12-13 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f1fd1d-8e8e-3428-aa92-099dc1e25a6f | -5.64938 | -44.96988 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d028a444-04c7-3b73-9a77-8dfcbc860076 | -9.47386 | -37.0695 | 2024-12-13 04:21:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f117b49a-877a-33df-b596-c66048626871 | -4.16302 | -42.44706 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4053698e-b0c6-31fc-b96a-f4ad25297705 | -9.16608 | -49.47438 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6e38daaf-1a93-3883-95d4-80accfc818d8 | -6.08325 | -43.97073 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb696ed5-1d63-314e-a5c8-9d1f4653da0a | -10.86985 | -44.93885 | 2024-12-13 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12307cb4-cb09-3d02-99b2-762278fd7afb | -6.97781 | -42.81336 | 2024-12-13 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db3f6ea9-55f4-389a-86df-d36a6987fa44 | -10.07801 | -50.81092 | 2024-12-13 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 278715e3-a509-3dc8-8bb9-885ad650febe | -5.20473 | -43.29336 | 2024-12-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bbd60de-7dfb-33d2-a226-fe463bf54f0e | -10.07393 | -50.81023 | 2024-12-13 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ddc0797-4bf1-31a2-a1c1-b676831927f2 | -1.99366 | -54.51379 | 2024-12-13 04:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7eccd95-16b2-366b-a6fa-e60f0ebd0ed8 | -7.80332 | -46.23223 | 2024-12-13 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 459148dd-80c1-3c93-be69-07d85f43bdbf | -4.16359 | -42.44338 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cbf88357-e11a-340c-8079-4dc2db1b5dcd | -1.99437 | -54.50949 | 2024-12-13 04:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e46c0caa-63ca-3af4-a1e1-5e93adbdc2f1 | -2.91275 | -48.00734 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6dc6707-31ba-3caf-a2a7-8d6d83d7326a | -2.4993 | -51.80753 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a153ac81-14d4-3b38-856c-f3054a5d84a5 | -2.51693 | -51.7933 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2fce256c-03f6-3b18-95a1-556fa23c1eb8 | -9.14085 | -49.48454 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1be3da75-e8f5-3624-ae3b-4ddc9c9bf459 | -5.73282 | -39.53492 | 2024-12-13 04:21:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e05642b3-48c9-3de3-b281-571e75b629c6 | -5.45787 | -44.81178 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5893b8f8-d2d9-3f21-9e20-645c3702fbd9 | -6.09059 | -43.53901 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 628108c4-2808-360d-9042-20bb4baa9dc7 | -6.11601 | -43.95794 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19007c54-2ba5-3d62-92ab-4cd00b1a3170 | -10.83301 | -44.43312 | 2024-12-13 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ae7c49-f700-304e-aa3f-ce19e25785de | -9.15977 | -49.48039 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1aee196f-6ab4-3617-8198-e04fd5f9a2c1 | -2.91285 | -48.01451 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 448b6d72-7a8a-3bff-96fd-325ba0f23781 | -4.77796 | -48.50474 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf57b599-74aa-3b0c-9668-c02abea5bed5 | -9.13704 | -49.48387 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fbe7164-62fa-3f4e-b54a-7744f6ebfadd | -3.01606 | -48.03562 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 986befb5-5ddc-3e09-bc22-d1c1ea9f7134 | -2.91432 | -48.00521 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f1e50d7-3c2c-3fee-bf3f-ce4caf6c49ed | -3.15125 | -49.90398 | 2024-12-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa38b335-8940-3a1d-a63f-425e42999a93 | -3.18277 | -45.61626 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce78d18e-e0ab-35d0-86a6-f50708a0fcbe | -4.67354 | -42.7342 | 2024-12-13 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22f3045a-4a96-3a63-8126-222bf176d0b8 | -4.17043 | -42.44445 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ea47a09-34bc-3484-b3dd-a1b77f1215a1 | -6.00075 | -44.6274 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 413d8d62-f06f-35e2-8126-c1ca6f4bee2c | -7.83295 | -35.18473 | 2024-12-13 04:21:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| af3a2a3f-bc5e-3f0f-a7a2-47c9be379475 | -5.96766 | -43.36627 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1fea8f84-9501-3bca-90f4-c4c56f8a1087 | -3.18617 | -45.6168 | 2024-12-13 04:21:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cd27123-af93-3795-a72d-91f1c537f68a | -5.4225 | -44.8631 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82bb8f94-705a-34ee-ab37-bbd2b858061d | -6.05729 | -44.0277 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9c6a98e-23a2-3f5d-870b-de9842c7773b | -3.71364 | -50.493 | 2024-12-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a0c9556-35d8-3273-98f6-3abbd998331e | -8.26597 | -48.02967 | 2024-12-13 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 604591d5-dc5d-3561-b84e-57efeceb7e63 | -10.2094 | -47.57991 | 2024-12-13 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b59798d-ec25-3bfe-9731-f6c29b65ccab | -2.4483 | -53.71195 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6015649c-f7bb-3036-a77b-12f92869bf01 | -2.2374 | -53.72838 | 2024-12-13 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b0e901b-5690-393e-8f25-cc82e57531f5 | -6.86514 | -51.98353 | 2024-12-13 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c6b4fb3-14cd-318d-8af0-aebb21e7b251 | -9.70981 | -37.35785 | 2024-12-13 04:21:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1cb3f97-cad8-324a-94d5-ecb987d75cc3 | -4.88311 | -44.4015 | 2024-12-13 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef8b50d5-b091-3c0c-86ce-707fd425e2ce | -10.03073 | -36.2844 | 2024-12-13 04:21:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5bce0e5e-c334-3b26-8920-e3564a72c250 | -2.65057 | -51.87906 | 2024-12-13 04:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7e27ac6-3221-35e9-ba8c-5b1af34b5496 | -5.00952 | -43.44432 | 2024-12-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e653af14-a2ac-32d3-97d8-5b25ba9dd6be | -5.93946 | -43.76844 | 2024-12-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02252d09-c85f-3da1-892c-ad2b04aabf41 | -7.42919 | -44.7318 | 2024-12-13 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 589872d8-7dd7-357d-a370-f3bdef821b8e | -2.91733 | -48.0033 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e91233de-801a-3ceb-be33-898a415d1824 | -4.64085 | -42.8776 | 2024-12-13 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6f6d169-137b-3496-8079-092052bd80dc | -6.21509 | -43.95174 | 2024-12-13 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bf223c7-ce6b-3fcc-88b4-813cc84c38a8 | -2.79347 | -48.56624 | 2024-12-13 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eff97a70-1574-34e6-87b8-9f7940e0081b | -5.28118 | -44.85502 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b566f60-2e35-3133-a3ca-478d38c71467 | -4.16701 | -42.44392 | 2024-12-13 04:21:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7bed4d85-6513-366e-9ef1-fde9eb9a90fb | -2.51602 | -51.79186 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d0af5920-8b94-3f39-9d8a-fe3b294a325a | -4.78304 | -48.50792 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffa2af32-9b5a-37af-932b-4271727d3b04 | -3.10795 | -48.28026 | 2024-12-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7bac34d-523e-370c-a784-e7354544f527 | -9.1615 | -49.4784 | 2024-12-13 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b4f76b22-64fa-3ce4-82fe-724e770c7cdd | -4.43058 | -44.1362 | 2024-12-13 04:21:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f278c3c-00f2-38ac-a60e-d1d8cacf6c78 | -5.24287 | -37.69204 | 2024-12-13 04:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b32c3ad8-a4d1-3d5b-a455-88b0e0afdde3 | -7.43197 | -44.73581 | 2024-12-13 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68ec6e0f-66bb-38a8-ba3a-97af0ee674be | -3.47477 | -45.80009 | 2024-12-13 04:21:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afd636c8-8af4-36fe-ab24-b16ec877e748 | -6.05511 | -44.04166 | 2024-12-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 206c1cbf-bd50-36d0-849d-f32bc8e6ee16 | -2.51786 | -51.78777 | 2024-12-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa918f6a-f580-3a5e-b5f8-4551069d3cdb | -4.06681 | -50.37212 | 2024-12-13 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5293308-9e04-37ad-bdc9-15d36fe75c7a | -4.11603 | -50.21031 | 2024-12-13 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9380084-641b-39fd-8b31-be2b74dc8910 | -4.57901 | -42.73432 | 2024-12-13 04:21:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86729746-8ac1-33ee-8217-87556a95cb7b | -6.08442 | -43.5344 | 2024-12-13 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d093427-86a3-33d7-ac6b-005e07679142 | -4.65036 | -43.81533 | 2024-12-13 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fac693db-8b42-342c-8934-75c2bfff4504 | -6.99986 | -45.62421 | 2024-12-13 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8bf7ab86-73e5-3f1f-b595-67d973a359c4 | -4.82668 | -45.09715 | 2024-12-13 04:21:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bff3e812-ff05-3866-9b57-743f42e510ab | -4.26555 | -43.82997 | 2024-12-13 04:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1ab6be5-466a-3169-a852-8a4f4f3557cf | -5.62258 | -44.83757 | 2024-12-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2ca3804-0045-3532-9007-584278e651c5 | -3.39681 | -47.56651 | 2024-12-13 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f26422-9ad3-3929-86aa-eb23a0178886 | -5.27781 | -48.79284 | 2024-12-13 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 302d2217-5d47-3c86-9ec1-b02a6f9b4bd3 | -4.64981 | -43.81881 | 2024-12-13 04:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb3d4713-d840-38c2-9305-8c7a53429f13 | -5.23979 | -45.13742 | 2024-12-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a74f808c-b214-3f68-bdeb-41ac40d14d35 | -4.51547 | -47.93841 | 2024-12-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2f69879-2d7a-37d4-9e43-1bca7da00919 | -3.49987 | -43.96553 | 2024-12-13 04:21:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eac1f1f-be67-3dfb-8026-7f9b77ff078e | -4.51138 | -42.06232 | 2024-12-13 04:21:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 63ead800-c441-3419-ba4d-c0fabb46a422 | -9.96225 | -49.82224 | 2024-12-13 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
