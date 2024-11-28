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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65908701-8e0e-3821-96cc-69e60498d454 | -3.2052 | -46.5896 | 2024-11-28 00:38:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8260e61-68d6-343e-9854-6e94ce473a7a | -4.7888 | -44.435501 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d359fa8b-c14d-35d8-a0d2-f10630a69229 | -3.3919 | -50.111099 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1238a5e-0c36-3791-af12-b69767287f8e | -3.1895 | -54.3139 | 2024-11-28 00:38:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d29b516a-5bf2-3205-bfc6-6965337ca1b9 | -3.7313 | -52.0084 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f537f967-4eff-3801-ba33-d058b9f1a8d9 | -2.5809 | -46.0261 | 2024-11-28 00:38:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e83e1738-63f5-30e4-877a-17dbe2b45b1d | -2.6651 | -49.501701 | 2024-11-28 00:38:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c502984-aac5-34af-9b63-ec069eff9b91 | -3.3415 | -50.071201 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4657b119-7369-338f-9b1e-acffe9d88149 | -3.1048 | -54.120499 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e33120-8c4b-33e1-add3-03015916ddbf | -2.611 | -54.215 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673c475b-27e1-331c-ac44-c61a6083eeac | -2.609 | -54.251801 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf82900-9250-34de-a68f-ee2c01a5b6f6 | -3.0798 | -49.200001 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7941c73c-223a-32a6-9fdf-3bd330b03991 | -3.6678 | -45.804699 | 2024-11-28 00:38:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92f7633a-bbbb-308d-9c0c-ca0437b0a161 | -2.5949 | -54.051701 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce2d9256-7d98-3d9b-a384-05b60de64473 | -2.9371 | -49.430801 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 558fcb68-a812-3aaf-94d3-078e985e7f85 | -3.9703 | -46.960899 | 2024-11-28 00:38:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57e0d72c-1818-35b0-bd61-25eb431d5181 | -3.8512 | -50.091999 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfac4d24-741b-3cec-9c8d-3dcd3b305b33 | -2.6395 | -54.296101 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3306b789-dcf2-34f9-a53e-7e4e912c1254 | -2.8697 | -53.991001 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f81422-678c-3dc6-9e61-d7a37eb7879b | -2.6094 | -54.208 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f0da35d-f7d0-37b8-b538-eb7aac890bb1 | -3.1028 | -54.019299 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59573c2e-848d-30dd-a8b1-118e137d3094 | -18.695101 | -48.967499 | 2024-11-28 00:38:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b3e95a82-4dac-3cf7-a9ca-861ab9d1e3af | -2.9116 | -54.1777 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c759ac9-24b9-36c3-9faa-d94ad7b894d8 | -2.7061 | -51.987301 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01c25c87-e297-3457-8533-00f0a1408fcd | -2.8764 | -53.974998 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83414200-5cda-3cc3-9780-42d02a3c0c76 | -4.7791 | -44.437801 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ec72ac1-c6dc-3f74-ad25-265b0512c981 | -4.1831 | -48.625401 | 2024-11-28 00:38:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b270e94d-a200-34fc-8bb1-de7fa84c6063 | -2.319 | -51.962399 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f56b8287-dead-37f2-b494-e9b3ec044de8 | -3.0635 | -54.027901 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51dc7bc3-b279-358f-840e-0e2f61acd558 | -3.0663 | -53.673698 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ded9ddf-e7d2-34c1-b0c5-44b50b5b14ea | -2.596 | -53.964802 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 289491e9-be0d-3c17-8b01-4ad948a81044 | -4.1318 | -46.117401 | 2024-11-28 00:38:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 537e9a40-f9c9-36c9-b2e4-8ef43d516dcc | -3.6905 | -49.571201 | 2024-11-28 00:38:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60feb3b7-0aef-3e14-b97f-d6f8c26d274d | -3.2571 | -48.896801 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459b99fa-1522-32de-a54f-62f01e1745d3 | -3.0938 | -49.216 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30bcbad4-9e9e-34ac-9adb-ede5357ca8b6 | -3.7864 | -50.123501 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e57d339-acb9-3405-8f01-8a95d266f015 | -20.3419 | -48.818199 | 2024-11-28 00:38:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 26d29511-bbbc-3f8d-af1c-fd83b046cf21 | -2.6059 | -46.838501 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac14386-7185-35f4-bd34-6739d20b4572 | -1.5367 | -46.076199 | 2024-11-28 00:38:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1f4ad83-22b9-38e2-a3c5-c330c3d79326 | -2.8139 | -54.0177 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9627d537-4e01-3e17-926e-88464bb5a6be | -2.7628 | -54.065201 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7994a1-32af-3600-9145-c4d6fd142447 | -3.0833 | -50.2486 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d892eddd-1bcc-3c17-8b51-1fcfdd1e98f8 | -2.8609 | -46.875099 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b4d5cfe-ee91-3c31-b6fd-eeee91242d17 | -3.9134 | -47.201099 | 2024-11-28 00:38:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 275b7849-23d8-3a76-8233-483e11411156 | -2.7431 | -51.6507 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd657f1-0fd5-3294-9dd6-a8ca99a8195b | -2.2567 | -53.602001 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 921f3679-49c1-3f9b-8924-f54957724fba | -3.9277 | -53.655998 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae175909-2ccc-306e-ab65-101c65d65806 | -2.7529 | -54.067402 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc851e97-892b-39a2-bb1c-41f8b5c08696 | -2.5739 | -54.3251 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aefdd48-0ec4-3986-aaf4-892c8bc9add0 | -2.1882 | -53.252701 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88d30a4-3133-3cf8-9af2-03ee877f203d | -2.9212 | -51.708599 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ec2812-9938-333c-924c-f94b723bada1 | -2.8362 | -54.070801 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a45ba2a-5dca-305c-adb3-e1534515205e | -2.9444 | -54.323898 | 2024-11-28 00:38:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e03ee011-5816-3474-a481-13253c359f60 | -3.1182 | -53.813301 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5687420d-6b71-36c9-bd44-bc67da666f2e | -2.6358 | -54.187698 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbc46a5a-f279-3d55-a27d-8aeb46403354 | -3.4069 | -54.273399 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c8f4ab1-85b9-3f83-8a12-3bc66882c0bb | -4.2373 | -50.879002 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c0c025-ca53-38d3-be20-178b951a47bf | -2.551 | -54.0397 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37de604b-083d-38de-ac96-8839d58ed9de | -4.6675 | -49.517899 | 2024-11-28 00:38:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 836a715d-94f5-3f46-89b6-0b0c0f92bca2 | -2.25 | -53.617802 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05adb0dd-2b05-3144-aa64-0b72ba5d10be | -4.7833 | -44.455299 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6107d3f2-a857-3946-8600-b0573eb38e10 | -3.7179 | -51.812901 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f13afd-a310-386a-9573-5c110152b13a | -5.9813 | -45.3801 | 2024-11-28 00:38:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd200de-9c09-308c-ae61-b6f7855fa3e7 | -4.4806 | -46.3759 | 2024-11-28 00:38:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 537e5dfb-0eb1-3427-8725-872c3ded6746 | -3.6644 | -45.789902 | 2024-11-28 00:38:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87fae079-c0d0-33f2-bbf8-8ac2fcb8d60a | -2.7829 | -54.0173 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 978e74c7-7eec-30db-94bc-68e4cd70f2a0 | -2.9101 | -54.1707 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01032d5f-7cad-3369-8da7-77f55e5197e5 | -3.3453 | -53.5401 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6ef9d3-e292-3a6e-b721-41145224db99 | -20.3403 | -48.810902 | 2024-11-28 00:38:00 | METOP-B | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 59452e08-8fb9-3874-a489-d7c79bdeb846 | -3.6995 | -51.368599 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df1f9502-254e-38cf-a360-4059d1ced327 | -3.0423 | -54.025299 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d94e5bb-1847-3065-81a3-d14ccb8ff2af | -3.4978 | -50.078602 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8bd912d-0b07-38a9-b6db-3d37a4a98f1b | -3.3327 | -45.514801 | 2024-11-28 00:38:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cddb06c8-8e29-3015-8bc7-2d6f70a465bb | -2.0556 | -51.164799 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8ba1c2-b097-3d09-afac-f5a15c3d4926 | -2.8471 | -54.119202 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad2fb76-d483-35e4-834a-d6cd1ab89ab2 | -3.6414 | -47.3134 | 2024-11-28 00:38:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43f91170-dba9-3da8-85e6-16b802489bd8 | -2.3228 | -48.146599 | 2024-11-28 00:38:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e6ac97-0451-3d9b-8ecc-034c4e1242ef | -2.749 | -48.6572 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a34e5d45-8fdf-3697-bddb-1c26931ecbda | -2.6089 | -53.976299 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be79d54b-8c8e-3c13-adfe-75d85d33b41d | -2.8909 | -53.9935 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b0dfd6-500a-308d-bb58-8605556efa92 | -3.3805 | -50.828098 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adedee1d-499e-357f-be36-67baa0482d1f | -2.1662 | -53.4291 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd0aa19-a619-3558-882f-2f00ea2d452a | -5.0953 | -45.8465 | 2024-11-28 00:38:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 541f314b-134d-310e-84b8-b92c0ac8ef57 | -2.8473 | -51.837101 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74bbbe3a-8eb5-3071-a7ff-ab2e527ea294 | -2.9674 | -53.8755 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9050bb5a-8fb8-3781-86f8-0c15e37de25c | -4.4202 | -50.822102 | 2024-11-28 00:38:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c650cad-041d-3817-8758-de498e51fa81 | -3.1089 | -50.360401 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a4b6796-e634-3d5d-802d-68d97d025c87 | -2.5862 | -53.966999 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72ba1151-df1c-3129-9ae6-c6fa58580ebf | -2.8456 | -51.830002 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569686de-ddd0-33e8-87a9-cb9611cc8ee7 | -2.816 | -53.020599 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1f24ba9-5b0a-3709-82b8-b192af1ea5c5 | -2.5484 | -53.982498 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca2f4961-f519-3ae9-b4a6-74c627fef7d4 | -3.39 | -50.103001 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e743c563-37b9-3577-95d2-f7fe6a17e5a5 | -3.2614 | -50.6222 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0305969c-9fec-3a9f-800b-c32a486c801e | -2.7298 | -48.8867 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f55e754-78b0-349d-8ac8-9f4bfc489825 | -2.9215 | -54.175598 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9e43dbb-8291-3618-b0ea-82e0a4766317 | -2.8413 | -54.047901 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1274bc-51d9-33d5-be11-b70f49cb47c8 | -3.0715 | -51.055199 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7876e4a-9971-3592-8832-48ad3310493c | -2.6285 | -53.972 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9138f60d-7452-3ec7-8aa0-36f4d96b1a47 | -2.3565 | -54.365799 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96727a71-b21a-3a01-af5f-5ce08223178b | -2.442 | -50.418301 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
