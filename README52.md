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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8c81afe-56d0-3dd5-9573-ff2154af9cd2 | -1.63378 | -52.6271 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2382cb15-324a-3962-b5d0-06f3d3fca337 | -1.24623 | -51.78605 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5253935d-c1f9-3afa-8425-1fb9c0a97cbc | -1.45143 | -52.66241 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 001dbea2-37d7-32e5-9a70-29351556e6a1 | -2.03565 | -49.00174 | 2024-11-21 04:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92be84fe-6596-3ca6-b769-027cf8afc511 | -0.96453 | -51.72102 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0aae077c-0167-3b4d-8ee8-3c8441fbc809 | -2.57398 | -49.09308 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a21734c-bf6a-3410-80b6-31bc99f13a84 | -0.89536 | -51.72479 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a958e4-a92b-38b7-981d-f768d2d53e49 | -3.2296 | -43.27185 | 2024-11-21 04:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55cf8723-2185-3d8a-8af8-81d7613e08ac | -1.74697 | -52.05777 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73f890db-a964-37fb-8838-e8855e061d81 | -1.62649 | -52.58714 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 078f665e-0e82-349a-a118-9a1533999351 | -2.20992 | -53.71735 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aa699ea2-f78b-3b66-8e12-5b05a58381fd | -2.17702 | -52.13183 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67d32d27-502c-3152-8ea4-7a54d7102804 | -2.02239 | -51.17487 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79c8f355-5745-35ef-b0c8-0adfce3b0c16 | -2.2847 | -48.40845 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddd71861-b06c-382a-ada8-c51ff617dfa9 | -1.73076 | -52.70247 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b210e21b-71ac-3d66-9c22-8572538cdd2f | -0.78552 | -51.77646 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a0434a2-90eb-39f8-b44d-f7f63aa0ec49 | -1.25404 | -51.78001 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb9024e9-1a78-319c-8ad7-ee9ba7a83794 | -0.88866 | -51.72375 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74afc30c-7848-3f78-bbf4-00ccbb04a93c | -2.20689 | -50.69344 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e417fe90-6887-3f54-b561-bd1b12f5ce1a | -1.24219 | -51.61459 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 459b2c63-4150-3d56-a2d7-93de2dfb5191 | -1.51389 | -52.22242 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c2525f7-c451-3b21-822f-5a4cdf9d43d1 | -2.15181 | -50.49231 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a912fe5-e24d-38f6-8db0-e87f32c5b534 | -1.71009 | -52.48694 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 438ebef3-dff5-3da5-ba82-0b34767faef3 | -1.4699 | -52.80649 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c0ea2c-07cc-3e87-a802-040daaadb2df | -1.97153 | -53.13793 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57f92bc8-8ac7-3bc5-a5b4-b29192150bc2 | -1.4822 | -51.13155 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be07b189-ec1d-3dd0-8ce4-e576d14cca7b | -0.85464 | -52.52711 | 2024-11-21 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a4245cc-fab4-3d5b-88a6-42841193ef20 | -1.14102 | -51.69766 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61b717da-9dc5-3adf-8922-1c114c2b7fea | 0.10071 | -51.21109 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb7f5faa-aef3-3884-b0db-b09558ba2839 | 0.84907 | -50.13639 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbb42f5d-03e6-36ec-942b-98bbf22aa03f | -1.20605 | -51.77983 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f2ad59b-491d-35cf-bea0-603f2f06d894 | -1.25627 | -51.76587 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7a850df-6a1f-3489-a302-04012726e0cb | -1.21723 | -51.79604 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a68cb0bd-3983-3d29-a7f4-58b2cb38c95a | -1.73692 | -52.38153 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc4be1e3-7514-3815-843a-de1dc328daa8 | -1.2027 | -51.77932 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95056156-a7f6-33f9-bd36-0225e7e50434 | -0.24894 | -51.03938 | 2024-11-21 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d8a8b38-2278-3b0a-a1b3-b843b215323c | -2.3862 | -48.92818 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c3976a2-4c1c-3bc8-afed-29a6695f8961 | -1.22218 | -51.74249 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 424af7c5-3e0f-3f89-aeab-18fd8119806d | -1.96175 | -53.00639 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 378e7d77-e788-38c9-a13f-8fb5960e22ad | -1.47126 | -52.01556 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a4d293-a125-3ebe-bb72-955beb37b799 | -1.42367 | -52.40736 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23c2b31f-e78e-372e-a6f1-eee63dde57e2 | 0.90367 | -50.14361 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f64e2dc6-99e2-3c9d-96d9-fe78ef1c105e | -1.4732 | -52.80701 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d996e8f-700b-358a-a679-032500eb7aef | -1.12221 | -53.3947 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6d2ffc6e-fa72-3c92-9fb6-add08fd27e01 | -1.36691 | -55.69637 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bae1b2df-1a52-3611-9897-f7b09ee9346e | -2.06377 | -53.43681 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fe155cc-3c82-37f6-a09f-97a07848611d | -1.20582 | -51.97787 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f9ca7b9-d710-3234-a3c5-4447329656f1 | -1.39368 | -51.58291 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 444fad3d-731b-3d32-963d-b1e9bf210c86 | -1.23898 | -51.78854 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae7686d-bf23-3d39-85ea-23c00a93d3e2 | -1.79036 | -53.61993 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93790f4d-a4e3-3add-a872-62ba29176072 | -2.15788 | -50.91416 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c5ab0e2-efcc-34f2-a8de-a9a10ecc689d | -1.59385 | -47.49168 | 2024-11-21 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2aa6d74e-79dc-369d-86df-025f9979cb1a | -1.31334 | -51.8758 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 359269ba-7af7-30e0-be88-d911e12d0cbe | -2.92174 | -48.95901 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b32931c2-e58c-361e-bc24-403b4e7e93cc | -1.23804 | -54.02028 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf241fdd-d64c-3ec9-9ea2-89c3fe2898da | -0.04704 | -51.24879 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 056b5777-2f92-36b4-8f48-1ca5d0cbe808 | -2.30461 | -51.27423 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 253c075f-28ad-363a-ae27-ad96074f6617 | -2.20321 | -53.67394 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c741d71-f544-3ceb-8212-ab447c53a314 | -1.36629 | -55.70032 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b52d296-d370-3006-aa47-9370410972df | -0.17808 | -51.62186 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 286af905-5787-3111-9360-98c099167c24 | -2.07659 | -51.11784 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1a18ff-9cd6-3566-adbb-85f0f754c5f7 | -1.75846 | -52.37421 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de32f7ce-2efc-359c-b6e1-e876b40c6674 | -0.09693 | -51.4244 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae9cfc2f-fe76-343d-a9ef-5879ca3e37e2 | -1.63811 | -52.59953 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d93c5dd6-aa6d-33e1-b400-0331601790d7 | -2.18425 | -52.12935 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a250ed6-8bfd-3945-aaa1-cb22d15c79c7 | 0.61395 | -51.77421 | 2024-11-21 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f538e790-5e12-326f-a271-c42924bfca44 | -2.18147 | -52.12532 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a30a3a0c-ada8-3557-9980-eea3bb1c3012 | -2.73274 | -48.65387 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcb6c040-b64a-3768-92f0-95a243c33204 | -1.36855 | -51.99973 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 592a5b3f-4980-380f-9d6e-e4f07f0445a4 | -1.26774 | -52.12338 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57fda303-1cda-3645-98ab-92cf006ae6cf | -0.1952 | -51.16109 | 2024-11-21 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc369391-a2da-30af-8dff-9d077dabd30c | -1.14081 | -53.66631 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 063f8327-e0f4-3f1b-b8c8-6e9e4ed30092 | 0.75767 | -50.24383 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5452abcc-4dc6-3d7b-b8a3-9c728a29adec | -2.14865 | -53.78168 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 708737b9-6ee6-33b9-b4ca-9ab101f6f48b | -1.5632 | -51.19679 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22d38f7f-b254-3337-80c1-faf0d202202d | -1.96229 | -53.00295 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1da9d8ed-d678-3c78-bea5-8ea19912f7ef | -1.65045 | -52.67201 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 882b4143-e98c-3480-b5b0-68321a215faf | -1.75792 | -52.37767 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a77a7ef-5e8a-38a2-8756-32feaa8d1edb | -0.87807 | -51.72573 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16ccab6-94d6-3197-8fa8-d70549220532 | -2.36818 | -47.88964 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfc1db87-c50c-3de2-b43f-829ad109e483 | -1.62807 | -54.97707 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d8597b6-7942-346a-888f-9bad96f9bff2 | -1.43545 | -54.53315 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68c7c3bf-bb90-3446-bbbf-6d010ced6c48 | -0.94554 | -51.64559 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddb752bd-540f-3153-97f8-134492e530ff | -0.80582 | -51.49296 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd33c40-91cc-3abb-abdd-3ab44cf2ff21 | -1.81635 | -52.69818 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5def7802-dc27-3355-9a8c-a44c95d97161 | -1.45861 | -55.45545 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8d0491-d106-31a9-b1a9-817501d2b06c | -2.02034 | -54.53284 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 241a4e78-7c28-333f-82cd-bb70aa7be028 | -1.61212 | -52.4192 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d3422ae-2057-3674-8cf6-93e5ec394c0a | -1.6561 | -52.52812 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbff5e57-daa8-38f7-bf83-4eda409ffba3 | -1.68745 | -50.1973 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 153bcb7c-bdee-310a-8dd5-17c2414a0733 | -1.82954 | -46.28244 | 2024-11-21 04:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7d0db93-4b5f-347f-9292-fb08d004976b | -1.5466 | -47.21408 | 2024-11-21 04:53:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68655ca0-b353-3df4-a234-69fbf17e96f6 | -2.93677 | -48.33676 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91d794f3-fbb6-36de-bffb-a449f134a819 | -1.38357 | -51.58136 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d2cbf80-c489-3db4-9f8d-28a8966baf9a | -1.42504 | -46.0165 | 2024-11-21 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87ce9bc2-d976-38f7-8aec-d6cf79b7d27e | 1.63852 | -55.75969 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9199026-0b14-38f7-9d7f-19a4b6247000 | -1.20637 | -51.97437 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66f3f2b6-e2c1-30e9-bb29-792b3a147b3e | -1.41666 | -52.81889 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30973482-9b93-39ab-9417-50d257710c51 | -0.63053 | -51.72769 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2080acb3-2cfc-3e4d-a4bf-3eeee9d564e7 | -0.86217 | -51.84941 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README53.md)
