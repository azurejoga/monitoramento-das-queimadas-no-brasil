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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 573decea-82a7-385b-84e2-716258a5caa1 | -12.97776 | -43.46478 | 2024-10-28 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9393c0e8-73cf-3c83-8c34-cac0cb440d2b | -12.89981 | -44.60768 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 85aaa558-a71a-3ae3-9b10-c66d0ab4c6fa | -12.89921 | -44.61139 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0f72475-2da2-3894-8515-8bbadd1b10e3 | -12.89644 | -44.60711 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fbaada9c-b657-38a8-aba6-ba48692b5c53 | -12.89583 | -44.61082 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7244874-65e6-364d-85ee-fdf881b710cf | -12.89523 | -44.61453 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 252aa7fa-41cb-306f-997c-7412e6a5879d | -12.89306 | -44.60654 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27100691-b62f-347f-a52f-11f670745899 | -12.89246 | -44.61025 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2eaadfa-f75a-312e-9d5f-7dd574c27e63 | -12.89185 | -44.61396 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f66e541-c173-31e4-8afe-2ad72806b654 | -12.88968 | -44.60597 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcd1c300-28a4-36b9-9167-04bff317ebf9 | -12.88908 | -44.60968 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd460fec-febc-382a-8a6a-ab97b108899b | -12.88847 | -44.61339 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295ccb97-303f-3fb9-92ad-22f56b611350 | -12.8857 | -44.60911 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3754c816-450b-31e2-ae11-7d4bedaef0fd | -12.8851 | -44.61282 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 601ebff3-aef9-3a84-9572-b73d3b0c651d | -12.88232 | -44.60854 | 2024-10-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7899f3d3-925e-32b8-a75c-400f27576e1a | -12.69619 | -44.47901 | 2024-10-28 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cdac49e-f06b-36f4-9b30-35c9df05550c | -12.68515 | -43.89383 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f76effe-2944-3693-8767-6ab21d5d7ded | -12.68458 | -43.89741 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4354dc1-a89a-3d2b-9748-87509579f762 | -12.49752 | -43.87341 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 249fb2ef-a5f9-305b-bcf1-b42dae8b608f | -12.49419 | -43.87286 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28ca5c97-08fd-3344-8740-168833298942 | -12.46407 | -43.78801 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f116e91-d715-3080-8b4d-309561fc9cad | -12.4475 | -44.4147 | 2024-10-28 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f9f217d0-2b90-3ba3-b2ef-cca1b8bb3a28 | -12.42932 | -43.7493 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23781488-a408-3766-acba-7c00d2300320 | -12.35922 | -43.76301 | 2024-10-28 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 894a907e-8339-3fba-8fba-a014ab811847 | -12.30924 | -44.46814 | 2024-10-28 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9348f3f8-e549-3b79-bdf9-90b5d4c1d751 | -12.30586 | -44.46758 | 2024-10-28 04:08:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6147261e-636b-354d-9dfa-87a7a98f6345 | -14.23259 | -44.13988 | 2024-10-28 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e523540-b1af-3ac5-8bf5-155f95514313 | -14.19719 | -43.72401 | 2024-10-28 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7724773f-93b5-3ea5-a854-936a44d476d7 | -14.11398 | -44.03187 | 2024-10-28 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5b6aeb6-f90d-3a87-a3f1-3fe79599d4ae | -14.06618 | -43.99126 | 2024-10-28 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b9fb99d-819f-3e19-9f19-25d36b213995 | -14.0624 | -44.4147 | 2024-10-28 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1cf7fd9-81bc-3f1f-ba68-5664d4dc992e | -10.82179 | -44.95071 | 2024-10-28 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 709e4fb8-85de-3a78-b098-a46e65240e56 | -10.81832 | -44.95012 | 2024-10-28 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca488dd6-17e6-3044-8446-4c2656fe9186 | -10.49164 | -45.32319 | 2024-10-28 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7678f993-78a6-30ac-b4f6-4b2b2c3fd307 | -10.89888 | -44.6123 | 2024-10-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cc8a80a-2c1c-3033-9b1e-0793d324f52e | -10.89545 | -44.61173 | 2024-10-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 597d9b4c-b78f-3181-8312-d0c1f710b9de | -10.87582 | -44.53851 | 2024-10-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 892c1845-cec0-3136-9dc2-0bd34c2a31be | -10.8752 | -44.54229 | 2024-10-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 884bdc8b-8291-3429-90a9-9c539147cffc | -10.8724 | -44.53793 | 2024-10-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed8f1265-5fc0-300c-bed4-ba5f4f69c58f | -11.95483 | -45.48772 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 640408d7-b643-3cbd-b8af-b63ebb86d7b5 | -11.95132 | -45.48709 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1cde0c2-76a4-3738-bfd2-1b5fbf6113cb | -11.94463 | -45.52716 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e177cf73-ba00-32f7-8a22-05eb9cdc6d55 | -11.94446 | -45.50647 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31490160-2034-32e0-8e7d-a714bf1837ec | -11.94028 | -45.50987 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6d8a1fb-8bc2-3c34-82c9-588a5e55032c | -11.93759 | -45.52595 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d465e0b3-8576-3ea4-9a2b-0ae2f09528a9 | -11.93692 | -45.52998 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 279ad21e-19b0-356a-8737-91032e3e8c49 | -11.62593 | -44.97459 | 2024-10-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8597f13c-7608-3ee6-8f20-2b624bb9c0c3 | -11.62374 | -44.96631 | 2024-10-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cc8f3d2-68c6-3d96-b15f-ecac236e24a0 | -11.6231 | -44.97018 | 2024-10-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ea4f598-3837-3fec-afb6-4dfb079bb3ea | -11.42475 | -45.14422 | 2024-10-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f24446dd-5733-3037-bc7d-35b65be6caee | -11.42192 | -45.13971 | 2024-10-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fca7d72-a7a3-3bfb-b9c5-29feb5a7908e | -11.27925 | -45.09774 | 2024-10-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e943f89-5b09-3d8f-bc70-059f6e780c4b | -11.27576 | -45.09716 | 2024-10-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 506031c1-7160-3818-aca1-5b1f7cae3c62 | -11.12893 | -45.28468 | 2024-10-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e128dda-4581-3ebd-af21-e1b1c96ab97f | -15.157 | -46.12303 | 2024-10-28 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a52604-856e-375c-9caa-2c75e2aa11d8 | -15.1535 | -46.12243 | 2024-10-28 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c92c9e5d-ec30-3004-b9d9-5a545e64c367 | -15.51947 | -46.65945 | 2024-10-28 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c60257dc-6305-3986-9298-377bc7f58a62 | -15.51804 | -46.66768 | 2024-10-28 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41bcd8e7-1fc0-338c-b65e-d3c59632af76 | -11.99696 | -47.16411 | 2024-10-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c4e6b9d-fecc-318c-a7e7-0be066fef0e7 | -12.66766 | -46.5811 | 2024-10-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 369cdeeb-ac1e-35e2-ab3d-cc778fdeed12 | -12.66324 | -46.58488 | 2024-10-28 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5525e80-c4b0-359e-85ea-85f423f54f66 | -10.53676 | -48.70296 | 2024-10-28 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad2c48f0-c708-3c5f-8716-dacee5151106 | -10.05354 | -48.0653 | 2024-10-28 04:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 492701c7-4eac-31d0-9a29-03d4ff15a03a | -11.58657 | -48.75978 | 2024-10-28 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 544dc5f9-43b6-3e33-b62c-65c6c7ff56b7 | -13.86041 | -48.63605 | 2024-10-28 04:08:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| daabf82e-18f3-3b4b-8845-df9299dce76a | -13.85997 | -48.6344 | 2024-10-28 04:08:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe19a7ad-3728-3ee3-aa0a-bc64d79ff2a4 | -10.71006 | -49.66441 | 2024-10-28 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58c4ecd6-cdc8-347c-9b5e-5568ee7cafec | -12.5999 | -52.45687 | 2024-10-28 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c85244ee-6246-3f0f-9a60-a484e5d6bcef | -25.19143 | -49.32778 | 2024-10-28 04:10:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 84162173-f901-3916-992b-7cd552404e8f | -22.53889 | -48.81288 | 2024-10-28 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eea9fe4a-ecaa-3a75-92c5-a20b3c92038b | -17.79179 | -50.80482 | 2024-10-28 04:10:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9346092-b141-37a2-8823-d44f0584f969 | -28.67982 | -49.11128 | 2024-10-28 04:12:00 | NOAA-20 | SANGÃO | SANTA CATARINA | Brasil | 4215455 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ae89dc4-d4b6-3f95-ad48-000eb7c7f927 | -28.63443 | -49.45431 | 2024-10-28 04:12:00 | NOAA-20 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 312522ec-3a3a-3c31-b791-f39685500d21 | -28.58601 | -49.44385 | 2024-10-28 04:12:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a2d65d8-7ecd-3291-8f06-a699bb8dd38d | -29.87201 | -51.1582 | 2024-10-28 04:12:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 93af59cc-1efb-3064-b02d-37de89f22d93 | -29.81218 | -51.17664 | 2024-10-28 04:12:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 170c12be-305e-3a3c-b1cc-1991ea3a7223 | -29.77101 | -51.41516 | 2024-10-28 04:12:00 | NOAA-20 | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| 38ab234a-b99a-3ee2-8b9d-7f592ff59edb | -1.1836 | -53.4956 | 2024-10-28 04:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 3e39d528-f4dd-3f59-a8f8-9edc520c68ce | -1.9763 | -52.0804 | 2024-10-28 04:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f05d2161-5f63-35b0-9662-ed824964919f | -2.2662 | -53.7825 | 2024-10-28 04:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 6083b970-d012-3fe3-a32e-5af237070896 | -2.2846 | -53.7822 | 2024-10-28 04:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 283b81ab-98da-39d9-8e92-b2a4afc116dd | -2.6399 | -51.7374 | 2024-10-28 04:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2dace339-0d29-32b2-a3c1-f4ba1d1d696a | -2.833 | -49.2413 | 2024-10-28 04:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 060d0fe8-f022-3629-8672-8a0a651ea224 | -2.8699 | -49.2615 | 2024-10-28 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| f6fc8ec6-6262-38ac-8286-afbbeb929dea | -2.87 | -49.2402 | 2024-10-28 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 94ea26e2-6514-38ff-9384-d35805abfeab | -2.8884 | -49.2609 | 2024-10-28 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| b2d83c69-f189-39db-8195-e7f27d4e6718 | -2.8885 | -49.2397 | 2024-10-28 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| f0c85d9f-0ab8-3269-aa75-3b6fb1b9c129 | -3.0317 | -50.4176 | 2024-10-28 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 95a6ce65-3639-3024-b368-46f7cfde4e9c | -3.0501 | -50.4171 | 2024-10-28 04:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7a1782ca-d3d3-30c7-aeb3-1ca1884d7d6f | -3.497 | -45.7971 | 2024-10-28 04:15:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 255da325-5e1f-33bc-8b78-6d6b665ce452 | -3.5154 | -45.8187 | 2024-10-28 04:15:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| adfa0db4-4d49-3a64-b82d-671609647985 | -3.5155 | -45.7964 | 2024-10-28 04:15:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 02e737ab-d11e-3396-a2b8-709ddb26d5eb | -4.12 | -47.3388 | 2024-10-28 04:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b19b206c-c167-319a-a7b7-3af99f44039e | -4.1201 | -47.3169 | 2024-10-28 04:15:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ea9be180-d55d-38e6-a7fe-3881a57dcebb | -1.1836 | -53.4956 | 2024-10-28 04:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| da124196-2b40-3e32-977d-a0f271b7d0c0 | -1.9763 | -52.0804 | 2024-10-28 04:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 763f9e42-790f-3d05-9b1c-f365007d9458 | -2.2662 | -53.7825 | 2024-10-28 04:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0b675eec-cb28-3a6c-af58-0020835f9ef7 | -2.2846 | -53.7822 | 2024-10-28 04:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 0f9c6092-c68c-3e27-91ce-ba35c5785aad | -2.4104 | -48.5479 | 2024-10-28 04:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3219d3f6-4f92-3974-8016-e52310c1875c | -2.6399 | -51.7374 | 2024-10-28 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |


[Clique aqui para ver as próximas entradas](README46.md)
