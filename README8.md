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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4f97602-f03d-327c-b5ff-c28cc36a7694 | -7.49137 | -54.98973 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| b1af3442-6b6b-3636-846f-671473c51f66 | -2.97387 | -51.04454 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d1d29c29-2f58-3aeb-9eb8-7045f6e99904 | -7.49633 | -55.02614 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 74db7907-7cac-3746-9fa7-d6eced8df151 | -1.81997 | -57.10736 | 2026-10-01 00:20:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b5702d4c-0f70-3b74-acc5-4c6ae1f5f711 | -3.24591 | -48.77642 | 2026-10-01 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e04c1bda-9c7c-3589-85fe-3e7458497f9c | -1.83508 | -54.99451 | 2026-10-01 00:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6b7f2f6f-5c9d-3b6c-bc4d-649055788e55 | -3.02597 | -53.86919 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3aed56cf-db7f-3af9-95b2-321d5b6cec5c | -3.07647 | -54.37733 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1ff009dc-74fc-318c-9a13-092379f0b1bb | -6.54773 | -55.29325 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2d82248-1838-3eaf-9a0c-e9a3230182e4 | -4.2437 | -50.76217 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7f54056c-1a86-3dbf-8bc7-d6b4b5349513 | -5.1813 | -46.20789 | 2026-10-01 00:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ee9e432a-8907-3251-8721-9f96a7516be5 | -3.59864 | -61.72317 | 2026-10-01 00:20:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| bced843d-ef6c-38ef-9541-dfe1c1f2c441 | -3.29043 | -53.85658 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 45f03b49-36e6-3d66-92a1-0fe5ac9347f0 | -4.034 | -54.22983 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 85d375b9-c01a-3bf4-9885-135fb5cf9916 | -3.57112 | -51.51247 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2d4a6286-f5d6-3fd9-a9c9-fd4cd116738b | -3.00263 | -54.23435 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb2880b4-0087-349e-aca2-53e467ea3373 | -2.92738 | -54.16024 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9ef704d4-cc03-3435-aace-21bfbdeceb80 | -4.12555 | -46.8801 | 2026-10-01 00:20:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 92b4a0b3-927a-355b-aebc-9971bfad2b92 | -6.5231 | -55.38702 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a7545a98-4443-3787-99f3-ddbdfcd74ec1 | -5.91247 | -53.49192 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| a8badf9f-cf89-3abd-ad77-04e9c5de2b17 | 1.87362 | -55.63587 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 73551972-7792-3b45-a8c3-891a2d441540 | -6.74536 | -55.59914 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bd6ff1c2-a5a2-33bb-8509-3add38769d57 | -6.14597 | -53.3121 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 86348fd4-4647-3d70-924b-865eef5a4ea7 | -6.73629 | -55.6004 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eedc01cd-fd88-37bf-9e80-92a9b8a159a2 | -6.8393 | -55.27207 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7971e8ad-b3f3-3dff-9940-2e46156b1d7f | -3.57788 | -51.48795 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 28a8bc9b-2c3d-390a-a188-06949dd7ceb5 | -3.43045 | -50.44463 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b22fea62-fb61-3a40-9e5d-36043cd05379 | -5.97826 | -55.3775 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1caacd3a-7e2a-3c54-a921-41535e69e264 | -4.26538 | -50.79151 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| bd68d6f4-14e2-3e9b-be91-51737efbfb5c | -4.83441 | -50.68472 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c51fbd5f-c567-308a-9d35-a4b0952978f2 | -3.01174 | -54.16964 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb1e4db1-9431-3df9-ad13-15af1d8d2ce0 | -2.85824 | -54.13078 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bf8e9b1e-8683-3bdd-a064-347a7f4aa9d7 | -4.2617 | -50.76626 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 315.6 |
| ff778baf-2cfc-3d44-9418-3149a0ac8f74 | -3.2645 | -53.99754 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4cc1c0b1-e9fe-3b42-9740-1c8dbb665743 | -3.29372 | -45.92431 | 2026-10-01 00:20:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 661861e7-52f3-3968-b6e2-8326de797c28 | -7.50032 | -54.98854 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3cfb9d07-aec8-3315-b13a-9a817b93b4a8 | -2.82632 | -50.46974 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| aaabd50d-7414-30ec-b9bb-b53d5cc1ca37 | -7.45565 | -54.99473 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f893537-f82f-3a6b-a509-8e638f1be03c | -4.62886 | -50.61031 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6b5c3ffa-23c7-3f40-8622-1c62ae985dff | -3.11081 | -50.2947 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ea410b84-4499-3695-abd0-f83fb4ad75f8 | -4.63074 | -50.62328 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| f6d5ed92-d0cd-3fa4-9689-5058042e6c92 | -4.05366 | -51.09327 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1ac8c447-d0cc-35d4-86bb-a0c825fffdd6 | -4.2826 | -50.76322 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 761.2 |
| 9585d167-4d7f-3b35-8974-a93c619de5c7 | -6.53754 | -55.28534 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7ed0d88f-e233-3465-94a9-2c996da88774 | -5.08767 | -45.78292 | 2026-10-01 00:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 7827b161-6158-3c8c-9fd1-141900c2647b | -6.34937 | -55.3299 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bcb64be4-594b-319e-9b06-659e10999342 | -4.04161 | -54.21977 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cea91ca2-ad5e-3044-8a76-e50220317baa | -2.99477 | -51.04154 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| ed674c6d-4228-332f-8ca5-dd36ab48c00f | -2.5038 | -56.9114 | 2026-10-01 00:20:00 | TERRA_M-M | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c13733a4-3409-39ec-82c6-f22854c86977 | -2.98256 | -51.03038 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 86121478-3a22-3169-9fb2-18fe9ca303fe | -6.33519 | -51.15255 | 2026-10-01 00:20:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 00fcdf5d-a484-3bee-b11c-16e3df016b93 | 1.97141 | -50.83795 | 2026-10-01 00:20:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cd7d3edc-d2ba-3dc3-8c76-3ab153e1e8e4 | -3.49412 | -54.73359 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e123bd12-32f6-39c0-8a6f-1723cae47aa2 | -2.87814 | -54.87992 | 2026-10-01 00:20:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ee36b9bd-45f7-3fb9-8eeb-9767a53b0249 | -5.7479 | -45.14024 | 2026-10-01 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 65f58fe8-cbf9-3744-b979-435dd9784b2d | -4.07554 | -54.87514 | 2026-10-01 00:20:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 48168c61-c334-3f5a-b213-28f18d880dac | -3.02034 | -54.23187 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 14739589-908e-359f-ab85-75758a7b7f28 | -4.28443 | -50.77595 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 698.0 |
| dfd96553-3c73-3792-a9b3-6e194be7cdf6 | 1.80043 | -55.62873 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a602a39e-2d11-32bc-b9a2-251cb1b6ef9d | -6.91048 | -51.67152 | 2026-10-01 00:20:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8c9fada7-170b-314e-8c21-0965b153fcb2 | -3.96421 | -53.46241 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| f539a12a-4d8f-3b1e-bc69-594a6705f08b | -6.26854 | -51.8293 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cdda921c-bba4-3c94-8528-d2638b311ab3 | -2.99009 | -51.03582 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6bf2efe6-d8ea-39d7-a1cf-2e32c1f6156f | -7.70475 | -54.79446 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 46a8999b-62ba-35ad-b8ce-1c0a192d4f40 | -3.01666 | -54.20522 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d2d2bfcd-9725-36c9-8cf0-483085cecd8c | -6.18334 | -53.18045 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d73a502-306e-373c-8d32-84627d403227 | 1.70794 | -55.91011 | 2026-10-01 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 14c65939-ebc1-38ea-8c9b-c28bbeefc756 | -4.15993 | -48.91197 | 2026-10-01 00:20:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7a0cd982-186d-302b-a179-a53038184ee1 | -6.0044 | -49.55381 | 2026-10-01 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9c7498d2-e40e-3619-a85a-2fdac4d79917 | -6.2845 | -52.91666 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2eadd92-18fe-397b-b8e3-9ca5a1b91835 | -3.12186 | -50.2931 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| a7b34b1b-b372-3107-ab33-a2eb887d3374 | -6.36191 | -55.14614 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22773844-b4f8-3355-bedf-b756564b4661 | 1.7347 | -55.97622 | 2026-10-01 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36719cdf-71e6-3924-9f74-300b6893d272 | -6.20247 | -53.18691 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7fc9e320-6015-37b2-b4de-5e7f186d31f4 | -2.94541 | -54.09407 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 489f7e35-e977-3a35-8b10-5d1f6c82af3b | -6.69874 | -55.04716 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60102347-5c01-3138-8a97-09551e4ec9c9 | -7.71365 | -54.79321 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe55bf22-0ada-32c4-8d0e-3708e916dd49 | -6.3696 | -55.13589 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bece7fbb-a6c1-3aa6-9daf-534f948f5c4c | -3.16701 | -54.09031 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| fd6470e2-b054-378c-9327-a391810b067c | -5.91371 | -53.50088 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a1fbb6fd-1ae1-3ba9-b4ed-9cb9aa3e5cbc | -4.29487 | -50.77441 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| cca46518-4fc2-3ff9-b6c1-8d14285334c0 | -3.09562 | -50.26767 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 71253282-2852-33fc-8862-89ab3efa346a | -2.95985 | -51.02071 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5eef67a1-06fe-3dc7-9d46-76ed840eeac5 | -3.57718 | -54.3246 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 79ede5bb-3b6f-31f5-bc79-d3737b7175fe | -3.0014 | -54.22546 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 57fee524-55b5-3092-8edb-fd25c685c103 | -1.4286 | -46.79902 | 2026-10-01 00:20:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 3d538845-315a-32cb-9995-8b1d914e735f | -3.01026 | -54.22422 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d31ddb7e-6509-37a7-928f-d73f373c4c5a | -3.98421 | -56.08675 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 075a9408-4e63-303e-a6f3-2bdb8f95bc70 | -3.16 | -51.35648 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 205.9 |
| c219905f-3673-3a37-b1b0-77c6dea62c4c | -4.31753 | -50.78397 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2b581efc-f401-30b4-9899-d2658a5cf160 | -4.24939 | -50.75503 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 192.6 |
| d530f6e0-f0ed-3690-86cf-0bb5cf3404a8 | -3.92489 | -55.92254 | 2026-10-01 00:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11e57168-615f-3d59-937d-25d5100a47f3 | -3.21069 | -53.94732 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ab423b20-697d-3f5c-8775-4460e8c91b5d | -4.30242 | -50.90102 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d41286f9-bba0-3adf-9e8b-ce386792ccbd | -3.1569 | -54.08261 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 11e0cb08-c4f2-3796-96cd-7b65c93fca7e | -2.4475 | -49.2261 | 2026-10-01 00:20:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fdbb9781-8424-34ee-ac99-6efd050fdd8b | -5.17708 | -46.18029 | 2026-10-01 00:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 2739cdaf-aa3e-30b1-a4c8-47a1212650bb | -3.15829 | -51.34457 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 2bc44b60-6dee-3483-bda4-13060b2262a3 | -3.0261 | -51.28327 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 51da65ef-a62d-3d8d-9d6f-f82cffc29477 | -3.17836 | -54.10689 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 460.5 |


[Clique aqui para ver as próximas entradas](README9.md)
