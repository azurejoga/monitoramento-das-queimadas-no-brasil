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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1abf4d8e-6d1e-329d-bade-615084342d96 | -5.9123 | -45.79415 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 500de775-7c66-3758-86ba-a004d3697374 | -6.2669 | -43.39592 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f5b3597-28d2-3a79-a31c-4fe09f7ea8c1 | -5.57067 | -42.92491 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68ff32b8-a66e-3255-9e7b-89813d616381 | -5.6367 | -45.42008 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dc6da8c2-87f6-392a-881f-2809e280ff88 | -6.25006 | -43.40755 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9399489c-b864-3c61-920c-a76d514f4cd5 | -6.26004 | -44.05806 | 2025-09-10 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 230108b1-8e6e-3c50-a4c8-eb10a2df6b19 | -6.08841 | -43.35873 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88956d39-a038-331b-8318-432210c6bd00 | -3.24663 | -50.81046 | 2025-09-10 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fd17a75-99ac-3cc8-b8a3-fa86331a2549 | -5.9647 | -45.79753 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4ccf9f6-b5f9-30e2-ae07-1bf532eb13be | -5.52943 | -46.50061 | 2025-09-10 04:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3676c119-b4e0-3f24-9a66-4f1434953492 | -5.91015 | -44.97252 | 2025-09-10 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45e4943d-e59b-334e-ab57-69af8304dc66 | -5.40016 | -48.85281 | 2025-09-10 04:40:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b20a9a6-4dfd-3a10-9e04-e49324f1d581 | -5.54679 | -45.37863 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7db90404-208e-3b4d-8ffe-31be9209e941 | -6.20756 | -43.54538 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 936736fa-0a1d-366a-b56b-8575dd29bde5 | -5.65951 | -43.9093 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf0c2e13-24b1-377c-8a56-2750e053652a | -3.20866 | -54.95747 | 2025-09-10 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c0dd61-c037-3051-8f1e-155ab262719d | -5.50487 | -42.67712 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23af640f-9fea-3acc-bf14-d22cf69e29a4 | -5.40144 | -43.44053 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2adcfa8a-e080-3adf-a836-f06751687a10 | -3.85845 | -52.00568 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd2be861-0754-31cc-a673-ad8cd1828f46 | -5.66524 | -43.89898 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc4d14ed-6e57-3140-a896-232a53314caa | -5.90861 | -45.79356 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb695cd2-edd2-335c-9d12-61cf93c5377b | -4.95563 | -48.4053 | 2025-09-10 04:40:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42076577-45e4-3e9b-9f7a-65f5acbeb5f0 | -5.3972 | -43.43981 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0564447c-9e4e-39e7-b3e1-ae21d5859045 | -3.37156 | -44.20211 | 2025-09-10 04:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce75112f-9e3f-3c64-a5e2-c6848e2581d8 | -5.44586 | -43.46315 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93f68bc0-1f46-3f2e-b2c0-51b9a3bbc6ee | -4.73466 | -43.35517 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09d798cc-b79a-39f6-9373-982aba49c19b | -6.34618 | -42.60735 | 2025-09-10 04:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c54089ab-478e-3ca0-b705-e2e582918c73 | -5.53688 | -42.66154 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ee9e08c9-f75a-3ef1-8893-5dea84891f73 | -4.09215 | -41.5706 | 2025-09-10 04:40:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 23ccd60c-c13f-3983-a30f-ab50b1736a05 | -6.1695 | -41.04951 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a697587d-0d2f-394e-bef5-701badd5c803 | -6.2559 | -43.41125 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 47ee25b1-b2fa-39af-ac13-d9fc209aea9c | -5.72825 | -45.60766 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc049d7e-84f2-3321-9dc3-5af57adb96a1 | -4.09066 | -41.58067 | 2025-09-10 04:40:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90c3fa4c-b9e3-32ad-9cc2-d5852d022857 | -6.18467 | -45.02851 | 2025-09-10 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09e0d94e-21e7-3a4d-8826-a9fd80be8a5b | -5.56388 | -45.11533 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67d7afab-0e3c-3785-986d-131848736d6b | -5.75084 | -40.95318 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d788fc8b-a4a3-33d7-ba2e-a442cb5443f1 | -5.39238 | -43.44314 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dd4b9e3-bd25-3eff-96a3-77f3c8622225 | -5.64041 | -43.11402 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 431ac793-95f5-30e2-96ae-53a5d6023acf | -5.99382 | -43.32967 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92977255-d101-3d14-af11-6326bf4798a4 | -6.25217 | -43.40648 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fbf7d33-7e22-35ad-9aea-bf1aed49e563 | -6.26456 | -43.41228 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 313fa60b-f235-3dad-a416-c3988ca30739 | -6.47868 | -41.75634 | 2025-09-10 04:40:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d74e5b9b-f2ba-3c3b-92d8-372260894bca | -5.42692 | -43.44446 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e4aa060-efb6-3cdc-9258-15f02819443d | -5.65539 | -43.90859 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3294d3e7-be0b-31c1-95c6-55280962c5ee | -5.91449 | -45.83002 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1639e9d5-0b0a-3246-9ec0-1459f7622f84 | -5.71739 | -45.42054 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f17a56f8-ef73-396c-af81-6c3a3fde2ccf | -2.74498 | -48.69759 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e1b8d1-0fd6-3cd2-8131-f518cf8adb16 | -5.93489 | -45.81979 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd6c57ef-8b1e-3709-aad8-ce99fec9a089 | -5.10439 | -43.04716 | 2025-09-10 04:40:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e9aa4c-d471-302e-85dc-a59a23bb7fb2 | -6.25649 | -43.4071 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 91574fde-f371-34b1-869d-0bc13b4b1922 | -5.74705 | -45.25193 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13ebb6fc-8f7d-3af1-b244-507056161b00 | -6.16697 | -42.65744 | 2025-09-10 04:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4abd864-1776-3c90-9210-6e430ca5d9a5 | -3.8021 | -52.25772 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f12f1a5-fb46-3306-ab70-7a3f4586a75b | -5.66003 | -43.90569 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99a5253c-1584-3a3c-92f1-08e0a4253aed | -2.88423 | -42.95362 | 2025-09-10 04:40:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7046fb36-4e01-3b2c-82dd-5074237da553 | -5.25516 | -44.43964 | 2025-09-10 04:40:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 092c3332-8de5-309f-a917-bc6af5bc5135 | -8.3719 | -45.0367 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bdf8179-b20a-302a-a4ec-d50b555c9a40 | -11.13502 | -48.35387 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1de6e23-85ad-3bc8-8308-383699d80e8d | -12.0902 | -43.33114 | 2025-09-10 04:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b2dadf3-e33a-3e73-a2f4-4f37b056f421 | -6.7369 | -45.12665 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84792055-85ee-366d-be6f-f559146dd10d | -7.81383 | -47.50871 | 2025-09-10 04:42:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0f72520-3721-3b26-8052-7583b081919e | -11.14481 | -48.3596 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b91824f7-e0b0-3acd-81b6-10a4ea83cf8d | -9.068 | -45.71396 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f6870bc-0e4e-3ef8-967b-d69668c716f0 | -10.65415 | -48.61081 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfcef040-06a8-3521-beac-44c5a1c1c008 | -11.45317 | -49.27087 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b1eab0b-4d44-3127-9e13-4816057a59b6 | -6.44536 | -44.06072 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9640727-f714-331e-ad42-79ef46a9b227 | -11.67696 | -46.90281 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9805f28f-cc4c-3027-a28c-350b42c28094 | -8.02847 | -45.56648 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 920f3a65-7ae5-3c1a-88cc-325529ef8c46 | -11.46073 | -43.63292 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 734ac650-aed9-384f-9e62-f99a78793d4b | -9.06425 | -46.98532 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c5bfaa50-4e72-3f27-be22-0f074ccf8157 | -10.5708 | -52.01736 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65139968-a974-3d3e-97c3-551752884091 | -11.12297 | -48.38724 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4abc8ad5-9986-355b-ac50-f07532031878 | -11.33109 | -46.52488 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba392a5-e069-3011-9766-7688b01d66a0 | -10.00872 | -51.67249 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 045beb69-de1b-3358-a4d3-175427f7337b | -10.27125 | -48.81387 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a4a45a6-ba06-3f1c-8414-b40b204d7a66 | -6.88809 | -47.88856 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 28e78002-7cf8-3995-8817-312e6bf842e0 | -8.06806 | -48.63076 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 60057d9f-65ae-3185-8e93-2242932f8831 | -11.18184 | -48.37274 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d7d9447-4c6c-32dd-9064-ff8de2c8fba4 | -6.87563 | -47.90165 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2f1df55-9043-32f3-892f-701eb6854fb4 | -8.04861 | -48.68983 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 14.2 |
| fcf21217-8a1b-3759-94e7-b1bac6838d55 | -8.75317 | -47.1006 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e529070-de9a-3222-8a71-502d6dabdc93 | -7.48105 | -46.09576 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ba484fe-41ec-3c73-9ef8-a6ad92890e6a | -8.57579 | -48.95365 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0605f5b5-0cc8-3b58-bcb5-0d31eebccd62 | -8.49386 | -51.33841 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ba2c160-224e-3e1a-b172-9fac7c7cf30b | -6.09108 | -47.22467 | 2025-09-10 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2b0c3d5-345a-395c-a71f-3d990175362c | -9.10526 | -46.98199 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b05bdc4-e8db-3fe0-8d95-b9e08c9b1c26 | -11.76301 | -50.58031 | 2025-09-10 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d3c6d42-ce0d-3870-a9aa-df9fa5ad46ab | -9.06065 | -46.98476 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2d330a7e-5bda-3086-856a-a3ceb04bb361 | -12.13895 | -44.83698 | 2025-09-10 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a57f352c-de7a-3f7a-8728-c375432982a9 | -6.7909 | -43.45225 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa6f1795-002b-3bb3-9d07-9f82bfd2424b | -9.82429 | -46.02264 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72446db4-5321-370f-b846-ffd9617791fd | -8.74726 | -47.09127 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4eb07bd-18f2-368d-a65f-5cea5658fd26 | -9.4551 | -46.43423 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 386e4ef1-5655-3dcc-9680-401b18bc0af2 | -9.14636 | -46.05148 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 344087a4-3c8f-3f3f-ba4e-a78083fa056f | -6.74284 | -51.95507 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cc3f41d-3b61-3390-b31f-a983c3738b18 | -11.6776 | -46.89834 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44331cde-8b80-3958-bdfb-54667c8c2e8b | -7.73767 | -50.72612 | 2025-09-10 04:42:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99e5ccdd-2218-3d1c-96c3-516d86d1795e | -6.99615 | -45.6517 | 2025-09-10 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cdd1124-ba47-39db-bae6-d3d6d5b8e703 | -6.85057 | -44.89876 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22093f9a-25d0-3b6b-b8bf-065154adb92f | -8.04322 | -52.38806 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README57.md)
