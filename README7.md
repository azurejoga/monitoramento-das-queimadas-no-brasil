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
| 89a1bb02-709e-387b-80c8-ca249ad4ecb7 | -11.73241 | -54.3079 | 2024-12-06 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b67a2b3-bbfd-3682-8eae-96cd76a87587 | -6.85431 | -47.31936 | 2024-12-06 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71071f35-541c-380d-8c88-a8475ca1036a | -15.57065 | -47.85506 | 2024-12-06 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63809d3d-f7e5-3135-970d-9048a5b6732d | -15.57087 | -47.8569 | 2024-12-06 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 824c2c7f-96b2-3e6a-a123-9f2afe42a39a | -28.72699 | -52.85126 | 2024-12-06 04:57:00 | NPP-375D | ESPUMOSO | RIO GRANDE DO SUL | Brasil | 4307500 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9fd56a84-f4b9-3246-9b47-2a15b61cd9f8 | 2.01904 | -61.46953 | 2024-12-06 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de3dbe46-9fde-3d7a-bfa5-178aa59d8713 | -1.44914 | -45.94058 | 2024-12-06 05:12:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 386c5136-d8c4-304a-bdf5-bd25fca7880c | 2.47926 | -60.69466 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92e00125-4c56-32ef-ba01-7a78ad922674 | 3.23559 | -61.03196 | 2024-12-06 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 07121f81-f36e-3e14-8a05-e9e4ac286d10 | 3.23632 | -61.03674 | 2024-12-06 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dbc2cca-395b-3ec3-bd00-f000b384cf71 | 4.32326 | -60.79063 | 2024-12-06 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 717b291b-e8fb-3133-b50f-35a38b2cbc3e | 2.42543 | -60.65019 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd66dafb-7be2-3886-998c-7eb74b97ae60 | 2.62391 | -60.4102 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc5a821a-5216-390c-b64f-8aba7b952e24 | 3.82205 | -60.41679 | 2024-12-06 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1580795-d748-3666-8e18-060ae7377211 | 0.75064 | -59.66219 | 2024-12-06 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fec2679-3914-326e-9a5d-4746d3ab7ef3 | 2.42474 | -60.64571 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc2926b-94b4-3479-8389-383f1772dae1 | 4.53048 | -60.80872 | 2024-12-06 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1afa2576-fc0a-3a73-b307-05bb6f6d119b | 0.85464 | -59.77015 | 2024-12-06 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e94ec2-a171-3f28-bb29-30d6da122806 | 3.5806 | -60.68435 | 2024-12-06 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a1c2b80-81cd-3a80-b073-f57aae98508e | 1.52707 | -60.67329 | 2024-12-06 05:12:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06a0da57-6bc8-3379-bd9c-50725a571570 | 2.62652 | -60.41172 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffdc2bef-cd9c-3d24-82a6-5636abdc9fcc | 0.70507 | -59.87952 | 2024-12-06 05:12:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e8fb09f-a960-3ae7-97d3-d31e21971b66 | 0.75351 | -59.65777 | 2024-12-06 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 676e4c9b-333f-39b0-8cb2-e200aa8b2dfa | 2.47858 | -60.69012 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6df20707-8b0c-3b89-933d-881079049b52 | 0.62617 | -59.65282 | 2024-12-06 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f056b1f8-a6f7-3f97-a954-25dd81092fee | 2.42917 | -60.64959 | 2024-12-06 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 403bc911-9038-3289-bbaa-f8f462689c4a | 3.8258 | -60.41622 | 2024-12-06 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc7b6d5d-9402-35ed-9714-06c437473e80 | 3.45306 | -60.53197 | 2024-12-06 05:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b2f15d6-815b-3582-a9cc-2bf2057ce597 | 0.75003 | -59.65834 | 2024-12-06 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f455359a-a0c6-3a5d-bcca-aa3a1782dc4a | 4.32398 | -60.79549 | 2024-12-06 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2e98f45-f832-360a-a7fa-02cb170c294b | 3.24019 | -61.03617 | 2024-12-06 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 894afaf8-75b9-3a2d-9c1f-33f95718d599 | -2.74615 | -54.16079 | 2024-12-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f6c3cf5-3c7c-32de-ad98-f4196afd2bcc | -2.52594 | -53.9823 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c63373b-1299-3529-a7f4-e4bfc4396721 | -1.67702 | -52.55667 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88deeb25-8506-318d-bc0f-d3ddf6bc555f | -2.24482 | -53.84762 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 971b8537-d90c-344f-acf2-313e1b20c53c | -2.61873 | -54.00906 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cdc204d-541a-3ea4-b3f9-5ae2b85df25c | -1.67328 | -52.74229 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70c3f3ba-bcd8-322a-b200-f489c3f20f65 | -7.08496 | -45.20922 | 2024-12-06 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd3623b8-2e60-334b-a68c-31417cfe9248 | 0.20032 | -60.60935 | 2024-12-06 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b0604af-2c94-3788-97f9-65cd6a88166d | -7.08409 | -45.21611 | 2024-12-06 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1724547d-abbc-3a9d-96cb-7b1637ac3c67 | -3.19363 | -54.62947 | 2024-12-06 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eff0814-8ce5-332a-8065-5bb9004c4d22 | -1.72477 | -53.18631 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e9ed809-6e30-3a5c-8670-23445fd5e819 | -1.81011 | -53.04714 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 670f5125-f235-3a4d-ad28-b1cf15644779 | -1.69434 | -52.79218 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76d8e490-29f8-3b0e-8850-dd1488c34707 | -1.7224 | -53.17579 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11e5df17-1f8f-3305-8e8c-7e5a000c150b | -1.67183 | -52.56329 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a794d532-a278-30b4-a206-fa475801b791 | -8.02393 | -47.68877 | 2024-12-06 05:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebae1718-9cfd-3b2c-8c3f-696e4ad1a1e7 | -2.46959 | -54.11926 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d524f1fc-6a2e-3577-aced-0d1dbaef71f0 | -1.53728 | -52.682 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12806ab4-82f2-33be-8686-71f71e4f9c95 | -2.61132 | -54.23392 | 2024-12-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e100a3b-72d7-3623-873a-0f392a07cd3b | -0.66715 | -58.0389 | 2024-12-06 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1429959-60d9-3c71-a439-5f68522b6040 | -1.71042 | -52.79463 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e790db0-b54f-3183-9d3b-ebaa43373fa9 | -3.60244 | -54.55249 | 2024-12-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c662c1d9-13ba-382f-b382-a46398117ca0 | -1.69721 | -52.61504 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9f987d9-63f0-3c9d-b83b-a6fd3dc9fbb5 | -1.69944 | -52.60069 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 389ce0fe-2336-3b27-9300-663c5a519372 | -2.42827 | -54.03916 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc73c0ce-1f1c-3b4c-91cc-fc0d32450ba4 | -8.01771 | -47.68793 | 2024-12-06 05:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e9bf960-37cb-389a-abc4-386d8d342248 | -1.67481 | -52.57113 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f228047d-556d-3533-99c8-a2ddce8ead82 | -1.68 | -52.56453 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd0bccf2-fa1c-3532-8a72-2c8c4fb79b3f | -1.68923 | -52.79855 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 199587a0-fc5c-3b59-b445-58f687abc09b | -1.67239 | -52.55967 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0782825a-5bcd-3811-966c-4bee5e821394 | -3.82052 | -54.75909 | 2024-12-06 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b67c4aa-ce9e-3e87-8a11-664d1e07b1eb | -1.47009 | -52.68309 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ef3a3ff-4cec-327d-a451-91d2fdebcbe0 | -2.36585 | -53.9157 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84437b3b-c80a-31e3-9d04-ab4758d38a9b | -1.67591 | -52.56391 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 859bf273-5650-3143-8f02-d88a0fdf40b4 | -3.60614 | -54.5531 | 2024-12-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba54dc13-4e4a-3853-af4c-3ec5d24027d8 | -1.01415 | -60.29522 | 2024-12-06 05:14:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0badaf90-04ba-346d-b792-6d11cb2ea78f | -1.72555 | -53.18135 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afaebf1d-cf80-3de0-8bf6-72fdad718a7f | -1.68055 | -52.56092 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0ad3e1c-d7cb-31e6-9495-81febecf3f62 | -1.66925 | -52.74168 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1af7c90d-0802-35dd-926b-07fd6f58ca63 | -1.65901 | -52.75452 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b704c68-0aee-3de2-bf3c-41774f300656 | -8.27348 | -48.03019 | 2024-12-06 05:14:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89992852-c3ef-3710-bedd-200c42403d5d | -3.1973 | -54.63005 | 2024-12-06 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfc92a20-f958-36da-9602-acaa622e4a6a | -2.28831 | -53.79292 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d948fa-c250-33cb-8c2d-369a68998480 | -1.67128 | -52.5669 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ead35d75-2199-37c7-a264-7701ae8be707 | -1.66304 | -52.75514 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abf2a364-93db-34c4-be18-5d5441b2df37 | -3.18493 | -54.51294 | 2024-12-06 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6c4fe18-8f96-37b7-80d3-1c5e16eb836e | -1.70127 | -52.61566 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e02b6046-bcc9-3ef2-832f-aa8efd3bfc40 | -1.69275 | -52.6437 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0be8ecc8-e9e9-3d66-bcdc-f3faecb6e0ec | -1.69168 | -52.57001 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 356ff652-92b4-366b-8dd5-d3e243d92993 | -1.6952 | -52.57425 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eba8b994-f8ab-31f1-bcb0-6a38af1303c5 | -1.66871 | -52.7452 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af8f7ee2-a478-368b-8378-747d5da1d07a | -1.67425 | -52.57474 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a0c72ae-b809-3051-96b4-0aa35b7171cc | -1.78424 | -52.75237 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2048d0-0235-3a4a-9ef8-051eb5a8051d | -1.70071 | -52.61925 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c9b5f4-6378-3ece-8442-7d5fec61d7d8 | -1.78773 | -52.75651 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e3bd0c8-f3e7-3b1d-a124-9bf285c256db | -2.44615 | -53.82111 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a359229-b7eb-3c84-b8d8-2a469024cc5e | -8.02506 | -47.69099 | 2024-12-06 05:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0561869-e8f2-3852-9f71-4bbd9c2c4283 | -1.67536 | -52.56752 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e2bec93-13c8-34d1-800e-cf2ba1992077 | -2.45249 | -53.63687 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4c92ceb-42a8-3c38-86e0-a4e184294883 | -1.68111 | -52.5573 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff24ba45-4875-38d9-9d67-c6934d9d8504 | -1.66816 | -52.74872 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c192f62-bf06-3c93-a5f9-1abf00e66636 | -2.27116 | -53.82809 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aaa2ce7-11b7-3631-bb68-dee3661b9677 | -3.82419 | -54.75962 | 2024-12-06 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f7f60d2-ddc9-3afa-b7fc-68e3e1e5732a | -2.52217 | -53.9817 | 2024-12-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 271fef22-ade2-37db-8f5f-a4c705466a73 | -0.15585 | -60.86808 | 2024-12-06 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d163ba4b-a10a-3901-8dd2-e2fe48033770 | -3.74798 | -54.74504 | 2024-12-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16cc752a-279f-357c-8ff4-7405b3c63446 | -2.60759 | -54.23339 | 2024-12-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b883239-1584-3a61-9534-cb4ad8799ed7 | -1.67647 | -52.5603 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6acc63e9-235a-353a-a17b-27cd0985c116 | -1.66761 | -52.75224 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)
