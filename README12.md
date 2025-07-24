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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f66490a-e0ce-36dc-bda8-19b531615457 | -13.70696 | -45.68271 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a9f387-cf1a-3701-88c6-58420c02f555 | -12.42829 | -45.37944 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7216a30-ecdb-3081-b7ad-04431aa7a550 | -13.70922 | -45.66844 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2647ce26-a834-3a40-a816-431b34505dcd | -14.7684 | -48.27524 | 2025-07-24 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 674cf14c-0e0c-3c44-acdb-cb1397d2c633 | -13.40715 | -44.31888 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14005e8b-3eed-3c43-bd3a-9372496b3e54 | -11.94375 | -58.77137 | 2025-07-24 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d3868068-a6ae-3cf1-9890-c619ab7b2263 | -23.05863 | -45.53721 | 2025-07-24 04:17:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3bbb4c5-67d8-30ca-ae22-8f999099aa88 | -12.25119 | -44.77883 | 2025-07-24 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6573d59-183a-34d2-97e0-13866e0f9f14 | -15.27561 | -47.13309 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85c60526-24ed-38f8-8b80-a69e70799f27 | -14.87724 | -48.34071 | 2025-07-24 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d47de60-01dd-3801-985a-8d5a2fecb612 | -13.70364 | -45.68217 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4b94fc1-a7cc-35c3-ba67-522547ed6f25 | -15.63081 | -45.90619 | 2025-07-24 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 098d8e95-dd6e-3e20-9b9e-b1d7a1125772 | -14.09772 | -46.34145 | 2025-07-24 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7db6f08d-60d6-3540-89c0-b8bce67f71ec | -14.3083 | -43.80198 | 2025-07-24 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36f558b2-f54e-3064-8e5f-70ff2f523569 | -12.2545 | -44.77936 | 2025-07-24 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31194c1c-7b09-30f1-97ca-50a3ec8663a3 | -23.06644 | -49.68922 | 2025-07-24 04:17:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cddbadc-aa55-3fae-b57b-86ef2c1f6171 | -23.36083 | -47.17856 | 2025-07-24 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 58e1b613-6d13-3bd6-9193-b6a1a59a79a1 | -8.30439 | -55.10913 | 2025-07-24 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ca33976-8bf8-3120-bae6-c82223afa0a7 | -21.61218 | -45.13713 | 2025-07-24 04:17:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87ca2409-25d8-30ef-8356-8f044261e45b | -21.75778 | -52.75034 | 2025-07-24 04:17:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15fa92df-c452-31f0-bf2e-885791107718 | -10.62847 | -45.23047 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09951084-3d18-35de-b505-a3c4055c5708 | -23.25714 | -49.55832 | 2025-07-24 04:17:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b0a5694b-c40f-31af-b75f-217278e5cbf3 | -12.35377 | -44.22966 | 2025-07-24 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7dcfb3c3-466a-344f-b81b-917ea65f53dc | -12.42554 | -45.37535 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d34e4d2d-a892-392c-8bcf-83478edc1b33 | -12.42165 | -45.37836 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ec8041e-12c4-3dfc-8406-1a7cd4efbe04 | -15.73183 | -46.18941 | 2025-07-24 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73c3f366-0351-35fe-afd6-a12fa8142b84 | -12.57624 | -56.97527 | 2025-07-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c9e2100-a850-3f86-a3a3-91517bc5a914 | -10.63124 | -45.23457 | 2025-07-24 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1472080a-023a-30f0-820e-efc0238bae47 | -14.76913 | -48.27092 | 2025-07-24 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ec98dfb-c22c-3af7-8c84-488881ca169f | -14.1781 | -45.34907 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e274507-d8c2-3f80-9367-3c892aea6612 | -14.05776 | -44.48574 | 2025-07-24 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62f0bdc7-73ce-395e-a843-636f412fa1d9 | -15.30129 | -47.38099 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60180bd3-dd5a-34df-a330-eb5181d3f56e | -22.36822 | -47.41528 | 2025-07-24 04:17:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8998d859-180d-321d-98f9-36d859e666e3 | -13.68204 | -47.737 | 2025-07-24 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1a689b70-dee4-3b23-99ee-91cb815a9b5f | -12.63318 | -47.8377 | 2025-07-24 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b1d41b9-ef3f-3ad0-8e23-fc05be2adb60 | -12.42441 | -45.38245 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04a63e99-ba71-3da9-8c6c-f474d43fb67d | -13.54217 | -44.50057 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9022abbe-2be7-37e7-b3c9-67cd4b8fa2e5 | -21.34278 | -45.4441 | 2025-07-24 04:17:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 55999c07-e61a-311f-a6b5-57de0af2d02b | -10.71116 | -48.85547 | 2025-07-24 04:17:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6598b176-8ff4-3db2-be33-92095268ade7 | -15.73853 | -46.86215 | 2025-07-24 04:17:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef3f3fc4-e3f8-3147-a53a-4fc09753ab03 | -9.66277 | -48.52724 | 2025-07-24 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f56a6f0c-9586-314e-a6ed-ecda3ff398d6 | -15.27902 | -47.1336 | 2025-07-24 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6f2503d-22e7-302f-8bb1-2efd4bb58bde | -10.17911 | -50.22618 | 2025-07-24 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a06c67e8-0876-363a-8d7a-c84747f076ac | -13.64972 | -45.7209 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 573aeda9-28a1-3992-affc-23874abaa2a0 | -21.36213 | -48.53066 | 2025-07-24 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da6ef6e3-7aa0-331e-a83a-54b90a8e0d86 | -23.2968 | -46.12859 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a453573c-7336-3613-bfdd-85c0e1d951d1 | -21.35778 | -43.75948 | 2025-07-24 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f7f92c3e-a1eb-39ce-8f15-20dd811bc07e | -11.99546 | -45.14849 | 2025-07-24 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d7d3ed7-7788-3fb2-b3b8-daaaba428cf3 | -12.66171 | -45.04434 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee661558-efc9-3db6-8d9b-c748aafbaefe | -11.94795 | -58.76804 | 2025-07-24 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| d2596834-71be-3024-a20c-5b09c5a75c12 | -11.77428 | -47.39599 | 2025-07-24 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 297e489e-d85f-34e9-ad5e-8157e7ff01b8 | -11.81058 | -44.26814 | 2025-07-24 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1fc91df-2798-326d-ae1b-f1197dfd21ff | -14.37306 | -50.33015 | 2025-07-24 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 369144c1-0325-3447-bfc3-2f3972052212 | -11.77716 | -47.4007 | 2025-07-24 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71586065-7ce5-3286-9eb9-5a2bace912bc | -14.79237 | -42.44258 | 2025-07-24 04:17:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a0415f2f-ebe1-351d-aeb0-b5f638e9d8a2 | -22.2449 | -47.05286 | 2025-07-24 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbe4737e-c3eb-3f04-8376-cc27e69cd6b0 | -20.29587 | -54.07498 | 2025-07-24 04:17:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b31ac3d1-13b1-356a-a015-de75b17f123e | -13.7059 | -45.66789 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7d3ed20-76f5-3fdc-bd23-b2bb44ff69d3 | -22.26051 | -49.57799 | 2025-07-24 04:17:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c94f0a56-8218-39c0-99ba-7e2027175880 | -11.11177 | -50.48801 | 2025-07-24 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca92adee-7b98-3375-acc4-dddafc6507bc | -20.04522 | -45.64883 | 2025-07-24 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0db3bee8-7cde-3a6b-ac7c-391555a31b9d | -22.39728 | -49.79439 | 2025-07-24 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 414aa7a2-d3ae-3324-a306-9ce4ae5c0ee8 | -21.79172 | -44.69653 | 2025-07-24 04:17:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0e2c9e56-8016-3864-b3fd-33b4baecc115 | -15.76018 | -47.77511 | 2025-07-24 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecfe3445-2067-3237-91d8-07dd150c4541 | -14.79179 | -42.44664 | 2025-07-24 04:17:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dd27d05a-aa24-3ca8-8495-3efde2fff9e5 | -13.29317 | -40.98062 | 2025-07-24 04:17:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ac8678bf-2dc0-3603-8887-f944d0800b74 | -11.46276 | -48.16374 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4a3779b8-a91a-3a16-b858-dbc1632e22f5 | -9.27219 | -50.25964 | 2025-07-24 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f90bae86-581f-3020-99b3-1c567d2c0c93 | -11.95087 | -58.77276 | 2025-07-24 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3e37e6a3-67cc-3075-941d-c92ef1a8c70d | -12.5815 | -56.98186 | 2025-07-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 231259e8-ab32-34e3-aa70-143043eec40f | -13.99838 | -44.02868 | 2025-07-24 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb312891-7591-3fe6-b5d0-d69e1102176f | -11.94549 | -58.76303 | 2025-07-24 04:17:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fcd02112-06fe-31f1-a927-c12e671a9b63 | -21.59298 | -57.60075 | 2025-07-24 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a0e754-1a38-350e-90bd-d4160fe61dba | -21.31356 | -48.56985 | 2025-07-24 04:17:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cefe79a6-0037-3d90-bc2b-95687bf07872 | -15.12597 | -48.35454 | 2025-07-24 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bffd573d-6340-36f8-b47a-8969a3b0b53e | -11.73669 | -48.18325 | 2025-07-24 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b0df91e6-26ca-3d7f-94a9-378a5b02fda5 | -11.58941 | -47.89801 | 2025-07-24 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba96b37d-dd42-3f72-af20-3a8db34de846 | -23.36862 | -47.17228 | 2025-07-24 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| adea99f4-a117-3342-90ec-d0f21355ecf7 | -13.70258 | -45.66734 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58f2b159-513f-3f14-bb4d-aef13b85e741 | -10.19938 | -48.90018 | 2025-07-24 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d416073a-9cae-3b36-92eb-2f2e7a3f8297 | -13.54548 | -44.50111 | 2025-07-24 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f7888fc-6857-3554-9685-fd5306b79ce9 | -23.7845 | -45.35453 | 2025-07-24 04:17:00 | NOAA-21 | ILHABELA | SÃO PAULO | Brasil | 3520400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9db0590-860d-376b-87cb-cb43c28fe974 | -16.60406 | -44.51812 | 2025-07-24 04:17:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e39db5b7-6eaf-31a7-ad54-a28fb081c9e4 | -16.42705 | -45.66573 | 2025-07-24 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df6cebfa-65b2-3f90-88cb-4061263673be | -13.69472 | -45.69534 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d96e1c33-916c-316a-9502-c869e12ce8ba | -23.78163 | -45.3501 | 2025-07-24 04:17:00 | NOAA-21 | ILHABELA | SÃO PAULO | Brasil | 3520400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 95b57d06-30d4-33e0-a6b5-007f4c190393 | -22.24105 | -47.05593 | 2025-07-24 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ede7880-02c8-30a5-b601-b5fdd8fe1de3 | -13.7025 | -45.6893 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7c71973-60db-34db-88d6-1a0e99b101e9 | -13.09613 | -52.14041 | 2025-07-24 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fabc627e-3f00-3b5a-925e-bd7e722872b6 | -12.65951 | -45.03675 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de3ea6f4-2083-3c2f-838d-7b0bf7de0103 | -12.42384 | -45.386 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9632f776-129a-315e-aead-e4e9886a3310 | -12.42109 | -45.3819 | 2025-07-24 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fea7d837-9da8-32c3-9c32-4dfefe0f80f0 | -11.12036 | -50.48956 | 2025-07-24 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55e69007-879d-3ad4-841c-e5353db69632 | -21.31216 | -43.7475 | 2025-07-24 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 390e9321-ea3a-3414-aab4-88097f83c087 | -11.4635 | -48.15928 | 2025-07-24 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c92fc53-a3f2-3faf-b50b-b09d6e984592 | -17.2373 | -46.79851 | 2025-07-24 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31b427c0-e0ec-370d-b082-8f3db3e8592f | -13.70526 | -45.69342 | 2025-07-24 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b6d6ecb-7bbb-3288-b016-cd124dba7472 | -11.10747 | -50.48724 | 2025-07-24 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abe58902-5ce6-3e3c-851e-5fab123da247 | -21.59205 | -57.60493 | 2025-07-24 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea55a29a-381c-3733-b19c-82e1bef5a22d | -10.00457 | -48.12277 | 2025-07-24 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README13.md)
