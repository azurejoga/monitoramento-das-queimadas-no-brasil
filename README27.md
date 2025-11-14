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
| 47e185f5-1394-3379-a46d-f8e88605443c | -2.63902 | -47.30235 | 2025-11-14 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f653341-b088-3a94-ad42-d2f7ab692a0a | -3.81779 | -44.24347 | 2025-11-14 04:23:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7819f2ea-09fa-39cc-b156-1f3af0c67516 | -4.04004 | -46.98525 | 2025-11-14 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b1d2fa6-0815-3cea-bd06-d8a6854ad447 | -2.63819 | -44.8767 | 2025-11-14 04:23:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eb0829f-6159-3a42-9365-62eb9ddbaff3 | -10.33525 | -48.06984 | 2025-11-14 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b9ef041-de24-31ec-abcc-117acc0b997f | -2.94591 | -49.36389 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c066d56-74e4-3c88-89fb-0fbd4de8f9d8 | -1.90166 | -47.15749 | 2025-11-14 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf1c6f61-2b09-36c9-9382-73498d68bf6e | -10.73046 | -45.0839 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7b32d08-d2e8-3601-a05e-bc205cbe1d15 | -9.05226 | -40.65843 | 2025-11-14 04:23:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef9d2211-1925-3d43-9a50-8e0833e26229 | -7.85153 | -44.30196 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d1dd7b-fd2b-33ae-9575-95afd79d45bb | -7.46742 | -42.57872 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| edc2ff93-d1ef-3332-8f5f-8fdbdedc6ef1 | -4.28705 | -41.7715 | 2025-11-14 04:23:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 109fee67-293a-36b4-99c2-46571461e72c | -8.68946 | -44.39339 | 2025-11-14 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dce614c-6d27-3bae-aad5-dde23b48d6f2 | -10.34766 | -47.82072 | 2025-11-14 04:23:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cc45c14-98a5-3189-b320-b86831d986c4 | -7.15428 | -44.9735 | 2025-11-14 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 856f7816-97aa-3c85-b07d-c44506e6a204 | -10.63068 | -45.00655 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56be2e6c-1b9c-35a1-8e33-af2efe87fd89 | -7.15483 | -44.97003 | 2025-11-14 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6efef2a6-e9a6-399e-a7f6-99af3b2f1b8c | -7.50982 | -43.01246 | 2025-11-14 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 028c3746-d5b7-3b36-8fbd-763d94dbe285 | -7.11353 | -45.20916 | 2025-11-14 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ec8aeac-80ce-31e6-bd8e-a50bad8f963a | -10.75977 | -45.0195 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 98edd68a-38c0-36c3-bbcc-26069ecdef2b | -9.24995 | -45.20036 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc7fe351-aa38-3b42-8182-1bb2635163c0 | -3.20985 | -50.19563 | 2025-11-14 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e3a605c-4350-31b4-a423-53e84967bc34 | -1.34031 | -54.60844 | 2025-11-14 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edf8274d-7d15-3860-bbd3-dc817d32e866 | -7.564 | -47.8177 | 2025-11-14 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de4d3c4b-ce05-33ad-9d97-a73a35cfb15b | -7.94245 | -44.32697 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb7cb35a-eb69-34f9-80d9-ceec3206116a | -7.85596 | -44.29546 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7363f97c-0ec7-3ccf-bf5f-467776f60631 | -3.11344 | -50.29135 | 2025-11-14 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8348f0ec-d641-3e16-965f-1f7ba5b600fb | -7.35592 | -43.35554 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 769cc446-9ab2-37f8-a593-2b2a09630c16 | -4.28804 | -41.81121 | 2025-11-14 04:23:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 940c2c07-3eaa-37a6-a32f-d52c1f78913c | -4.52167 | -45.60577 | 2025-11-14 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83aec3d5-135b-3810-985d-76a64c7f994e | -7.28605 | -45.46531 | 2025-11-14 04:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8edf651-703e-3c7a-8bf0-8870d8346d5c | -7.63667 | -46.15497 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8a00eb3-21de-37f1-bab0-2617116badd2 | -2.63838 | -45.7565 | 2025-11-14 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97127ed9-08a8-3e7c-8abb-904904edbc73 | -4.30297 | -46.26889 | 2025-11-14 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af27fea-0e14-39ee-b34b-0bfd7cc36add | -4.63238 | -43.27826 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3ef2b0e-ee5d-3d01-a68f-52fd1e5745a1 | -7.78007 | -48.05588 | 2025-11-14 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f51312f8-487a-3d2e-9591-c8ff15efaff4 | -3.656 | -45.44817 | 2025-11-14 04:23:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6abaa665-6fec-3783-9b45-de70c1812c61 | -2.23717 | -46.07702 | 2025-11-14 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2b99794-76c1-3964-8b92-180391039789 | -9.34666 | -46.58828 | 2025-11-14 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fae40e81-709d-37d6-9d18-427d778406a7 | -1.10692 | -52.59277 | 2025-11-14 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 531d3a1a-eb58-395b-8c1a-21668108d200 | -7.78293 | -43.79424 | 2025-11-14 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee34829e-c0cf-36a3-9b0e-46f61468b869 | -3.47727 | -45.64572 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca0c3d54-a485-3ac4-ba82-dce3a7b5fd27 | -7.15815 | -44.97055 | 2025-11-14 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5739c0ec-1be4-3c88-94c9-6db0c01d6699 | -2.88106 | -45.28653 | 2025-11-14 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8047706d-aa23-321d-b733-cf76f9dd963c | -3.80447 | -45.03532 | 2025-11-14 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d7ed9ed-9f46-3bf8-9672-bdc17be372b5 | -2.82388 | -46.62157 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd83870-b88d-30ae-bb79-1782599ebfbf | -7.46103 | -42.57377 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7512afd-bc3a-3b4a-a4a4-290a8d9e6155 | -7.9299 | -44.32509 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eb27ced-1857-3147-a7ad-9bf62cecc304 | -2.51872 | -47.80865 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2344bac0-9299-36b4-9d74-24cfad9ebd8d | -10.44816 | -47.33694 | 2025-11-14 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2504fd60-79d7-3665-a052-66a38ebb63b7 | -6.85662 | -46.7494 | 2025-11-14 04:23:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a6b9eb-cd55-32f6-a993-42b7fa32d923 | -7.45055 | -42.57216 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8d53c73e-1079-3bc9-9f70-5d648b8069f4 | -2.83659 | -45.47922 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 06ad6408-918e-3cf0-8aa0-6c2237e8f2b5 | -4.13227 | -43.01269 | 2025-11-14 04:23:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2a0a734-3014-3384-9b9d-b723dc9dbe73 | -4.60691 | -43.29611 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f4fcca3-1ea2-3522-85ee-cd8e0376cadb | -4.52623 | -44.62408 | 2025-11-14 04:23:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8112cf22-d248-3695-a6c3-79b6c44d9848 | -7.4686 | -42.57095 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6813c12e-af49-3e8d-b5b4-b4e3627073db | -4.61035 | -43.38307 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28b28b5-5462-323e-96be-64702a03d460 | -7.92715 | -44.34262 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f83c77-ef4f-35a3-9293-f4373d9c13e5 | -9.31495 | -47.83912 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 84901748-0091-3038-a4d6-276f3b689fc5 | -8.94559 | -49.8148 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0e01feb-78ef-35f1-bf33-6e1947eb12eb | -3.45064 | -44.53264 | 2025-11-14 04:23:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9985615-b4b1-3774-97c1-20156b70782e | -3.95372 | -47.50138 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b2ae4d4-44b5-3564-b942-9df8098cd4ad | -2.63165 | -47.30118 | 2025-11-14 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8b4e4d9c-3ab8-363c-866e-2ff300ce4aed | -8.94084 | -49.8191 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93040da9-1b6a-3a0c-a06b-18662ceedbd9 | -7.39268 | -43.32016 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a38f8157-0092-3610-b025-917399110791 | -2.94236 | -49.35944 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 330f3f30-b9e5-3c27-85a3-abf3f9f57e76 | -10.55347 | -44.83132 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff61160d-ad82-331a-9d72-dfdfb001a3b2 | -9.31909 | -47.83582 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d615d6f-d7da-3c83-a115-8c760f67f313 | -4.41096 | -41.4808 | 2025-11-14 04:23:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61b41ae0-4bf8-32c5-a719-4a0842e843f9 | -7.84596 | -44.29389 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e50b0fb-7903-3a79-82cd-dbf835daa9ba | -4.01315 | -48.81055 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ac1bc11-7f2e-36fa-80a9-038f0eaaad85 | -4.25896 | -44.59986 | 2025-11-14 04:23:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4857bafd-4b24-3570-9ebf-efb4f1e44a41 | -7.53725 | -46.58026 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b99f3f5e-0085-31af-8ba5-d6f5d165b1a1 | -3.63149 | -49.10957 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93a95a39-69d9-39e5-92c9-b9f66303f043 | -3.21495 | -50.19207 | 2025-11-14 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80de6226-ce49-399e-b493-f76aa9b46f1a | -8.49947 | -39.61658 | 2025-11-14 04:23:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67cd2722-05c1-3aff-882b-3ddbf08d8bbd | -2.83999 | -45.47976 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b40f8d06-e18d-359e-ab70-732c283da23b | -2.88049 | -45.29012 | 2025-11-14 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9236d283-8668-3568-a6c7-f7b433a77c59 | -3.98733 | -47.99817 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cf2b81f-4765-3ad7-b20d-131a57e60a21 | -2.38019 | -48.68013 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6bd8a094-e66a-3f6d-9fb5-52f8d9cf25de | -5.02663 | -40.60355 | 2025-11-14 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9413fd7d-846b-32e6-9fc8-9c6706073a33 | -6.6897 | -47.79986 | 2025-11-14 04:23:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98d75bd4-f8eb-343b-b41d-cf170e91e685 | -3.43008 | -50.16912 | 2025-11-14 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1e2530a-204c-30bc-9353-a7c5e81a7328 | -2.88444 | -45.28707 | 2025-11-14 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c404aad-61b5-389f-8346-42cff4263842 | -10.92093 | -44.58872 | 2025-11-14 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a81c288b-2ce1-32ae-8698-33a514222318 | -5.39802 | -37.862 | 2025-11-14 04:23:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 558718b5-cdd9-3713-8dec-e79f1b9738db | -7.35085 | -43.36591 | 2025-11-14 04:23:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f3a6598-eb30-3cca-955c-89ef3391912a | -2.90219 | -48.0615 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 380d43b6-ce36-3c81-bae7-b37b5f27752a | -10.75052 | -44.55848 | 2025-11-14 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e5440f8-9a9b-3679-b695-50451855b9ab | -2.88387 | -45.29065 | 2025-11-14 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32f1026a-de96-35bc-989b-3d649209eb12 | -7.02229 | -46.43807 | 2025-11-14 04:23:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03dab48e-c636-3c23-8095-e1b3d57a50b7 | -3.30133 | -50.10293 | 2025-11-14 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bb82362-3835-3584-b9d1-f765c7b1f20e | -7.66358 | -45.87869 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4262c410-e580-3450-8091-bcf2bd244c04 | -2.28125 | -53.64357 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5adb15a0-7db8-3b24-99d4-aee8c3a9592e | -3.74431 | -44.27791 | 2025-11-14 04:23:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 332fb00a-91d6-3f75-903b-52b932c8781e | -3.73516 | -39.59599 | 2025-11-14 04:23:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91795d90-fcbd-39ad-b481-adee15a87e57 | -3.99441 | -43.22659 | 2025-11-14 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca35201b-3474-3f17-9791-b1f3c929baea | -5.16399 | -37.57907 | 2025-11-14 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 13f8b8f6-f295-3733-a2ab-9a1ab45019f8 | -3.40096 | -44.71714 | 2025-11-14 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
