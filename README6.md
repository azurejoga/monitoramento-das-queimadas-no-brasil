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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 803ca0c0-e832-3c8d-aeb7-d2f8cbbb1dc0 | -12.591 | -48.199501 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6137ce-1f77-376c-9bea-c0e4e1a2b27d | -22.9251 | -47.076099 | 2025-09-06 00:15:00 | METOP-B | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8fe8842-c34f-326c-85b9-63785cf1481d | -12.5797 | -48.194698 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e160946e-ed58-3fd7-8fa4-d87b31c6e1dd | -8.7349 | -48.6875 | 2025-09-06 00:15:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 683821f8-5d33-3fa0-8289-321aef03ca6f | -9.4906 | -51.134499 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3736204c-b545-3411-8a89-d99169c2a214 | -9.7886 | -51.660301 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abcbb030-5c0c-3200-bc48-57efd46b6652 | -22.063299 | -48.793098 | 2025-09-06 00:15:00 | METOP-B | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82cc8656-2225-32b7-a6bf-1991c0e9a4f1 | -12.2941 | -53.872299 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43ce8c3c-f843-3722-9bc4-d6298c7dd7ae | -5.1193 | -44.968899 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32653318-d7cd-3283-a344-0dac0b2eec62 | -22.6383 | -49.229301 | 2025-09-06 00:15:00 | METOP-B | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a8b0bb1a-d5eb-3427-a90c-41eb00c91237 | -4.1792 | -48.091499 | 2025-09-06 00:15:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b860111-3bcf-366d-a7fa-9b44700409b8 | -10.934 | -46.385502 | 2025-09-06 00:15:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9deebf7-72c9-386f-a678-823a126eac65 | -7.1338 | -43.986801 | 2025-09-06 00:15:00 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 30633a48-4c6d-3673-9ca1-7b624294840e | -4.8817 | -45.142502 | 2025-09-06 00:15:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0c717f-4392-3ae0-b991-df2abbd9d963 | -15.2561 | -47.1693 | 2025-09-06 00:15:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 58e34368-8b50-3772-b394-3003b207fe41 | -12.7825 | -54.8438 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35a504f2-5210-395f-903e-07cfa529f380 | -10.0238 | -50.5625 | 2025-09-06 00:15:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97a712c3-2202-31b3-a7e1-e78acba81b3f | -5.764 | -44.7752 | 2025-09-06 00:15:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 881b3c28-d25d-3253-97a9-0bbf7b88b938 | -9.4861 | -49.331501 | 2025-09-06 00:15:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aae27694-6b83-35e6-8bc0-05a115b5a58d | -23.954201 | -49.563801 | 2025-09-06 00:15:00 | METOP-B | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 9a3c534e-8642-3d81-b5f0-4e7069fea51b | -18.235901 | -45.974201 | 2025-09-06 00:15:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17c5d7ce-5fbc-313d-bb14-35982fdde45d | -6.616 | -52.835602 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bcd6a53-a87a-36a1-969e-6d43f3983865 | -15.5292 | -53.627102 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6807bdde-5a14-3162-bc0f-13b9d2390fbf | -10.0107 | -49.750099 | 2025-09-06 00:15:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a5bfa49-f997-3436-9512-0d0c0fc35fcf | -6.0748 | -53.460499 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e938f57e-ede7-32d8-8c1b-ea9585fa82e4 | -4.2992 | -42.9207 | 2025-09-06 00:15:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9f10e07-9e7d-35f5-b9a0-5d64bedfe10b | -7.5979 | -52.159 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f6d0cf8-01f1-3d82-9061-8251fc7d2b92 | -3.5521 | -49.0984 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df7870f4-41bf-30a7-857f-99926558d274 | -7.2122 | -44.975399 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f84e0be6-3ab4-3f4d-a339-b9264d59f415 | -19.603399 | -45.264599 | 2025-09-06 00:15:00 | METOP-B | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a463db6b-c0e2-3199-bebb-668135c354f3 | -14.6445 | -48.225201 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be5b00c9-c52d-3a76-a711-356729149b97 | -5.9653 | -53.7118 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a344e61-dfe2-3c0d-9298-80aadeba2760 | -5.752 | -53.815601 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c608228-e150-3527-bc2c-87c65fbfa4c0 | -11.8146 | -47.811501 | 2025-09-06 00:15:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56dc69e2-b705-3a29-81c5-9dbd56ac1705 | -2.4508 | -48.830101 | 2025-09-06 00:15:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c2f025-802b-35d0-aed1-63274476fad0 | -11.285 | -55.583302 | 2025-09-06 00:15:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a95a957-7163-3512-b0b6-1fad828959ea | -16.132799 | -52.966599 | 2025-09-06 00:15:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3d9836-8f48-397e-a004-19dc35b5419b | -12.4824 | -45.006802 | 2025-09-06 00:15:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 817a2668-8c3a-3a98-8e73-60841d6bcd33 | -12.98 | -44.5317 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49f8bc04-f52e-3967-b448-c1dd3502ee89 | -23.944401 | -49.565899 | 2025-09-06 00:15:00 | METOP-B | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 12b1a46c-8c9f-3a58-b5d3-0755910e3bda | -5.7729 | -53.628899 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4542a1a3-c28d-31d0-889a-c23962259c4b | -15.5171 | -53.616501 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d93d9a42-14b5-338f-9ad5-38c746487cf7 | -8.8833 | -50.4697 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4877f6c-c029-3344-87e4-38e5f43b8249 | -10.9048 | -52.040401 | 2025-09-06 00:15:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2109c076-1d81-31f3-b92e-b48322259939 | -10.7464 | -44.868801 | 2025-09-06 00:15:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 69ec11f3-ef53-3606-a0f3-8d9a1297e70c | -15.5318 | -53.5877 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d72a0128-fdc7-39e5-8a70-5e519de65908 | -13.6921 | -48.057999 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5659fea1-78ba-33a9-a246-f203efa6358d | -15.4951 | -53.608101 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77489092-0e36-3d62-9c82-16dd72ad6d69 | -6.4635 | -48.438999 | 2025-09-06 00:15:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b2ee518d-38ac-3cb1-b5d0-20ffb2260f77 | -10.0385 | -50.5825 | 2025-09-06 00:15:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7ff4825-7994-3da7-b4d9-4e3671a1f283 | -5.2879 | -60.130402 | 2025-09-06 00:15:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e77852b-5b92-327f-b84f-57f8280d6d4b | -22.628401 | -45.7145 | 2025-09-06 00:15:00 | METOP-B | GONÇALVES | MINAS GERAIS | Brasil | 3127404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38c56f14-fa29-3c0b-9047-04eb4d6e6294 | -8.8555 | -50.483398 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce449f51-66fb-3c03-8bd6-05919cf2e9af | -14.059 | -52.214401 | 2025-09-06 00:15:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f2dea13-1d95-36f1-940b-5f09353a4dbe | -14.3712 | -48.057598 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 220d3035-3c5a-3e6d-ad10-880277d032c0 | -9.4791 | -51.129002 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f5e28f-559a-3fd7-b476-e0ec3d82b65b | -5.5305 | -45.408298 | 2025-09-06 00:15:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64bb75cc-51e5-3216-bdff-e4c2b9e84b5f | -4.5967 | -47.301498 | 2025-09-06 00:15:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4616875-8f62-3766-9bfc-0db23825c099 | -11.8162 | -47.818501 | 2025-09-06 00:15:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98d56db4-3581-3cb5-bd74-10a4b293514d | -6.1935 | -46.133801 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e824c71-013d-3ea1-aeaa-c1af899caf76 | -7.522 | -50.3601 | 2025-09-06 00:15:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e19681f-5058-3bdf-a01a-7503451aa095 | -17.952999 | -51.812 | 2025-09-06 00:15:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01a609b0-042c-33bd-b0a1-a5fe69ecd227 | -6.1244 | -58.1856 | 2025-09-06 00:15:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b55bd2a6-d723-3b42-a86b-8d339ff34a53 | -7.8799 | -45.360802 | 2025-09-06 00:15:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4e719d-7bfd-3a58-ac03-6e46c0a21892 | -6.4619 | -48.431999 | 2025-09-06 00:15:00 | METOP-B | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 095d4d68-31da-3282-bbef-20b6e46f123a | -6.6258 | -52.8335 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78830029-4d41-39cc-ae86-2f0333a57adc | -4.3026 | -42.935101 | 2025-09-06 00:15:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3df5438-b396-3110-8a16-5b5102228a58 | -13.3882 | -43.3825 | 2025-09-06 00:15:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aa45ed78-67a2-3595-a357-b2f61f64b4ce | -12.7576 | -54.8204 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b80d45fe-5f55-349a-9d12-8e9e2edb988f | -22.6457 | -47.564098 | 2025-09-06 00:15:00 | METOP-B | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d695fa3e-236c-369e-8c2b-6f1f515683cf | -15.5342 | -53.600201 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b139ff1b-1ae0-311e-9a2a-0c8d24681105 | -6.6711 | -52.806 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74fe4bf3-84ea-3826-a28f-f07373d30091 | -15.5073 | -53.6185 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 521239fa-d5fc-3742-a4a2-8372b442b5e8 | -4.2861 | -42.908501 | 2025-09-06 00:15:00 | METOP-B | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f040e11-11ad-388d-996a-2ca5bcdd2694 | -15.5196 | -53.577301 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fbd281d-4ef9-35bd-b7ba-7750352f5da2 | -6.1056 | -44.606998 | 2025-09-06 00:15:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b2c8a89-5d9e-3510-b3df-406e28beedae | -8.8817 | -50.462502 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2401061c-72f7-376c-aab6-7fdc838d3e0d | -11.0591 | -46.436001 | 2025-09-06 00:15:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0705160-997c-346e-a13d-14b71f43f089 | -13.6493 | -46.304401 | 2025-09-06 00:15:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 708773be-2e75-32f3-9cf0-b4333fbb03e2 | -10.1131 | -46.4491 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcfd4061-9993-331c-aac8-d16a51ca2f42 | -12.763 | -54.847698 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87f0571c-84f5-3f11-a03c-dd466c40ad2f | -8.8881 | -47.043701 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a229583-af5f-3c54-b419-c2b3276be3ce | -5.7566 | -44.787899 | 2025-09-06 00:15:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a12d882e-d022-311d-afd4-3908b46c5c54 | -10.403 | -44.376999 | 2025-09-06 00:15:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4ab4f85-2201-3682-b815-650872408c3c | -5.8139 | -46.722099 | 2025-09-06 00:15:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bedfa8f5-a8b0-33d6-9813-12b9650aa17a | -6.0787 | -53.478401 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f669d13f-1cfd-379f-83d5-e25873490db4 | -6.0031 | -53.272598 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff200e7a-8ce4-39b8-9c1b-9fa8b62fcb7f | -8.1428 | -46.986301 | 2025-09-06 00:15:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3447c50-ce0f-33b7-aeda-f185fe8f5507 | -11.1922 | -43.616798 | 2025-09-06 00:15:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f42832ee-3c67-31b7-99d0-375ef72e5f8d | -15.5049 | -53.606098 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cf015a1-279f-3f1c-b423-1c5506c7c58b | -19.901899 | -43.8577 | 2025-09-06 00:15:00 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49bcae86-1b9c-3d57-af0c-4e765ae6d908 | -11.3525 | -47.361198 | 2025-09-06 00:15:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d085d69-6375-35bc-8440-a72bb958b549 | -6.8032 | -44.9893 | 2025-09-06 00:15:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96bdcecf-4800-3957-b8d0-e0bf444e8cd9 | -12.8074 | -54.867199 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bdfd991-2057-3a53-8b6f-94d6daef56e1 | -14.6347 | -48.227501 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2dc8dcf7-bca9-396a-a370-1e6b0bc24456 | -20.326 | -46.156399 | 2025-09-06 00:15:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf99ccd-2456-3fe8-889b-19332a6bd980 | -9.776 | -51.696899 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0dbaf33-0717-3cf6-8151-a1b9b0edd1e1 | -3.1193 | -48.733898 | 2025-09-06 00:15:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c63e3c-4504-3559-b637-5f9ea621d320 | -11.4012 | -52.2108 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2557ad8-e5a3-365f-a64a-41caab99fa8c | -11.411 | -52.208698 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
