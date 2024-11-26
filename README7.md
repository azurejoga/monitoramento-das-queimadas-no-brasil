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
| 12abd580-c68c-312a-9fe4-b7211fe34ebb | -2.4817 | -45.4221 | 2024-11-26 00:41:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db65bbd9-4944-3077-9a5e-25e4e90f41c1 | -3.7925 | -49.939301 | 2024-11-26 00:41:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b4b439-6586-3d45-988d-22ea1d7ccd86 | -1.4796 | -53.806499 | 2024-11-26 00:41:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3329ba40-4eed-3de9-9f64-19fbba5b6be4 | -3.1901 | -48.4356 | 2024-11-26 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 270c3405-6c3b-363a-938b-261dfbf52220 | -3.1803 | -48.437801 | 2024-11-26 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae1e5d0-9972-3da0-9503-1fca9395868e | -3.1787 | -48.431 | 2024-11-26 00:41:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e438ad4-802f-3ff6-9dc5-a1988bcab9e4 | -3.5953 | -50.3857 | 2024-11-26 00:41:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10c92cd2-0dfc-383e-9df9-520ce39cfeca | -3.9826 | -48.068401 | 2024-11-26 00:41:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94349a81-08e9-38b4-96b5-bfb90b3508c2 | -3.274 | -48.755699 | 2024-11-26 00:41:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87559788-6ec2-3441-b3ab-0ea185d574fb | -1.3497 | -54.6348 | 2024-11-26 00:41:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e901902-7814-3309-a040-d60fac6c207d | -2.8198 | -53.0222 | 2024-11-26 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| daa90243-a8d0-3044-8a37-d668f0770ae4 | -3.9267 | -42.401 | 2024-11-26 00:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 45.6 |
| b961f763-2501-3e93-9caf-74bede0fe098 | -4.6733 | -47.9434 | 2024-11-26 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 2beb79bb-7c35-3179-89a7-6114f7a1676e | -3.5858 | -50.3577 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 25c357ab-38f6-37f1-9d6e-80f14e4909ac | -17.6256 | -57.5897 | 2024-11-26 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |
| 787e9a07-b04d-3bd2-8bdf-921b62fce718 | -2.9238 | -45.1685 | 2024-11-26 00:50:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a6a19bf6-d5b9-34fc-9339-1d5ba1ad7f6b | -3.6043 | -50.3571 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6a447f9c-ec74-39c1-9167-b576f2ac6d54 | 2.6901 | -60.4301 | 2024-11-26 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d13b502c-1bb4-3a73-b356-5c0fa08cd155 | -3.9265 | -42.4246 | 2024-11-26 00:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| f7cc90e5-38cb-39ab-942f-a8206093f851 | -3.8691 | -49.1415 | 2024-11-26 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| c33add14-918b-3733-9805-bda7ee28c39c | -6.0676 | -48.0352 | 2024-11-26 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f8de61fe-9b9f-3525-a2c0-048003c0897e | -3.5857 | -50.3787 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 261.0 |
| 4b1a7bfb-ad50-32f5-8c68-990633960519 | -3.908 | -42.402 | 2024-11-26 00:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 571116c1-d0f4-3749-9568-41125bc7b5b9 | -3.6042 | -50.3781 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 227.8 |
| 33313434-6fe5-36fc-a26d-e84a50f24500 | -1.4951 | -53.8146 | 2024-11-26 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 89e01398-980e-3484-b3d1-676c86337b03 | -6.0677 | -48.0134 | 2024-11-26 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 5aacceda-7d0c-3b53-af9e-a68c4a6acda4 | -4.6547 | -47.9444 | 2024-11-26 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 438e81b6-3635-34e8-8b86-37bb7ee6b996 | -2.8014 | -53.0227 | 2024-11-26 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 772b7d0b-48f9-3a9c-a672-f76c9dc2cbfd | -3.287 | -51.1609 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b60481b2-6397-3541-90b8-441b2231c326 | -2.8017 | -52.921 | 2024-11-26 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| cf498cc6-28cf-39e2-af3e-f5eebf033b38 | -3.8506 | -49.1422 | 2024-11-26 00:50:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d5d8a9f1-7d4d-3a75-bc5a-5d49eb60f409 | -3.9078 | -42.4256 | 2024-11-26 00:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 4e2c7dc5-6723-33d5-929c-1ed235d95ffc | -2.783 | -53.0231 | 2024-11-26 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8eb15514-e1ba-3581-b3e6-663542816401 | 2.6718 | -60.4304 | 2024-11-26 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 81b03b4c-b2a5-3858-87b5-a12b7c80cd6b | -3.5856 | -50.3997 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 18043b6e-3076-3e5c-9301-9b5876435f8e | -2.8014 | -53.0024 | 2024-11-26 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a775796b-b39a-31f4-9b91-bd8491a433e2 | 2.6901 | -60.4111 | 2024-11-26 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5237ab6e-34d8-371c-be5e-851989d10304 | -3.3938 | -44.1722 | 2024-11-26 00:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 002b1e1e-c853-31d8-8b87-0323758a396c | 3.8257 | -59.5896 | 2024-11-26 00:50:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 98157266-b5b9-3ab3-908c-e6911a677c9c | -17.6453 | -57.5874 | 2024-11-26 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 0d3bb256-7417-33e6-b8bb-9ebc7ee765b0 | -3.6041 | -50.3991 | 2024-11-26 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 7fd05c40-5036-3f06-a992-970677a8f624 | -6.0862 | -48.0339 | 2024-11-26 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 163cff21-fe3b-3b94-814b-4f9cdb4f1f8e | -1.4768 | -53.8148 | 2024-11-26 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 259b4f45-c617-3d9e-ab54-8b8f1c14fe1d | -3.6042 | -50.3781 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 292.3 |
| 8373fddb-121e-34f0-951a-60aeeef05d45 | -3.986 | -48.0626 | 2024-11-26 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 231.6 |
| de1ea947-7f45-3ecf-b858-c0cdb77b603b | -3.5858 | -50.3577 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b5e4022e-b637-3317-a0ab-751136d6862a | -3.5857 | -50.3787 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 338.1 |
| beac3c54-beb6-3388-8366-f56717812952 | -6.0862 | -48.0339 | 2024-11-26 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| bd0ad0d8-42ed-39ea-a6ed-382f9853ea45 | -2.8198 | -53.0222 | 2024-11-26 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 1dea2a43-f3e2-37f9-913e-9ff2c380118a | -2.8014 | -53.0227 | 2024-11-26 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 9792d75e-1540-3a11-bd07-40867caed111 | -3.908 | -42.402 | 2024-11-26 01:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 8aacc30f-8711-3537-9891-c368395d53bc | -3.1691 | -48.4394 | 2024-11-26 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| bb562c1c-9b72-34dc-9dbf-e005b380357c | -4.6733 | -47.9434 | 2024-11-26 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1fa4404c-c93c-3973-afab-f3e2be8d41e9 | -3.9859 | -48.0843 | 2024-11-26 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 376fe953-4561-35bc-aec4-2b90f4ffe818 | -2.9238 | -45.1685 | 2024-11-26 01:00:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 27195a8c-c08a-362f-8940-a2f2313b5baf | -3.1875 | -48.4603 | 2024-11-26 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1b29549f-a07a-3f44-8ebb-5262ddd548e6 | 2.6901 | -60.4111 | 2024-11-26 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| aa5ce449-b964-3a5e-8783-0ee5008cdfb6 | -3.287 | -51.1609 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e102eef3-9b85-3fa7-a198-c6d66477f15c | -3.9078 | -42.4256 | 2024-11-26 01:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 685de4e5-ad37-3bf5-a488-08fb99c1f09b | -3.76 | -52.6491 | 2024-11-26 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| eac64012-6a71-3fad-89ca-e66b05a067fd | -3.2907 | -50.2627 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7efab096-6f62-3179-ae41-b85a50ac1da5 | -3.6041 | -50.3991 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 5b2bec72-2c34-34de-af58-c58a68565584 | -3.9265 | -42.4246 | 2024-11-26 01:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 6fd7ba84-a889-3266-903c-fba2a20262c1 | -2.783 | -53.0231 | 2024-11-26 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ccabade2-9e27-312a-9df3-3b9f4764f335 | -3.1877 | -48.4172 | 2024-11-26 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| d79788f0-aa2e-35d5-9bec-65197191f686 | -3.9267 | -42.401 | 2024-11-26 01:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| dce2d696-92b7-3679-a5f1-cb13929c683b | -3.2061 | -48.4381 | 2024-11-26 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 35be67b0-ae55-3a42-a4be-96449f9b3a0d | -3.1692 | -48.4179 | 2024-11-26 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 42a100d4-53ac-3cb6-9a6a-a218e7636223 | -2.8014 | -53.0024 | 2024-11-26 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4ee1d859-1e85-3646-9fad-9fe94437b911 | -3.8691 | -49.1415 | 2024-11-26 01:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| f36eee45-fa0d-36df-b0ff-9e907c24e7cc | -3.6043 | -50.3571 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| dc8e9863-ae8f-3228-b2f3-c7852613dcfc | -17.6453 | -57.5874 | 2024-11-26 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| c50ecedc-9ce7-31d7-bca6-fae26c0fd2dc | -3.9676 | -48.0418 | 2024-11-26 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 03adc609-47d5-39a2-857b-2db659c4816d | -3.3938 | -44.1722 | 2024-11-26 01:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 45271725-a8ed-38bb-998d-7fa204de4c2c | 2.6901 | -60.4301 | 2024-11-26 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.8 |
| cc637e18-d870-37a9-8ba3-e76f5d96472e | -3.3752 | -44.173 | 2024-11-26 01:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 6f1411ec-3e98-30ac-b73f-2f4a87d160c5 | -3.9675 | -48.0634 | 2024-11-26 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 297.2 |
| 22aeb7ee-df8d-37fa-bcfe-30e51a1cc7b1 | -3.9861 | -48.041 | 2024-11-26 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 61ede8e7-563f-3708-a359-34325e796958 | -3.5856 | -50.3997 | 2024-11-26 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 9bfb7549-0298-39f7-a30d-001a3e13e60f | -3.1876 | -48.4387 | 2024-11-26 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 258.5 |
| 241bc54e-084f-3fa7-8e7c-6327ec9984e1 | -2.8013 | -53.043 | 2024-11-26 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f3b803c1-ea8a-3245-bd4a-40701f49b022 | -6.0676 | -48.0352 | 2024-11-26 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 2782352e-d918-3f25-a7e1-63dd4791395f | -3.3939 | -44.1492 | 2024-11-26 01:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 888fcb7e-1d41-3c68-934f-eb5f0f8f679e | -4.6547 | -47.9444 | 2024-11-26 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| ee4ad9a2-48f5-339e-a569-5eddf09908cd | -3.9674 | -48.0851 | 2024-11-26 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 2180ed7e-6537-3076-8d3f-896ea095d19c | -2.8017 | -52.921 | 2024-11-26 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 32b3b5c2-88ff-3f0e-89a9-def837fd14ad | -3.19 | -48.42 | 2024-11-26 01:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8f6a27-61c2-33c1-9ddb-0c524da1b69b | -3.97 | -48.04 | 2024-11-26 01:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2faa5da-63dc-3607-982d-16f5089ac25a | -4.0 | -48.04 | 2024-11-26 01:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45bb4c0e-7cd8-351e-a854-a7df8718a33f | -3.2419 | -53.2954 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e95c5320-d7f2-32af-aa15-ef3bcfc64ad0 | -3.6041 | -50.3991 | 2024-11-26 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| ae5d4435-e482-377b-9e16-30058d0b57d7 | -3.2604 | -53.2746 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e04b89dc-6643-3a73-9a73-c13a331ac247 | -2.8013 | -53.043 | 2024-11-26 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 45f0d5d2-44a6-376a-8ae4-13df43609f8c | 2.6718 | -60.4304 | 2024-11-26 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 925e7be5-3219-3fed-8b36-6fd7301ad569 | -17.6453 | -57.5874 | 2024-11-26 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 6fdba9be-03fa-362f-8ade-f3081dcf9ded | -3.9078 | -42.4256 | 2024-11-26 01:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| a4f170b6-0757-35b6-8b3c-38e42c2e9eb3 | -3.908 | -42.402 | 2024-11-26 01:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 8ca5528a-3e33-390d-9e37-35d68027b034 | -6.0862 | -48.0339 | 2024-11-26 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 71e82360-f666-38ca-8b93-6bc2a6242915 | -3.1876 | -48.4387 | 2024-11-26 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 48bdd0bd-4c88-3a83-8b39-e57c55c6d813 | -1.4951 | -53.8146 | 2024-11-26 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |


[Clique aqui para ver as próximas entradas](README8.md)
