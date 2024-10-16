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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50507b3c-0824-3586-9d41-ade0ddccaa80 | -17.2177 | -57.3102 | 2024-10-16 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| fdea55ad-5787-39da-b693-e07821113654 | -17.8675 | -57.252 | 2024-10-16 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| f54ddfe8-bdf2-3001-b07b-cdb0675d5f2e | -18.2544 | -56.5821 | 2024-10-16 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.3 |
| fb827742-1def-35e8-8545-8731aa8cb3c9 | -18.2742 | -56.5795 | 2024-10-16 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 227.7 |
| 2b2f4581-76f1-3041-b68d-f842253acb93 | -18.2746 | -56.5587 | 2024-10-16 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 03481325-baaa-3415-b81e-a98a75723ed6 | -19.5615 | -56.968 | 2024-10-16 00:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.2 |
| 42c90051-aa7f-3c01-98e6-219852f254a6 | -19.5619 | -56.9471 | 2024-10-16 00:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.9 |
| c2635812-1d57-3f74-a95c-28cf1ee0c3d6 | -19.5812 | -56.9862 | 2024-10-16 00:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 227.6 |
| bb4c704e-ff1c-3d2c-bd5b-730e66760b0a | -19.5816 | -56.9653 | 2024-10-16 00:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 201.5 |
| 26564492-8fd4-32e9-9760-cc5a1ac74984 | -19.6013 | -56.9834 | 2024-10-16 00:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.5 |
| 46195d72-5a70-3cee-b3f2-8312d0bd4148 | -19.6016 | -56.9625 | 2024-10-16 00:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 08f06bb8-4057-3450-b55d-93e4f68437ac | -20.8536 | -49.8742 | 2024-10-16 00:57:01 | GOES-16 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| 96f15242-5db3-3e3f-9585-ca9205d83583 | -9.64711 | -40.5898 | 2024-10-16 00:58:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 6f6012dc-fc82-347a-8b56-1d66bb88c248 | -9.64644 | -40.59647 | 2024-10-16 00:58:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 4ce339c3-5439-3cc7-ba1d-159132605b2b | -9.58588 | -43.5117 | 2024-10-16 00:58:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ddbba7f3-f801-3f98-9fd0-821819315d25 | -9.47317 | -40.3753 | 2024-10-16 00:58:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 4a152032-e65f-3604-9d11-71d1c0a474b4 | -9.45826 | -40.37789 | 2024-10-16 00:58:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 14fd024b-6acb-31f9-afff-a4d6ee62dc2d | -9.4535 | -40.34943 | 2024-10-16 00:58:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 56173b42-38cb-3854-a1b1-70332819f471 | -14.55097 | -43.13639 | 2024-10-16 00:58:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9ea8c8e2-e4f4-3c63-8d74-6ecf7a744820 | -13.90798 | -42.51797 | 2024-10-16 00:58:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c0598ece-7b65-3fcb-97d0-205d1957e050 | -13.82174 | -46.94094 | 2024-10-16 00:58:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5629c263-33c2-3c8b-804c-39c80707ee46 | -13.56822 | -42.75498 | 2024-10-16 00:58:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 4ef5ce49-11b9-3cad-80f2-7162700cca80 | -13.55676 | -42.75676 | 2024-10-16 00:58:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 7acd0e2c-4e69-3981-8e4b-501c5ee79080 | -13.38985 | -46.95237 | 2024-10-16 00:58:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 66cededb-3f9b-32ff-8dbf-a168144e2b02 | -13.38852 | -46.94299 | 2024-10-16 00:58:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| db08cee5-6037-3b5a-aa9a-6d3023355f9c | -13.3809 | -46.9537 | 2024-10-16 00:58:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8f59825e-a17a-326c-9763-ae39aff3bc96 | -13.37958 | -46.94443 | 2024-10-16 00:58:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 49a7a93c-dbef-3df6-9ee9-ab7f844b1bcb | -13.3614 | -46.62465 | 2024-10-16 00:58:00 | TERRA_M-M | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6c67cea-fd60-3a34-97ea-842094ed612d | -13.26122 | -41.96636 | 2024-10-16 00:58:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| fd280720-4c5b-3103-b070-530384c93df0 | -9.99841 | -48.64833 | 2024-10-16 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3dcd3266-ef10-3608-b23a-1569cb67f703 | -9.99716 | -48.63942 | 2024-10-16 00:58:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 7fec7023-ad01-3a61-8193-8ad4a74c94a3 | -9.96965 | -47.4014 | 2024-10-16 00:58:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 64a4c512-132f-31db-88c0-4d62d6d0c3c5 | -9.9683 | -47.39207 | 2024-10-16 00:58:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 17f4611d-6a08-3596-9d20-e57c6680a788 | -9.9656 | -47.37344 | 2024-10-16 00:58:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c2de78d-2060-367c-8ede-8fd502708b3e | -9.93325 | -48.11941 | 2024-10-16 00:58:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef2add42-e639-337c-afca-76a0efb61dc4 | -9.61375 | -47.55502 | 2024-10-16 00:58:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 694f3bf6-6297-3e01-8c22-43f4550a16ef | -10.24914 | -47.29375 | 2024-10-16 00:58:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1b4ceaad-fbd9-3cba-a7f6-ba8f7502d497 | -10.25049 | -47.30313 | 2024-10-16 00:58:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d66e584d-895e-3e5f-844c-88c65cad76f9 | -10.25952 | -47.30177 | 2024-10-16 00:58:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 17c032ff-2bc3-31fa-b49c-1adf5af4ed9a | -10.26087 | -47.31115 | 2024-10-16 00:58:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a212d6ba-747d-3b95-b4e8-dfdb63960c36 | -10.81857 | -49.24972 | 2024-10-16 00:58:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f5da7a39-22e7-380d-86f0-d96691d9dba3 | -17.22552 | -57.30913 | 2024-10-16 00:58:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 62b5c4ff-d979-3657-9a31-317d60766e7b | -17.02511 | -57.50559 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| e3fb101d-9665-3dad-9bc9-5518a427b97d | -17.02133 | -57.46597 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 373.4 |
| aab9e139-41ac-3608-8185-eb0f3887fde2 | -17.01153 | -57.50037 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 453.1 |
| 7c7d85aa-ff55-3e9e-b3ec-7a382558f607 | -17.00432 | -57.46761 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 398.6 |
| 5730bc58-f9ef-3697-b3ba-aa6c76cac795 | -16.991 | -57.50887 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.5 |
| 40494499-54b7-3af5-9eb8-334bdf8c16f0 | -16.98732 | -57.46925 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.6 |
| ba204118-cd87-33b2-a656-01298143195d | -16.96878 | -57.84127 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 31e9edd1-e5ae-3209-b3d3-533f9f4f6468 | -16.96755 | -57.8462 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 6aad1034-4393-335f-a9ce-5e5c6128e47f | -16.96749 | -56.82465 | 2024-10-16 00:58:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| dde0c0f4-f78c-3122-a576-ab1bc4f1fe3f | -16.93652 | -57.51914 | 2024-10-16 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| fcfca1f0-cea8-35cb-90b1-05a5d7eef1fd | -14.26392 | -51.12455 | 2024-10-16 00:58:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d5f97906-fd30-376f-b8e2-2d19564ce5ce | -12.5243 | -48.73042 | 2024-10-16 00:58:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2eb3eddc-7b18-385c-90f8-33de3c963526 | -12.51625 | -47.41872 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ec3fa7cc-339b-350b-bf8f-55aa37f38856 | -12.50865 | -47.42918 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 41580dcb-a8c9-3106-b94c-20e3dd2e54eb | -12.48913 | -47.29187 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ec809fb9-2254-3d8a-897b-a9d701c645e1 | -12.50736 | -47.42007 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f04872d5-7de2-3024-8e4a-4d7fd962fb32 | -12.48782 | -47.28268 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 929fdd73-7d43-366d-b62c-c0fb06734fac | -12.48021 | -47.29322 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7080c022-1dce-3c29-928f-7082c862a732 | -12.4789 | -47.28403 | 2024-10-16 00:58:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f630257f-53c4-3782-93a7-3aa1abb90441 | -12.37815 | -48.60045 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c6ea227-02e6-330f-9a85-3ddc97845ebc | -12.3769 | -48.59142 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3ba4ceb1-4576-3057-a58c-4e942b759c31 | -12.07233 | -48.38792 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 00b47845-800c-32fc-91b8-414d26e180f6 | -12.07109 | -48.37894 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb052085-611f-3e8c-9090-63991efed335 | -11.80467 | -47.40039 | 2024-10-16 00:58:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ac488bb8-2ee2-32e5-abd7-543495fd7ffa | -11.80336 | -47.39123 | 2024-10-16 00:58:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e671453-2fb3-32da-bee8-d1725dbfcafe | -11.79896 | -47.88073 | 2024-10-16 00:58:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97e15207-e9e9-364b-8b46-ed51c217021a | -11.79427 | -47.39887 | 2024-10-16 00:58:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 4de1817d-124d-3883-b275-2a5e0cdfd85f | -11.63615 | -47.58435 | 2024-10-16 00:58:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| eab99862-a388-334b-8454-3c2ea8679e04 | -11.62128 | -48.45683 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6e710c0d-94ea-3e4d-b878-cb4dc5011f1d | -11.60361 | -48.45942 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| feb78a7c-3881-3901-97c3-05f3d10cf544 | -11.59091 | -48.4979 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a6915fc-c616-3dcd-9b7e-ec972b02d06d | -11.58593 | -48.46201 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8a9f58c0-fc78-3cce-b32e-953712689ff4 | -11.58219 | -48.4351 | 2024-10-16 00:58:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5c86aad9-19e2-304c-8d21-87fbdb06ff46 | -11.31439 | -47.58574 | 2024-10-16 00:58:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0054fd8-7609-3e8f-9a6f-f46f425f61f6 | -11.20445 | -47.855 | 2024-10-16 00:58:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 335a0581-bcaa-3db8-9937-50ca50b18e4b | -11.20318 | -47.84597 | 2024-10-16 00:58:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6b7d77e7-3583-331d-9f8b-9728d31d8144 | -10.83637 | -49.24716 | 2024-10-16 00:58:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 34c0fc0a-ffde-3b4c-8aa2-91efa3a1940e | -10.82747 | -49.24842 | 2024-10-16 00:58:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 9d5c3e09-8f28-3798-bd35-e91d79b0e560 | -10.82622 | -49.23935 | 2024-10-16 00:58:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7493014c-73a9-33cd-a8fa-f5582786dba3 | -6.48732 | -43.87476 | 2024-10-16 01:00:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0ae657d2-ebc5-39bd-a58b-b20599262492 | -6.48175 | -43.88221 | 2024-10-16 01:00:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 581ada83-a479-390d-b984-5eec81661c85 | -5.51056 | -43.69935 | 2024-10-16 01:00:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 42a08c7c-ec98-3ef7-bc26-0f75f229fc14 | -6.72188 | -43.55854 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 58859d02-7b3f-35bb-bb6c-8ce48c8ee8f3 | -6.69766 | -43.96584 | 2024-10-16 01:00:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 155112f6-ed02-3c94-b13a-7b9cb1c52432 | -6.69511 | -43.94936 | 2024-10-16 01:00:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 731a5a1d-0405-3dfa-aa08-23289a85c840 | -6.61427 | -43.42894 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 45c09c60-51ae-38f1-aaf7-3c43e500d1fa | -6.60902 | -43.4175 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 45833182-512f-307c-bd64-7b44d1ae1e34 | -5.50785 | -43.68126 | 2024-10-16 01:00:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4c5e9baf-99ed-35f6-9a67-3a549da99902 | -5.26967 | -43.40379 | 2024-10-16 01:00:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| dd27830a-d649-3ce9-b07a-c841e2d56c1e | -5.0759 | -43.16142 | 2024-10-16 01:00:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 34c3121f-90e9-3b9c-b1c3-8ed0e5506c6a | -5.07393 | -43.15516 | 2024-10-16 01:00:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1d8b470d-a4d7-3474-8aae-0f9c25434c7f | -5.04688 | -43.66894 | 2024-10-16 01:00:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b8f7a28c-c037-3bf9-85bb-5dee9d01bd7e | -9.51902 | -47.79758 | 2024-10-16 01:00:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef7e65b4-83e8-3ec7-96d7-7b4106c030cd | -9.4961 | -47.82896 | 2024-10-16 01:00:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e212dd1-b12e-3742-a474-1dd882573d24 | -9.4948 | -47.81987 | 2024-10-16 01:00:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ddf6085c-f619-3df2-92b5-a826571d78e5 | -9.28946 | -47.60872 | 2024-10-16 01:00:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 99777464-fef4-38f6-b7cb-56d6f43c7fa8 | -9.28814 | -47.59947 | 2024-10-16 01:00:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cc3cae36-f149-3569-b5ff-d4293b7dcb5a | -9.21008 | -47.95482 | 2024-10-16 01:00:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README12.md)
