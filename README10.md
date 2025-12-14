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
| 0a70704b-9cb7-347d-9257-a574f00a6dcc | -3.88498 | -42.51966 | 2025-12-14 05:01:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 537aeaab-d718-3c96-be8e-1b1b9817f164 | -3.67271 | -44.82636 | 2025-12-14 05:01:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 466dbb2c-b539-3ee9-a40b-bb9a2407eba9 | -2.4806 | -45.43829 | 2025-12-14 05:01:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 056fdb8f-73e7-3df6-af62-b6a63cb88545 | -2.28435 | -45.58493 | 2025-12-14 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b2d544-6e76-311d-be8c-93010140572d | -2.97024 | -52.37286 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2273e56-9b62-3b27-adb4-da02c25bce8a | -2.97211 | -54.32862 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61a7f625-1d4d-3dd0-bbfb-66017f970cb6 | -3.31899 | -53.29156 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ace55846-6804-32fe-bf0c-6b7934baf11c | -1.02773 | -53.54928 | 2025-12-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3bd1d31-e5a1-33d9-931c-ce329950dfa9 | -4.34436 | -43.63524 | 2025-12-14 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1991a67d-56dd-3298-a7c5-d63705b959d0 | -2.88692 | -44.96836 | 2025-12-14 05:01:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3a070fc-a65b-3123-9c4a-422f04fcbfa3 | -3.0596 | -54.52547 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f34641ac-24be-3ec2-b7cc-62ff66611cdd | -3.16404 | -53.02997 | 2025-12-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18b6a918-1f64-38ba-9f78-21921b1f9168 | -3.46289 | -52.59355 | 2025-12-14 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 007122aa-68a3-3b0a-b2c2-b144d186c752 | -3.15505 | -54.60527 | 2025-12-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df69961b-10a5-3cc5-960d-dc9b45683c09 | -3.67224 | -44.82955 | 2025-12-14 05:01:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98c67263-ed17-3ee5-9cc5-6b625d37767e | -9.86729 | -50.56592 | 2025-12-14 05:03:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b887aa9-5840-38f8-bad9-5b01439f9df0 | -13.43096 | -56.83138 | 2025-12-14 05:03:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99b8f3e0-4864-34c3-a09d-ae136f8109bc | -11.08897 | -48.25176 | 2025-12-14 05:03:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b774ade-e6c2-3e28-b228-d78d1295d69e | -13.4343 | -56.83195 | 2025-12-14 05:03:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ddd2088-3670-375f-99b8-5313c20ab565 | -11.09297 | -48.25729 | 2025-12-14 05:03:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f92cfac-9847-30e8-bcaf-e2d4e23e17dd | -11.08832 | -48.25665 | 2025-12-14 05:03:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d44b9e8a-8ca9-3f65-be6d-4798e57c13d4 | -11.09362 | -48.25238 | 2025-12-14 05:03:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6da3144-c7dd-3c94-bc05-c9d43cd1106c | -15.97634 | -56.27436 | 2025-12-14 05:05:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fe70cbd1-b37a-32c8-8a70-1470238e7a7e | -16.93875 | -56.45642 | 2025-12-14 05:05:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 620d3b4c-7dcb-3c46-a650-799b8f20ea1e | -16.20858 | -56.60006 | 2025-12-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a39ed8b7-6be6-30ac-a6bb-638667efd866 | -29.0046 | -56.34101 | 2025-12-14 05:08:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 23e7f838-7ef6-3dc0-ba6a-51f0c4f3ea38 | -23.75668 | -49.64709 | 2025-12-14 05:08:00 | NPP-375D | SANTANA DO ITARARÉ | PARANÁ | Brasil | 4124004 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 4710cccd-33ce-32ca-8c82-45b3620003a2 | -3.14845 | -54.60685 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee76f2c5-e8ca-30a0-a192-51862b3e0a78 | -2.77454 | -54.52553 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ae45031-e503-3a08-a31a-8465dd557c8b | -3.53581 | -53.02532 | 2025-12-14 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 062fb9d7-0025-380a-8075-2542cfe3a0f1 | -11.08817 | -48.25798 | 2025-12-14 05:22:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32f2b610-d7f4-3d29-aff1-0ce22500f2a7 | -2.9722 | -60.06949 | 2025-12-14 05:22:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 260eace3-2e2a-3839-9205-faff972a13f4 | -2.97166 | -60.07293 | 2025-12-14 05:22:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 806e520a-d3a2-3ec8-be49-0d82e6f9233c | -2.28229 | -53.71437 | 2025-12-14 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39e80914-097e-3c17-a774-494a11c40877 | -2.18523 | -53.67279 | 2025-12-14 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09774bd7-1aeb-3d9d-b222-851f25253e56 | -2.1135 | -54.21753 | 2025-12-14 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe3148e0-9261-3652-8037-76ece621fc85 | 3.0862 | -60.37421 | 2025-12-14 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38af794b-cf05-3b6a-bbf5-8cd72e81be02 | -1.7967 | -54.0561 | 2025-12-14 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b504f773-5971-3851-b7e3-53dfdb450188 | -3.42817 | -52.89817 | 2025-12-14 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f9b13b-4620-3b42-b5d2-fb42e97bc0a1 | -3.06112 | -54.52606 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd0e5430-c22c-3af6-a7da-ef81360b033b | -3.31797 | -53.29294 | 2025-12-14 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0f05497-b821-3ee1-92e5-7aeea732d783 | -3.40072 | -54.59187 | 2025-12-14 05:22:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e83de24-e0f8-3cc9-8e44-c2bc946e516d | -3.149 | -54.60317 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7f0d5a5-558a-3140-a9ef-8ac83eb87c9a | -3.16654 | -54.9759 | 2025-12-14 05:22:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63afe38c-8ef2-312f-a777-e8f6c2ca1e4c | -1.42731 | -53.48105 | 2025-12-14 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3489366b-af9c-30c0-95e9-5e0a5a47fce8 | -2.28464 | -53.71393 | 2025-12-14 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e63d6ce8-baf0-38b6-aff5-c8c57b8e6f36 | -3.15311 | -54.60383 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e791e8d1-2da9-3006-bca8-d8827d62b345 | -1.4323 | -53.47753 | 2025-12-14 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 111228e0-41be-3350-aa9a-596b526cc65d | -1.02575 | -53.55391 | 2025-12-14 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a75c9fe-3d83-320e-9088-9f0e8c1e3353 | -2.18681 | -53.67485 | 2025-12-14 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15887de-44a5-37f9-9b99-273a083ed23b | 2.87631 | -60.26035 | 2025-12-14 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5a6c092-ce92-3599-9623-42ff6b18a9e8 | -1.02512 | -53.55797 | 2025-12-14 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2af17555-b268-3e35-9dbf-1b007a1ba887 | -1.57354 | -54.32338 | 2025-12-14 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68da65df-fb76-3e01-ab40-406393230330 | -1.02941 | -53.55858 | 2025-12-14 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 713001f0-07ca-3194-9a7a-e392112678a7 | -3.15256 | -54.60748 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b9e42f2-fdd4-3642-b554-6dd88b8fe725 | -3.16847 | -54.97308 | 2025-12-14 05:22:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65446eec-b22f-3d32-ae01-55eeb672c2b4 | -3.16707 | -54.9725 | 2025-12-14 05:22:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96edebc1-c818-3545-91e9-942f421391fb | -2.97001 | -54.32861 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7404146a-793a-375a-b1e0-e3c7bde64d82 | -3.30294 | -52.58812 | 2025-12-14 05:22:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a94e098-be1d-3567-b8a6-07f6577b4ed6 | -1.78655 | -54.15147 | 2025-12-14 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a0bad05-c1b9-3e9d-98ac-106e65db279c | -2.74264 | -58.18434 | 2025-12-14 05:22:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29032bc1-42c2-355c-8241-e4e250a0751c | 2.87687 | -60.26399 | 2025-12-14 05:22:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47b23792-231f-3245-b0ae-5637676946fd | -0.63504 | -58.00506 | 2025-12-14 05:22:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26e6beb9-d08d-3dcd-b50f-f6c4c985ec5b | -1.79541 | -54.05613 | 2025-12-14 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebdd0a58-7b2e-3932-8c75-70fb9b916fa5 | -2.18743 | -53.67075 | 2025-12-14 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 521f9fa6-2c1d-39d9-bda2-2c3b48beac79 | 0.96825 | -60.59683 | 2025-12-14 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b10be22a-722c-3e88-8935-7e694a3b37bd | -1.87915 | -54.68695 | 2025-12-14 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61e43260-9cbe-3eaf-a704-faa07254ce37 | -2.77397 | -54.52919 | 2025-12-14 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f937cd-70cd-3398-9ecd-3531cd9664ea | -1.42797 | -53.47688 | 2025-12-14 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 973e83f8-4be5-3c17-8179-086073253bbf | -1.78457 | -54.15129 | 2025-12-14 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3334f07c-0064-3509-a907-7f67faf773a4 | -5.25316 | -60.12612 | 2025-12-14 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40945992-1813-3c6b-915a-a3dbaed6a930 | -12.37536 | -64.00785 | 2025-12-14 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2998ee95-f00b-30a9-8e86-170d8aab5c58 | -12.37474 | -64.01165 | 2025-12-14 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9b56ab8-0b0e-3ad2-82f6-67df7b851dbc | -16.93776 | -56.45706 | 2025-12-14 05:25:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| be691636-53ed-38a8-99f8-431f0b1c9b4d | -5.13716 | -60.38668 | 2025-12-14 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9a86f7f-a25e-349d-91f0-d8e16ba3f64a | -18.34254 | -54.54441 | 2025-12-14 05:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54a50fdf-55c9-3e49-b105-be509744cf30 | -5.25647 | -60.12664 | 2025-12-14 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b0fb875e-a6ba-3ecd-84d9-a3cab9b660da | -1.02418 | -53.54901 | 2025-12-14 06:52:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2834a550-2328-3291-b5b3-f38e564b65db | -3.15434 | -54.60093 | 2025-12-14 06:52:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5607fa12-73d1-3e1c-970a-cda2c0900e48 | -3.6929 | -43.9977 | 2025-12-14 07:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 927a4734-9afb-3de7-b21f-c6867d514580 | -3.6929 | -43.9977 | 2025-12-14 07:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8cbc0f7f-8734-3723-a258-289f444c581b | -6.47005 | -37.57931 | 2025-12-14 11:17:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 17.0 |
| fb8a26b5-c98a-3f6c-b047-950c4a4de75b | -8.10019 | -36.52568 | 2025-12-14 11:17:00 | TERRA_M-M | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 62af3551-26a4-3426-8b1a-18bda7ebf46a | -8.10299 | -36.53204 | 2025-12-14 11:17:00 | TERRA_M-M | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 6b2d4853-ac21-3770-ad72-14f65a3e231c | -8.44399 | -35.31224 | 2025-12-14 11:17:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d831955a-53c3-3b23-abe4-de113bc43265 | -9.87962 | -36.6396 | 2025-12-14 11:17:00 | TERRA_M-M | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 4b1f9793-f761-37e6-89ef-ed80cbbd1928 | -8.92654 | -41.03038 | 2025-12-14 11:17:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 0e5eae9b-b8d4-33c7-887d-e146bfa9b83e | -6.47648 | -37.5729 | 2025-12-14 11:17:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 9010435b-06a5-3a03-8be6-956486c8daa4 | -6.47445 | -37.58599 | 2025-12-14 11:17:00 | TERRA_M-M | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 1a8a2498-4569-3cd2-b462-b0b6a84f4336 | -8.44536 | -35.3029 | 2025-12-14 11:17:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 60c2877a-ebc8-35ca-a3b6-8c8d4bc09c6c | -8.10141 | -36.5424 | 2025-12-14 11:17:00 | TERRA_M-M | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9d6e953b-f03f-391b-b5e6-2bf361bdcd1b | -8.09864 | -36.53618 | 2025-12-14 11:17:00 | TERRA_M-M | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 59.6 |
| d6632fca-8d5a-3503-a17c-6d76156506ac | -8.0513 | -43.1001 | 2025-12-14 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.3 |
| c717b353-9dae-344f-b0b1-81381074bf1a | -8.0324 | -43.1022 | 2025-12-14 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 211.7 |
| 467145e7-8968-3806-b55b-efd5cff72d77 | -8.0321 | -43.1257 | 2025-12-14 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 198.4 |
| 60070e05-994b-3e0d-ace8-55154c63a7a0 | -8.0513 | -43.1001 | 2025-12-14 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| a4e6ec5c-0a02-3b9a-a297-1f15b4021b02 | -8.0513 | -43.1001 | 2025-12-14 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 153.9 |
| f6a02084-841a-35b0-be10-d9deb9625863 | -8.0513 | -43.1001 | 2025-12-14 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| fc461220-6c93-314a-8440-f17d9b57b230 | -3.4991 | -41.9965 | 2025-12-14 12:50:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 175.4 |
| 9e88a511-e50c-3880-8a77-48caf0e4d3d9 | -3.4803 | -42.0212 | 2025-12-14 12:50:00 | GOES-19 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |


[Clique aqui para ver as próximas entradas](README11.md)
