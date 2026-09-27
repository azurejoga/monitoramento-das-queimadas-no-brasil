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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54783993-558d-3f16-901b-d43c163d6ed1 | -12.9457 | -51.0695 | 2026-09-27 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 15c79f5d-a622-3190-98f3-ef7f8d8bcce1 | -11.7329 | -50.573 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 6f4a409b-25c6-376b-8310-c98149a6d114 | -12.2623 | -50.8105 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 072030fd-47bc-3f92-b0a5-ab96d7dfbafb | 1.6566 | -55.9227 | 2026-09-27 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 8e5c01d1-515d-3619-bf95-71d258746d94 | -12.9101 | -50.9029 | 2026-09-27 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 671ed3c7-b2bd-3446-b97a-811ac003d74a | -12.2244 | -50.7936 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 59b63651-eec8-32a5-846f-6179c9f45b01 | -11.77 | -50.6329 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| cd56a5b7-3c26-3aa5-a654-e92a0fbf8c27 | -2.7151 | -57.5109 | 2026-09-27 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| efb6bc9f-5a58-36e5-bc36-ecaeba41c0f4 | -12.1027 | -50.0355 | 2026-09-27 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 48b2cb1b-8e53-34e5-ac9d-03f993cee57b | -12.0372 | -50.5804 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| fdbd3358-5947-3531-a5d3-7d2acca074b3 | -2.9997 | -54.209 | 2026-09-27 15:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 35187262-7dd3-3f38-9133-9d351b43a64d | -12.2123 | -50.3451 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| eba07bea-9adf-3fcd-8cc2-c5b4b03b3bb9 | -12.1112 | -50.7215 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| dad16d9b-1240-3dca-9010-debf1bcd69d5 | -12.0537 | -50.7496 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| c23ce963-33da-31df-b4ba-46bf6bba9961 | -11.6186 | -50.5861 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 40e4d491-36df-3321-8d93-9bf4f221f1e7 | -2.6629 | -56.4575 | 2026-09-27 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3c1a9271-bedd-37f4-838e-1ab1da3557a1 | 1.6565 | -55.9818 | 2026-09-27 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 557d8deb-e1a0-3dec-8675-658919f9803a | -12.156 | -50.2874 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 3bbaed21-333e-38e4-9736-ecec00943b58 | -12.1099 | -50.8071 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b56562fb-ee09-30aa-b9ce-5617ae42c434 | 1.5834 | -55.8645 | 2026-09-27 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 11ca6dd6-7c89-3b9b-b473-16b1ac12f545 | -11.0991 | -54.0285 | 2026-09-27 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7f5bcb70-5b17-3969-b605-f825420a0397 | -11.7697 | -50.6543 | 2026-09-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ca21bb99-d8f4-3815-bf64-28a546b8b0bb | -12.054 | -50.7282 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 76238414-4597-3eba-ab64-b0d7ac2930b2 | -12.0352 | -50.709 | 2026-09-27 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| cb7854ec-f9e0-3285-b83c-204fae61ee80 | -11.171 | -50.0366 | 2026-09-27 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 65e2e4d7-3e7f-3d7c-aa5b-e7c720303ef7 | -11.0583 | -51.327 | 2026-09-27 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6a5e5926-9125-3e80-8404-ece244637c85 | -2.7151 | -57.5109 | 2026-09-27 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a34741a6-8d29-36ce-8f6d-0a9f7cbf2d3f | -10.5349 | -57.4382 | 2026-09-27 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0c9c6bbe-bb74-3ee7-8f6f-78049f664951 | -11.7697 | -50.6543 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 23fe68b6-68ab-3023-8b67-0e1af176b343 | 1.5834 | -55.8645 | 2026-09-27 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 91e0014b-ba8b-357d-ab7a-00207cbaf98d | -10.0531 | -50.1978 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 8a234be9-a309-3082-8e26-96d910903ec1 | -2.7151 | -57.5303 | 2026-09-27 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 594e2b35-8bcd-32da-b2be-27faeadf7147 | -2.9158 | -57.7789 | 2026-09-27 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 0923c8f7-c67b-3bbe-902d-2e3492e11408 | -0.8215 | -48.6609 | 2026-09-27 15:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 76eadce0-901b-3695-ba0a-f1dbc1ba0eac | -12.1109 | -50.7429 | 2026-09-27 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| fee40f1d-8c68-3351-a529-25f791ee4c15 | -11.1714 | -50.0151 | 2026-09-27 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cce6204b-933a-3b6f-800c-b3990d8bac75 | -11.2654 | -51.411 | 2026-09-27 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| d0af2a65-7c44-3620-96ff-4b4cdc730775 | -12.2498 | -50.3835 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f99a9e65-1218-3460-a7e2-e52a89c7c236 | -11.0991 | -54.0285 | 2026-09-27 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 7bbba702-f663-32fc-b842-ca43a376a699 | -11.6567 | -50.5817 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 15e0f9e9-96e5-3b47-9f21-a6569e2d5783 | -12.1112 | -50.7215 | 2026-09-27 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| da445d64-cb7d-348a-9b69-20706d64a9d1 | 1.6383 | -55.9033 | 2026-09-27 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ca083faf-aebb-31ae-b98e-aba8e8bb1dcb | -11.9619 | -50.5251 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 60277244-f6d7-385a-ad84-f4b54ecc2f49 | -11.3048 | -51.3011 | 2026-09-27 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c5354bf7-5866-3681-b2ec-1c3deec1f564 | -10.0906 | -50.2154 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1fb9b833-93d6-3e27-ae16-b0770d886e83 | -11.9783 | -50.6943 | 2026-09-27 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6d3f5205-3c1b-3259-8976-85ee9a4ccfc0 | -1.9489 | -56.3319 | 2026-09-27 15:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a7f4075b-d606-3aaf-839a-779226834ecd | -11.2856 | -51.3243 | 2026-09-27 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fa5a4e27-7c66-360c-8f90-8fa1ccb0ae39 | -11.6767 | -50.5153 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8a65c8f8-0a7a-3fa4-b415-db41a4ec8920 | -11.0393 | -51.329 | 2026-09-27 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 63e95e90-a007-3f5e-ae9e-31ad14cfbde3 | -11.3046 | -51.3222 | 2026-09-27 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 0c0917e4-4c0f-3675-bada-c5b61701b2ef | -12.6071 | -51.9595 | 2026-09-27 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 54df5e5e-5f58-34b1-90ae-8d9ee04bc926 | -11.1524 | -50.0172 | 2026-09-27 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 6cde330b-89e3-3d3e-bb30-4d41c06a5b78 | -10.0162 | -50.1374 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| c1678a1f-96fc-3c8c-aba3-85f99b0b7a40 | -12.7674 | -54.0502 | 2026-09-27 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6719958f-535d-3829-9f28-86d965f91d36 | -12.9457 | -51.0695 | 2026-09-27 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 925d115c-756f-3048-9d11-e8b3284bb71e | -2.9341 | -57.7786 | 2026-09-27 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 16b9b587-81a5-3bbc-9f5c-0c1009e6ecc3 | -10.6097 | -53.9697 | 2026-09-27 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f2b56e35-de93-394b-967a-25875527d817 | -10.3363 | -50.1905 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ca39bba3-e608-3e65-85aa-2fe3a4a6d92b | -10.1284 | -50.2116 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3d806e11-625e-3228-b93c-d5451cceb205 | -11.7322 | -50.6158 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 41a37620-432e-37c7-b80e-ea949b0ed30f | -10.1089 | -50.2563 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 474d8cdd-cec1-3852-88f2-730c4c96a792 | -11.2859 | -51.3031 | 2026-09-27 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b7681907-8234-3d97-968e-52fabc004e74 | -10.1278 | -50.2544 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 30256ebb-3f8f-3fee-ae97-a7f19d898adf | -12.2241 | -50.815 | 2026-09-27 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 889db860-282d-32bf-bbfd-8d95983df401 | -11.7887 | -50.6521 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3596446f-bc57-3201-8983-4b806da5de82 | -11.0988 | -51.1324 | 2026-09-27 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 08c6c287-6511-32ec-baf6-a8896116e31e | -11.9434 | -50.4844 | 2026-09-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| cf9aaadc-04cf-3750-ac57-78dd8f6760a9 | -10.0159 | -50.1588 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 18e895e8-df62-3032-94a8-5661756367ac | -12.0349 | -50.7304 | 2026-09-27 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 4d0d8b6b-7c18-38f9-8124-56276781428f | -12.7677 | -54.0296 | 2026-09-27 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 5d90f940-51cb-3242-8ab6-b7b06ab6111a | -11.0051 | -49.7109 | 2026-09-27 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 5358c343-2720-39c1-947e-4a5bdbbb613c | -10.2446 | -49.986 | 2026-09-27 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 62dfb620-7f67-3764-98f8-cf30a492d7e2 | -12.7868 | -54.0275 | 2026-09-27 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ea4bddfc-e200-39c5-b22c-6a50cf5df96a | -11.1901 | -51.3766 | 2026-09-27 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 487bfc29-9ac1-3ac0-af96-2e80c4deb578 | -10.2824 | -49.9821 | 2026-09-27 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f2ef6a16-1a14-3f29-979d-728d29dd7ec7 | -12.0352 | -50.709 | 2026-09-27 15:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 87ec45cd-f2d8-3dd4-91e3-d9dcf77d5891 | -1.9489 | -56.3319 | 2026-09-27 15:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| da10025c-1566-3b03-81d5-0e9ee1830e0d | -11.1901 | -51.3766 | 2026-09-27 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c287b9cf-f27d-3254-954a-a5bfd352263b | -11.171 | -50.0366 | 2026-09-27 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8091c16c-db3b-38ad-8e7f-2e5543de92d5 | -12.7674 | -54.0502 | 2026-09-27 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 617dec00-6eb4-37c6-a15a-b9d7102e906d | -1.3932 | -48.9961 | 2026-09-27 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2ca39dbf-1945-3495-8ff9-7917ae78f030 | -10.7677 | -60.7279 | 2026-09-27 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a4c8ae23-346c-3017-a4a5-c7d26633220e | -11.0991 | -54.0285 | 2026-09-27 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| cde11e60-a56a-3cfa-b549-c1ee6ad64fb8 | -11.2859 | -51.3031 | 2026-09-27 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 91566b52-813e-353a-be46-cb195c2699e0 | 1.5832 | -56.0417 | 2026-09-27 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3c1687c0-8d77-3569-829c-a615bf55fed2 | -11.6815 | -50.1932 | 2026-09-27 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 46ea2d5a-2d84-3831-86d2-4adff60bcd10 | -12.7226 | -50.669 | 2026-09-27 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f754cd31-0faa-3812-8286-d96e14235976 | -2.7713 | -57.0229 | 2026-09-27 15:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f75ff618-e277-3c6b-896c-4b0dabf126dc | -11.9431 | -50.5058 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 9678cd20-d322-3046-854d-24b8ec23e96b | -10.2827 | -49.9606 | 2026-09-27 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2bc0392b-b15b-3139-a5a8-16372950725e | -12.1366 | -50.3112 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f0bf1707-6d21-3c16-95b5-0a7f1c4ffdcc | -13.2186 | -54.5182 | 2026-09-27 16:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 55b7f649-3b62-369f-8dcf-96798f01022f | -10.1278 | -50.2544 | 2026-09-27 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 00b5b345-6c31-3b7e-9141-204ff304f636 | -12.1553 | -50.3305 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0937ad35-d265-3078-8018-6dc2a26d08ab | -10.1089 | -50.2563 | 2026-09-27 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 80a0ced7-a5e0-350e-b58a-fd61f33133d0 | -12.1744 | -50.3282 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 79a27108-76b2-38f5-a81b-0f2c7f1cbd00 | -12.1557 | -50.3089 | 2026-09-27 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5eaaa2e3-8dbd-3991-85f5-4bd6b0bcf406 | -12.3706 | -62.4459 | 2026-09-27 16:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e312f0c5-a170-3e4a-839a-3c988ef68d06 | -11.2859 | -51.3031 | 2026-09-27 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |


[Clique aqui para ver as próximas entradas](README65.md)
