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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b678f76-b1ec-3bd7-a756-fd8c07fff775 | -5.5372 | -43.90965 | 2024-10-20 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 193fdac0-1502-3a9f-84e7-d0f36ac1e849 | -5.2638 | -43.98787 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d0749a1-b86a-3473-89b6-8bd9ff4922d2 | -5.26325 | -43.99176 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bac2e7f3-71ba-38d6-bb59-53e91e3ee606 | -5.82973 | -44.0492 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32da48af-d085-3768-91fd-09c349d57ea8 | -5.82918 | -44.05304 | 2024-10-20 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8c3c1ff-d948-3797-861a-fd324e584cc0 | -5.46819 | -44.17483 | 2024-10-20 04:55:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5a86ea5-7213-3cba-adcd-b67003968d75 | -5.46766 | -44.17854 | 2024-10-20 04:55:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e7a58f-2615-3a51-ab8e-2b78ffd5e0db | -5.34001 | -44.70971 | 2024-10-20 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05a48951-3c11-3894-83ac-e054f4502564 | -5.33951 | -44.71306 | 2024-10-20 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f619bcd3-1090-351c-ab18-d731c7f5929c | -5.17812 | -44.04201 | 2024-10-20 04:55:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79258520-f65f-3f66-8135-53a48a0696d9 | -5.17757 | -44.04585 | 2024-10-20 04:55:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e894185-62b4-3c87-9bee-414907c027a9 | -5.13143 | -44.08881 | 2024-10-20 04:55:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c40f656-d6cf-319f-8871-169c2cca40cb | -5.13091 | -44.09256 | 2024-10-20 04:55:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc1c766-f5ce-3ebe-9435-79428a711148 | -2.98993 | -45.61354 | 2024-10-20 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e22f478-8fc9-39a3-9e24-2582118f27ef | -2.75489 | -45.36484 | 2024-10-20 04:55:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89d2b3d3-502f-3b84-a32a-87567c3d2803 | -4.75905 | -46.08294 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3873880a-7a93-3a7d-81e3-d04e32d167ac | -4.70819 | -45.96961 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2067f48-123e-385e-beb1-057afcbc10eb | -4.42338 | -45.96923 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90e88625-361b-304f-af09-04d56a49b607 | -4.42258 | -45.97477 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebba9c7f-c598-3369-b2f0-513c24e21119 | -4.4177 | -45.97417 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1101ea07-6917-3580-952d-4ea3c6acbdb9 | -4.39002 | -46.16568 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9171c6f6-4f13-3914-b522-bbe942617fb7 | -4.30135 | -45.96564 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a62b062a-eb30-3346-9d09-997db199fb87 | -4.0432 | -46.03206 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d42a235-5822-3f2b-b998-ad2d346b2336 | -4.01501 | -46.02288 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5861ca8f-3d75-3614-96c4-08a1a50765dd | -4.01416 | -46.02865 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5cfe01d-b5cf-330d-a8e3-7c44b137cf13 | -4.71111 | -45.84857 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7ef1512c-89bc-3557-9394-6a99244c2228 | -4.70703 | -45.84208 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 845f16e9-1e42-3ebe-9c11-3b23de8064a4 | -4.70621 | -45.84768 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b3de58a-7489-39e8-9f5a-f98ca56dff8a | -4.70212 | -45.84121 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a60f6b6-882b-3623-993c-b1f76a76c20f | -4.7013 | -45.84677 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2df20eb9-907a-3889-a3bb-bc9e39fb7d10 | -4.6972 | -45.8404 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 709d2713-611b-3194-b38d-c83edafc2132 | -4.6964 | -45.84585 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d25c316b-d955-3530-9df4-14a0b3368a81 | -4.68552 | -45.81686 | 2024-10-20 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29e47c74-4541-38f2-b7d7-d995219ce7ed | -4.5433 | -45.76849 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0706a97-563b-39ba-a104-fe0c63f05fc6 | -4.49538 | -44.75922 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a74aee40-3a59-3067-b6b0-108f015f3677 | -4.49492 | -44.76245 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f7d830c-d7b7-395f-b261-9cb9a0358bb2 | -4.49102 | -44.75187 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0f56f88-b5de-307d-b6ef-f4fd2f7fc7da | -4.49055 | -44.75515 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23fbf877-6e4e-3c57-859c-52b370c632a2 | -4.49009 | -44.7584 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eba31482-7fcb-323d-a7d3-92f40e0c213a | -4.48962 | -44.76168 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4489bf72-c6ec-39f7-b5d9-726d1c9a6df0 | -4.48479 | -44.7576 | 2024-10-20 04:55:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7e1d67d-0b67-3447-a39f-995c3311dc57 | -4.46363 | -45.89841 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5902cec6-4fde-3f18-b9c3-22e96ae845fd | -4.44085 | -45.70818 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 723cf43f-a372-3417-9387-297c5e5fbcdc | -4.43991 | -45.70608 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf015a96-bcf5-3a06-8e30-46f283e0073b | -4.38968 | -45.80574 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 34785fad-4187-37cb-af65-a804f9a96f49 | -4.38552 | -45.83374 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 443416d3-47a0-30bf-8f45-ecacb7f71653 | -4.38552 | -45.79984 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9a906026-6be3-314b-8dfa-7d15a8f7849d | -4.38476 | -45.80496 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2bbf2c38-0232-3a16-bc06-7933d5e5c3f6 | -4.38468 | -45.83946 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c71a6013-1b81-3ce0-a2de-c120f001be76 | -4.38065 | -45.83278 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17587eed-9c10-3121-92fa-c6eb564bce5d | -4.37979 | -45.83855 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f15a9365-9081-3a0a-ae8e-94b8674a848e | -4.37892 | -45.84442 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58da4519-3d02-3414-a131-1bd51b1f33ed | -4.37408 | -45.84328 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 396d89e6-d6e9-33a8-bdc4-1f4426c8929e | -4.33997 | -45.62593 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba2ee302-4843-36e2-a362-951809128e27 | -4.33957 | -45.62878 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48808f76-b0f9-397a-95ec-1938c9775c7b | -4.33948 | -45.626 | 2024-10-20 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc8bbb2c-45d8-39db-9fc5-c6eef1606084 | -4.19023 | -45.73439 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86a66913-8122-3b3b-b061-2ffd293f7aa9 | -4.18941 | -45.73992 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71bae758-98b0-326d-a170-8566bb204079 | -4.18858 | -45.74547 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c050190-cc78-3169-9546-138f3d61a3e9 | -4.18776 | -45.75094 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3e8adb0-803c-376a-9703-78a8460bd849 | -4.17628 | -45.82792 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 225f1918-38d9-3134-b888-5e6cff638600 | -3.91235 | -45.75161 | 2024-10-20 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45974efd-43a1-393d-b2f3-7f6172221754 | -3.7774 | -45.90696 | 2024-10-20 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb38b8a-8e41-395a-87be-3a68d47199f5 | -3.77662 | -45.91228 | 2024-10-20 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b181dfaa-2918-3b7b-a2bc-e211e5d3e177 | -4.96958 | -45.90617 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6fcc4758-28c2-3dc7-85a9-ddfaf95fb044 | -4.96883 | -45.91142 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6554fb29-f8fb-3d9c-b596-c4c9f575a31e | -4.96466 | -45.90542 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dac35b00-1485-3123-96a8-b3720b798fb3 | -4.91378 | -45.82934 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 30c92f6a-f289-330a-b2a6-eb893f192743 | -4.91295 | -45.83501 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6480c5d-0759-3203-853f-a61767a8a53b | -4.90886 | -45.82841 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9edd883f-6d57-3dc0-85de-a07b34e954c4 | -4.90804 | -45.83401 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1dbade99-5e60-39ae-9d2c-0a5457d5258e | -4.90725 | -45.83945 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 95d8260c-a339-3c1e-beb5-43cde99de841 | -4.90479 | -45.82163 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f2606aa7-4978-3dc1-a9b0-3fa68076102f | -4.90393 | -45.82751 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 455e21eb-12da-3973-8983-2290bee81da1 | -4.90312 | -45.83308 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3de96184-b77d-32b9-89cb-a50e95ce74eb | -4.90233 | -45.83851 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f17008ff-b920-33d4-b212-ed132431fdbf | -4.89978 | -45.82129 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 547cb905-097b-3a8f-84fe-2ed43ded3fa3 | -4.89894 | -45.82705 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 932bf902-8bfb-38c6-a7fb-d615f8a0b9e9 | -4.89815 | -45.8325 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04457bcb-ccbb-3701-93ea-4a7046fb699a | -4.89479 | -45.82081 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 153320d3-07fa-35e9-8904-45aa41c4d2cd | -4.89397 | -45.82647 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a8cf2c57-4d57-3d29-a25b-9929804ac434 | -4.89318 | -45.83191 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4dc138f2-500a-37d2-99a6-2d2e4f72f00e | -4.89241 | -45.83725 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6c54579-a22e-3de7-8ddf-88bfc4e67a5e | -4.88903 | -45.82561 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0601de82-ce59-3a2a-899e-b6867249fadc | -4.88822 | -45.83123 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b729fa25-3811-3bbd-a9f4-f27ff629aaf1 | -4.86792 | -45.86707 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44d852d4-6677-3760-934b-58a62f4fb390 | -4.86713 | -45.8726 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3600bb9e-a04f-3286-9858-e2f7728f06b8 | -4.86217 | -45.872 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dea69441-41ad-3b8b-b7f9-6b4cd4cbc0ac | -5.97929 | -45.36865 | 2024-10-20 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe16235f-10dc-3385-a4c1-a57973a80b96 | -5.97886 | -45.37179 | 2024-10-20 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be49bda3-bd38-3c2b-85c1-93941fc797e7 | -5.97773 | -45.3703 | 2024-10-20 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8fb4ae58-b9cc-359e-b273-b574ddc59910 | -5.21689 | -46.09741 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93d84f43-7038-3d21-b09e-a3c25b430092 | -5.21608 | -46.10292 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8582922-f2e7-321c-aea3-ae4f1baa3719 | -5.21113 | -46.10268 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0055944-50ab-31c8-ac4f-53569717c6b6 | -5.21036 | -46.1079 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84740914-9284-3d27-a1bf-15267f9386bb | -5.17437 | -46.18423 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b258341-f03a-3245-9332-f3ad489e933f | -5.17103 | -45.57344 | 2024-10-20 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e9b01ca-7d0e-35d4-ac7d-046cebab2e85 | -5.16955 | -46.1833 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f7e51c4-f386-323f-834c-cb6965388459 | -5.1365 | -46.11675 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a550aef0-97ce-3353-a078-31108113d4d6 | -5.13423 | -46.11797 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README43.md)
