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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d289030a-d716-3253-8610-c2bee17a264d | -10.52235 | -46.06943 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b7ceffe-dc72-397d-9166-7b46fd60bec1 | -10.52145 | -46.0503 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90bfb1ec-cca1-35b6-8246-f74e68860a16 | -10.51767 | -46.07242 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efe5ea31-3731-3132-9164-c96d4d8fd647 | -10.51705 | -46.07609 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2547c168-d84e-34bb-b122-a15615a22472 | -10.51614 | -46.057 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0742ac5c-e4fb-3a7f-9a08-3aec71e0dcc1 | -10.49026 | -46.32299 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 07dc0d49-3791-35ca-9497-6861826adc91 | -10.4882 | -46.31896 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d4c59482-5989-3bcd-a045-ddf7bd99d0ca | -10.48755 | -46.32277 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 139306da-f403-38f3-8e38-2d17ff9849a0 | -10.48683 | -46.31843 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ee038b5-107e-3096-9b17-9c41af0edba0 | -10.48616 | -46.32222 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 05378b40-41dd-3a56-9bce-f8b82d773c40 | -10.47607 | -46.34025 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ef2fcf9-dc4a-3e5b-a370-0e09cb0cf5ba | -10.47196 | -46.33949 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a92d826-686c-3027-9539-146425ee9c3b | -10.47131 | -46.34327 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7e12a65-ba06-3ca6-90cd-9846c9ae7a20 | -10.45031 | -46.29283 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e8a29a7-9913-3afb-ab2a-5e6717ddb80d | -10.44965 | -46.29662 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba68d844-e92c-38d4-bb2b-2e282d3f492c | -10.37062 | -46.19722 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9c64de6-7858-3c8f-8b71-b6f9c8a8c664 | -10.36635 | -46.17314 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87ec3b77-3f7f-35ec-adf6-a54af1154552 | -10.36292 | -46.16868 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9489fa12-8b87-3b4f-92a6-61e0852ce1e3 | -10.3283 | -46.17405 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d676b9f-39fa-3bf4-955d-4bdf76c90519 | -10.32764 | -46.17781 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f187707b-d7d7-3da3-9a6a-61ebc04f0918 | -9.54939 | -46.51968 | 2024-09-29 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae27dcee-72d9-3730-a2fe-f4e9619cc9a1 | -11.31571 | -46.30089 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3901f8a0-6e8f-34ca-a9eb-a241ba01855c | -11.31508 | -46.30453 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e5f8b18-8863-3960-a813-648a0a4fc138 | -11.307 | -46.1607 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a8873e9-11c3-39a3-8aba-b37491850ea7 | -11.30633 | -46.16446 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a57272b6-39bf-335a-add2-ed2876d96cdd | -11.29489 | -46.30043 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87c8de6e-73e3-376a-91ea-26c93c638bab | -11.29427 | -46.30395 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a0122e8-6986-39ba-8f55-500fc3cf009c | -11.69611 | -46.35455 | 2024-09-29 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 159312ac-e201-3160-9400-4fd97adb35a8 | -10.91965 | -46.38331 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65314291-f52f-3b38-960d-98d342abcb9b | -10.91897 | -46.38712 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7bcb1952-f40f-3260-b97e-ba1a797f87d3 | -11.4572 | -46.95835 | 2024-09-29 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5210211a-9229-3a6f-b035-06ed0fb3852c | -11.45715 | -46.95786 | 2024-09-29 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 885fb20b-649d-3594-a3f3-f10d7b0df01d | -11.45299 | -46.95749 | 2024-09-29 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58f34eb9-fd0a-372c-b30d-6cae6c43d2c0 | -11.41583 | -47.23317 | 2024-09-29 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba880aa0-31be-3d81-81f9-09adaca8e6cb | -11.41359 | -47.23359 | 2024-09-29 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d256d8ff-9d40-3107-9a3f-d55ea2039f33 | -11.41287 | -47.23774 | 2024-09-29 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8a57993-a201-3e99-b2e3-90f12c9faddb | -11.41077 | -47.23652 | 2024-09-29 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3464453a-0664-36c0-98f3-b0b7191be493 | -11.41071 | -47.25011 | 2024-09-29 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 004eccf9-bad3-3e66-9011-e4888ac8c0e4 | -4.58379 | -47.09635 | 2024-09-29 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65bc86a9-ea38-3842-9f99-490d6e313883 | -4.49002 | -47.75599 | 2024-09-29 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc190e16-f8cf-3831-9594-1000a9354d83 | -4.3799 | -47.61341 | 2024-09-29 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 587be6b3-fa00-3838-a89f-4232e9d9c884 | -4.37495 | -47.61241 | 2024-09-29 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c312a913-c01e-313f-88c9-5200b6f761d9 | -4.43962 | -46.34297 | 2024-09-29 04:02:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 763e1bc3-ed3b-3cae-bbb0-a551fc4a5c3e | -6.15793 | -47.70732 | 2024-09-29 04:02:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a185e9d-6df1-3ae2-b322-ed1ad040d1af | -6.07891 | -47.65357 | 2024-09-29 04:02:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5a679236-4f79-374f-9295-2d4875a8d0be | -5.76755 | -46.55407 | 2024-09-29 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8842e291-6133-3fff-a86c-2baacbaa903a | -5.40388 | -46.57961 | 2024-09-29 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4fbe49b-2ed1-3ede-adbc-06e67b07dae4 | -6.1619 | -47.71328 | 2024-09-29 04:02:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af09e924-9ffd-32b7-b451-3c4a819311ba | -6.15699 | -47.7127 | 2024-09-29 04:02:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f169de5-21a3-3c46-bef6-2570984b2ffa | -5.39932 | -46.57888 | 2024-09-29 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7083b36b-0926-3881-940d-f3edc1248e53 | -5.39853 | -46.58358 | 2024-09-29 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32a06105-f233-3786-93a6-984592aac034 | -5.24312 | -47.38752 | 2024-09-29 04:02:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87070050-90e7-3978-a234-e24c6c72763b | -8.34252 | -47.53817 | 2024-09-29 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a39b843b-e15c-327d-826e-43fb40f7718e | -8.3186 | -47.54639 | 2024-09-29 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9d34a4b-2182-384c-8042-c69d9eccdc19 | -8.18525 | -47.67644 | 2024-09-29 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cab9473-edec-3cc3-ac10-104eff1e38a7 | -10.82296 | -48.12111 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7536355a-29b0-375f-91b4-ba72fd94415c | -10.82218 | -48.11987 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2f0b09fd-dcab-3048-a885-beba74c93d5e | -10.72185 | -48.73985 | 2024-09-29 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7369861-6af9-3aa3-93d9-092ecaab4b38 | -10.66259 | -47.93316 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be034c06-7b02-3b05-8ae5-b63d72615b03 | -10.6581 | -47.93193 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d64d16-be87-376e-9f87-897e650448a7 | -10.55147 | -48.05135 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 337306fa-335f-347a-8d3e-01fbee999261 | -10.55062 | -48.05607 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bda01599-90e3-3165-9472-2a6fd70819db | -10.54779 | -48.04537 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00cc771f-9a58-349a-943a-fe70fb715639 | -10.53519 | -48.03609 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77e2eb6d-ccd6-3078-8f6f-9d1e52a8d11f | -10.53243 | -48.02514 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71a13058-fd0e-3c4e-88c5-9cdb806551f1 | -10.5316 | -48.02972 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60bd852f-c60c-33c5-8ced-5acc9a954ed9 | -10.53071 | -48.03458 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76c06d23-f07f-3592-b89f-d3f5fcc59a83 | -10.52784 | -48.02421 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b4200d9-5825-3778-ac84-bdd1d7f3df0a | -10.52701 | -48.02875 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2f5573b-d1db-3686-829a-881fbb7f7408 | -10.52613 | -48.03355 | 2024-09-29 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc3d8388-45a5-3ba2-87ea-0c07202096ab | -10.43515 | -48.19939 | 2024-09-29 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ba43646-f587-3b26-9021-81d684729403 | -10.43039 | -48.19899 | 2024-09-29 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5062463-10ab-3fff-86f8-4be954d6ee31 | -10.42381 | -48.18205 | 2024-09-29 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b86310b0-a69a-3c56-98bb-7b19f9b9eadf | -9.89161 | -47.40992 | 2024-09-29 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bd417d9-4a4d-3287-9c92-75009741ce21 | -9.89082 | -47.41433 | 2024-09-29 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b334035-b6d3-327f-8039-97cc363542be | -9.88636 | -47.41348 | 2024-09-29 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66ef83ad-9bf1-3371-b0ee-9ad470027712 | -9.88556 | -47.41795 | 2024-09-29 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2364166-be89-3176-a246-a665d425eed3 | -9.5362 | -47.78561 | 2024-09-29 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4dabe317-15d9-311d-9b1c-49262f16a9d2 | -9.53157 | -47.78487 | 2024-09-29 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56f19835-ce6d-34d5-8d58-fe9e88db79e1 | -9.5009 | -48.53559 | 2024-09-29 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8858d95a-26ea-3fc9-b50d-b580220eeb36 | -10.23845 | -47.76931 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ff22e8a-be8c-3550-be5b-456eaf2e20c9 | -10.23839 | -47.76638 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47e7c45-8a8f-3394-9068-3511f4e618ff | -10.2375 | -47.77147 | 2024-09-29 04:02:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 896ac1af-c04c-3291-b0f7-937ec737493d | -4.91887 | -48.61544 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5032df21-4a82-304f-bf73-8878d3c537f8 | -4.91474 | -48.60792 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a82f59a-78bd-3550-be1e-1bee63e88f9e | -4.91418 | -48.61115 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2531bab-2009-3501-99e3-3763d2a43080 | -4.91303 | -48.61779 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a3ce7fd-f596-35fd-afaa-7ab7b4ce6c53 | -4.82925 | -48.54049 | 2024-09-29 04:02:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1bbc0a-8d55-3d92-ae26-850e44d44e16 | -4.82398 | -48.53965 | 2024-09-29 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e125e3a-7f60-3c7c-a3dc-5ec9a23b44d5 | -4.63089 | -48.53301 | 2024-09-29 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b57fdcc-e306-3a61-a282-3f9e5b32e6d4 | -4.63031 | -48.53641 | 2024-09-29 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 632aaf75-56a7-3655-8791-8b39d0fc95b1 | -4.49034 | -48.12011 | 2024-09-29 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc9f5af5-b576-339d-a95a-4db9b8974453 | -4.22625 | -48.58941 | 2024-09-29 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3133c29-7ec9-365a-8aae-b104172e5507 | -4.91944 | -48.61216 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e037322f-156f-3964-8e27-360d2b450fe4 | -4.9183 | -48.61874 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b46386e8-e392-398a-875a-ce2c7f42b41e | -5.95812 | -49.18243 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 477483df-e48f-33cd-bdc3-a5863272e825 | -5.9575 | -49.18588 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d42a273b-34f3-38e9-b0e5-f785f923206e | -5.94997 | -49.18256 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e60deab0-772e-38ce-be7e-2679daedcc63 | -5.93077 | -49.1972 | 2024-09-29 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ab956dc-b0e9-3a03-9b04-71d396327dcf | -5.57219 | -49.01585 | 2024-09-29 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
