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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 818ee8a0-9fec-3d16-8166-ebec07a41b9c | -10.28922 | -44.04439 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15753238-99e8-3536-9df6-35dcd08b9ede | -5.06224 | -45.85539 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e02e4e43-1e64-3ab4-92d6-6b87ef97e398 | -5.27854 | -43.26281 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22ac72ef-768c-33cf-b897-99ac9391396f | -10.57683 | -47.42745 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5991c3e-ff90-36aa-8184-c3574ceeb3ec | -7.16278 | -44.9945 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f29d468a-4a8d-3213-913e-0d892f03f425 | -10.59527 | -47.39989 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6ee4aad-f069-3a62-a2d1-9c946c7d6b2b | -5.87845 | -43.91439 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d4ccc58-1d68-3ba0-8cf7-43868e31574a | -8.82417 | -47.30911 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef23582e-7676-33a4-9f77-60fbbc644466 | -11.48417 | -44.16647 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b61c7c-e675-36a0-9a2d-1632c61bef55 | -4.83273 | -41.46707 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51694a1a-3b5f-35cd-9210-6bfa7d2e42eb | -11.48755 | -44.167 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc1fd00d-484a-3562-8f4c-fb08ae942eea | -8.08318 | -45.4176 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e5353d1-d934-3e01-9a37-3e9e45c07b73 | -10.92705 | -45.42253 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af496a00-df46-37c8-9fec-e3cae26cdc5e | -9.24506 | -44.38023 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a12d52d-e60d-3c49-9393-1686d3fe69e1 | -7.11301 | -44.7459 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f62af976-d3ad-323f-b958-40c34a70f39e | -4.93294 | -41.54607 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27715e23-d0ec-3379-8d62-febe5678d329 | -8.81822 | -47.30411 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2778e1ee-0ea3-36db-8831-6133d635d4bd | -9.45536 | -40.58617 | 2025-10-17 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 23e546cf-6987-3b89-8427-a5277ce2c0c3 | -4.8155 | -43.19872 | 2025-10-17 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f461c6a4-3f91-36ee-bb8b-9bb4477a62e0 | -4.21472 | -48.35683 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f2654c4-3de9-399d-8061-700a8d3b0eb7 | -4.91316 | -44.34086 | 2025-10-17 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c034e068-b210-3f60-a443-a2d14f306149 | -6.40509 | -41.89475 | 2025-10-17 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed9febdd-176d-3b5f-8e53-92c944f7e8a8 | -5.72078 | -43.83308 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae88cd7-4a35-3f6d-8b5e-e849b709f312 | -10.87068 | -47.93225 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 749e721b-0853-380c-81d3-a84e9ebe35b3 | -10.43173 | -45.02069 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27762e89-fdb5-3605-b9ac-ced4a224b996 | -8.2587 | -44.07124 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14c04255-e30d-3390-a401-f0e8a31ccef7 | -8.45655 | -44.17815 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 717e64a3-e11e-3dba-90fa-0ea4499b8ab4 | -3.8179 | -52.34342 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba24849e-aa8d-3ec4-83ee-c6ccc5694ac9 | -5.76533 | -45.58783 | 2025-10-17 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58538312-a9dd-3b95-8c5b-8dddbe1e8974 | -10.71779 | -44.53071 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7224eb1-5082-3f01-9bb2-97d0825a62e3 | -11.40166 | -44.2551 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38578119-e7ed-3907-abd3-04b53ad41db8 | -6.22348 | -41.54221 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e5164ca1-ef32-39fe-a6c1-71d4c7747f95 | -7.17687 | -42.18203 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43e031d2-3dde-3a21-aeb3-21239c339add | -11.49844 | -42.39298 | 2025-10-17 04:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 25d0d2c6-3a13-3e53-8087-b0711273a405 | -8.25799 | -44.03132 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23e7c44d-28a1-3e18-814f-0c1dd684a59e | -9.08706 | -48.02472 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d69f6a5a-066f-34a9-9c72-e51d621dc8a2 | -8.38423 | -46.24551 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9892c2c-a583-3e02-8c8d-40adbf016d35 | -6.21147 | -41.54887 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2cc9d771-5cfb-3283-9c83-25534c6a5133 | -10.13822 | -44.58533 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5952aaa1-f03f-3171-a118-fcbfadbb765e | -6.32152 | -43.62259 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c869fbd2-14c8-347b-b5e4-f58d329a454f | -10.10181 | -44.57975 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bb4b0e1-67ee-3f56-b73c-4af194ab483b | -10.71003 | -44.53686 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4fa307a-f4b0-3d8f-912b-8da4b4a7375e | -6.89043 | -43.99068 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f69c6320-5bfb-385b-9859-e5ffe869bf48 | -8.21226 | -43.31017 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 06b31bb6-0999-3d56-8763-7a4b3998de22 | -10.58908 | -47.39508 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bee86d1-685a-3754-b55e-31c479efed57 | -5.0298 | -45.13698 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e40ee0b9-be9f-3152-acd4-c8654e4b7a01 | -7.95189 | -44.12122 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d2c0f6a3-ea7f-3986-a323-aec5b9b1c3c1 | -9.05445 | -46.99382 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ea7a0ba-0b59-39b9-abd0-aa4fa1d0db14 | -10.26062 | -44.05119 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5199bf74-e038-38bc-bfce-be24d6b05a8c | -8.23249 | -44.8315 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c97e8be-5d32-3c4f-9a18-b9fb06164e8f | -3.83942 | -44.54819 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb0838d-16ff-3b89-b5d5-ccb6efd3fa2f | -6.13673 | -41.77861 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 478ee201-fe08-33c7-a5ee-afe0de05a886 | -5.34627 | -43.54963 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42578c1a-2dba-3d51-9e8a-058bfb19c604 | -6.67131 | -40.84702 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bacdd919-c7f6-3fa8-93d7-3e36f79ca99e | -7.59008 | -46.08143 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c1c920-8af8-3859-abe7-3f1bfa18b69b | -4.08012 | -43.39883 | 2025-10-17 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0e6ae3-9694-3095-9a19-3cff1ca07a9d | -9.22643 | -48.59005 | 2025-10-17 04:19:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cf6cd74-2576-3259-a0a9-2882dac428c0 | -9.98052 | -47.00944 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 062bd9b8-70b7-33fd-8334-1bcd8739e199 | -3.28883 | -52.54747 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a402e8f6-f370-3f76-914b-822cedd9ba4c | -8.73612 | -40.59692 | 2025-10-17 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b8ccb95-6d25-3eb5-8339-dcc634220e1f | -6.36093 | -45.48075 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaddb453-4456-3c22-a401-3ba9d5b41b7a | -6.95521 | -47.71559 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 257edafd-9575-3ff5-ae10-3c29ae4d2065 | -3.27079 | -53.25515 | 2025-10-17 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a50b4ed-4ad9-33d3-8f54-c1643ad48f09 | -5.46191 | -44.64266 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a974a3f8-6b41-3fda-9c79-ed85d81200f5 | -7.27462 | -41.96362 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7849c16d-762c-3c91-9215-3b7e7d124c48 | -6.40296 | -42.54609 | 2025-10-17 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 56e514b1-814e-37f0-83f7-a61eeb27d86c | -11.40159 | -44.23259 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dc546ae-2172-355a-9cef-6c20be0bce49 | -11.38573 | -44.20009 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9741fb12-34d9-3b88-9724-7be77014da9d | -8.84071 | -44.39998 | 2025-10-17 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e86643f8-e2af-34e2-a703-c660d3b4cc31 | -6.59245 | -47.0689 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f1b45cb-9bf0-3bfd-bbb2-7a091a3af962 | -8.38364 | -46.24913 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d222b121-e269-399e-9e9d-00ba8312725a | -9.30006 | -46.92912 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7963afd-4b5d-3a33-beb6-de1c0b88432d | -6.78762 | -47.0402 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c801560c-fad8-3519-b910-8d96dc9b8c7f | -9.15686 | -41.05209 | 2025-10-17 04:19:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 630ce12b-d6e7-3503-8850-24874b079989 | -8.09981 | -44.98423 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7240a93-7a0e-3694-b2b1-7bfa0f11e6bd | -9.73621 | -45.20647 | 2025-10-17 04:19:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e85e726-49c6-305f-bc6a-c3ae4de852e4 | -8.31852 | -47.86172 | 2025-10-17 04:19:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a514421-07df-39aa-aebb-596bc1fa4c4c | -9.88579 | -49.11971 | 2025-10-17 04:19:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0db89d1e-f591-362d-b27d-63609f7e9e4b | -10.27411 | -44.05309 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40575405-8761-3146-9ba4-bcfed851fad8 | -6.8877 | -44.68591 | 2025-10-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dba4aedf-038c-33bc-bf4f-3ad01f3052e0 | -10.13472 | -44.54145 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50dedfd8-864c-30ea-b6be-6e593bbd7438 | -7.90009 | -44.98117 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dd12972-8e9a-3f89-942c-bc8633532dc0 | -8.47211 | -50.10675 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f1b2575-e3b3-38e0-b9dc-27f086bb3949 | -5.87937 | -44.75868 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f847466-dbca-3394-a970-298d1e9dbd4a | -8.23044 | -43.44035 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf4d4acf-a877-353d-b6d5-58f0b55257e4 | -5.62883 | -42.67321 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9eb0612-bd7e-3f25-af43-c486fc7b5e82 | -10.30325 | -44.04272 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| affa62a6-5ceb-3811-9a9d-d503194c0a3b | -5.8753 | -43.91027 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82b7d916-6eba-369a-9655-6ad422b4507f | -6.33282 | -44.01077 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2578beec-f429-3d5a-96ad-4af9611c4858 | -5.29097 | -47.92778 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7674f8ed-c7f7-3772-9f79-751c69d37c17 | -11.39806 | -44.18697 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff7a5e7-d099-3f2f-8554-b7a7f0cd73f1 | -8.24858 | -44.82037 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24a9c0e4-fe4d-3b95-be75-ba41e84c5f2b | -9.21765 | -46.89285 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea4a29b-0443-3381-b988-dc18e7fdb045 | -4.25518 | -48.56921 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ab51d12-e9cf-3039-8a55-cca9a94556d2 | -6.93478 | -43.68124 | 2025-10-17 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 071cb4a5-86a7-3e9c-8fd4-3f507a52b28e | -4.64003 | -42.50897 | 2025-10-17 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9b420350-1b37-31c0-9b32-05bb09d5051d | -5.64872 | -44.71124 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05946412-4a45-3f82-abf5-c79a7312c747 | -7.67948 | -44.62708 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 247eeaa4-b4a3-315e-9bbf-8ea925ac0e23 | -5.88829 | -43.89458 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d67e12e-f1e4-3a84-857a-104554d45cd6 | -5.25766 | -44.20515 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
