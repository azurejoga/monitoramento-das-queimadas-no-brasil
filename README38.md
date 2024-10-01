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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99cfe5d0-866a-30fc-a414-ab4da1f4ded4 | -19.68729 | -47.23235 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44c9c590-b23d-31cc-976f-b4cf3d234d80 | -19.68575 | -47.23885 | 2024-10-01 03:28:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37352985-51fb-3afb-b928-921b869d73eb | -21.61407 | -47.8603 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf49b6d1-f88a-3158-b3d5-70a2c8514c4b | -21.61251 | -47.86651 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38a5fe4c-650d-39c9-88f7-f2b6baacc3d8 | -21.6119 | -47.81286 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0555ff6-4405-35c8-9c06-fd29a2d4c853 | -21.61185 | -47.85514 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83dc0188-951e-3edd-969c-9b9c4a8e65cb | -21.61096 | -47.87273 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02638071-5384-3767-894b-4fd81e59c8cb | -21.61033 | -47.86137 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 813bac4c-139a-3b65-b4ab-0c629b95b041 | -21.6094 | -47.87896 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99c09d8f-028a-3088-bd3a-e9e6326541b0 | -22.53646 | -48.8152 | 2024-10-01 03:28:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9b41bf2-b8ba-3c8c-95d9-4096388bb0cf | -21.60905 | -47.85226 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8dcaae76-bae7-381d-81dd-ede8cae81467 | -21.60881 | -47.8676 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1f6eb59a-5460-3972-ba8d-bae0a6042d6c | -21.60874 | -47.82542 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e3a1ee77-f435-3a23-9811-2dc6be7d560e | -21.60832 | -47.84081 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 2db951ea-8f32-3ead-842f-43a456688bf9 | -21.60783 | -47.88522 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1659ce0d-c350-3a05-b5d0-b83e2e661711 | -21.60749 | -47.85845 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a584cb3-6bfa-3dea-80b8-fcd8aa1cae55 | -21.60728 | -47.87387 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 426e4f8b-ac48-3a87-9f3b-ff049550f6b0 | -21.60716 | -47.83173 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fa8d4ff2-479e-361b-831c-2c6ca829f4da | -21.60679 | -47.84707 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f3ccd934-3be2-3b40-adef-5ba591a100d3 | -21.60626 | -47.89149 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac75479a-8057-321d-85a4-026824cdbabc | -21.60594 | -47.86464 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a106377e-4a2e-3e32-a493-7abf5069ee95 | -21.60575 | -47.88016 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cb78cde0-5d27-3c3b-a329-e6eb7dee0a37 | -21.6056 | -47.83797 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| f0d04f5c-6898-3597-b309-b0616dc204d8 | -21.60528 | -47.85328 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e1ed8782-8fe4-3d1f-b7c3-411515edad7e | -21.60484 | -47.82632 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7127abc3-298f-3466-af5a-c679679dc7c9 | -21.60437 | -47.87092 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7d45cf9-7503-3c98-9494-a21523dbd6a9 | -21.60403 | -47.84422 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d454e286-c1c0-33b6-b10e-afafa1f6130f | -21.6039 | -47.81674 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0db289a-bbd6-3656-86c6-b26b5c07fd78 | -21.60376 | -47.85947 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6c440264-dd98-37ba-9296-5909b10526e8 | -21.60356 | -47.79019 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c47681cc-f54b-3109-8d15-3828d1f072a7 | -21.60329 | -47.83267 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 21.1 |
| fee41d22-1c7f-3095-ad67-3f05020884f8 | -21.60279 | -47.8772 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d692613-97f8-3e98-8c45-39e14d8b119d | -21.60268 | -47.89273 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 674d5548-756a-3218-bf8a-84f1d25c71a3 | -21.60247 | -47.85042 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ab845624-4a3f-3a78-8eab-729152c1a55b | -21.60226 | -47.82329 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a1cb4b59-c873-31de-8c1b-aed3802a8ff8 | -21.60224 | -47.86572 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ee6e544d-2302-3756-91ac-a6e328f2baec | -21.60194 | -47.79661 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65503208-d85a-35a6-98ee-089018d994cd | -21.60176 | -47.83893 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f6f8067c-ae30-309b-bb94-97570c7ac7fd | -21.60157 | -47.81102 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b53b0965-e2f9-3e13-9b65-dcc150586b9b | -21.60122 | -47.88347 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77c59219-b3e9-3cb9-99fa-942eaa80b49b | -21.60092 | -47.85661 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e10effae-15bd-3e43-8d2d-4ca381b6ef3f | -21.60069 | -47.87206 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b1f56f5a-30a9-34ee-8ca4-dd90710291fd | -21.60063 | -47.82977 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4ea2c162-2b94-3145-add6-b3e6f6090036 | -21.60048 | -47.80243 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a0ff34a-10e4-346e-bcd8-b3064063cdb7 | -21.60023 | -47.84518 | 2024-10-01 03:28:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 26979915-406c-3c5c-a299-28ec6e97c507 | -21.59999 | -47.81744 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |
| abdce148-d189-32ba-856c-fd9d854ef5e8 | -21.59965 | -47.88973 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1429ae0-02a5-319a-8cd7-77a4c634e361 | -21.59944 | -47.79109 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d55e1719-af46-3803-8f2f-8582e96dcc51 | -21.59935 | -47.86284 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b51aa522-64b6-3a0c-a392-84ddec664fdd | -21.59916 | -47.87833 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 021d8163-3c8a-31aa-a2be-fd61a3e0bb00 | -21.59904 | -47.83609 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 92dd7923-9fc2-39f8-8f04-21bf7863a1bb | -21.59902 | -47.80824 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| b298d56c-e2b1-35de-a080-5447eb0f4bbc | -21.59871 | -47.8514 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b7f67f49-a51a-30c1-b4a8-eb2af6024b19 | -21.59841 | -47.92281 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcaf1d10-75d3-3564-a0ba-d7e282f5e746 | -21.59807 | -47.896 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8d7fc93-5866-3750-a91f-8486da1a3469 | -21.5979 | -47.79737 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c457c4f4-ac1c-33b6-8d0f-be5aacb4eeee | -21.59777 | -47.86914 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 562b7d7b-e308-31e6-921e-d2caa0fe7d3c | -21.59762 | -47.88461 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3bfc87a0-261b-3148-b3e0-6aea7fd393cd | -21.59748 | -47.81433 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| a77e4d32-48d4-3b02-a8f8-5edb88548c3a | -21.59746 | -47.84235 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 8732dbf2-d5b5-3c40-a682-7debc222b703 | -21.59718 | -47.85764 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 63f5a3a8-f9f9-3cd0-94a0-e964d5caa516 | -21.59683 | -47.9291 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8378dbf9-ba85-32c3-ad52-34cbed82c6d3 | -21.59678 | -47.83057 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 289.6 |
| 31b6150a-c43f-3f81-81fb-ac911b6fd32e | -21.59654 | -47.91787 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e60b9933-7e96-382f-9f75-f589f30a99bc | -21.59651 | -47.80302 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46776a19-2434-3d7c-9653-105a26b4fddc | -21.5965 | -47.90226 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae0ada49-9030-3a51-8796-fc9706f24cb9 | -21.5962 | -47.87539 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| eb6898e6-f9d7-3e66-a910-4a703d71489a | -21.59608 | -47.8909 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b5393386-2ba7-3816-971a-795e37315a3a | -21.5959 | -47.84857 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 73585e2e-8bf5-3d98-8c45-76909e274c76 | -21.59564 | -47.86393 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0c1950d8-c7f9-31b6-9367-e76f2c4acb1f | -21.59537 | -47.79485 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32ac9278-bb34-36fd-8a85-41a5d8bafdc3 | -21.59521 | -47.83699 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 31.2 |
| d3f0a09e-7c0e-31a7-8bae-a27534e7df64 | -21.59509 | -47.80882 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |
| deb50130-2ef0-373b-b9c5-37eac501cacd | -21.59492 | -47.90854 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d32e7424-d9dd-3f99-8b58-1e6bbdbb50f0 | -21.59463 | -47.88163 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 93590d9a-cf02-3795-bf28-446f87bce2a0 | -21.59455 | -47.89719 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f3a6a9a5-a631-3486-ad8c-e725a96b0d28 | -21.59434 | -47.85479 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8949efe4-2b5a-38cc-a24f-eabea11a86c8 | -21.59418 | -47.82746 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 366.6 |
| c700c7b9-7c4e-3e0d-b8da-c6668332d143 | -22.35748 | -49.32291 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 99267d79-077f-3b54-822b-90410c5dbfbb | -21.5941 | -47.87024 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ddb2f096-9b7c-31cd-98b7-f36d5bbdb38d | -21.59393 | -47.80056 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0ce0e4e-0afc-3370-bee8-635347726771 | -21.59367 | -47.84328 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 56390974-3162-30e7-b512-a6de9d02ffac | -21.59335 | -47.91481 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6df02ce-afc8-3299-a46c-b151ba24bf43 | -21.59306 | -47.8879 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| de336f64-b0dd-3376-9983-3e3e8fe7115a | -21.59301 | -47.90346 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1a5a4fa3-4a3a-3901-be55-f5d7f34b6704 | -21.59275 | -47.86108 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5b0e9990-e798-36aa-a435-bd1df27bdb7c | -21.59257 | -47.87649 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eaa3f236-eaf6-3b2e-b47d-e482a5e73f6e | -21.59255 | -47.83392 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 0f549482-f6be-39ee-8beb-281019059be6 | -21.59251 | -47.80618 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 20a43cd3-b45e-3a49-be11-0944fb73ed7c | -22.12253 | -48.55419 | 2024-10-01 03:28:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38041c73-23bf-302b-a4ce-0bccf4fa34e6 | -22.12071 | -48.56133 | 2024-10-01 03:28:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1efea583-0624-327c-bd55-470c02157a5f | -21.85197 | -47.17278 | 2024-10-01 03:28:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef77e822-7271-34ed-85a3-a57365a3cb73 | -21.5834 | -47.79929 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 480ef078-5473-33fd-8f18-4d3904a73b83 | -21.58302 | -47.87176 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7d4c3b4d-d2ea-37e5-bcfb-eb18abd24a68 | -21.58248 | -47.86024 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| efa5364a-890b-35b7-89e2-b2756b186fff | -21.58206 | -47.80475 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 213f3542-7646-3601-8568-bff66c045710 | -21.58144 | -47.87799 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1f161e51-0274-30c4-ae94-3a3d4e913e7c | -21.58123 | -47.85088 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| b5600a16-7f32-3a01-a424-348b95db0e38 | -21.58064 | -47.83908 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 683c0684-9e34-366a-bb57-84e73df433de | -21.58064 | -47.81053 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 182.8 |


[Clique aqui para ver as próximas entradas](README39.md)
