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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d74cb01-5271-3411-ae73-1927c1860319 | -12.66887 | -42.69756 | 2025-10-31 04:08:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 015a3052-bd57-3f1b-91c6-2be2d7e1f98c | -10.54 | -44.78267 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ff5b4921-6013-3b46-8d9a-81d50968b1d8 | -12.22229 | -44.04772 | 2025-10-31 04:08:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e262f765-ca03-3256-beb1-a148ec5cb80e | -13.2422 | -54.35549 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32b0e0c7-ef34-3aa4-be96-11b85c8960bc | -8.16941 | -45.50078 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fa8e763-fedf-37f0-a62e-7e6822a86c6f | -10.49697 | -43.32157 | 2025-10-31 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 264ee228-a2ab-32e5-a9b3-20fd19ced4ff | -14.08389 | -44.16171 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64d7ef7c-8e48-396c-ae8e-3e2a967dc192 | -13.12646 | -44.83125 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a3011e6-39b5-32fa-a4a5-2bcf2f35ac41 | -12.13559 | -47.15005 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67a3c972-4bd7-38f8-bd6a-224c92209539 | -12.84293 | -43.46392 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b4e0373e-7070-30f8-9081-22d26e7820de | -10.92613 | -44.76594 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58ad4d36-d90a-34e6-9cb1-89da105c05e5 | -13.27088 | -47.75746 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2fb0ea6e-f957-32d5-853c-44b765488d5e | -10.81182 | -44.26399 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72a3af43-e85a-3347-8f9e-23cc1a2d36d1 | -11.10395 | -44.72706 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 717cae8e-1932-352b-a7ec-db7c8ada4cd8 | -9.87677 | -44.86628 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9686c8d-fca9-33b9-af29-81baaca0f6ec | -7.66396 | -43.59586 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f01504a4-e728-381c-9c5d-bd93f6f1671a | -11.5037 | -43.2541 | 2025-10-31 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9f2a8b15-fc15-30ed-ad04-026d03bfe1ba | -8.15976 | -45.46741 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6acf676-a480-3d2a-b456-9ecd752985ba | -13.53751 | -47.42703 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c339fdbd-8c03-35d4-91de-4e156005bce4 | -8.85746 | -41.44473 | 2025-10-31 04:08:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 84ffdec0-da4d-3ed5-81b5-c915be7d671c | -13.33978 | -54.28617 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d92129-1729-33f3-8749-47333080be5c | -12.03828 | -43.94688 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea9897c-c2e7-3b07-97f8-3e167dd71ff6 | -8.11493 | -44.48875 | 2025-10-31 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 14dc4163-9f1c-3e65-b0ee-c8e53f1b1f77 | -8.79556 | -42.82375 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4fa2b7b6-95a4-33af-bacd-e3a16bab0180 | -10.03673 | -45.05981 | 2025-10-31 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b9caa2c-2de5-36ad-885b-802c3c8c8a0c | -7.95359 | -46.7192 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcc4733d-7aa8-38d0-81dc-473454d8b4e6 | -7.81082 | -46.39705 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b83164f-c1ac-39c4-8e9b-7c398a344b80 | -7.9205 | -46.79278 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 545130fc-0e46-3e72-8bd9-f45cc9bf1d6b | -10.64006 | -45.24724 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da0cce5f-c0f8-30ca-8163-05d3e9913b82 | -12.51469 | -46.93342 | 2025-10-31 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63be22bd-fcb6-330f-a7c7-04caf0989f8c | -13.53246 | -47.42407 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42446895-d13b-3b94-8916-06c58aad9a5f | -10.88354 | -44.36062 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38aaba80-3082-3258-a1ba-694fc40d6401 | -9.73263 | -48.02264 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09340beb-036e-3e60-9223-5343b26f7c7f | -14.24411 | -44.45318 | 2025-10-31 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ce3ccbd-dcc3-383b-905e-4304e869fdf7 | -7.38365 | -47.62166 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38716f69-0521-30a4-bf9c-b932133363c3 | -10.70845 | -44.48589 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1705bd23-5010-3e3a-be8a-48d974f72558 | -14.38954 | -43.71741 | 2025-10-31 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3acb676f-da32-366c-b85f-1cdc57317d2f | -13.99827 | -44.01821 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e68fe21a-1406-309f-8512-d72f3886780c | -10.89023 | -44.31944 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41dabb22-59d7-3cb7-834d-f73fc0df77f7 | -12.10358 | -47.12891 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f3b6cb1-adc5-34ef-8786-7907217e3632 | -7.11837 | -47.01382 | 2025-10-31 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bccbff9-e43b-3c2d-842a-1804ee3dc5d1 | -12.16993 | -53.63137 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edee7b9e-fb15-3afc-b273-940b02333afb | -8.32901 | -47.93331 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed44aaf4-7ece-3bf1-ba7c-bd35f41bf9a0 | -12.60254 | -43.20301 | 2025-10-31 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798d2e0c-2033-363f-8e9a-a0843189acb1 | -7.87313 | -47.82885 | 2025-10-31 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f20f820-9887-3e5a-a1a2-31c0a5c0e4be | -12.18908 | -47.0365 | 2025-10-31 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 579cd2af-f0e6-36d0-90d0-d75463cd82fd | -10.84572 | -44.9286 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81228a0c-bea4-31d6-ba23-2a82da9d6162 | -13.82095 | -47.06459 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69eb4a82-a946-3b55-bb15-a49b01cc8b54 | -10.53115 | -44.92237 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc276fe7-7304-3a90-aacb-7092fd600459 | -8.5583 | -47.78334 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2c787af-d421-3d69-900f-dc50570a7b9e | -8.08451 | -45.13161 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a068b066-f23b-30f2-bbb4-6fc36870997f | -9.34714 | -46.59701 | 2025-10-31 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d435825e-d822-3369-9dc8-7ab5fd58182d | -9.30398 | -45.84668 | 2025-10-31 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45b114de-e283-39ba-9ccd-7615b74fda9c | -10.74385 | -44.63685 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79e3a2e6-8d13-3bdd-90ee-b3c9fe1dc3da | -8.07244 | -40.77443 | 2025-10-31 04:08:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 35bc3348-ae93-393c-beb4-ca5ec4b9e50b | -8.31684 | -47.92684 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 834f192c-cef7-3ecd-8ed9-3182dc3bab2a | -11.64133 | -44.04152 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d680415-a473-358c-bb8d-d973df74de76 | -13.70043 | -44.19742 | 2025-10-31 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f624f1b-0b65-384e-b374-00d0b552f7d4 | -10.55609 | -45.14256 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c78c3ad0-dfdb-3e77-bb94-f395268fc769 | -9.8577 | -44.85075 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31aa0f4a-7945-33b5-ae9b-ef891b4ddb0d | -13.81722 | -47.0639 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbcec0ac-7694-3c14-b0b9-97f892945b1a | -11.12705 | -45.15669 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 619df219-7207-3226-a0a0-b6941b33d205 | -12.94199 | -47.92932 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dddec1f6-718b-3046-8a3e-dbddb5778f2f | -14.16525 | -44.34624 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dad1314b-b326-3336-b68e-ba34b72364b7 | -10.25145 | -44.55325 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83ecd307-52b9-3abe-b9a7-37cce5d7083a | -13.23622 | -54.35419 | 2025-10-31 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9fd5c935-3539-3664-b9e0-1c4b507b7a07 | -13.93926 | -44.04507 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05fa61f7-c63f-3bce-98e8-af3b1669c651 | -10.63874 | -52.1897 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57d1eccb-1a01-36af-9c23-dcf5bd0f8f06 | -8.31707 | -45.37996 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0674add0-6a72-3e84-b555-08b7c689f017 | -7.30394 | -45.66442 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba8f210f-e575-393c-85c4-c179fd169fe3 | -7.65837 | -43.58726 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dff27d34-8b8a-3318-9500-f62b1a03a7e6 | -12.27639 | -48.0475 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce073c0a-6355-3061-9296-69c29263aa2f | -13.80227 | -47.06126 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94126d71-c4ee-377c-81d8-43235ef7d634 | -10.80969 | -47.58871 | 2025-10-31 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ea04c3a-5b4c-370c-8b41-83ddafc90eb3 | -10.74789 | -44.64897 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54137abe-b4a4-3245-925c-91e54ab955d5 | -11.71686 | -43.91618 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d63f31e-16a9-33aa-8f3d-8389857a7bd6 | -12.82571 | -43.48652 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 869868ed-4d7c-3ddf-8100-d745dbfca566 | -13.66929 | -47.20249 | 2025-10-31 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1617686-03ad-3d56-834e-0d0c791b0cd7 | -12.19117 | -47.00963 | 2025-10-31 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e197a38-7265-30f5-89e9-02c0154aeed3 | -8.72943 | -39.80934 | 2025-10-31 04:08:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7823345f-7b52-3092-bdcd-d6709fe4514c | -9.84733 | -44.86953 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4888ad3a-eb69-37b0-968b-2276d73c84a3 | -8.16419 | -45.50936 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8a493bb-33de-384f-a6a9-25ba7733be6e | -7.65313 | -43.59785 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 39298b6d-33f2-3edc-b937-62e6cf260aa9 | -9.8649 | -44.87249 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1870346c-7955-3244-8e75-5247db5e7267 | -10.74703 | -47.83082 | 2025-10-31 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d392035-cd41-375d-bb72-ae52c84ae6c9 | -11.63737 | -44.04459 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6761160-ea1e-3456-b25c-ab250894d380 | -11.65197 | -43.91277 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23c86747-5fd1-3e30-8224-10ec0b346b67 | -12.10912 | -47.11983 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b4e8197-fc3e-3f79-b4ce-5756b5c90187 | -13.61261 | -43.98273 | 2025-10-31 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94902b66-3454-339a-9c2d-fcb1089f3f45 | -12.934 | -47.92801 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2bc62b04-389e-3429-a6db-81b40eb7ad98 | -7.93534 | -42.23024 | 2025-10-31 04:08:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7758aea-bb48-37c3-a965-57f57fd89a07 | -13.82702 | -47.05836 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37f6941b-58f7-3f99-8118-31424aef515b | -8.79669 | -42.8167 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aeedcb0c-5eb8-3735-8992-585334c9f26c | -12.31104 | -43.1988 | 2025-10-31 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c676c6a1-35cd-3e9c-beac-2f4232f8e661 | -11.56161 | -47.07041 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 561eb854-43c7-3f31-82f8-97028b3cecd7 | -11.63678 | -44.04824 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df43a923-4206-36b4-928c-215153185b81 | -8.17628 | -45.69101 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54c1e6de-498c-306a-ae7e-74f4d6f95e75 | -12.7254 | -43.00626 | 2025-10-31 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c30ea267-2958-3337-b16a-d8e5f85b9b50 | -10.53247 | -45.04502 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 464727fd-3c38-3f79-9497-0a46c094929a | -11.05382 | -44.02356 | 2025-10-31 04:08:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README25.md)
