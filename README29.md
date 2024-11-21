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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 804c3eb8-4407-3ac3-ae67-20d8cbb6b16e | -4.24676 | -46.12112 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 69dd28ab-01f6-33a6-912c-3406823329e2 | -1.9755 | -46.36571 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa778e1b-420f-3ba5-80ae-287e63085ae2 | -2.0189 | -51.17915 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c062cc09-39e8-3845-8b04-550202e0dc6e | -2.52039 | -46.28062 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df2f5f86-09a6-3bae-a973-d6e817105e67 | -2.72583 | -51.8157 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7e47370-ae9a-3388-83a0-74dc66220e72 | -2.63786 | -46.2205 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ebd72f0-8216-3439-9177-5aba31422730 | -2.92951 | -48.33847 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 802b8b7c-02b5-32ea-9eb0-b0233ad947a2 | -2.0912 | -46.31996 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a07dd622-b2d8-3cc9-bf75-1b83c2a4772c | -2.14943 | -53.77353 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eecc5a0-46b9-3288-9ddc-bfa54ff163e4 | -0.42315 | -51.56814 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cf98afe-7b8d-3137-889d-19452f18a3ab | -3.00721 | -48.04401 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a1d85e8-0b08-3e45-a7d8-670ef1789301 | -4.02117 | -46.65257 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5794838-05ec-3ccf-b46a-578d9729b01f | -4.071 | -46.83417 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f02a5f87-0747-3e7d-ae4d-b4009b8f7032 | -3.39746 | -51.20185 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adfe511f-b771-3e44-afa2-cb84bbff81be | -2.87576 | -51.79066 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a359f90e-1e28-37c1-9ff6-b8e023740414 | -2.25341 | -53.67943 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b23d362-613d-3c53-877e-d2937ac83ad2 | -2.92389 | -51.44928 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2444de8-47f9-3dbc-9c87-590306fa451c | 0.1371 | -51.09996 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5782f209-6cd7-3a13-8d2d-eca2b83c6f86 | -2.02396 | -47.0014 | 2024-11-21 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9a179f0-24d1-3df4-addb-2948170bf4ad | -2.17989 | -52.132 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69f024b7-bd63-3f9c-a5ab-8b00b82ee18c | -2.35446 | -48.96288 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7a590e1-995c-3b81-9c56-1f8c48448be2 | -2.42015 | -49.10975 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 335d46e4-2160-345f-8490-a838ecf042ff | -2.63562 | -46.21304 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a001bcf2-5b05-33c0-8833-a7ace745a876 | -2.62993 | -54.27152 | 2024-11-21 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6115a559-0377-332c-b0d5-c39a3ef5cc7a | -3.10133 | -53.1719 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9382ef44-6ca7-3ade-950b-76ca76dc54cb | -2.08226 | -46.29024 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55983f0c-87bb-315e-98f8-7e30cbf93253 | -1.37725 | -46.51245 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b7a5e4c-d3c4-3235-ba69-f9c6b38564f7 | -2.35823 | -49.07254 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 26ce6b45-c75b-33f9-8cfd-516735687020 | -3.0878 | -45.98257 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad1229a4-b3d9-351c-9c98-3e655321b83e | -2.95094 | -48.33448 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf9e7257-9825-333f-90a7-708fad5e2e4a | -1.46099 | -52.67806 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0207d4b4-39c9-3308-9eda-1d2fecec57be | -3.19046 | -46.28136 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75fb6930-d479-3ebc-924e-910cc9bf236d | -0.94752 | -51.63877 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a406ef2e-8a45-34d9-ac1c-73063bc3dc88 | -1.69973 | -46.16328 | 2024-11-21 04:29:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8094b454-8930-369f-aafb-7f94816b811d | -0.86841 | -51.85225 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5ca9c6f-9981-3d67-bc42-01ebd7ee2085 | -3.02428 | -51.52637 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a32b096b-5b2e-383d-adc2-1b6e2da787fb | -2.65376 | -46.14104 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebf81e42-3bb1-3c42-9c14-8423c77e5fc4 | -3.10371 | -53.21207 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39d62927-a942-34b6-97ed-af79af35fed7 | -1.34538 | -55.43774 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dadff0c-9330-3bf2-9082-83bfbb698d90 | -4.08706 | -46.84021 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfff6fe4-706b-3d28-ac5d-a326a8fea1fb | -2.83292 | -46.68004 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d61c4c0-d0cd-3280-b5f3-a63c41f79616 | 1.38096 | -56.03052 | 2024-11-21 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f988bda-1041-36ee-94ed-8e193e1feec6 | -2.58848 | -51.71517 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5120b89-8936-31be-bbd8-7168511ef01c | -4.04166 | -46.22332 | 2024-11-21 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a499e6c-f437-36f0-ab6a-e5f6e7cde61a | -2.78261 | -51.72405 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e93e0750-b5b8-3efd-8739-7bb24b23301d | -1.20658 | -51.76147 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 926f14f4-7eaa-3682-813f-9847d091d401 | -3.26757 | -50.61824 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc40f0ba-8205-3f7d-a594-87a6d063f653 | 0.45092 | -50.78975 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 369de37a-a199-3a36-9434-4f2ee4fb069d | -2.56848 | -46.55354 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db4ca585-0b02-3963-bc7c-36da2c4bdb9b | -0.91788 | -51.78023 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fba42265-3dbf-3b3d-b3d4-f5e03297c816 | -2.33881 | -53.93209 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9b972412-7c8b-333d-85ce-ba26aa820f28 | -2.78923 | -52.5507 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43e07206-9129-341c-bcda-174a159da6dc | -2.53413 | -45.43636 | 2024-11-21 04:29:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 351e3457-952a-3430-9718-3d32959acc9f | -2.92231 | -46.84217 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d529ce0c-aa89-3476-9d4c-e6ca06aa1be3 | -3.92669 | -45.77372 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cefc74fc-0f68-3cea-b391-48619b3e3353 | -2.6265 | -47.96335 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02846ac8-46df-3ba8-add9-3fea029ec575 | -0.93454 | -51.71856 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5eed3f-2bf3-366e-9537-fb05ea8f3098 | -3.23074 | -43.26516 | 2024-11-21 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec7e487a-60de-30ed-afc3-7b469b6c1a26 | -1.39602 | -53.57837 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91bebb35-854a-3784-94b4-83fc2c52f924 | -2.26549 | -48.40616 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e14665d-d97f-3749-9542-6bef4fc46f82 | -2.6302 | -46.05164 | 2024-11-21 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e3aa2ab-c1ba-3c36-91d0-31f1a0e50dfb | -2.54702 | -47.29225 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6435c98-a741-3bdf-ba5b-de7ce012f557 | -2.73852 | -48.63989 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccbb73b1-4e12-35cd-9c13-eb935a469add | -2.68874 | -46.19631 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be12ead0-0920-3061-a48c-633cba71dbae | -1.29251 | -52.22576 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce9a219d-2c20-3c4c-9704-b3534301ab31 | -3.80264 | -46.51944 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 089ac6ef-7d04-3865-9c7c-214f1e33d6b6 | -3.37693 | -46.12454 | 2024-11-21 04:29:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3364ed1a-6c2d-3591-b56b-274fcb7729ca | -2.68919 | -46.06792 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db240b32-da82-354a-b1a1-d095d3120de1 | -2.74193 | -48.64042 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb0d94b8-41fd-3905-af00-17b2ae80cf0f | -3.32936 | -50.25166 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3522242-c820-36a8-b139-1f06cac71a42 | -2.6933 | -46.23262 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9aca87e-c168-3aca-97ed-7be0b09b4799 | -1.56237 | -55.12216 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b459a893-4d4d-3e80-b490-018cbe1d938e | -2.67381 | -46.16552 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dfc9c17-c06f-3464-bbbc-13c03a0f16e5 | -2.63731 | -46.22398 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4226abc-cfbf-36f9-ae22-361ea13a2ba6 | -3.08556 | -45.97502 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53756404-4c37-3003-9071-dafb2ae03710 | -1.96501 | -48.38583 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 154d1e31-7800-3772-88a2-a880afeafec6 | -3.18983 | -45.03483 | 2024-11-21 04:29:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80361d3d-054d-3cd2-aca2-e99272c3f89c | -1.14065 | -51.68081 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 600dfadf-3ba8-3cde-b813-93eb68ed6f09 | -2.55592 | -46.0546 | 2024-11-21 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 07b27221-bd62-3e49-bba7-6007d0548677 | -0.95508 | -51.72182 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7404fb-56c8-3beb-8c3b-2276bdac9dcd | -1.65278 | -55.25948 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f035f0-3d8c-3903-b348-35b6a0a70c5e | -2.13856 | -53.64175 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f967b62b-b118-36ce-a623-383581b67626 | -1.23462 | -51.74357 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21ecc884-cc98-3c7a-9f05-d2437b1cdf56 | -2.14479 | -53.77278 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cba0b33a-2745-3368-9de9-301840c156a0 | -2.32164 | -46.85408 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30abe729-242a-3c7a-959b-2b04041df33d | -2.21756 | -46.39602 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8618d046-4dcf-3ddc-ac9a-fac1a945a47b | -1.36771 | -51.998 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39173d2-0760-3ec4-9311-b6480bc1de0f | -3.81178 | -47.79296 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36067c0b-f430-3700-b08c-cccba341d74e | -3.57189 | -49.99208 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef712af0-f48b-3a38-a3e0-b6c9326368ea | -1.6297 | -52.57328 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c23589f5-6d8c-364a-b5c2-24ecf5ccb4b9 | -2.56139 | -48.1681 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83904c14-b913-3fe0-98a9-8fcd2191a21b | -2.24956 | -48.41857 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a44afcf-a989-30b5-82eb-f7b553c987a1 | -3.27605 | -45.44941 | 2024-11-21 04:29:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0f1a5d-f767-3867-b13e-3b9b32eac75a | -1.97974 | -48.68655 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2adb6aaf-1d79-3a27-94a4-290e22f7cbc4 | -2.65665 | -46.55315 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ba95916-d08b-3de2-b745-d2268c9deb56 | -2.35385 | -48.96666 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 015140e0-5442-3304-98b3-fb6db6b5fbb4 | -2.25926 | -48.40145 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6ed0025-59b9-3e8c-ace1-5b080056f932 | -2.25717 | -48.70231 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b028abef-0777-3a40-8370-1b96e70fe1c1 | -2.90428 | -53.05761 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8374990-5efc-3070-9f6a-2894bafae8fb | -2.90797 | -53.06237 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README30.md)
