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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ca589b8-a92e-3265-a75e-a70767d98e11 | -5.45196 | -46.18055 | 2025-12-27 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fec7d89-a1d3-366c-aa12-4e2d93a8fbc2 | -6.54645 | -43.1043 | 2025-12-27 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecefb581-789a-3094-8aea-50e1df1e2b7e | -3.76767 | -43.55507 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fabf3d7-7228-3b4b-b22d-504b33481304 | -5.34205 | -37.05567 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89767880-4440-3c6a-a22c-1f2ebd18307a | -5.34696 | -37.05228 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d781427-9064-3ac3-8171-e1da29f20055 | -3.97337 | -43.40778 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 286aca7d-4dcf-3fdb-99f5-3e38c6fb9b1a | -3.6527 | -43.51202 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c58be351-397b-3559-a49b-c7577e52a525 | -6.30807 | -41.88674 | 2025-12-27 04:18:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2efa22b8-77ca-3593-ada0-fa812a701480 | -3.77101 | -43.5556 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76412fb1-8b1c-33a6-b913-520eb5771bca | -5.92969 | -43.51437 | 2025-12-27 04:18:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3239e0b4-3353-3f50-bde6-b378330c7d2f | -4.98471 | -42.72931 | 2025-12-27 04:18:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 378af294-c170-3b08-b0dd-324eea4a4375 | -3.31241 | -47.38432 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e6865b1-1a32-3c6f-b279-235ce7f803e7 | -4.17451 | -48.58581 | 2025-12-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c61d794e-e1ee-3251-acbf-c5fa61434384 | -2.4547 | -47.78408 | 2025-12-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 791514b1-3084-3329-b537-4c58122c2cbe | -2.45593 | -47.77635 | 2025-12-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4331c612-9358-34f0-8ead-379f7daa895d | -0.08721 | -51.28043 | 2025-12-27 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 05a7a571-8e6c-3cfa-a8f7-af6a05992f1a | -4.92034 | -40.66266 | 2025-12-27 04:18:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16ed4acc-10c7-3a4d-9d41-e268d8d2b716 | -3.12839 | -52.85001 | 2025-12-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d9bb9f0-684d-3445-a954-48ed7b02c598 | -7.19229 | -43.12792 | 2025-12-27 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2cfab977-6542-3fca-8bd1-6303db96c7fd | -4.66795 | -42.39976 | 2025-12-27 04:18:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28e61634-22b6-38bd-bda1-f80d8cf88cbb | -4.62891 | -47.94323 | 2025-12-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b20c080-c205-3401-b9a7-235c962bd26f | -4.91976 | -40.66645 | 2025-12-27 04:18:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef5e2092-7c1d-3a28-8be6-53debe1c5052 | -3.46914 | -52.80364 | 2025-12-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f10e058-87d3-3a2a-8c23-897d28e976e1 | -5.34819 | -37.0442 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c14a24b0-31eb-3fcf-bbfa-2ab7972cc95c | -6.54977 | -43.10483 | 2025-12-27 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d537ef3-c10d-3cf5-a601-fc9e251c4155 | -2.92588 | -48.23779 | 2025-12-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c97cc07c-021c-33b2-88d2-5bef1fc27079 | -3.46844 | -52.80768 | 2025-12-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02dda7b2-4953-38e2-8f5d-118be31b26e2 | -3.75257 | -49.72524 | 2025-12-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd7fc7a7-5ddb-39b6-a54c-59696420e47c | -3.65605 | -43.51255 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc72b5ba-f063-32c4-aeb7-c117cb216556 | -3.61803 | -42.40804 | 2025-12-27 04:18:00 | NPP-375D | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a817cd8a-a7e8-31ae-aa5b-9cc3f4b7e473 | -6.66822 | -44.68923 | 2025-12-27 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7361d3ba-a567-3e8b-977b-66d39d53dccd | -3.31767 | -47.37736 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7c3e8919-e630-310c-9d6a-171a0867e714 | -5.34624 | -37.03815 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b14ebcde-e36e-3770-8e29-562117337473 | -3.76711 | -43.55859 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8baac680-22ce-328f-acbc-b733359b0b83 | -6.18223 | -43.41589 | 2025-12-27 04:18:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fcae9848-dc3e-3b2d-8fe5-8df6d1cf4a9c | -5.67289 | -47.52048 | 2025-12-27 04:18:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5abbfa1e-dadb-3664-93a3-9f6d6f3e8ad4 | -4.67503 | -38.06721 | 2025-12-27 04:18:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5cee3b10-9209-305a-8cbe-d53f735726fd | -4.17288 | -48.58188 | 2025-12-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bd6a431-8509-3620-a80f-cd669e31989f | -2.67796 | -42.74449 | 2025-12-27 04:18:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce5b44b6-69df-358c-9604-1de56cd2d7aa | -2.89322 | -52.59269 | 2025-12-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42a331aa-e9c8-3114-acb3-f0d9f8e4ccd6 | -5.82075 | -39.08603 | 2025-12-27 04:18:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5bd83836-9b6b-3420-97ff-6923cbff3305 | -2.45947 | -47.78097 | 2025-12-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3db21657-8b92-3fe1-be2c-548907ead68a | -3.76264 | -43.56507 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 561127bf-4e33-3a8f-8ec5-1be36eed36b0 | -6.53816 | -43.11366 | 2025-12-27 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 569a3638-1d19-3657-83df-86548c15943c | -3.89901 | -42.55494 | 2025-12-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| fd7f610e-c70f-3a87-bf28-4f5a65fec1db | -3.65158 | -43.51905 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed8798db-45fb-3660-8588-c750af5d5a8b | -4.65714 | -38.78691 | 2025-12-27 04:18:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d969d46-a0c7-3149-b426-ac724461ab0a | -2.68684 | -42.75297 | 2025-12-27 04:18:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feac947e-b5ce-341e-aaa5-5fefbde72d11 | -3.30897 | -47.38027 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5bc4d7d-7bad-30d5-98d7-a343b3d45702 | -5.34328 | -37.04757 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8eecc60c-89c2-328b-b02a-11cc56d86829 | -5.04548 | -42.36578 | 2025-12-27 04:18:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e1ec241-f30b-386c-a3e2-97928f0957a4 | -2.93015 | -48.23848 | 2025-12-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec753e29-46dc-381d-a29c-01318699bc02 | -5.47858 | -46.83452 | 2025-12-27 04:18:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 614b62bb-b515-367e-9ae4-5fa3181fcfe5 | -4.44562 | -38.93088 | 2025-12-27 04:18:00 | NPP-375D | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5f88657-3c4b-394c-8170-704654346298 | -2.96603 | -46.78782 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c13abd90-a72f-3a10-a9fc-ef51bd9ab38a | -3.40997 | -39.35377 | 2025-12-27 04:18:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5eafce5-3a01-36d9-b9fe-88d43dae2071 | -2.46484 | -47.77405 | 2025-12-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 546b1b6a-2533-339c-9891-61512b942a96 | -3.0008 | -40.33878 | 2025-12-27 04:18:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 458721fc-ccd3-3a1d-b4eb-fb83ee5fcddd | -2.60914 | -47.31313 | 2025-12-27 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13b4f8f5-982b-3880-a29e-18081fbb26e7 | -3.54519 | -43.20504 | 2025-12-27 04:18:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3eb5d8e8-fda2-3b47-9b3d-b7445e945e95 | -3.25926 | -52.4308 | 2025-12-27 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe8ace66-7234-31f0-b95a-d92f69b35ab8 | -3.13419 | -52.85106 | 2025-12-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43501fa9-077f-32a5-adf6-08a1e1c4bad6 | -3.90565 | -42.55598 | 2025-12-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e041ef73-b774-38c5-8c4d-c0ad41753f95 | -2.89386 | -52.58892 | 2025-12-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc0af376-d98d-3962-b452-a533b084ed16 | -4.40024 | -42.1438 | 2025-12-27 04:18:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d66c8cbb-c656-393c-b7f7-6574440dff09 | -4.67901 | -38.06783 | 2025-12-27 04:18:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc2ec467-60d2-3431-acb3-e87d10081e9d | -3.25298 | -52.43365 | 2025-12-27 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a32b84a-64ab-3640-97fd-aa2a6f1d1177 | -2.69671 | -51.64807 | 2025-12-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36c96ad5-3b7d-3251-8a67-130bce4e45b1 | -3.31641 | -47.38499 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9039bee-dce0-3c17-b25f-1a538fb2a1f9 | -3.65661 | -43.50903 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdf17df3-b4ac-3b6b-967d-a9bc39d30b00 | -3.45058 | -42.24732 | 2025-12-27 04:18:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7624c49f-f318-3c05-9978-46ca9f597855 | -2.99734 | -40.33824 | 2025-12-27 04:18:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f2895d79-52f7-3da0-8843-e74528d09492 | -5.93643 | -44.45501 | 2025-12-27 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0780e2a-8c75-3d1a-816f-2efda61cee70 | -6.04306 | -41.93347 | 2025-12-27 04:18:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b0dc6f1-f456-3f13-84d9-69e9a42bc86b | -2.37226 | -51.90846 | 2025-12-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d58884c-8544-3d3a-a39f-8a06b225d5b9 | -2.60858 | -47.3166 | 2025-12-27 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e57ba1d-c2a3-36d8-84f6-f200296df8ad | -6.17891 | -43.41536 | 2025-12-27 04:18:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e26925e-f8fa-3d46-a3bf-f47bc3c615a3 | -5.08075 | -37.64767 | 2025-12-27 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b174215b-60a4-3a85-bf4a-2b5714d2f80e | -6.10141 | -42.18587 | 2025-12-27 04:18:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23b85092-acf3-32d8-953d-df9f7a3c7c19 | -2.45532 | -47.78016 | 2025-12-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b797a282-3d31-3a59-9a60-162a383911c3 | -5.11891 | -47.30984 | 2025-12-27 04:18:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d15b49a6-a3a9-324b-a9b4-2ed4bfdb580f | -6.0425 | -41.93703 | 2025-12-27 04:18:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d5a7cdea-68a1-3e19-b25a-f70bb1ee66e1 | -2.37781 | -51.90926 | 2025-12-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca24c17a-63c3-3f77-b5bc-63f95cf03b72 | -3.46841 | -52.80761 | 2025-12-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 244a2b37-0779-3fb5-91fc-dd9680034c5b | -3.46909 | -52.80355 | 2025-12-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537b83b6-8673-3de2-8c35-2413ec29c9bb | -3.32141 | -45.9926 | 2025-12-27 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0446cd95-44a3-3f84-b702-25aeeb0eedc7 | -3.76655 | -43.5621 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 61810968-04a5-30d9-a250-a12c862dd030 | -3.44108 | -39.02657 | 2025-12-27 04:18:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 38e9fd07-05c8-3982-9a2d-3f4de650793f | -5.1847 | -40.11331 | 2025-12-27 04:18:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ac7b847-dd67-33e5-a48d-07c9dfee8434 | -3.7593 | -43.56454 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c21563ce-452e-39c4-8fc6-50fc86df3deb | -6.55364 | -43.10189 | 2025-12-27 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3564b381-feb2-3c74-9ad4-9a10826200a5 | -4.17224 | -48.58587 | 2025-12-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab20a72c-dce2-3d47-a683-79623a76d4c7 | -5.94055 | -44.45522 | 2025-12-27 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da485a64-a3eb-3ec8-aebf-2728ea55ac60 | -4.40655 | -40.69429 | 2025-12-27 04:18:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1696e33-4583-3d1d-a1f5-8165f12a4269 | -3.32211 | -45.98832 | 2025-12-27 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3958b615-0830-3d34-93a9-b60d728df23b | -5.33775 | -37.05501 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0617ac6a-7019-3b16-a6ac-ab07f2b69e4b | -3.65995 | -43.50957 | 2025-12-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71daa1a1-65de-334c-8bf0-dd21ce480b4d | -3.31367 | -47.37669 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a0b56c01-f591-3c75-b5a5-72d6edde77ce | -5.34507 | -37.04629 | 2025-12-27 04:18:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4019bc8-8b00-3042-b2b8-a15dd77d69b8 | -3.75336 | -49.72043 | 2025-12-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
