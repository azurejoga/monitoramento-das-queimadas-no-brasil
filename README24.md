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
| 8db6c9ed-4995-31d3-bf8e-f10945cf7df6 | -5.95082 | -43.38898 | 2024-10-18 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6732bbe5-af5f-3ce1-96d6-97d299517c46 | -5.94948 | -39.67546 | 2024-10-18 03:51:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 20ee712b-177f-3d4f-b1ba-6c7c94648110 | -5.9489 | -39.67907 | 2024-10-18 03:51:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd9e886e-dd4e-34b0-8bf2-39a606d5f847 | -5.94676 | -43.38831 | 2024-10-18 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d4611a2c-e57a-3947-a4c6-22ec9f641bc0 | -5.94611 | -39.67493 | 2024-10-18 03:51:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32b75705-fbd0-32eb-829f-6a1e15d86e16 | -5.86879 | -40.17558 | 2024-10-18 03:51:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0969be53-3c99-33e7-81e7-f7fda825f2f2 | -5.85612 | -39.24199 | 2024-10-18 03:51:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 80d2a623-0f3a-3525-b492-f1467dac2df5 | -5.82217 | -40.3142 | 2024-10-18 03:51:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 83311409-aa56-3f49-81e4-95aaaa8ae48c | -5.80299 | -35.58814 | 2024-10-18 03:51:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b87c5ca8-4d23-3126-9267-24c48849f7dd | -5.54416 | -43.9105 | 2024-10-18 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6011b58d-758c-31e8-a980-efb5fa9595db | -5.54069 | -37.27356 | 2024-10-18 03:51:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b490a439-cead-3476-b7f8-7755e27bffe1 | -5.54057 | -43.90593 | 2024-10-18 03:51:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f99c8f4b-bd68-32b5-8e7d-0abaa270288a | -5.21975 | -43.19231 | 2024-10-18 03:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac1e619-2e05-3cda-b73f-0e7f345b7704 | -5.2157 | -43.19164 | 2024-10-18 03:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f2467b4-dd68-344f-8b1e-236b85487e9f | -4.48215 | -42.8821 | 2024-10-18 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b798c2d-6280-3a44-b18e-c633dbb2e280 | -5.16543 | -43.99623 | 2024-10-18 03:51:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 18d6d9d8-85c8-302d-b148-d85558991ea7 | -5.13443 | -38.30425 | 2024-10-18 03:51:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e16e275f-cb99-359b-b730-c73a0d72859c | -5.01317 | -37.10571 | 2024-10-18 03:51:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| daf51afc-7c4a-3517-a64c-5e32aa5c8049 | -4.7924 | -37.7566 | 2024-10-18 03:51:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d5a54b9-18cc-36e9-ad3d-83e2cdf0e12d | -4.65755 | -43.81816 | 2024-10-18 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7701c6e-242f-3608-b5d4-075d73ab2faa | -4.56384 | -38.83976 | 2024-10-18 03:51:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3d98e62-4aec-3ad4-9e07-4f775ef1038a | -4.54234 | -42.97503 | 2024-10-18 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6400ddfc-153d-30a8-a50d-2373249e06f8 | -4.53891 | -42.97079 | 2024-10-18 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddf3b741-9a1d-3b56-98d2-0fb57684b1cc | -4.36081 | -43.85943 | 2024-10-18 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a28ca9d3-9048-3958-83bf-44e772cde079 | -4.12851 | -43.34082 | 2024-10-18 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6327cfde-66a8-34d2-bc47-5cdd49df9030 | -4.10684 | -40.14368 | 2024-10-18 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e335f455-3822-30ae-93f4-e7d39a70247b | -4.07031 | -42.69677 | 2024-10-18 03:51:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b86b8812-68b2-3fdf-a143-8f99b85cc773 | -4.0109 | -40.38644 | 2024-10-18 03:51:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3608db6-29de-3ebc-9cca-179951eb3b1b | -4.00613 | -40.39373 | 2024-10-18 03:51:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fc404dbb-2892-3dad-8fb1-3f9d5eed4142 | -3.97697 | -43.16209 | 2024-10-18 03:51:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b75a77-4d7b-33ce-8fd2-634f47c7ff32 | -3.90791 | -42.41212 | 2024-10-18 03:51:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff13cd80-b007-39c4-8526-76d036e3d638 | -3.9048 | -42.40648 | 2024-10-18 03:51:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2dc0243b-d9e8-357f-bc84-1df2b9910ff3 | -3.90398 | -42.41148 | 2024-10-18 03:51:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36a505fd-94f8-311a-aa07-8f15d7d2a400 | -3.90303 | -43.4775 | 2024-10-18 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5121eef7-8cb5-3c4a-93ee-47a1b098f00e | -3.90273 | -43.47843 | 2024-10-18 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6606b212-c995-3801-95c0-761dedc099c3 | -3.79942 | -43.23322 | 2024-10-18 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 742d147d-e91d-3652-9875-0061ee111a9d | -3.79051 | -43.23559 | 2024-10-18 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 97c38279-a15b-3b0f-82eb-eeb282411f88 | -3.78028 | -43.90934 | 2024-10-18 03:51:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc9de7d4-a775-3022-9a49-77e7357d09bd | -3.6677 | -39.06845 | 2024-10-18 03:51:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a68a312b-83fa-30a9-83be-bc284c35b411 | -3.53763 | -43.62048 | 2024-10-18 03:51:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ab930de4-4ae8-307b-83a4-8ac70612f81d | -3.53336 | -43.61977 | 2024-10-18 03:51:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 59270c3c-f833-389e-8025-a565ed8bc2df | -3.51877 | -43.23181 | 2024-10-18 03:51:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f38be6fc-f148-334d-8934-aca1d6d9b1e4 | -3.51815 | -43.23558 | 2024-10-18 03:51:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 206c6262-6c56-3835-9799-e9c36aa1c067 | -5.60803 | -45.20037 | 2024-10-18 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb232cfb-71bd-33b1-a976-226f8e419cd0 | -5.57658 | -44.88499 | 2024-10-18 03:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15d78c57-a4d5-38a8-805b-1a7807c67ac4 | -5.5758 | -44.88964 | 2024-10-18 03:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| edfd5896-6e8e-3bdd-a005-5da7145f9ede | -5.57207 | -44.88422 | 2024-10-18 03:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 66def82e-0a61-330b-865b-b9f5894850fc | -5.57129 | -44.88883 | 2024-10-18 03:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 563727ba-16e3-3ab7-a28f-a8bcbaac6fb2 | -5.57051 | -44.89349 | 2024-10-18 03:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 396469c0-9a0a-37a9-8f96-9e59c7d2b8f5 | -5.4249 | -44.6339 | 2024-10-18 03:51:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0952d415-a378-313c-ab0f-fca5c6a9f111 | -5.42045 | -44.63317 | 2024-10-18 03:51:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76fca048-27fa-3ae7-bae1-cc0f4c59b058 | -5.28946 | -50.92885 | 2024-10-18 03:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19728b77-383f-3a23-9a0f-873bb0567a2f | -5.24815 | -44.17711 | 2024-10-18 03:51:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a798d88b-0b38-3979-bcfd-64a17f11ea13 | -5.24451 | -44.17231 | 2024-10-18 03:51:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16f3f6ac-b108-3a42-b1c8-0407f8e97280 | -5.24018 | -44.1716 | 2024-10-18 03:51:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e92abc-aaf1-39ba-a069-0f4bc985ff41 | -5.14188 | -46.09176 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 559bf09f-1533-3a5e-adfd-8d43f1f887e9 | -5.08663 | -44.25363 | 2024-10-18 03:51:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16e6ae3c-0ee8-3332-ba6e-f73cf0a48b1f | -5.08591 | -44.25787 | 2024-10-18 03:51:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24469332-b720-3617-8107-f1b7092d3d26 | -4.94965 | -45.66332 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d3a1b79-92f3-3370-bda6-6938b95f8cf8 | -4.90388 | -45.88013 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4fc65e0-80d2-375f-9a11-1bf300498f0e | -4.89462 | -45.91961 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 627bd3ab-4830-327c-bb80-c556f9b0d058 | -4.89363 | -45.92532 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e07fd21-545b-311f-b508-adb0f0f0e7ef | -4.89177 | -45.92282 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3c51cf6-14c0-3c8a-a68c-9c269a155f9a | -4.88875 | -45.92435 | 2024-10-18 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8036db03-9540-3b52-9beb-0579ac174e89 | -4.68758 | -44.12854 | 2024-10-18 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6daa841a-32fa-3f8f-a41d-a5ef2add8c6a | -4.65798 | -46.33681 | 2024-10-18 03:51:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c30e832e-e7aa-3a69-8ebb-987ce180b2b9 | -4.65748 | -46.33971 | 2024-10-18 03:51:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 941fb63b-6bf0-35c3-9cc7-ef3f969cb87e | -4.64166 | -44.53814 | 2024-10-18 03:51:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8322722b-1cc9-3c0b-8c33-ba49c2f25312 | -4.62421 | -45.61291 | 2024-10-18 03:51:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c15609e-212b-3816-b9a1-cc5545d40cc8 | -4.61153 | -45.88479 | 2024-10-18 03:51:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3111fc6e-76d6-391e-825d-b0c759e6386c | -4.60809 | -45.62046 | 2024-10-18 03:51:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 246c9262-a0c5-33b5-88ac-72a75ba022fc | -4.6066 | -45.88411 | 2024-10-18 03:51:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1ec1e76-31ba-3a9f-b406-ff9881bf5a06 | -4.5808 | -44.53032 | 2024-10-18 03:51:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c3e3976-2a2a-33a2-bf28-56308b5a850e | -4.55061 | -46.67781 | 2024-10-18 03:51:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20709971-84fd-3af9-b3c9-b809f8140146 | -4.55008 | -46.68104 | 2024-10-18 03:51:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e4cfaca-7b3a-362a-8dda-b270c3775ab9 | -4.54542 | -46.67697 | 2024-10-18 03:51:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 638c7177-2f2b-3a26-8413-8e6729d1bff1 | -4.53975 | -44.41831 | 2024-10-18 03:51:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c88a2d1-92c3-33b2-8ebc-f4f8ed1526aa | -4.48418 | -44.97572 | 2024-10-18 03:51:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60d5f667-e6f7-3ca1-8b90-d46683b01247 | -4.42659 | -45.97152 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 16350cbc-a470-3e7c-8838-6d52d818e3d0 | -4.42571 | -45.9768 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1cb61f2b-3143-366b-8deb-7e64f735635e | -4.4226 | -45.96488 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07281cdf-37ec-3d77-ba6f-b8c8e8df9059 | -4.42167 | -45.97043 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 42371e89-172d-3fd4-926d-001e8f1b18a1 | -4.42074 | -45.976 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 52f852d2-140d-3531-bc11-3bfd9c5fcafa | -4.41983 | -45.98147 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9edcfe5c-4b59-3b99-a249-0a16ae0e0d67 | -4.41769 | -45.96383 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a067913d-d466-3d24-a054-90ba7676d90d | -4.41676 | -45.96936 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 784cb884-6ace-3881-a18b-61dc5844f8c8 | -4.41581 | -45.97501 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dc0ce450-16af-38f5-9ae3-aeb3dae00d7b | -4.41487 | -45.9806 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 61678542-63c1-336b-9d98-ebd8ae2d6589 | -4.414 | -45.98578 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f08135c8-21f0-3424-86c0-f8eaba9db5ec | -4.41087 | -45.97405 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 636fef6b-11e0-3c3c-bede-37073624e7c4 | -4.40993 | -45.97969 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 81d85c82-f298-38fd-a03e-28368d2f305b | -4.39231 | -50.81336 | 2024-10-18 03:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93c9190f-1743-3a8e-a37a-11122fae3278 | -4.38745 | -50.81269 | 2024-10-18 03:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 882fa8f4-8314-367b-a17b-c87fe56d927e | -4.38553 | -50.81232 | 2024-10-18 03:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 734032aa-ac02-317c-b128-d3085fa342db | -4.38302 | -44.22225 | 2024-10-18 03:51:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3144f9a-99e8-3bc0-9a96-8cc71ed67b0b | -4.38232 | -44.2265 | 2024-10-18 03:51:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be7ced3-3fbd-3594-94ab-aba8b8965fae | -4.38208 | -45.41399 | 2024-10-18 03:51:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 119f1c6d-cdba-33aa-ab38-62e0ed3f9688 | -4.38123 | -45.41909 | 2024-10-18 03:51:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fa2a5ee-2e9b-3bb7-9882-8f519f28c086 | -4.36684 | -48.48911 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cafdd8f2-adf6-3370-ac2e-2c9a78f51607 | -4.36616 | -48.48479 | 2024-10-18 03:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
