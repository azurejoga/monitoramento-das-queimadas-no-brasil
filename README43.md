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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30895855-7f50-3311-8aa2-52c6959561fd | -7.4082 | -42.6442 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0982e1bb-2207-3113-9a04-317db8e1f281 | -6.6109 | -43.74621 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4d37ebe1-73e8-3d2d-a30c-258e7e3ab24b | -6.42778 | -43.72697 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 440f3486-9e45-3c0b-a5da-1cde4c635d8d | -6.62271 | -43.74465 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 321eb8d5-1026-3160-88c7-e04320136146 | -6.80883 | -47.88177 | 2026-09-23 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4fd3333-3be7-3443-ab4d-157cc27e94cf | -6.98428 | -42.59891 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 564fb295-4cfc-3529-b0d2-7be45afe573f | -6.81334 | -47.88083 | 2026-09-23 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7849e7ec-56a0-3192-bd96-9341a0794f1a | -5.27835 | -47.25668 | 2026-09-23 03:42:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a76698b-b09d-3a38-a2a7-3a5ac9432634 | -6.33878 | -43.36634 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3e2da45-bf83-3105-a526-096a9dc06723 | -7.13065 | -43.07833 | 2026-09-23 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96207572-cb5d-3229-9a2d-65b2b10af047 | -6.61365 | -43.76285 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1bbe224-8c75-3ac2-a485-04ad2adf9011 | -7.65133 | -45.44446 | 2026-09-23 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d9b71b6-08cc-3178-9170-45927476c618 | -6.89845 | -43.63237 | 2026-09-23 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff8fd08-9fb4-39b8-9be1-3ce79cd87d69 | -5.77442 | -47.16419 | 2026-09-23 03:42:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4c33019a-f532-30f3-8d79-34246281a077 | -6.61646 | -43.74731 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 7580b9f8-49de-34b6-a5a1-30697b730a53 | -6.59974 | -43.74417 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4a936e21-4503-3e16-80be-52a19d09976c | -5.34593 | -45.17363 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5fd0b933-938c-35a3-ae74-61ce6259b34f | -6.89703 | -46.55268 | 2026-09-23 03:42:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1612b7ed-f59c-356d-906a-e6d38e4ff9db | -6.81462 | -47.87396 | 2026-09-23 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbda5e65-f6c0-3d4f-ab23-44a2a82baca5 | -5.61863 | -45.24239 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4b00e62c-ad82-3dc9-b645-5b5c6870d31b | -7.1642 | -45.81144 | 2026-09-23 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adba6f4c-ff06-39f7-af59-2bdb239c400d | -6.72261 | -44.15351 | 2026-09-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4bdf0bae-5c95-3969-841c-6fc2c326ad22 | -6.59555 | -43.73554 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b480e4d-ca25-33e2-bc2f-82ccdb7d8038 | -6.33815 | -43.36998 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e25ad1b-b9f9-3bcd-aa7c-8efe0ee4f5ff | -6.33926 | -43.36695 | 2026-09-23 03:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d30370f-d36c-3e6e-b37a-78dbbaa79e37 | -6.61782 | -43.7398 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 59650e2d-c184-37c7-9251-db238ef4c993 | -6.97915 | -42.59797 | 2026-09-23 03:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31c3a370-9c8e-397d-a9e7-e0e407d5ae6d | -8.8183 | -37.34813 | 2026-09-23 03:42:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6c08a84-9814-3a4b-8142-e31e5a9cb11d | -6.60145 | -43.74545 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 87e6d857-9d83-3df8-a227-a5492493a81e | -7.02631 | -44.65047 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b5fc4698-ae73-3c75-a748-89c596216297 | -6.61296 | -43.76664 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8549d90-a5b9-32f4-8947-13459c62bccb | -6.60807 | -43.76182 | 2026-09-23 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8bb8e38-5e90-3db7-a5a5-3e5c79d348d9 | -7.03141 | -44.65579 | 2026-09-23 03:42:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b280b8c2-766e-3185-a9c8-077f1a886baf | -5.7616 | -45.11378 | 2026-09-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1e9c8f93-0dc9-3ff5-8ef3-0988762a1e92 | -6.89292 | -43.6314 | 2026-09-23 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea538b29-4e76-3bde-b481-ce12bab15cc0 | -6.81019 | -47.87473 | 2026-09-23 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fc9f619-a1c3-3bab-9bf2-c66230c7111f | -6.32416 | -43.9344 | 2026-09-23 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 87e62c09-bcc0-33fb-95e6-17c4f7e63747 | -6.91075 | -41.69374 | 2026-09-23 03:42:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fd5379dd-f30a-3588-b3a9-71a047e3e2bf | -6.57896 | -44.14966 | 2026-09-23 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50ac4e68-353a-3af0-bb80-14716a64fd1c | -5.60333 | -44.02769 | 2026-09-23 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c86151c8-0eea-3f4f-bab0-72da93b42be7 | -13.29222 | -47.89491 | 2026-09-23 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863c0159-15cc-3c99-98a1-1473efd66887 | -14.62298 | -45.65487 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 071c5769-91ca-3a88-855c-2fc0d4da0ef5 | -9.99854 | -39.17091 | 2026-09-23 03:45:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7b51ff06-2b3b-3780-8164-39d50f3c3f15 | -12.42348 | -46.97539 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 920d3720-9754-34c9-837a-ef331c4b6535 | -11.87831 | -45.7667 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ecc847e7-414b-320e-b68b-f5670e365a4d | -11.6908 | -43.45231 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560bdbb6-c1ab-3c88-ae6a-18dee185ff35 | -8.3193 | -46.88184 | 2026-09-23 03:45:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de4d5173-b76b-334c-b055-94181917831f | -11.26007 | -43.41078 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a2b648d-9ffd-3ecb-bfe0-b60e32b9099f | -11.65516 | -43.47589 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 813c5681-1975-3430-bcfe-a5fe2187b400 | -12.42448 | -46.97045 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85e167b0-d30b-3277-b5e6-91455e17378b | -8.59695 | -44.5378 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89b5e2d0-4a9d-39f7-b660-206107958fc1 | -8.08518 | -44.34839 | 2026-09-23 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2edeefe4-3bbf-3718-8d64-8368b90b7836 | -11.13474 | -42.7821 | 2026-09-23 03:45:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 147f8ac5-aa0e-3d88-b4fc-59dda3473cef | -14.74888 | -47.15462 | 2026-09-23 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9b1cd1d-cc99-349a-bd04-4efde6b6f7f1 | -11.88908 | -45.77319 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccf67279-2304-3d04-9ac3-0ccc1c474134 | -12.41528 | -46.97525 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ca90e169-030a-3872-a402-5bb56180368d | -8.48365 | -44.7554 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fba04f4a-4612-3c29-b3a2-88165fe0cbba | -13.93782 | -47.83811 | 2026-09-23 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75058539-84ba-3a23-a75b-e8b5cc79dcaa | -11.45173 | -47.39166 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e02fbf0a-14c3-38a3-acea-0b28bee9eb17 | -14.75583 | -47.15132 | 2026-09-23 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e42fc34-f434-3d28-ad44-cd4e23320b6f | -8.60063 | -44.53967 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6ad936d-7beb-3f60-b163-5c550f95ef06 | -11.46761 | -47.37943 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7e5b17e4-b5d6-36e0-86cd-2170405e7eb0 | -8.75807 | -45.84489 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 023d3fdf-3d50-3c5d-a4a9-465de68bbdbf | -11.46678 | -47.38462 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b99acdf1-bdc7-3073-a0df-cb8329d66ea6 | -10.71499 | -48.71689 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79163bb3-6451-3782-9d26-11e7081ff4bd | -10.00598 | -45.19064 | 2026-09-23 03:45:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d4fcbed-f4ac-361f-9453-b06a7aebabf3 | -14.96652 | -47.54094 | 2026-09-23 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7adf7a08-c550-3554-8bae-f349b2417983 | -14.75388 | -47.16066 | 2026-09-23 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2157f7fb-d9c4-376e-a9d6-710f8d000195 | -11.4682 | -47.37785 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8f71ce17-b5cd-3ce8-85f6-72f78e287bd7 | -8.80264 | -44.26633 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 384c07c6-b826-3c74-a7fc-0129bd4a7576 | -10.49907 | -44.87541 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07aca46c-e7a8-3a57-9397-4c162a065202 | -8.35888 | -45.61512 | 2026-09-23 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2e67223-3999-3b87-8d63-749a06b0b8b5 | -9.57945 | -46.5364 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac111c50-9b87-3c07-970b-3996d900de4c | -13.85183 | -48.58403 | 2026-09-23 03:45:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 921dea6a-08b2-3e9e-b1bc-87e72d56c954 | -15.63073 | -43.52209 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f8700247-d6b5-33fb-be2c-a06dfb31bb85 | -11.87914 | -45.76252 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b9a6de20-f3bc-3fa8-8633-cbd0d133b2fd | -13.21839 | -47.02616 | 2026-09-23 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 55e6f834-e612-35f8-b341-360f6c0de5ee | -10.50391 | -44.88049 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b782ed41-2bcb-3cfb-a53a-3a0df9a657c3 | -8.81316 | -44.27168 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| adae3ac2-8477-371b-b8ad-78865a906a58 | -8.12371 | -44.43819 | 2026-09-23 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da204a6-ddcf-3189-8da4-132caa3bf594 | -11.4317 | -47.39117 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f1cb52c-32c9-3960-abd2-c54fe1bf3466 | -11.52636 | -45.35891 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93ca6041-c373-3ad0-89e6-41f348f2e120 | -8.76399 | -45.84256 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b6ce9ef-d154-31b9-ab56-d05fab3426fa | -11.46255 | -47.37135 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6780231e-7e7a-32de-97aa-081b74248f4d | -8.08759 | -44.34879 | 2026-09-23 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 481f039d-ecac-316f-92c2-92250462da6d | -11.68022 | -43.4533 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa4a483c-8e63-375c-8052-1bc73bf21ed6 | -13.91879 | -47.83422 | 2026-09-23 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aac41689-f9c7-3c00-9570-cb95ae29ea3e | -12.41631 | -46.97899 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31589f2a-c8e6-3a03-9899-16f29b9a0864 | -15.62757 | -43.52978 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1997b64e-ed6b-32d3-a8c7-da91ed29dc89 | -11.29288 | -44.04177 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1b32567-ab49-36d7-8683-1e60201ba605 | -10.82153 | -48.47639 | 2026-09-23 03:45:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51651ef1-3da1-3170-99c7-a93c5be35b4a | -15.6287 | -43.53244 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d8d30fb-40ca-3e26-a305-b12de3c6d279 | -11.68524 | -43.45427 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 909d3d1d-d0d2-3c02-ba6b-a046697defff | -11.52718 | -45.35469 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49d8f2ff-74a1-3306-b126-c2dc7e5dcdf2 | -9.83669 | -46.38532 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d3346c6b-5b85-3968-a7e4-69d3ff21e50f | -15.62855 | -43.52458 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 232efdf9-cecd-3fc9-9174-d35c749fab23 | -11.44312 | -47.40101 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a902057c-6ca7-3992-9559-3516fa659ef0 | -11.43281 | -47.38576 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01c475c3-d7db-374b-a2e8-a272c0110420 | -12.11778 | -45.64805 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 226d78eb-00e3-3267-8554-70f982701c10 | -9.71169 | -37.27474 | 2026-09-23 03:45:00 | NOAA-20 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README44.md)
