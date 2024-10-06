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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c7065ab-b74d-314a-b23c-07402514616c | -13.67885 | -51.1946 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| afd0cdc4-db87-3c0c-9b7c-cd217565346d | -13.67549 | -51.18605 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eba3d021-b57b-301b-b685-9dbe5c0a7c3a | -13.67454 | -51.1906 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64d323eb-c00e-3856-9d8d-9bfade559b04 | -13.6738 | -51.18872 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4fcd0e47-b8d3-3306-8804-85e90f68c3a0 | -13.67288 | -51.19328 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2c0ba79e-c688-3209-b137-1e64af9d024c | -13.66856 | -51.18929 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 983ebb34-2e97-30fd-af95-9427fec5fa09 | -13.66782 | -51.18739 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 611f6cb4-bf71-3271-9e0d-cc3642779306 | -13.66761 | -51.19384 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fbbbf9a-a331-398f-bea7-3f4603752e16 | -13.6669 | -51.19194 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 57d062fb-92f3-3b5a-9fb8-5139064c80ea | -13.66259 | -51.18797 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a942bb27-9da0-339d-81fc-81d868d47f4a | -13.66184 | -51.18605 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d551b90b-7411-312a-af9c-308b134dcce9 | -13.66163 | -51.19252 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 097a45a5-5862-3604-a561-45c10c5d5f1f | -13.66092 | -51.1906 | 2024-10-06 03:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6dd8938f-1e98-36f5-a209-01e02c02e4f9 | -16.06998 | -50.44885 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4415630c-db7a-310a-8396-0db2d54e10ca | -9.38189 | -51.07323 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e5796e6-c02b-3a02-93a7-ea3e5bd986a1 | -9.38085 | -51.07866 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfe59926-e1c3-386e-8b1a-ab8807300d0c | -9.37878 | -51.08938 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2c4157e-2383-3a61-8b8d-23d54fa0c817 | -9.37775 | -51.09471 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6faa4613-13ac-36f0-9fd2-423d64278d34 | -9.37135 | -51.09337 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2c7e890-d3f0-3400-9826-d1b96143feb2 | -9.36805 | -51.07602 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0492bfa-e69e-3294-a4eb-ddcd0f9e81c5 | -9.36701 | -51.08142 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e9b99a1-6fd4-30f2-811d-cbe5b46df543 | -9.3606 | -51.08016 | 2024-10-06 03:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beb12ad1-7057-3408-a76f-388b69a63680 | -10.51548 | -50.96168 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 306a2563-3c99-3597-8005-4059e642ab26 | -10.50926 | -50.96032 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f338640-a637-3564-ba36-7a43f9dc423e | -10.43785 | -50.75037 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a03dc8d-5432-3e34-8944-dca47232aae4 | -10.4335 | -50.74785 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fad2779-8cd8-31f6-b4b6-fba759324e0e | -10.43257 | -50.75266 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd88d656-3de9-36aa-b5bd-5c1fc4ff6b8e | -10.43165 | -50.74929 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f60091e1-a29e-3e75-b0e8-f59bed6b1380 | -10.43068 | -50.75411 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75314810-5442-364a-b0df-68d6c949993c | -10.4273 | -50.74674 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abd7c528-5f8f-3de7-8234-4ad4100d96ba | -10.42637 | -50.75156 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eb6fedb-0993-3de8-8f09-0efa6e601bc5 | -10.42545 | -50.74821 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6bca5c3c-12d2-3116-8b2a-c991a804680d | -10.42543 | -50.75641 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21650cc8-7028-33a1-8a2b-b72163573856 | -10.42449 | -50.76128 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b56b0f9-38f8-35e4-b98c-55002c9dd454 | -10.42448 | -50.75303 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 968b2dbb-eb19-3f92-8387-a25e1ae7acc3 | -10.42351 | -50.75788 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b32fe099-c97f-35ef-83b9-e4b8a33fa68c | -10.42018 | -50.75044 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 508695ab-5084-3a63-8994-e642c964684a | -10.41926 | -50.74708 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8f232e2d-abd5-35e4-b322-ce127c81d367 | -10.41924 | -50.75528 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b613da5-d5d1-313c-b231-be536b9ae4bb | -10.4183 | -50.76011 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1163494f-6665-3305-bdad-982a331f0eee | -10.41829 | -50.75191 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ab70730-3936-3f61-b0b2-de866d507893 | -10.41737 | -50.76495 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb4d68a3-cf8d-3459-93b7-f4591a082e5c | -10.41731 | -50.75675 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e71664c3-a9ce-3149-986a-f00cabb41ad4 | -10.41635 | -50.76156 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72159848-48e1-3ffd-b8c3-4f50b929e352 | -10.41538 | -50.76638 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cadca198-bbbe-3f5d-90d5-379864a71d87 | -10.41399 | -50.74926 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 93b18b78-b7c0-3d6c-939b-06c75b323160 | -10.41305 | -50.75409 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 477fe8b2-0cff-3713-8af7-3c3f07d5ad07 | -10.41212 | -50.75888 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6efc22ec-8f57-3b10-bf57-67f5a57f6273 | -10.4112 | -50.76366 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b49e907-3d72-3346-896c-7ea5f3c72161 | -10.41027 | -50.76844 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed325436-3a3a-3f4d-9694-c597c56fafcd | -10.40934 | -50.77324 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 006a94ce-867f-3074-be46-0857b5fdd8e5 | -10.4084 | -50.77807 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d44827b-a7f3-30fc-9068-4c841ff557c2 | -10.40794 | -50.81363 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef37622b-5e31-3b9e-9b03-8a5ecd48c79b | -10.407 | -50.81845 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c220ea2-4a68-36c5-a488-3d5864cf04c7 | -10.40598 | -50.75749 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec40b603-e805-38df-8486-32da14793f02 | -10.40561 | -50.81495 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f96c44a7-a885-3c6a-a6f5-a80496064c74 | -10.40505 | -50.76227 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1bb0e9ac-70af-3e1d-abc3-eaa40cbfc705 | -10.40463 | -50.81981 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e02a9f0-8858-3507-bfff-47da346fd1a9 | -10.40412 | -50.76705 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ab28a16-418e-357c-b84b-c72e18f1cb71 | -10.40318 | -50.77188 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bc4468d-e09a-37ea-998c-e5c397ac83b7 | -10.40266 | -50.80765 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43aa86f8-64fd-34b7-a620-3e318e1405e1 | -10.40221 | -50.77683 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbe287b2-9252-3acd-9ed7-e081b25d3829 | -10.40124 | -50.78182 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bec9183-4dc0-3775-bbe1-edff014e1032 | -10.40028 | -50.78678 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 539423eb-0ee2-39fc-ac96-6553e49120d5 | -10.45253 | -50.70888 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd8f7161-7b5b-3a22-9ffe-0365d42533fb | -10.45159 | -50.71359 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5d9d9cb-db09-3231-a546-f41727172d46 | -10.45136 | -50.72159 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 381efabb-17ee-3338-90f4-f45f33313eff | -10.45066 | -50.71829 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a922f935-219a-3c43-b50c-0751af285223 | -10.45046 | -50.72627 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa891c16-52ca-3595-8a29-7ecc90e028ba | -10.44975 | -50.6967 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5eab1fa9-d7a9-3c26-9176-1272f8e79dcc | -10.44972 | -50.72299 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8eea8bf-9cab-335c-b8d2-33a3a419ada7 | -10.44956 | -50.73097 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0cd085a-5ee3-3118-bbbd-32ea0ece92be | -10.44921 | -50.69345 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07aab7f0-2a7a-38f3-ab69-b5238e7a08ec | -10.44884 | -50.70142 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 329df36a-4872-36d8-a347-b869a0dd8d9e | -10.44879 | -50.72768 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1e69100-6699-37b0-852c-cbf70d1eb8ea | -10.44827 | -50.69817 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| b16ddb4e-8710-3b41-9e4c-9109a2479196 | -10.44793 | -50.70615 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35dad0e6-ed97-3ab6-a28c-2c031f2f64a6 | -10.44785 | -50.7324 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96684428-02bf-3720-915c-cc91159710a3 | -10.44733 | -50.70287 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 96e06605-fd31-3610-a6e2-84637995023a | -10.44701 | -50.71091 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ca73578-fb51-354a-b3ea-32d46d2cb5da | -10.4469 | -50.73715 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e41c0b54-67db-3b63-9f0a-3a711ebf4253 | -10.44639 | -50.70761 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 5f73d321-0daa-3a04-989f-bf3d949fe61f | -10.4461 | -50.71567 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 41e32a27-8a4b-30dc-bf7b-1345f08fdf24 | -10.44544 | -50.71235 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| aa39f7b0-6ae4-3b52-af9d-372c5d8d43cf | -10.44519 | -50.72042 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3a2a6e9-49d8-3df3-958f-d8eb2bbf61fa | -10.445 | -50.68252 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eca363e0-2db9-3f3b-ac75-031d79b53344 | -10.44453 | -50.6906 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6b20865f-6d60-34b4-a70d-77cdef4abc75 | -10.44449 | -50.71709 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0e7a5e3d-939e-3e4f-b15b-2508430da900 | -10.44427 | -50.72517 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 116d7028-16b5-3758-ad07-e5dab815e621 | -10.44404 | -50.68734 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf5939b5-f197-3268-863e-dc42f123c6e7 | -10.44361 | -50.69539 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e03eeaf7-8ba7-342c-9744-7d45323b73f2 | -10.44355 | -50.72184 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 609599d0-d819-3484-8214-85a29fbe0e63 | -10.44336 | -50.7299 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c60e4ee3-d8a7-3e57-9b2a-aca58d7294dd | -10.44308 | -50.69214 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23ed105b-337e-32b2-9241-37a52e87d777 | -10.4427 | -50.70013 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 207.7 |
| a99fd480-059c-3a0c-9741-c81c49e31415 | -10.4426 | -50.72657 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0ce17312-9947-3e85-b9a7-492746847e2b | -10.44244 | -50.73467 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df7cfd53-dc3d-3d29-bdd8-b15a6ef9fcad | -10.44213 | -50.69691 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| f97d00e2-89c5-348e-a654-10257d9d365f | -10.44179 | -50.70485 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 4f3f5e1e-6c70-3f66-aca0-53d0a2ae6fdd | -10.44165 | -50.73133 | 2024-10-06 03:55:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README57.md)
