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
| 9f513754-fbb5-3818-b0ab-8b08b42eddc4 | -11.46517 | -50.77491 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 00c3d952-4118-3019-8abd-6b83e2166118 | -12.81026 | -47.14614 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbd84b36-3314-3984-9ec8-3dbd8f15e914 | -14.62339 | -52.03759 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5e1bc06-e461-3629-aa4d-bfcf3f6f26ce | -12.80216 | -47.96241 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a473b863-31bd-3606-9544-ddbb878f6382 | -12.7007 | -54.67786 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4957ad72-7ad1-3b03-a5b4-674a8e19ec32 | -13.01166 | -47.98467 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58bee996-d6f8-38c3-8836-23c42dde3190 | -12.69533 | -54.7138 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8e3171d-b72e-360c-92c4-607b23753660 | -12.69945 | -54.71035 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 502e3764-233a-3fae-bd7f-eddfe498d3d7 | -12.69181 | -54.71328 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 734b8788-171f-359c-a566-6bcbd3e84abd | -11.35948 | -47.33611 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08b8c0a0-cf36-37fd-88de-426c31b9de20 | -11.36012 | -47.3348 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 713b8b3c-d953-3287-85c5-d432cbd0e463 | -12.94873 | -48.02969 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cad68a3-db79-377b-a035-292e80ea3a5c | -12.97023 | -48.03185 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4eace7c-885d-3805-9a47-9f6836d67363 | -13.93833 | -44.83992 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| cdb274ea-8d48-39d5-bbd6-d93543c19fe2 | -12.04072 | -46.55245 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f07624bf-3148-387c-8be4-4951d1427392 | -11.86955 | -50.49183 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4ac3f501-af03-3e5c-a7c5-f6d833427082 | -10.75041 | -44.77713 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae841eae-3798-3c9f-9053-376ac2a7f22d | -12.69187 | -54.6888 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f524983d-5a20-33a3-8b41-e908faf67e48 | -12.94689 | -54.7407 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 535bfd18-e966-3d50-8197-c796aeed24df | -12.73125 | -48.02717 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c4e693-98f2-33e9-8d84-11905a40e663 | -12.78341 | -48.00127 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3568c835-f1ce-3c26-a2be-f55b6d8e48ce | -12.70416 | -54.7029 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f8be0314-3dcc-302d-8320-4ac0e0eddc0c | -10.91651 | -45.57051 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97509c33-2499-3c84-ba74-559bea5a6f95 | -12.70303 | -54.68638 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0e145a94-b98c-3a29-8b22-6c66b18564b7 | -8.17279 | -46.77511 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 041927be-a371-338f-9ba4-61dfdaeb9831 | -11.82048 | -50.48491 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b858c034-0a81-378f-b06a-b110eb7ce1c4 | -12.86727 | -52.97271 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16558f68-c701-3a4c-9120-6f7b794adeba | -10.93315 | -47.35573 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bb354dd-cf16-3cb3-9aa3-146599e83978 | -11.37022 | -47.34344 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56019c95-0e99-3c20-a2be-e4e617c5566b | -12.25271 | -46.79225 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 210add7e-b0c9-3103-9370-0a97e88bc03a | -12.78377 | -47.99844 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1be2ca5a-4aa5-3e35-ac52-9a5f8c0424b3 | -7.39837 | -49.98038 | 2025-09-14 05:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65ae9c1c-a7a2-3fab-b816-f3a1f3bbd085 | -11.37611 | -47.3409 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 379f3aac-80a7-3071-bece-b190f70e31ec | -14.37824 | -52.93006 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ede4175-8a32-37ff-9e7e-b7ca823bd855 | -12.66371 | -54.68453 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| c07bdbc3-9c3a-3f16-a338-8bc6e16872c5 | -11.2325 | -47.626 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7ee2741-c2be-326e-a37b-624b1ec20f6b | -14.1658 | -46.15634 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a68c4bd0-c4af-3024-a0af-f5c72ade2d5c | -8.93736 | -46.157 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f422988-d239-37ec-b6bf-7e98c138dd13 | -12.70244 | -48.30108 | 2025-09-14 05:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 608d5f85-410f-39ca-b110-5bffb82f5c1c | -12.76987 | -48.00473 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a43c7c68-85b1-3a34-a4d2-37ebefb300dc | -12.69885 | -54.71432 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 71f48eaa-85ba-3701-96d0-729f23bc37da | -12.66607 | -54.66851 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9152a67d-e56e-31bc-a3e4-65628f364595 | -12.69831 | -54.69386 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| be3c0b82-2dc2-3540-a288-e61b8f849778 | -14.16516 | -46.15496 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c858842-32ec-3145-a075-a395fb77c567 | -12.67371 | -54.66558 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e473270c-b50a-3353-ae59-57dcbc09ee0c | -11.28765 | -51.14316 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d93fc5c9-ecc1-3aba-8f51-b2caffa63480 | -12.67546 | -54.6781 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97f44c71-1ad4-30b2-8218-00ecdf2ce7fe | -12.80459 | -47.1454 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e53d7e64-90c1-3485-b72d-55fcf919ec7c | -12.70476 | -54.6989 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 24f88c28-a9f5-3c10-8aaf-e6281471ebfe | -12.77842 | -48.04045 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31a578ac-ee2d-3645-b273-ce73e153d28b | -14.36819 | -52.93525 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd18173c-0ecf-3c6e-998d-7cf21de85f05 | -13.88813 | -48.29647 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ba664c4-37b7-323e-a300-23b116b11402 | -12.65962 | -54.66341 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d437787-f8e6-3605-8601-e1f1c2c4e2e2 | -12.25847 | -46.79294 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 560bc297-0a24-3084-a978-5b5b04b7fc57 | -14.27528 | -53.00796 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 465b4e55-14dd-3b49-8c43-b0c05f29c6c3 | -12.92956 | -54.73519 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4bd9eb0f-19ac-3fae-941e-ae5be5f67e4d | -11.78192 | -46.65434 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 221cb245-af87-34a6-b067-38aa07fce7cb | -12.69712 | -54.70187 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3687f5e9-423d-3a30-82c0-322b57ff650d | -12.69658 | -54.68134 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8bb5ab6a-e8fe-387a-9fee-ac668436e83e | -12.81937 | -47.95548 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b03f5a8-135e-3b65-a169-27e7bea6029b | -11.23447 | -47.62712 | 2025-09-14 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fedd2fd6-554a-38b9-b5df-ebc6dc9ec0ec | -12.14308 | -47.59048 | 2025-09-14 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1212bd03-e529-3b4f-aaad-86669b308905 | -11.86509 | -50.49119 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 6f4060c2-9a76-3635-bec4-d0900e83dbd7 | -12.70177 | -54.71882 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 02df3b47-f94a-380d-9a8c-8803fe674beb | -12.68889 | -54.70879 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e73c75da-9a2b-34e4-9161-507bfce42229 | -13.93169 | -44.83924 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b2bdbed6-71db-3658-9878-637c38331f6a | -15.63657 | -44.38207 | 2025-09-14 05:08:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 705eea83-f1a0-3de8-8143-60c152b44150 | -11.35178 | -43.49605 | 2025-09-14 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc14e240-d9e8-3c4e-b259-2dfd5df305e9 | -11.82377 | -50.49442 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c278277d-9dd4-39b7-a043-4c0d9def9dc2 | -14.20162 | -46.32943 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 460ef33e-632b-329b-9d71-4199509cea8d | -11.44884 | -50.76177 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fee23ad8-228c-3282-b137-fc5fa6a77ff7 | -13.53446 | -43.00891 | 2025-09-14 05:08:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 38c42be5-bae0-32f5-bf8a-de2f2a676ad6 | -12.73702 | -48.02441 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43788b46-3e89-3b48-ab43-743c10f1f383 | -12.78754 | -47.99351 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1757b68b-2917-39b5-807c-7e3cfcc1faf5 | -12.06887 | -45.63864 | 2025-09-14 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4099e3a0-a1f8-3f86-aca2-dfc155f708ef | -14.17097 | -46.15868 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd07dae7-f28b-3cb7-934b-7ebda880a8d9 | -13.94553 | -44.83539 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 67dcaa13-1b60-31e9-bb28-40994e4a80e4 | -12.67723 | -54.66611 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 175b13ec-cebe-3f7f-b016-179b739bf494 | -10.8827 | -48.18443 | 2025-09-14 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbb1df83-6c0b-3562-b7c9-031658b03a29 | -13.53366 | -43.01106 | 2025-09-14 05:08:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dd7ea868-95df-38db-87de-9cc2d4cc9d5b | -8.76947 | -46.0447 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df9feb35-22d7-3cde-82a5-204d2b19510e | -12.74236 | -48.02514 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 72c99811-e318-338f-8838-ebafec49530f | -7.38972 | -49.9791 | 2025-09-14 05:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f987fb7-baff-32a4-972a-b675c5506c76 | -13.90823 | -48.30892 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adb2f7a3-e4cc-3d06-9fc7-3630ad5e4ace | -11.28846 | -51.10682 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fe463f57-67fd-31e1-8088-3de560a74852 | -10.92127 | -45.58226 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1be6a6e3-5af1-3278-8785-632389cd753a | -12.78656 | -48.00155 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 194d1707-6378-35f4-8eb4-ceb4c8052bcb | -12.92589 | -47.94898 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a0afe4a-a1f3-3da8-8d0f-22c43a57d1d8 | -11.39746 | -43.52865 | 2025-09-14 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6a5f118-c9ee-3bff-b8cb-0c9581faab5c | -12.78722 | -47.99615 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f546133-7daf-3f69-ab5a-7c955b7d2f3a | -14.62287 | -52.04151 | 2025-09-14 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a267a3d-040b-31de-a795-b9839efeb5ec | -14.36104 | -52.93803 | 2025-09-14 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec18f0d2-1601-3bb4-9e22-845199535e1a | -11.47613 | -50.75931 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0de582d9-d369-3dab-b13b-78c05a821836 | -12.68423 | -54.69173 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5fdaf39-45fc-3ec0-9018-c069ef844e84 | -12.68542 | -54.68373 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 26853f18-e65b-3862-b694-fc5ebe8ed6ec | -12.67016 | -54.68959 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 115aa61a-a2e5-3355-a98e-d4adf9e17877 | -14.15483 | -46.25144 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20c2be70-7c3a-3ef3-83ab-a308c046d4c7 | -12.76828 | -48.01812 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67e6ef44-65a3-3099-82d1-1d718ea43c2c | -11.8321 | -50.50012 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 17bf5fc6-4a8b-3db2-a8c1-5fe309549c8f | -11.39337 | -50.45367 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README57.md)
