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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6935aaff-8b11-3f54-9f1f-72cd7dad9134 | -3.9083 | -56.028099 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac3ab44f-5baa-3470-bb65-689389068ae5 | -2.4799 | -56.046398 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bedddf40-1a1a-3460-9dfb-dce8ecb72cbc | -8.7468 | -45.1436 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9511595f-e043-317a-9681-2bad6d6088ff | -14.865 | -50.294998 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 288988dd-94e7-3b61-94b8-aafc16ffdc1f | -18.339199 | -42.246601 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4717566-18b6-30b0-8dfb-1c98e7f72cf6 | -7.5128 | -47.337002 | 2026-10-09 00:28:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 519882cb-005a-36c2-97d9-908111e96350 | -5.0001 | -45.312302 | 2026-10-09 00:28:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c364485c-d437-379a-b895-5e74fdc52896 | -7.1813 | -52.646702 | 2026-10-09 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3140017e-4623-31d4-9601-b6e6d8d9aecf | -11.1943 | -45.300499 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 121d5865-6b08-38e5-bce0-954b4b3d77a2 | -6.9922 | -47.676601 | 2026-10-09 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f56ba29-1c3f-3b7b-b841-462e7ca08347 | -13.3673 | -43.880901 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 606b4304-98e8-3778-8377-6a8d8a4249bf | -2.9742 | -54.0723 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20521d1a-c23b-36c7-8219-5780f5137986 | -2.9577 | -49.1814 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3420351e-6247-30bc-9f92-31cc799a7755 | -10.9985 | -47.478699 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3b2a97b-a20e-3169-8cd5-f0bdf38fc277 | -11.6113 | -43.6912 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b80201e2-edb9-3f66-903c-abed8ae4ea38 | -17.0061 | -41.172298 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf688921-4eb5-3cda-94d9-a9a76df8f2ef | -3.0041 | -54.114399 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb73eefd-9cab-3c3d-8fd5-59561007e7e2 | -5.6982 | -53.4715 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcfa9270-673b-3057-84e2-39bc4f4e1698 | -1.5392 | -54.5499 | 2026-10-09 00:28:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f048dd-478a-388a-b264-a1883942920e | -11.1988 | -49.411499 | 2026-10-09 00:28:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aeee0ef5-6705-3bd3-895a-15f4af248f55 | -1.7787 | -47.135799 | 2026-10-09 00:28:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dcc03d2-0a35-303b-8084-d0d69c68943b | -12.3767 | -39.483898 | 2026-10-09 00:28:00 | METOP-C | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6a0b1632-61b4-39ac-aeb0-82bf778733a5 | -5.3699 | -48.973499 | 2026-10-09 00:28:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c68352db-9a14-3617-9a1e-922a37579e7b | -9.9267 | -44.801601 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aee47305-e9bf-3511-ba45-54de277a9cab | -10.5057 | -47.3391 | 2026-10-09 00:28:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c225077c-ba8d-3436-a52b-b219de216166 | -8.9849 | -45.917999 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6108b66d-d06d-3afc-b521-7342e581b95b | -3.1225 | -54.187 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3329d391-772b-3e93-a2c2-5e260ed66cd6 | -3.5984 | -54.582401 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a496c5-e8b7-31d8-b2c0-18a801eb2ad1 | -10.4573 | -47.868198 | 2026-10-09 00:28:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 932e94aa-41d8-338c-a897-cab629b91566 | -12.0176 | -43.483799 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 107367e9-0fd0-34af-b22e-97c0e59432b7 | -11.7858 | -46.805401 | 2026-10-09 00:28:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7e7394e-d279-3e31-85f5-83672e83e00f | -10.4235 | -47.292301 | 2026-10-09 00:28:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d64c5ef-938c-3758-9755-b57ce7f58722 | -3.2155 | -54.283501 | 2026-10-09 00:28:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cde832fb-8a99-3b73-a5ed-a281bcd9eeb0 | -5.9881 | -41.382702 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4f49148-83dc-3922-9a46-ec07fd6828f7 | -8.4833 | -54.634899 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455348e1-68dc-3811-90fb-d766ec17b3ba | -5.1015 | -42.6478 | 2026-10-09 00:28:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bb566ff1-eafa-384a-b70c-f07be035468e | -8.2902 | -45.717999 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53fa2d2a-a005-3412-adb4-0e0fbc62e21a | -17.8274 | -52.361 | 2026-10-09 00:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0a0a8916-0031-310b-b6fc-883d0d77dfcf | -5.4351 | -43.453499 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10183e5c-3be5-35ff-879f-b2a727f2d88f | -5.9944 | -40.977402 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be6f9e6d-aaa2-3f7f-949b-cced1259a609 | -12.0012 | -43.457699 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16c305f1-7244-37a0-b30d-3fe949af404d | -2.737 | -54.107899 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 846b5a82-ccda-300d-a2ac-55d899cc41c9 | -6.1078 | -55.703899 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5d7d9c-6084-3413-97a0-b50024140f18 | -11.7223 | -43.635502 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29f3e9db-34f0-318d-9137-1de3adb2f8a6 | -4.5336 | -47.054001 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff1db34c-5cd7-352b-a083-eae2c8ee87dc | -6.4886 | -55.3055 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd5e78a-27e0-37bd-8399-90fb3181479f | -17.514601 | -43.673 | 2026-10-09 00:28:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2460d42b-a067-3312-acc7-1f1bc1e97011 | -3.1189 | -54.171299 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e112a03-3450-389a-a204-fa4b87a209df | -6.8894 | -45.903999 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ae1ad72-ff54-3bfb-923d-d82bdf77a78d | -2.9707 | -54.056999 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dfb2584-80aa-38f2-b3f0-e645c49294a0 | -8.9093 | -45.222698 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fbbc52c4-8fe9-353c-a42c-dd985fdead82 | -7.2258 | -55.153599 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3671d27-b3a5-3c5d-84be-34190b48b13d | -9.2761 | -47.448601 | 2026-10-09 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6159e6ed-9791-375c-a4e0-dc95495c03e8 | -8.9931 | -45.908901 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce3d24a4-7708-3ac2-a324-938a9c37261b | -18.282801 | -49.507198 | 2026-10-09 00:28:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1249104-ccc3-351e-b4eb-287216c68b92 | -5.4211 | -44.634102 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b765d0a0-f825-3033-aab2-c73cfa8a43e2 | -9.9137 | -44.790001 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23b5dc19-4bd1-327a-aa62-45ee3df4a593 | -4.5434 | -47.0518 | 2026-10-09 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff3cd8e9-6686-3a52-8f88-41f527ab86b5 | -5.0926 | -46.207401 | 2026-10-09 00:28:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08bf9255-6fb8-3ca2-879f-d1b1483d8e48 | -5.3262 | -43.429298 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69cefc50-2933-373e-a2ac-a2ca4840656d | -9.0237 | -44.372799 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 52d19fe1-8793-3d2c-9dd2-5a369e3c23bd | -11.6456 | -43.705601 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fddd9fb8-6cf5-323c-b746-caeabc5ef21c | -8.0659 | -45.638401 | 2026-10-09 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92f8b44e-19d1-3e37-a264-7b4ae03639a1 | -13.6344 | -44.424 | 2026-10-09 00:28:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1d1b0e2-0839-35a5-b04e-991f34efcf9a | -7.2011 | -55.181 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c29dd6-1003-3d7c-8f21-916a7354f24f | -8.6729 | -47.095001 | 2026-10-09 00:28:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b8ed4d6-59b3-35ae-aca8-85c18ce20a74 | -18.086599 | -42.270302 | 2026-10-09 00:28:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eaf139bc-2a82-3f64-8e9b-0a67c2c8fcf8 | -17.814199 | -52.3428 | 2026-10-09 00:28:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d88c9390-cfdd-3dc5-a0ee-b79fa3d0a316 | -11.6473 | -43.7127 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6812585e-a6c7-3420-88ff-d2f1134bb76c | -12.029 | -43.488701 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3010de-a3c2-315d-a68e-80eaeb60f7c4 | -9.1338 | -45.8479 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25c00e08-d730-3612-8645-c31f30e42f74 | -12.0257 | -43.4744 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84c7461d-bbcc-3c01-b1a3-418f54fc96ef | -6.0555 | -44.033501 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d129877-7ded-38ad-ad24-bd3583040a17 | -5.1728 | -45.613899 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9ff5da3-5fbf-3781-ba89-b1c8937d730f | -9.9251 | -44.794601 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 983277b5-268a-3c0a-87da-4438b2997f2d | -13.3787 | -43.885601 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2d23403-e07f-3edd-8264-97df48afebd4 | -4.9375 | -45.667 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c7c255c-1fe0-355b-a28d-04b3486e5804 | -17.0079 | -41.18 | 2026-10-09 00:28:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5fe7b6b-e70c-35f6-9f4d-62371c016c35 | -14.3959 | -43.824902 | 2026-10-09 00:28:00 | METOP-C | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bd7f7202-8c60-3451-af95-92e1225ec6c2 | -11.6162 | -43.712399 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ac6063d-094f-3001-97bc-da6939461070 | -12.0323 | -43.457901 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6740783e-880e-3778-a3ac-36073140bc74 | -2.9652 | -54.122799 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53870c74-1a8b-314c-ab5d-210c58c29ee1 | -9.1322 | -45.8409 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc4afc3f-c5e4-3c50-b2cb-b4d0acff6149 | 0.7787 | -51.966099 | 2026-10-09 00:28:00 | METOP-C | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 27086bfb-3cef-320f-810b-55580a012e0a | -8.9817 | -45.904099 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fb9c7b76-6a12-3963-9ed5-8f7035941f0a | -3.7637 | -58.5863 | 2026-10-09 00:28:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 182bf6d8-3165-3c56-ba9e-29063d17226c | -2.4888 | -56.176498 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d16598a-7a71-3196-8da0-ba9681b0438e | -3.5883 | -54.674702 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b24f4ee7-9bbd-3b82-b72d-7dbef250d6e8 | -11.1861 | -45.3097 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e81b61d-f89d-3549-a1cb-2d505e156dcb | -13.8777 | -43.813099 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40a5cfdf-3456-34df-9bbd-55b318bf9e7a | -6.934 | -46.598 | 2026-10-09 00:28:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b483049d-06d1-37df-bf2a-4d44a4231533 | -2.5615 | -56.182999 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 850c9ec6-a839-3f33-91e6-cad57a1c4ca4 | -6.6998 | -47.019199 | 2026-10-09 00:28:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 711c3d28-51ef-368d-aa7f-f4e76ee02a1f | -8.7484 | -45.150501 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09aa64e0-5361-3d41-8412-d692a3b916a6 | -4.2863 | -49.094299 | 2026-10-09 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26dec505-656a-3ec2-97fa-d756c7bf05da | -14.8748 | -50.292999 | 2026-10-09 00:28:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| da276896-8d77-3c84-90ae-8a0747454312 | -6.8532 | -41.7654 | 2026-10-09 00:28:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4515d17-3d6b-35ce-bd29-01d91fee4228 | -7.4116 | -44.7644 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2eabb422-298a-3499-8f38-77583353f71f | -6.8206 | -39.319901 | 2026-10-09 00:28:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b48935b5-347e-3c89-ba6d-bfc21e789ea7 | -9.0797 | -45.111301 | 2026-10-09 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README28.md)
