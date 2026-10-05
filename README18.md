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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a921baf-8625-3b5a-b421-c0c2808fe9d0 | -6.2077 | -52.82936 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a49f02df-03d8-3549-9b07-d5e514304cd1 | -1.19429 | -53.38735 | 2026-10-05 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f40d877a-4eab-3350-a4dd-366b36b9009b | -4.11886 | -49.0716 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 914e8ae2-e804-3977-938b-a77b7a27c89f | -3.08051 | -54.1774 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| aa17c061-aa39-3473-8b5c-fd59e941fec6 | -3.37611 | -54.10733 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5c9ca3a-a735-3d8e-a8f0-2e97fb6b7344 | -3.788 | -50.86943 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d92f7d6-aa44-360e-a8e1-2ea422c5ccf8 | -2.81566 | -54.12743 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fbfc280-f9f6-3388-a4f8-80aae8bc747e | -1.46058 | -53.59715 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7b0946-3e99-39cb-8105-d1e812ae1a57 | -6.8942 | -43.67025 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9e3e061-5047-3b20-8ec8-e60b8f8dd3ee | -1.61503 | -55.10647 | 2026-10-05 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82113db0-44ae-307b-9670-c23520e1b421 | -3.84826 | -50.32199 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 09dea8fc-ff51-36b5-bf03-3f90da2c8543 | -1.51827 | -54.82726 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcb7cdcf-a95a-3e28-a3cb-2c50dcf0742c | -6.31688 | -43.34131 | 2026-10-05 04:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2146e49-9c90-3630-a17d-86f9eddf987a | -6.43249 | -43.72076 | 2026-10-05 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93e47536-d094-3565-8e7b-e02c99f1d7bf | -7.89299 | -44.19979 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f296c89-4f19-3cb1-8240-20237ee26fcf | -3.11633 | -53.76185 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cac67c8e-0cbd-3b3e-a441-7d6c0ffcd3ba | -3.07517 | -49.54458 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e623fbb-b973-3c48-88d8-71973d762e48 | -2.93524 | -54.08321 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffaccac6-9a41-3e96-93e7-1566c88562fd | -3.28781 | -53.83437 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0bce4e47-aeaa-374c-9e3e-d823f22a7063 | -2.27371 | -48.74699 | 2026-10-05 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cb85660f-f8c7-39c9-8d86-2be5d195e70a | -3.31683 | -53.84836 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b826f2e5-7abd-3a12-b3a7-df7c532b9bd5 | -3.11555 | -53.75314 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d1157d1-881c-306c-92fd-f20dba31fedd | -2.59544 | -48.95468 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de0e2407-dd60-3c40-83b7-4af2d76379f6 | -3.06803 | -54.15616 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ac1c415-0ac2-3db4-852f-581d63f1e109 | -6.15475 | -43.62867 | 2026-10-05 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fb18007-b774-344f-b705-3999404064a3 | -3.04999 | -54.3905 | 2026-10-05 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1eadb822-8cce-3646-9f89-ecc52d8033cd | -2.94784 | -54.13695 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3dc5d2d-7cfd-3cca-af20-0449168509eb | -3.30916 | -53.84755 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 797ebbbb-5227-3ca8-85f2-46f9f49f7b24 | -3.11249 | -53.74061 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d36bff0-f003-3122-9067-8c3edae54578 | -2.81825 | -54.1117 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a78c0802-4dee-3acc-bc14-281c99191249 | -3.04544 | -54.22984 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c36edd0f-4d71-3ec3-82ba-c108a2a46a10 | -3.31881 | -53.85221 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c48a3c0c-1055-35c3-ade9-90d085799592 | -2.58119 | -51.87426 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66dc37c0-fff4-332d-b246-ed4994f00501 | -3.11317 | -53.74928 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d8b2a2a-9454-368b-a472-77fd0ba1ad98 | -3.11149 | -53.74645 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65d830c4-f2f7-3cb5-8d6f-fdb6dba3314c | -1.47069 | -54.53152 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07b96953-2064-325e-84f0-9ab8eb6c7e37 | -3.31731 | -53.84541 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bc5ed1a-b7f3-3114-83a8-53e3574a9d68 | -3.12418 | -53.76362 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0d75068b-c79d-3d1a-bf5a-8d76db6080d3 | -2.79323 | -54.10103 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 106d3ff6-7ca4-322e-8897-add4fa8cc4e7 | -3.61108 | -50.97751 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f9a94e-8149-32c9-b448-d29db2619067 | -3.05525 | -54.2314 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d08a7a81-1214-32a4-b1b0-dca6ec132185 | -3.00445 | -53.86843 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3a67725-53da-37dc-acce-304c15c4621c | -3.51284 | -54.61194 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea41a3a5-7943-3aa4-be43-5e0631426aad | -3.10279 | -53.71745 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bc241b60-0744-3dbe-9de7-352768c67c83 | -6.31985 | -43.34585 | 2026-10-05 04:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e475cfd7-9b61-3fa7-9535-a048b98b28f8 | -1.47674 | -54.52886 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c618d5fb-dc3b-3e3b-b71c-eb0140909d8d | -2.90823 | -54.0851 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 110b6086-6ebf-33fb-bdf7-38b69865f011 | -3.31029 | -53.85637 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7236c8-1890-3563-bd5b-86b83b33b588 | -2.58266 | -51.86544 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13378a09-75d5-37d9-b28d-d476957071f3 | -6.88297 | -43.67255 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85d06444-6507-306d-bbf2-ccc5894a4a0e | -3.15262 | -50.43559 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7406dc7-37e9-325f-81d3-9a31d02978d0 | -5.80684 | -52.75933 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a2b3147-58ac-324d-8291-9cda29737d36 | -1.88309 | -56.28239 | 2026-10-05 04:38:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bd8cec97-4363-3460-a82a-42a11a80a7af | -1.33284 | -54.22959 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d42c7eac-28ff-3fb5-8534-a62cdb68a266 | -3.00397 | -53.87122 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35593a7d-ebde-3955-ba82-9643f61d7bd1 | -2.8994 | -54.13824 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26438f90-9b03-3fd5-a7f7-d02bf0861744 | -3.31474 | -53.84547 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad28326e-4f8e-3c9c-a4b4-aedd309f94d5 | -4.30284 | -50.78933 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40f4d995-dd85-3f50-b128-960f2bb59b88 | -2.69781 | -49.03691 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3372595c-477e-3045-b11a-19b6da36a790 | -6.91316 | -43.66491 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2757448-2d4b-33f2-9819-89ae7d1cfb5f | -3.10422 | -53.70874 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9e44003a-b6ab-3297-8410-21b0a0f3581d | -1.09355 | -54.11198 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3688e076-cdf6-3d7a-bee0-44586bc261ae | -2.8167 | -54.12111 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762ee986-b3bd-3a89-83ef-9251ff5484db | -3.94113 | -55.51718 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87dc15d3-56d3-3570-99bb-794752f4c783 | -3.29387 | -49.12643 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea10ed4f-027d-393a-bc82-cd68883096a7 | -3.09991 | -53.73497 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7e54283-4431-3634-bb02-ac5651bd4208 | -3.2137 | -53.87083 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2310956f-ac4f-3f36-ada9-0c2e87d6f997 | -3.09774 | -53.71658 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef52f211-ac34-307c-b272-6aeeac9af023 | -2.82661 | -54.12606 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2637a928-c404-3ef3-a60c-4ff26d879c5b | -3.5937 | -54.31667 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebc77b04-b7f9-3843-97d8-caa149c04494 | -2.16662 | -53.66488 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9373fb9-20a9-3269-988f-a0aca4799c93 | -3.28244 | -50.4024 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c151990-a481-3461-9b93-6c731c4ba8d9 | -2.82346 | -54.11259 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8b5b614-05af-36b9-8948-473e0c9cae5b | -3.59424 | -54.3135 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cc530f0-20aa-3c9d-babc-a51f5bb77b19 | -2.81201 | -54.11707 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe800b57-4392-3fbc-959a-6028cb90813a | -3.2848 | -54.17562 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6510402-4480-3772-858a-9fb3f675df83 | -3.57334 | -55.41998 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6639769c-162d-391f-9845-b69d9ccb270e | -3.71242 | -50.64261 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5eba7bdf-5187-3816-b029-e020ec755413 | -3.11413 | -53.74342 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5c369ba-7935-3710-b1dd-901565c42ca0 | -3.2983 | -49.12262 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1676e8a1-1bb1-3fb5-8fa7-cf4d03760aa7 | -3.15846 | -53.07573 | 2026-10-05 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db0d5161-4afc-3dc3-acb1-4a8e1eaeb0f5 | -2.9423 | -54.20399 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c64469e-c2d9-3930-bbb5-13eaa4f401b2 | -2.93952 | -54.12476 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb904d5-8128-3acc-bfdc-bb225c6923e1 | -6.35448 | -42.52282 | 2026-10-05 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af6a1295-b98f-3a3c-ba04-1545211ff9e3 | -3.10183 | -53.7233 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| da35b396-5037-3b9b-8b59-c7cad99ce4ef | -3.79212 | -50.87007 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d24c0f86-bb83-389e-956f-39ce1407e3fa | -2.2197 | -53.70834 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d91aa599-3143-3297-bf74-2a2343d3e948 | -2.94835 | -54.13382 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad11a409-e9c9-3f11-89c8-13909c970464 | -4.25522 | -50.7786 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be76716e-888a-35ba-bf99-461e9adc9564 | -3.51119 | -54.62194 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3389bb5-3c5f-3ae4-bfb8-9f6f9dca2448 | -1.47618 | -54.53236 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb20b32-8eff-3f05-92c0-abeb909082b5 | -3.05496 | -54.16997 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6f58562-660a-3caa-842b-9f981e7bf533 | -0.38137 | -52.04107 | 2026-10-05 04:38:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87e7d1a7-dbff-3a47-a2a0-4d74a409768c | -3.048 | -54.21406 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c30c1b1-0971-3be9-a988-75026923167f | -2.58934 | -51.85299 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04587840-b27a-3c3a-9ea5-717976e11cd2 | -6.71057 | -45.55787 | 2026-10-05 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 022bc9e5-7f70-3147-8b45-ff5d5c61f9b4 | -3.11599 | -53.72017 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9050e42-17a6-3d70-a0cd-9017adf02c9d | -3.37353 | -54.09949 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad833b4-6856-3183-9e01-17d9a68f9922 | -3.43007 | -44.4443 | 2026-10-05 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0099032d-4de9-30a8-89fa-ad289ffb89ef | -3.88524 | -55.80812 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
