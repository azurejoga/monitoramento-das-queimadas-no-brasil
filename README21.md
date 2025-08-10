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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 179d0b88-6c0c-36fa-825b-28a36b78b2ec | -6.95412 | -44.55352 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 858e7efd-9564-3f44-8d08-ffb0522abaec | -6.63876 | -55.26389 | 2025-08-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15b87d4c-fd71-3172-ad76-016469375c8d | -5.28066 | -56.01981 | 2025-08-10 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea5e448e-ec85-38cf-89af-52a3f77b1e53 | -8.24819 | -45.83593 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a19807d-85be-327e-9979-fe3b8877d56d | -7.15824 | -44.06247 | 2025-08-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5ccab6e8-8079-3e35-95b6-c316bbf49eab | -7.88602 | -45.56047 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c71ac83-0bba-309c-a959-12e05e0053bf | -6.13652 | -42.96099 | 2025-08-10 04:44:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d9f5daea-e4f8-3da1-aab6-8f305168a6a5 | -5.47007 | -44.70224 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 066080fb-0a62-31ad-9f57-4368ad886803 | -3.83543 | -47.74956 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ac65a82-d4a1-3ea4-9d84-3123ae6d0552 | -3.23496 | -46.79519 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84dec67b-458b-3253-b025-9b3429fb28f2 | -3.43022 | -49.04699 | 2025-08-10 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1b4581cb-5125-3a80-bf58-618a68728dbb | -3.59204 | -47.52639 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16206770-d979-33cc-b3ae-39cb14e87249 | -4.35034 | -47.53606 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 09d1acd5-2450-35ee-bec1-21df5c17070f | -7.02957 | -43.55081 | 2025-08-10 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79f5cc32-7ca1-384f-bf14-62c610a6361d | -2.22232 | -50.46367 | 2025-08-10 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3f8fecf0-b6ea-3017-92d3-a4a7a6196c8f | -4.3497 | -47.54017 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6495024d-5bae-31bd-93e9-7d390786e753 | -2.58496 | -51.92293 | 2025-08-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45434c37-0c74-3e7f-ae9a-e085ec41d305 | -3.22392 | -49.34267 | 2025-08-10 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3e89937-d8b5-3be1-87a5-a354a00aa936 | -3.37076 | -47.64188 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2497f24-8aeb-3cc3-b1ff-2b0d623f093b | -6.97821 | -44.80233 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae49db38-74c1-328f-b5ec-6d59978413f5 | -6.05911 | -43.74458 | 2025-08-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a577c139-c88f-32ca-ba61-25c8e82d56ea | -7.41169 | -43.99367 | 2025-08-10 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e092e21-6b91-35af-8701-c36c9d55eb77 | -3.6238 | -47.52517 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79606e12-8128-3356-a620-47cecb4f9db9 | -4.29374 | -48.27295 | 2025-08-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e87bf13d-1876-3bf5-9e41-6e5d987277fe | -3.22726 | -49.34317 | 2025-08-10 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27cc4f8b-72c5-3180-b8c7-1c3c8e6d94f6 | -5.20569 | -45.61955 | 2025-08-10 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3456ff14-51ba-3d53-a09c-f29ff8a3df48 | -4.34783 | -47.53894 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 77f62267-fca6-374d-bb52-05778d92582c | -6.95273 | -44.5503 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 21ca3203-845a-3268-bd3e-49effcd962ed | -7.58826 | -44.39898 | 2025-08-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 966cf8b5-ebd4-35a6-a3da-85529ff9d39d | -3.62442 | -47.52114 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e35ce58-4010-3522-a9c1-c50d7b4a869f | -7.70315 | -45.54504 | 2025-08-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6c86813-b5af-300d-a46a-a852ec750364 | -6.67859 | -44.73188 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b90907d8-1755-3f0f-854a-59478d281191 | -7.87841 | -45.5601 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e23ef80b-5bdd-36bd-8c9f-4b9174595a0b | -2.43888 | -47.32796 | 2025-08-10 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e9f2de7-5117-3170-853b-14eb418c461f | -3.9677 | -47.87721 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14c41cb2-8691-369b-a8fb-d68e4fa7e32d | -5.66734 | -51.36741 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed52f145-a4ff-3153-8d19-519de1eec284 | -6.52805 | -47.43281 | 2025-08-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae3fb149-6b5c-30e7-a74e-e51a6b481154 | -4.54421 | -48.00988 | 2025-08-10 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bab5f578-0028-3e7e-808a-646bee249984 | -7.88328 | -45.55664 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4478483-db5c-37fc-a771-a48e061780ad | -5.47882 | -44.70347 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecc790fe-c404-33fb-80c9-c692901f8a2f | -5.38548 | -41.32663 | 2025-08-10 04:44:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a618a98c-54a3-3370-a979-0bc22bb2812e | -6.94832 | -44.56208 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a821f484-c565-38e4-9e43-aadcdf580d9c | -6.1906 | -45.44233 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5e9300b-283d-3651-bba6-b6dc4ab30d41 | -8.11305 | -47.44148 | 2025-08-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acfeae68-ee75-3fc8-9683-34b36fa37225 | -6.21301 | -41.40432 | 2025-08-10 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d948a30c-019d-3c2d-b798-e9f6ee63617d | -7.42724 | -43.98598 | 2025-08-10 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 87202c56-3e83-3e78-8310-7e9f240857c9 | -1.93769 | -48.79636 | 2025-08-10 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a035d769-2843-3929-8ef2-2e544313336a | -3.18844 | -41.85694 | 2025-08-10 04:44:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c879558-bdc0-3ffe-ae1e-b492a186df10 | -4.29912 | -48.07534 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7b345a6-6549-332f-9634-2135bdd8c451 | -3.22781 | -49.33965 | 2025-08-10 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74d031a6-af85-32b4-b941-992c3928b464 | -7.13949 | -41.49176 | 2025-08-10 04:44:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d054b597-d43e-346f-b9c1-9e014db6f082 | -5.05373 | -38.13444 | 2025-08-10 04:44:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 47026dc5-adec-3908-8ab0-df070e9cd6d2 | -3.64824 | -48.32556 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f435ca7-77b8-3180-bdd5-c3d677063240 | -2.36988 | -51.90799 | 2025-08-10 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7ef2a557-1561-3d48-923b-4afdc944280f | -8.50879 | -45.70619 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88db50da-f707-370d-b30a-62ead5836b45 | -6.98203 | -44.80725 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cafa6b8-824c-30da-9f34-11e93e9c3121 | -4.11097 | -38.17925 | 2025-08-10 04:44:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f4d01d0d-3d2b-31c2-b9b1-785b94e46b1d | -7.87535 | -45.55127 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 275a74dc-660b-38de-9a27-bc86c0c4000d | -4.1096 | -38.17411 | 2025-08-10 04:44:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 64814230-5210-37ed-82d8-9965c3ff4dc9 | -8.37305 | -46.9823 | 2025-08-10 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67665dd6-9590-3a4d-bfe0-2fd8865461af | -3.21678 | -46.81485 | 2025-08-10 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69f64f89-789b-3159-9fc3-2661d9c3bc1d | -6.57648 | -44.56829 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b1389c4-aec3-3916-8064-fbe6a32d1707 | -5.05739 | -38.13285 | 2025-08-10 04:44:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc91ca70-66f3-3eef-9e53-af2ccb602225 | -7.73056 | -45.53603 | 2025-08-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0857a757-319e-3ded-9869-c7a672070d32 | -7.39708 | -39.67967 | 2025-08-10 04:44:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 52d97e10-de2f-3369-8fc4-8669fb43ce8b | -7.88875 | -43.54726 | 2025-08-10 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ef1167d1-60d2-386a-b22f-353dd26d01d3 | -4.9546 | -47.59912 | 2025-08-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1c9743c-8700-34d8-82a0-11f273853944 | -14.03287 | -46.34058 | 2025-08-10 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30d593f4-67d3-3b45-b5a3-4412c7794fe7 | -12.55887 | -47.08385 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b2baf87-62a1-3155-932a-6df8ce0a044e | -8.92199 | -60.75381 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e15fb3ac-d3b8-349d-8f70-f27705729ccb | -14.11038 | -45.40047 | 2025-08-10 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3322485a-7927-3555-88fa-08c9657486cf | -13.63024 | -49.00251 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4dcd4da-3a49-3c20-a81d-38937a3162ad | -7.07555 | -59.16671 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6abb5e24-9a1b-3b42-bc06-debdfa464aa5 | -9.49133 | -46.28305 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 528b1e3b-26a0-3dc3-a0b1-a9a6975c8246 | -7.08246 | -59.18467 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8383b647-ad4d-3c5e-9e64-32603eb36e4f | -9.93609 | -60.50832 | 2025-08-10 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a929993-c459-3b9c-85cb-93f86aba9f86 | -7.39379 | -59.99593 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9149280-29d6-349e-9f8a-446b99a1501b | -8.06762 | -49.71257 | 2025-08-10 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26666a3d-393d-33f5-8014-69160aca1ea2 | -8.56542 | -54.68098 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e64a1ca0-0c4f-3fc4-b74e-ee9c9123951d | -14.29809 | -51.98455 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 039775e2-bd3d-38d9-95eb-e3313a133743 | -7.06483 | -59.17057 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcb76a03-d85f-3472-b9aa-fff14b79a6ed | -13.61555 | -46.94384 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35ad59a7-5310-3215-850e-dae36997f7b5 | -7.08637 | -59.19111 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e64480c-0c97-3c64-8e17-c8f44cbcbf0d | -13.59866 | -46.94131 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9895091c-ab7f-3c2c-b41c-694f2b73ee24 | -7.39839 | -59.99983 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86fee1a9-b8d8-3491-aaf9-d692b2418165 | -8.88095 | -44.78567 | 2025-08-10 04:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 42ad8058-28d6-3706-924d-f1ee8a50e097 | -9.5536 | -62.7169 | 2025-08-10 04:46:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b52c2676-517a-37d0-9704-1cb0a36cacaa | -11.776 | -44.95426 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f27e703-c73d-3795-97c0-d4e1e025d0b5 | -13.63225 | -48.98855 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65225247-a690-3853-9744-343c85a026b8 | -14.70033 | -48.56443 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87d83d97-1e1f-342c-b38c-fee232a686e3 | -9.37517 | -61.52478 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a2180d33-d8a5-36f6-96c2-e22bc2898882 | -7.06597 | -59.19276 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da7e036e-f115-3465-bee0-9d7e364309c1 | -11.33764 | -51.4428 | 2025-08-10 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea827b49-2ea7-33cc-81f4-7462fb2b9c3f | -12.53131 | -45.67267 | 2025-08-10 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67ab70ea-9fec-33b5-9d25-e3345045528e | -8.93369 | -60.74921 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4435aec7-3d62-3384-9fb1-a5c86c2170f4 | -9.7136 | -61.29622 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5921e3e-7d19-36ff-9dab-cb6695cd5177 | -9.49743 | -46.29963 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1741881-8649-3ea7-8fae-d8dcb1c58c49 | -14.12073 | -42.14435 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 40185b1f-8f78-3f23-9c82-61c9dfc9b71f | -7.06793 | -59.2103 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27984ca2-3d9c-3be2-a0f8-d18bee26f2cd | -9.49189 | -46.27918 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |


[Clique aqui para ver as próximas entradas](README22.md)
