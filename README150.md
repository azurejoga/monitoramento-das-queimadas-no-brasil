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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf60dd0f-3c74-34c5-a035-1d4540bb4bc4 | -15.90908 | -57.16904 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eda9578-dcd3-3edf-bcf6-e5899c97b406 | -15.90836 | -57.17466 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7577499b-3650-3d77-84cd-d7d1f0271736 | -15.90824 | -57.17089 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5710a21-002a-31a5-9183-eab9acca9402 | -15.90763 | -57.18034 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea599759-39b7-3497-9aff-d02c05ffda06 | -15.90755 | -57.17666 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 625e723d-05f3-3126-87ea-27b9c7275cf6 | -15.90368 | -57.17458 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ea5a0ba-4366-3f4c-82a0-e52fa64b2f77 | -15.90299 | -57.18005 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48618040-df00-34ac-b9b1-c8a3778d479f | -15.9029 | -57.17649 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73e9d5ac-ec48-339f-8f70-400b43d333b7 | -15.90234 | -57.18508 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66c1fc03-a3dc-3869-829a-cc4d774c8e71 | -15.90227 | -57.18177 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e9520b2-2f04-3dbc-860d-be3041f0a96c | -15.90167 | -57.18674 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe45f64-d53e-3f4c-a765-ec7a45060a59 | -15.89773 | -57.18459 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d152a570-e98c-37d3-8ae2-735e712aaed0 | -15.89706 | -57.18622 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fab0a5a9-c776-3e30-acfa-7e7f37b4c619 | -15.89254 | -57.18866 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27823605-7407-36c5-9146-7c93d7b269f2 | -15.88797 | -57.18783 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53e746ff-ac04-359b-a021-b32c97eb90b1 | -15.88338 | -57.18713 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4b7361e-3879-375e-9e03-5799985c14d7 | -15.68548 | -53.9132 | 2024-10-01 05:31:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc347a95-17b6-3848-861c-0786e76d09ad | -15.68501 | -53.91747 | 2024-10-01 05:31:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1172c57d-9724-3af9-bb6c-f0691e6c6b5a | -15.68455 | -53.92171 | 2024-10-01 05:31:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cfbfb4f-4c87-3b76-8852-3ab7159201a1 | -15.6841 | -53.92588 | 2024-10-01 05:31:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc2f5567-c7fa-3241-bdf3-703ebe54540a | -15.62604 | -57.45792 | 2024-10-01 05:31:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11daa387-9ac3-35fd-b85a-32004afbab13 | -15.62213 | -57.45272 | 2024-10-01 05:31:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e671257-ac16-32b8-849c-636d819aa13e | -15.48481 | -53.37596 | 2024-10-01 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d670887-a7f1-31e0-be40-efd0dda74545 | -15.48433 | -53.38057 | 2024-10-01 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36f6fa10-fd4b-383c-a583-e262f8b4d55b | -15.37384 | -53.75605 | 2024-10-01 05:31:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f459c263-0184-35d4-b4d0-c9b4bacf9ed0 | -14.93409 | -57.94543 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c620b319-eafc-3b0a-9b61-928980ed485a | -14.90135 | -58.02773 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e2016e5-2ff2-3f62-ad70-7bf62145ecbb | -14.90013 | -57.97023 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8e34170-d3b0-3d98-80b0-603f4b664a35 | -14.89761 | -58.02296 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c50ec501-a4ce-3532-b7b2-b187778e0b62 | -14.89705 | -58.02724 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baba6cd7-ea27-3cdf-aea4-a3487a479fe2 | -14.89333 | -58.02234 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 633df65c-bc78-3511-b402-776a196e0a44 | -14.89071 | -58.00893 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25dc5eb5-e7be-347e-af43-f9a7db1f89b3 | -14.89015 | -58.01326 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae078978-2f5b-39d4-a683-ca57f7364399 | -14.8896 | -58.01747 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e5dbc89-b795-33d5-a799-a4ea3df1d7b6 | -14.88905 | -58.02166 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73abdef1-4c72-3a94-8737-947be44665a7 | -14.88643 | -58.00827 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2aadd03-62ef-330f-924c-f8bde9b8e66c | -14.88588 | -58.01253 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a30f1ba3-7e8c-34d4-b380-b15a6584ac1c | -14.88278 | -58.00274 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 436b9493-2adc-3a43-a074-635cb7a3e3f6 | -14.88222 | -58.00708 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd4af80f-4c81-36e9-8c68-2e47e8e1f6b0 | -14.88165 | -58.01141 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e8d2b49-4156-3e7a-835d-e053c44c94c0 | -14.87855 | -58.00161 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b10a993c-b405-380c-81db-65797b0e9952 | -14.87799 | -58.00595 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7006e50-6a94-3c0e-a89a-1f3fc39666f6 | -14.87742 | -58.01038 | 2024-10-01 05:31:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 599d5dc4-1e18-372e-b6a0-f8d87c2473af | -14.70077 | -57.82248 | 2024-10-01 05:31:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab0bbd56-fa64-39b8-b1bc-05be1fadff6e | -14.69644 | -57.82191 | 2024-10-01 05:31:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23598ea0-fbf9-304d-8fe8-3efac0a1fc3a | -26.411 | -53.22604 | 2024-10-01 05:33:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9c545e9-182f-3bfb-8c67-a5a631db65d9 | -26.41061 | -53.23248 | 2024-10-01 05:33:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cb8748fe-c3a8-3a35-b4c9-f6673903c95f | -6.54631 | -43.02305 | 2024-10-01 05:44:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 736e79e2-6c37-35d9-ad3a-236bf2a6b81d | -6.54015 | -43.01742 | 2024-10-01 05:44:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| ca01c495-e2eb-3963-ae19-2cd362a23ea3 | -5.97912 | -45.37215 | 2024-10-01 05:44:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c0cbf97f-b861-3d31-adb0-40d40c63fcb7 | -8.44797 | -46.44724 | 2024-10-01 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5e4ff743-ae72-3a4f-b160-e3a081eb519a | -8.44613 | -46.45222 | 2024-10-01 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 235fe6e5-208d-3edd-8c0c-c2e7113204a9 | -4.75688 | -48.00313 | 2024-10-01 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6a6b63e1-f481-31e7-b606-229fa15fbab4 | -4.75366 | -47.99734 | 2024-10-01 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bface6ff-84c4-3f72-9e67-3b8f80460fb5 | -4.46577 | -48.10929 | 2024-10-01 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 296be37d-802d-3845-959e-ff6eab4274d4 | -4.46073 | -48.11511 | 2024-10-01 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ddbe12ec-6f46-3bf0-9454-17af35d3fb9c | -8.16125 | -49.45049 | 2024-10-01 05:44:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4b4c0759-9bb9-3323-81b7-34cfa1583d16 | -3.06675 | -50.48009 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed5332c9-3bad-32b4-9996-64a90912fd4b | -2.39849 | -50.32077 | 2024-10-01 05:44:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2a50c8c8-ae84-34af-8032-ac051638155f | -2.39712 | -50.3301 | 2024-10-01 05:44:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a7944be6-56c2-3822-ab79-de622579b6fc | -6.17753 | -50.90234 | 2024-10-01 05:44:00 | AQUA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4c498b1-7596-312a-9819-2c4e603878dd | -3.03259 | -51.33314 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c49cc8e5-2023-3a5a-85a8-994eb6c9a458 | -3.02371 | -51.33185 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1b30ff47-b888-302e-b16d-fd6858b3b9f7 | -3.02239 | -51.34071 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ccd74fae-17be-3e71-957a-8dbdb813cd13 | -2.90972 | -50.73349 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3b73e772-93c0-3f50-9a19-8071c0219f42 | -2.90837 | -50.74263 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 1c4047bf-3959-39b1-817b-d2f7ff0a7a94 | -2.90702 | -50.75175 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 223.1 |
| b5a5eeee-b2e4-3edd-9f56-bd18690f59dd | -2.90567 | -50.76086 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a5b92169-99ad-3486-a0ef-a82ebc52294c | -2.90207 | -50.72305 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5bf36f8d-b316-3bf8-aa58-dce7647ae8f1 | -2.90072 | -50.73219 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 4bd0acb2-0aa0-3a08-8094-8e46b6afc8e3 | -2.89937 | -50.74132 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 340bb9af-0b2f-3e17-b0b4-79845ae72dac | -2.89802 | -50.75045 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 187.7 |
| c8c983c6-1594-3a6a-bc5d-efda82e60d07 | -2.89668 | -50.75957 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b30d6f81-ba1a-3a37-a0ff-33db42e19f3b | -2.89441 | -50.7126 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 53597117-d605-357a-b86f-5f4926d6ca77 | -2.89307 | -50.72174 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 265.8 |
| 7735c382-bbd8-3b94-a8eb-270c80f4388f | -2.89172 | -50.73088 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 13d6cedb-493f-36b2-8674-b4ce9e8b8a25 | -2.89037 | -50.74002 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| bd4703f4-a791-381c-88dc-59185101fd80 | -2.88903 | -50.74915 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 12b09f42-60ba-36e0-8894-4407eebd6a27 | -2.88768 | -50.75827 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 21ea029f-5dfe-32b6-8580-fcc5121e59b4 | -2.88675 | -50.70214 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7f7215b7-10c2-3f90-898d-4e74face5e2b | -2.88541 | -50.7113 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 50514a49-71e7-359f-b167-fbdd22aa0f34 | -2.88406 | -50.72044 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 5a79cc94-343a-39e5-9d65-e51629201a7a | -2.88272 | -50.72958 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 0f80bac6-95cf-3880-9c36-395533c81335 | -2.88138 | -50.73872 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8f49b066-83a5-3eb3-ba1a-6a4ce48eb6fc | -2.88003 | -50.74785 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d17b03c7-be69-3086-a8ca-1060a2d2101a | -2.87869 | -50.75697 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| abcf04ca-ca8b-34f2-92ed-a6cff8c217ad | -2.8764 | -50.70428 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 81d56fa8-b37b-3e2a-83d7-be877900affe | -2.87503 | -50.71342 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| b7588a82-e7ce-34c9-acdd-0eeebb3f5552 | -2.87472 | -51.6474 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 957b7122-eec6-30a8-8112-37ff33a377b6 | -2.8734 | -51.6562 | 2024-10-01 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8729bf1c-16f6-3b86-aed3-f7130a3ffeaf | -2.87093 | -50.74081 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| ce838682-d937-3985-a90e-4ba298dc6d24 | -2.86956 | -50.74993 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 57c94cff-9e92-3e05-9be3-20c023882058 | -2.86602 | -50.71212 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 371ce364-e1ba-30dd-b995-c1251c66b3c2 | -2.86466 | -50.72126 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 836a703e-130a-31d1-9b58-5bc6379490ad | -2.86329 | -50.73038 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d2c345e8-59fd-37b4-99c4-ec10d63de45e | -2.86193 | -50.73951 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4695e8f8-b3d1-3117-a6ed-6bf6704665db | -2.86057 | -50.74863 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d3f2bdc9-b241-32a8-b5e8-ef1818b36db7 | -2.85702 | -50.71082 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3b9b7120-c91b-3af7-b869-1af5fc6cf052 | -2.85566 | -50.71996 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 8537bea3-c06d-33ec-b717-6d8633e1eb3b | -2.8543 | -50.72908 | 2024-10-01 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |


[Clique aqui para ver as próximas entradas](README151.md)
