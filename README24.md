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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0945c896-67ba-3438-b000-1fa500426375 | -3.5142 | -54.62243 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e6e25d4-4491-36d7-8949-a3ad76b423a7 | -3.9429 | -48.43496 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62605f99-3925-3a26-918d-c7a68077a194 | -3.10497 | -53.73584 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9e2f093c-cb12-31d5-9a09-1893fb70d42b | -3.27892 | -50.01175 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd225efd-8a6e-32e5-b179-7d301c05645c | -2.67914 | -49.03389 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e4c3059a-38c6-3813-878e-370f919d7a29 | -2.94333 | -54.19767 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9079902-4531-3588-ac44-e20fb4ba9ee3 | -4.47 | -54.96589 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c76ad84-770b-3223-aa7d-00648b3866d5 | -3.61574 | -54.60534 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a463355-36f7-3b09-9a5a-1002645a6ff8 | -3.07211 | -49.53928 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07374c85-f84b-3586-9cde-e552f9457771 | -2.81252 | -54.11394 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb376d13-d5b4-3eac-8062-506a75a418f4 | -2.92754 | -54.13011 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abc47e78-995e-3ae0-98f1-cd3fbd9ee816 | -3.12205 | -53.72669 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53dc44c7-5f1d-3718-84c7-00653bc3acfd | -7.51652 | -35.17178 | 2026-10-05 04:38:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7acea740-fd70-342e-9ac2-467dd2620332 | -3.91786 | -49.70485 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dc17fd6-298d-3375-aa0e-2cdc8de95e07 | -2.46969 | -48.04103 | 2026-10-05 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1e4c336-be81-3709-a7ee-8ce6a8b61d53 | -0.35308 | -50.36807 | 2026-10-05 04:38:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e01a9d2a-baa3-3dbb-ab32-d9e87e396e0c | -6.05429 | -53.48327 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c608d7-626d-3486-8ef1-f03c52d38080 | -6.89359 | -43.67422 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 455b47bc-4dd6-36b7-9027-93dcb0c9e3ef | -2.93429 | -54.1216 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 761d5c32-5419-3ed1-9dbf-877640d71179 | -3.10736 | -53.72123 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f32779a2-85be-39fd-93c2-770c6b2bdc36 | -4.44788 | -54.96579 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83454df9-866b-3568-a04e-da6e4c4fbb67 | -1.10481 | -54.14482 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f351be8-da9b-3020-b0aa-a391a62ccf02 | -2.78801 | -54.1002 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d76c6c23-8851-379c-b8f9-414438de918d | -5.99919 | -53.51992 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb091a12-d991-3b9e-a6ea-e4797a95a0f6 | -6.00094 | -53.50978 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7779e5fc-8d1c-345f-99af-a8e800f7d472 | -2.53659 | -58.03679 | 2026-10-05 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49e19d33-b7c2-3b49-a773-3d0b48529bfe | -1.09522 | -54.10162 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52aa984a-187e-3313-ad50-4536623619cd | -4.04129 | -50.76175 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4bceedc-5989-3762-bca4-a16cb0aa6727 | -2.25307 | -51.93254 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b8bf229-2d50-367c-9e98-c3b0c1839fe8 | -3.18365 | -54.07812 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b394bc7d-b8d6-326b-81c8-e0a50f88effa | -2.78853 | -54.09704 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd40152b-263e-3eac-b148-59eb6a69bf0c | -2.22018 | -53.70539 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 520ba598-f4e2-3410-ab5d-209b7858eefd | -4.1133 | -50.8069 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d035be9-91f7-31b2-9f6c-9d40fc918539 | -2.80887 | -54.10363 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43db4d0c-5920-3e90-a142-7c9964bafffc | -6.87943 | -43.67198 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 179fd478-10f5-3134-b160-77db0a096128 | -1.17665 | -49.25607 | 2026-10-05 04:38:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ef3cbb8-bfae-3896-be0f-ac1fbc8a8897 | -6.91713 | -43.68064 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2e8eba6-0c15-33f6-aa5f-e09fe57223a1 | -6.21375 | -52.68805 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12725687-9cab-3413-b141-c3d634d84ce3 | -6.60462 | -41.56151 | 2026-10-05 04:38:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e0a34ef-6d18-36ab-b2de-883f15c0d9b9 | -3.46593 | -54.59735 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 7c894e02-724d-3125-8f91-7a480453cd9d | -3.47123 | -54.59839 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07e5bab3-29fc-34a0-8f47-e1d093f0c651 | -3.04595 | -54.22667 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de5877fc-e135-3050-b25d-20c55adac2b6 | -3.30256 | -53.83989 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe4c3323-c47d-3177-ba56-70350a65e0e6 | -3.11194 | -53.72501 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e6edc05-4f72-3a66-9098-6ee7cceb50a0 | -2.68288 | -49.0345 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 181bdeea-843a-3c24-94d9-7d8a09de3671 | -3.13263 | -53.71399 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4bbfa9e1-0cf3-3abd-9b3f-9d4bfdc1dedd | -4.22959 | -49.97174 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d467046-14dd-32b4-a251-a4b58864bf5e | -3.40532 | -51.67608 | 2026-10-05 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77412556-024b-3b5e-8d8f-da7818e7d134 | -3.37196 | -54.10033 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaa5eb0f-4f32-3274-829e-b348014cbf53 | -3.11843 | -53.71706 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f94a31b-e1ac-3708-8142-123891a7be22 | -3.27033 | -54.00366 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c92a6cfa-9a68-3a2e-a3f4-138a8226f95e | -6.21222 | -52.8301 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93366e2a-b347-34f2-bcc1-135d8814d54e | -3.1249 | -53.70916 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a9c4a1fd-f4bc-3e11-803f-b1f1177775a2 | -3.11699 | -53.71434 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2847c0b1-3d46-3cd4-81ad-e38b6081c0dc | -3.4295 | -44.44783 | 2026-10-05 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62cded7f-1bf9-3d89-afc2-d9e1eb7f1a8f | -3.05109 | -54.22421 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43fa60f9-50c2-3efc-b649-02848b888db9 | -6.90067 | -43.67531 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2fe61024-5268-3bdd-ab1f-81db80298934 | -3.46738 | -50.10731 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ca74f38-5dd3-392b-a3bc-c479b2a054aa | -3.51599 | -54.62615 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23fbf603-e274-3e0c-8eec-4e5d2664803c | -2.93308 | -54.16233 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5571db9-3d5b-3867-94e4-3956baa6b143 | -3.51115 | -54.60832 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d3d80c5-220f-3148-9e6a-3f17d5cb4e12 | -2.90304 | -54.08419 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a6612eb-0ec6-33a7-9514-323f5502f7f9 | -5.06249 | -40.46029 | 2026-10-05 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa4bb62b-f039-3629-bd86-7834ef2e0488 | -4.08138 | -48.96254 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59abacae-ab5c-3796-8861-9ad2fcec8b14 | -3.84338 | -55.84486 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a850210-4dc0-3c3d-8bf2-6cb5ba4900da | -3.13668 | -53.72066 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 77fa83af-3711-35b1-ab66-f0d0338ff088 | -3.27842 | -50.40175 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 903f6fcf-aa3d-3449-b9db-3e94b7e51355 | -2.09966 | -48.23008 | 2026-10-05 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25bf9204-5d5c-32fb-9033-48fcd760f7f3 | -3.05964 | -54.17395 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd90c06b-33ed-3114-b8ea-a2a2de707c56 | -3.11449 | -53.72894 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cdf9665-64e3-3c91-ac3c-94ab607c9495 | -0.38057 | -52.04596 | 2026-10-05 04:38:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ea5dba2-e07a-3cea-9ff6-5ce8ec275a8f | -3.31017 | -53.84167 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a27819c-beb2-3597-bf20-b135272342d1 | -2.5938 | -51.85379 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a81f4d4-b3ad-30d2-befb-eb6528f283f9 | -0.39156 | -52.03778 | 2026-10-05 04:38:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 03233d09-7fcf-3089-9650-621b0184d437 | -4.25468 | -50.77791 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7b81ebc-1d30-3835-9b4e-940d41ae63fc | -4.28658 | -50.78673 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c34c7ed1-7de8-3852-bb22-0037c5982965 | -7.09476 | -41.75923 | 2026-10-05 04:38:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 71e2218c-521e-38b3-8c1b-b91c06d1c209 | -2.15915 | -53.66148 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039a1842-8a53-30b8-99ac-9faeb94f3439 | -1.61545 | -55.11256 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d054d0da-7802-3c00-9b9a-1cdba77561f7 | -1.1994 | -53.38807 | 2026-10-05 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7772246c-1a23-3083-ad84-1ca6ab76615e | -2.85164 | -51.2966 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2fc3af9c-8cd8-3a88-a92f-4bbe778a1c3a | -3.30865 | -53.85051 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9447eaae-21fb-35ce-9bf7-2667758f3389 | -3.1256 | -53.72477 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c9ecbc7-2b9f-39c2-bc45-f7bf44b2918a | -3.65757 | -55.50328 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7b793c3-520a-3db2-aadc-fff885ce0855 | -3.80558 | -47.48982 | 2026-10-05 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 546c95a0-8572-38bf-8d5a-7021a8c36ae3 | -1.10373 | -54.15163 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f5fd492-09f3-3e57-b9d5-cd32e0f585c7 | -3.41784 | -48.33521 | 2026-10-05 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 889e6b03-e8c9-3913-ad9e-abc47e572f1b | -4.45867 | -54.96741 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 921d2071-8f56-32d2-babd-a4edbbf3cf41 | -3.31323 | -53.8543 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64d28532-ad3a-3915-af23-463afac2067f | -6.91186 | -43.66757 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b2eef12-c11d-3846-b9d8-0ad931042927 | -3.92086 | -49.71044 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a85f5c50-8a62-3392-bf36-23470799105a | -3.85894 | -55.82349 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd2ecb67-46db-3718-b2cb-258133dd9433 | -6.20417 | -52.7962 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06af5567-e85e-3a94-96be-46069e33f507 | -3.2791 | -54.1777 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 281039b6-2243-3aaf-9f3f-452f37f1dfe5 | -3.47293 | -50.09798 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9aeb3db7-16c5-3a25-bb26-15dbe855792f | -3.91733 | -38.67748 | 2026-10-05 04:38:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a6b7e8f9-df81-3c07-9086-6957c87fa174 | -3.46174 | -54.58968 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 26c54f0a-6474-312a-8f85-87886b08e773 | -3.57066 | -55.41624 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 225dabd9-0576-3ce2-a58a-98947447b508 | -3.52374 | -54.63082 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8877c4a3-92e7-308c-a27a-f5500c0214a7 | -5.13295 | -48.32499 | 2026-10-05 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README25.md)
