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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1aa9c25-0fa2-3cbc-a2c9-e9be8973ad4f | -8.37477 | -45.02098 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff77da2-3c86-3652-a776-714948ad11c0 | -9.89228 | -46.48182 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f55a1b4-9e21-3051-af1b-836d725c5e84 | -7.86881 | -46.25302 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99d19506-1da0-3e27-b93f-2d33bbb31101 | -11.45558 | -49.26979 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d00ba3a8-bcab-3214-ab16-1ecac8af7b69 | -9.02137 | -49.7919 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de8493ed-4fc6-30ad-92f1-25921bb4f3d4 | -9.1694 | -60.79383 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe6f0e2-c1a4-3e92-8ce8-a3683eb85a55 | -11.43858 | -43.68803 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99ece4fe-edcd-33e0-a30c-546a7fe9451b | -7.40203 | -61.63457 | 2025-09-09 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6559933e-68e0-3a89-9b4d-fb814b585288 | -14.30816 | -44.87682 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d64a8bb-2d91-3966-a5c1-56c0488b72da | -8.40634 | -49.09889 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 264e15e4-b8e8-345d-9648-6e01dc0aff55 | -9.7235 | -46.78633 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8731f4e3-ac75-347c-8332-7e32cb05a2c3 | -11.20624 | -54.99968 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2a05d4d-b483-3608-a177-85c88bcc001e | -12.18705 | -53.88391 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35e239bb-63f1-315f-9959-157fd020b076 | -11.12017 | -52.02631 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc6d5f0-84fe-343d-9965-a1cb3eded4f4 | -11.94899 | -50.97088 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1632663a-51b0-3b8e-ba5e-857c104758df | -12.15888 | -49.07834 | 2025-09-09 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c52b2720-1bdb-3714-8a96-729f9df8e637 | -7.3954 | -61.63227 | 2025-09-09 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 740fe0ed-1779-316b-bd4c-953b0305b496 | -10.1583 | -46.21198 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| efaef368-2711-3b1b-b2d6-f545d8ec719e | -8.5011 | -44.64691 | 2025-09-09 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f5038ab-c8e3-3c36-b0b4-840bfd0f1bc4 | -8.06866 | -48.63121 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99907fa8-388c-3bd3-885c-2f76872cbb39 | -12.84025 | -52.94579 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 56d87d0b-2971-3e1c-9e39-9465d96f35d8 | -11.30833 | -46.50972 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8099d90c-ac4d-3fb5-aa04-a91216acaa00 | -9.87612 | -46.58859 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df15bb5-6754-39eb-aaa5-724508cfa772 | -8.19889 | -44.7649 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a0a4aef-4688-320f-9fa6-66d26679079c | -10.98075 | -45.11168 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a6d4e10-ce5a-3321-915c-3411f6accc8e | -9.87441 | -46.52978 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa760bc4-5ea1-388a-b3fd-d35b3aa8041e | -9.35504 | -46.50734 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d71f2b36-1bb7-3381-b2b9-bbd3cb7e868f | -8.33545 | -45.05956 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a706b730-21c4-312c-88e3-dd143772e92f | -13.29825 | -43.75142 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81eb7660-36c2-32cb-a74b-659129ced9c5 | -13.12865 | -54.92389 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e33f26dc-a76d-3328-805a-d509150387ff | -9.13865 | -60.52813 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3a9741e-d948-36dd-8218-61fdc840a53b | -13.19934 | -51.77216 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 952feffd-7ab0-3d4a-81fe-6550d3b294a2 | -9.18533 | -59.37681 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7c940b-b348-3bc0-a237-c4b7d9875dce | -9.09591 | -49.5163 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed96ba03-2ac9-33fe-94da-52154713b97c | -12.83006 | -52.93956 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d4c5586-d014-3719-b123-bd6dfebbfadb | -9.56213 | -48.67152 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 961801d0-a0ed-3d63-9402-89d0b218bb24 | -10.98139 | -45.10713 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| e8421d6f-aadb-33ae-b9a3-122236b3256c | -8.02528 | -44.50793 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52119d69-0b1c-358c-8465-a78397454f99 | -10.33297 | -46.34629 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e2efdb4-bbc2-3b37-b32f-d3de0373da08 | -12.02922 | -51.08306 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0e6100f-3e84-34f0-b090-1ef6d5ec77ab | -6.54743 | -54.98669 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90a04b61-7ff5-391d-8298-ca97ea2ec77d | -10.56998 | -49.18702 | 2025-09-09 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4535f931-f8e7-3765-ab5d-30592be1cd40 | -9.85776 | -47.79623 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b867298-418c-3d19-9f45-0e0184d4cf0d | -9.85163 | -47.79166 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd158e5e-dd1d-3327-acaf-37a061ce12b9 | -8.37822 | -45.02463 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91021f32-ac1f-3364-84b7-4d364ac7585d | -8.87601 | -47.90199 | 2025-09-09 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc079e22-e3d8-3969-a5da-50632573327a | -8.70363 | -45.32931 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f68cc921-ecaa-3c88-a202-91b0b0f4ee35 | -11.13186 | -48.42059 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f12758ba-01cd-3adc-9530-f77e5fca749c | -13.03434 | -48.02736 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa93d5b4-14e2-35c7-a332-08bfc44d7d66 | -9.16455 | -60.79476 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3002c021-e289-3d68-9c54-e717fc427574 | -7.4291 | -49.27373 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24adc223-7115-3c5f-844b-e36e143f7c6f | -13.0126 | -54.82234 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa94dc1b-da11-35dc-8ad4-d3986373e2b2 | -7.99359 | -46.33347 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 709f6ea4-86ca-3980-a632-1f7dbd4cfee8 | -11.84246 | -46.76371 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 341db21b-503a-3397-a1dd-eba146c94944 | -11.84304 | -46.75974 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46e0c120-9da8-3243-96ed-74756ddacc04 | -8.65724 | -45.74106 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9debaec4-b629-3c92-8c04-2629a25f71b6 | -8.21303 | -44.77163 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47e737fa-1325-3f58-adbf-caeadf98936b | -6.40315 | -58.20941 | 2025-09-09 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e0ceecd-769a-3679-af59-8363fb2aaa09 | -12.30881 | -47.23523 | 2025-09-09 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86be6651-4c79-3299-b610-8c4c86a7fa18 | -11.22408 | -59.13081 | 2025-09-09 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00ac0335-b6e1-39be-867f-1babe24bcc09 | -12.95555 | -54.76655 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96ad539f-ed9a-3cd1-b4f0-5543c778d2ae | -11.42456 | -43.60516 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f0e73d3-1155-3a8c-bcc4-086330383056 | -9.78197 | -48.33173 | 2025-09-09 04:34:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a68a0c44-af3b-3b57-9cd8-7d16525c5fef | -8.19955 | -44.76729 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e253c57b-0af7-30c8-b7a9-046665cdfaa3 | -7.5003 | -49.51046 | 2025-09-09 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96223bbd-9ff6-32b5-a07e-dd83e208d306 | -9.85722 | -47.79976 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7dc3eef-1ade-366f-8148-975388957908 | -8.50176 | -44.64241 | 2025-09-09 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da38c91e-eda6-3892-9a7e-8afae3a8519f | -11.93266 | -50.96436 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c541ab2e-b058-3948-95ae-f646e57e8524 | -11.34336 | -46.56421 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 368ce863-c7ee-3e8c-aed2-6be72ec0530f | -14.35036 | -47.32592 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 985dbe0f-f2d1-372d-8e8a-92709e562ff7 | -11.30656 | -46.49721 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bb545d8-5c16-3284-95fc-ce87a0771418 | -11.21891 | -55.00195 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5c5a182-e8d0-3ebc-84c6-e6ebb60176b2 | -12.84754 | -52.94707 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be5d5d22-d91d-3eee-a42e-e153adb61b62 | -10.89997 | -55.70353 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c5c92629-d4e5-3b4c-8a30-7ddf36011ea5 | -11.29618 | -46.48864 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edef1b2f-9544-34c0-9ca9-9ac5b79112f9 | -8.12366 | -44.87275 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cd2fa19-7831-303b-bf25-38606d3a7640 | -8.42625 | -47.29054 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71d884f7-5564-3d52-af63-9f02af25fbc7 | -13.06934 | -48.08088 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be253375-ab7b-3e15-b8c2-e7d9679280f1 | -7.61235 | -44.6884 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b59866f0-e7d4-31dd-95f8-d20094be4b81 | -10.28251 | -48.80822 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0be2e255-b26f-3a7f-83c1-0c93dc7dda11 | -11.65197 | -46.87232 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f8de1df-c264-33da-ae18-9d7e80dae0f7 | -8.0304 | -44.02649 | 2025-09-09 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1fbfa713-0e66-39b0-a1ef-aed4382e8a46 | -12.4652 | -48.03619 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb8a9f4c-d271-3b86-bfad-64469763cfcf | -12.81445 | -56.51202 | 2025-09-09 04:34:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7dde92b4-f7d6-3c75-9481-58e1f648b6e1 | -11.31968 | -55.12305 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c907b1e3-cd1a-348d-b7c7-b588ab2d727b | -9.50036 | -48.28327 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f863968-73ee-3bbe-b610-0b2d35985216 | -8.04471 | -44.06314 | 2025-09-09 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe025d34-d854-386e-bd3b-c425ac4935bf | -12.19101 | -53.8773 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab0174a5-e47c-3f0e-9973-b7092ed75fa2 | -9.24208 | -57.06742 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 483d9915-7354-3f8b-9cc9-f8a68ec5fdf3 | -10.70371 | -55.38433 | 2025-09-09 04:34:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6113df57-4763-3d51-9179-0eb054046fd1 | -8.37608 | -45.01226 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9772ec0-e3cd-34ad-bea4-66c1c039f627 | -8.09227 | -54.75312 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7866a252-d181-3872-b7d7-996e176b48e7 | -10.58137 | -52.03372 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eec8530-bb6c-3f7e-9279-e59b5bce2f02 | -12.62238 | -56.9687 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aaaf4b3b-f4c0-36e8-b3a5-3e18330249a4 | -14.33933 | -47.32828 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 536e4eef-f741-30d5-ba20-b4fc0546e804 | -11.96073 | -50.98426 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 932e86b5-aac4-3b1b-8256-519db12ca294 | -8.03882 | -48.62297 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d5134de-c3bf-3168-8ff1-8f44207cb209 | -13.04633 | -47.15495 | 2025-09-09 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b9e2554-6a1d-3d2c-9322-b13dac88987b | -11.18817 | -48.40777 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44e3e763-8728-3e90-bd99-60a3bc2acd1a | -11.13719 | -48.36378 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README34.md)
