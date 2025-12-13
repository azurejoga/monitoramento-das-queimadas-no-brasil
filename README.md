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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 624e1e53-3ce5-3ff5-8983-6b5feb8a6eda | -3.2009 | -41.844 | 2025-12-13 00:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 4bab039f-321f-3da5-a4b7-ea739b32db5b | -3.182 | -41.8687 | 2025-12-13 00:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 2e9bf0d1-f7b6-3cd9-a1f0-517087c906b6 | -3.2194 | -41.867 | 2025-12-13 00:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a650e198-4bb0-3ff1-8344-9983b39033df | -3.2007 | -41.8678 | 2025-12-13 00:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 160.0 |
| d836bc00-a4dc-3952-b594-7a2847680ae0 | -3.2196 | -41.8431 | 2025-12-13 00:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 63c86722-736a-3244-82dd-c5b7ea1d7106 | -3.1822 | -41.8448 | 2025-12-13 00:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 7024ad84-6d21-3f88-9872-3fd520b8e5a0 | -2.6754 | -46.8905 | 2025-12-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 21155a7e-3ecb-3821-aa00-3506a2864f1f | -12.885 | -52.5172 | 2025-12-13 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1c7e759c-9662-33d6-9d01-68d25cb1a46c | -3.1822 | -41.8448 | 2025-12-13 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 20b6f8f2-24ea-3b4d-92d0-c83cfa6228e3 | -3.182 | -41.8687 | 2025-12-13 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 198c65cf-9079-3584-bdcb-ad7f73f3d65f | -12.885 | -52.5172 | 2025-12-13 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 32148f73-993b-3c58-8472-41ba0e86226a | -3.2009 | -41.844 | 2025-12-13 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 217.6 |
| db636e61-f740-388c-af05-0d6f9dc0c6a8 | -2.6754 | -46.8905 | 2025-12-13 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| aa1a2379-ce8d-3e0c-a44d-2d311bf2845a | -3.2194 | -41.867 | 2025-12-13 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d256dd6c-358a-3e01-8692-70860e169200 | -3.2196 | -41.8431 | 2025-12-13 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 73a987f1-9739-3fa9-9452-26438bf8f64b | -3.2007 | -41.8678 | 2025-12-13 00:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| cdc209d3-0fe4-306b-89c4-8347aa50d42e | -3.2196 | -41.8431 | 2025-12-13 00:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3c64e838-fd8d-3d6f-9fac-dc4d301da0da | -12.885 | -52.5172 | 2025-12-13 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e8e22e3f-a175-3a09-ad2b-f3a84e639484 | -3.2194 | -41.867 | 2025-12-13 00:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| db4e5117-7b1a-378b-9495-5543268bea28 | -3.2007 | -41.8678 | 2025-12-13 00:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 191184c1-17f9-3144-99c7-3d3ac0039b1f | -3.1822 | -41.8448 | 2025-12-13 00:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 957b9652-3dcd-30c6-92c1-8f7f1d210c9c | -3.2009 | -41.844 | 2025-12-13 00:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 4925fb5f-d98c-3252-82f8-4c346d0ef23f | -12.885 | -52.5172 | 2025-12-13 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 854de56e-fee5-39cc-a9c1-b449f83de346 | -3.1822 | -41.8448 | 2025-12-13 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ed40bb3d-a11c-3063-abe3-37f9d800c1a0 | -3.2194 | -41.867 | 2025-12-13 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 81272183-416b-38f3-9177-fc1df1dcf425 | -3.2009 | -41.844 | 2025-12-13 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 5e3dd76f-34ea-324e-b44c-5c9475a9d448 | -9.1717 | -35.7132 | 2025-12-13 00:30:00 | GOES-19 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.3 |
| ea083a81-2878-30f0-a730-d4fda07a885d | -3.1505 | -44.4111 | 2025-12-13 00:30:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e7bbe1ce-b043-3f78-b700-9803321fd880 | -3.2196 | -41.8431 | 2025-12-13 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6560c33b-49f8-3aa5-921b-1cc224c9d99c | -9.878 | -35.999 | 2025-12-13 00:30:00 | GOES-19 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 4bd0a77c-c15e-33ee-9173-465dca44fd36 | -3.2007 | -41.8678 | 2025-12-13 00:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 893062b5-4870-3e6e-8f05-c680e5039de7 | -3.0185 | -47.079399 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 188e69cd-1cf8-32c3-abb2-45c34ab67283 | -3.1975 | -41.8456 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d55b7f9-0cb1-3568-9a72-e52165b36e4b | -2.5708 | -45.054901 | 2025-12-13 00:38:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59db8b80-6cad-37a1-8286-4dc7f31f4d0d | -3.1226 | -50.602699 | 2025-12-13 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2f6d2f1-c75b-321a-924a-e03ef658a4af | -8.3925 | -44.051399 | 2025-12-13 00:38:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89b29d5d-83ed-3b5c-9522-ce8758f98746 | -2.0901 | -45.605099 | 2025-12-13 00:38:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6aba2de3-e7a3-3842-9b9c-54cae7f67f29 | -4.027 | -49.866501 | 2025-12-13 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8e0ef2-4afc-3a64-bfd0-76bba7e9944f | -2.422 | -51.916401 | 2025-12-13 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6ea5a65-832c-3b1d-b73a-d81faa9a7db3 | -2.1809 | -46.0868 | 2025-12-13 00:38:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 343dae53-308d-3421-abed-8a5ee4dadd78 | -3.1523 | -44.409698 | 2025-12-13 00:38:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7d7e7f5-2e1d-3f48-a54d-539b43362c99 | -3.8258 | -49.706699 | 2025-12-13 00:38:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d4fa03-7d9e-32f2-81ad-d5da5d3c584f | -9.8767 | -35.983898 | 2025-12-13 00:38:00 | METOP-C | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3653efda-be57-3234-8cab-481f392b9639 | -2.664 | -46.883801 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7422274-82e6-3ab9-b697-8a026bab8d59 | -1.8919 | -54.338402 | 2025-12-13 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5feebf-f27f-3795-9d89-1f2794d1f2f1 | -3.3775 | -52.596001 | 2025-12-13 00:38:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48300f2c-b74a-387f-8817-80221358afa3 | -2.497 | -51.793201 | 2025-12-13 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe42af21-aad5-3d06-8ec5-e21727bcd544 | -12.8764 | -52.505001 | 2025-12-13 00:38:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29a69544-b023-329e-ac9a-eb049e37b1a9 | -3.1877 | -41.847801 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbe96627-051d-3b11-bb70-78a7550bf764 | -3.0218 | -47.093498 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5946d6-99e3-3db6-88ca-c9cfb8623700 | -4.4796 | -44.882198 | 2025-12-13 00:38:00 | METOP-C | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fafd19e-d4c6-3016-9ebc-1517e2ef21da | -2.5411 | -45.193802 | 2025-12-13 00:38:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d26054f9-2fed-32b0-bd98-9aeed055bdef | -8.0398 | -43.0882 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee505cee-5b41-3e8b-b1fe-6be5e5ea2f41 | -3.4282 | -52.9133 | 2025-12-13 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae9878a-372a-3ba4-b64b-702f9a9284a9 | -3.645 | -49.5005 | 2025-12-13 00:38:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc33d4a-ed8e-3ea7-aae6-516814699a68 | -8.0443 | -43.106701 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e249a50-f2ac-3f1f-821c-679f4e2af861 | -3.1209 | -50.5951 | 2025-12-13 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcfda1ed-4032-3a9a-abb8-4eee2b157659 | -4.1837 | -47.840302 | 2025-12-13 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01cb4a4f-5ae8-3243-a001-b830a9d05f6c | -2.4989 | -51.801601 | 2025-12-13 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb94e7c7-fd94-301b-b33b-3192c6d4498a | -1.7933 | -46.061001 | 2025-12-13 00:38:00 | METOP-C | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| daa06179-975d-3984-9191-dab3abaefdbf | -2.5806 | -45.0527 | 2025-12-13 00:38:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85733bde-f9bd-3716-be42-675645492d9d | -8.3827 | -44.053699 | 2025-12-13 00:38:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71ae21fd-aef5-3092-a821-a149e72aacfc | -2.5392 | -45.185501 | 2025-12-13 00:38:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 310ff44e-ae16-3ae8-813f-2c397f4ec046 | -2.6673 | -46.898102 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71175b13-dc8f-341d-ac89-3450b97c357f | -8.4102 | -44.038502 | 2025-12-13 00:38:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40d9b11d-571e-34e1-a41f-bd690cc74472 | -3.2041 | -41.830299 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b907d73-8def-3aa5-8d43-c0d715c9f505 | -8.0323 | -43.0998 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb9bf488-8a25-30ed-968a-1dbc0b31b0c6 | -3.4795 | -43.826199 | 2025-12-13 00:38:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1087a83-0fb8-3661-a80e-49bb5f77aa8a | -2.9461 | -52.5513 | 2025-12-13 00:38:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f61d2400-b7a2-3052-a4ab-184f68602038 | -3.3032 | -43.514198 | 2025-12-13 00:38:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38d27f5d-f592-3c57-9d70-6e5890de16f3 | -3.2006 | -41.858501 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eca46a7b-7e5b-3c18-bcb2-0952c2b2ad81 | -23.3381 | -45.421902 | 2025-12-13 00:38:00 | METOP-C | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc30cd70-894b-3e8b-b0e4-4501c5f8573f | -1.8893 | -54.326698 | 2025-12-13 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9877785-f1de-313d-818a-e8d45d19fbbe | -3.4206 | -52.925499 | 2025-12-13 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea1933d5-fd9e-3e0c-a1f5-f220b8c22263 | -2.0112 | -46.3792 | 2025-12-13 00:38:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8afa417f-6356-3e0a-80f7-9254a639b461 | -2.1826 | -46.094398 | 2025-12-13 00:38:00 | METOP-C | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc88a23-aeb1-30d7-a900-7677d660ec57 | -2.6656 | -46.890999 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b56d3dc8-f46f-31f0-a25b-e1083ea0cbcb | -1.7728 | -46.106098 | 2025-12-13 00:38:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09f8db5c-c8c4-3762-b532-36f2fed525dd | -3.2434 | -47.249298 | 2025-12-13 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e65bcfc-0227-305a-901a-c0d03716d6da | -4.2069 | -44.2901 | 2025-12-13 00:38:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f39660ba-cd3b-3c43-9366-ff81e5f58024 | -2.0039 | -45.410999 | 2025-12-13 00:38:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| edef9e3c-5756-38fa-a112-313c98dd3042 | -3.0497 | -48.473202 | 2025-12-13 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8d8ae1-b700-3485-aacc-4e6a76262055 | -1.9056 | -45.476299 | 2025-12-13 00:38:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9294b37a-61b2-3ad6-9253-cb4e8e4da6c9 | -8.03 | -43.0905 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e501691b-34e5-350e-8bfd-84a3a7da3bd5 | -8.0345 | -43.109001 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 80457fd6-c0bc-3206-9517-22551ad23e56 | -8.0225 | -43.1021 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f2960fb-ebbf-3292-83f0-e243dd7414e3 | -3.4773 | -43.816502 | 2025-12-13 00:38:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4b717d0-6041-3c4e-9071-8727194076ec | -8.0465 | -43.116001 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5cca198a-ec9a-3141-8597-0dea23a118e9 | -2.4239 | -51.9249 | 2025-12-13 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde70a6d-8986-3e9e-b56c-c6a63e785cb8 | -3.1944 | -41.8326 | 2025-12-13 00:38:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67b9ccb0-665f-325c-bde6-700709d05450 | -1.9037 | -45.468102 | 2025-12-13 00:38:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6bcbc95-7691-3ef3-b065-9ef50a22ca4c | -8.054 | -43.104301 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1168a1ed-994c-378f-b860-0dc9f25c0152 | -2.3657 | -45.726799 | 2025-12-13 00:38:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a395225-f242-3830-bd0d-a6f42a57629e | -1.8991 | -54.3246 | 2025-12-13 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f602e704-6c7b-3df2-9e56-51cf665d7c01 | -1.5653 | -45.8325 | 2025-12-13 00:38:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73badd11-3b29-3852-8ca9-6fd0a0c91e17 | -8.0421 | -43.0975 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 12c01afd-6ad4-3891-8593-0140dcd5f119 | -3.4184 | -52.915501 | 2025-12-13 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae9b110b-749f-3366-ab07-5dc4e3b436db | -12.2764 | -38.412498 | 2025-12-13 00:38:00 | METOP-C | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 60aa2480-ef5b-336f-a052-2b1dc9a769f9 | -2.5383 | -45.359001 | 2025-12-13 00:38:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1e34db-98c8-3e68-b78c-e5cc65169403 | -8.0518 | -43.0951 | 2025-12-13 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
