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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 352b5205-891a-35f4-b239-7096ed612737 | -11.60544 | -49.82307 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed799c8b-e1c3-3ed3-a3fc-4a749bbd589e | -11.37693 | -50.85326 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 153a6e68-ca29-3391-a612-e12b97d13576 | -7.27266 | -47.90824 | 2025-09-18 00:52:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fb50d84b-2821-39f2-a82e-70161c571e48 | -7.26408 | -44.90847 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9723ff31-7f6c-3d1f-8372-04067a09859e | -7.26161 | -44.9021 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9141c154-d75c-3f5a-bd5d-8e95369e3098 | -8.07985 | -50.16603 | 2025-09-18 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 627e0664-379b-3aef-a24a-0db9e1639402 | -6.69532 | -46.33083 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 4bbff054-77c5-3a4b-be9f-c90c9317c3e0 | -5.81319 | -53.43609 | 2025-09-18 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53ba5a72-381c-3442-a327-e99b3ea20743 | -6.13528 | -47.80841 | 2025-09-18 00:52:00 | TERRA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 12e49f62-3244-3041-a39f-b3a4d71b33f0 | -8.65789 | -46.44701 | 2025-09-18 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a7f04c97-14d9-3257-8cf2-8bed022e85d7 | -9.08465 | -59.02307 | 2025-09-18 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b1b3df39-f3fc-34d3-8ca9-40c256570627 | -8.54534 | -48.97404 | 2025-09-18 00:52:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4806cb00-be56-3b6f-866f-afb448dd1e5f | -8.72657 | -50.02889 | 2025-09-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01afdfcc-4c36-36cc-84b9-d36c3823c236 | -6.51922 | -51.19449 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2189c78-b4e9-3efb-a182-7ccce733eaa6 | -5.08776 | -43.84517 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a23c84ac-7e67-3daa-85bf-a3fadc428c10 | -7.25126 | -46.61748 | 2025-09-18 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| d9197ecf-ea7a-34e6-b5f8-542c99946e53 | -5.80566 | -45.92567 | 2025-09-18 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6d6c3169-40ce-3202-a852-2ce60ad9c2a5 | -11.38609 | -50.85188 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 7fa20e2f-2940-316f-9a62-cb1f1259ef1c | -7.52201 | -45.28801 | 2025-09-18 00:52:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 52f29822-d00f-3283-886c-bebb5c7941a5 | -4.7183 | -46.12505 | 2025-09-18 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 86890668-2479-398b-a975-aefd36f29ac6 | -8.97621 | -46.30514 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4260f3ce-9877-35b6-9eb1-10c629d9f64f | -9.12764 | -48.12229 | 2025-09-18 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 14e5bb9b-2de0-3b25-9ab3-f97f9db550d3 | -10.84619 | -53.7829 | 2025-09-18 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c165e2e-a0cb-3165-9c4b-dc5a115f7db5 | -7.4197 | -49.9938 | 2025-09-18 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b99e326f-9318-3811-8615-1e58345bcf33 | -8.99625 | -46.34584 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a641b316-6231-3996-a720-becb157b654d | -6.72001 | -44.14759 | 2025-09-18 00:52:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| bdab589a-fcda-3d30-bbea-a414c1f0ecb4 | -4.62019 | -47.42569 | 2025-09-18 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 87583f1b-5cf2-3fd1-9c04-780f37bf09d2 | -10.641 | -48.73279 | 2025-09-18 00:52:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d274b9be-714b-33a5-b6ad-94ea53824a79 | -11.47727 | -48.70114 | 2025-09-18 00:52:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a9641791-30ac-3e4d-b17e-c02760e77de8 | -5.09052 | -43.83752 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b3295f9e-d5ed-310e-8a2f-482d7c924b6a | -4.72454 | -46.144 | 2025-09-18 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 18c359f0-d518-35f7-abb0-d50ea06107b4 | -11.20108 | -47.38303 | 2025-09-18 00:52:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bc94e206-54a8-3dcc-bad4-90d14fd250e1 | -5.62947 | -51.73124 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6705e192-4458-3bad-9dd5-26a79610022a | -7.26707 | -47.91472 | 2025-09-18 00:52:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| efaeab34-274b-383e-b89a-e6c4a306ff7f | -9.08128 | -59.03008 | 2025-09-18 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| dc36a377-c237-39a9-8c77-dbf455d617c7 | -12.26268 | -53.9112 | 2025-09-18 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7924bf1-6a9b-37e3-8c8f-8d5a16649b17 | -11.59581 | -49.82459 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8abacc12-fd47-37d2-a480-5ebbf670ae76 | -10.63897 | -48.71969 | 2025-09-18 00:52:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b88b6485-f482-3882-828c-7b7779683424 | -6.89358 | -44.78076 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9aacd016-0ffe-360a-ab2b-22eeae431205 | -9.14267 | -44.90001 | 2025-09-18 00:52:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| a0d1ab1b-e287-352a-a618-c01b8de44714 | -7.19763 | -48.60658 | 2025-09-18 00:52:00 | TERRA_M-M | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ae5847a1-63b8-3342-ad31-019515697c3e | -8.72826 | -50.04021 | 2025-09-18 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5727d3d8-3635-393b-81d6-25b884aa8c57 | -5.82005 | -45.92358 | 2025-09-18 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5fa45501-ba2d-36ea-ab38-96d7885f9c8e | -7.27898 | -47.91292 | 2025-09-18 00:52:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2fd87cc2-1b19-35d6-8d6d-561467404f76 | -8.63245 | -54.64322 | 2025-09-18 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85121898-5d36-3d2a-b568-41472895f30d | -7.41137 | -50.00714 | 2025-09-18 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8753ffe7-ca66-3201-94ac-3f5e5dd1c42c | -3.60649 | -52.6268 | 2025-09-18 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ac1f0e9d-eb7c-328d-bf77-4f847d9a18a4 | 0.45487 | -50.89279 | 2025-09-18 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4f66c3bb-0748-35a6-95a3-1a974205fe76 | -3.27397 | -49.14841 | 2025-09-18 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 98b2f7df-1355-3a13-bf7a-f295dc53afbe | -1.76343 | -48.05271 | 2025-09-18 00:54:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 49748854-61d9-3c37-aa9a-a52fef9db591 | -2.71301 | -54.9523 | 2025-09-18 00:54:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 99e82235-2753-3fd8-8740-35073903b40f | -2.91397 | -48.30901 | 2025-09-18 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4963a78e-420d-31d9-a8ea-0400a670b885 | -2.38206 | -47.72135 | 2025-09-18 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f937c2e2-f70f-3587-90a8-f9dfd2f61251 | -0.68429 | -52.36849 | 2025-09-18 00:54:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d4c2cf8a-137d-34cc-9824-2a14cf2dcff6 | -3.51483 | -49.45992 | 2025-09-18 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 14ba33c1-472e-3ec1-af95-9bbb6c0d11e7 | -2.71423 | -54.96112 | 2025-09-18 00:54:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c8e4533-28fe-3de1-aa5c-b4429882b75e | -3.51329 | -52.75151 | 2025-09-18 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| a65fba8c-e562-352c-8a75-699012972032 | -2.91567 | -48.30312 | 2025-09-18 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e1c922be-d5ad-356e-9445-df5c6ea65a6a | -3.51269 | -49.44508 | 2025-09-18 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e4b8259a-7656-3ec3-9913-53134f83ee87 | -1.58382 | -54.12326 | 2025-09-18 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f874707-ffe2-381c-a8cf-7f968a19a844 | -3.19463 | -54.97174 | 2025-09-18 00:54:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d6422155-aecf-3742-896a-a220b3ff0a54 | -2.38564 | -47.72733 | 2025-09-18 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 9433c669-94f0-3221-af1c-0d08cc689f85 | -3.19586 | -54.98062 | 2025-09-18 00:54:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8f7168cd-e1cc-3c0c-ae45-85356c2a7245 | -2.92645 | -48.30719 | 2025-09-18 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 26737d4f-7cd7-350f-a88d-158616f1a274 | -2.91848 | -48.3217 | 2025-09-18 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 1f41ef53-2f20-34c4-bbce-ece871528b39 | -13.9838 | -44.9645 | 2025-09-18 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f9186f7c-9c90-3488-8d6e-14d05f5ec1cf | -10.4085 | -61.1915 | 2025-09-18 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5d07fa79-8910-33b5-a205-395cb055f1d0 | -10.4084 | -61.2108 | 2025-09-18 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4983bc3f-533f-3e1a-8ee1-211576ee3819 | -22.3457 | -46.7406 | 2025-09-18 01:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| e6b800b6-09ac-3ae5-9492-01a75a82d675 | -19.054 | -48.25 | 2025-09-18 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| df3a4962-4d39-3957-a43a-51cc93337177 | -19.5869 | -57.7765 | 2025-09-18 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.1 |
| fe61cd89-66be-36ba-90b4-93899fef946a | -5.8245 | -45.9129 | 2025-09-18 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| cec87efb-423d-320c-a91d-c1df57052230 | -18.5505 | -46.0369 | 2025-09-18 01:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 937407f7-4e19-378c-af3d-61d6f617188d | -6.558 | -43.597 | 2025-09-18 01:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e1414fde-885d-3be9-8cfc-db59b3131ce6 | -9.0826 | -59.0212 | 2025-09-18 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8fde80c8-f848-3ff3-b3d8-1add7e0d57d2 | -4.6971 | -41.9748 | 2025-09-18 01:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 2282e2fb-bbc7-37a0-88a6-186539e284a0 | -9.0826 | -59.0212 | 2025-09-18 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 36b5bccf-baaf-3f27-942f-9b10077f49b1 | -12.2331 | -46.7794 | 2025-09-18 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 35304e94-08ca-3194-b7b9-e43d734397f6 | -6.5935 | -45.6532 | 2025-09-18 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3e4a8957-c16b-3073-a406-22dd21ad5140 | -4.6971 | -41.9748 | 2025-09-18 01:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| b5701cd0-a5a2-31a9-b11c-278db91f72fd | -4.6973 | -41.951 | 2025-09-18 01:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 804d302e-7567-3c26-afcb-a995f3d2d3f8 | -12.2523 | -46.7766 | 2025-09-18 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 7e00dfca-0195-3c33-ae13-254796c36f2d | -17.917 | -40.1616 | 2025-09-18 01:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 4755a33c-feb1-3f83-adce-d0848669cb09 | -19.5869 | -57.7765 | 2025-09-18 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| f637c459-feea-326f-8b11-3f8d6ef3be55 | -22.3457 | -46.7406 | 2025-09-18 01:10:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| e7b4ddd3-ab12-3bfd-b089-83c0484ca2fc | -7.3847 | -47.0378 | 2025-09-18 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| f20d70e0-d68a-3b0b-bcd3-fedb5c15ee75 | -18.5505 | -46.0369 | 2025-09-18 01:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 142a383f-1b10-3cb9-817c-1d53adcc16dc | -18.5499 | -46.0606 | 2025-09-18 01:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 18886ed3-ccdd-3077-9b43-d6ee2f38d61d | -13.0747 | -42.1261 | 2025-09-18 01:20:00 | GOES-19 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 60.5 |
| c5446894-3b52-3d66-a02d-66316fcd4606 | -6.6995 | -46.2946 | 2025-09-18 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 91db3bcf-fcbb-36ef-a147-8addd400efa8 | -21.579 | -51.8618 | 2025-09-18 01:20:00 | GOES-19 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| 5682d3b6-4d43-330d-96c0-3c9b7754b79c | -6.6122 | -45.6517 | 2025-09-18 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c4618c31-60b5-3727-96a8-bc99d40eadf0 | -6.6808 | -46.2961 | 2025-09-18 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| bd41f640-b9be-305b-8527-fe7be8e2e78c | -18.5505 | -46.0369 | 2025-09-18 01:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6649da2d-3d03-3f26-bc97-14cd184c42a9 | -19.5869 | -57.7765 | 2025-09-18 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| d128433c-41cb-3f21-b075-95f07d2c2358 | -6.6806 | -46.3184 | 2025-09-18 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 6fe8fc00-6c5b-39bb-a334-b9b0f3eeabc2 | -6.5937 | -45.6307 | 2025-09-18 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 5a92c215-4eda-3086-aade-609f33692dda | -6.6124 | -45.6292 | 2025-09-18 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 178.5 |
| cf8f27f8-5862-3e0a-b0af-1cc5bc708905 | -6.5935 | -45.6532 | 2025-09-18 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d3a13347-8572-357f-8863-e87ce022a479 | -7.3847 | -47.0378 | 2025-09-18 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |


[Clique aqui para ver as próximas entradas](README5.md)
