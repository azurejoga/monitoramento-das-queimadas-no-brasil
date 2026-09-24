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
| 96cee8ad-86c3-335e-923d-ee0f5312e39b | -11.59292 | -58.50847 | 2026-09-24 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5206bcb-950c-3242-b20f-eaa92f3feb5c | -8.20551 | -54.72699 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0163d39d-da03-3f29-9761-86cc79d09fb1 | -10.75632 | -44.81942 | 2026-09-24 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caa4006d-2d72-383b-b763-a891f5ca113a | -6.61071 | -59.91667 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7954d228-dbbc-3796-918e-5ccfa530fd4b | -6.66827 | -58.57702 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9f770b7-589a-3004-8542-dcb44accee35 | -10.11082 | -46.01581 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cffd604-97a5-30b3-909c-f942fcfc52c8 | -11.11021 | -48.29712 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c844990-47df-355b-965c-aa19f0cc88c4 | -8.14499 | -46.82241 | 2026-09-24 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15a06016-7ce3-3cd3-aee5-1c611d0006ab | -10.08359 | -46.0284 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e01f369a-f375-36f2-a3fc-5cb49faf8963 | -11.4834 | -47.33193 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc635ebe-8aaa-3f90-9026-fc7f6af583fd | -13.08146 | -47.41236 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3db24cb1-35b0-3303-9f70-4c460f8d612e | -13.07917 | -47.40425 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21ddda68-9f90-3ec3-bb5f-ad853160a690 | -8.45627 | -51.49063 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76b2d014-3124-30a1-8f68-1d0e329101cb | -12.41737 | -46.95376 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e21e4d8-4bde-378d-8f3f-448c190d19c1 | -11.45445 | -47.63644 | 2026-09-24 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d21854d2-313c-336f-a267-a33564c7356a | -7.89651 | -61.17195 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97614335-a0bd-306a-a7de-ca84bd7fb0c5 | -8.46048 | -48.69212 | 2026-09-24 04:46:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a38c444-108b-3a05-8a6e-4a04e7e9d5ea | -9.47524 | -40.33345 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 55.0 |
| af576719-ca7b-3ca3-890b-0164c5307c74 | -12.12119 | -47.37886 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 273d6eec-1ed4-3ace-9914-d74a99b43b4d | -10.14381 | -45.54317 | 2026-09-24 04:46:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f63db2b5-911c-3cd3-92c3-35b9c1dd1f43 | -10.45667 | -44.94809 | 2026-09-24 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa2e61a3-8502-3877-821c-ed61eb202cea | -10.07844 | -46.02068 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45d53059-f3cd-3f43-9853-8afee70911ba | -6.61614 | -59.92318 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac93be96-03e2-323d-a4c2-54a4cc9f0a84 | -11.41334 | -47.40174 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89fdd686-7339-3c3f-a50c-ce845d9e43fd | -11.63369 | -50.61398 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc6187d-9f83-3085-9d34-0555d6eb48c4 | -6.45875 | -55.00353 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5a22a33-0502-3695-9e35-46209daffa34 | -11.92209 | -50.73029 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fec74c42-3e03-34bd-922d-65862ccdb069 | -9.25501 | -46.24837 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fc265764-a421-3188-89ae-2a2957ee1990 | -11.96922 | -50.07849 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d31697b-9ddd-3a0c-9145-71b5d366f81c | -7.51626 | -61.48378 | 2026-09-24 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ebe695-ad58-3701-b9c7-be50bef9ca0a | -6.10718 | -57.67201 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbb8bc8c-16f9-377c-a574-37c98438db03 | -8.09051 | -54.98822 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 884f8e7a-d645-3499-98ff-8d7e2b6febfe | -11.42695 | -47.40388 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d05c5183-4ec2-37c7-9376-20bdf19a13a7 | -14.37707 | -47.24526 | 2026-09-24 04:46:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 876918cf-fca2-3c6d-bebd-5ab4d4f0ae88 | -10.08536 | -46.04082 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e9a0807-c51d-3407-939d-ac3347a5cb76 | -6.44262 | -59.96011 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 72c1b75d-f156-3e1f-9284-95541d043520 | -7.42581 | -49.82815 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93a7065a-a4f9-3559-8da2-19b229f9196e | -9.34877 | -50.09997 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4005b0e-3b5e-3a63-a067-22f2e881ae3f | -12.70457 | -47.00161 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f40c3159-5e74-3f64-be2d-e2f9f432a3e9 | -9.86057 | -48.50139 | 2026-09-24 04:46:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aec80bf-3ded-3f28-bd56-3927f68785e3 | -6.66602 | -58.57056 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d554b58-af4b-3675-8cf0-7fcb86c37a4a | -10.61562 | -54.00254 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a948d39-108e-3f73-9e81-2d5e94531c96 | -12.02936 | -50.28822 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89f3b39b-cf05-3fc1-8ec7-f902d61a0bef | -12.14157 | -50.75551 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7363f13-8cd3-3236-9e7c-c5a20b8a27e6 | -10.27255 | -49.96193 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e2d633e-b3e5-3bc9-9aae-c967a7a34f4a | -15.16335 | -43.56795 | 2026-09-24 04:46:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b2d060d-81e9-389c-97b0-b9d65834329b | -10.0749 | -46.02013 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c93697ff-a596-3392-89e1-89557acbef1c | -8.19656 | -48.22404 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6781939b-8fbb-3ead-a8b0-f7ffb918208e | -5.6009 | -60.19537 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aaf1ed0a-f545-367a-82ea-e96383df7e78 | -13.8205 | -51.8573 | 2026-09-24 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 734ffb5a-9951-30eb-99ea-eda70223f696 | -12.12856 | -50.74948 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 96d89bf8-e169-30c5-851e-8108f9182a89 | -6.09204 | -57.62793 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6559e1aa-c7d3-378c-88a9-29a6784d91b0 | -9.2569 | -47.34468 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f3aec19c-6d6e-332e-9a89-2a3505733033 | -9.5795 | -46.51144 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78fb67de-9ac6-3f25-b12f-2d219f6098b3 | -6.62697 | -59.93642 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79306035-53c5-3dfe-9d05-654bd8416fb2 | -12.01728 | -47.80606 | 2026-09-24 04:46:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d023b57-a09d-3e35-ba2e-cd176f958341 | -6.68512 | -55.05259 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dea444df-7a03-3e2f-b8b3-971f9bfcf61e | -10.61688 | -53.9983 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7abb528-eaa8-3b8f-8c46-251712eabf32 | -11.46392 | -47.3903 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6ee3eb7-4b3a-3022-81bd-335221a25414 | -11.31676 | -44.00598 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6a1c04f-fd0e-3fb7-83f8-044c9a7b8460 | -9.24624 | -47.3467 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 291e6351-12d1-3636-98f2-4128c73ff0d1 | -10.41788 | -49.35901 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4c2cadc-a6fe-32f7-8127-a3ab84b7cfd9 | -7.41391 | -49.86041 | 2026-09-24 04:46:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15f2e566-f87d-3216-aa18-83964d02eb57 | -6.67857 | -58.56837 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad86f223-8718-3682-bb76-a1566a583570 | -6.09436 | -57.62689 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a4b3ea3-3faa-399e-a500-e4114946448b | -6.63421 | -59.93542 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 312e91e9-2cf9-323b-bcf9-a7cf72fa4223 | -10.24826 | -50.2611 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73373077-0f78-35dd-8e23-b494b509da8e | -8.90374 | -45.90961 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68843c1a-847e-3daf-8eb1-34d24852bfcd | -8.45715 | -48.69159 | 2026-09-24 04:46:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aded2415-fa15-3f3d-9c25-e2205256dfc7 | -7.58957 | -57.66187 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23eaac78-3b64-3ab5-8cf0-2450da3142c5 | -10.71926 | -48.74032 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b164f1f7-5205-3c51-aae1-dda028885674 | -11.13135 | -48.30751 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0026fbf6-79f7-3a02-8b47-2787ece647af | -13.46101 | -46.26875 | 2026-09-24 04:46:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f1e5131-4a7f-3544-8925-49d3be3f4378 | -10.9788 | -54.09332 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d88f845-d48a-3ad4-9591-bb1a93cd0214 | -6.30449 | -59.95142 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c63ff5f-2246-3847-b652-005d2728e867 | -10.10215 | -50.19196 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d74cb2e-c07a-3177-b004-419a9f2ab940 | -7.97075 | -45.2237 | 2026-09-24 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60040c59-44b7-3792-ad47-95f074919b27 | -6.88881 | -59.21975 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0a4c669-a8ed-3148-a69e-de046239b9c4 | -6.60876 | -59.92732 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 77de2403-c9c5-3517-b568-39eea39aa85b | -11.40882 | -47.36264 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39b5299e-b778-3254-8656-81ba0782c096 | -8.23429 | -48.21598 | 2026-09-24 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a31180eb-cb49-3b63-9263-364d951b85e8 | -6.67497 | -58.5737 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ee55868-a12b-3f29-99c6-551fda34ea76 | -10.07537 | -46.01047 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d450bc11-614e-30ff-babf-8efefc75eb21 | -5.99668 | -57.72065 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ae94bcd-e730-3c18-88fd-aa90c7f72a70 | -11.7949 | -50.98981 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7e3ef7-1dd7-3d0d-87be-f3d2e2ed52bd | -11.22286 | -51.36256 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8858da4-8c89-3aa6-ab9f-39df010d7dc8 | -12.14059 | -50.74009 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c7c0491-a112-3a00-a30d-38921906d44c | -10.08595 | -46.03687 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28582f00-2960-3c04-9b5a-b00a278f3b13 | -11.93183 | -38.29059 | 2026-09-24 04:46:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6b00795e-5b7d-32e2-947e-10f4a981719e | -5.90913 | -59.9261 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c06ec11-cd15-331a-94cd-b81e92670025 | -10.08712 | -46.05335 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f998985e-d41e-3ae4-8322-f39353b2e45f | -11.42853 | -44.18668 | 2026-09-24 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f4bf1e7-72bb-3f57-8fda-c8b3013cb43c | -10.24818 | -49.98389 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a702ac5-7f5a-37cb-83b7-f28892168593 | -10.12838 | -46.06775 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb66e5f9-f996-3ad1-bf6a-192b38804e2a | -5.65606 | -60.21585 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52edeb31-6cb3-3311-9923-7cfba23bdacc | -8.93136 | -44.28499 | 2026-09-24 04:46:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08fdc4ed-5a32-351d-86f9-777df4748af1 | -8.91898 | -45.90403 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d60b6094-f34f-367c-b14c-79cc107202f8 | -8.30376 | -44.76894 | 2026-09-24 04:46:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adf752ab-9f52-380d-af2d-202962d8973a | -9.96928 | -47.98513 | 2026-09-24 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f6e44b-4812-3919-b71f-b3715427ab65 | -8.58732 | -54.62379 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
