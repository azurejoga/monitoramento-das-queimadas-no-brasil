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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3675292-6db0-37a5-8764-297d4a9e5f7b | -8.3842 | -48.28463 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8db39e41-47eb-3d02-af65-dc178f5c805f | -6.69969 | -48.4009 | 2025-09-03 03:53:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30ec021e-333e-3ff0-afb3-5a3c0f256297 | -6.70043 | -48.39677 | 2025-09-03 03:53:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ad1bee-843b-3158-bdb1-339aa49f057a | -7.48173 | -44.81351 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e648963-7e72-3e49-aa94-7d63ac5a3b11 | -7.48236 | -44.83537 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ce4aad9-f640-3472-839f-58e322ffa2c0 | -6.46129 | -44.67578 | 2025-09-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f7a6acc-e5d4-3fd1-a722-68e547ed1d6b | -6.16355 | -46.60302 | 2025-09-03 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65fa3901-f915-339b-9918-a9cd2f3e3e24 | -8.88246 | -45.82082 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05b9c63f-b722-3fb9-88c3-cbbcc4fb99e2 | -7.90849 | -46.45726 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 965ee031-f3c3-3191-b523-adeb9323e5a8 | -7.40584 | -44.01554 | 2025-09-03 03:53:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 195df23e-cf02-30da-a100-4ba11c7a659d | -5.8059 | -43.22715 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5a6d59f-ebd5-3cdd-95d1-5c5730f0cd75 | -6.89726 | -45.56422 | 2025-09-03 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e7c1702-a9ae-3023-88f1-c06065c6c43e | -6.12483 | -44.23463 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1558fe5a-73c8-319b-9779-9bbb01fba018 | -6.51087 | -42.19346 | 2025-09-03 03:53:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a1d70c7-3585-3d34-b792-de83cf8c047b | -7.00587 | -43.43816 | 2025-09-03 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a982ff11-0c54-3215-9954-77ebb0df6b19 | -7.10922 | -44.31319 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63a339aa-1bff-319a-aef2-e83a02558af9 | -8.88413 | -45.81137 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c29ccb4c-a134-393e-9ebb-4a122e5661ce | -6.12116 | -44.12696 | 2025-09-03 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64870089-7129-39ce-ab68-553f5eb4d67b | -8.88163 | -45.82554 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec53c88d-da31-34a1-90f2-a99ed191201e | -6.9949 | -43.2621 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3070f549-610c-3589-a1c5-26e9c5b2e205 | -7.89681 | -46.43908 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7a95fed-5de5-3d78-8fa7-66ead10b435a | -7.90374 | -46.48426 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96823087-e9dc-3c6a-bcd6-d6e034040dd1 | -7.91886 | -46.42656 | 2025-09-03 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 007267dc-3d64-36f0-8b96-b6431c879bb7 | -6.09886 | -43.29128 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dc96d8f0-4bce-3548-8eeb-101a6aa2e528 | -8.04906 | -45.36488 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 217484f5-96ee-34b6-aac0-85c73db41bf9 | -6.45795 | -49.53085 | 2025-09-03 03:53:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9860eecc-225c-358c-8692-5701b3230c64 | -6.34852 | -45.66624 | 2025-09-03 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9886da60-365e-3376-9d93-d3223be31b04 | -8.01617 | -44.10584 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81d9f157-a8be-3a91-aea1-a393a94f90e5 | -8.37427 | -48.30785 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06975a98-c36d-39a7-8da4-da03d2310ad9 | -8.01964 | -44.11031 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24599534-b53d-39f7-a261-0f584a120751 | -6.17519 | -43.31165 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 93422206-54f8-36c3-8c91-75785625e1cd | -6.99972 | -43.25768 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3765c473-b651-33d5-89ef-88297718a5df | -6.27771 | -43.5986 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfc840d4-03d2-3f74-9fa7-b26754db7ddd | -5.80416 | -43.2374 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 143e3444-49f5-3a9e-b99b-142f684b4b17 | -6.99712 | -43.25486 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bb6c19a5-994c-33b4-821b-3dead8c54666 | -6.69109 | -43.49588 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbf25317-cd8e-3456-959e-141d1472babc | -7.00273 | -43.24533 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 622026d2-7c91-39cb-98a7-fdaaf46569dd | -7.80107 | -45.45303 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0584d276-a52f-3eb3-868b-d3a9d506a587 | -7.64771 | -39.01961 | 2025-09-03 03:53:00 | NOAA-20 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 85c373bf-1090-3f7f-b7c1-d91953d185de | -8.06675 | -45.36889 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b727c27-49d4-3866-8897-e7603cab1ef9 | -6.24596 | -42.62308 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 188ec628-a5d7-32f3-8f72-a5d05716d234 | -8.36594 | -48.31398 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9f38058-af77-32ae-b6c4-9ab157a034d7 | -8.37803 | -48.30888 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c804d47f-3b65-3839-9b44-6f4df92cd9f0 | -6.45878 | -49.5261 | 2025-09-03 03:53:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50ff43f0-d73a-3ae3-9e86-0a29620a8dcd | -8.36246 | -48.30226 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a436f8c8-3202-3f0a-bba3-532dfe061651 | -9.24342 | -44.49783 | 2025-09-03 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3e07824-32bb-3a1f-b772-f094b9390785 | -7.69874 | -48.7367 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| eb2f9cf5-6c8e-35fe-b11a-4ccb4cef8a15 | -7.89692 | -46.46651 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 653c9c48-d5ad-36b2-b199-ab42c0df04af | -7.49606 | -45.33572 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 068e7793-d13e-3ecc-b4b7-889c0a1a90b2 | -6.17004 | -43.31782 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 98dcaefc-f7c0-396d-a641-1ae94d98ed6c | -6.19698 | -43.35464 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 252da2ec-1b5e-3f9c-aa5a-f76547a0ebc3 | -8.54947 | -47.47925 | 2025-09-03 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b6efa7a-92d0-3b33-9cbd-a73bb11c8345 | -6.80091 | -44.64468 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ee3c77c-d782-343b-aabe-391ee78f2239 | -6.6402 | -44.26432 | 2025-09-03 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66d4b391-b12f-35e3-9b69-cd3a1db350ee | -6.51302 | -43.0917 | 2025-09-03 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5163a4cc-71fb-3ec9-8fe7-a1eb57b7446d | -6.26148 | -42.60106 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e0e2793-1aeb-3e7e-9e0f-1f2a4819783b | -7.01009 | -43.53561 | 2025-09-03 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf1b2d62-9202-3cc1-85ec-ef9cb82d674b | -6.96996 | -44.36615 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a011add-8137-3c41-812a-0d356a2a18c5 | -6.27557 | -43.31046 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9ce208d-e3f0-3aae-a316-f938e0146484 | -6.97915 | -44.36348 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36f697f1-908e-39c9-b580-4ca488ccbaf4 | -6.27497 | -42.6623 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b1a1959-293e-3a0b-aae1-e99281c47592 | -6.30438 | -43.5624 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63155193-800c-305a-a96a-06be679b154b | -6.80164 | -44.64041 | 2025-09-03 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c1aca5d-f53a-3c63-a448-db334904407d | -6.97458 | -43.2931 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1af557a8-5228-3646-ad0d-77373c6fe176 | -7.50561 | -45.34536 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84da77d4-1503-335d-b3a3-cb4858778fc0 | -6.26684 | -43.51237 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 853a051c-a655-3839-adf3-8817bb7b167f | -8.88613 | -45.82658 | 2025-09-03 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56db4cf7-fb9e-3c49-87a9-6118537b544a | -6.28855 | -43.58156 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c85b78b-dfe4-3a93-9d5f-3121113cb36c | -6.99795 | -43.24976 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b861ed92-ba75-32a3-b3fa-90c7176cd2c6 | -5.80817 | -43.23808 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 016a3a20-73b8-3dee-9fc8-679dacb1113e | -7.6957 | -48.75329 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9db5d419-8df1-3be5-af66-4075cfb5f81d | -6.37432 | -43.00868 | 2025-09-03 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2f5f676-015b-3e1b-babe-311b098cc495 | -8.01678 | -44.10217 | 2025-09-03 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57d3ee5f-8fc4-321a-8d5e-1e78a5847eea | -6.9269 | -44.26292 | 2025-09-03 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df179228-02e7-34fc-b3ba-7560f7919f15 | -7.00295 | -43.21916 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc8b62cf-c5ec-370c-97f3-f89d94c24ecc | -6.97116 | -43.23998 | 2025-09-03 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c604da9f-9c8c-31b1-acef-fef38243f977 | -6.27134 | -43.58636 | 2025-09-03 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f2af2bb-ef54-33c6-9a8e-db403e869b5c | -6.49153 | -43.71358 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b4bcaf7-6e3a-3386-909e-a45fdf383eba | -6.34741 | -42.55666 | 2025-09-03 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04f0faf0-c500-329a-b182-1f569ac4d189 | -5.86462 | -42.97646 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3238f234-4acb-3f52-a9f3-107677166e66 | -6.30627 | -43.55133 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bcbf7db-c9e6-39e6-bb4b-002f51a65092 | -8.05141 | -45.363 | 2025-09-03 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29095758-f01b-319f-960d-ccdc55517a21 | -7.55858 | -45.71108 | 2025-09-03 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24d83da4-5d25-32f2-acf9-ac3b8ec6c23d | -6.28738 | -43.58839 | 2025-09-03 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d8798e2-f6a3-313f-b747-d4db4d1301c7 | -7.49955 | -45.35342 | 2025-09-03 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4397d5dd-45db-3151-a1c8-f165fa067db6 | -5.89908 | -43.39183 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19f28d5d-b8da-35ff-bd67-46407f8f3431 | -7.47874 | -44.83052 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c6a5188-93f4-3271-8e75-3e12ee856811 | -6.72988 | -42.26099 | 2025-09-03 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c099865-0446-39b9-9e68-48f3ed15d2c5 | -8.37967 | -48.30885 | 2025-09-03 03:53:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43920305-ad7d-3171-81a4-0b9671089700 | -6.87186 | -43.83842 | 2025-09-03 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a907cc91-a977-3645-8fd2-3d8131b40608 | -7.92679 | -46.46626 | 2025-09-03 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4f0030d-0f9f-3b23-a921-cff0fcd8161d | -5.90389 | -43.23282 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4465f666-67f0-3d98-9e4c-bb28e7ec0d9b | -7.47726 | -44.83888 | 2025-09-03 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 232da9a3-a8ed-3416-8511-781d84bd4393 | -5.92877 | -43.36374 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 243cd557-7b48-3853-a7c0-f5f1766df849 | -6.2396 | -43.40168 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4d1d82d-a438-3b1e-a5e1-94d7bb72999f | -6.34491 | -43.77268 | 2025-09-03 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5fa3897-80b1-3d5d-98d4-d11d6ce656a7 | -6.22592 | -43.3846 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fff697a9-917b-30aa-bc0e-39f3b18baf78 | -7.69083 | -48.74813 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 031b65ae-ec69-3424-a04d-1da258ac4833 | -5.81452 | -43.22498 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 31d89959-bf02-3ec0-8da2-5ca0d6c46e81 | -7.69645 | -48.74923 | 2025-09-03 03:53:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README31.md)
