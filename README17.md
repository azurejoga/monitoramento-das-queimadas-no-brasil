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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf092440-d160-38e6-baa8-1e32e3a9509c | -7.74906 | -45.73004 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc4e6f02-ae9a-38ae-a1e6-63e25e2d98ff | -6.44821 | -41.8378 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f482fb6b-4956-386d-a9b3-b13c7de60b06 | -7.13602 | -42.49742 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 21ce704f-a110-352a-8d89-4cd37da30c3d | -7.75757 | -44.72184 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2611d92-bfd7-36e4-819e-ea30bf580e2e | -7.92296 | -44.13105 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad45bacd-5055-3c57-b23f-395f18ca00e0 | -7.62379 | -47.83619 | 2025-10-14 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0342fa63-722d-33fc-b483-c696963f5f39 | -7.8758 | -47.27106 | 2025-10-14 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e508ffb-6e3d-3d19-93e1-cb93aebe37ec | -5.87441 | -42.87863 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b50c7e6-6aff-396b-82ca-1ce2272981ac | -3.75351 | -41.67866 | 2025-10-14 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 62a5dd48-edb5-3129-9430-32c93601bd72 | -6.15126 | -41.77245 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 138dc60d-5374-36d6-b642-5b21c1919677 | -6.22354 | -47.03786 | 2025-10-14 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d56b783-de93-3ec3-81ed-6470e63a8e1c | -7.68298 | -42.37888 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4888d76d-b7ad-3689-be14-c8f6f4879c9a | -4.05707 | -47.25323 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f5a36a-ecfa-319a-b96e-37e497c4c2fd | -5.62035 | -42.71883 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 23376bba-8004-3722-9338-172cae5f4f73 | -5.87801 | -42.87922 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 6def35f9-17b8-3a49-a481-520ed451f5c9 | -5.8816 | -42.87986 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 8a7f2d32-05ba-3697-83d0-4d5bc491d4c2 | -7.32244 | -39.25986 | 2025-10-14 04:04:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b67531ec-ec04-328a-916c-b05425847423 | -6.29835 | -43.00146 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f58f321f-cd86-3f2a-b190-eb810de8a663 | -7.68768 | -42.37194 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5697edfd-73d8-3bc3-af49-fb31bc2f34e0 | -4.42775 | -47.59962 | 2025-10-14 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b891a7e0-c4b7-3d0f-95f0-0d8c6508fce1 | -8.25029 | -43.38626 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20c8d12e-083b-3819-8be5-e92dad47ccff | -3.15936 | -42.88784 | 2025-10-14 04:04:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf07cf7-2b22-3806-a3e0-7215a844c9f1 | -6.11188 | -46.34205 | 2025-10-14 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 639bcbb1-0d90-399a-88e7-68749848771e | -3.12025 | -49.10034 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c89a5a4-2a3b-3281-a198-be8585151b49 | -6.0476 | -43.38977 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8d0acf5-1401-3dcb-b8ed-0f9f16c8bf04 | -5.59221 | -42.57757 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74d5b535-774c-3b92-9f20-a2e872ac5bee | -3.93418 | -42.80428 | 2025-10-14 04:04:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e6dc003-02c8-3886-a225-1df7159e290e | -7.90096 | -44.99409 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b20d6205-2f7a-35e3-bc99-41d6410a42cf | -5.49558 | -43.07138 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 968871ef-99da-3869-a96c-3a7c084e0194 | -4.66737 | -43.13778 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efbea82f-4d63-3bad-8e5f-a647b0b20e9b | -5.85013 | -46.45088 | 2025-10-14 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e26b08f-b629-3174-98f3-0008ff81ec26 | -4.83315 | -43.20309 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b068470-bc71-3298-aad9-1b5dc6960877 | -5.98532 | -42.90839 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| feabf670-e6bd-3687-84de-be2f5b81fed7 | -5.48749 | -45.40615 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff4675c1-26ca-30dc-9f25-b2381182c3a9 | -5.60672 | -41.11376 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec40d0d4-8249-3ec4-abd9-dfe61e3f3303 | -5.20546 | -41.6545 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28058189-1b83-382d-b728-f335f16412b6 | -4.2324 | -43.01172 | 2025-10-14 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87513fda-7e08-355e-a769-2e974eb0d7b1 | -4.66367 | -43.13717 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| dde3981c-f0d4-32cc-9e43-48ff1c9306c1 | -3.44116 | -50.24987 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b0665bf-339c-34fd-9ea3-a68ad133e4f9 | -7.9179 | -45.0036 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55cd368a-ebe6-3746-914f-35bb57fc5de8 | -7.94039 | -44.12262 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f393eb1-4c87-362c-b88b-f5d4159ea64b | -6.15586 | -41.76569 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5173142-8b77-3421-a625-540eecdd6810 | -7.94191 | -44.11364 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f04ae817-a428-3dd8-a292-1b4f09cc2737 | -3.09756 | -50.38221 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1b86d0c-4a9b-3ce9-950f-ebebda095378 | -5.98783 | -42.87084 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 553427aa-5eb3-3828-87c6-e4b4b05c7e11 | -7.02938 | -46.98502 | 2025-10-14 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76ef51d4-b7a1-3d24-a385-b3c1e5a7d085 | -8.36857 | -36.45648 | 2025-10-14 04:04:00 | NPP-375D | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b175b18a-5fa5-30f2-a4c0-b6a60047635e | -4.74817 | -45.89667 | 2025-10-14 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22cb77a6-4214-31a6-bb21-3cb5d7f48c01 | -7.56333 | -42.68793 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08c89faf-05fa-3e67-9ba4-859c0bfcfbbe | -2.52803 | -47.80213 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 350b3117-e306-3e15-87c9-726fc377e8ac | -5.73552 | -40.76962 | 2025-10-14 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7c55eb59-7213-3afd-9bc6-a00dce0f4328 | -3.62865 | -41.62746 | 2025-10-14 04:04:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dec2b84-eec5-3bf5-8729-0d40502b878b | -5.73636 | -51.30425 | 2025-10-14 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98d698d1-e422-3d7c-9f2e-da6c8900e9e8 | -5.60449 | -41.10604 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af553916-541a-34c3-be3c-0b92cf0a49a3 | -7.68644 | -42.37944 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 951b214b-6c50-3b5f-a316-51cf0657156e | -5.9993 | -42.86847 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ffc5244e-5212-3e7e-9df7-8799aad8e359 | -7.55982 | -42.68736 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fd364035-df10-36fa-8e38-8e69ba6bda1f | -3.04233 | -40.11137 | 2025-10-14 04:04:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 33192978-cc46-3d39-989a-5f2355980acd | -6.15185 | -41.76879 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2e9dcb01-5a1d-3b2f-b2b9-420722688bbc | -3.9985 | -48.34028 | 2025-10-14 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 811459bf-8378-347f-b0fd-63a9581f1b26 | -7.08865 | -41.95873 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fd279a15-62f2-31c9-aaed-c75d02ecec1a | -7.90914 | -45.00726 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae597e52-82df-35ef-b49d-409a0e28c562 | -5.88295 | -42.87172 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fb486882-4eb7-3008-b55d-e26e2bf58e2c | -3.5046 | -49.71802 | 2025-10-14 04:04:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5f06818-efd0-39c6-a62e-ea92de90ea2a | -7.79517 | -42.44341 | 2025-10-14 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82c51dbc-f8a9-3e60-84b1-24b77b350515 | -7.53556 | -42.70341 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 0d449687-2d64-3ae7-8b00-553b19618e66 | -4.59336 | -46.3418 | 2025-10-14 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4dbd79d0-4484-3a48-b72c-72368fbff19d | -7.92839 | -44.12523 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd7ed56f-ba3d-3afd-9b62-a0707e70f07b | -7.68236 | -42.38266 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2c71bb0d-8fe5-379d-965a-fc9a11908a6a | -7.15906 | -46.53055 | 2025-10-14 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c4cc65d-1a30-3366-8d96-c507a171d14b | -6.33799 | -41.60831 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7051a785-7d7a-372f-87bf-26c140c46163 | -5.26039 | -43.21221 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea6721e-834d-3423-a281-f53e572309e2 | -3.06965 | -49.41146 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a65e34d9-ffae-3f6b-ba3c-04922a8766f0 | -5.11222 | -43.20335 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f30f913-776b-36fa-8556-51cce8c1ac87 | -5.79149 | -43.89144 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 44d16f72-1274-37e2-8e99-943c6efa86ac | -5.48683 | -45.41005 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e189261-7ba3-3d35-b0a3-4d430daa6ecf | -8.50312 | -37.94414 | 2025-10-14 04:04:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e8b94db-a4b6-3fc0-83c7-a1d6933ed982 | -4.05068 | -47.25124 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44b32d89-5df1-37df-a304-8e54d1fd4ddd | -5.63181 | -50.02899 | 2025-10-14 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc64efa2-5b23-30ec-b674-f6224e67d410 | -6.30968 | -46.94041 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d01d2a47-31ed-3a4c-827c-db4121175dca | -2.53892 | -47.80098 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36dada97-7cdb-3243-b1fa-9135825e192b | -5.64902 | -43.60659 | 2025-10-14 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a683e88a-5ed3-3c28-b98e-98574b1f2e7d | -3.07266 | -49.21323 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db2f0659-16f9-3e5f-a9c9-9a2e69f74b9e | -3.35132 | -43.51477 | 2025-10-14 04:04:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bf4a9df-f3bb-3e15-97a0-70db6f282099 | -7.68021 | -40.40876 | 2025-10-14 04:04:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0407576-cd5d-3956-b491-35ca83f696f6 | -3.43515 | -50.24879 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 729c6c34-508a-3247-b2af-3ae5e3aeb3cf | -4.66952 | -43.12467 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 057d85a4-a2f8-38e8-9049-ad772845c150 | -3.12601 | -50.21378 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a17290e-0c8a-33fc-8242-5f4dc7b60ce4 | -5.31951 | -43.42252 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4445ef7d-71cf-3970-a036-d44439328acb | -7.94337 | -44.12774 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8a4d0bba-cec6-3a4a-a8d7-c2448ee40f1a | -7.53621 | -42.6995 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 55f09da5-c62a-30aa-9920-de328fccbab1 | -6.76287 | -39.08263 | 2025-10-14 04:04:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78cf5b29-598b-356a-b578-a4ed4f4ae5c8 | -5.42367 | -41.34464 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d933e68c-8b4e-3aa8-a49c-f9c20ec8a402 | -2.53841 | -47.80405 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45eb817e-7090-329d-972a-fb0be7ddc9f7 | -4.23064 | -48.68725 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba5c97a5-c289-3ea0-a7d4-d26a6ca24560 | -4.82803 | -43.21129 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af4e2f99-77cb-3b12-aa0e-8d7d26ca09fd | -6.96876 | -41.68187 | 2025-10-14 04:04:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84bcaafe-5e85-3c60-ad05-b8d9f14c8c6b | -4.84211 | -45.21069 | 2025-10-14 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96df3345-3a28-37ea-a818-dc51f0220d57 | -5.94452 | -43.73515 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a2379b3-e1b8-378a-b165-b2a5cb612146 | -7.74763 | -42.44014 | 2025-10-14 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README18.md)
