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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bccccd7-ecb4-3179-a5d3-dd6c52820523 | -11.19355 | -47.56409 | 2024-10-25 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 634f8910-6e6a-332d-b7a4-a62a08692c97 | -11.18713 | -47.50869 | 2024-10-25 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 347e35cf-7ce2-3e51-bd25-5a27fc436cdc | -11.18653 | -47.51281 | 2024-10-25 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 545bad54-c4c2-3883-ab3e-5014d88b4794 | -11.18356 | -47.50813 | 2024-10-25 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ff1e33f-baa8-3d80-9eeb-76a7cca25b34 | -11.77845 | -47.07681 | 2024-10-25 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c843b19-1904-318b-984e-f320abd82626 | -11.77477 | -47.07627 | 2024-10-25 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d10a629b-7117-3742-a76b-c44e661cbbbc | -11.69734 | -47.12446 | 2024-10-25 04:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe6b9bc6-3823-320b-ac48-487f5d014200 | -11.69368 | -47.12391 | 2024-10-25 04:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5401234-55ff-3f7a-b4d9-1d272278f85e | -11.69304 | -47.12824 | 2024-10-25 04:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e39c7cd-301f-391a-af0a-155cd3563327 | -11.69001 | -47.12335 | 2024-10-25 04:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e69f6f5-27e0-3730-b592-f61baa157efb | -12.56766 | -47.06839 | 2024-10-25 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85122cf8-2cea-3ba3-943b-55a7f1134a32 | -12.56285 | -47.04908 | 2024-10-25 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99e2ad3d-c08c-38b5-a6ca-1828b959f7ea | -12.51145 | -46.87299 | 2024-10-25 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ee664ee-c105-3e00-ac2a-784cde8540b2 | -12.51119 | -46.87483 | 2024-10-25 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 915a1bd2-cbd5-3d48-9695-55e6fe85433c | -12.36473 | -46.90215 | 2024-10-25 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6257cd91-06df-30d5-b5ba-67e0e147798d | -13.53114 | -47.3319 | 2024-10-25 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95fd2a3e-d838-37ce-ba67-11d526799036 | -13.38423 | -47.8464 | 2024-10-25 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5d9ae2d-b732-3364-8675-eb5326d9822e | -12.93523 | -47.6878 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2b45e70-a689-3801-a26c-6e5bff99662d | -12.93433 | -47.68864 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac3866c1-9a86-36e0-b8c6-63d562231905 | -12.93163 | -47.68709 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0b2e7eb-5965-3d3f-b0f6-e12674163d83 | -12.93074 | -47.68795 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa20ac63-6a85-3111-88bd-8587ae751782 | -12.80077 | -47.89893 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60d3d63f-1ea3-3ef2-9107-9af93fe2df67 | -12.79958 | -47.89616 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 169f3d70-5bda-39e4-82a5-cdcfb28deb5c | -12.74053 | -47.41341 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a7f5d5f-bc44-32e6-927d-4560fdc338da | -12.70951 | -47.96274 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11e78006-37f4-36bb-8dc5-de87cf8ae5e0 | -12.61116 | -47.25329 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea66b63b-f91a-33ac-bf09-38e5797216df | -12.61053 | -47.25767 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc529283-332c-3cca-ae4b-9659aa14acf4 | -12.49825 | -47.28756 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38caa7f5-05a7-32d1-9bf6-30590a734756 | -12.49762 | -47.29194 | 2024-10-25 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fd20099-ce65-3059-9360-8e0ee091bd30 | -10.80537 | -48.61545 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0c738e5-0be2-3fe3-a918-be1a345c711a | -10.78362 | -48.55106 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78c1ee28-f66d-3fe8-972b-31c1519adb83 | -10.78307 | -48.55471 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6db37b9-a80a-3df5-8485-bda3b8673657 | -10.75227 | -48.53175 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 782e72d7-8880-3782-b832-d7f0576752ba | -10.69224 | -49.1077 | 2024-10-25 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9847a64-caa7-37dc-9d7d-486fdebb2d27 | -10.68887 | -49.10717 | 2024-10-25 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53b6bfa5-d6d7-3dbc-a434-f7aae2c0b7e4 | -10.68832 | -49.11079 | 2024-10-25 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95f3e046-fbe1-35e0-a510-9a19b3060e9d | -10.6855 | -49.10664 | 2024-10-25 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bec066d3-7891-3b01-a519-de05872446d4 | -10.68495 | -49.11025 | 2024-10-25 04:40:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fee9878-1bfa-3b41-98f7-6955f77a3698 | -10.55569 | -48.74435 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4875d071-4fd9-398e-9e72-f7a33d9d4cad | -10.55229 | -48.74382 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56abb46e-8cdf-3518-b3d6-ff48fa391131 | -10.38629 | -48.82321 | 2024-10-25 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ba5337a-c916-34ab-832e-075603518026 | -10.33912 | -48.63187 | 2024-10-25 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 690f93c2-dd29-3be8-ab1e-b141291be4ce | -10.28948 | -48.89013 | 2024-10-25 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc654901-cd46-3167-aa27-b1bdfd4cf1cb | -10.28892 | -48.89376 | 2024-10-25 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65e43947-932d-349f-9992-ad640648574f | -10.71286 | -48.05678 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49a4c807-46a0-3afb-8a0e-20ad1fdab6e5 | -10.7119 | -47.94521 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abd352e7-1f5f-344a-a5c3-8ba5a92ec4d1 | -10.68002 | -47.79866 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4050851-cb0b-3cf1-96eb-7491acee6a40 | -10.67355 | -47.8181 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a6706a5-4ce4-36b1-9573-215b0b901d28 | -10.67296 | -47.82215 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 275899d4-17b2-38b1-a92b-dbe3fd04dee3 | -10.65307 | -47.93232 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74f7109c-0f67-38c6-b669-418dd8f8de78 | -10.6513 | -47.92015 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 806612ae-92e1-351e-8df7-589080f6b820 | -10.65073 | -47.92401 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8fa2de32-8f69-3def-b358-78b02912c916 | -10.64781 | -47.91958 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b397f03-28b2-3fe5-96e7-3df2870a3c48 | -10.64724 | -47.92342 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 829bd1d1-ed35-30c9-8bd2-413b04f93852 | -10.64376 | -47.92279 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4af88a32-dfd3-32ff-bed6-ea49705e3b68 | -10.52529 | -48.13829 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cfd7161-ee7b-3f4e-9501-6054397cdec8 | -10.50855 | -47.66875 | 2024-10-25 04:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97352e40-5871-37da-8adc-cd909fcc0bb6 | -10.47548 | -48.28248 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d080b6ac-cf5c-35f9-bb7c-3ba85448ff0b | -10.47293 | -48.28213 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6deeff7c-0c9a-3c1e-ba02-28c5d4560c32 | -10.47235 | -48.28592 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6064828e-05e3-3dc8-b6a6-acf452936787 | -10.47203 | -48.28197 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 338e55bc-9f8c-366e-978e-734d51b73c9b | -10.47146 | -48.28576 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8ce7aae-4623-3dec-bd30-4149cf62f11e | -10.46948 | -48.28162 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa211c2e-167d-3a8c-8e86-41cf90b88b44 | -10.4689 | -48.2854 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8398da09-f090-3a6a-80e9-1f68793abbce | -10.46832 | -48.28919 | 2024-10-25 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89aa4f4b-5f74-3dcc-8a74-33b783bca5f3 | -10.44349 | -48.07984 | 2024-10-25 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e2414f0-4377-3ea6-918e-43155a282d6c | -10.44291 | -48.08368 | 2024-10-25 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e057472-a52d-35c6-b306-0d24f4f8c79a | -10.44002 | -48.07929 | 2024-10-25 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9502f8b8-5e5a-367a-a673-5de622c51b40 | -10.43944 | -48.08315 | 2024-10-25 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b65ea47a-29a0-3d5c-a9b8-63b96812657a | -10.43887 | -48.08699 | 2024-10-25 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 15093170-c3bf-3681-86da-42ea39179abc | -10.43598 | -48.08261 | 2024-10-25 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8056b769-acc8-32f2-9f99-56f7ba2d51b8 | -10.42336 | -47.5176 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2eb9144-cd01-388e-8fda-ac57667210b8 | -10.42276 | -47.52163 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40dece89-1e30-365a-8917-6c3847ede968 | -10.41981 | -47.51707 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eac7d83c-e7ed-3f8c-b5c7-7fd787e25322 | -10.41921 | -47.52109 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6e1ec66-2433-370a-b7ea-3d96780cb386 | -10.41626 | -47.51652 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75dde39b-05c7-344d-8d30-2c3013719aef | -10.39845 | -48.04865 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4c1bd3c-4905-3579-8b01-181769454531 | -10.3971 | -48.0494 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4c72035-5c6b-3cd7-802d-89e5a3813d68 | -10.36232 | -47.51786 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bf50050-1381-3a88-92a0-c6e1e8f26fc3 | -10.36172 | -47.52187 | 2024-10-25 04:40:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acf6a99b-2779-315a-9919-d9187d0e1ca1 | -10.91357 | -47.82493 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f894d0f-e323-3dc8-acf6-3a684207b00c | -10.90948 | -47.82824 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34be29ce-d6d1-3ac8-b046-81512af48e2e | -10.90596 | -47.82767 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa2c63a1-e829-3bf4-92c4-a571c63778a7 | -10.90244 | -47.82714 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 891ffd3c-2d5e-3bd6-b697-f776cdf4dcfc | -10.89892 | -47.82664 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168f2197-5fd0-350c-a072-46377b15bfc1 | -10.89599 | -47.82214 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a7172f9-aded-383e-801d-1804b35f64cc | -10.8878 | -47.9258 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1ee2942-1f3b-3ced-ab6a-ad5b5410fb80 | -10.88545 | -47.96569 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cfc2eb8-965c-3958-8512-41cb6e7c84ab | -10.86272 | -47.80568 | 2024-10-25 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 816add22-045d-302f-8d1e-ddd04f04b04b | -11.63463 | -48.47287 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 094183a3-9558-3b55-93ea-74a1ba146300 | -11.63336 | -48.46963 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f4f440d-f7d7-3c17-81cf-c4aafe68634a | -11.63277 | -48.47345 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 513024a3-783e-3a53-a38c-af267c1adf85 | -11.63174 | -48.46851 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08a0a109-8054-3033-8545-31e79811d32a | -11.63117 | -48.47234 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b67fc0a2-143c-3dd6-8644-46d0a5cbe7c1 | -11.6299 | -48.4691 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3e2d864-f8cd-3076-8aeb-0ea2a5006d0e | -11.62932 | -48.47292 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7c54080-f626-3623-b408-0c914cdc7ab8 | -11.60051 | -48.59285 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6edbb4d-92ba-3abe-a866-603930259c52 | -11.59994 | -48.59662 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8bda4ef8-a9dc-3392-8fdd-b477635d9354 | -11.59937 | -48.55397 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8877d097-1be4-3a80-be80-b00dca88b8df | -11.59707 | -48.59231 | 2024-10-25 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
