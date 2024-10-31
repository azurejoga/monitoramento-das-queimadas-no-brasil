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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0fe2fe9-1596-3459-9e14-0c64266abf0a | -2.16788 | -47.95146 | 2024-10-31 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a0116ad-ab24-33de-88c2-084cb7db67d4 | -1.96617 | -47.9505 | 2024-10-31 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9093b68a-4dd7-33a7-805b-a63a3ca14672 | -1.96553 | -47.9545 | 2024-10-31 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7f13363-7027-3389-876b-e7aaefef4edb | -1.96262 | -47.94994 | 2024-10-31 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef61b228-5f5b-3aeb-8448-8fe9ed615243 | -1.96198 | -47.95393 | 2024-10-31 04:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd69a6df-253c-32e8-9516-1b92f97f3e19 | -1.66604 | -47.77147 | 2024-10-31 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05d5c013-f72d-359c-9a3d-dfe655910adc | -1.6625 | -47.77091 | 2024-10-31 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fe6437e1-524a-3f86-90b9-7be84845c5b2 | -1.34881 | -47.74945 | 2024-10-31 04:23:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b355556-b1d3-3aa5-94ca-878e38505e06 | -1.34526 | -47.74889 | 2024-10-31 04:23:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b22d3a0-6b61-368d-ab6b-687148e3ffc3 | -1.27482 | -47.24098 | 2024-10-31 04:23:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14084b36-c14e-3507-bd6f-4f3612136274 | -1.27406 | -47.23782 | 2024-10-31 04:23:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf9bb193-6549-3558-bca1-4381170b5464 | -1.27347 | -47.24162 | 2024-10-31 04:23:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fba8866c-5a94-37ad-a02a-4fd459343b4b | -1.14283 | -47.31561 | 2024-10-31 04:23:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65b20114-099c-3e6b-9ff7-958bf9c02fd0 | -1.13994 | -47.31123 | 2024-10-31 04:23:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f0b745b-cea1-3da4-87c8-82ecac618d75 | -1.13934 | -47.31507 | 2024-10-31 04:23:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1265f77c-7e98-3dae-8f2a-d71a2f9d0a06 | -1.05701 | -47.63298 | 2024-10-31 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59887404-5ccc-33f0-a9a6-7665c72eefee | -1.05639 | -47.63694 | 2024-10-31 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff2300cf-38dc-3fdb-800d-f7e9c52d45da | -1.05347 | -47.63242 | 2024-10-31 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fef94e4c-875f-3c3e-8324-19b63b99c56f | -1.05285 | -47.63638 | 2024-10-31 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a73cc35f-1296-37fb-a763-51f30d8de71c | -0.897 | -47.59796 | 2024-10-31 04:23:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a28395b-9295-380f-bd8a-cbb88278a848 | -0.89675 | -47.59696 | 2024-10-31 04:23:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b7d203f-26ac-37e8-99cd-7315a851d72c | -3.24533 | -48.47023 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51f4191e-2577-3ce7-8742-1a0d0c52c798 | -3.24401 | -48.47155 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b16218c1-5743-3758-aa3a-5089f33f36b1 | -3.09826 | -48.66174 | 2024-10-31 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2934f063-fda7-3517-baf5-39bce12b3051 | -2.91241 | -48.61239 | 2024-10-31 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cf4e28c-c69a-36c6-9890-fbde89a1db67 | -2.9081 | -48.61602 | 2024-10-31 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfb02f57-9d6c-3e83-af8f-04cac07c9904 | -2.90446 | -48.61545 | 2024-10-31 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33371171-14e1-36e5-b084-4cbb6cf6c5ba | -2.82486 | -48.43783 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 897e9a5d-ab83-3799-8bf1-6e816df1516f | -2.82419 | -48.44195 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54afc271-682b-3990-a6d2-964360a039f5 | -2.82059 | -48.44139 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c11c74ec-6e40-3b6f-94c7-94af394d66fd | -2.52251 | -48.46177 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9741cecf-7714-3bf7-84a4-b1430a0fac69 | -2.52184 | -48.46593 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f1e8293-1e55-39be-9815-db344a9ad1fd | -2.52117 | -48.47011 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f85a013-7e8e-32b0-a390-0a986407e1af | -2.5205 | -48.47428 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a51e96e6-22e7-3a3a-9336-f2322e81e6d3 | -2.51983 | -48.47845 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db1f7b77-f5dd-3da2-8d23-fb1a7e9ee8c7 | -2.51889 | -48.4612 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f3b4ec1-ff9c-3f90-bc4c-956eed125dcf | -2.51687 | -48.47372 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 884dd087-8072-3c07-b725-adf1f01968ea | -2.5162 | -48.47787 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f535494f-09ef-3668-a946-a230ac291337 | -2.51459 | -48.4648 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 482ebb24-9b84-3af3-ae80-13f41083d3a0 | -2.51391 | -48.46899 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9288cd9e-c7e3-32af-8c11-97732174b084 | -2.46104 | -47.81051 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3fbf4de-5069-3bea-829c-927b5ae4427c | -3.24825 | -48.46804 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01b03380-991a-3709-8972-2605d722d42b | -3.24599 | -48.46614 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe17eba3-1049-36c9-a247-d33ccb72d56c | -3.24465 | -48.46746 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03f19c0d-ecde-3025-8542-056b75e0b019 | -2.8894 | -48.28882 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34fa7060-d125-3686-9e37-7180f4135eac | -2.88583 | -48.28826 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ee1225-9f64-3f72-a28f-c0cd25cabccd | -2.86189 | -48.46064 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc8199af-2dc8-30d1-bbc9-a7ecc89652a0 | -2.66944 | -48.12838 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fe16105-5984-372b-8918-d5a834e6f692 | -2.66588 | -48.12783 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc31e7d7-3ebd-3216-86bf-b28a87977480 | -2.52842 | -48.47128 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88234ffe-0d89-3923-bfad-0ea1481fcbb1 | -2.52479 | -48.47069 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2dff4285-3ada-39db-87f0-671e2dc5d550 | -2.52412 | -48.47486 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07e7b447-f155-37f7-92a5-4f7bc06f09b1 | -2.51821 | -48.46537 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9027fb66-6a1a-3470-8fc9-1bf167656ed3 | -2.51754 | -48.46954 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abd21696-f09f-3538-876b-8d8ffd135468 | -2.5168 | -47.45697 | 2024-10-31 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4172f30-a141-36cb-a4ce-d10472ce97b9 | -2.44494 | -48.50227 | 2024-10-31 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3918bf41-0ff7-3a4d-937e-53dd89ed2c21 | -2.4321 | -48.46593 | 2024-10-31 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 007b5a9d-685d-3aa0-bd92-4d78d8d747c8 | -3.94976 | -48.13461 | 2024-10-31 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09af2d64-967d-39dd-9b6d-f13957e9a42f | 0.08454 | -49.87082 | 2024-10-31 04:23:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37807c6f-1ffb-38ab-b679-44113513a663 | 0.08397 | -49.86724 | 2024-10-31 04:23:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adc8e5fb-8a00-33ac-840d-81eb4852a0ca | -0.61229 | -49.44083 | 2024-10-31 04:23:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 475e009a-aef1-3f5c-b885-8dc67180aa38 | -0.61131 | -49.44273 | 2024-10-31 04:23:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc63824f-0d31-39a8-b434-42e5a16e924c | -2.01346 | -50.25148 | 2024-10-31 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c5325fb-b805-3146-861f-28bdb39d27f8 | -2.01289 | -50.25504 | 2024-10-31 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d891c5e-b851-3b2f-a8e7-3f25839dd13b | -1.5811 | -48.72073 | 2024-10-31 04:23:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f99f6ebc-9ea6-3cba-af6e-936bf4a08c87 | -1.57938 | -48.72155 | 2024-10-31 04:23:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5030e1c3-f54b-32c0-badb-92f9493b0cfc | -3.45844 | -50.30253 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19b393e8-d121-3ee3-8798-7233acff54d3 | -3.45762 | -50.30764 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 22273199-c0bf-38af-8107-27278c77d9b7 | -3.35687 | -50.26369 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4c1ac89-7014-3949-badd-5a88ab4b2471 | -3.26974 | -50.34555 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8870f00c-9c84-32f3-ae1c-b4693352b983 | -3.26917 | -50.34902 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5358f90-77de-3d6d-8ea4-1d007fadbbd1 | -3.26806 | -50.3479 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85d6648-817b-346b-8b17-413f71e3c5bb | -3.2657 | -50.33688 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b8e4fa76-0026-38b7-afef-bb875506acd0 | -3.26516 | -50.34838 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29a414f9-f1b2-30db-bad6-645d8aa6d57f | -3.26515 | -50.34034 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 960ae357-5498-36be-a758-3c01ae13ac75 | -3.26459 | -50.35185 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f89798-53e9-3c10-9f73-94abcd7b6332 | -3.26406 | -50.34725 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c1c5294-a14d-3c70-9b0a-03d124887111 | -3.26169 | -50.33624 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 958c54ab-ebd2-324f-8eef-0b10e33bd316 | -3.25769 | -50.33558 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7db7ed61-b6e6-3de4-9589-af57a22d7e2c | -3.25714 | -50.33904 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2c9ac60-4f7e-3a62-8bb1-a5143185d213 | -3.25659 | -50.34249 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 910035d5-1605-391b-b199-be8ca24400c2 | -3.25368 | -50.33492 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8215df76-a880-3d4f-bce7-959803bd806e | -3.25313 | -50.33838 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 513f936f-8c6d-3c6b-a456-6f49b14d61e9 | -3.25258 | -50.34184 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80842463-1df6-3aff-816a-f19f484b6dde | -3.25148 | -50.34877 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f03e3f17-cfbd-38e9-af6c-87d0c1fb85f0 | -3.24913 | -50.33773 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dcbc2a8-ffb2-3da7-8e75-746e2266cb82 | -3.24857 | -50.34121 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0936fa12-f24f-39e2-9a04-8773917e04ea | -3.24802 | -50.34468 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02a0c413-cc54-31fb-aed0-604c6ed8eb6a | -3.24747 | -50.34813 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f59c09-1b70-39d3-9989-1cd3876b3ea8 | -2.79128 | -49.47724 | 2024-10-31 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36d174c0-2255-3a25-9624-a283d39c74bc | -3.46161 | -50.30828 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6f77288-ae86-35ea-bed2-44ad8d58a966 | -3.45446 | -50.30188 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68f53b04-c46b-301b-ab9d-2b7e2b1c710a | -3.42629 | -50.22401 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 126cff6e-335c-3083-b3dc-0be918667dfe | -3.35605 | -50.26878 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5764d6a1-c29b-30ce-8554-fad30972531e | -3.29009 | -50.2345 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec6fe315-4f3b-3192-8ed6-947dc29eaa41 | -3.26861 | -50.34443 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ffb211a-369b-37cd-a822-d2d360a24b5e | -3.26751 | -50.35138 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12a0c158-5db0-3e8d-a310-d85fb67da662 | -3.26631 | -50.34147 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cc49479-d254-30d9-a3df-2581aa346ff0 | -3.26574 | -50.34491 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21fee051-5f95-3ce0-8eee-1c38d5172cea | -3.2646 | -50.34378 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README20.md)
