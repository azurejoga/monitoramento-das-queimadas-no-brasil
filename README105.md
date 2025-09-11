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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ae9d9d0-103a-34b8-88ff-fc41eb9cdee8 | -13.84217 | -47.35094 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e13ac138-8355-3f4b-a1d6-a0bfc6c977f9 | -11.47673 | -49.24715 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c19d77c4-cd21-385c-9ded-3f50e332a0ab | -15.15953 | -52.41977 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7de2839c-c920-3303-b518-29d7a438d76f | -11.36455 | -46.56188 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ad2ebc89-d221-301c-853c-bd9a589330a9 | -12.03684 | -47.61566 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa94cbe4-2fc2-3e6b-ac3d-b21a815b5dfd | -13.58741 | -47.70077 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cea6faca-d5b2-3036-811e-3f6fb620008e | -11.15395 | -52.05159 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4f62a3f-4e09-30d8-a75f-4b2db70fe8ca | -9.46102 | -46.74327 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbdcced6-b03c-3dff-a2a4-188b1424bd7b | -11.48212 | -43.63681 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae9c9463-100a-3422-b1ca-9f632bf0f2f5 | -9.05857 | -50.48896 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45a77132-0b5d-366f-a9c7-a289977e2c53 | -11.72981 | -50.62767 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 29ffdaa5-105a-3f3f-a65e-273422377b6f | -10.66525 | -48.62975 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80320cc3-9c23-3b62-bd5a-546f8e02ff83 | -9.97477 | -51.68978 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61b13ec7-cd5e-388e-90ca-d81f4e697f0c | -15.65688 | -53.87081 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cbae23b-03f8-3649-adce-f7be177f96ef | -9.51717 | -54.63841 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a5d7e01-420a-3c98-985e-629a865a8272 | -11.12249 | -52.05729 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c8aa886-b5c5-3781-aba6-717cec6bd77a | -15.15123 | -52.40733 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbdb63ef-d788-374e-9091-7378f50bc03a | -12.5867 | -44.78772 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f55cbab8-7213-340e-804b-4d8bc9e1382f | -8.5193 | -51.37904 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9875df07-aed8-390e-b8b8-79a32772218b | -9.97808 | -51.69031 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9461b368-dba6-33ac-ab4f-fe85d8f592bd | -14.88169 | -55.86447 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7e647eb-4e19-357d-b6d4-063a5aac5001 | -12.83664 | -52.94244 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9a84628-5514-3c42-85b2-aa18bfef4265 | -11.8114 | -46.75356 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cd95710-e813-39c1-ab30-2b37c74fdc0c | -12.37878 | -54.17328 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5ad387-9188-3e91-bf43-0aff11031a0f | -11.47189 | -43.63563 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eae343ff-7482-3d15-9162-d592a919eaad | -14.31097 | -54.75661 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c62f6be9-d6c8-320c-ab50-5ed25c63e02c | -9.30262 | -46.7709 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ee83c6f-9f5c-32ac-98de-09bf1efe0c1c | -11.1396 | -52.05646 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff475b0f-9927-3e20-9338-8b95aafcecaf | -15.82388 | -52.22321 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 601f6da9-3c86-3f61-94f3-543b036e99f0 | -11.48969 | -50.33973 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e93d735-2ef6-38e3-b657-4114eb622757 | -8.87276 | -49.69169 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a766b1b-5dde-3807-80c0-0f6a8fa5f0ca | -13.44973 | -43.48491 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b93f637b-a06a-3d9d-9475-ae27fc266e41 | -15.66847 | -47.03514 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65990e02-1e65-308b-b733-73e23bab5a81 | -15.10533 | -50.14544 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f95b5d67-8009-3a8b-a9cb-1fc523665dd9 | -11.35939 | -46.53741 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ecf8d222-8e65-3679-b972-aeb53b571def | -14.30861 | -44.87197 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5db7e4e7-d691-363f-8eee-ae1a7aa2257c | -13.84365 | -47.33995 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ac8e7f5-a78f-384e-a053-c549e047f18a | -14.91233 | -55.87268 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a16faff-f306-31a7-aea9-0d0c8ddf4ec9 | -15.67811 | -47.02808 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 659f019b-1e85-3c2f-a5ee-19eee2db2f77 | -14.43928 | -52.94522 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4752f79c-25eb-3ec8-a2d5-a8e739d8e7af | -9.02507 | -49.77168 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0df5d4cd-3c6d-373d-97df-2be4015a7528 | -11.48089 | -43.68562 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82d8c75f-2bf5-3784-b1f7-fe6f1643e305 | -15.80334 | -52.26804 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0036479c-58ab-32c4-89f8-4a597693ab08 | -9.93906 | -46.05743 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0808bb70-53c4-310b-ae1f-356e76eb75f1 | -8.92416 | -51.05024 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d5a7458-076d-38ae-9bc1-6e81ae4a6819 | -11.35733 | -46.52124 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b1f95de-7225-3bfe-b25c-2b2aaf63b611 | -9.45616 | -46.71018 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 228dfb1a-260f-333a-a318-5082d1ccedf5 | -13.97538 | -48.2462 | 2025-09-11 04:46:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ba4e214-e7a8-3fbc-b580-e213d93c2d8a | -11.43804 | -43.57541 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 599f318f-0fd8-3e72-85e4-8d4ea9c59385 | -12.91761 | -47.97864 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80ae39f4-c309-371b-96e9-637b61722f0d | -13.27133 | -51.73086 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9185fd3-e8db-3067-886b-4946395fa2c0 | -11.77172 | -46.51476 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce2c9bb1-13c6-37fe-8b01-612668e4263b | -12.5666 | -44.63819 | 2025-09-11 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 889abc85-33a3-366d-b7a2-6fe67aa9a824 | -10.20056 | -51.67902 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75b38a97-b933-3cf5-b99d-623244fe197a | -8.51766 | -51.38947 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 120e2600-1f59-3fab-ab2f-70880dfcf78e | -11.61087 | -52.2115 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ddda853-360a-3979-b024-2912c42133d1 | -15.13724 | -48.60791 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 798a1747-31fb-32b7-b465-40cd620465f9 | -13.65846 | -45.72528 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1437c612-c85b-3673-8bc4-c18cf80e9d25 | -11.13243 | -52.05889 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdca2a0a-dc9c-3fce-adb5-00fb89ff734b | -10.32496 | -48.80919 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b7ecc7f-733d-30bd-ad38-8e85085515d6 | -14.38589 | -47.34311 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1d7e7cb-2337-341f-9482-b4f04d106f19 | -11.22554 | -55.00455 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acb850d5-a8b0-32bd-ac37-e7f51e90f2a6 | -11.97513 | -51.10999 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 234a7ede-7347-36e6-952d-6f2868d4736e | -11.10074 | -48.40536 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2df33323-1ec8-3655-ac2d-7e501bab2772 | -15.14318 | -48.61171 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a3518e01-39fe-38d8-bebd-48d1e4bf5522 | -12.0359 | -50.93731 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa66b04d-72d5-3449-ac6e-1703a8a0a2c2 | -11.12801 | -52.02225 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 493b5f4a-095b-37e3-85d4-2c1b8a3687eb | -15.13628 | -52.43788 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03f92cdd-443e-395e-b379-436723ae151c | -15.79587 | -52.25573 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7630836-ecda-3cc5-8d08-39690d557288 | -9.88194 | -50.18833 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df748bbe-fbff-3b8c-8595-8c837e81092a | -9.34391 | -48.94357 | 2025-09-11 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68bf002d-b19f-3529-b7a4-ffaf53580845 | -12.96774 | -54.75152 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a4812bd-99cf-35b0-9f2f-2ae88022187e | -11.43331 | -43.5716 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e9128a6-06c2-33d2-b470-4aec6cee8fc8 | -9.69184 | -46.75285 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca597019-01c9-38d3-bd48-c97a82e02e15 | -11.50619 | -50.39208 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7330e8cf-4e80-3e32-8e37-f8e533339126 | -9.68734 | -46.75569 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb6492b8-db27-35cc-8dc9-c82a831ddaa7 | -16.28437 | -45.68797 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 872a2e5b-aa19-3b8f-986a-5d94863ec13f | -10.41397 | -50.52757 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c9058b8-4746-3c4e-aebd-c49e1112ff04 | -14.78579 | -48.2225 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2b6067d9-908b-3a4b-9094-d2e63e5d557f | -11.34328 | -46.49902 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6d5f713-53ff-3ddb-ae43-66bba717b451 | -11.78465 | -64.92748 | 2025-09-11 04:46:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ee4228a-622f-39df-93f3-e548be510c1f | -9.09567 | -49.81304 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1c353c7-8bb6-3d74-b4ea-1b0152493a96 | -9.06863 | -50.49047 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 391bd7b0-5930-3b51-8152-6025027b4925 | -10.77739 | -46.00485 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e50cfa1-485b-3199-bfa4-8f03bd7c1bec | -12.8849 | -47.95656 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f97dade7-8aa1-3c36-89ec-f2c5c47391c6 | -9.99243 | -51.70692 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58ae63fc-6e30-3bd0-a2dc-853479e9d311 | -15.59285 | -49.39364 | 2025-09-11 04:46:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd3c01bd-8e6f-388c-8fca-91d97b67f0d7 | -12.97942 | -46.72245 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec7ef0e0-74ee-3eb4-ad81-4674dc85a4ec | -12.0522 | -50.94361 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1f7e26e-26d7-36e3-9797-86c33ab953ac | -15.16341 | -56.3543 | 2025-09-11 04:46:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81b2d309-b73f-3e77-b30c-6b8c9d991fd0 | -12.58602 | -44.79295 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b52ded70-8e01-39b8-9118-565cf30a7ea2 | -10.20022 | -46.67756 | 2025-09-11 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a80067-bab1-3369-9bc3-6f74d6c5bb4e | -15.69318 | -53.83631 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76ae903b-eb09-3ecb-92a4-6118df02979a | -11.38045 | -43.51564 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69e388ce-a90d-37d6-bf03-ffd423c773b0 | -12.42998 | -47.80763 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c89fe799-56f1-39b4-9284-8238bc7844c3 | -11.26064 | -51.12798 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 757d667c-8a05-34cd-9043-359f31020354 | -11.43252 | -43.5778 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73cd1395-2485-3190-b146-fcb2d182a5d5 | -8.08317 | -54.74452 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77ed8951-0651-30db-820a-a3ed5e04602f | -9.70044 | -43.54179 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c58d5a6-6fcf-3df5-a86a-ca4ac882e1dc | -11.47541 | -43.68792 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README106.md)
