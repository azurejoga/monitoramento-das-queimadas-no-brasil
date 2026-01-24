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
| 975dce88-f4bc-36f0-9efd-180122033c9a | -21.13855 | -48.66711 | 2026-01-24 05:10:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 908fe980-325d-3c15-ae0e-15e7c9c05065 | -19.6839 | -56.85738 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8dee736e-2f84-3edc-8d26-cc1f893d0ff5 | -20.45325 | -48.6832 | 2026-01-24 05:10:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 114d7625-73b3-3a2f-8c62-c99c32613794 | -20.32922 | -57.84938 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0c73233f-8d72-3b59-a823-969b7015d46f | -20.33986 | -57.84728 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 1e7456ca-a2ed-312f-9536-5acdfe855f23 | -19.68734 | -56.85794 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7cc91482-d1c5-35b5-b72d-3e6fbba2fd9d | -19.68095 | -57.19294 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8c90c3fd-8eb8-37ae-b565-2fb6965e19da | -22.02141 | -56.33823 | 2026-01-24 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f25e2ac-80f7-3568-8a18-a9f8b24b6f1f | -19.69021 | -56.86246 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2e69e897-9500-3b3c-84e4-241fcdf19db6 | -20.36806 | -57.85518 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2d43fb8e-6fdc-3091-abee-87078e1bc4c9 | -19.17972 | -57.54396 | 2026-01-24 05:10:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3de28bfd-7c63-3db5-8b78-0b02bb624c7c | -25.41421 | -52.99282 | 2026-01-24 05:10:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ea093a2-8547-34ea-b5b8-2f30aca1ec9c | -23.01 | -52.38298 | 2026-01-24 05:10:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8f75aec8-b21c-366c-9ae7-ef78da36d9cc | -20.32586 | -57.84881 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 28e5a6ee-8564-3047-ba64-07c87eec28d6 | -19.67738 | -57.1895 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 116e8bdc-2c6d-378e-a650-2c927dd83c1b | -21.13892 | -48.66298 | 2026-01-24 05:10:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9f55378e-874a-3cca-a8cb-caf3a06a9924 | -20.37701 | -57.86445 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0799a908-36af-31ee-a097-bccecf2a01d9 | -19.6768 | -57.19338 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 327503a8-af70-3e58-816d-2041b6c6489a | -19.6734 | -57.19282 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c4f87595-cb41-3ac7-9170-bed865dd6dee | -20.35183 | -57.84858 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8a190045-579b-3d65-9950-6f31b05bbc4f | -21.53847 | -57.53711 | 2026-01-24 05:10:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6dc1044-1973-343e-a9ea-b66a18b3cecf | -20.37086 | -57.85953 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a0811a05-60d7-3e80-8a61-265d7fa2f8a0 | -22.0256 | -56.33442 | 2026-01-24 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6b6dae9-58da-3c3e-b3cd-71720965db88 | -20.49882 | -55.19307 | 2026-01-24 05:10:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f603c20-6ed7-323a-b8a0-bff92980660f | -20.45891 | -48.6838 | 2026-01-24 05:10:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22aea794-ad9a-3ab1-9c98-9550b2d11b6b | -20.33314 | -57.84616 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1082da22-d9ae-3004-bec7-1a1400655f68 | -19.67283 | -57.1967 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 97deb315-e482-3c85-a13d-474b1d3630f2 | -21.14227 | -48.66645 | 2026-01-24 05:10:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| eca5f0c5-2d7d-3e92-b3eb-59b540a085ee | -19.67702 | -56.85627 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0480e459-6b99-3624-8e28-9634a5af95dd | -20.3675 | -57.85897 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3ac7e69e-01fd-3b4d-8d76-583cc2b419df | -19.6802 | -57.19394 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 77a88342-6d86-3ccf-b1ab-69db4dedf0ca | -20.3365 | -57.84672 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57f5be5a-ea3a-3a6d-a50e-d828bdbe9470 | -20.34321 | -57.84784 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 0ef0565e-9ff5-3db8-8832-1208c316aec9 | -20.33257 | -57.84994 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a079faa2-3694-3f7f-9158-83a2273afa6d | -30.05148 | -50.75584 | 2026-01-24 05:12:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 0fa47a7c-25f0-30ec-b0af-5c93e08e864e | -30.05729 | -50.75259 | 2026-01-24 05:12:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 2389ea38-7c95-3d25-b4ef-62dbf3d20036 | -30.05175 | -50.7571 | 2026-01-24 05:12:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| b7c46ad8-a629-3e55-b19a-5c3b751c6873 | -30.05757 | -50.75385 | 2026-01-24 05:12:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 9874f20a-9614-38a9-9ed1-6d438c10f9e5 | -3.84726 | -38.58049 | 2026-01-24 05:16:00 | AQUA_M-M | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 24.1 |
| bdbcbbd0-f22c-34af-87f3-9acaeb039dde | -3.849 | -38.58617 | 2026-01-24 05:16:00 | AQUA_M-M | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 81b954aa-53a2-38ea-9bca-21730c80d03c | 4.23965 | -59.98528 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dc33cfa-3136-38de-8d99-dd0941793f64 | 4.24019 | -59.98872 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf571c53-9ce6-3849-b231-ab6eaed210eb | 2.43255 | -61.14368 | 2026-01-24 05:31:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cfc6ba3-a895-337a-bf16-37289159ac8c | 4.16665 | -60.67984 | 2026-01-24 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92eb41f4-8221-3cf4-bd3f-0ee646a6eaaa | 3.78076 | -61.00211 | 2026-01-24 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31a6ecb6-53d3-32d7-88fa-df33f10e4af8 | 4.24464 | -59.97388 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f72f40f8-5c0a-384c-a96d-e8827da445ea | 3.2215 | -61.19423 | 2026-01-24 05:31:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e72ca4c-4b78-340c-80e7-5a53edff708d | 4.17054 | -60.68282 | 2026-01-24 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ccb200f-f740-35f2-9366-5ac9c7dc70ba | 4.63785 | -60.43021 | 2026-01-24 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dbf32cd-2b03-3b6e-941d-1a08dc08e843 | 4.01917 | -60.58481 | 2026-01-24 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b52f870a-b237-311d-8f1e-7ee71c2bf33d | 4.24519 | -59.97733 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0e4d5b-1448-3c13-9fb1-adeeb3126c45 | 4.24242 | -59.9813 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e2121b-f7bb-3c01-88d3-62388d2a01be | 2.51529 | -60.98397 | 2026-01-24 05:31:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d49cd39-4e8f-3487-aa39-49cd9bbc9884 | 4.24296 | -59.98475 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13b28f5c-767f-3ac2-a8ed-8404b97c64bd | 3.656 | -60.16903 | 2026-01-24 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 894a3e17-8fcb-39ca-9d0d-dda2084b95b1 | 3.49494 | -60.9099 | 2026-01-24 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aa08e6b-5419-3c3c-9619-c027b5e5b1bf | 0.55038 | -59.85188 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5e05112-2775-33fd-bb38-1911379e28cd | 0.55373 | -59.85135 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 721689e7-88fb-33f8-bf62-5b207731bfc4 | 1.92649 | -61.19696 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c98d9269-6bfb-3f3c-9b9f-cef8f9fb5b4c | 1.32704 | -60.41868 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9fd4600-8c75-364c-ada2-34c017628fa4 | 0.55707 | -59.85083 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 480fa7ea-bd37-3502-a17f-163873d40738 | 1.69268 | -60.35744 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c25ba05b-f22c-3110-a823-6f3da7e53bc8 | 1.35745 | -60.0354 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c4478b4-f662-3157-af1e-2216975ecd09 | 0.77832 | -60.18285 | 2026-01-24 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf1e54b-b709-390a-8dcd-4e573cf3dd98 | 0.55652 | -59.84733 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f55af80f-c1b8-367f-b634-e7719cc374d8 | 0.55541 | -59.84035 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e73e295c-0ddd-30aa-ad15-be492392f585 | 0.55597 | -59.84384 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffa650c4-2452-3338-92e0-db1501abd9bc | 1.35408 | -60.05721 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 966ca097-9499-3296-aee0-4be9bc3514c3 | 0.54983 | -59.84838 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54cfca01-4215-36e7-a59b-b0933c9e0e36 | 1.32758 | -60.42212 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09342b17-309e-3d85-8019-3f6a1f7a5ad0 | 0.55262 | -59.84436 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f607629-a89d-3e44-a5ed-6abcf41ceabe | 0.77887 | -60.1863 | 2026-01-24 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 938321e1-1ef5-3004-9200-202ddad88ed7 | 0.55318 | -59.84785 | 2026-01-24 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36ab2892-a9c4-3e8a-a24c-18376fe7bf11 | 2.04522 | -60.87202 | 2026-01-24 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eb5b1c2-fa9b-3a83-8f2a-918f3a7d4a36 | 1.81207 | -61.24332 | 2026-01-24 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554106c9-a615-3cc4-9fa8-a9137fbe775d | -18.25551 | -51.27779 | 2026-01-24 05:37:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 148047f6-69a4-3ac5-b29f-e368cb021402 | -19.67419 | -57.19221 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e0d4d733-a129-34ee-8f94-f8108795b034 | -19.68949 | -56.86536 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e4ec85a9-6609-3ec1-8ac0-8aeb1cda8b6b | -19.66804 | -57.203 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b36ac771-731a-3d4e-98d2-be6f001ef925 | -14.33418 | -57.7228 | 2026-01-24 05:37:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04aad29a-85fa-3b5d-8448-65eb5da9e8ea | -19.68013 | -56.85811 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0a10e79a-835e-3eb6-8b97-3aa9023df2bd | -17.70113 | -53.26815 | 2026-01-24 05:37:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50216a4f-3ec5-307d-836c-dd38ba4c134f | -19.46698 | -55.44634 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 4645e363-c72b-3c62-8a8a-dc1af058b7bd | -17.70683 | -53.27357 | 2026-01-24 05:37:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f265313-bd88-3b62-bdb9-71a24e7fdd53 | -19.56614 | -54.44306 | 2026-01-24 05:37:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa1b2146-a1e4-3993-ab98-dc4aecfc78d5 | -19.66571 | -57.20613 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 03f89831-a632-306e-885d-cf7b94cfedfa | -16.17331 | -59.45043 | 2026-01-24 05:37:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86f3e353-8559-3060-be29-d36c54e71cb5 | -19.67193 | -57.19537 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| de2e11b9-3e81-33fd-b3c2-5cf7461291a6 | -16.44254 | -58.16579 | 2026-01-24 05:37:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ca0808f0-ec9f-3a55-b4aa-e90dc0a3ac9f | -19.46736 | -55.44264 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| dd009b30-b61c-3f9b-95bc-2d66e006bbe7 | -18.24856 | -51.27693 | 2026-01-24 05:37:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb3cb0bb-b4b8-36b9-87a7-d063303a5130 | -17.712 | -53.28421 | 2026-01-24 05:37:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558c0882-4da5-3399-87da-995099c1c976 | -18.25311 | -51.28213 | 2026-01-24 05:37:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20b043de-9a9d-3f4d-a8ae-fe5186a40545 | -18.25369 | -51.2752 | 2026-01-24 05:37:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c04af99a-cf63-31e6-a0b6-bb1ba370a7ad | -14.31042 | -57.59355 | 2026-01-24 05:37:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b3bbb2f-973e-3caa-bf82-31659af4fef2 | -19.56069 | -54.43816 | 2026-01-24 05:37:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e4b54c3-ff87-373c-adb0-1d68fd699cac | -19.68515 | -56.85873 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2a0d6f87-f50d-33f9-b0a6-90622a58c4d8 | -16.30848 | -56.56365 | 2026-01-24 05:37:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fca0e83d-3bee-3865-84fe-67fdd07d91d9 | -19.67511 | -56.85749 | 2026-01-24 05:37:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c0bf411-ca91-3ed8-9d83-ce18ed6475d5 | -19.66866 | -57.1973 | 2026-01-24 05:37:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |


[Clique aqui para ver as próximas entradas](README7.md)
