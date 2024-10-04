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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 718683ec-defc-3d82-a607-c5d641dd4e48 | -17.40979 | -44.93702 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9caa8ac8-2418-388b-8349-2f08ccfb9e6b | -17.4092 | -44.94067 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06554a25-5e44-3085-aafd-9f06ddd10018 | -17.40587 | -44.94009 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d288059-6b2e-34cc-b959-85b859d59af9 | -17.33633 | -44.9283 | 2024-10-04 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab50b46e-de20-34de-bca4-326d6d3fb857 | -16.97447 | -44.76469 | 2024-10-04 04:10:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b238cf2-efb3-3d25-9c1c-5ddc11e0d756 | -16.97388 | -44.76833 | 2024-10-04 04:10:00 | NOAA-21 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65d8c109-15cc-3085-b546-418a3f81e987 | -16.97056 | -44.76775 | 2024-10-04 04:10:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f936391c-16ae-3851-b63b-8b8f52a7d9ae | -16.88155 | -44.64385 | 2024-10-04 04:10:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50dc677a-a595-3dd6-838b-0178119415cc | -16.87824 | -44.64328 | 2024-10-04 04:10:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 344e6f9c-d9ca-3236-aab6-aa068113a18a | -14.19965 | -46.46348 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1fe58a4-ef2c-39c9-80dc-6d48bb161928 | -10.7994 | -45.57697 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b9073e-7352-3733-89aa-613a3718917d | -10.7553 | -45.59879 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00d2f97c-3dfd-305b-a09e-a7c742676e54 | -10.75462 | -45.60284 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 341876d1-cfdf-34e3-944e-f2fa161c51e1 | -10.75238 | -45.59423 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63197665-0c53-3feb-91c6-429745918a9a | -10.7517 | -45.59829 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 081948e8-91e3-3314-b128-69889c83a3a4 | -10.74879 | -45.59374 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5f02e4b-37e9-3328-8e6c-dc3e28e42a3d | -10.64143 | -45.19258 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a128ddc8-317c-3e59-805b-e10599873feb | -10.64077 | -45.19658 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 164e0c67-63e8-30d8-b42b-00c2bf84e364 | -10.64011 | -45.20056 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c477968-1848-3254-aec4-d2c053c683aa | -10.63374 | -45.19535 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eeb92b3-0a66-3e94-8d2f-b73fc131c156 | -10.62825 | -45.20668 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e876c347-3550-3cd7-b56c-b92ecc610912 | -10.62759 | -45.21066 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d50cba4e-2277-3bac-be32-734510dfabe3 | -10.62539 | -45.20208 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e4bff7bf-4368-3c16-a8fe-a4ac6df4df60 | -10.62473 | -45.20606 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b09fffc-9110-3bf6-8255-a8932f45a117 | -10.62407 | -45.21004 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b3a1cc6-9759-3a48-8319-fc2519e9772a | -10.62385 | -45.18956 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c820b7c3-15aa-38e8-a269-e031112c307f | -10.60427 | -45.19855 | 2024-10-04 04:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2013c46-71a9-34eb-9450-ed4d89126975 | -11.52731 | -44.91385 | 2024-10-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84c59d5f-8f8b-3790-acd5-5e6c5ce0f96b | -11.5245 | -44.90943 | 2024-10-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e088067-d49f-35d6-b5d0-8ed835c70e06 | -11.52386 | -44.91327 | 2024-10-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6799af63-b064-3abe-a021-0a89e46cbf46 | -11.14805 | -45.03455 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd6c3ef-ff5a-3cf3-a2ab-5b39fbfd851b | -10.80832 | -45.61185 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5875e785-3ba9-33bf-ba8c-5242e13b2606 | -10.80543 | -45.60711 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 945095f8-c491-3227-95cb-1c07a6cc41d9 | -10.80474 | -45.61125 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a7be4058-11cd-3afd-9a76-fe9683229be7 | -10.80252 | -45.60246 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c897ae1a-c66b-3406-86d1-41de5fdf8ba4 | -10.80185 | -45.60651 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| daaec7a2-452e-3a88-8cb6-0811c2317fda | -10.79894 | -45.60188 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dc69a2b5-7daf-3763-bed6-22426fc5b629 | -10.79827 | -45.60591 | 2024-10-04 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cc60fc3f-bd37-391f-bf6d-417f45d45e84 | -13.19454 | -45.485 | 2024-10-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efa931ea-57d8-32be-a07e-e44e6915b5cd | -13.1712 | -45.43268 | 2024-10-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba14b3e-bec2-3082-897f-b8cdc1f3be40 | -13.17054 | -45.43657 | 2024-10-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ce063f7-10b8-31b9-9ab4-b52a67888314 | -13.16708 | -45.43599 | 2024-10-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cb5d72b-4c3a-319d-b33d-dc195e434030 | -13.16296 | -45.43929 | 2024-10-04 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70f48226-b2d9-32d4-9cf0-a663a641ed5c | -13.15844 | -46.32576 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f96399fc-d60d-3406-89ca-b2495027e2fa | -13.15485 | -46.32502 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62562f64-5fb3-327e-880e-c92471d382f7 | -13.15275 | -46.31559 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0094f8e-a2c1-3b4c-a08e-5c8431a2bf5f | -13.15124 | -46.32445 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9f16b02-7273-36bf-b9b6-a7b5df0bade9 | -13.14987 | -46.31075 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| caa32fb2-bb7c-3b55-a392-bd51a81571e6 | -13.14911 | -46.31519 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 851ba72c-f42d-3015-b656-78c2ff31744f | -13.14701 | -46.30579 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7304d78-3d9b-3646-9345-8c2f88e0dedf | -13.14623 | -46.31031 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b49f7d9e-38fc-34f3-849d-d124e6752078 | -13.14547 | -46.31474 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9c953a11-41cd-3047-b9e1-18e82da02963 | -13.14416 | -46.30077 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 993d9cef-59ef-3edf-bb42-733fcdf3ec68 | -13.14056 | -46.30013 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f286baf6-b059-392c-b42a-f327be858bbd | -13.13621 | -46.3039 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f902814d-253b-32fa-9fe2-0e0e0a7fb54d | -13.13264 | -46.30311 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ab709102-ed9f-30be-a2e3-129d084ba502 | -13.13188 | -46.30754 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acaeaa0a-041e-3013-b0f4-81be1fa31c25 | -13.12755 | -46.31113 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8966986c-81ce-3f0a-b34e-d43743c8349f | -13.124 | -46.31025 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeba23db-0510-31f3-ba20-ff9f932bf50a | -13.12325 | -46.31458 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f7a68c-ddca-33cd-ae4c-6eee896ff5fd | -12.89753 | -45.07 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64eaa35a-1636-3ce9-9586-ffb5f0a4ca34 | -12.89702 | -45.65899 | 2024-10-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcbc74df-0efe-37aa-a7d4-8286cbdecce9 | -12.26808 | -45.96364 | 2024-10-04 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f19f820-0164-339f-a0b1-68262b10a382 | -12.26738 | -45.96783 | 2024-10-04 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1b8863e-38e3-304a-8949-dd4feb983c74 | -14.20321 | -46.46424 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff1d7b32-7ec3-371a-8f80-29d505cbf81a | -14.20248 | -46.46852 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fcdd6c1-10d8-3456-8724-f78bdd11baa9 | -14.20175 | -46.47276 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a3c8152-c139-31ff-acab-352fde7e3d9b | -14.19817 | -46.47208 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a441e02-641e-3a53-b53d-f25fbbf9a6da | -14.19385 | -46.47575 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2e4e2cf-f360-36a7-90c6-73deaf2763a7 | -14.19026 | -46.47516 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce7e52fc-50ce-3768-9756-551112a82c60 | -14.18667 | -46.47452 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10eeb10f-02ba-33a2-b5ab-55157ab58bbd | -14.06321 | -46.5152 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de8e49af-6c1f-3eb0-bc7c-a4460d412d81 | -14.05999 | -46.3489 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10da2b6f-64ff-3692-bac8-6550c3f6edb7 | -14.05642 | -46.34826 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af2dd960-7982-338a-a3c2-a5c167efd1bd | -14.05144 | -46.35603 | 2024-10-04 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9491a8d3-7482-33d8-b5e1-964530f5361b | -14.0346 | -45.46563 | 2024-10-04 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18e67ab9-4bd1-3c59-9ced-ce89f7bd86aa | -14.02106 | -45.48306 | 2024-10-04 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b08b36ee-533b-391d-9a5c-c2a6778d42a7 | -15.76036 | -46.16424 | 2024-10-04 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 701d792f-760e-3f29-b9a4-4c98a7386470 | -17.61716 | -46.98056 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d1e43bc-819c-3f5a-914e-15d66d9d4b90 | -17.61643 | -46.98481 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23f2c714-4b0e-3c44-a328-4ed6057a4400 | -17.61434 | -46.97583 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aeccadf3-b57b-34c5-9bf3-2c5302276844 | -17.61364 | -46.97987 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c027089-8292-311b-9829-b6e46c3adf32 | -17.6129 | -46.98416 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4f9b463c-2715-3fe7-a7de-706ef34a51c4 | -17.61081 | -46.97518 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aaae8edc-1a2a-32d5-a9b2-36485bfe882c | -17.61011 | -46.97924 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62a889e8-1ef7-3904-ad1d-4b82837ed592 | -17.60937 | -46.98354 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b543e5dc-d34d-3521-bba7-7c20f79e1bf4 | -17.6073 | -46.97449 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 536f14f8-d33c-3ab2-818a-3946583b92b1 | -17.60658 | -46.97863 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fc5bf13-277d-3232-8ec7-50cd213dde20 | -17.60657 | -46.9576 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1653bb2e-92fa-35a7-a904-18ac9ca710b3 | -17.60588 | -46.96165 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 949dd044-1656-3cb9-997f-c8af02991919 | -17.60583 | -46.98292 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 924d8266-6402-30e6-9484-11559d843843 | -17.60518 | -46.96566 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10a7b8f3-8b46-3d8f-a2d3-c6567863d1a2 | -17.60378 | -46.97381 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f2e52abc-1da3-35cb-822e-7f910409e447 | -17.60304 | -46.97803 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba153e18-e748-393b-8d54-fe1903a7b3de | -17.60022 | -46.9733 | 2024-10-04 04:10:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8401dfe-1175-3f17-b895-28eddb18fb3b | -17.53535 | -46.738 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf44e14e-32a3-30c3-84de-bfbe2ceac4a1 | -17.53465 | -46.74207 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fff7c091-e102-35b4-9907-8191d2d17b56 | -17.53186 | -46.73735 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7cb7d365-e6d7-3ee6-a2dd-0c699d8e370c | -17.53116 | -46.74142 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4488d7e1-6f07-3593-ace4-0bf2f2961452 | -17.52837 | -46.73669 | 2024-10-04 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README70.md)
