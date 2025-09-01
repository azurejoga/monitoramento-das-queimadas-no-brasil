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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdf7b445-26d2-358c-ba05-536d0425a5e1 | -12.9197 | -56.9471 | 2025-09-01 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 254.0 |
| c938b611-c938-37c2-ad79-0199550ffb62 | -9.135 | -65.5453 | 2025-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| a5139ea3-58ec-3f7b-8e98-efd24d867649 | -13.1837 | -45.2865 | 2025-09-01 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 64667e53-be3f-3196-8827-c6816e8ef997 | -9.1165 | -65.5459 | 2025-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3cf80896-634e-3f2d-9284-efa9afb6ccbb | -12.9194 | -56.9672 | 2025-09-01 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 7fef7f82-881c-3dd9-95a9-a61632638281 | -12.2287 | -43.8772 | 2025-09-01 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ac74ecee-e36a-3a10-ae43-ea29165cae0c | -13.1644 | -45.2897 | 2025-09-01 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 3db14f34-2b4f-35f2-b91c-2e77125e7775 | -12.5722 | -48.2059 | 2025-09-01 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 197.4 |
| d9a3769f-9e33-31fc-a4f4-c1a167eb274c | -6.8095 | -52.8154 | 2025-09-01 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 614f0a28-f98a-388a-b4ea-5288fb77befc | -15.5862 | -48.3435 | 2025-09-01 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 2786d889-70d8-313b-bf36-e61a004dfc1d | -6.4373 | -55.6212 | 2025-09-01 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 468120fb-1255-3219-a497-a725f0848c10 | -7.0965 | -63.0437 | 2025-09-01 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 25fe9ee6-53be-32b7-b75a-95deaf01d3d6 | -12.5526 | -48.2307 | 2025-09-01 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 16d6aed7-39cb-3d8c-948d-95ae79ab73e5 | -6.8281 | -52.8143 | 2025-09-01 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bb99ed99-6e74-3f6b-8ba5-84ce39b8689b | -7.076 | -44.3376 | 2025-09-01 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 9c92e6f3-d9b8-3099-a0af-e69f5e69e15d | -14.7618 | -46.7667 | 2025-09-01 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 121d6757-9f48-3dca-b8ea-b54061a8710f | -7.6783 | -61.0908 | 2025-09-01 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d5760f73-261c-31f4-9f66-6fc4759aaed1 | -8.6468 | -67.2515 | 2025-09-01 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9223066e-e775-34fb-8a2c-b1fe4436777d | -12.5718 | -48.228 | 2025-09-01 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 27da7b4b-1430-3eaa-83ce-7959bcb5cb65 | -7.0946 | -44.3589 | 2025-09-01 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f37521d3-64d6-360a-9815-f685987210ba | -12.9199 | -56.927 | 2025-09-01 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2f75a810-9a11-38a3-99c9-d6580d22242a | -8.6469 | -67.233 | 2025-09-01 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6a089b19-921c-3424-886d-ab7d431f61e5 | -4.9124 | -43.187 | 2025-09-01 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| d0d133a7-8947-3d99-a9e9-9653c3b46db7 | -12.2094 | -43.8803 | 2025-09-01 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e6207d7f-5a3f-306c-ad8b-02f1fa8761f7 | -12.9387 | -56.9454 | 2025-09-01 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| ff979a54-79bb-303c-b74d-4ae809a726f4 | -15.6063 | -48.3177 | 2025-09-01 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2700c14a-2c94-34ee-afee-569a4f5d8e73 | -12.9006 | -56.9488 | 2025-09-01 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d6fce69f-6e2c-3039-8b1e-4830940a6aca | -6.8279 | -52.8348 | 2025-09-01 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8b989c1f-582b-3c5f-8020-e1fd27b69b1b | -5.8876 | -52.1064 | 2025-09-01 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| eeaadfe1-9ed3-3ebf-97cb-6e5432c2d1f4 | -9.8804 | -65.0139 | 2025-09-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| ce7c246e-4e4d-3481-96d4-25da18650a98 | -11.0454 | -47.029 | 2025-09-01 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 469024a2-1435-3561-87ed-e325d75b40ba | -15.7102 | -48.9479 | 2025-09-01 00:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| efbc08da-f38b-3aa3-b31a-6f62a8c21f11 | -15.6906 | -48.9511 | 2025-09-01 00:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 10fdc3cc-d3d9-320d-bf46-458686c318e8 | -7.0948 | -44.3358 | 2025-09-01 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 4c9e682e-1bb6-3342-afc5-6a1736cb7175 | -6.7626 | -43.7881 | 2025-09-01 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 91721cbe-2f94-34f1-8963-04ff5eb9583a | -12.9385 | -56.9655 | 2025-09-01 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| bf2812c7-7a2a-3700-8d0f-3d719087fde9 | -6.7438 | -43.7898 | 2025-09-01 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 69e5e27b-42de-348a-8402-2e70d957a927 | -10.6128 | -44.3284 | 2025-09-01 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b929d5f0-2525-31a6-8f3e-6a14517898fe | -10.0434 | -48.0998 | 2025-09-01 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4efe0a74-df2d-3287-9f36-582e12f0bbaa | -7.2745 | -60.6486 | 2025-09-01 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b621b751-42a2-3972-b92e-9d7465e0e184 | -11.026 | -47.0538 | 2025-09-01 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 902bf606-4009-3640-b65f-a025d3d37693 | -9.0799 | -65.4349 | 2025-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9dc24153-423b-3125-98d3-f379145f83e4 | -9.1522 | -65.8434 | 2025-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 55e441b6-8805-3976-9f38-cf3ed9d9aa9a | -11.3696 | -43.6341 | 2025-09-01 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f16d0e3a-75bf-351a-bbd2-db69ac1c9e3c | -13.1648 | -45.2665 | 2025-09-01 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4b6ab558-4a40-32fa-877d-fbacced7f956 | -14.7622 | -46.7438 | 2025-09-01 00:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d2950339-a1c3-30e6-91eb-868e8452071f | -15.6058 | -48.3402 | 2025-09-01 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 98f74a68-f80c-3775-9d39-875ac9d0bd6f | -15.5867 | -48.321 | 2025-09-01 00:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d3254ed4-c8a3-3c66-bf33-5724039cda9e | -12.553 | -48.2085 | 2025-09-01 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 9cc6bcef-88dd-3ba2-8d0e-526a46c85523 | -7.2744 | -60.6677 | 2025-09-01 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 94c39be1-c2b2-393f-82f3-c41334ac1541 | -4.9125 | -43.1636 | 2025-09-01 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| addbe060-599c-3059-90eb-5e76ddabf522 | -9.1336 | -65.8627 | 2025-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 36320e0c-1ac7-3476-b260-f3f96d7cc697 | -12.5726 | -48.1837 | 2025-09-01 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 47c7a3a3-cba4-391d-809f-409d3c4a065b | -11.3701 | -43.6104 | 2025-09-01 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 697fa7e6-5b7a-3102-a503-ddc0a4567928 | -8.8454 | -64.15 | 2025-09-01 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| dbb53082-2118-3da1-9da8-ce165a3bf048 | -9.1337 | -65.844 | 2025-09-01 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e45ad9b7-6f5b-3db7-837e-05a1f60dbb4f | -12.5914 | -48.2032 | 2025-09-01 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9e016151-4228-3018-a5a3-e8cbf9611ff4 | -7.0757 | -44.3606 | 2025-09-01 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 21e501da-e687-376e-ae1c-7a7161cbd914 | -11.0263 | -47.0314 | 2025-09-01 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| cbc5b6c7-a115-32c6-bd02-ac3f34e903c1 | -6.1665 | -43.3273 | 2025-09-01 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0fa39a8d-26d0-3824-b0c1-af05a09cbd03 | -13.1644 | -45.2897 | 2025-09-01 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| bf27af2f-2919-3f31-bd0a-012adf011e5c | -6.8279 | -52.8348 | 2025-09-01 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 143affdc-4cf4-3c7a-a121-8bf0f5cc19fe | -7.6784 | -61.0717 | 2025-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5fbd9486-d663-357e-b11f-8ade6a015052 | -4.9124 | -43.187 | 2025-09-01 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4f1d9ef5-8369-3af5-a8c4-500179efae16 | -7.0948 | -44.3358 | 2025-09-01 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a4cf84f0-5a03-35a1-9081-50f8aae34f5e | -14.7618 | -46.7667 | 2025-09-01 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 63d4cefa-1e00-39fe-9c66-7ec1e9b332b2 | -12.5722 | -48.2059 | 2025-09-01 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5a40e5f0-73ea-3ace-a8b2-61b7f2d2a754 | -6.8466 | -52.8132 | 2025-09-01 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f982c226-8848-3619-a100-e27e24a534a7 | -9.1165 | -65.5459 | 2025-09-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 9a8d08d7-73bf-3bef-b556-3050fa7b4ca8 | -7.0946 | -44.3589 | 2025-09-01 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 2f0554c8-bfac-33a1-b39e-96459a9dbd7c | -6.4373 | -55.6212 | 2025-09-01 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d7075f62-a837-36e9-86c3-b33c2512962d | -13.1648 | -45.2665 | 2025-09-01 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| de417168-d9ad-34bf-b878-fb9138b2498d | -15.5867 | -48.321 | 2025-09-01 00:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| bd4d9665-761a-371f-8f74-eb09abb0aa13 | -10.6128 | -44.3284 | 2025-09-01 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| dfac6903-e2cb-3e6a-a9a0-7ad286c2a349 | -12.9385 | -56.9655 | 2025-09-01 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 22b1c134-af35-3318-82a6-a73c8ae72fa8 | -15.5862 | -48.3435 | 2025-09-01 00:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 19f18368-350c-3a98-8513-5bb09dceceed | -12.9197 | -56.9471 | 2025-09-01 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 213.5 |
| d929b929-0f67-3873-869c-d84c15e915e2 | -7.6783 | -61.0908 | 2025-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 372a6327-2bcc-3a9b-b885-9e9c9ffdc33b | -12.2094 | -43.8803 | 2025-09-01 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a210c09d-be58-303f-b2f4-1626dfe89420 | -9.1336 | -65.8627 | 2025-09-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3f113801-4c88-3182-bb6d-cf1c9ea13178 | -9.1522 | -65.8434 | 2025-09-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a10c9136-d20a-388e-9769-19046defb8d4 | -12.0976 | -44.717 | 2025-09-01 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 38ba06f6-a4c6-399b-b36b-1ba12abd5fee | -11.026 | -47.0538 | 2025-09-01 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 701a8f2c-1d06-39ab-8661-994f2d7af54b | -15.6911 | -48.9288 | 2025-09-01 00:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3b299672-a91c-37c4-ae20-aa2c95721c6e | -14.7813 | -46.7633 | 2025-09-01 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 037f4715-d509-3eb1-834b-5b46f890c2cf | -12.553 | -48.2085 | 2025-09-01 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a6b24642-7db6-3c6e-9ba5-87bf4ac8c834 | -7.076 | -44.3376 | 2025-09-01 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 821cd164-d88f-3249-920f-b684fe5c3360 | -4.9125 | -43.1636 | 2025-09-01 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 4724fd25-8e5c-35dd-b3a8-5283a5e3dbcb | -12.9194 | -56.9672 | 2025-09-01 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| b1fe1d1c-a398-3054-b9d2-cc6e730fdec9 | -11.0263 | -47.0314 | 2025-09-01 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 3ca862e3-7644-306c-a3f9-0128d302d48b | -15.6916 | -48.9065 | 2025-09-01 00:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f70aec29-71de-3e7c-b7a9-1c1b63c6f830 | -9.1337 | -65.844 | 2025-09-01 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 526ce788-7a31-3a48-bed3-5fe8081c1421 | -12.9387 | -56.9454 | 2025-09-01 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 9a7c7054-0754-3f98-bd7b-a9f8897fe3fb | -15.6906 | -48.9511 | 2025-09-01 00:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 05a46873-e021-335c-b9cb-eb2ee78b5d4c | -7.2745 | -60.6486 | 2025-09-01 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 05e0db7d-e998-34cf-be7b-8199451e8c6a | -15.6063 | -48.3177 | 2025-09-01 00:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4de57a63-2b1f-3e51-9bab-3b76786680a0 | -14.7622 | -46.7438 | 2025-09-01 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 10a6bb50-0b01-36af-91d0-a6471aa73bf2 | -6.7438 | -43.7898 | 2025-09-01 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| eaaead0e-68b8-3843-9ccc-8a346fd3d107 | -12.9006 | -56.9488 | 2025-09-01 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 81f4329a-a582-3244-93de-803b8cd9be44 | -11.3696 | -43.6341 | 2025-09-01 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |


[Clique aqui para ver as próximas entradas](README2.md)
