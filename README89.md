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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebe76855-a1be-3291-863a-d27aa2f230f2 | -8.8733 | -62.4685 | 2025-08-25 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 817773d1-5387-3a19-b5de-64047e572d88 | -8.8919 | -62.4487 | 2025-08-25 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 517ae023-fd93-3577-8993-b7165d5e942c | -9.06 | -65.7344 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 6ebf4da1-a913-32e5-9f42-c05701d6bb45 | -6.8229 | -58.956 | 2025-08-25 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| c27e78a3-4b27-331b-82f3-6d4806fbf934 | -9.1812 | -60.7939 | 2025-08-25 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 07a400ec-d824-384e-bfa3-d570cfbeecbd | -7.8892 | -63.0737 | 2025-08-25 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7d1c9bb7-cd77-39d0-a3f9-0f454da55f35 | -8.9874 | -65.4192 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| bec466fe-5998-3f88-a156-6995e2e9a592 | -7.9078 | -63.0542 | 2025-08-25 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 89707193-f0ca-3fdf-9f8b-e410dee6fbaa | -7.9076 | -63.0919 | 2025-08-25 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d7daaecf-c957-3e16-80d6-d066f5ab7968 | -9.0415 | -65.7349 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 6036da62-9862-3b69-9c76-23abd0357fd7 | -20.37797 | -46.7478 | 2025-08-25 06:01:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 32e86f5c-8fb5-3acd-9977-d5f09999e0ac | -18.29664 | -49.53269 | 2025-08-25 06:01:00 | AQUA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| ae14f0ed-84eb-35e6-8312-d6a47d52a9f2 | -19.94479 | -50.43969 | 2025-08-25 06:01:00 | AQUA_M-M | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8cefeb84-498f-309d-bf64-140056820afd | -13.4225 | -46.8957 | 2025-08-25 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 6d952b50-278f-39e7-a830-6fb01c4fad5a | -7.9077 | -63.073 | 2025-08-25 06:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 231.6 |
| a860cc56-bee1-3b84-b16f-a47d9bd94373 | -7.9078 | -63.0542 | 2025-08-25 06:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 803d2cb8-c25b-3aa4-824f-e9796adb567c | -8.8919 | -62.4487 | 2025-08-25 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3ae73b87-91c4-3de6-8aea-b2fcc8df907c | -9.0415 | -65.7349 | 2025-08-25 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 8b15c019-0a3d-354e-8f03-499b1c69e4bf | -7.8892 | -63.0737 | 2025-08-25 06:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 3820fa71-950d-31a1-becc-f52a8e18506c | -9.1722 | -59.4629 | 2025-08-25 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c1899e9b-66e7-35ca-a54c-fbd9f294f8a8 | -6.7819 | -59.6711 | 2025-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 609afdda-4dfe-32b9-94ef-7c8aff3c38c1 | -7.9076 | -63.0919 | 2025-08-25 06:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7a939f41-2eba-3a87-9d36-a46978af3962 | -8.8918 | -62.4677 | 2025-08-25 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| baa803fa-4387-382b-bb95-9e410664b633 | -6.782 | -59.6519 | 2025-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| be2c1b8b-e905-3111-bad4-8d6515c15505 | -8.8733 | -62.4685 | 2025-08-25 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 0f49869d-5f0e-3086-a4c9-d4477a588732 | -6.8229 | -58.956 | 2025-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 672e62f2-f116-3891-bdba-8a0c22d239d6 | -13.4419 | -46.8927 | 2025-08-25 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cc28a6dd-3fcb-3873-a109-aa2492950f0e | -6.8413 | -58.9552 | 2025-08-25 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 0485ac39-90eb-3313-b5dc-af999f6ac9c2 | -9.006 | -65.4 | 2025-08-25 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c210aff2-6a81-3ab4-9b0a-bf03c685098e | -8.9874 | -65.4192 | 2025-08-25 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| ae40be3e-6919-34e9-aa6e-f1ba7f76b1ed | -8.9875 | -65.4006 | 2025-08-25 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 202b8832-116b-3370-a6f7-ae547e625091 | -8.8734 | -62.4495 | 2025-08-25 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 123.4 |
| ecc793c2-52b2-33fd-b351-bc70227d03c0 | -9.06 | -65.7344 | 2025-08-25 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 085737d6-c0d8-337b-b84a-1d3bfa9cba2e | -9.06 | -65.7344 | 2025-08-25 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 718d4521-6994-317e-b4e1-ebdbbee0f40d | -8.8733 | -62.4685 | 2025-08-25 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7f134325-8b20-3324-99a0-991c0f67039c | -9.0415 | -65.7349 | 2025-08-25 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e43cda83-2dc0-3f6a-9811-b896024891c5 | -12.7459 | -48.1375 | 2025-08-25 06:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8f9e9b4c-a24e-32f4-8893-4c3be8dc0d84 | -8.8919 | -62.4487 | 2025-08-25 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b10910cd-e1aa-3501-9516-a7e161f3cba6 | -8.8734 | -62.4495 | 2025-08-25 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 107.6 |
| afe66d59-2ccf-3e67-9029-7bda1d996377 | -13.4419 | -46.8927 | 2025-08-25 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 907ce70f-6cdb-3d85-9c48-8b0431e1795e | -11.6499 | -46.2057 | 2025-08-25 06:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 9993e4c3-7252-32ef-9413-c73cf491bce2 | -6.782 | -59.6519 | 2025-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| e65df54c-b2d3-3a6e-82bf-bbfa30b383a8 | -9.006 | -65.4 | 2025-08-25 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| aedf48de-ad11-3367-ba4e-929e554e1a9f | -6.8229 | -58.956 | 2025-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6a2efbf3-9a10-32d5-9fac-7ead69aaed13 | -13.5188 | -46.9032 | 2025-08-25 06:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ec72efae-e24a-339b-b53e-1a123208dfce | -8.8735 | -62.4305 | 2025-08-25 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1fc8aa9d-e3e4-38e6-8863-a5ae2b4fdcc0 | -7.9076 | -63.0919 | 2025-08-25 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8ece51f9-ef4b-3995-80c8-41b035d38bcb | -6.8413 | -58.9552 | 2025-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 6319d790-8c16-339d-ae8a-fcd19b7881ab | -8.8918 | -62.4677 | 2025-08-25 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 103f1ce8-e9c3-304d-aee0-aa68814ddcd8 | -7.9077 | -63.073 | 2025-08-25 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| fff2ff56-54ea-3258-9b13-2a37a4ae2036 | -8.9874 | -65.4192 | 2025-08-25 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 41168a9c-76c1-3832-9a01-df0109dc7b5b | -7.8892 | -63.0737 | 2025-08-25 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0e2f02e8-6fa7-33ee-b39e-ec470bdd0c9c | -9.1812 | -60.7939 | 2025-08-25 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 50e61656-fa72-3fbb-8cd6-7e2873e77af3 | -6.7819 | -59.6711 | 2025-08-25 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| d0688f56-45c8-3800-9a0f-2874ac1507eb | -8.9875 | -65.4006 | 2025-08-25 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 11fc7622-9642-3d8e-80dd-9ed54e09dfa7 | -8.2128 | -61.393 | 2025-08-25 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 663f5646-1ad8-3820-8769-5a2a7b94e73e | -9.1722 | -59.4629 | 2025-08-25 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 98ea0e7c-31e1-3af8-bd9b-1219f3f0a986 | -9.1998 | -60.793 | 2025-08-25 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1b5c7ac3-d50d-390f-a4ba-c51a20784907 | -8.8919 | -62.4487 | 2025-08-25 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e90919f3-fef4-35d4-aacb-057c929415c1 | -8.9874 | -65.4192 | 2025-08-25 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 285621f9-e260-3533-95ef-f42ccd07c701 | -7.9077 | -63.073 | 2025-08-25 06:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 3d6b06c7-bce4-32f3-9e13-e9f8eeb76fed | -6.7819 | -59.6711 | 2025-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| ca7eafc4-96d8-3c35-af3e-cc7b64e5d767 | -9.0415 | -65.7349 | 2025-08-25 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 6856ae5b-cfc3-3f84-baf8-26456f448cff | -13.4419 | -46.8927 | 2025-08-25 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 82cd1124-e23d-37aa-85af-cacd7c56a5cf | -6.782 | -59.6519 | 2025-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| c8c0990e-3411-306c-be5b-1fe56ec4d2a1 | -9.1722 | -59.4629 | 2025-08-25 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9d987e8a-9c9f-3c01-b70d-b08996df831b | -6.8229 | -58.956 | 2025-08-25 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8bc0f1d9-68ed-3fd0-8c14-b6f33565c9a9 | -8.9875 | -65.4006 | 2025-08-25 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b91f73c3-c8c5-3b6f-bf3e-bfa5377e7881 | -8.8735 | -62.4305 | 2025-08-25 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d1f9767c-9730-33c9-b508-7a89cd56eaa2 | -8.8734 | -62.4495 | 2025-08-25 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 6fc9dbb0-7a42-3ff6-9a55-3da73a42267e | -9.006 | -65.4 | 2025-08-25 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b7af6082-5c70-3cc2-96c5-a41437f8d308 | -13.4225 | -46.8957 | 2025-08-25 06:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| aba8ca41-631d-372b-b103-4a31574d350c | -9.0786 | -65.7338 | 2025-08-25 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 13d7eb76-4726-3a34-b62c-41410ac144c7 | -7.8892 | -63.0737 | 2025-08-25 06:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| cb66acc4-85e4-310f-9f1c-c8987a02be44 | -8.8733 | -62.4685 | 2025-08-25 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 26475d19-9a56-3cd2-a59a-194b5b08a93a | -8.8734 | -62.4495 | 2025-08-25 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 39191e03-2597-3db9-a792-a63d6ea8c32e | -7.8892 | -63.0737 | 2025-08-25 06:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 3f4a7d80-b44a-3b1c-a7f6-620e1fa24cc6 | -8.8919 | -62.4487 | 2025-08-25 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9ef88744-78cb-30c2-8021-405066433932 | -11.6308 | -46.2083 | 2025-08-25 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 85586bc1-4eb4-372c-af6f-bc68170b0ffd | -13.4419 | -46.8927 | 2025-08-25 06:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 5fb20a97-61d4-38bb-92e3-ade18148ec00 | -8.9874 | -65.4192 | 2025-08-25 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 2fa60a41-0a9e-3e50-91c4-b45ce2bd35de | -11.6304 | -46.2311 | 2025-08-25 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 67fe0639-700a-3201-8364-b2c94da2ad92 | -9.006 | -65.4 | 2025-08-25 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3381600c-e16b-35d4-ae8b-9c986f4c56d7 | -8.8733 | -62.4685 | 2025-08-25 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6510f8e1-794f-37b4-b60f-5b12f70ad65b | -8.8735 | -62.4305 | 2025-08-25 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0515e21a-6af5-3d26-a6c4-aefda1443a8e | -8.4951 | -63.8805 | 2025-08-25 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0e2db7b9-862c-3e24-a52f-24d6977b07e4 | -11.6495 | -46.2284 | 2025-08-25 06:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 6a89d3d6-4edd-3e27-abac-6999394dee45 | -6.8229 | -58.956 | 2025-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6c41a697-24fb-363d-a317-c616b10d58c0 | -9.06 | -65.7344 | 2025-08-25 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 6a78ced0-b2ee-3629-91b2-e615c4a9af5d | -6.7819 | -59.6711 | 2025-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| bcde8ee0-c1bf-3f56-98ee-0d130e30c23f | -6.782 | -59.6519 | 2025-08-25 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6dff9b75-f049-3045-a6e9-11add7c713a5 | -8.9875 | -65.4006 | 2025-08-25 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| da3c9bdb-6a5f-3308-881e-ee723c04598d | -11.6499 | -46.2057 | 2025-08-25 06:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5193d68a-8734-31cf-9aea-fc32771f3703 | -7.9077 | -63.073 | 2025-08-25 06:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 074a50fd-9455-3c9a-8a8f-b342b632161d | -8.66215 | -68.67742 | 2025-08-25 06:46:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72d10527-7e28-3136-8e32-a74071f2b04e | -8.8736 | -62.4115 | 2025-08-25 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5716a553-7ff4-3b6b-8029-df7751bbcdf6 | -9.1722 | -59.4629 | 2025-08-25 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 11aac127-cf8e-384f-a05d-5e6383c0dbeb | -13.4324 | -51.776 | 2025-08-25 06:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5934c641-d61f-3bdf-9553-4051bed103a4 | -8.8733 | -62.4685 | 2025-08-25 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5f9717fd-2a6c-34d8-ad0d-097361bd2e47 | -8.8919 | -62.4487 | 2025-08-25 06:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |


[Clique aqui para ver as próximas entradas](README90.md)
