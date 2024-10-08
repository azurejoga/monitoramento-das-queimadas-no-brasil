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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f1cb743-9884-3a3e-bf73-a293081911a6 | -11.25414 | -60.37492 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72f9c7eb-457a-34b0-bb58-13b5a54010fd | -11.25374 | -60.48885 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2efa9fb2-3c8b-35cd-b13c-3aa8d8033e72 | -11.25318 | -60.49245 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 843d6d47-46e7-33c5-be31-a4ed1cda828c | -11.25263 | -60.49604 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d3405a9-646b-32a1-9598-c9bfe6026cf6 | -11.25086 | -60.39629 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf8e94d5-5837-32cb-820a-11155da061fe | -11.24873 | -60.49912 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0657188-e140-3006-bbe5-92d5822f165d | -11.24538 | -60.4986 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f2418e2-cd39-33f7-831d-d6b20085bb65 | -11.23092 | -60.48142 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71aa243b-2eb4-3e64-917d-7e2128c24ddf | -11.21869 | -60.49415 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35372a00-7338-3df6-8331-8b851863e02f | -11.21199 | -60.49312 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09de4e7d-46ee-3329-98a8-9a3f420aafb6 | -11.2098 | -60.50741 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9baed17-243e-36ae-89eb-ce199a56223d | -11.20915 | -60.24195 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248f3588-84cb-3249-baef-80547a6983d3 | -11.20202 | -60.5135 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 778f6d77-5272-3d96-84c3-a3697acdd747 | -11.01068 | -60.56767 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4897d685-204e-39d0-afff-a57921e6c520 | -11.00307 | -61.1203 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a589c4f1-b1a6-3daa-b7ea-8af36183da51 | -11.00237 | -60.57726 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85a8778e-907f-3cc2-a1e5-87a33ac7e9ca | -10.96747 | -60.97778 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372f6965-ca48-3f32-8326-3e1d544b3557 | -10.96664 | -61.11451 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c7c8ff9-260a-33be-8224-777f8f97d5c5 | -10.96609 | -61.11802 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 166a189a-6033-3df5-84de-bbbe1249354d | -10.95814 | -60.99408 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ad4cff-8a5a-38be-b95d-758dca358ed1 | -10.94764 | -60.99602 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f65574a-0a3e-3e68-9042-bb4f9ea2f962 | -10.94433 | -60.9955 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6ccd9ab-d899-35f3-944c-1745d80d3b2e | -10.93613 | -61.37527 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5268a4b-f637-321d-b9af-4db3c4741f21 | -10.93392 | -61.36775 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02a8ce5b-8906-3d39-8c6c-1ffb0580e296 | -10.93228 | -61.3782 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9618c98-77b0-3f86-9ed1-8501f2a0eabe | -10.92159 | -60.94505 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61cd1aca-fcd7-3276-bf74-5a7e1968859d | -10.91827 | -60.94453 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd1e8048-dc4a-3ac1-96f3-7b32f95716c4 | -10.91351 | -61.34655 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2f5c13-98d2-38e9-971a-f509aa2b72c4 | -10.9102 | -61.34601 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 736eb408-d402-36c0-884f-5cf500444c73 | -10.90887 | -60.93944 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f80f2fdc-eb59-35b4-a0c1-214a042efcbe | -10.9061 | -60.93539 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f01b4aa-e844-3a7e-87c1-12b4d5211d60 | -10.90501 | -61.35567 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e1bff09-07ec-3f07-878d-2171eaccaa34 | -10.90438 | -60.90263 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6ba3265-43f9-310d-8ca8-95a799b4a50e | -10.90387 | -60.92782 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63a66f79-5fd5-38d0-a7db-6fceac331de5 | -10.90225 | -61.35164 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 175393af-6297-3ed8-b2a9-64d96d2506ca | -10.90116 | -61.35864 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b48298a2-4499-355c-9062-743cdf92f6f1 | -10.9011 | -60.92376 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1d3ea76-771b-375d-bb7b-48f49bdbfdb2 | -10.89839 | -61.35462 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63147d3c-ad6d-35c6-950b-fd346dd6444b | -10.89288 | -61.34655 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 848a13e7-80d9-3cab-b04e-db2db7e33974 | -10.88903 | -61.34953 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d11d0963-1667-3904-998f-5b8b221f224e | -10.84992 | -61.36113 | 2024-10-08 05:23:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2e364ee-ed37-319f-ba25-4475443e4148 | -11.38075 | -60.58562 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2192989-e874-3299-bb91-06408d82f2d4 | -11.35324 | -60.57054 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc5e3a6-e665-32d0-93a0-0c0beba53e48 | -11.35269 | -60.57411 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aa5a2be-b368-3147-b0be-44275172d161 | -11.35214 | -60.57766 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da3771d5-5249-3415-9edd-f0baf37f6cad | -11.33596 | -60.54946 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b6a4ca1-261d-37c3-b392-6d28af4685ec | -11.32983 | -60.54485 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d526c8f7-1558-361f-a8df-7b09b6f87d0d | -11.31536 | -60.54988 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8dc2c85-869d-323c-9f68-71f4f7041a26 | -11.31426 | -60.55706 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f72329e6-9704-3fe6-baa1-2a572adb449c | -11.2998 | -60.56215 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01e4c472-644d-3d50-aaf2-65795ac9af22 | -11.29646 | -60.56161 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d85c6b1-ac2c-3069-bb56-335315a711b1 | -11.28206 | -60.58862 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb7bfb5-f586-335c-8287-de0808e98a76 | -11.28036 | -60.57738 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1bb8091-4430-34ee-9566-85e69fe8067b | -11.27986 | -60.60291 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd72e370-0101-36fb-8e6f-431c00aaff06 | -11.27981 | -60.58094 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 388ae0cb-5eae-3cc1-84c9-8768af4d8a04 | -11.27652 | -60.60241 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bb1fd1a-6f85-3b54-8dda-dde0b63ce777 | -11.27537 | -60.58761 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e7cad3e-0789-35b0-a9f0-87f45b2f281e | -11.27313 | -60.57996 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2fceedf6-f789-394c-adee-dd0cb850a9aa | -11.27088 | -60.5723 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9fe6524-377c-35cd-86ec-6288c7d5dc26 | -11.26475 | -60.56765 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4689b53-749d-3641-9173-aa60c0001bfe | -11.26087 | -60.57072 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3b28443-b010-3780-9c64-62ee64476e7c | -11.25365 | -60.5732 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0d24547-cdff-39d7-9fcc-b846eb75e70e | -11.25031 | -60.57263 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb1bd5c3-8e59-3137-b421-1be8d28d79ca | -11.23717 | -61.18667 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7f57bf6-627b-322f-b830-592ecc73dae3 | -11.23717 | -60.57403 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a5064d8-1dd5-3495-a255-d7d4e3e93ac9 | -11.23332 | -60.59895 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8770ecc0-53b2-3244-9b8d-67eefd5976c1 | -11.23219 | -61.17509 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47f7bb37-1ce2-3da5-bbc6-d4560a34e803 | -11.23053 | -60.59486 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e67e69-96e2-35ba-b4e6-9352a8b6c835 | -11.22998 | -60.59842 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 082b2891-4ddc-3286-b9f1-2f1027996af0 | -11.22942 | -61.17105 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cafd8d2-8ace-314a-bd7a-0a6ae3b62586 | -11.22888 | -61.17456 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3e0cbf0-5147-3340-9dbd-b1115f543d48 | -11.22771 | -60.56886 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14255db3-192d-3666-924a-d0ab4828890b | -11.22666 | -61.16702 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1f7bca3-635c-3d51-88b1-c13c5df99547 | -11.2228 | -61.16999 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8e99e48-fff7-3960-97ae-e6ab2d44015d | -11.19724 | -60.63345 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5894b8d5-90dc-3640-b534-450e2b6e75bc | -11.19391 | -60.63292 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74f57b97-9505-3884-a651-f9d17535d595 | -11.18793 | -60.44894 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 478684b5-2423-3ee5-a006-c5a0409110e3 | -11.18779 | -60.62831 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 895d6680-ab5f-3a97-992e-e62dcb03bfbf | -11.18574 | -60.46327 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f617a165-b35b-3cc2-a795-81f8f7029ae7 | -11.18404 | -60.452 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eef9b00-1ddf-3294-93bb-8fea465be458 | -11.18349 | -60.45558 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b197a33-f6e5-3ff7-8cce-cf68af3e19f0 | -11.18295 | -60.45916 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a4de52-ca50-3ade-828d-7ea78668115c | -11.1824 | -60.46275 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128f7a2d-7676-30cd-9f2b-c2e411d6a7e4 | -11.18015 | -60.45505 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7233638-5839-30a3-b5d1-9c496af6eda6 | -11.1796 | -60.45864 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 638c0deb-8dfd-34eb-a929-e840e415cd83 | -11.15887 | -60.61644 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1914737-aa39-3997-875a-890793b0f3b0 | -11.15564 | -60.65975 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5256edc-80b6-38a9-a5c7-7b66705dc32b | -11.15554 | -60.61591 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 148652e4-a091-37c7-b603-5e52309e2a58 | -11.15499 | -60.61947 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 829180db-ad74-34d6-b94f-11b4a803d118 | -11.15275 | -60.61182 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c544029-f51d-3031-9940-867348df5651 | -11.15166 | -60.61895 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24f9083f-9108-32ed-ae41-e4cb115db618 | -11.15111 | -60.62252 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53ff126a-ec6f-3358-988e-d611a0c678d0 | -11.15056 | -60.62608 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23eaad4c-dab8-3aea-8f27-78824fcb1c33 | -11.14941 | -60.61132 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd0db3a0-f66b-3951-8436-c45cf1811e67 | -11.14777 | -60.62199 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ca0dd50-c31c-36a2-b5fb-f154e8ad2be4 | -11.14723 | -60.62556 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f69126b-fc99-347a-ae34-2053c277269b | -11.13838 | -60.63877 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75cbf06d-195c-34d4-9bbc-d4946ac41a94 | -11.13783 | -60.64233 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429d52b3-038b-37a7-bebe-6b629d6aa9d3 | -11.10737 | -60.6012 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 086ed40a-0aed-3772-89fb-3e4725620270 | -11.10156 | -61.38023 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README124.md)
