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
| a984f7e4-66b4-3c16-b8d3-a527b94a6fcc | -4.48738 | -44.75879 | 2024-10-20 04:32:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f226311c-557c-36f8-8c62-5e7af11df0bb | -4.46445 | -45.89553 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04013641-5187-31a5-bc34-80fdb370f161 | -4.46389 | -45.89912 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a877265c-1251-3c57-9cbc-e9c2bca9f218 | -4.44186 | -45.7036 | 2024-10-20 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64c5a0e0-f8c7-3a8f-b38e-bb9baee432fd | -4.44128 | -45.70729 | 2024-10-20 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e8bc3ee-cea2-3dbe-a5cb-4993e5c0b417 | -4.42444 | -45.97044 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc98b7b-0e46-3edf-b257-da15673f7234 | -4.42106 | -45.96994 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c43080d-a6e8-3bc2-8808-4de4c85edfb2 | -4.4205 | -45.97353 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c97eb3b3-5bea-3f6d-a95e-71e636cf230b | -4.41712 | -45.97302 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da686128-86e4-385f-b9e9-a07eccd84ca7 | -4.41656 | -45.9766 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 449c085e-ad84-30fa-bac9-a720878473e6 | -4.39371 | -46.1664 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97a43181-ecee-3a4b-801f-23ff6e982fb0 | -4.3916 | -45.80331 | 2024-10-20 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 26032130-f45d-3962-9982-876a42f3f5cf | -4.39036 | -46.16584 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4ea19be-85c8-34f8-b603-3deb87bbbfd8 | -4.38821 | -45.80283 | 2024-10-20 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 71a9f7e1-b225-3615-b60f-6b1b744f93ce | -4.38656 | -45.83588 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10c996b1-f3b3-37f0-99f8-f8c9fc43d642 | -4.38599 | -45.83951 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 343f2000-a337-3248-9ce3-d1078c817112 | -4.38482 | -45.80228 | 2024-10-20 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39b605f8-b0bf-395c-88e4-cd7b0aa0fef2 | -4.38374 | -45.83171 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b50252af-e078-3973-b130-e922f0e37e6a | -4.38317 | -45.83534 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b06d2031-57df-3bfd-987f-24ddbbb4df1b | -4.38261 | -45.83897 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02f3fbfd-42e8-3773-b0e6-c4fc0cf49915 | -4.38205 | -45.84261 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02f3e560-836a-3b6c-9495-a9ddcc24c9c9 | -4.37923 | -45.83842 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30a0a033-37a6-3b1e-976f-7d221cc00737 | -4.37867 | -45.84206 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc7ab2bd-1d1f-3067-8aa9-77b314b4c6e5 | -4.37585 | -45.83786 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9741578d-d2be-3ef3-b911-5bd77e38bdb4 | -4.37529 | -45.8415 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20762b2e-bb1a-3cff-b815-681a0c95ae67 | -4.3719 | -45.84094 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7384d1d7-b75f-3497-98bc-454f5f071b52 | -4.30278 | -45.96651 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 577ea7e4-89f6-3820-a02c-75becdf3dd62 | -4.2994 | -45.96599 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce2cb556-118b-36c5-99a3-2ff24ed2d94c | -4.19438 | -45.74708 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5928b38f-3f2e-313b-aeb5-3167a04690c8 | -4.19323 | -45.7321 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2635fdd-82c3-30c3-8c3c-cb16b0eabe3e | -4.19043 | -45.75017 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dbce1f2-f789-3e91-ab3c-e03608788e66 | -4.18477 | -45.7419 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47878d82-193d-39ca-b6c8-cdf91e63edc0 | -4.01586 | -46.0207 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a71f9e-2755-3f92-b867-a7f77762ef50 | -4.0153 | -46.02429 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed3cee5b-051b-3b63-b8cb-62df33d54d0a | -4.01249 | -46.0202 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a343c3d-713e-33a9-b115-b3ab683bdbf9 | -4.19267 | -45.73571 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 319f73fe-40be-38e2-a14d-14306d45ef9d | -4.19211 | -45.73933 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d86f9104-d75f-36d6-8faf-2c912f754f35 | -4.19155 | -45.74294 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 902813d2-c45c-3229-9c68-ad015f01617c | -4.19099 | -45.74656 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1a0f8b4-52f0-3971-9bcd-64acd6969344 | -4.18984 | -45.73158 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d4ed4b8-2b84-3c80-97a6-fc6c95eda50a | -4.18928 | -45.73519 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf0602e1-3408-3045-9d42-359c655e6753 | -4.18872 | -45.7388 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e9e1327-ffd3-36c5-b055-668e8f7b0d6f | -4.18816 | -45.74242 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f91a36b-2099-30cb-9c1c-9ba9160f2cd5 | -4.1876 | -45.74604 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 153d6ad7-49e0-33d9-b541-9f0bb881ba0d | -4.04559 | -46.02891 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11f965b8-31a6-365e-ae1c-46a7d2d92834 | -4.01194 | -46.0238 | 2024-10-20 04:32:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e8e8cf-06cc-3fb3-a971-2f1713e97014 | -6.3522 | -46.34473 | 2024-10-20 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a309f026-7c71-350b-9d7d-26ea0aedd300 | -6.28506 | -45.9885 | 2024-10-20 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d162dab0-c60e-3a04-a226-fe4342322dc6 | -6.17744 | -45.43933 | 2024-10-20 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d726ae3-80c4-343c-b61a-6e651650ce2d | -5.98292 | -45.36829 | 2024-10-20 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 162114a6-6037-3944-96d8-c42f92df3fd4 | -5.97943 | -45.36776 | 2024-10-20 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 110c4799-a400-36ab-96dd-a690fce880e3 | -5.97885 | -45.37159 | 2024-10-20 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b733da1-3c60-3fd2-bd0f-5c70317e8a15 | -5.37976 | -45.11881 | 2024-10-20 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67fcf2b9-03be-3bd4-8b25-7be14863e633 | -5.32283 | -46.36351 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 32842123-5512-302a-a7cc-b2668b727a68 | -5.32087 | -45.05434 | 2024-10-20 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3b7e5d8-b939-37c0-b72e-e854aee3b3fd | -5.24318 | -45.86914 | 2024-10-20 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09d6db4b-4a3d-3d42-b18f-0987160594e0 | -5.23425 | -45.97208 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4040fe26-baad-33f3-9fa3-8fa4faec932c | -5.21862 | -46.09542 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4dec4c6-3240-319f-80a7-227d9a69f60d | -5.21806 | -46.09902 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b8eca9ae-3a3e-3a49-922d-60b053433f80 | -5.21524 | -46.09494 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a0dabae-55d0-3c85-8f95-752e20d11205 | -5.21468 | -46.09855 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| faba9f6e-75f5-3450-81cd-1f32c9bc3f8c | -5.21412 | -46.10217 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d5675c69-7735-38c8-946c-31fcb7843b3b | -5.21356 | -46.10575 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fe9b4a7-e63c-3396-ac4f-c69db1fc5967 | -5.21073 | -46.10167 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79ef03f7-2443-3a3e-9ccc-393b4a0e28e2 | -5.21018 | -46.10527 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13ad81e6-3cee-3001-9ec8-18d65a7db25d | -5.19073 | -45.73354 | 2024-10-20 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92e53fa2-e872-37f9-b638-a4cd7fdccfe7 | -5.19016 | -45.73719 | 2024-10-20 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3fabf01-cadf-399b-b298-8ea5d4e5de56 | -5.17383 | -46.18386 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f32762eb-8b9c-3553-9173-4f6d59f9357a | -5.17354 | -45.57235 | 2024-10-20 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93e8e6e8-8c39-3292-a06f-f4e9ba59e055 | -5.17118 | -45.4727 | 2024-10-20 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49373e14-93ec-30d7-bb7e-45312005756c | -5.1701 | -45.57184 | 2024-10-20 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2350ed4-5b72-3c87-805f-655b22b19a7b | -5.16774 | -45.47215 | 2024-10-20 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ea685a7-f357-3d88-a385-3000d23884c8 | -5.13826 | -46.11563 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4e3c49c-cda4-3b9b-b32e-7d39b2b9480c | -5.13488 | -46.1151 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27b4fff1-5c9a-3ab7-b8c2-7a48a5b21045 | -5.13211 | -46.15506 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10035b7d-639f-3665-9556-adb1770fbcc9 | -5.13156 | -46.1586 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b82585-24c5-37d1-8722-3f9cc2c44ed9 | -5.12874 | -46.15455 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ead26d3-9182-3fd2-9180-0c6341954a4f | -5.12818 | -46.15809 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b79a815-afd1-3348-9b78-7f3514b297c5 | -5.12426 | -46.16114 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e92c4364-fef9-3cb5-977d-f4616d535e2d | -5.1237 | -46.1647 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61f547f8-d91a-3347-995f-9427f8b3bee4 | -5.12088 | -46.16064 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65b85b36-9c98-35db-bc82-fb55c0972f65 | -5.12033 | -46.1642 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53fffa95-c0d3-3c44-bbf6-6e71bc38f218 | -5.11751 | -46.16012 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b8120b8-aedd-369f-9f2f-8308ff3659e8 | -5.0985 | -45.94726 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c7184a-cd36-312c-95e4-fff4431b629f | -5.09779 | -46.13133 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6674ece0-1897-3d16-b1c0-2dda9e505d2a | -5.09511 | -45.94677 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebb1d7f9-f1b2-3f1e-abb1-4941c2393bde | -5.09442 | -46.13079 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae546d37-3d4a-3ebb-8d06-59e26e4847ae | -5.09386 | -46.13439 | 2024-10-20 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6acab9c9-70b1-39b5-b99c-dedb748fb870 | -7.58917 | -46.85326 | 2024-10-20 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f09cbb5-ee92-30b5-bc0a-d911c31c6b3b | -7.56452 | -46.85677 | 2024-10-20 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a3edcd7-c867-3e52-97b8-ce5aec5a3c47 | -7.17884 | -46.79775 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b22c0185-e72f-3273-9827-6ebe639068f4 | -7.17829 | -46.80132 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20cd1acc-1dd3-3c7d-8eca-11e9f3d69685 | -7.17493 | -46.80079 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70f79476-8a50-3b78-977e-601d43759b97 | -7.17158 | -46.80025 | 2024-10-20 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa0322c1-794a-356c-b2c7-768bf1cd10c4 | -6.7829 | -46.42532 | 2024-10-20 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad6a5993-0870-3c67-9090-532e9d415e64 | -6.77952 | -46.42479 | 2024-10-20 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62629409-8d76-30d5-b08a-4ab80db31500 | -5.05025 | -46.85316 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a90f384d-9fcd-37f7-8375-57c748c39709 | -4.99293 | -46.48629 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 587c35c3-e04a-3a9b-a011-d98bd4a8d9e5 | -4.99013 | -46.48228 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58a4c2a9-3894-36e7-9f8d-efa1dcd50145 | -4.98958 | -46.48578 | 2024-10-20 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
