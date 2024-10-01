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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d409f88-236f-35c1-a7d2-a9ca3e87f9b3 | -13.00382 | -51.22527 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c8069b34-4151-3af2-9d64-bc79265fd59c | -13.00379 | -51.28692 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b899f696-78cc-3dab-875b-398a715c2d43 | -13.00377 | -51.34795 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 974c3a16-d3d0-32bf-be8c-6b75449b1579 | -13.00367 | -51.28905 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2e5c4f94-7c2f-3ff4-81d3-b27425a96819 | -13.00346 | -51.23314 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b268fba3-1709-3792-b974-8fbd8fb8f5c3 | -13.00324 | -51.34995 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0342c84-eaa3-3a92-90c9-e18b6e9daba2 | -13.00323 | -51.23081 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f756c3fa-55f3-3f9e-917f-72f35b0dd939 | -13.0032 | -51.29242 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b25221f5-6371-3c37-aec9-92170947d351 | -13.00304 | -51.29453 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e1ee00cd-453f-36d4-806e-11fbfa7bd49a | -13.00283 | -51.23869 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ffdcf88-d544-3062-8b76-c87c9863e543 | -13.00263 | -51.23635 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 99ac38d9-6c72-35b3-bf46-cdd15830ec32 | -13.00261 | -51.29791 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| db7f431a-6e1a-32d8-8fad-555a09ddcd92 | -13.00241 | -51.30001 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| fd9df919-9809-3b54-a6f7-e16e7c36059b | -13.0022 | -51.24425 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b3d993e-952c-31ec-8f85-c7a7c9871324 | -13.00203 | -51.24193 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50d9b957-92f1-3ded-a021-70b3c9006da5 | -13.00201 | -51.30342 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 3333c9bd-5537-3d9f-a996-0aff5796ed1f | -13.002 | -62.71233 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89ca0e03-b188-3a00-9b8a-4d7e400feb46 | -13.00178 | -51.3055 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| e1c69d3a-ef90-3483-b532-a75e0cd7b79d | -13.00157 | -51.24976 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a287461b-cb3b-37f8-91c1-9a887be88fd6 | -13.00145 | -62.71592 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d39b2f52-1ae3-3bbe-a6c6-f3935df11280 | -13.00144 | -51.24747 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4e8bb7d-ec1f-35ca-84a5-36032fba1902 | -13.00142 | -51.3089 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 27366318-cdb5-3848-8847-1597f76e35e7 | -13.00115 | -51.31098 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 74b8d8c6-49bf-3502-a7aa-d3ad11945359 | -13.00094 | -51.25527 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1f5506d3-0902-30ee-985f-591b41b58104 | -13.00085 | -51.25298 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 47da7faf-3ef1-3ff1-b6f9-5b6fee057e36 | -13.00083 | -51.31438 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f01073c7-6608-3265-908c-03a5cef68f79 | -13.00053 | -51.31644 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ac3effd4-18d5-34b7-a8c6-1e738ff67c3c | -13.00031 | -51.2608 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a0bca48b-c2bc-3564-aab4-70421c3ffada | -13.00025 | -51.25851 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b07adce8-92cb-3c62-827b-d25606322a33 | -12.99968 | -51.26631 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7512874-caed-301b-a4ab-067ba52f5fa6 | -12.99966 | -51.26405 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b93e05cf-c773-35a6-9c63-25a3556fa395 | -12.99906 | -51.26958 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68efa4a0-5ed3-3ecc-9f86-a65cf3f37ed0 | -12.99905 | -51.2718 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f6b65bce-89de-36e4-b3fd-9d3155b3c243 | -12.99865 | -62.7118 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c344ef9-9fee-3c4c-90a9-4c2f6a56dcf3 | -12.99847 | -51.27509 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 955450e6-524c-337e-ad8c-e4432961ec3d | -12.99842 | -51.2773 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54847abb-554a-361a-b517-eb4e0581ee0f | -12.9981 | -62.71539 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 504e0c50-d5a1-37f1-ae8d-322ac20a2492 | -12.99788 | -51.28061 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76067381-96d5-3f77-8e2f-54c2915519ce | -12.99779 | -51.28279 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5a5233a-5f3f-3518-9626-35b83a9f6ea2 | -12.99757 | -51.22687 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b36f0f1-ef4e-33a8-bb1e-727ca05c9991 | -12.99755 | -62.71898 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5135fbd-1def-37ac-a402-16c5d9416952 | -12.99729 | -51.28613 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 29c84b21-ed9e-35ee-b50a-48209092e107 | -12.99729 | -51.22449 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae2d3233-1aa7-3e18-b4c3-37aedcc770eb | -12.99717 | -51.28829 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| df826bef-2e0c-3687-b87e-364455992e0d | -12.99693 | -51.23241 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 057ff241-6033-3756-b75b-3bd832707698 | -12.9967 | -51.35261 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cea4c084-5603-319f-8d47-6b3c632ff88c | -12.9967 | -51.29163 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9699287b-6c1f-3d57-b983-ce4a5defc5c6 | -12.9967 | -51.23005 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0e6d18e1-c691-3a4a-b369-ed675f7d40ae | -12.99654 | -51.29377 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5cea96c9-0d08-3df2-a8d0-64419f05cd33 | -12.9963 | -51.23795 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c6f41e9d-8421-3a78-adeb-519c74300419 | -12.99614 | -51.35463 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3dc03977-6202-3663-8a3b-aad2ce8c7c29 | -12.9961 | -51.29713 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| f36d85bc-9e39-34e6-b6d7-85bc41577d63 | -12.9961 | -51.2356 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1d0a4725-c6c5-360d-9acc-5299b0f06a19 | -12.99591 | -51.29925 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ab16dd31-7ef1-32a0-8127-a388f9a3f0b2 | -12.99568 | -51.24346 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c6f4ee33-b42c-3e0f-9bd5-779b67b5a3e5 | -12.99551 | -51.30261 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 3c205885-bb13-37d5-b579-07708199f54f | -12.99551 | -51.24112 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 906eeae5-69b1-351f-9463-0f68850d37d6 | -12.99529 | -51.30473 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 3651f845-0852-3ebe-b028-0b079c5337ee | -12.99492 | -51.30811 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1624124c-a777-372a-92fc-14fd4145987c | -12.99475 | -62.71486 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b38efff-4700-3baf-a116-74a35a247aa3 | -12.99466 | -51.31021 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 13c0fb4d-20ef-30c6-ae7e-64cf6a3c094a | -12.99442 | -51.25451 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b20a431c-ebb5-3f92-b8e2-4711c66bca17 | -12.99433 | -51.3136 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c75b8217-83d2-3309-951f-572e6a905cb9 | -12.9942 | -62.71846 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e96cba-4a61-3bc0-b6fd-e06dbf2e8d87 | -12.99403 | -51.31568 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e57507dd-ccdc-37fa-8d45-b374a600ae4c | -12.99379 | -51.26003 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a0bd4c3f-1ca8-3588-b4ed-bdf4d038165d | -12.99374 | -51.31907 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc6e5080-4c71-3522-8a2a-a87437978042 | -12.99374 | -51.25772 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 15dadae0-6ce1-3d3f-b1f6-1b8a9ad161b8 | -12.99341 | -51.32114 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 813873d6-2569-3f5f-92df-6a54e537a291 | -12.99317 | -51.26553 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3063827-f9d8-37a5-9faa-f607b78102bc | -12.99315 | -51.26325 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 96618777-626f-3f58-a4c8-d11d6d136c7e | -12.99255 | -51.26879 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ae01de2-6808-3654-a5f6-9c09ef255830 | -12.99254 | -51.27104 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| be0306e5-b8a2-3fb2-bb64-eb5c37924394 | -12.99196 | -51.27431 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34292139-66a0-3726-955a-0de05a49bd30 | -12.99191 | -51.27654 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb68e31e-4935-3404-96b4-4097574f9f9f | -12.99167 | -51.22054 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6cb7cc4d-46d9-35ce-9679-00c4c5b8514c | -12.99135 | -51.21813 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 603c8401-1922-3556-ae66-da58528229c4 | -12.99129 | -51.28202 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a05b8157-4809-3d2b-9454-d7bb899cc987 | -12.99104 | -51.22608 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ab6237b-d2d7-3df0-a6fd-947ada0fbf61 | -12.99078 | -51.28532 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 69c0a863-3616-3240-9dd4-20bee6c6b44f | -12.99076 | -51.22368 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f1d1187-d800-3ae4-8c9a-094efef6caa6 | -12.99066 | -51.28752 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 766f3719-b938-3dc0-9930-9e6b1d7ed89b | -12.99041 | -51.23162 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 73ab1018-e4a3-3b81-b23d-9594d3ef4842 | -12.99017 | -51.22922 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5504d5d8-21c5-3b78-83d2-6da851579494 | -12.99004 | -51.29301 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2f405e4-169d-32ac-a8e8-06cb935040e1 | -12.98963 | -51.35727 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd0d8f4c-fbad-36a2-ad2d-bc667495c18b | -12.9896 | -51.29634 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6445b237-444d-3066-8816-3a2c30f361bf | -12.98941 | -51.29849 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| dce5d70b-bbe4-38d1-8184-d2e145c149a7 | -12.98904 | -51.3593 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05186c87-d609-3768-92ca-85b8943e44c0 | -12.98902 | -51.30183 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 743990e6-08c6-3c6d-9e37-7d1e97329d6a | -12.98879 | -51.30397 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 73b3e154-43b8-3ec5-b1d2-f0b23009b869 | -12.98843 | -51.30732 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| bec38717-c3d1-3d2b-bf35-bcf36abb62dd | -12.98816 | -51.30945 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a4a45371-c08b-3df6-8950-199336986b83 | -12.98784 | -51.31281 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 44c819f5-6293-37ed-bfa7-e01e67e7886b | -12.98754 | -51.31492 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f5626755-d2eb-3e8b-99f3-09e019068e0f | -12.98745 | -62.69526 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17d30295-3743-3ef1-aba1-bd4cb2c48608 | -12.98725 | -51.31828 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ec7f1298-71f1-3f39-ac60-8eb6ed8126ab | -12.98692 | -51.32038 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e3a328b2-1a16-3ed1-8607-4de1a035b4af | -12.98666 | -51.32375 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 71b7e7f7-4295-35bc-be19-e7a879b83767 | -12.98665 | -51.26476 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README140.md)
