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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b32b4b9-5fe2-3a79-a399-cae18ed071f8 | -17.24315 | -46.85197 | 2025-10-23 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a413726-8294-3cb4-9682-5236c34c8b45 | -15.58451 | -49.06861 | 2025-10-23 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa9038de-50f6-3671-90ad-e07da5cbd795 | -17.61235 | -46.58254 | 2025-10-23 04:59:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bb897a45-62d2-37b0-9421-a321fe5f2f17 | -14.87057 | -59.63843 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2edf459d-ef72-3f35-b165-e84f6eee137d | -16.0815 | -51.41012 | 2025-10-23 04:59:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6bec5da-4cdd-3e3f-9675-3bf41b503a92 | -17.61553 | -46.60583 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3c25d0b-817b-30ef-b65c-4bcbce0944ab | -20.55604 | -54.5573 | 2025-10-23 04:59:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b0c502be-235a-38bb-b866-69d7b86342a2 | -14.87664 | -57.26871 | 2025-10-23 04:59:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43d3ab61-037a-3058-a56b-02dc9cfbbea5 | -15.67513 | -53.34898 | 2025-10-23 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a62a0a-5c6d-378a-a1a0-d60be11f6c40 | -17.14604 | -53.30615 | 2025-10-23 04:59:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6af570b4-f70c-35da-a7d6-d945084d431d | -18.22938 | -47.4178 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f0a405d-667a-3a9f-b8c2-f033724e49cf | -17.55434 | -51.04558 | 2025-10-23 04:59:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 149fed45-2bd6-3dd1-86fd-ba21ab1cd9ac | -17.60915 | -46.61305 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 64aaa12e-cad0-361d-9b77-39251a9386da | -17.60442 | -46.60458 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd4be5d2-4e0e-3ec7-baa2-0a94a74723cf | -17.60753 | -46.62841 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 6c8ac0aa-fee0-32d8-b4d9-68c2f977c267 | -18.22539 | -47.41732 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0185f3d-b86e-3a0e-8092-c9d618356a25 | -17.24276 | -46.8556 | 2025-10-23 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57a36e8c-2a5e-3283-b279-f05db02881ce | -18.23029 | -47.4216 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d353c62-3a33-39aa-839c-0a8a7c4dbba5 | -19.15415 | -49.13063 | 2025-10-23 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7160c5c-f49d-3e80-bbdf-8293f0bf6fa1 | -19.78843 | -50.98233 | 2025-10-23 04:59:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6d4e897-5dba-3528-90cc-856d01c95e17 | -16.47309 | -46.47557 | 2025-10-23 04:59:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 093a2997-c702-3c30-aeb8-8994fcec32b3 | -20.48703 | -45.98045 | 2025-10-23 04:59:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 019511fe-bf80-333f-ad15-3a5cd1e70db8 | -20.26101 | -47.91067 | 2025-10-23 04:59:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54a5e4d0-1a31-3861-a320-e750a84fecc1 | -20.98077 | -47.36477 | 2025-10-23 04:59:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0357c1b4-f8bc-3f06-907a-2b3af5fdd815 | -18.72519 | -46.83381 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 559f1b0a-69bf-3462-a646-d2f39eba4a9c | -18.23107 | -47.41461 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13bbf8f7-d4a6-37d4-b4e9-4f3b55d99ace | -14.84484 | -54.22426 | 2025-10-23 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7210a308-db1e-3258-a47a-0ec1893251d9 | -15.51193 | -59.27369 | 2025-10-23 04:59:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb1f7511-9661-333a-8b77-6b27abae74bf | -17.61348 | -46.62523 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4af87104-2ea7-3fdd-94f5-b2b686b90fd6 | -19.15351 | -49.13626 | 2025-10-23 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07fe77c1-4e90-31ca-8ca5-3384abefdaa1 | -16.49815 | -49.7468 | 2025-10-23 04:59:00 | NOAA-20 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b78f16de-a5c4-3283-9694-01b26cc3f4d8 | -17.60714 | -46.63218 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| baf8fd66-ece1-3a23-94d6-be94da51efde | -17.60482 | -46.60073 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3bf68f5e-9f92-373d-8acf-76fe451bc179 | -17.60359 | -46.61248 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7d873327-12e6-3d1c-81ac-ec1c5821647b | -17.61388 | -46.62142 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7911020b-af34-3b8c-b38c-3ec040706913 | -18.23068 | -47.41811 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3958cf77-338d-3a8c-ae16-f3679bea4aaf | -16.47272 | -46.479 | 2025-10-23 04:59:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21f30220-12e0-3cf9-970b-cf08772c2d23 | -17.60956 | -46.60913 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2e5a4219-d1d1-3360-a7fd-3c48faad4102 | -17.55484 | -51.04173 | 2025-10-23 04:59:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da6a7d8e-34c4-3c6b-8961-d0cc089af036 | -21.02225 | -48.41622 | 2025-10-23 04:59:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af805290-bfec-3b6c-9e4d-949976470575 | -15.60271 | -48.0539 | 2025-10-23 04:59:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ad0821a-049f-378b-990c-15fe7a746a90 | -18.225 | -47.4208 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 202a4608-82cb-3f8a-95df-30fb5c7a2353 | -17.79272 | -47.62601 | 2025-10-23 04:59:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23d53ec7-24b2-3a2f-b03c-17df9d20ed83 | -17.79194 | -47.62567 | 2025-10-23 04:59:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6acdef9-70e9-387d-b948-1f1ce9ec33d9 | -21.02191 | -48.41956 | 2025-10-23 04:59:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10b14f10-240e-3195-837c-ae7777fff47a | -17.21359 | -47.65592 | 2025-10-23 04:59:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55573578-9c7a-36db-bd5a-cd783800ea0b | -15.67572 | -53.34483 | 2025-10-23 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ead188d-fd18-3977-86b3-88dee5c847ce | -18.72499 | -46.82899 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72e67aba-e849-3983-9010-aaa49308eaac | -15.7142 | -59.13641 | 2025-10-23 04:59:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9759ea74-1a66-39e5-a33d-30ba0407e104 | -17.61429 | -46.61753 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f647368a-a73e-3e8d-95e4-8d282f5bcde3 | -20.26137 | -47.90725 | 2025-10-23 04:59:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 063c7fae-435e-35eb-94d5-2b0e7396d8d8 | -18.71941 | -46.82867 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c732ee22-2be7-3e62-a832-5d8ef2ed3d73 | -14.84144 | -54.22373 | 2025-10-23 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 869276a6-8556-3838-9b2b-01427f4e6578 | -17.60874 | -46.61694 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| aede7d5e-8218-3394-9923-4e037df0a96d | -18.22901 | -47.42131 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7195b34-879d-3c7d-a132-792e46051ec2 | -14.87497 | -59.63483 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e326ca15-08c3-3fb6-8b4b-d5214b93a1c3 | -17.39956 | -47.52171 | 2025-10-23 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 399c9e28-ae4d-3a40-81ec-e2488464eb12 | -16.20753 | -59.32853 | 2025-10-23 04:59:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c4a7cc77-4b81-3b49-aa80-dda1747f84ab | -17.64983 | -46.65252 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7c0f17e1-84eb-3b91-af7d-16774cc27ef3 | -18.72003 | -46.82964 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c2c0b6f-b813-3ed3-8774-0ff8df458a11 | -20.69729 | -55.43583 | 2025-10-23 04:59:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3aa10e6b-13bc-3419-a82a-48722d5727b7 | -18.71963 | -46.83331 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d63ad86a-7931-3928-893f-7e35eb1ef422 | -15.58473 | -49.06601 | 2025-10-23 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7abc439d-0892-3d34-a3f3-5ddba8906576 | -18.71406 | -46.83293 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52cad9aa-bf88-3c48-9ef6-ac2c88f793a2 | -17.60562 | -46.5931 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5107398-6e86-3bb5-95ec-0eae4699d7e4 | -17.60229 | -53.84772 | 2025-10-23 04:59:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39cc61c9-8a16-3288-94ae-b2553850ef7f | -17.61593 | -46.602 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c188e0a2-9fa8-302c-8474-c836a73358f6 | -20.97528 | -47.36399 | 2025-10-23 04:59:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3c5276-0d3f-3e8c-93df-f77cab766d62 | -14.87388 | -57.26446 | 2025-10-23 04:59:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9134a32c-1299-3607-b345-96568f04788b | -14.87444 | -59.63315 | 2025-10-23 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 104a956a-bcb1-3900-9428-817995284173 | -18.22974 | -47.41429 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d589c158-69e3-385f-a520-af0977b41163 | -21.84213 | -43.71387 | 2025-10-23 04:59:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| aa3f73f5-399d-365c-b713-ae69e181e005 | -17.24315 | -46.85196 | 2025-10-23 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 042447b7-8343-34aa-8ae4-5373f47d93db | -17.24276 | -46.85559 | 2025-10-23 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4deb6e4b-5881-3153-aac8-cecbdc25a3fc | -17.14604 | -53.30614 | 2025-10-23 04:59:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1e28b97-65dc-3dab-9499-8f99619a4f07 | -18.22539 | -47.41731 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab91beef-033a-3c1d-99cd-82b27782efef | -17.60793 | -46.62462 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 5ef4b479-afbe-3505-9ce4-4b1756673fab | -17.60874 | -46.61693 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 99281c92-76b8-3dec-b821-ea33007f7a6b | -17.61791 | -46.58319 | 2025-10-23 04:59:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 380bf2df-bea4-31d0-807c-204b4b36cc60 | -17.60359 | -46.61247 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f4c4b88a-00e5-377d-bb22-7e9a4e067bba | -18.225 | -47.42079 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa2e1ab7-6f06-341b-ba0a-7d61f95c1ec1 | -15.60271 | -48.05389 | 2025-10-23 04:59:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9c46df7-acf6-3314-b736-c424ddf0376b | -17.21359 | -47.65591 | 2025-10-23 04:59:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda8f825-3cad-36ae-a7f9-9f5bac342faa | -19.15415 | -49.13062 | 2025-10-23 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc8af46e-4d53-3cd1-8e1a-3137a75df861 | -15.58451 | -49.0686 | 2025-10-23 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3dce042-b195-3c22-834e-906b02e51e2d | -17.61235 | -46.58253 | 2025-10-23 04:59:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8675fe2a-09c7-3111-a130-10d7db9d3c64 | -17.61388 | -46.62141 | 2025-10-23 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3ec34e3f-5091-3b0e-9ae7-5b0bb88d4a0b | -17.39956 | -47.5217 | 2025-10-23 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e13456b1-4989-3eb5-b836-ce6378e74ba2 | -18.23068 | -47.4181 | 2025-10-23 04:59:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea5fee2e-9ea2-3f44-af5d-47a40749f4bd | -18.72003 | -46.82963 | 2025-10-23 04:59:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3cc3f49-2fbc-3b85-b2a7-a474e8d9cfd2 | -3.0168 | -49.4906 | 2025-10-23 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4f10616d-d6b2-39d5-8286-359e8ab44595 | -3.0169 | -49.4694 | 2025-10-23 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ea0a790f-6cb3-3a2f-b288-d5d9e6c2bb7d | -12.0036 | -46.7667 | 2025-10-23 05:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1320116e-c61d-3e54-9ea2-068acd48b025 | -3.0353 | -49.4901 | 2025-10-23 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 92238615-67ff-35e8-ba21-511633931a55 | -3.0354 | -49.4688 | 2025-10-23 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c334b53d-3f39-3bf4-a50c-afde7e2853f9 | -25.22194 | -50.90101 | 2025-10-23 05:01:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 21e803c0-e864-3d8c-9b7f-743f27ed1d77 | -25.22545 | -50.90361 | 2025-10-23 05:01:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ce9d114-45c4-35b2-8a8f-08305e5b5794 | -23.43988 | -47.43438 | 2025-10-23 05:01:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 940f0e5c-d4f9-342b-86ec-dcfc843b1e8e | -22.14537 | -44.83281 | 2025-10-23 05:01:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7ab96e01-844d-34ca-a6c1-04257f2fb381 | -21.44023 | -54.55313 | 2025-10-23 05:01:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README36.md)
