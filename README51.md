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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc4802ba-60b6-39df-b996-122dd6bcb4c0 | -8.41538 | -44.13885 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b98fff0-f2dc-39d9-abbd-5854c4783084 | -8.38453 | -44.16251 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 826cc28b-7c17-3d6d-a2ac-8af3724a5460 | -7.46383 | -43.58879 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a25c4399-e98e-3a34-aa11-b52be01a89da | -8.38232 | -44.15503 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a53a3fa6-105c-3df6-80a7-4f51a25cb4b3 | -7.10246 | -46.90171 | 2024-11-10 04:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bf974b2-8d62-3c99-923a-a45bd8bb36b8 | -8.38508 | -44.15903 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c0aa4e8-67fe-3c58-916c-4b75703d4b35 | -8.37846 | -44.15799 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02fd4765-4a21-3149-b86e-72d5954dfd9c | -8.39941 | -44.15416 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77a87d2e-0507-34dd-91f5-2fd693c2cc5e | -7.20961 | -46.95738 | 2024-11-10 04:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e48f0d3-98b3-3d26-a35a-3e2fefcaea27 | -7.41202 | -43.09167 | 2024-11-10 04:16:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3debe758-822a-338c-8be0-19ee72378665 | -8.41262 | -44.13485 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4000fc80-2b63-39ae-a75d-498a49a897cb | -6.24108 | -45.68267 | 2024-11-10 04:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b8b225d4-1e54-3212-9a09-2518d5cd8838 | -8.38784 | -44.16303 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5c0d76b-6029-314d-b964-e97039ee5f46 | -8.41264 | -44.15624 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d3d3c62-598b-3334-9429-aa470e7197c7 | -10.19701 | -36.29349 | 2024-11-10 04:16:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b16ed434-f9eb-3337-9786-4c29d5a7b9f3 | -8.38782 | -44.14164 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0401e33-8d0d-3e47-961b-d2f55a37edc8 | -6.79072 | -43.65202 | 2024-11-10 04:16:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f025576-0c61-375b-baae-0cb561594a4f | -8.40493 | -44.16216 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f79f2a4-c1a8-3d9b-9264-b35013d6a9ac | -7.42782 | -46.65197 | 2024-11-10 04:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e501a50-9461-3458-a8f9-639ed438c083 | -8.3812 | -44.1406 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 37fea034-17be-3a8e-ba8b-5c8d80404255 | -8.41592 | -44.13538 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f80c177-c537-3590-80f7-e7927a17d743 | -7.63203 | -43.55908 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a7ee936-be5c-3f83-8121-76e54a9a1e0b | -8.39003 | -44.14912 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a09d9588-44ab-320e-87d8-8bf21363adb5 | -8.37648 | -44.14642 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fccf726a-121b-3897-8bcc-cc8b60adf006 | -8.39993 | -44.1293 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46dc2b06-8d11-375e-b23b-b6580e3ca17a | -7.16373 | -39.03212 | 2024-11-10 04:16:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ec894408-36fb-3951-bb89-216808792b2e | -11.09699 | -43.33528 | 2024-11-10 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4197e035-6ef0-3048-b642-9eaf47d1d26c | -7.39782 | -43.59973 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5e1e39a-ad52-3fad-92ae-7aeaab93462a | -8.36932 | -44.14886 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06d592df-1eea-302c-9c45-85362fa282fd | -6.29024 | -47.34918 | 2024-11-10 04:16:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f053a846-39c7-3502-bd51-50fc632eca7b | -6.73712 | -46.38421 | 2024-11-10 04:16:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e23209ab-f7d1-36ff-8a95-c8334592415b | -8.37262 | -44.14938 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e13eb293-0da4-33b3-bd6e-ee24c2ecf022 | -8.39058 | -44.14564 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4eb8df2c-f171-35d3-b720-ac016dbd6e7f | -8.66715 | -45.81721 | 2024-11-10 04:16:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c101a9c5-09cc-325e-8201-c0b13936ccb6 | -8.41319 | -44.15276 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51b9c619-4adb-3457-b3f0-b680e3ef671a | -8.41152 | -44.1418 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 696b1a8f-eece-399b-85d2-48d8911fc79e | -8.37426 | -44.13894 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05bcfd3d-cf81-3f3e-a2e1-703f40411852 | -8.39886 | -44.15764 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55e633d7-16ba-3f79-a848-45adddf64521 | -8.37593 | -44.1499 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a894e0-2efd-33e3-8ea3-ed17027a24fc | -8.3715 | -44.13494 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19833742-62f9-30cb-8041-393d3fbe5de2 | -8.37204 | -44.13146 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04e92b34-e9eb-3d49-8e9d-beebe24a8f27 | -7.12909 | -45.40017 | 2024-11-10 04:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c51df98-539e-3e17-b1ce-86134c93123c | -8.83916 | -47.70454 | 2024-11-10 04:16:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62de4b06-5bf3-3b08-8389-69427d540601 | -7.43643 | -39.76167 | 2024-11-10 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 84ffe5c8-56f4-3a75-b52f-7bd206a7c49d | -8.38286 | -44.15155 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c195bd00-a4f0-3c49-be67-67eb905a44f0 | -7.23233 | -44.99409 | 2024-11-10 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7e42875-f84e-35fc-a3c8-254f30200d03 | -8.41043 | -44.14876 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87c849b0-5f6d-324d-b7cc-634638d74f55 | -7.43835 | -46.63237 | 2024-11-10 04:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be0bb103-2e39-3280-b063-609811be20d6 | -7.12566 | -45.39964 | 2024-11-10 04:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53cd6390-5693-385a-b330-d156422ba94c | -11.7033 | -48.98381 | 2024-11-10 04:16:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44752339-5773-3d2e-974f-37f7de2a9015 | -9.7185 | -35.96338 | 2024-11-10 04:16:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 068622e3-651b-345e-b2a3-733d22ef60fa | -8.38065 | -44.14408 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f03c4d16-5c23-3799-87f4-8c538dd1cd4e | -8.36877 | -44.15234 | 2024-11-10 04:16:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c134fd09-2e1d-3d4f-8232-ef90215c4ee5 | -9.41522 | -41.18925 | 2024-11-10 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 915ad7f3-c464-3418-927b-90a440103862 | -8.37208 | -44.15286 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e00ace18-55bb-392d-83e1-fb592bf86213 | -8.39776 | -44.1646 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99169dfe-f995-3d31-9a12-c97fab3e7520 | -6.95181 | -47.78741 | 2024-11-10 04:16:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6399e647-ab99-36c4-aa1f-43ed98e627a7 | -7.43576 | -39.76632 | 2024-11-10 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| df790f19-d7c4-38ce-ad65-f44e1cb3b053 | -12.13176 | -39.38374 | 2024-11-10 04:16:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a8f2c4e5-3fb3-3c46-a825-7c4ebde1523a | -6.09815 | -47.05242 | 2024-11-10 04:16:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0336136d-cb54-3eb0-bd55-6dc511f39979 | -8.37702 | -44.14294 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 858d8131-e675-395b-89be-08ffedf191c3 | -8.37535 | -44.13198 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2053746-a361-3447-b4e0-c2b2b3e680c2 | -6.66234 | -47.87814 | 2024-11-10 04:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d332cf9-7d51-3b30-bf11-17382ad7cd6a | -8.40878 | -44.1592 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b185144-ea86-3c8a-a59e-9bc609695170 | -8.38725 | -44.12374 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f800bc10-7183-30f3-a012-91fc54a392a7 | -8.40272 | -44.15468 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e181bf1-77ea-378f-99a3-e11e8166e5c5 | -6.43336 | -47.04588 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07e599c0-9a69-3222-89a2-04ea0ad01d82 | -6.08678 | -49.61389 | 2024-11-10 04:16:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04a7c55f-bd35-36f5-8526-ac9f1d7cba12 | -8.37956 | -44.15104 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99235f98-70ed-3f64-906c-7581276a4de9 | -8.38341 | -44.14808 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3cb7c8a6-37f0-31ed-9043-718611394d72 | -8.38838 | -44.15956 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90a89cfc-5fa3-3ba7-bf67-8b4dcf3cd9bd | -8.39995 | -44.15068 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d6e4f61-54c4-38cd-9066-877164a0033b | -6.48517 | -47.511 | 2024-11-10 04:16:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eddc4cc1-a6e5-355b-81a3-bd2a4f16c8b1 | -7.14446 | -41.10389 | 2024-11-10 04:16:00 | NOAA-21 | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 61d80e15-131b-337e-b29c-5acbe2decb95 | -8.39001 | -44.12774 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1813e63-4fc2-37c2-b558-b9d3d2638f19 | -7.63533 | -43.5596 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1fae5a8-0cff-3517-bc4f-8b50faab8509 | -12.56115 | -49.67187 | 2024-11-10 04:16:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6d4aaf3-bc79-3f0d-8e50-d2734318f088 | -8.295 | -43.62534 | 2024-11-10 04:16:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45def7ad-5de2-31d5-8741-bfee0c1203ba | -8.39332 | -44.12825 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19550cb8-7bd0-3409-9427-b6d56935ae08 | -8.39665 | -44.15016 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeaf6865-8649-3af7-96b2-eae22ed20757 | -6.40722 | -47.51558 | 2024-11-10 04:16:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d555da2d-87ca-3b30-8026-860022430f23 | -8.39555 | -44.15712 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5db7309c-ab11-3cf9-98f4-9ad3bcbb7449 | -8.53869 | -40.97635 | 2024-11-10 04:16:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d3be77d9-3fa4-3b70-9263-22573bb05227 | -7.43203 | -39.76586 | 2024-11-10 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4ae2d3db-d4df-3f31-9317-508c2c47d5ff | -7.43271 | -39.76118 | 2024-11-10 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5e112ef0-0161-3248-9c09-7381b576525a | -8.3961 | -44.15364 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebe917a4-e86e-3c59-b036-04a7a87fd8b4 | -7.17596 | -45.39238 | 2024-11-10 04:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c2dfd8c-2313-371e-bf56-c9d7e4beb984 | -7.63479 | -43.56306 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75c3db0d-a14f-3418-b151-48b9348a4759 | -8.41098 | -44.14529 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b0d149d-6f3f-3b25-b920-22ad48676611 | -7.4732 | -43.5938 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5284c0bd-27c9-3f8c-8373-aa75e4c6c43d | -9.83465 | -36.16095 | 2024-11-10 04:16:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89a50f6c-7733-3d81-b913-74e902104b97 | -8.37484 | -44.15686 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 933ec804-b050-3b9c-af10-b486f733c57f | -7.03429 | -44.84824 | 2024-11-10 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 010bb24c-5cb7-3ddd-91c8-9e312bbd63d1 | -6.03186 | -46.37575 | 2024-11-10 04:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 322d500c-3499-323f-a9bf-b5ae793bd6cc | -6.3292 | -46.72042 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dfb77da-f86e-3c07-ac5f-995c1657b6c6 | -6.4203 | -47.71243 | 2024-11-10 04:16:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01036649-5807-3838-b4f6-33af06eb47c8 | -8.39719 | -44.14668 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93342dcd-66eb-3d21-af25-ff7bb9b4fe8c | -6.24333 | -45.69098 | 2024-11-10 04:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bf86eb7e-9fbc-3dc7-a47d-cd145c349f0b | -8.41155 | -44.1632 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc8827b8-fbd2-3406-99c8-ab1b0f400677 | -6.26841 | -44.54581 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README52.md)
