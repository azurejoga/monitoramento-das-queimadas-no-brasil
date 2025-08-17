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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5cb59d0-0249-32a5-97f8-012650d96714 | -10.84176 | -45.36329 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3d682a11-d698-383f-854f-ee5257fbf9b1 | -10.83065 | -45.3209 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 389ce531-21da-3fce-8078-d3daf38251d4 | -12.55578 | -46.93813 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b6a245b-e5c3-3ca6-a950-1f7fa1348914 | -10.83733 | -45.31133 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b587e56c-0bc2-3f08-ac06-8fa994a8e6cd | -10.82297 | -45.336 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79847b50-261a-31d9-85fc-99616f5c02fa | -13.6011 | -46.8985 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbfd475b-4748-3028-9c09-1819f9f5f27f | -10.84304 | -45.30708 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e154d40-fa89-3fd4-8c98-fc9e8949e58e | -10.83795 | -45.35705 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3897cad9-0a48-3c1f-9856-f72b28a366b6 | -15.7689 | -47.80586 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c81b409-dc66-3612-8889-9b3b823a6538 | -14.19108 | -45.32135 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d828cd5-05fc-3fa2-bf96-1bead64924fc | -17.8362 | -40.12827 | 2025-08-17 03:51:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9dd34d69-ff28-37a8-8f1b-a863f7e546b5 | -10.84987 | -45.21434 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3bfbe33-7856-38f1-8d88-714aaafbdc71 | -10.84375 | -45.35264 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a548f442-6f2a-3fdf-8f51-ece39054558a | -10.84889 | -45.21956 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3b2d6ac-ee8b-3c63-8581-2c0caf0c4c6b | -12.55365 | -46.94926 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8aa27248-a43c-3ebb-8497-6059b8514054 | -10.85363 | -45.33096 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d172bd5-613b-3e77-9283-b5fb9bbb24c7 | -10.83451 | -45.35461 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3b8ede14-7e42-3e4b-9a8e-4ba6ccb7c3c5 | -13.60023 | -47.76113 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 433918fe-9e42-389c-9b6a-f45d9423670d | -12.57212 | -47.04797 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 510cfb5e-b9cd-3482-ab4b-c189c650e0c5 | -12.44558 | -47.00541 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0c44863-89e2-3976-9319-bb626afa3679 | -12.1341 | -47.91882 | 2025-08-17 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3756eae1-489c-3732-837a-e5a89c24841a | -15.64177 | -48.13777 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fcb3a72-1767-3dcd-a186-f68f03fbc2ba | -10.83737 | -45.36634 | 2025-08-17 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f65ee4b7-7d1d-3dec-846f-6f4f33b59649 | -13.56789 | -46.98717 | 2025-08-17 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d67097ce-cb58-3840-bc3d-42485087c643 | -15.18274 | -48.77079 | 2025-08-17 03:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0086806d-b8ca-354a-89a3-10d25f0ef07c | -13.60285 | -47.7763 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f803601-5080-334b-ac85-dd4ac40068dc | -13.60671 | -47.78509 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9795698d-b159-32e6-b101-2952ad9e6855 | -14.60231 | -47.95796 | 2025-08-17 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b36110af-5501-366f-85af-f4cfe15fb686 | -12.44617 | -47.00227 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 617574b3-1c3d-3ca1-8664-97473e7a4c4f | -12.57307 | -47.04571 | 2025-08-17 03:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c69a8ed6-fd88-39ef-acc8-0215572ed395 | -15.7696 | -47.80244 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 332390ee-b512-331c-b403-a9603eefed34 | -14.18569 | -45.32302 | 2025-08-17 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09ba3dad-cd3e-3550-850f-e587e234bd05 | -13.60743 | -47.78137 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9111077-fd75-34f7-870b-ad9b7de70b5b | -15.64577 | -48.11806 | 2025-08-17 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e034702-1df9-3b03-8166-b761094db382 | -12.191 | -47.23932 | 2025-08-17 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e33d53f-40b9-3ee3-8795-7115fe4234ec | -13.61288 | -47.75331 | 2025-08-17 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3575447-b01c-3a45-bd16-57d43a870ab3 | -13.4377 | -45.88309 | 2025-08-17 03:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7013f2ac-4545-33e1-96df-ee0c76c92672 | -20.20854 | -49.14053 | 2025-08-17 03:53:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7844bc79-c4bb-396e-be70-522aa63d8cc7 | -21.06443 | -50.30858 | 2025-08-17 03:53:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 96051098-2bd4-3079-9c43-f058a72e0084 | -20.28839 | -46.05319 | 2025-08-17 03:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a331acf5-863e-3ccc-8bb6-2b8926a636ac | -20.29313 | -42.2079 | 2025-08-17 03:53:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c760231a-f401-3a2b-9919-45cdd755df2d | -23.01863 | -46.23982 | 2025-08-17 03:53:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8cdac01-fa16-3dfb-bfc1-63d00b0415a2 | -19.61298 | -47.03669 | 2025-08-17 03:53:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e384fbba-d182-36bd-8206-4c7dcaecf5eb | -21.0371 | -45.7552 | 2025-08-17 03:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db8f1220-5557-3d8e-b8c1-8c6e0c1cc9ca | -21.47333 | -47.01266 | 2025-08-17 03:53:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35df8b78-4419-314d-99c9-ec240087e58d | -22.80353 | -47.47115 | 2025-08-17 03:53:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 226f46dd-c546-38f3-9f0d-c26c46fdbd2d | -20.29243 | -42.21196 | 2025-08-17 03:53:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 1e49638b-37f7-3bda-8d89-d06d73acfb8c | -19.61182 | -47.03843 | 2025-08-17 03:53:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661bf0de-6e82-3417-bf9d-2637a66b5d2d | -21.07304 | -49.39441 | 2025-08-17 03:53:00 | NPP-375D | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 48558e57-d2cf-3b0e-b34d-9ddd3df959f9 | -21.07286 | -49.39059 | 2025-08-17 03:53:00 | NPP-375D | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 38a1a30d-16b1-3d08-9e84-1302192140c8 | -20.56982 | -44.87711 | 2025-08-17 03:53:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1d606954-5450-3688-8ccc-f7b5d83ba9ce | -19.62926 | -45.2802 | 2025-08-17 03:53:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e6e8de0-599d-3a7e-899a-9700931ecdb7 | -20.01264 | -47.71007 | 2025-08-17 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dbaebe4-5e29-3ca5-9e7f-98862d20dca8 | -21.65095 | -41.23426 | 2025-08-17 03:53:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c0f6711e-4539-3c6d-9814-30d04e5872ce | -20.28918 | -46.04912 | 2025-08-17 03:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81b8e3a5-2062-3b60-accf-f92511afea97 | -21.6538 | -44.07679 | 2025-08-17 03:53:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11db2128-8374-3b75-a98c-5948ec63b802 | -19.78212 | -46.0451 | 2025-08-17 03:53:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25b8a79f-6a85-3f8d-8dc0-7cf7255bf049 | -19.63001 | -45.27629 | 2025-08-17 03:53:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a801052-0ed8-3f0e-8202-b52f18818d0c | -22.80452 | -47.46636 | 2025-08-17 03:53:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 353dfb93-1a30-33f3-81e1-bc5975df096b | -19.62777 | -45.27677 | 2025-08-17 03:53:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4dffb5bb-22ce-3da7-bc12-cc951884a3e6 | -21.47138 | -47.01417 | 2025-08-17 03:53:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b12108f0-e584-315e-b514-db828e8db192 | -23.01942 | -46.2357 | 2025-08-17 03:53:00 | NPP-375D | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 70ddb1ef-3192-3e16-ade8-93bc13fa55eb | -20.01198 | -47.71173 | 2025-08-17 03:53:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bc07291-c6a3-331c-8c54-6e5579b658b7 | -21.07378 | -49.39103 | 2025-08-17 03:53:00 | NPP-375D | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5925408e-f6c8-318b-87dc-c9da7621ca39 | -21.93265 | -44.65062 | 2025-08-17 03:53:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9be86a28-61d0-3bd7-b678-330f16150c93 | -20.29184 | -42.20838 | 2025-08-17 03:53:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 269551d2-aef8-31ce-ab71-940ed3270a1d | -19.16548 | -46.57952 | 2025-08-17 03:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea5204f2-fb2b-3dd4-8b58-3fe05471f146 | -18.9362 | -48.17904 | 2025-08-17 03:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e853a76a-3c2a-33ba-a0f0-468ecb03dc32 | -18.93679 | -48.17798 | 2025-08-17 03:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce5c9fdf-121f-364d-8e4d-7eaa444cda89 | -20.29116 | -42.21243 | 2025-08-17 03:53:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1c85ccf1-ca27-3a0b-953a-5432a5856f6f | -19.63186 | -45.27763 | 2025-08-17 03:53:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb2213ef-7356-3621-a1d8-9419d7b6dbb3 | -20.20925 | -49.13718 | 2025-08-17 03:53:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7a062cf-c937-3ecf-b86e-caf00be475eb | -19.98718 | -45.51607 | 2025-08-17 03:53:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cad8f2e-749c-361f-8ffc-0841a09b11d7 | -21.06524 | -50.30487 | 2025-08-17 03:53:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 62e489e8-6a9d-3582-8ec9-a3942c6193c1 | -21.07214 | -49.39399 | 2025-08-17 03:53:00 | NPP-375D | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| bf733b7e-c70d-3513-a424-284b15acc89e | -17.21605 | -49.58445 | 2025-08-17 03:53:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 847a0fe6-0864-36fa-95fc-8c4f799fc6ca | -19.16359 | -46.5823 | 2025-08-17 03:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cee7220-5408-3e1e-a7ec-b5ba6cae2231 | -17.06158 | -47.15246 | 2025-08-17 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16f2ddb7-0ef7-3355-98f5-35f47df15021 | -18.26647 | -45.15257 | 2025-08-17 03:53:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66ed18bc-676c-3c73-9e99-c2078b666f98 | -19.67588 | -41.98102 | 2025-08-17 03:53:00 | NPP-375D | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 362d92b9-e596-3092-97b9-c56d013fa1f9 | -17.26735 | -44.92074 | 2025-08-17 03:53:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1082be59-e815-3610-9f9f-255a40a2ce1e | -19.3572 | -43.14205 | 2025-08-17 03:53:00 | NPP-375D | PASSABÉM | MINAS GERAIS | Brasil | 3147501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b34a5bae-1917-339a-b5c1-3c647558efe8 | -16.83745 | -48.91257 | 2025-08-17 03:53:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4673f21-f300-31ae-8411-a3f77ad861ad | -19.1689 | -46.5789 | 2025-08-17 03:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e3d03fe-1ee7-3af4-b717-2af2cbf7722d | -19.06443 | -42.7183 | 2025-08-17 03:53:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0800fe6c-215b-3842-89dd-37824364e7fb | -19.67935 | -41.98162 | 2025-08-17 03:53:00 | NPP-375D | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9145c155-c878-39f0-b3b6-c9503ef7fb41 | -17.93166 | -44.37307 | 2025-08-17 03:53:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1f11ccb-4a78-3058-af2b-d03c3cc1621f | -19.06345 | -40.01271 | 2025-08-17 03:53:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4e00ff6a-6954-35a2-8e7f-6566f3d2926b | -18.62473 | -40.00444 | 2025-08-17 03:53:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8f2d02f7-23ad-3bd8-a53e-65dc097e1546 | -19.42802 | -43.72898 | 2025-08-17 03:53:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 504f90dc-35a9-3c1e-b444-8dea6eb00250 | -17.89842 | -44.41922 | 2025-08-17 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cc8ee6d-c7ee-36ee-bcfa-f8b074776182 | -18.06077 | -46.35948 | 2025-08-17 03:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75a80931-83db-3f7b-b24c-bd6d1928c5bd | -19.67758 | -41.98022 | 2025-08-17 03:53:00 | NPP-375D | IMBÉ DE MINAS | MINAS GERAIS | Brasil | 3130556 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5f4492e-eda4-3425-b14f-c51a571ec522 | -19.35354 | -43.14139 | 2025-08-17 03:53:00 | NPP-375D | PASSABÉM | MINAS GERAIS | Brasil | 3147501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54a79ae6-9191-35af-8b5d-a80a443122bb | -17.27152 | -44.9216 | 2025-08-17 03:53:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c547afc-d1f4-30cb-83ed-2980c6d8863e | -17.83713 | -46.51423 | 2025-08-17 03:53:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 918b100c-732d-3c20-ba95-b630e1449ef7 | -19.16445 | -46.57787 | 2025-08-17 03:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f163402-081c-38cd-ae99-7aba3d1fd9ce | -18.959 | -43.74692 | 2025-08-17 03:53:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07fc1769-bd83-3b13-a982-5c5020e98e92 | -19.36845 | -42.92773 | 2025-08-17 03:53:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d8bb8672-9151-3676-b7dd-1e9870254b61 | -17.50468 | -44.19775 | 2025-08-17 03:53:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README15.md)
