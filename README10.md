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
| 3ae6d984-d1be-33cc-b464-c18be5603abe | -4.76795 | -47.6134 | 2024-12-22 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daa41806-0411-3c67-84f5-54415cb9a4b2 | -8.80048 | -49.79618 | 2024-12-22 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f33ba9a-378f-372f-b120-b25131c2ad19 | -11.10926 | -44.62648 | 2024-12-22 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93593f58-d798-32be-a945-f03a78859c92 | -5.22879 | -44.33588 | 2024-12-22 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c301f9f0-480c-34db-a3c7-100d3e4d6153 | -10.57294 | -44.6095 | 2024-12-22 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8be07e65-4411-3e4a-ba1a-af4626db4ff6 | -4.71532 | -46.82716 | 2024-12-22 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d443dedc-3c90-34bd-9f27-4f62cd446871 | -12.44142 | -41.4475 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| befb9e73-2828-32f6-837e-a2ef02418417 | -6.01835 | -45.88978 | 2024-12-22 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0873019b-fab7-3bc1-995a-5264b4ca4962 | -12.44201 | -41.44308 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1a06be23-cebf-3f12-a58e-6d33beb8fc7e | -6.00096 | -45.40886 | 2024-12-22 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37e05ccf-3d08-35d8-8a9d-2fc68e5c3651 | -5.23442 | -44.91423 | 2024-12-22 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 120ba63f-3696-391f-b3ac-e9799b3f2f67 | -12.4476 | -41.43464 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a4fe9e66-77e6-3fd7-9a43-4c877027c2cd | -12.46066 | -38.47626 | 2024-12-22 04:27:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4456077f-7908-3afd-85f1-36246d9f7c9c | -11.96867 | -44.2394 | 2024-12-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 054cce92-58ef-3801-87c2-0f1c60d0349b | -6.00429 | -45.40937 | 2024-12-22 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5a795ba-0425-3bde-9f4c-8eab37a75c53 | -4.77091 | -46.38581 | 2024-12-22 04:27:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea2c4f1e-98e9-35f9-837d-beebb70d9b1c | -11.15273 | -49.69535 | 2024-12-22 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a93af5a-c716-335e-9a07-a9fa4ec1fe7d | -5.75582 | -46.15666 | 2024-12-22 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8b98ba7-cf07-366c-8e73-f0a27173b681 | -12.34377 | -43.67636 | 2024-12-22 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2253967-803a-39f4-b8e6-996aca8ed199 | -11.43737 | -42.30407 | 2024-12-22 04:27:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9eafe0ff-b596-38a0-bd37-7f743e724e3d | -5.94905 | -48.04464 | 2024-12-22 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e6baaaa-05c9-3484-a352-6ab7c54e7d33 | -5.23162 | -44.91014 | 2024-12-22 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a93603f4-13ba-3d70-ad83-6628604798ab | -12.4426 | -41.4386 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 102d2a54-5c3b-395e-926a-9bae0ff9059a | -5.2182 | -44.9081 | 2024-12-22 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f525b6f-db9a-3bdf-966a-2f3ee8cd628d | -12.43764 | -41.44231 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a4032a96-3e79-392c-a417-f20e557aa4c8 | -12.44698 | -41.43929 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 70655640-57b8-394b-962b-49ab1ac276fb | -5.89577 | -45.56124 | 2024-12-22 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe472eef-18d0-3955-b6c0-ace892af31b1 | -11.15617 | -49.69593 | 2024-12-22 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b2bc3e1-8f83-32ce-8492-809a6a9be784 | -7.86444 | -43.086 | 2024-12-22 04:27:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50baa7a8-8baf-3284-a810-f41a9450dc5b | -5.36072 | -45.17299 | 2024-12-22 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aeaafccf-efbf-3077-aec6-c4cee4b69039 | -5.3026 | -46.46592 | 2024-12-22 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c361d179-4c38-3b43-9769-b4498c4cdb4b | -3.94577 | -54.63237 | 2024-12-22 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f87c4427-52b4-3ffa-8382-6fbb2660bd30 | -4.27853 | -55.7444 | 2024-12-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 850fd249-5986-3308-a755-6d8206d88f1f | -12.44323 | -41.43383 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 33698e63-a80a-33a6-887c-00eaadce4ce0 | -4.5978 | -47.97604 | 2024-12-22 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9a075c2-da88-33c1-8548-93172783b377 | -11.15554 | -49.69973 | 2024-12-22 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33489158-af9c-3e4f-97d3-992b7b18ba17 | -6.16057 | -46.08944 | 2024-12-22 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dea67cdb-da02-3952-999e-3de92c1a951a | -5.41791 | -47.5691 | 2024-12-22 04:27:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e117626-ca26-3b28-a4e9-4bb3138cf555 | -6.16111 | -46.08599 | 2024-12-22 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97d57926-60fc-36fa-98a1-9c8301f7a44c | -11.11282 | -44.627 | 2024-12-22 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80d91dc9-bf34-3264-a252-c165142d6a44 | -4.27919 | -55.74061 | 2024-12-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b258989-1da6-3dd3-aeb6-0af643e4f928 | -6.00375 | -45.4129 | 2024-12-22 04:27:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a49e3578-8266-386f-b6c0-fea9b854f8bd | -5.22936 | -44.33219 | 2024-12-22 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41895e45-3c58-3af3-8a95-30c59b6adb4d | -12.3355 | -43.68002 | 2024-12-22 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8340d5c9-2587-37be-85e4-b5c40b84adac | -12.43708 | -41.44654 | 2024-12-22 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 02674a1e-d1ad-3c45-aff5-7a49b411030c | -6.30179 | -41.697 | 2024-12-22 04:27:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c6531942-83a3-3a02-ba6c-bf6ef632ddea | -3.95096 | -54.63316 | 2024-12-22 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4cba5af-3f0f-388d-b03b-55ad31e3c41a | -12.43954 | -41.42794 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7bbec1b5-e5e9-33dc-b214-3c063b651a6c | -10.56941 | -44.60895 | 2024-12-22 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a967069-49a3-3877-aa2d-b9a16c79aac3 | -11.79076 | -49.31828 | 2024-12-22 04:27:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 868729c3-6ecc-3ca1-8d33-717cf9e6268a | -6.24501 | -46.1804 | 2024-12-22 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05558b01-afc7-3607-be35-d36a95147f2a | -15.60302 | -39.62078 | 2024-12-22 04:29:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8d745368-0e22-3b45-8736-af9611f36af9 | -13.39802 | -42.32089 | 2024-12-22 04:29:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6737268f-fc32-313f-8aac-c6e379122445 | -13.40274 | -42.31757 | 2024-12-22 04:29:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 55519ca5-db6b-3a7b-af74-59c2096e97bb | -13.40327 | -42.31366 | 2024-12-22 04:29:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1a894ca-ce85-3da7-a9c1-40bac2472f9f | -11.48694 | -54.03071 | 2024-12-22 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99599f85-86e7-306a-9aa0-2640b7b63595 | -13.39855 | -42.31699 | 2024-12-22 04:29:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ab9ea803-a6ae-3154-b3dc-9b1b44204895 | -13.40222 | -42.32148 | 2024-12-22 04:29:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 96367f9c-1c11-374c-bc00-4cf15c3fd696 | -27.29634 | -51.98202 | 2024-12-22 04:33:00 | NOAA-21 | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5806e1de-b78c-3278-923f-aa5953bdd048 | -12.44014 | -41.43567 | 2024-12-22 04:36:00 | AQUA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 1a83b51d-e6a6-3e28-85d8-3777fa34f6b8 | -14.08772 | -41.9774 | 2024-12-22 04:38:00 | AQUA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 99adb111-7e59-3adc-84f2-b5c82868c9ce | -4.60387 | -45.44928 | 2024-12-22 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dae1e9e1-8336-3a9d-908a-e66b397af614 | -1.2976 | -53.12666 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e33bc5f-3242-396d-94db-b8c2051c2ec1 | -2.49032 | -49.04887 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7125ec29-cf5d-3cd3-95f2-4893671da52a | -4.48264 | -47.1418 | 2024-12-22 04:50:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18378f2-10e4-3592-af46-8503992d56a8 | -2.56741 | -49.45685 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a1013b5-3c88-391f-8aa4-af46fc102eb7 | -3.76579 | -47.19855 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a0ce064-6a2f-3573-8226-159a8b9268ac | -2.56973 | -49.46511 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a298c4d9-aa2c-37ea-885b-17dece479f28 | -3.90717 | -47.00623 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f21c79c-75a6-3f8d-9c1b-06e6e814831f | -2.51605 | -54.22557 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f2ec2e-a036-39d2-82ad-801b625bcdcd | -2.44882 | -51.78758 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 578449aa-08fb-358e-af7a-d72769019a8f | -4.13924 | -46.11323 | 2024-12-22 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 419fd530-85cd-3e7b-9b5b-6f4db130434a | -2.76857 | -47.39132 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 118ab2e1-ee64-36d3-952a-247e580e96c6 | -2.80017 | -54.18962 | 2024-12-22 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f17e3a70-5a1f-3832-889a-3f735177f0a6 | -2.49849 | -49.06652 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d5a4854-80c0-39a4-b725-28cb5f1cba3f | -4.03196 | -50.05133 | 2024-12-22 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eac4349-2e86-36a2-830e-95dd890b86af | -1.30142 | -53.4529 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3794b9a6-d5e5-3c1b-a206-804d251d6db6 | -1.29083 | -53.10336 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84237822-654b-356b-8bd5-9d7f2f760602 | -0.95812 | -46.85339 | 2024-12-22 04:50:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e9bf9d1-9e9c-3b69-bc61-906b54c77084 | -3.9234 | -46.90117 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6b5d951-daaf-3cb9-aa9a-5e56124ee477 | -2.83232 | -51.78366 | 2024-12-22 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8f46862-0ecc-37b2-a64b-a5e6d3080e33 | -4.9558 | -44.00376 | 2024-12-22 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ff2a16-1b5b-3c5e-8240-03847f461d3d | -1.81206 | -48.45424 | 2024-12-22 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744d714d-de22-381e-957b-a8a8477156ce | -1.71333 | -52.59241 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8b717f6-6142-3bb7-92dc-a6eb67a5fab2 | -2.57264 | -49.4695 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| de34b9c8-9672-36de-bbee-d21c22b668b5 | -2.3682 | -48.51909 | 2024-12-22 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 680ca01c-2e19-3324-bd0c-9da800311e1a | -3.80121 | -46.72118 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dc740e2-66d4-30b2-a470-4a8f317346b2 | -2.1596 | -48.44712 | 2024-12-22 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b98250ec-2b9b-3a7a-831f-1a3c07d23ea8 | -3.93389 | -46.43869 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 533083cc-7d91-3e64-a001-da0e7350abfb | -2.03958 | -52.11235 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cb14821-754f-3e41-a33a-68fa32a96af6 | -1.7064 | -52.41923 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c81f6760-6cd7-3dfb-b75d-1a478d8f1215 | -3.75127 | -47.18581 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eadc26d4-05b9-3c05-8e1f-a6b27f879fa5 | -3.81122 | -46.71132 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a554b969-a75f-3e39-8ae1-4f959bf2c746 | -2.97295 | -48.08359 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3891680-85d9-3066-bf90-fcc49f513e68 | -4.0212 | -46.09249 | 2024-12-22 04:50:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7aafeac-81f2-343c-9b2b-fb4e9d4a0f34 | -3.2525 | -48.06842 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f84b7a67-9081-35f9-b7b5-4ca560e59ee0 | -3.08412 | -46.56192 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6db90bf5-715f-36c6-8163-fbafae1770f5 | -2.93343 | -54.30022 | 2024-12-22 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b54aff-b9f1-3130-8c8a-46462c19c0ee | -2.5033 | -49.05908 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80619b69-054d-3eb3-930b-c92d1f9f8816 | -3.09242 | -46.56329 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
