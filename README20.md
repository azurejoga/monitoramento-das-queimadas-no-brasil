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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f02410c3-be2a-31d2-aeb5-1425a6e51d06 | -13.77983 | -47.88529 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b71dc41-80c3-332e-b800-6817776369f7 | -11.99538 | -47.90008 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ce1d6d0-1a1a-3542-aff6-329499c46094 | -13.61713 | -48.08017 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 556a833e-1fd7-3a99-826e-b043058dde5d | -14.12245 | -40.67565 | 2025-09-28 03:38:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca0bf0a0-4381-3f8d-858c-6d71d14f2149 | -13.62466 | -47.31757 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae97cde9-88a3-309d-b07d-175b0364e493 | -13.51938 | -47.39589 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf94f6fa-70be-3a1a-b6a2-ca01dea06f5d | -10.53913 | -43.62366 | 2025-09-28 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cfc52d80-ba15-3753-9f2f-ed4ec418e539 | -15.33084 | -47.89911 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69460eb6-0a7a-3301-977c-5a1a9b3e7476 | -12.93607 | -45.12254 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 79528854-e90a-3de4-9e01-ff6faaaa10c1 | -12.69425 | -45.4711 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4a6373e-1b56-3346-bb2f-80f4b7f43e77 | -15.03034 | -47.14831 | 2025-09-28 03:38:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83f02388-a6eb-3957-a34c-cda20a219684 | -12.42142 | -44.10944 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f092ac5c-cdfb-3a87-9c6b-1855fec7225e | -13.626 | -47.32059 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1425f868-1eb3-3e35-9481-097a2c7d8561 | -14.58431 | -48.26308 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7dd6c0d8-98e5-3d8d-a51d-cd5c33e470c1 | -15.53666 | -47.90979 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dad652e2-a31c-30f7-92fe-5248ae97a879 | -12.89606 | -45.18011 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57dd09e7-6e75-3925-b203-5ab99db577da | -13.6396 | -48.0701 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a5211c3-d4ac-3847-9a72-f41630ffe9f9 | -10.75363 | -45.39162 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 823e2450-08f7-357f-8956-f5fd7982b836 | -13.7912 | -47.92653 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 83d0f9e8-54c0-36b7-a4f2-f1efa50b9e27 | -11.3758 | -44.96608 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e55451ec-cb45-3f14-8c6c-fd7dcf94ca27 | -12.42097 | -44.1165 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a7883f5-bf94-34a0-a808-b440c035e83d | -13.54081 | -43.499 | 2025-09-28 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4faf282e-94f0-36f5-b8b1-930cb902194a | -11.71104 | -44.42948 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f9f0f5c-a8e3-370a-b0d8-4f81c200e950 | -14.73391 | -43.94299 | 2025-09-28 03:38:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a9b346a-a5f1-3d8b-a84a-f7526051f880 | -10.90665 | -45.75441 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 99c2d3a0-caa1-31ec-a2fc-11dbe97ce432 | -15.29353 | -46.43391 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73c0a355-5b97-34be-b0fa-94e7e6051aa2 | -12.90824 | -45.14767 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0971aa8-0299-38fb-b64c-8ad2386d7475 | -11.43712 | -44.96932 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6fb9c62-27ab-3dd6-be19-70caadc31bea | -14.33471 | -44.50106 | 2025-09-28 03:38:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 119ad16c-f460-3d42-a99d-edaae8e3c43d | -12.99316 | -49.44005 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1c8c805-e016-36e4-ae99-6fbab8b96c84 | -12.01916 | -47.91808 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f7bcae5-39e9-3eba-b6f1-1bae9437113e | -10.41712 | -46.15392 | 2025-09-28 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35d018af-3158-3024-9153-dc889f6123f3 | -11.36994 | -45.02732 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0188dd30-e864-343b-a67e-a3e551b69d14 | -9.44937 | -47.61253 | 2025-09-28 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9824295d-b0fd-30b1-834b-7a5dd7fc075e | -9.04981 | -45.51615 | 2025-09-28 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df067681-76f2-3ab1-8e84-35a506da3c2f | -14.81777 | -45.45745 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d91e3a13-64f0-3028-8cde-180f80c40afe | -12.92731 | -45.16699 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d223397c-7741-3ba5-93db-a802577e5c4c | -10.91331 | -45.73788 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82ce72bb-410e-3d8c-9663-90a3ee108a1a | -13.59952 | -47.29208 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d0d8192-f88c-39a3-8313-97aa3c1cb54f | -13.43378 | -46.51653 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1094100a-1ec7-3856-b5fa-92c1b59f1aa7 | -9.12181 | -46.67277 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 009e8f97-d812-376a-9b25-1c45eb593530 | -15.54285 | -47.91119 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c102409-9684-3949-8e17-ace379980ef2 | -11.36129 | -44.95097 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d43d2828-1a8d-3a3e-a1ab-525e3ba3da15 | -10.42234 | -46.15963 | 2025-09-28 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 622b20c2-f5d1-3357-a752-a64ee2f8202b | -11.78768 | -44.86659 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37a92c54-86f9-351a-9c68-b6e411d8294f | -11.99103 | -47.04299 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 453f41e5-f463-3978-89c1-904e09f64734 | -13.52472 | -47.40148 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb37594e-14f8-33f2-8790-338eeaac3185 | -12.41702 | -44.10916 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c362999-5718-3993-b5c7-2dd4a9d85268 | -12.98385 | -49.44875 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02e9b390-d722-3998-a304-1c616a520f51 | -12.01549 | -47.91538 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35f779ee-c0e7-3461-96f1-9647112f8b82 | -9.45003 | -47.61699 | 2025-09-28 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edec8d17-a641-3e88-89dc-f069c24574f5 | -11.42937 | -44.91989 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfdb8317-9a2c-3f27-803a-4e50945d080d | -15.31822 | -47.89718 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8d96bdc-cb96-35f1-930f-4e676d7d2c35 | -14.5414 | -48.39983 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ebf211c-76cc-3788-83c6-2f423c796d1f | -14.79172 | -45.64269 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a19b4da1-6139-3ee1-8b7f-177a64cb20b8 | -15.15034 | -46.42766 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6bd5a2b-af26-3026-b5e4-2665440ae002 | -15.27817 | -46.42174 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b8fb8fe-5ca0-33ae-bf3e-510f6c21c50f | -11.60828 | -44.41316 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68962ae5-83a1-3b84-83fe-6c12cf3edd15 | -11.79718 | -44.90635 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7f1037-9b3e-36e6-8518-d06055deae46 | -11.98566 | -47.88085 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07ea89f3-15b2-3f79-92b6-63942fc768c4 | -9.21632 | -46.77484 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0f23b078-a78e-32af-9f17-92bc21b2d490 | -11.35889 | -44.96354 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29485d3d-56a9-37f8-b706-efb631d45052 | -12.42081 | -44.11269 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d6ccd7a-88a9-3ced-8a65-f476358b0373 | -16.40441 | -43.71925 | 2025-09-28 03:38:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7389b8e-ecf9-3589-8f77-18ff58974ce3 | -11.71361 | -44.42981 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d992cc66-14f3-3d6e-8d2f-a5ed775583c2 | -10.91683 | -45.7334 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e698c4b-2c3d-3ceb-8f49-4723c9be7a11 | -11.72238 | -44.41343 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46e34351-c0f9-3b0e-b586-2ee7839f5ac5 | -14.72853 | -46.82969 | 2025-09-28 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4d402e-a67a-3a98-bbba-dd3a9824f73f | -13.62092 | -47.3138 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 58f04216-7c0c-3116-9605-f1ad5116f72c | -14.76749 | -45.67754 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cc781ce-d564-3aa3-8458-0933333b4ff4 | -11.37289 | -45.01183 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcd8ae98-d02c-365e-bda8-0cca560cc6ae | -9.28582 | -45.7053 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bceddb94-df0f-347d-a570-cf644ff91493 | -11.65451 | -45.3376 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3874b074-e812-3cb5-bde7-080e37088118 | -14.43394 | -44.87855 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 010ed0fe-e7a0-394c-8177-efa95127a2d5 | -9.09073 | -45.86481 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de27187e-7a1f-3d03-95be-9e2b36718db2 | -10.91064 | -45.75125 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f147937c-ca0f-3d2e-98d0-7d32ba60da40 | -14.58537 | -48.25811 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3052ea0-7f7b-32cb-b737-0583b71099f0 | -12.95096 | -46.38174 | 2025-09-28 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 85ef7486-bde2-3000-be07-448ebe32f795 | -11.38746 | -46.9888 | 2025-09-28 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ff3d0ad-bcbe-3844-a2b4-107d2287d506 | -12.43876 | -45.21057 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89497583-9bbb-3d51-8548-3b63279fd83d | -11.38956 | -46.97834 | 2025-09-28 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a891730-814e-3b79-96c5-ecc6e653802d | -13.61312 | -48.09901 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e49292a4-1d14-3f23-93cc-ab65468a9c06 | -11.44293 | -44.99922 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 685272fb-d962-35c3-8006-d2d7d6da4b9b | -14.34056 | -44.49852 | 2025-09-28 03:38:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 145166c3-ca28-32de-92d5-100c179bd0fa | -11.442 | -44.97404 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6891474-1a31-3c0e-ab33-2c5d0ce37776 | -11.4492 | -44.99686 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2d909ca-c6f6-3263-8707-409bc307e5b6 | -15.90355 | -46.21342 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4d60a00-9d0d-3045-a723-41595d3d89f9 | -9.6572 | -43.85964 | 2025-09-28 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd06d277-01a5-3f99-9cd8-2a2adff88d34 | -9.2152 | -46.78049 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 629fedcf-27ee-3542-a8d3-c933d11aa3a6 | -13.608 | -48.09118 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f4fb2149-c94c-39fe-8b57-43f451c7aaf0 | -15.23011 | -48.06284 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4fcb204-e04a-304f-bb0f-9244d98a125f | -12.43603 | -45.20258 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc9d79b4-9060-3223-953e-cd9d8e6ec5ee | -15.90752 | -45.17825 | 2025-09-28 03:38:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b653d88-8062-3275-ad8c-bcebe8ce8c48 | -12.98942 | -49.43985 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc213fb9-2cb7-3588-9b9e-c1a9b16a9383 | -11.62374 | -44.41972 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8386c258-96df-36da-9c50-07e6bb4ef20c | -11.3808 | -44.97028 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d839a34-8d48-3c4c-b9ea-6b117dda35bc | -14.59229 | -48.2587 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd9315b2-6050-3988-861a-01e2df84299e | -9.28622 | -45.70784 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a45429d7-0906-3ead-bcd0-de8e55f78552 | -13.71643 | -48.34534 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d138f3fe-4f29-3b67-8f07-f0ea6326293f | -12.69296 | -46.87524 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README21.md)
