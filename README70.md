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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4234bd8c-f205-37f2-878d-414be4fed519 | -20.12127 | -44.25212 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b9ae9897-a2e2-35e9-9d2a-812129c1b04f | -20.12116 | -44.27472 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71da3150-7e34-3b6e-9fc9-65ebd89ead26 | -20.11956 | -44.26313 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 587e84d2-f8c5-325d-ac24-78e0a5966fc6 | -20.11796 | -44.25153 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8000e7ff-0cb7-3899-beb4-28f47e490c1f | -20.11784 | -44.27416 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5595d59f-d391-39cc-8280-41542d9d927c | -20.1124 | -43.51281 | 2024-09-26 04:08:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77800971-32c6-310d-89e9-045adc25a85f | -20.11183 | -43.51656 | 2024-09-26 04:08:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8a58e414-e0ee-3de9-8de6-f20127808930 | -20.10917 | -44.24242 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d16aa9df-f870-3db3-9de3-c03f25ea8be6 | -20.10792 | -44.2724 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac59584a-836d-3ac2-94f2-a91283fb3bce | -20.10735 | -44.27607 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03872641-3afa-3206-84b8-b0cc99223e48 | -20.10586 | -44.24184 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf99b821-84db-3f3d-b7af-dc7c3e83346e | -20.10255 | -44.24125 | 2024-09-26 04:08:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 90c92ce5-4d3c-34cb-b8b9-e1dd2fe8b99a | -20.09998 | -43.8415 | 2024-09-26 04:08:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 10585331-51a1-3563-aab5-fecbc3479e38 | -20.09941 | -43.8452 | 2024-09-26 04:08:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c857a280-7bef-3bb3-832a-79ac9435162d | -20.09666 | -43.84091 | 2024-09-26 04:08:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 02862d6e-62ab-3ee8-b9e4-db593b146de9 | -20.09609 | -43.84462 | 2024-09-26 04:08:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58cbdcfd-0089-3583-8f7e-07f1b5d327df | -20.06853 | -43.80178 | 2024-09-26 04:08:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| afa2e587-bd1f-3462-8fb9-66787f8612d7 | -19.9518 | -43.87689 | 2024-09-26 04:08:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dfa7da73-1cb6-3abd-9de9-7b45b3b4b395 | -19.936 | -43.7795 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7867f355-f509-30b1-868b-233da491caf0 | -19.93323 | -43.77525 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3174e21f-42bb-33c3-a08b-3f4e04769b1c | -19.93319 | -43.79787 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 533278ed-2069-35fc-841f-1775a7d8d496 | -19.93267 | -43.77895 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1433b675-4286-3998-b885-9511c62ec703 | -19.93211 | -43.78263 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8eefaeae-7fed-3a56-a808-b9f6792fbdf6 | -19.93043 | -43.79363 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c22fd74e-6711-39b3-862f-4ce2b2c39917 | -19.92987 | -43.7973 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e74b2701-7c44-3b88-9a3a-b0430fc2b738 | -19.92934 | -43.7784 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6251073d-dfb7-3d56-8538-3a4640869aa9 | -19.92822 | -43.78574 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3597f109-d0d7-3c40-94db-ebd5fd66de16 | -19.92766 | -43.7894 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e2f3e11-4533-3f54-abc9-a371e575c228 | -19.9271 | -43.79306 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9374e212-01f2-3025-8a4a-021befc5c1a3 | -19.92654 | -43.79674 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6a620227-d2a5-3fdc-bc12-b3c27c1ea7cf | -19.92598 | -43.8004 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fd01e373-c746-3b63-86d9-4c2283a0b1a8 | -19.92546 | -43.78151 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1524730e-afa1-39e1-8c0a-5b8584ac138c | -19.9249 | -43.78515 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 25ba49df-ec5f-3c6b-b8b1-a832fde72d71 | -19.9221 | -43.80349 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7d912e1-875a-3e5d-8c0c-ee14867987fc | -19.91933 | -43.79926 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29b934da-7c0b-3b63-bf12-de56e87d4811 | -19.91878 | -43.80291 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f97c96e8-7149-3340-af0b-c38c3a8d2b85 | -19.91657 | -43.79501 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6fb43004-a2fa-3f1e-a73f-849de9604f9e | -19.91601 | -43.79868 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7276229f-faf7-3230-bde7-5553c13b90fd | -19.91325 | -43.79442 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f162f86-509d-3442-877e-64fe0171df1c | -19.91269 | -43.79809 | 2024-09-26 04:08:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 133a89a3-5d0d-32d3-9ce1-bd51845abbe2 | -19.81162 | -44.06063 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fdcb90d-332e-3e82-829b-235ae1406c71 | -19.81106 | -44.06431 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 487e103e-628b-3570-b6d6-9ccc00e7f61e | -19.80831 | -44.06006 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da614b74-ebff-3cde-a0ad-cd10123708d7 | -19.80774 | -44.06373 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 618ee191-5513-34b4-a7f8-9b68d38f484d | -19.78702 | -44.13165 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b3affbd-aba8-3bd0-8339-941ab7309cbc | -19.78371 | -44.13107 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2becf121-1423-3489-a315-621d8267f89c | -19.75358 | -43.97538 | 2024-09-26 04:08:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e3ff8d6-7d64-3c7b-a962-b69b017bf0e9 | -19.75301 | -43.97905 | 2024-09-26 04:08:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeeec573-ee78-3b01-9b14-c2c0a4050dda | -19.75026 | -43.97481 | 2024-09-26 04:08:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f8da6be-34d8-3b75-9667-46148c2bb7f2 | -19.74969 | -43.97849 | 2024-09-26 04:08:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13e1b8d5-3dc2-3498-b724-a3f843bcbb40 | -19.74897 | -43.64967 | 2024-09-26 04:08:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86cfc8ac-6f57-35a5-90d1-b3b3c7aa4451 | -19.65665 | -43.81202 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 435b0861-ace6-36e6-9f80-ec53e442dbbc | -19.65608 | -43.81572 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 373e2aef-01bb-3046-a7b2-8d2eb3ee8672 | -19.64944 | -43.81456 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d91eeb3-ebc8-3333-9f78-a4a9405e6952 | -19.64612 | -43.81399 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21620178-9c22-33a3-b975-7b00a70ed460 | -19.64341 | -44.15946 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a757c8e-60d0-322a-8fe9-6e8ff97bbf15 | -19.64336 | -43.80973 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c87e924c-f1c1-3083-b562-ca4cdc76af30 | -19.64284 | -44.16312 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b23e1a6-ab44-38b8-b5af-4555b6a84001 | -19.6428 | -43.81341 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 227c15dd-8d1b-30fd-a5e1-3d0159282d0a | -19.64228 | -44.16677 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81466c93-ea21-36ae-8c7f-befd7d957382 | -19.64171 | -44.17043 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a8ab266-77f5-3050-984d-8af80f905f56 | -19.6401 | -44.15888 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a6fb757-acb0-3f26-82fd-5a7785546545 | -19.64004 | -43.80917 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb50ba62-d9b8-3185-aeb1-f6f27796c579 | -19.63948 | -43.81284 | 2024-09-26 04:08:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2990a76a-80bd-3cfe-8dda-2aeb5593cf54 | -19.6384 | -44.16985 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbebb89f-fd93-36ae-b732-d53175c59a56 | -19.63792 | -44.151 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a050e85b-cbf9-3264-a625-c6b875f42f41 | -19.63783 | -44.17352 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59ad0025-178e-313f-a369-f36f8f4e1dfa | -19.63736 | -44.15465 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05fa5a54-8307-3f4e-8cb5-826edf5757af | -19.63726 | -44.17718 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3dbbfde-23a5-3086-9986-dc4af0d7cfcc | -19.63679 | -44.15831 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 845cd438-81ae-3dd0-a3b2-87dcbf48761f | -19.63669 | -44.18085 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4d2033c-90de-32f5-8ddc-40ca645de572 | -19.63613 | -44.1845 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f246d58a-02b1-3fb6-96a9-e99797ff3192 | -19.63604 | -43.61188 | 2024-09-26 04:08:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3b142b5-1cfe-3390-ac97-c3b8afaff5f4 | -19.63338 | -44.18027 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c061041-2837-387d-a7c3-3b15fd771fc2 | -19.63281 | -44.18392 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e026f9b8-7ed9-3528-bacd-81611c19d678 | -19.63225 | -44.18758 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42b4c464-cc1a-3e36-bb60-a4179f88895b | -19.63205 | -44.23256 | 2024-09-26 04:08:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1639ffc4-84f5-3c4f-bc00-a240c8e98d47 | -19.63106 | -43.59974 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3796d198-d372-3561-96f2-d57bb622e0f2 | -19.6303 | -44.18011 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4945c6d3-7b18-3731-a041-26892ca3e190 | -19.62973 | -44.18376 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7fe02ad-1cd0-37d5-8577-1da5f3045096 | -19.62943 | -43.83382 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e142e414-3ba1-3c91-94bd-ff9dea39b05b | -19.62917 | -44.18741 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0a1af46-2258-3afc-811e-5cb3927cd439 | -19.62887 | -43.83751 | 2024-09-26 04:08:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de0a94e8-5815-3558-8519-7434a7dd3c04 | -19.62813 | -44.17222 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 540d2351-0fc9-3667-858b-d905f9ad2925 | -19.62773 | -43.59919 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c09ca68-8294-390f-8efd-6092ef0dd8ed | -19.627 | -44.17953 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edcaa2b2-7420-3bbd-a8db-2a50b0a83165 | -19.62642 | -44.18318 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b1e4b71-da93-3a39-a33a-bb4e608e454f | -19.62379 | -44.15644 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15703815-2aab-3ad6-91da-415dc0d9f979 | -19.62369 | -44.17896 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b43775a-dcdb-335c-af15-c655135cf96b | -19.62312 | -44.1826 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f60b57a-b8a2-33f4-badc-f0f60edd9471 | -19.62265 | -44.16376 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37dd933d-a4af-3645-a7c9-840c5682316a | -19.62255 | -44.18625 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0d03a94-e601-3921-8fc5-2d99c73f915b | -19.62208 | -44.16742 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3e0a378-962e-30a1-b49c-ec18af9a080f | -19.62048 | -44.15587 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c92788ab-c149-369c-9a6c-2bd24a25f874 | -19.62038 | -44.17837 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 929073c4-d432-3798-a00e-67e259c091bd | -19.61934 | -44.16318 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe2f81f3-eb08-3d35-be4f-49d70a73c5f1 | -19.61877 | -44.16684 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad05a4a3-5a9a-3282-8e6c-47a0367eaf79 | -19.61773 | -43.59755 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da6a4e1-cd93-3ba3-95dc-a0385788ead1 | -19.61763 | -44.17414 | 2024-09-26 04:08:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73e9853b-8942-3372-b71d-5409453cff75 | -19.61717 | -43.60122 | 2024-09-26 04:08:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
