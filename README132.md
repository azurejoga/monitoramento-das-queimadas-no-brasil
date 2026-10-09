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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0fa02a7-cc03-3f73-a500-36dd55073785 | -5.5906 | -47.28194 | 2026-10-09 05:04:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70b4dfb2-a21a-328e-9437-d6ca647dd991 | -6.48799 | -62.85981 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3442c93-4264-35a1-a9b0-18830c031c60 | -9.69072 | -58.09779 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c3e5ffc-ab2c-35dd-a1b6-4580c42e0db9 | -11.01182 | -45.42281 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25a1ce2a-14ac-32bb-ae4e-274af59131b3 | -11.7509 | -44.92647 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bdbb00b-1dfe-3fb9-8777-cfb2bb9f4baf | -3.02732 | -54.06321 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0142c8a4-7263-39a3-9c32-9374b279dd91 | -6.00996 | -53.49908 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b5ae1d8-aa0b-3b1f-a8ba-1f230c517230 | -2.88441 | -54.09668 | 2026-10-09 05:04:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 203fc5ba-6cb0-39f8-8d16-6b0f02eb4824 | -2.98123 | -54.05678 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9306ccbc-e8ec-35cf-b991-5ca97d412a9f | -3.1642 | -58.62739 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21a7cdf6-dc8b-3ea9-a26f-f3c4415e8583 | -3.62774 | -54.23055 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88527314-35f4-336c-b9cc-f072e0297d06 | -3.72575 | -53.69738 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0bc642fb-51c6-3786-bb48-2e3b9b5f3e16 | -11.38676 | -47.56809 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8615ba2-d1e8-3af6-8463-9bb4ed689bf5 | -5.69577 | -53.45629 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8155d9e8-42b3-3efc-9c87-97f08c6bb32f | -6.49868 | -55.3209 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c7bb665-99d2-35fa-b922-ac9a1faae9c3 | -3.1148 | -53.78569 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 685e5b0c-c99c-3696-9bb0-28677d82772a | -3.08593 | -53.94348 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7da3e5d9-51ba-32c7-a881-abf82d5fd28f | -8.2392 | -48.57682 | 2026-10-09 05:04:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 502febb7-c79a-3397-9be6-e725730d444e | -3.32569 | -58.14908 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed210487-3d42-3cc6-b879-29b826f363a7 | -2.972 | -54.11459 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68a3332e-23f4-39fd-852b-61955ba66e21 | -8.14876 | -49.44045 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0325e50-a0b9-3032-ab30-a4941b94760b | -3.01448 | -54.05027 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66a7ca36-ee66-3bfc-bd92-c375c6d237d3 | -7.5723 | -61.54731 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5973a9ce-bb39-316e-a27b-be2286755988 | -4.11679 | -59.88202 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 691a8001-17e1-3c1b-8103-bd4223677faf | -3.10789 | -53.78462 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 858aaf2e-a8c3-35f0-a038-c2b545f2b5a9 | -11.01684 | -45.42324 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 02166b06-442d-389d-90df-6e072d3c9de7 | -5.23656 | -45.41036 | 2026-10-09 05:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d326cd3a-4c3b-3259-94aa-4352b15f7304 | -6.4863 | -55.29472 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e75afed-f105-3be3-8377-8941a16d0a66 | -4.07174 | -59.83945 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cfbd5a8-d0f9-3b05-9e81-7e6ec9b9f29d | -11.07567 | -44.08566 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f297513-3925-3499-9c3b-7ef7a9f1d586 | -3.29994 | -54.06971 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04ce6618-a4bd-31cc-bf1c-c373187765b4 | -3.27105 | -54.04943 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d7fa31-05cc-35aa-8447-1dab2a67c914 | -5.93417 | -51.82722 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9fd35d-2d6e-3f6b-887e-b533690d1715 | -6.10292 | -55.72543 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77418d8f-0ab6-3fa0-be59-32f6c10dbf7b | -3.91088 | -55.74776 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a148037-770d-336a-b8ea-09022ae8aa6e | -3.00978 | -54.05738 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff11e95d-b15e-3bba-91cc-8221166cb653 | -7.08714 | -52.68402 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5effaeb8-68d0-3a85-afb2-f3b401a3779b | -4.11308 | -54.62396 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69af5843-a3d2-3503-be46-86c10611c095 | -3.55797 | -54.69196 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8c5d92d4-1461-34de-86c0-d997141e7ba7 | -2.98644 | -54.13665 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cf246fc-c492-3ecd-913e-27009ac7f9d0 | -5.31765 | -55.85769 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d688ad41-54dc-3469-81ae-c2bccdda7fdf | -3.08675 | -54.29829 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7c63ea9-f822-30bd-9e22-3bc56a85a48b | -2.93871 | -54.05393 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f314bcff-20e6-375c-b995-daab1124e10d | -3.09879 | -53.9299 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1fe3c9f6-198c-34c9-ab49-526c32922da8 | -6.1199 | -51.95626 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5123c45-fa02-3d39-973f-fab9cc849fbe | -2.57948 | -56.1893 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee72d053-dd33-3d07-8a89-80e2dfb1af36 | -3.09055 | -53.71669 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4cd5df1-6b59-3470-9dc2-b300a24d2f63 | -11.22407 | -45.3219 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f6d5a130-ffd9-3476-aad5-633f77ffcba4 | -10.846 | -48.77241 | 2026-10-09 05:04:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74d797c3-9ccd-371e-a4c5-387659eb3aac | -4.29663 | -54.80703 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7aee79a0-40cf-39ae-b8cc-28458f0744f7 | -3.22058 | -54.29492 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c482a3eb-e7b0-3d82-bdc0-94eb047a69ca | -3.00847 | -54.75432 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 554318f1-b2c3-3bd6-83e9-3747a3c34ae0 | -3.07912 | -54.27799 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3a00a30-b588-3a26-92b6-d9f087c88bae | -7.18643 | -52.63186 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f65cd7e4-ff19-3133-bc17-7ab7876135cd | -4.12274 | -55.03486 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f014cf38-f079-3571-a2cd-2ddf876e04b8 | -3.58899 | -54.58045 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a6197b-0e15-3613-b3c8-a1478025f937 | -9.88491 | -50.48861 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8aab21c9-4731-3633-9609-62ffd641a1ae | -5.87821 | -53.51769 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eab472e2-cd5c-3565-97c8-d53461d95455 | -3.0029 | -54.12339 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ea4dce0-5544-3d9d-a751-86328379f5ed | -3.05816 | -53.93899 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a33e00-c3cc-32c9-9097-a64f9d9b786d | -6.45954 | -55.48965 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68b35f4f-cbe4-3246-952b-84693893900e | -3.11765 | -53.79 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d46f00cf-f480-35f2-ac07-3067a7f1ed23 | -5.86212 | -53.46754 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a11efd10-3591-3d84-9835-917d5c3327e0 | -6.10738 | -53.5036 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82950068-f6d3-37bc-8a40-e5116db3f1d8 | -3.63325 | -60.63112 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 778fdd6c-0c63-39af-864a-baeb64423935 | -3.08515 | -54.286 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6579755-3deb-3dff-90fd-a4e2068dbfef | -3.00218 | -54.77009 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 526609c2-fffe-3167-ba8e-894f21e65b3f | -2.56957 | -56.17955 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3a96e57-391a-3ea2-823f-b3d145d1e082 | -3.10514 | -54.18554 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dd2b79d-8363-37d5-bc19-015fdd3cfc7e | -3.73431 | -59.46309 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 109be651-e6b9-3de0-86c2-025d6d94c005 | -7.51768 | -47.32866 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5afd6041-9756-3558-8269-05cea96279a6 | -7.75572 | -54.94892 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4db2110-981a-3509-84a5-63dba7a87752 | -3.58885 | -54.67076 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b52673f-60c1-3deb-8a20-989392d25af1 | -5.70246 | -53.47926 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a230798c-e256-3b59-a6b1-2681f67013d0 | -9.30406 | -47.46131 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 99796f8c-ecae-3036-9b27-027f1f84a16e | -11.65032 | -43.67339 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 635ee81b-db33-334a-b5b6-beae9a3938a0 | -3.10798 | -53.93923 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a50f0f74-b812-32b4-90bf-a0182411ab0a | -2.89603 | -54.02357 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55da7740-bec9-38b5-9e28-83fef071a4c9 | -2.96231 | -54.15272 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58ce645d-ac6c-36cd-aefb-d6ea09b81c4f | -6.204 | -53.14653 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60616caa-e9f1-3b2f-9405-67a7816988bf | -6.05066 | -59.9094 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04b14d47-13d7-3e12-8aea-5fd1da5e931f | -7.09611 | -47.73467 | 2026-10-09 05:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1adaaab-95ec-35a2-b785-c472c7daf1ca | -3.16147 | -54.72709 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9eae4a89-afeb-33ed-be61-0ee942d77d0b | -8.17813 | -54.71978 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9748f2a-ee3f-32ba-abab-4e47626f2aef | -3.22065 | -53.89051 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462f57e9-ad2d-3548-92d4-8c8756995ebd | -3.90178 | -55.89778 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d3ad13f9-5136-3308-9608-3d975e0111d9 | -4.74428 | -55.65954 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a06f9a2e-28ac-3be2-a8b8-7709bce21524 | -3.00734 | -54.07275 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 674f87c6-e95f-304e-b3a3-2f2f9e6a2140 | -8.97371 | -45.16157 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd3763c6-ad54-3c53-90dc-f0a092305fcb | -2.98411 | -54.06118 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c9dfb2-6378-32a4-a716-63aaa77b8f97 | -2.91476 | -54.11329 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45797367-c4d3-38aa-b2ea-25eb1ef78c3f | -5.96748 | -55.37153 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d32fd391-a5aa-38da-a600-c7738d39baf9 | -6.05103 | -59.90777 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87355996-0dcf-3904-b90f-be0f0597d922 | -2.57328 | -56.17798 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd283502-14f7-337e-8fd3-83780386286e | -3.96996 | -51.86299 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1758a6fd-7599-3b79-85fa-e3a4b11d9d33 | -3.09507 | -54.29158 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40b761fe-4851-36ee-8e2b-079019223157 | -3.25139 | -54.03856 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d5fb4aa-03e8-338b-9f31-54b0fd6cda64 | -11.86815 | -43.56731 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d4ccc8f-1606-32be-a9c6-d7abc4b59c5d | -6.11811 | -55.70174 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e099bfc0-1537-3dfc-a6ee-cafe946bab69 | -6.04775 | -53.28394 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README133.md)
