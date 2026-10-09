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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92af745c-3a37-399c-abe4-d08631849119 | -4.13921 | -53.99334 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b6274fb-5653-3738-ac4c-4a571f1f712f | -4.37491 | -54.74482 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dbeaacf-c371-3013-9141-cf6848277539 | -3.30558 | -53.70401 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 060f7c1b-6916-3be1-8942-b1c6175c2422 | -2.99222 | -54.1455 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0311b8b2-78e5-3a71-b681-672d7710dcbb | -5.90549 | -53.89083 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e62a2f5-9ace-365a-9962-f8d0b03d5e06 | -2.8748 | -54.20257 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0ea1101-573f-39dc-88ee-675c936d49f2 | -4.53803 | -54.98317 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b3a08b4-dc1c-3e67-bdda-d3099ca52d18 | -3.95139 | -55.33179 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e319331-9678-332f-9049-4a4617d1ae5e | -3.03134 | -54.2383 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883c6906-e85d-3a55-b771-530ebb0bf7dd | -6.10402 | -53.50306 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddda0715-2534-3229-b415-5f5409422407 | -2.98312 | -54.11234 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d16a0e9-b314-3903-8c05-850fb7044efc | -2.97816 | -54.07599 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9a06016-c804-3540-9b8b-04e8ab9b3a19 | -11.18378 | -45.31611 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0066ad73-1874-3a2d-8a33-e4013ad5aac6 | -3.62712 | -54.23444 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b6c35d4-cd1b-33e5-99f2-80abba62f68d | -10.87348 | -44.80127 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d73b8549-9417-38b2-a6f4-ee44070eac83 | -3.49765 | -54.61228 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1df416f5-26bf-37a0-91c1-a709570a0dba | -5.70855 | -53.49065 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5204f92b-66d1-30f6-bb17-22c2077bc642 | -3.00263 | -54.07989 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7686a427-b51d-3334-8ab8-4d992403ec02 | -3.58624 | -54.68677 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f476d226-2fc5-34c1-b30c-eb1d26ca2f6a | -2.94508 | -54.05888 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb1d5f0e-9e03-359e-a07c-cac693efe589 | -2.52437 | -58.07782 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d8a8b53-3ca8-3435-96b3-e1b98d95e7ca | -6.70051 | -47.38871 | 2026-10-09 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e28d960-74be-354f-befc-5c95383280b9 | -7.57401 | -61.53807 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1faca277-729d-381d-b8ec-5f34ccad6080 | -4.74281 | -55.66848 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| de6cafcb-dbfe-3618-8a57-283a45b6b974 | -11.19178 | -45.29442 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a9c2c2c-0bab-38a2-b3cb-d3a355cf6582 | -3.56746 | -54.66731 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfd16501-2c6c-3d7b-b2b0-438ecbc1f95d | -4.8001 | -56.14515 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ff724fee-493f-371a-818a-c4f9229db87a | -3.35958 | -59.48008 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfccf0fe-f2ff-323c-a891-88651c2d7a5f | -3.26616 | -54.01349 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58f676b0-3d2e-31b7-b8d0-ced2662d5a0d | -3.01946 | -54.08953 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29ab716-81ed-322d-8a4d-62d71f5b2638 | -8.32807 | -49.12101 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c836b2-6465-3434-8249-3c2cca91647a | -3.86375 | -58.64539 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dd9a5ff-a7bb-35f5-ac79-300a0ebf74ff | -7.18586 | -52.61393 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c0d3c3a-fb4c-3d37-b960-a3cac41a77e3 | -5.82989 | -53.53915 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1727eb8-dddf-3743-a606-7074c2ad61c7 | -2.22782 | -58.11131 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8051e911-14bc-3334-a3f0-d8e062b99287 | -3.56521 | -54.65871 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a970bc17-5ef1-3a93-91b8-fa08fe91eda8 | -3.93059 | -56.03065 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e8cdcad4-1e8a-3453-843e-38e312498e51 | -3.90937 | -55.89898 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe47a584-b644-3b4c-9138-4c1de0d49d40 | -3.27618 | -54.06198 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c90e7362-509b-3fb3-8933-018f95822714 | -11.98998 | -43.48423 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d7a2f4e-05e3-3d5c-86fb-30d4bd57712e | -7.90144 | -54.7207 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3221029f-ebd9-331b-9755-40be3ff519cd | -3.18913 | -60.40163 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a03ff2d2-cd75-35f5-8cd3-59a9945e0762 | -2.98392 | -54.08481 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1881c3f8-1e5e-3667-a605-a6263adf938e | -3.11818 | -54.17171 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 23d2c721-848f-3b68-b3f2-287b86006db9 | -4.12171 | -59.88282 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fb016c5-ef7b-3365-93b7-9676fcac7530 | -7.58207 | -45.65384 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3afffb2d-9b70-3819-b81d-63aaf4681921 | -8.16534 | -46.80246 | 2026-10-09 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0162bce-ec64-3e59-9f9e-106687a23430 | -8.96725 | -45.17191 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dcf5eaad-1148-335e-a3eb-1a918a32461a | -2.88461 | -54.18803 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97880dcb-7b9f-3e59-924b-e90f85def1cc | -8.32078 | -45.45213 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b98b13bd-45ec-3b1f-8728-2bb14be6d5e0 | -2.88095 | -54.16376 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afb3d09c-731f-3604-b93c-ab2227a60b3e | -2.99092 | -54.08593 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64bfcff4-4486-311e-afa1-2ffbf67b0371 | -3.02545 | -54.07472 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcb7480f-7c02-3fa7-aac0-52beee78e872 | -3.04162 | -54.26418 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0090317-89bf-3dc7-bc0b-1d55b64555c9 | -3.0486 | -54.1535 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53b1733-7dcf-3a2d-80ea-8da1e2c3aa10 | -3.0756 | -54.27747 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d94fe55c-4503-35f8-aa27-6da039fda956 | -4.50269 | -50.54372 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e85cf8bf-e31d-3506-b65a-5e96e25371ba | -3.30727 | -53.86884 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 906638e0-175f-3424-af10-4ab48c9c5d3e | -5.9532 | -40.93089 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73cdcb5f-0a49-368f-b3dc-165a3a951377 | -4.03795 | -49.05911 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e425482-4e67-34bc-a62e-fca9d556dff7 | -5.10087 | -46.212 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a35c597-2539-3a03-b7fa-7a35a37c9407 | -3.03032 | -54.11105 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25e177f3-ac02-3448-802e-d84f11706488 | -8.90895 | -45.2314 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 901498c7-63a6-3fb3-98dd-d1321e2bdf04 | -3.5962 | -61.61886 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c947463-f92f-376b-9ff6-6057febc7ebf | -12.00925 | -43.47706 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0aeb5096-cbf4-36e0-82f4-4cb4340d8452 | -6.20343 | -53.15005 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c918fc61-2e5e-3599-953b-673604786a02 | -6.51681 | -51.11847 | 2026-10-09 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d38ec5e-3f78-345c-a8ee-70cbce7e487f | -5.6963 | -53.47456 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 931bc6b2-d0f0-3e43-b229-dbf5355f6421 | -3.09848 | -59.19663 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4bc7074-dd82-3b4d-886a-7d869d3c845b | -4.29652 | -60.95601 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8433d6b7-d05e-3cdb-a285-d1d8ee57c427 | -8.91867 | -47.45239 | 2026-10-09 05:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83b1acfb-d4db-3bb0-872f-652557d64ec2 | -5.70133 | -53.4863 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f9474c2-5b27-3500-b88f-f950cb293531 | -3.73319 | -59.46453 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ce05bae-ae05-36d8-b3d6-5c6c3df49f6b | -6.48695 | -55.2907 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05df5cd1-dccd-3351-853e-0291abbd1630 | -8.74736 | -45.14418 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03e17205-d292-34bf-bf0f-f69f68ee92ab | -5.81974 | -52.11956 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6973090-f773-389c-9aaa-e67727a7c8ca | -3.05969 | -54.21888 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db2833f6-f852-30bf-8aa3-989448bb0f91 | -7.39396 | -44.7476 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9f033528-9635-3a41-98f7-7ab96debb422 | -3.07229 | -54.25289 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20473880-a64d-32e4-8993-f1688d3d7bb2 | -6.46245 | -55.49428 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ba6194b-d3a9-3de3-8301-d7a0b85e3554 | -11.83004 | -43.59338 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4a88d3bc-f3e3-3800-9b84-3886d10ce260 | -3.8818 | -55.99414 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69e53e80-2d94-3c6b-a223-c3c301680123 | -5.70352 | -53.47903 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 760067d3-cf31-34cf-8a53-9683a555d335 | -6.21712 | -52.88039 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f047290-a97c-3f11-822a-56e7172ed2a6 | -3.42992 | -54.54103 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18ff904f-3249-39a4-906f-0880428698e4 | -3.50994 | -54.62656 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db870990-2d0c-3ba6-a528-626d7ae01a68 | -6.49779 | -55.30424 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b4434ae-6449-3239-abd4-d3e69b99f0c4 | -8.21816 | -46.42963 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d24684b5-0a4a-37f9-8e43-817f88d5f176 | -3.01509 | -54.04643 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e966179e-cb8d-3f6c-8077-7aaa85ad7ff5 | -3.93211 | -56.02139 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe2b1616-ba99-3b8e-b7b1-74441fecf0f7 | -2.97321 | -54.03977 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 803960ce-df50-342f-a62f-520fe1689116 | -3.60319 | -54.58271 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f1218e0-6ec9-3cb6-8490-256b1a4c9da0 | -2.94276 | -54.11778 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ad9eb6-85c4-3bf1-9b33-0f96bb7d6fe1 | -8.96872 | -45.16131 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb7399c1-b951-39ca-9615-44c9deb25c0c | -3.17322 | -54.74561 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d399b396-f1ab-34f7-ba4f-5ff5fc4a1c4b | -3.29232 | -54.00597 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6dd0ed3-883f-3f21-8aba-03190a8ebc8d | -4.14065 | -54.02821 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ee9aa1-9fc8-3a2b-b871-d63225adfcb7 | -5.28226 | -47.91133 | 2026-10-09 05:04:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f09ac79e-1ffa-3922-bda8-8945de869188 | -3.53037 | -54.6586 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20d2765d-d723-3be4-b44d-e278b6abea90 | -8.72955 | -45.16418 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README136.md)
