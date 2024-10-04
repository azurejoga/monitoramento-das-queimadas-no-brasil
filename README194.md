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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b879c9a4-62c2-33ef-a4e2-838fd3ba7d7c | -6.6169 | -45.1767 | 2024-10-04 13:55:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c57f6091-6518-3c03-96e5-6f2ad4b47972 | -6.6339 | -45.3565 | 2024-10-04 13:55:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3b5c7ea0-653d-3ede-ab8e-aae2ee2f1985 | -6.929 | -47.6901 | 2024-10-04 13:55:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 6cc21198-f7e0-3006-9881-20d3377e0c0c | -6.9479 | -47.6668 | 2024-10-04 13:55:46 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| bd96dcb5-308a-3a21-96d3-147163341930 | -6.9477 | -47.6887 | 2024-10-04 13:55:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6dc1e15d-8429-30b7-852c-d7c5a8e40aa9 | -8.1759 | -43.6957 | 2024-10-04 13:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 6ffca6e0-1056-3bc2-8ece-9d5e357a38f0 | -8.1762 | -43.6723 | 2024-10-04 13:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 474d84c5-7adf-363a-a82d-294406df9b48 | -8.3194 | -42.8343 | 2024-10-04 13:55:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| c910abb8-aca6-3416-9ff0-a8f6bda7984a | -8.3128 | -49.5679 | 2024-10-04 13:55:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ad2794c9-f0bf-3267-8464-022cb74b7d4d | -8.3316 | -49.5663 | 2024-10-04 13:55:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e0d3b83d-2e8e-3c04-baec-3502d86a7003 | -8.2859 | -45.4317 | 2024-10-04 13:55:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 5f07939e-af9c-3dbd-8784-f8fe511dfd44 | -8.4347 | -47.1199 | 2024-10-04 13:55:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 5c0ff933-3b1b-35f7-a5e1-8ea68c8b819f | -8.742 | -45.1563 | 2024-10-04 13:55:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 233fc108-5bbc-31a8-b28f-44a0899290c3 | -8.7423 | -45.1334 | 2024-10-04 13:55:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 82880a74-881e-30bd-9c84-ebeab69beff8 | -9.8855 | -47.2124 | 2024-10-04 13:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f4c5f159-8d5d-3c00-ac40-0de4725eee7d | -10.2381 | -47.7038 | 2024-10-04 13:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b596689d-9ba0-333e-a081-1fcf8db04b51 | -10.2192 | -47.706 | 2024-10-04 13:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| f3ceed42-0eb9-3646-9814-2ddef8262602 | -10.2378 | -47.726 | 2024-10-04 13:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c2c5f595-b7df-3877-a548-78ac9cb03ccb | -10.2574 | -47.6796 | 2024-10-04 13:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 22ff3821-dd80-3454-a70e-fcd5c8c42409 | -10.5929 | -48.0597 | 2024-10-04 13:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| ca481ed6-81dc-3bca-8a2f-aafe1c995b40 | -10.6367 | -45.2027 | 2024-10-04 13:56:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 304bd864-645d-37c4-8c36-9264c8ce5fb8 | -10.6119 | -48.0575 | 2024-10-04 13:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| c1ac25a2-601f-3943-a6dc-dc80c0ee76ff | -10.7322 | -47.6239 | 2024-10-04 13:56:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| d7cfae19-cae6-3342-9e98-7c76294dd0f5 | -10.8216 | -45.5444 | 2024-10-04 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| ddf05302-16e1-3851-aebe-375ab7dbbca8 | -10.7359 | -46.1465 | 2024-10-04 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| b7273730-582d-37f2-a1ae-900b31c9d0d3 | -10.7355 | -46.1692 | 2024-10-04 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 5eab8355-f189-37a7-918e-3de7e403e2fa | -10.8021 | -45.5698 | 2024-10-04 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 394d49ce-518a-3aba-bab4-fc2c93e6c272 | -10.7309 | -47.7126 | 2024-10-04 13:56:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3a673c90-dc33-3250-a50f-77c9f7220d7a | -10.8018 | -45.5927 | 2024-10-04 13:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 7db6110d-5f37-34fc-89be-bb82064acaf7 | -10.9187 | -46.6192 | 2024-10-04 13:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 6f0d252e-4409-3707-b9f3-8d7d2a30cf3d | -11.2376 | -46.9148 | 2024-10-04 13:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 97474b84-039e-3f39-a300-20aaad6cdb25 | -11.2971 | -43.4088 | 2024-10-04 13:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.4 |
| d042bcf1-a302-3f62-9316-236709c97544 | -11.2783 | -43.388 | 2024-10-04 13:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| a818ae10-8830-3d65-b355-947c6d0fab7d | -11.2369 | -46.9597 | 2024-10-04 13:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 54a519bd-c7f8-3117-afbf-5a5a171310d6 | -11.3853 | -47.2088 | 2024-10-04 13:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 13d99f4a-2b33-3a5d-8c90-f6dcdb9b585a | -11.3849 | -47.2312 | 2024-10-04 13:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 6fbbee1b-2502-3d6f-a8dc-96f3796c6c81 | -11.275 | -46.9548 | 2024-10-04 13:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 6584625c-b704-3e12-b866-5df174f6cdff | -11.4043 | -47.2063 | 2024-10-04 13:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 29519856-e5d2-3a48-b6ff-52031a74da18 | -11.4622 | -50.9021 | 2024-10-04 13:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d415a4f4-4475-3d48-8aed-c445304d4200 | -11.4743 | -50.0667 | 2024-10-04 13:56:11 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 3b707c42-c63f-3d38-98f9-443f584990df | -11.4746 | -50.0452 | 2024-10-04 13:56:11 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 76ea8009-49fa-3857-a8c0-75c4ba15c321 | -11.6804 | -47.8156 | 2024-10-04 13:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 97ffffa0-f715-309e-9b58-ecf31386f33b | -11.7415 | -49.9925 | 2024-10-04 13:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 89256954-34f5-3320-9b98-d4f6a19f5d65 | -11.7412 | -50.0141 | 2024-10-04 13:56:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| cc9bc9de-a37d-3cd5-a512-dcb9adc2e8ed | -11.9483 | -50.1618 | 2024-10-04 13:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 98d5b8ca-f0db-3a52-9bcd-d873a933cf22 | -11.9487 | -50.1402 | 2024-10-04 13:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 85c18df3-9298-319c-8c03-632bbf90b836 | -11.9296 | -50.1425 | 2024-10-04 13:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 6e7a378e-0327-3423-abf7-2663d36fdd56 | -12.0124 | -47.371 | 2024-10-04 13:56:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6b47fedb-182a-36bc-8bd5-8c789d13f0d7 | -11.9862 | -50.1787 | 2024-10-04 13:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f94767d4-2b3e-3016-8c55-5c00edfe4acd | -12.1533 | -50.4595 | 2024-10-04 13:56:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e53ef674-69fd-3d6f-b700-075dfbf2135c | -12.7815 | -50.5758 | 2024-10-04 13:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| edd6e542-2b53-3165-80b6-5a26df28af94 | -13.199 | -45.492 | 2024-10-04 13:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a1d03172-91bc-306a-bc18-dcc80f9297d8 | -13.1779 | -48.6737 | 2024-10-04 13:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f69338fa-c698-35e9-bb19-33964b97a08d | -13.1443 | -46.3261 | 2024-10-04 13:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e4db2f4d-035f-3551-aaab-bcfffb02ca92 | -13.1447 | -46.3033 | 2024-10-04 13:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 02b280ea-5159-3a7c-aff7-ec4d8ddc01c1 | -13.1787 | -48.6295 | 2024-10-04 13:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a827905e-f2a6-322d-9a60-f173b093ca4c | -13.5255 | -48.6018 | 2024-10-04 13:56:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 091c240a-f823-3206-bb97-57ee9188ea5c | -14.0378 | -45.1648 | 2024-10-04 13:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 315.2 |
| 1278452b-555b-3805-bdac-93381bedbc9b | -14.0382 | -45.1414 | 2024-10-04 13:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 270.2 |
| 1f4a1df2-bc52-3dee-b70d-447272dca043 | -14.5876 | -40.7321 | 2024-10-04 13:56:27 | GOES-16 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 861c554b-8038-322e-96a5-0ca0ffe4d230 | -14.5362 | -49.2898 | 2024-10-04 13:56:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 93277000-120d-3797-87d8-8a4fb7ca257b | -14.7017 | -48.7559 | 2024-10-04 13:56:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d6528ece-d695-3199-a2b3-90c8f993e8d2 | -15.4247 | -47.6736 | 2024-10-04 13:56:32 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 62fc163f-e23f-3e7e-bcf2-2e2f37ffe8b4 | -15.6304 | -47.2063 | 2024-10-04 13:56:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 00f66ba4-59d0-365b-b726-769fce09f3a8 | -16.8626 | -57.4744 | 2024-10-04 13:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| ffe23e27-2627-32b9-9a9e-99e09a988780 | -16.7985 | -57.8284 | 2024-10-04 13:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 4b7177ae-80d5-3f24-983e-6b1e33fd2452 | -18.8613 | -43.5837 | 2024-10-04 13:56:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.6 |
| 96031ad4-7fd5-3129-8799-ce381619e35b | -19.6122 | -46.2632 | 2024-10-04 13:56:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9f940574-b3db-3d70-bccf-4d5e9d388379 | -6.0782 | -44.719 | 2024-10-04 14:05:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| c895a6a8-e812-39c6-b86e-b990c94f2754 | -6.097 | -44.7175 | 2024-10-04 14:05:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f37aef53-2af6-3e70-858d-69e710af5f9d | -6.1468 | -47.4846 | 2024-10-04 14:05:41 | GOES-16 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7513be3e-b015-3e9c-afbc-96d66ac0cf60 | -6.0972 | -44.6947 | 2024-10-04 14:05:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 33012900-323d-3d01-bf0d-240cf5f2a269 | -6.9477 | -47.6887 | 2024-10-04 14:05:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4090481e-5eac-3d2e-94fd-26e6edc3bf91 | -6.9666 | -47.6653 | 2024-10-04 14:05:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 317f9ea8-c0c3-324a-82d7-6c6c4d4a9083 | -6.9479 | -47.6668 | 2024-10-04 14:05:46 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c12d9a0b-13f5-383a-a464-22ed38d87a76 | -6.9882 | -59.0844 | 2024-10-04 14:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 38cbe509-3080-3ab7-812f-1a71749cdd86 | -8.1567 | -43.7211 | 2024-10-04 14:05:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 722f8bcb-3f8b-32c4-a0ac-ee91766710f8 | -8.1909 | -42.5406 | 2024-10-04 14:05:52 | GOES-16 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 53.2 |
| eb3a686c-d4b2-3458-9da9-857acd1382cc | -8.1756 | -43.719 | 2024-10-04 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 91174d1e-4da2-33d9-bb19-3dc4e4bd0e4d | -8.1241 | -44.8101 | 2024-10-04 14:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 27bc337e-a8b0-3b61-bf74-5c4cd8cb150a | -8.3194 | -42.8343 | 2024-10-04 14:05:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 1f028881-84ae-38c9-9647-00c83f794af1 | -8.4347 | -47.1199 | 2024-10-04 14:05:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 90a0d98c-8c2e-35f2-8e33-4246336dda1a | -8.5212 | -44.7225 | 2024-10-04 14:05:54 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1b5ddc8a-1878-3a70-9aff-f3d478f71935 | -8.5675 | -44.0713 | 2024-10-04 14:05:54 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0fa26990-52a9-3340-b147-6221ff7a15f6 | -8.9663 | -49.8314 | 2024-10-04 14:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e38a7b22-9e2f-31ab-8456-529e9c6f0c4b | -8.9665 | -49.81 | 2024-10-04 14:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7060ce5f-3196-336e-afdf-c7340f81a8cc | -9.5962 | -46.2618 | 2024-10-04 14:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 02753c52-b6f2-3ad4-8b85-69987b53079e | -9.9826 | -42.0735 | 2024-10-04 14:06:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 6c7d0d81-e783-3e39-bda0-b411c5924510 | -10.2574 | -47.6796 | 2024-10-04 14:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 74aaf7a8-22bf-30f4-ab77-523d01794723 | -10.2192 | -47.706 | 2024-10-04 14:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 577c4824-a8e1-3dec-bd61-809b7f896d66 | -10.2188 | -47.7281 | 2024-10-04 14:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 401d24b0-6612-347c-b971-71d547c64d8f | -10.2381 | -47.7038 | 2024-10-04 14:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d41dc8f7-c15c-34ab-8925-54375dbc487b | -10.5933 | -48.0377 | 2024-10-04 14:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| bfdb5659-39f3-3a7a-9932-fab2a8fbf7d8 | -10.6119 | -48.0575 | 2024-10-04 14:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| ba866c05-0e3a-389e-abb7-0c2cb2e03471 | -10.7309 | -47.7126 | 2024-10-04 14:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c4330cb5-f1b5-3be5-8186-b199301e5959 | -10.8021 | -45.5698 | 2024-10-04 14:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 656af964-049b-3341-8c93-4b29aa5180c4 | -10.7115 | -47.737 | 2024-10-04 14:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 67b9e2c4-8e66-3389-a438-bb64ea46f984 | -10.7445 | -45.6002 | 2024-10-04 14:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 39bb0fa0-2c52-3108-a28f-75f9554993e0 | -10.8216 | -45.5444 | 2024-10-04 14:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 725f33b1-e3a7-3c44-9d78-7baaec26f730 | -11.2376 | -46.9148 | 2024-10-04 14:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |


[Clique aqui para ver as próximas entradas](README195.md)
