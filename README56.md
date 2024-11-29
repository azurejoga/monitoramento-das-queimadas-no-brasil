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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4abac347-7441-3a4f-b34d-c7e2e10ba207 | -2.81215 | -54.02272 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7baaf30c-31ec-319e-80f4-a03675838331 | -1.37027 | -53.6272 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afa4bc03-85e6-39b3-9ac8-92c6b57edb9c | -1.15482 | -51.69598 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 559d858b-2eb2-3ea9-b312-037ad3a2777c | -2.3561 | -55.87545 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4de143bc-6604-3482-86ff-1e0b7650e744 | -1.69832 | -52.63628 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9bb04b1-45f4-3363-bef9-b9a6a92385bd | -0.94273 | -51.6604 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 681a76e9-00d5-3f03-8872-eb8ab069e6a4 | -2.40279 | -53.85595 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d570e6ce-7388-3917-ab0b-41788b822337 | -2.16009 | -54.47097 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ee24612-9d41-315c-9142-be682667c492 | -2.3352 | -46.87607 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1a5e4cd5-842b-3ce5-94af-ed60625fd9dd | -1.5995 | -52.28841 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f38c32cf-fdb2-346c-be5f-f146f18d07cb | -4.07102 | -46.82613 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54be405e-6334-366c-bb44-5b55c62254c1 | -1.92397 | -52.89064 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04cec1ed-5276-357a-962a-5cc375558820 | -1.34664 | -51.98531 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fb38be8-453e-37ed-9e3d-5813fe141208 | -5.31307 | -43.08434 | 2024-11-29 04:57:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0baf4202-7f5e-3d4f-adfd-4ba2ff4c571b | -3.40158 | -54.27781 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56165920-d1b2-375f-9a25-c4437aee5893 | -2.85707 | -54.10371 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8937d8ba-cc91-34db-93e8-f4625a613987 | -2.97902 | -53.8901 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77be9d0b-867c-3b37-be08-89a89e39a13f | -1.08756 | -53.36851 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 566c0693-7d0e-375c-8594-ac90f7e6516b | -1.26435 | -47.44358 | 2024-11-29 04:57:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec015465-a2cc-386d-b5b5-e22d2d751be9 | -3.10631 | -53.81488 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 273ff641-fafb-36bb-84c7-63f8cc2ba98a | -2.36689 | -53.82578 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17a56a33-3b53-370b-bd74-b874655f13fe | -2.82722 | -54.07793 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 199c8bae-669a-3420-b40a-509cd03cf0e8 | -3.70868 | -53.39885 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b7b04bb-755a-3360-99ad-577f86b68be8 | -2.69821 | -51.6796 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd12d58f-db25-3e13-9917-810718cdb4b0 | -1.20815 | -51.7855 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97285a66-bdfb-3a1e-af44-0d8e1d7f946a | -1.66383 | -52.20082 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee0a4dd8-642c-3d49-b731-c68aa28aee01 | -1.08212 | -53.38171 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a683964-20b8-31d4-80f5-dd2eb1d37f5c | -2.72584 | -51.72874 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c41feb3-67a8-35fc-929a-fee1b32a4571 | -2.60406 | -53.98275 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df4b36a0-9a69-3c64-acd5-25091de67db1 | -1.5038 | -51.9843 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e968de31-1991-3c77-b6db-ba129eb255ee | -3.99037 | -50.8737 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6850ef4c-72c9-3007-96c0-c99d16dd877a | -1.94801 | -52.97552 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5158d3bc-1c04-30bc-bacb-3507c8004f06 | -3.39333 | -54.28714 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56d1f0d0-baea-32e5-915c-2d3ab51798c1 | -2.85266 | -46.68702 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4213d8e5-92dd-3d6c-9a11-ea2b64fd4e12 | -2.29447 | -50.69013 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0052436-b695-3df5-8ccc-8961ef43c6e3 | -2.44153 | -50.42057 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e36a0c23-427d-38ab-816e-a7ca0bded131 | -2.42153 | -54.14826 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4edc2a5-3147-37d9-99d9-fde0df0f77a4 | -1.19565 | -53.87506 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5cae4e56-d4b0-371c-955c-99b0f85ea91e | -1.67865 | -52.50096 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ab4d6f0-8e08-3a83-ba4e-9dcbb265d28a | -3.03702 | -48.51331 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec103ec8-28f2-320e-a1e3-3f7465ff1481 | -1.81227 | -52.18795 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12092a8d-327d-35ac-a8ab-366b98bcf3d2 | -1.79541 | -52.14186 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7f1986-4278-33e6-965d-bde48b8c5b9b | -2.97187 | -53.89251 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b57cad2-4fa0-3f83-b06a-be14193e9921 | -5.75731 | -43.396 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6576bc2-96ec-3bf0-9a7d-12806bc183f2 | -1.70109 | -52.50855 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6305645b-364c-36ac-be32-a77a2316cc09 | -2.86588 | -53.96053 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe5e69a-c2d0-3a30-86bf-7099e233e7cb | -2.92773 | -54.327 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 179accf5-2a44-3bce-8a2c-b884166f14f6 | -1.63862 | -53.87018 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64ee578f-880e-3fe8-9656-47b391051245 | -2.98191 | -53.28199 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e5cb6f67-d2ac-3aa2-a436-b0e4bb5fc07a | -2.59726 | -54.09115 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1c1db7-1582-342c-b47c-ead5f88d0d30 | -2.41762 | -53.84767 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25a612d1-6e31-3a7f-9fb3-4981589638e5 | -3.31836 | -54.17957 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf75d305-6693-352c-88fa-8dd7804e3e6a | -2.74542 | -54.07866 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a45c5c5d-4033-3d15-a274-4dd359a582e2 | -2.85379 | -48.09686 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0954ca54-216e-37e8-b4d9-b13572dc8bdb | -2.37073 | -53.82285 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59ad7b3f-2376-35ef-ab9d-c1c0fbf93f81 | -1.14119 | -53.70013 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 837e1c76-fe5f-3764-9637-7cbbd469064a | -3.03836 | -54.18483 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c155f08e-42ed-3e06-8e7f-5918e5df9990 | -1.15881 | -52.23498 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d87d281-df89-30eb-b4b9-751f7bf22c59 | -2.69276 | -51.98889 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75729a4a-820f-3d72-be31-b65fa9c7394f | 0.98593 | -50.25186 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2b77578-0a6a-384a-bf97-8e62e815951e | -3.49907 | -53.8278 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da31b389-26df-380f-bb40-61b84c4626db | -2.20183 | -48.33311 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b577512b-f968-3a40-8319-a37843abfd1a | -2.99006 | -51.33038 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f636473b-8d85-31ff-a299-42963050a14b | -1.96455 | -46.44533 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 63650fbb-2b32-31a2-be1c-7b9c1822443d | -1.57116 | -52.29483 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c350fa1-ddb5-374e-9719-8b5ef9d73402 | -2.85543 | -53.96244 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c67842a1-0acd-36a2-97b2-ceb21c5916d1 | -1.06798 | -53.16896 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 490b5edc-4a84-33f8-b8ec-4ea1567f5252 | -1.55804 | -52.02525 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e25458e-d0d1-30d6-a629-19917324b0d0 | -3.05544 | -54.03223 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc2e7172-6ec9-3603-bd69-df020980395a | -3.50621 | -53.82539 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41a6731f-be22-3abc-a65b-60824122d483 | -2.02996 | -53.49873 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 00df0f8c-ed4c-38db-94b6-7a3a9695578b | -2.22429 | -53.66996 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 981f9b14-3362-3734-ae74-b421faf4b497 | -2.80392 | -54.03202 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42ac8291-ba1e-3ae3-8fd0-ca9cea41aeb0 | -4.90971 | -44.02936 | 2024-11-29 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 883389bb-4bf7-30c2-ace5-7ae01280b33d | -2.8496 | -54.02145 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83dc8dd8-6701-3785-8224-06c8dbc44716 | -3.33433 | -50.21962 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45be0db8-c356-361f-b2e1-b2c3d68947a8 | -3.12149 | -53.76096 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69d3f506-d660-3713-9c51-86722a1ec029 | 1.86164 | -55.8102 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 915d3400-3041-38b8-8234-872ee95c3b4b | -3.0997 | -53.81385 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98223f4e-00dc-320e-8887-0d0aaa4bbb3e | -2.86397 | -45.54152 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8485a2f9-c919-34ce-b633-9d69ab8d9059 | -2.0275 | -51.43471 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6037eb7-2317-3d5d-9843-e454baa24a80 | -3.73217 | -53.77247 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17453826-443d-3bca-9639-2dec713ca696 | -2.94659 | -53.90269 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1f27c9a-d8a2-31a3-9477-893b3c93a098 | -2.83107 | -54.07499 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c3a3699-d3d4-3022-93a9-bb602a058b92 | -1.66093 | -52.50536 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cf05d2a-3245-3f4a-a9ff-8df1a06ad3e8 | 0.97779 | -50.12547 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3042736-02cf-3136-b6ad-9181c1d52021 | -2.18896 | -50.57638 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9037e467-472a-3e91-99b2-c697c2c2dbc9 | -1.1478 | -53.70116 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c13dac1-1e1d-3eaf-9ec1-8f29550e6179 | 0.98013 | -50.26072 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e734191a-5220-360b-8a56-cff47aa4bd96 | -1.62601 | -53.88583 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee0199c7-42ac-3a9a-bcb1-f1c37b013ce2 | -2.57442 | -49.99641 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7b7dead-52fb-3c28-80b7-5aa0cc524e34 | -1.68954 | -52.43118 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4ba2438f-ae24-39c9-8c68-9bc5fa6ceb38 | -3.09888 | -54.03954 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f143cc7-f8b9-3161-97c0-130e4e4205d8 | -1.21265 | -53.55006 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634e79b2-6069-3071-b250-32a836971555 | -2.84127 | -48.09494 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 066b1bbd-b311-3daa-beff-8dc5a54dc2bb | -2.59576 | -53.97091 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c3095c2-21cc-3994-9dd7-4fa7b9ba16c3 | -3.39196 | -50.10656 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bb70236-2256-39e9-94ad-02d4fd3bc3f7 | -5.73686 | -46.62349 | 2024-11-29 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93ba0513-0840-3196-bfc5-f024dc3b0bf7 | -3.01477 | -54.05415 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53339b0c-3cae-389b-95ee-fb60c5958f0f | -3.11304 | -53.9924 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
