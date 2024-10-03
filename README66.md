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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 534bfe53-5d7b-36de-b0d7-a01e5854f6fb | -15.23519 | -43.33548 | 2024-10-03 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b32c38b0-ef6b-34d8-b063-31871cbdc36b | -15.23487 | -43.33685 | 2024-10-03 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5f482277-4bdf-30cf-aa7c-900d9eb9cdd4 | -15.2342 | -43.34072 | 2024-10-03 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b42e0f5c-6e3c-3308-8fe3-87d4b215ea64 | -15.23193 | -47.50808 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f37c032d-d1d1-345b-a976-5e2312772c0f | -15.23012 | -43.33587 | 2024-10-03 03:36:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 54c3974a-ee18-338f-9578-2c09f8304a79 | -15.22555 | -47.50773 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5192224c-124b-3c14-8fa2-3995dd7aed43 | -15.2247 | -47.51173 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad0c8a55-3bb2-3cf6-9e13-ede93d348e9e | -15.1968 | -47.5213 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4df0ca9-f937-37ab-935a-59f794e83af1 | -15.19586 | -47.52566 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45b53c96-7ca1-3dd5-bd19-d3469aced7aa | -15.14878 | -48.08942 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bacb179-77d2-303e-b5c0-8684462dac49 | -15.14767 | -48.09131 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a059ae5a-092e-3285-891c-f7a1d2890e48 | -15.14754 | -48.09509 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c0f4b1e-527a-307c-a253-78b189a59354 | -15.14646 | -48.097 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f68ef1f-de41-3197-ac5e-2314ce298f3e | -15.14233 | -48.08828 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82510dae-c438-3d49-9749-4890fc6f24d6 | -15.1411 | -48.0939 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4118f9d6-8151-3c35-8bee-4b11ece2c772 | -15.14003 | -48.09576 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b20160b7-a623-3c06-b296-fde32b875158 | -15.07918 | -41.93687 | 2024-10-03 03:36:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a80a1195-d2f1-3535-a681-c3680dbbc93e | -15.07834 | -41.93872 | 2024-10-03 03:36:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2fee2a5a-c9cf-3fad-b971-c7586dd13241 | -15.07833 | -41.94137 | 2024-10-03 03:36:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 986e920d-0371-343c-8308-414daa7a3e2d | -15.01866 | -47.55596 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f629ed83-a7d0-36e5-92c0-2997c2d3c6fa | -15.01785 | -47.55981 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fbcdb57-1875-3148-96eb-7ca76aff3c7b | -14.78354 | -48.05993 | 2024-10-03 03:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f874224-4fda-3746-86d6-2f04c2428f07 | -14.78239 | -48.06526 | 2024-10-03 03:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99e4aed2-b0ee-3d74-8675-822f35b2590e | -14.75469 | -42.42365 | 2024-10-03 03:36:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4705c2f-950e-3306-9a76-7fbdb77301dd | -14.7542 | -42.42127 | 2024-10-03 03:36:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c89d289-4834-3a9f-aaaa-c7834cfb4cc3 | -14.69876 | -48.75732 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0890577a-1b65-38bc-a566-153c0af4e226 | -14.69748 | -48.7508 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 058d48a2-c466-312e-b837-8e0751b1d6c4 | -14.69656 | -48.7551 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f929e300-3860-3e0b-8961-c7febbe39b72 | -14.69585 | -48.77056 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 36d51f04-a543-31bd-bcdf-6b1d857ae48a | -14.69539 | -48.76055 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d838133-54a1-3fd9-bcf7-e52404ad3190 | -14.69392 | -48.74753 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4b1c0a8-5a4f-3b3b-b1d0-0da0acef01a7 | -14.69365 | -48.78057 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9c1ebce9-950d-3851-b7c9-52234cabd0ca | -14.69303 | -48.75151 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d2733f74-7a86-342e-93fe-1fb92c3e50bb | -14.69194 | -48.75645 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 25f5040e-afae-38a7-92ba-795143390e9b | -14.69178 | -48.77755 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fc3cbdcc-10f8-3e03-8470-13e7b9601017 | -14.69032 | -48.76378 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b6199261-3f09-3cfa-8b28-6bbbea34222c | -14.68821 | -48.76137 | 2024-10-03 03:36:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9fb1fac6-8c69-3ac4-afbb-fcf859220b78 | -14.51324 | -45.24017 | 2024-10-03 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 685d6b8d-e7c3-3d85-8832-db87e14d2e6e | -14.51251 | -45.24383 | 2024-10-03 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e77cd0-51b3-3050-8157-c9600f08bae7 | -14.51001 | -45.22791 | 2024-10-03 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd46f4d4-0a04-3ad2-bbc1-857d919aea14 | -14.50926 | -45.23164 | 2024-10-03 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96d8d873-2006-3b03-aaad-71bd9dc06925 | -14.50852 | -45.23537 | 2024-10-03 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa58bca8-7416-311c-a099-63b4094c2275 | -14.50456 | -45.2268 | 2024-10-03 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb95eb32-e865-3065-9701-18755d812635 | -14.49429 | -49.29172 | 2024-10-03 03:36:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9b6cfa5-d33a-36b0-92df-278a46dafc4c | -14.48718 | -49.29107 | 2024-10-03 03:36:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77a78572-73a7-3e6f-9f6f-3859ec554a82 | -14.43856 | -45.71604 | 2024-10-03 03:36:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae699af4-80c7-31e3-b359-eeff729ebddf | -14.33786 | -42.35108 | 2024-10-03 03:36:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9457eaf-6a23-3974-b561-45033125f05c | -14.20676 | -42.01735 | 2024-10-03 03:36:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 039d013a-bc60-3788-bae8-b144b5b8c6c2 | -14.19995 | -42.07807 | 2024-10-03 03:36:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b4c11a65-0205-3793-bb9e-f1bf43f4a2ec | -14.19718 | -46.47042 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baea0dbf-10b0-3897-a6e9-33b97705ddcb | -14.19569 | -46.46228 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba845d81-dde7-3d94-9da4-8992cd70abfc | -14.19468 | -46.46728 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3efab1b6-0981-31a1-97ab-40fd6951438a | -14.19367 | -46.47233 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aada5d61-fa06-3fa7-825c-07cc1d7fe287 | -14.19335 | -46.45922 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f187d686-2f2f-399d-9311-f3624a50e260 | -14.19231 | -46.4642 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f6f72d-0628-3a14-8cd2-2aea30beb348 | -14.19126 | -46.46921 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e36d414-42a1-39cc-a483-eb9cba8c6de6 | -14.19023 | -46.47413 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 605699f7-0d0b-3a82-84db-06c5d582a3f2 | -14.18969 | -46.46147 | 2024-10-03 03:36:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15512cc3-7ced-3cb8-bb66-fccbb03126ee | -14.16473 | -41.85624 | 2024-10-03 03:36:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a58bcdbb-886e-381f-a26f-478059909970 | -13.99087 | -44.03292 | 2024-10-03 03:36:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a59332cf-73cd-34b9-a401-0fcff1c99457 | -13.99028 | -44.03601 | 2024-10-03 03:36:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3612880-941f-31bf-8fb3-31ad6810318b | -13.75529 | -42.61456 | 2024-10-03 03:36:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6518a8b9-a5d1-3146-b274-d3bc53def807 | -13.75357 | -42.61147 | 2024-10-03 03:36:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 668d4fa3-9502-3daa-a788-a8109905782e | -13.75025 | -48.32357 | 2024-10-03 03:36:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0525f47-653c-3529-b04d-29366b81e32f | -13.74929 | -41.05825 | 2024-10-03 03:36:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2f8645c-51ed-3fb4-8d30-b237e0b1b64c | -13.7487 | -48.33084 | 2024-10-03 03:36:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40693bcb-3787-3c98-84d0-fbb17ff0ad31 | -13.73861 | -48.16309 | 2024-10-03 03:36:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2d398fa-8d41-3198-9e41-71f95c6a1df4 | -13.73591 | -48.16488 | 2024-10-03 03:36:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 275bb7e2-83f1-3da0-890a-7613b625f663 | -13.73316 | -48.15628 | 2024-10-03 03:36:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ea55a5-435d-3a6d-b811-50a3a1b207d1 | -13.50176 | -48.6167 | 2024-10-03 03:36:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8453f4ba-100a-32d0-9c80-0faf0301a35b | -13.50074 | -48.61649 | 2024-10-03 03:36:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a00e7036-2320-35ff-b7df-88a629bc96e9 | -13.49628 | -48.60932 | 2024-10-03 03:36:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d408213f-4742-3ee4-a48a-2c49096df0c4 | -13.49486 | -48.61576 | 2024-10-03 03:36:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb174b97-494f-36b1-b8f1-90be94242a7a | -13.49386 | -48.61551 | 2024-10-03 03:36:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5928742f-db77-35cc-b915-343a9cedea86 | -13.38116 | -40.458 | 2024-10-03 03:36:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a414f72c-ca71-3366-b67b-917a5e98efc3 | -13.37995 | -40.46104 | 2024-10-03 03:36:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 25361707-7d12-3032-bf4f-0c4a0f3b8470 | -13.30819 | -43.71488 | 2024-10-03 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9becabd3-dfaf-3d3d-8173-57ff11121639 | -13.30315 | -43.71386 | 2024-10-03 03:36:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7bc89d8-3f28-349b-af72-0aa72db77c74 | -13.20667 | -48.6508 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5833da3-a5e3-3126-9647-8a091113bf08 | -13.19999 | -48.64863 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e3d0277-d598-3ad2-8b4f-ff6e0feb3aae | -13.19386 | -48.61338 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0a8cc1a-ef25-39bf-8644-ae438ad33b6f | -13.19356 | -48.61135 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60eb4dde-9b14-35bd-b1d7-2bef97b8e318 | -13.19327 | -48.64661 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4efbce90-22b7-35e6-a838-a9fd2cd859fd | -13.19324 | -48.64909 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae4a1939-fa17-3eb6-aa8e-ab8dcb3fc8cc | -13.19241 | -48.62002 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bde4cee-39d8-3698-8b6d-66988acc36ec | -13.1922 | -48.61783 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02acb49b-5d60-3bbd-abc8-81887be3a672 | -13.19167 | -48.65424 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2763ce1-6645-3509-a75a-5d3580432777 | -13.19163 | -48.6565 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4207735-276a-39eb-a3f5-100921142621 | -13.19099 | -48.62655 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d06255de-bea1-3aab-9335-c40db719deaf | -13.1908 | -48.62446 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c45167e9-0f6c-3e26-af01-e2d2d68a38c8 | -13.18956 | -48.63315 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12e6f569-d8a4-3448-be93-c48d94b9aafe | -13.18945 | -48.6309 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d409417b-ec18-3ca5-a6c9-d1f63aa53ea1 | -13.18691 | -48.61253 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2eb887a9-806b-3002-9f75-6f33ed883a43 | -13.18663 | -48.61045 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8236187d-9adc-35d4-9385-f3cc52ff0c8c | -13.18486 | -48.65473 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f48cf16-04aa-30a9-b6fb-1e1732684cb5 | -13.18347 | -48.65929 | 2024-10-03 03:36:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f181db9b-dcd4-38ab-b1e8-64bc8b9b2247 | -13.17793 | -45.45237 | 2024-10-03 03:36:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bde2b91c-1bb0-3903-91e8-e24b7157ad87 | -12.99528 | -44.72713 | 2024-10-03 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3323991-cc0c-3604-ae4c-534397c53115 | -12.99058 | -44.72231 | 2024-10-03 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6e40890-6a6e-39bc-9a32-b31a9503be42 | -12.7446 | -45.45727 | 2024-10-03 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README67.md)
