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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84e4e89e-8064-3ffe-84a4-da5d56b0bb29 | -6.517 | -43.06437 | 2025-09-06 11:57:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f8121896-9cc6-347d-9a77-10ca82c0fd29 | -9.19084 | -46.04232 | 2025-09-06 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b766cb52-7dcd-3547-a531-6075541f7b8b | -7.3055 | -43.73053 | 2025-09-06 11:57:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f66684e1-dad4-3aa2-b28a-3fc2a2af6603 | -11.58624 | -47.73541 | 2025-09-06 11:57:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| da41c13e-a3d1-32ab-9319-310fc69d5f28 | -6.52231 | -42.40881 | 2025-09-06 11:57:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 1af2e3f8-a05c-3183-ba2a-8b09bc60e8ed | -13.03973 | -42.30311 | 2025-09-06 11:57:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| a175178e-f262-309c-a41e-fcfdc3a9a621 | -12.53208 | -42.56549 | 2025-09-06 11:57:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b2154f91-f088-30a5-a59d-80c2eb68db95 | -11.59192 | -47.74318 | 2025-09-06 11:57:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 41727eb7-c1cc-3504-a5f5-7633ad1fe532 | -7.40907 | -44.95914 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 157e9b53-7205-388a-8711-5008d3ed5185 | -10.60838 | -44.33776 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 3736c089-ace5-3ad0-b80d-f4d8194b552a | -7.79947 | -45.42559 | 2025-09-06 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 96b1f249-6ce4-3350-b13e-4fbbb8a39a1d | -6.87055 | -45.54975 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 4df3c440-7d6e-30a8-aedd-3f8680a2ccce | -11.02444 | -45.96585 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 509fbc5a-4062-36ff-bc29-c8c015adf8fe | -8.35626 | -48.28664 | 2025-09-06 11:57:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8daccb4a-3292-3eb3-9ab2-d6a16442c356 | -9.65657 | -35.72212 | 2025-09-06 11:57:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 2af62fa2-f73b-3fd0-9adb-425ba569a1fb | -8.36915 | -48.27417 | 2025-09-06 11:57:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| f6bedcdc-8e90-358a-a4ee-ba0b5c7161a7 | -12.16844 | -42.40473 | 2025-09-06 11:57:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1be893b3-a732-3fb2-befa-2757aca1f7fa | -10.7664 | -47.75473 | 2025-09-06 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 86d3e3ac-852f-341c-b883-93e908bb7180 | -11.00599 | -46.01541 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2d7f8070-0294-3939-88e7-aafc4b745d92 | -7.05003 | -44.34388 | 2025-09-06 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| de47b07f-8bdf-36dc-b142-d6d86c568d1c | -6.87292 | -45.55619 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| dfa61004-f461-3322-893e-c6ae75e63239 | -10.31793 | -46.4297 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 05734cb1-023a-31f1-974a-b3efa3e78089 | -6.49482 | -42.40787 | 2025-09-06 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ae9b3ee9-d6e5-3c49-80d1-351cf8411f4e | -7.85653 | -44.90855 | 2025-09-06 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| a6c738ac-226a-31a8-a5cf-d2b2ec00e56c | -11.23367 | -46.19066 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 9a638091-92e1-317e-a07a-8e0f602b200d | -6.14652 | -45.48352 | 2025-09-06 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 02eabee4-4e40-3bd8-91af-ed9d112feba1 | -8.64054 | -45.73886 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 99828c4f-03a4-3154-9da9-ec06d297d544 | -7.8101 | -45.42696 | 2025-09-06 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 5125662b-8828-381a-9404-3c8b30332554 | -10.33249 | -46.42405 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| bc937d42-a911-351d-a282-5013d56ee383 | -13.02629 | -48.06638 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 11dfa4c6-f6f9-3872-9d35-db14a483a140 | -13.34902 | -42.46523 | 2025-09-06 11:57:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| fa552562-8e9d-3afc-9a65-97cf6b7b82c8 | -8.11029 | -45.31301 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dadda838-9cad-316c-9c05-c50a62b50dbb | -6.22098 | -43.58095 | 2025-09-06 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6b719d92-fd25-35b4-b8c6-41a9ea353af2 | -12.7367 | -45.09824 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 55696a0d-9dbd-3acc-a242-6532823e2a05 | -8.02727 | -44.03688 | 2025-09-06 11:57:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 91dcb018-f2ff-3865-8d1c-d8b262cf05c9 | -8.34688 | -46.94892 | 2025-09-06 11:57:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| f4cebe2b-8a92-35f4-8822-fce0bb029738 | -8.92076 | -45.7865 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b4409b4a-ddac-38b3-b402-302f1ad45a10 | -10.32237 | -46.40109 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 7049222b-e870-3d9b-b3b3-d1a43f6c9875 | -8.11147 | -45.33276 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 32122ad6-9044-356d-bbfc-13b859fead50 | -10.31801 | -46.35738 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| b264a935-eb45-3fd8-b92f-43c20f91fb36 | -12.53078 | -42.57449 | 2025-09-06 11:57:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e490af31-7b22-3640-b575-ec4b8b5600e0 | -10.75881 | -47.75982 | 2025-09-06 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e1377588-42a3-3cc1-be67-35a974fdf2c8 | -8.91006 | -45.78502 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0af1bc86-68f1-3b09-8833-42ac98c62a68 | -13.02899 | -48.05038 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3ccb515a-8ff6-3a2b-8a61-4f5a095a70ce | -11.79788 | -44.27966 | 2025-09-06 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d310fcad-9d1a-3881-8564-d7038c4e9c24 | -6.23659 | -43.27973 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 18bc1c2c-b123-361f-9bab-729726436170 | -11.36339 | -50.2984 | 2025-09-06 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d6440715-c9cc-3abb-a095-54a6d402a3e3 | -13.01772 | -48.07631 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| bb30eeb0-30d1-3fcb-b452-e79245445c5f | -11.02005 | -45.92542 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 776cfca6-4da8-3515-807e-0651d51fa911 | -9.80925 | -46.00163 | 2025-09-06 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 67ebd688-4a16-3265-a7a0-6b1a5eaf2939 | -6.52094 | -42.41806 | 2025-09-06 11:57:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 850acbad-73b5-31c2-aafb-b8c906ec4dc8 | -9.28006 | -40.87363 | 2025-09-06 11:57:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| f3ffb21d-5b1a-3714-838f-6de4a3425d7f | -10.97862 | -45.98469 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d13fc116-932a-3169-b5b4-296ac9518a50 | -8.89281 | -45.75557 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ad23187d-0112-3626-b3e3-b35f3acb1701 | -6.14872 | -45.4694 | 2025-09-06 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8906e36f-70b0-31dd-9032-35b0f5941ad8 | -13.01433 | -48.06514 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| ee0634a0-5a93-3a6e-a09e-b5259398f137 | -9.6841 | -51.103 | 2025-09-06 12:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 75516787-708c-3c0b-b92d-f2d3d9d0ffd8 | -14.4364 | -48.4421 | 2025-09-06 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6214fef0-c891-31fe-8588-41743987f088 | -7.6881 | -50.2991 | 2025-09-06 12:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ff2a9574-c50d-3a7d-ad9f-1fe111cab2d6 | -10.6128 | -44.3284 | 2025-09-06 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 237.3 |
| f8d0b50f-a55d-3d46-9a5f-3fa82b78da3d | -9.6843 | -51.0819 | 2025-09-06 12:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 2eaf3afc-c8f4-3b00-b8dc-d1ecc1671fc1 | -11.0051 | -45.9755 | 2025-09-06 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| cb60ac0d-247d-3049-95dc-866bc6cba14b | -15.7186 | -53.5743 | 2025-09-06 12:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 5b24b3df-bf5d-3252-bb00-be4e00d68c24 | -11.0055 | -45.9527 | 2025-09-06 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c4e03bf0-8423-36ad-b631-8651d4bc9ccb | -10.3137 | -46.4248 | 2025-09-06 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 6f350b58-c6d5-31d7-9ce2-f3fca85f7152 | -10.5937 | -44.331 | 2025-09-06 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 9c8ebd5b-4fcf-3d37-9c65-65034e1547b6 | -9.7029 | -51.1013 | 2025-09-06 12:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b3947ff5-7307-3bb3-89b1-4632abfe0c21 | -20.47523 | -46.20866 | 2025-09-06 12:00:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b30c02a-6bc1-3494-af6b-a97e4997042c | -14.4427 | -48.45689 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 34846e30-afaa-323a-8a7a-aaaa89a406c8 | -18.69118 | -40.65036 | 2025-09-06 12:00:00 | TERRA_M-T | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 1068692d-df98-3921-8eeb-6933ae737234 | -13.91285 | -48.02007 | 2025-09-06 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 495b59ca-e859-355f-ae9e-7e526e4f2d11 | -20.42573 | -42.21034 | 2025-09-06 12:00:00 | TERRA_M-T | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d1b81519-90e7-354b-9d2d-d79d7b2027ab | -16.30762 | -45.69369 | 2025-09-06 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4a419d8b-6ed1-3532-8089-8bc95eb60305 | -13.31871 | -51.62513 | 2025-09-06 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 5d62c92b-73d9-371c-a935-8d631f0baec6 | -14.43362 | -48.43785 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 270accae-84c5-38ca-a5fe-6966a1105b40 | -17.7091 | -44.49214 | 2025-09-06 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 499812d2-9e79-3b14-b88a-a814e03093a0 | -13.72009 | -46.93824 | 2025-09-06 12:00:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 03dffdfb-cb3a-36fa-a28f-d7e2e8cf0e3c | -17.70016 | -44.49065 | 2025-09-06 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e25beb4d-2d03-3c38-94a1-214f60b9817e | -15.72405 | -53.57122 | 2025-09-06 12:00:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0d72750e-8b49-3f55-8f7c-06bc251b4aef | -13.84768 | -46.26907 | 2025-09-06 12:00:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9d358720-ed63-3812-9867-36c6873d2e57 | -19.9543 | -46.91432 | 2025-09-06 12:00:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dad8b4ef-77ea-3897-bdf3-955bb0058027 | -15.0728 | -50.09476 | 2025-09-06 12:00:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2cee2443-b566-38a9-b9d2-27cc5bd49668 | -20.39481 | -42.37168 | 2025-09-06 12:00:00 | TERRA_M-T | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8a6cd480-0594-3d6b-9b2f-f08725b93d0d | -18.77747 | -40.69218 | 2025-09-06 12:00:00 | TERRA_M-T | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 8ac3d481-0e31-3211-90e3-f92d73d2ccbe | -15.14278 | -43.75804 | 2025-09-06 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c69524b3-2946-3ee9-b26d-d93d9b5c2ec4 | -18.67593 | -44.3139 | 2025-09-06 12:00:00 | TERRA_M-T | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef56b560-1fa0-3a95-a64e-ae842a7e133e | -16.45812 | -45.25591 | 2025-09-06 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cfb567fa-0212-3209-a730-1a9de330c3d6 | -15.21005 | -43.80325 | 2025-09-06 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5a8c5803-0e19-394c-8a59-e45cf16940e8 | -14.83137 | -48.1885 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 7e75d5c0-750e-3b73-82d7-b0150735994d | -18.76087 | -44.86307 | 2025-09-06 12:00:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bdb34aa3-685e-3a35-8bb2-a982aa41131c | -18.30798 | -43.93528 | 2025-09-06 12:00:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d4489bab-bce2-3618-b80d-39ae3624f6eb | -20.47361 | -46.21904 | 2025-09-06 12:00:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01762e2b-e82c-3789-a7e5-f69e9ab0879b | -20.21022 | -41.37952 | 2025-09-06 12:00:00 | TERRA_M-T | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 24b78aba-ea5c-3d77-95c1-1992426fbb8e | -20.91465 | -42.13123 | 2025-09-06 12:00:00 | TERRA_M-T | TOMBOS | MINAS GERAIS | Brasil | 3169208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 945cb77e-7aa9-3797-bbe5-2fe4e556a0eb | -20.44949 | -45.53503 | 2025-09-06 12:00:00 | TERRA_M-T | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36371ead-1e0b-3097-8cab-b46540c65176 | -14.43614 | -48.46273 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 130.4 |
| cde7f352-7192-3635-bc90-e1db9d6326cd | -18.02602 | -47.08509 | 2025-09-06 12:00:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2e66ba13-b33a-3e01-80ea-17116f42a105 | -16.32744 | -47.72977 | 2025-09-06 12:00:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cbbc94c3-46e6-3917-a402-c3a5051292d2 | -16.09561 | -47.86299 | 2025-09-06 12:00:00 | TERRA_M-T | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 333a5010-a1f8-37db-8aef-01ca414e463a | -14.57171 | -48.01271 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README90.md)
