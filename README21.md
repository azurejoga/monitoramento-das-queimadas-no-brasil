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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 203f9493-5364-3eb5-a45c-10c87a95e593 | -2.79789 | -47.14614 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f19428bf-7548-3d00-b1ac-a4cd1d0167ee | -7.8767 | -45.62483 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6340524c-00b9-3ffd-b73e-679a58b8d599 | -5.93624 | -45.07465 | 2025-09-20 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d7e08d8-85b8-3535-8e82-53a47514c9e5 | -4.87383 | -46.82986 | 2025-09-20 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e03a057a-139d-35e0-ad86-6041da29b8b3 | -6.34756 | -55.55909 | 2025-09-20 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19e3c42e-d627-3df9-8124-71eb13d61082 | -9.17405 | -44.63197 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41847fb2-1cb8-3a06-af03-a48c7bdbb6f4 | -6.35346 | -49.85833 | 2025-09-20 04:53:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c0ddcdd-aec7-33f4-8964-6a42f292255f | -4.47981 | -55.08764 | 2025-09-20 04:53:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd3d6c1b-7de2-37c8-b549-c48d06924528 | -6.01706 | -51.60616 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97158dc7-0058-3779-ace2-f5be3a6c21ff | -8.47448 | -44.71202 | 2025-09-20 04:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1480eea1-731d-3429-be69-f0328bcdffcc | -5.78988 | -43.6508 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b210d37-8301-3a9f-8848-b35a2c26260a | -7.92004 | -43.89002 | 2025-09-20 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6068c25b-77a8-3fe9-9d02-ff86629aeafb | -7.1133 | -47.85434 | 2025-09-20 04:53:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77296889-d43c-3bd0-92e2-33aa575c9756 | -4.66313 | -49.32558 | 2025-09-20 04:53:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5234e83e-e9f8-36b6-ad7f-63b5e7ac0a31 | -9.11645 | -44.65675 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eafaac36-1212-3d69-b4b2-c5ee75408ced | -2.83579 | -48.66121 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42938cf2-ac71-3654-9366-209a00181355 | -7.92047 | -43.8868 | 2025-09-20 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f85f7c67-d827-31b6-ab82-d46717acfa50 | -3.83146 | -49.1373 | 2025-09-20 04:53:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ea9afc3-1146-3a74-8f7e-c5dadcee8c4e | -5.76578 | -53.41466 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29eb1a8c-0209-3af0-841a-204fa8a7474b | -2.79235 | -47.15559 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d50666d3-1c04-3718-9f1c-2fcda59a2b77 | -3.98306 | -51.0607 | 2025-09-20 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11a660e9-412a-325c-acba-a1e4859bd75d | -5.73546 | -42.58385 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 70b38da8-954f-31f6-9b36-216157350a02 | -4.65732 | -46.03618 | 2025-09-20 04:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e54ef5-e2ca-3fa5-b4b9-6e5d7a2698df | -6.31076 | -42.92794 | 2025-09-20 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02b3fcc5-a43c-3b59-ba3b-f0a20764ffef | -9.16893 | -44.6309 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1dbbb61-29a2-37d1-b244-919845b3c10f | -7.6065 | -45.47514 | 2025-09-20 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfeddfb5-d668-3260-9211-85ea68986965 | -3.22998 | -47.12827 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03576a85-c9b1-38e3-9491-5bdf6fea0de1 | -8.49222 | -44.73377 | 2025-09-20 04:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c90c1664-ed93-3a29-89ad-b200c3de4a35 | -5.74102 | -42.58527 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b106f7ec-7466-306d-a66d-31d341efecc4 | -3.59531 | -55.30062 | 2025-09-20 04:53:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8615291-9231-3152-9688-50494cf480f9 | -6.60451 | -43.58835 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28ee83cf-8de1-31ce-9595-6f5e871f75a7 | -9.02034 | -46.31778 | 2025-09-20 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c11e972-63b1-3df1-8a63-6f74ceebbfbb | -2.98831 | -52.62739 | 2025-09-20 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4befad6b-6df0-3dd3-b496-ec53e2bd14d3 | -2.43116 | -49.33912 | 2025-09-20 04:53:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ead1cd1f-ab15-3707-b666-113cadef878d | -6.02691 | -49.87322 | 2025-09-20 04:53:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fed077f0-e12b-3390-8ead-8bb597f11520 | -4.66671 | -49.32611 | 2025-09-20 04:53:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f70310e3-b720-3c5c-9276-021b954847d6 | -3.51719 | -49.44639 | 2025-09-20 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 516ade44-dd82-3f62-83a2-867038910e86 | -9.17365 | -44.63509 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00a8eb62-14de-3ed1-a793-4452155a257c | -5.74656 | -42.58685 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4736c997-0908-397a-82ff-87692f314f68 | -7.83733 | -45.62995 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d58f17c-a26f-32eb-888f-da8a4d453b87 | -4.63477 | -51.00085 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0de831e3-f783-32a4-95d1-810515874667 | -5.10589 | -43.20738 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4c1d1d14-ae7e-3372-a45c-55d46016ab98 | -9.17324 | -44.63821 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 181f984b-f157-32ad-994c-d734d3ff9c4f | -6.18155 | -45.42569 | 2025-09-20 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bb88a70-50c2-3ca6-8692-8ae51eedffa2 | -9.11397 | -44.67522 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8804a293-5ba0-3d99-9617-7635564a8371 | -6.20113 | -41.2282 | 2025-09-20 04:53:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a57e381-835b-37cf-9ef8-9aa7e207ca97 | -5.82705 | -43.87809 | 2025-09-20 04:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8ed1630-4d6f-3f6e-b756-9424d583809f | -8.894 | -40.43828 | 2025-09-20 04:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 071ec132-187b-3dcb-99bb-c412c8222a2b | -9.16812 | -44.63716 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e14074b-7c3e-334f-8fc0-1283bcfde2f9 | -7.25807 | -45.49531 | 2025-09-20 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 029d8e8c-ecc2-3715-9f34-65624e55c13e | -6.26457 | -43.91515 | 2025-09-20 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 585a522e-686c-34f7-aecd-9709c68bb7e8 | -6.31024 | -42.9316 | 2025-09-20 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f0c3da3-f4da-3d7f-bc39-887a63c5f58f | -4.64149 | -50.97993 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a145c144-9869-3496-aed1-f6f59edc6580 | -9.11604 | -44.65983 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85709c23-8419-3b9e-9140-2d849cfdc04d | -5.10846 | -43.20646 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8262cc79-62e6-310f-9b5a-2ed1c3537c07 | -9.11875 | -44.67866 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aa0efa4-3a7f-3e29-a74f-98dc1e3a70e9 | -3.34711 | -48.39262 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 805d6d48-951f-3c25-8af1-b687284f8e9a | -4.6661 | -49.33016 | 2025-09-20 04:53:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b97d406b-3562-37a0-bb7d-e259536c7bfc | -8.48756 | -44.73004 | 2025-09-20 04:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e29520b6-0977-39f2-8086-f7bcb6e7e4ca | -2.6907 | -59.42452 | 2025-09-20 04:53:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d6b8c2f-f65b-3316-9673-6626e0bf301d | -5.04108 | -47.90591 | 2025-09-20 04:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7b4ae456-cc89-3fe7-9b7c-a5e729ea5d80 | -3.35149 | -48.38881 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 744cc016-a709-3b48-b415-4104bde407ff | -7.59422 | -45.49347 | 2025-09-20 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f77594d-4991-349b-a128-d7ab2aebbbe2 | -9.16754 | -44.62901 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29b56856-d3af-3d25-b5e3-887545f3a2e4 | -5.16476 | -45.41983 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 887c2af6-c615-3e34-a398-d9cd0d321743 | -4.29895 | -48.27001 | 2025-09-20 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc865200-739d-3bc7-ba72-878b194487e8 | -4.86966 | -46.82924 | 2025-09-20 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fccf2c75-351c-3e5f-966c-16a9e1edf6a6 | -5.55218 | -42.16085 | 2025-09-20 04:53:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c7a7c1c3-c895-364c-8cb5-6338d93c4a9d | -2.16389 | -52.10584 | 2025-09-20 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06afb466-2bd9-3f78-90cc-7990e029e280 | -4.94485 | -49.9281 | 2025-09-20 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 371e3766-6039-3921-b73d-642d333129bc | -7.83662 | -45.63497 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7392f7ea-8f48-351e-a77b-495980be8e64 | -2.7892 | -47.14989 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bc8b679-2c8e-3c33-a0a0-441aedb1c19c | -2.69296 | -59.42398 | 2025-09-20 04:53:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d7db750-8cfd-344a-99c2-642c29660592 | -6.10702 | -47.85078 | 2025-09-20 04:53:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd53195b-4cb7-3cdc-858a-5c784f452dc6 | -4.94195 | -49.92371 | 2025-09-20 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdbe5f5b-66e5-3916-8b94-760bee1f1609 | -3.34779 | -48.38826 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4860ce9b-051e-3523-bd76-fe5bf080bf45 | -3.51658 | -49.4503 | 2025-09-20 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a578d8a4-2208-3a26-a2c9-321b0fe628bc | -5.19314 | -45.48197 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bf074f2-cffd-34b5-8c2f-8da53a7df7a0 | -5.84233 | -46.28861 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22e79a8b-626b-328b-8fe5-b7c60c8dfdce | -3.59649 | -48.98778 | 2025-09-20 04:53:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9468e78e-12e4-364a-b71b-229c5f4dcb22 | -5.04575 | -47.90141 | 2025-09-20 04:53:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2280888c-fc09-36a9-bdc0-bdaddb86380f | -2.43176 | -49.33527 | 2025-09-20 04:53:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9cfa8473-e116-3b8d-800d-9b28b93ae186 | -2.92253 | -48.96259 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128ba3f5-4991-3718-8344-2cb9f897a6f1 | -7.18351 | -44.411 | 2025-09-20 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99345e50-313f-331d-8b15-33d9d898b288 | -5.74706 | -42.58325 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86b90c42-262b-3a39-9191-1ce6418b5a6f | -2.83217 | -48.66065 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daf832de-607f-34b5-9ecf-9dfbf7bbc0a8 | -4.35982 | -46.2925 | 2025-09-20 04:53:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ae49d8-6b29-305b-b792-3b7c44526d49 | -2.51647 | -51.90995 | 2025-09-20 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7422298-0f08-3eba-ac3a-107f38e8585e | -5.59289 | -44.09253 | 2025-09-20 04:53:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb75334b-aed0-3f3c-9320-70b1b4972b92 | -5.54698 | -42.15587 | 2025-09-20 04:53:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 94e00fd0-fb13-305f-8030-4fdb4b1886ac | -3.73649 | -53.8079 | 2025-09-20 04:53:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d023f5e4-9d8d-36e9-baa6-b8b4adb89a3d | -2.43466 | -49.33966 | 2025-09-20 04:53:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7e87dc2-3f68-3b81-b9e7-96647650d057 | -4.87325 | -46.83363 | 2025-09-20 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f2f7c2-960f-394a-a3bb-4215657139df | -5.84155 | -46.29069 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea4aab4-663e-306a-a4dc-6ea9f4ac47ed | -9.02097 | -46.31329 | 2025-09-20 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a44489f-1b83-33fb-bbd0-3b4bd505dd0e | -5.59332 | -44.08958 | 2025-09-20 04:53:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f756ce64-02db-354f-b92f-d32db8f8173b | -4.25864 | -54.84338 | 2025-09-20 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48ccd87d-2d9b-3691-98db-638c506deab6 | -5.11221 | -43.20134 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 236d57ca-ce51-33df-b65d-8e21db2258b3 | -5.82548 | -46.28142 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a78bc13-27ec-3c23-8957-289cdc3c8283 | -9.01833 | -46.33205 | 2025-09-20 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
