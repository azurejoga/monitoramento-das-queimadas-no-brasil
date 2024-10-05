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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c46f0203-b4bb-3051-94fd-0be92fd3caff | -17.01241 | -56.69508 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 7ba1c8bf-75b1-3fc0-a388-081ca186f0c6 | -17.01077 | -56.78857 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| cb59b146-357e-38d0-a741-c3f29ad6946b | -17.0106 | -56.73204 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 59dff782-ce50-3639-8bdd-61a2c882c6b8 | -17.00981 | -56.79306 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 248ebff1-49fa-3a5d-a6a6-1e16816dd2b9 | -17.00963 | -56.7365 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 45924c8a-6252-37ce-9813-3b3f282b78f4 | -17.00866 | -56.74096 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| f4c2f51c-f688-3248-b2bf-c460cac4f992 | -17.00487 | -56.78716 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 3b28f53b-2c73-3b4e-9607-8106c54bf316 | -17.0039 | -56.79165 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 6db4a441-6afa-3c07-85fa-3bc9a71521e6 | -17.00277 | -56.73957 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 75888da9-7a06-31b9-b387-0ad8cf41cf9e | -17.0018 | -56.74405 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 89b89223-f923-3f12-83af-cc0834eb5bc0 | -16.99994 | -56.78126 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c9643b35-8f7b-36c5-ba6e-a37f235e737f | -16.99897 | -56.78575 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| dd70f943-f114-31e6-ba0d-2c07b144c142 | -16.9989 | -56.75745 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e0d5a04a-3336-332a-b2d2-109889ef64fc | -16.99799 | -56.79024 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c0317812-4614-357f-9880-37699cdbc15a | -16.99793 | -56.76191 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3a414988-8d6b-3738-98d4-37990f03802b | -16.99702 | -56.79473 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 917e0303-43c6-306b-8ae1-e86dd00db15f | -16.99696 | -56.76638 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3f704481-aa56-3fef-8cad-50177677abff | -16.99688 | -56.73818 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 12ca193e-75fa-38b1-a5f2-00922f4f686a | -16.99591 | -56.74264 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4e0d7f53-fdde-3b64-ab4c-79ec062d1f71 | -16.99501 | -56.77535 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 050c8d5c-bc9e-3daf-8692-953c09c6349f | -16.99404 | -56.77985 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5a633909-4cfa-3e8e-9109-9c14cd47af00 | -16.99306 | -56.78434 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 35f06cc7-bf3a-358d-bb5e-15cfb2df7706 | -16.993 | -56.75603 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9da45d7a-f1e6-31a2-adea-a3d4195650aa | -16.99208 | -56.78884 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 6dc359dc-7c42-387f-857e-66c46e083879 | -16.99203 | -56.7605 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 355d2e43-7a43-3f35-9fd4-fa4354e492ea | -16.99111 | -56.79333 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| f7d39b2c-8861-3e33-8729-d5b2ff52f6da | -16.99106 | -56.76498 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 33aaf8b6-b2e2-3d01-b9f0-80753a8a0926 | -16.99099 | -56.73677 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 0019e946-f271-305b-9ffa-d07999932d01 | -16.99009 | -56.76944 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c46e16c7-8ee4-35fb-b450-b96de5dd0803 | -16.98911 | -56.77394 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b146ffc5-d8c9-3f22-99ae-a9cb1941327a | -16.98905 | -56.74571 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f3e31143-da92-38cd-895d-78d8743a37ff | -16.98813 | -56.77844 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a37f5ba-f4a2-37d9-9552-b18d17879e5b | -16.98808 | -56.75017 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 94f05023-06e6-3726-9834-1f396b0bf5e4 | -16.98716 | -56.78293 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| b16676d4-67a9-3ae0-9683-eb88456115de | -16.98711 | -56.75462 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3b2548b6-cfab-3806-9dea-cc75e3e2c454 | -16.98618 | -56.78743 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 5d93ca85-51d6-3998-940a-331eba1ff6fc | -16.98614 | -56.75909 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 75c73169-6204-3b10-8c6e-9ca6493ded55 | -16.9852 | -56.79191 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 83f18957-e3e6-3018-b13e-3d3fd3884f19 | -16.98516 | -56.76357 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 4531dfbb-786e-320e-8381-1bd509cc4186 | -16.98423 | -56.7964 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 22962d07-2216-39ee-b0f9-152521f9997d | -16.98418 | -56.76805 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 291461e3-6cbd-3a98-9228-6c1386cd7897 | -16.98321 | -56.77254 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| ccce5fe7-6903-33df-a00d-8508bec8f06d | -16.98223 | -56.77703 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 2c0eb551-51e8-3946-af45-1b47fb25c01e | -16.98125 | -56.78152 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 3d224cd8-5f80-3c56-97f8-9157cc4a72ec | -16.98028 | -56.786 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| d39299c2-8fcd-3072-bab4-494ffc549db1 | -16.9793 | -56.7905 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| b5ed3d65-f580-3143-b02c-9fa53b467a21 | -16.97832 | -56.79498 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 84db62c9-654e-34d9-a847-8951ec525f18 | -16.97828 | -56.76665 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 70824e14-6901-3f93-9fdc-78218a54a965 | -16.9773 | -56.77115 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| e1b4a02c-dffb-3bad-bc02-0b99d5264fc4 | -16.97633 | -56.77563 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 08d11ffb-ddae-3c43-8d3e-d70ff54dba8f | -16.97632 | -56.76501 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| c36f2269-04d8-3e5e-8bb8-2e97004cc335 | -16.97537 | -56.76953 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| cf1e5ab9-19e5-3578-a35a-d7ea0767c1ac | -16.97535 | -56.78011 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 89f6abc0-a676-3648-825d-7aa99f1c716f | -16.97442 | -56.77402 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 07ca9226-725f-3ba4-abb6-56eecfbd2f29 | -16.97438 | -56.14798 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| b2dfd238-cbff-3dd0-838f-29651d01d3f1 | -16.97437 | -56.7846 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 260b51a6-abd7-3c8f-9abc-37e36ced1e06 | -16.97347 | -56.77851 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 30d32486-2c09-37b2-8b6c-259700a60161 | -16.97252 | -56.783 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 9ef2a8e0-402f-37fa-86cd-f991bff0fb83 | -16.97238 | -56.76525 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 6ff94732-4daa-3a72-80bc-c3dbdc06ad83 | -16.9714 | -56.76974 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| fe8aaaec-e114-3ae7-9d43-cd17f8ace62f | -16.97042 | -56.77423 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| bb815f09-655f-37da-96e1-74dad02174d5 | -16.97042 | -56.7636 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 3ee080f0-046b-38a1-bbfd-f85b32a28a7b | -16.96947 | -56.7681 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 785c80d1-785d-330c-88dd-68b496a4a6d5 | -16.96944 | -56.77871 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 9afc2b51-877f-3352-9442-085b6247b7c0 | -16.96869 | -56.14665 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| a273c7bc-a7ac-3700-999f-f70d1e13c842 | -16.96852 | -56.77259 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 295a609f-dfb0-3272-a0ba-cef7f3b4438d | -16.96846 | -56.78319 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 9e71a2c5-d63c-3939-9efe-9467611e09a4 | -16.96757 | -56.77709 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| cd472717-c46a-3ac5-8117-a47b6b0c339b | -16.96662 | -56.78158 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 29c46ecb-74d8-3152-a38a-1996ab395dc4 | -16.93248 | -55.83914 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7f4d80c2-28d0-33b6-9401-0827a71ffe4a | -16.93163 | -55.84308 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2d057c24-5fc3-37ed-9e8a-e22d8882adfb | -16.9298 | -55.84049 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cb623920-2094-34d0-af3f-4cd94040567e | -16.92774 | -55.83392 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 37f4848c-ee76-3c71-bb4f-c9983f1e670a | -16.92689 | -55.83786 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b134d723-05f3-379d-adad-7398b6c9f35f | -16.92604 | -55.84181 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| eb695ef7-dc2c-3dd8-8aed-262b718cc2bf | -16.92584 | -55.83133 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c1493ef3-5be5-3225-bfd7-4b9eb6ee43f1 | -16.92502 | -55.83527 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 366e5781-6d02-39ed-b342-7aaf42df64c7 | -16.9242 | -55.83922 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0a910598-4fd5-3256-9c82-f249c6cfa299 | -16.92338 | -55.84317 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fa821a1e-c77b-3572-b2bb-462163ed01aa | -16.92188 | -55.82221 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 44d226ed-f498-35ea-b0f8-ece73e769bea | -16.92107 | -55.8261 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| af90c44d-c60b-3e42-9934-912a23ef8ec8 | -16.92026 | -55.83001 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 27586e99-2b45-3e74-9e57-8eb32fa9badc | -16.91975 | -57.7015 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d088014c-27da-311c-b40f-aa25c68ec5c5 | -16.91548 | -55.82486 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 39119f22-a545-3446-8ea0-0b17d169586c | -16.91466 | -57.69481 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a1bbc0cd-da78-3762-8375-a75da77bbe2c | -16.91466 | -55.82878 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| efd237ae-b409-3bec-8ab9-c9b19cccbcaf | -16.84477 | -57.46195 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| eefd83f8-15a9-3b2d-89eb-3b284ea10fd0 | -16.83862 | -57.46045 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7d35cc78-b133-3c92-810e-b5ba21a18ae7 | -16.83245 | -57.45896 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fc3665e7-d67b-3609-992b-ba97d240fbc3 | -16.83136 | -57.46393 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 691a5842-4b8e-37dc-bd81-30e3ad0ee722 | -16.8289 | -57.45765 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d0a945a8-8fac-3032-a813-d33eb1116f43 | -16.82782 | -57.46265 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c3f03733-3fd1-3762-9415-e2fd4c5c0c9a | -16.82519 | -57.46245 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6c7888e4-87c5-3411-9313-241b9c184b7c | -16.82178 | -57.81493 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8094b2c2-11a7-331f-a1d3-1d26a5fb96c2 | -16.82166 | -57.46114 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e5109205-5f32-3ac0-9ccb-9be4524a10ae | -16.82042 | -55.90281 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c9cf8d65-5358-302f-a6f4-c275babe3c61 | -16.82014 | -57.45597 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 78da977a-c082-3f9a-8775-2463250a8a14 | -16.81959 | -55.9068 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7845aa20-14e7-3020-95fd-563c8bbdad0a | -16.81903 | -57.46096 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 59b172a8-3074-385f-9f61-3ea06ac0d94a | -16.81705 | -55.90113 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README84.md)
