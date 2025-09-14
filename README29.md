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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8a6cf9f-f81c-365d-ae18-e98786a5396c | -13.01155 | -46.74246 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb51ad93-ffa7-31b2-b7f5-dc6372d43351 | -11.39702 | -50.45461 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6cf325e-f86a-3b38-a37b-80c66c399296 | -11.21473 | -47.66745 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dbcdf29-2285-3673-933a-6f8ef044b14b | -7.43911 | -44.38933 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 858e3f69-ed25-3188-a7c2-613a9b1bc044 | -12.80654 | -47.9597 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e2af4455-0e38-3276-a0b2-2e1e28516b69 | -11.47223 | -50.80066 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d5b746a-5a93-31b9-afff-5ed14046b56c | -12.95349 | -48.03865 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a90eb602-88df-309a-ba11-5bbd77716a19 | -13.29069 | -43.78252 | 2025-09-14 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 149fb1e4-6884-3a9c-b595-2083f8088961 | -9.05671 | -47.02417 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f50a996f-16e6-3d55-8078-4f74a2e57871 | -11.38151 | -47.71112 | 2025-09-14 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d604cf5b-1531-3ade-b4b3-05f9044633ac | -13.53951 | -43.01199 | 2025-09-14 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 32ffbf3c-1521-39ed-865c-d07a9a3c40a5 | -11.46671 | -50.7711 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8a3bca5-8a26-38c4-a66c-f9a165556dcc | -12.92838 | -47.958 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38bf5fc5-0c75-3397-a119-a77ee9b1f51c | -10.40552 | -48.60471 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fbf82682-2400-34ea-a280-3ed9e6ae07b6 | -12.08457 | -44.73015 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b166b152-5739-3a27-974e-4aa7a7eafacb | -10.36183 | -50.48152 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be2986b4-71ad-3d49-821e-709b0c21ae5b | -11.62481 | -48.53794 | 2025-09-14 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ca29fbb-3b90-3ae1-85a9-b37a728f09f2 | -6.86376 | -44.89737 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c666af7-bb29-39fb-9f54-a8cf1c78c5bb | -10.76787 | -44.77559 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b23200f-5131-374a-b888-ef9071864cbc | -7.52609 | -47.63879 | 2025-09-14 04:40:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e4d1595-732c-3742-8a9e-6f4d1461a5eb | -10.59956 | -44.33931 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 61ab4d45-7b01-3607-b92a-698442e6d9d1 | -11.14394 | -47.65247 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7410fff8-b6ba-35c1-af33-fd577c2e678e | -8.93272 | -46.72902 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ac623b7-7298-3fdc-bbf9-3ce2744d6acc | -12.97533 | -47.98852 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 552235ec-570c-3f51-b9a8-39092eea7cfc | -7.54016 | -43.98697 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da6e22cf-d0fc-3638-bcdf-98cc2712e351 | -10.76522 | -46.47716 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0674c605-68c9-3015-bdb9-10c9207308f8 | -11.5025 | -50.80194 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41c016a0-d2da-322d-a925-d58940da6330 | -13.94688 | -44.85519 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 7841b2a1-73b8-31e2-8fe8-1bcca4e342b0 | -11.49259 | -50.80035 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1441e607-c8e4-34fc-802e-cd2864c322e6 | -8.35341 | -44.74129 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dd68c91-3c6e-3b89-bf41-fb5c7828bd01 | -12.11577 | -47.57464 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c050130e-2e24-3a97-a674-02784a3931a6 | -10.35732 | -48.83202 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7272bbec-9de2-3b18-90ab-5f2c6ab76747 | -8.10467 | -50.1655 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96ab964a-a483-3f74-b442-296ae71cc6f0 | -10.71931 | -48.68656 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c734eb7-d5b0-3d1b-ab69-3788bd3de767 | -11.47994 | -50.79473 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5b02428-e699-3d09-a147-e7534be6e287 | -11.48266 | -50.75573 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4675b7ae-5df0-30ec-b802-9a9562f546b7 | -8.76177 | -46.04284 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b73d8912-8301-3a75-a432-ee56f66eefde | -11.83649 | -50.49332 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e86b4447-6e22-346b-8e8c-08df701c760a | -10.91401 | -47.19543 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 05126f3f-fa19-367d-bea7-9d7cb81235ea | -11.39363 | -47.34024 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19c41ab3-fd92-3a0f-b38a-27fb05257dc8 | -12.74993 | -48.02251 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e120de2b-c9ab-36bd-bd97-1cb00523b45e | -12.92953 | -47.95996 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a583ac5-14a6-31dc-a59d-576e0a4648ea | -11.46413 | -48.69762 | 2025-09-14 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3d0271f9-bc95-360c-b63b-95e9d75af4ac | -11.9136 | -46.53251 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1e826ae-531d-3dde-9192-1f876bfb1d93 | -11.48322 | -50.77374 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a2828c0-55fe-3cc3-9fd3-3c8ecc23b602 | -8.96154 | -46.18858 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 726da45f-301f-3223-8528-a1ab8ce6306a | -11.46356 | -48.70145 | 2025-09-14 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 0c477f28-bbda-353e-8899-8218a07111c1 | -11.40814 | -55.35804 | 2025-09-14 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b0190061-6ed0-3dd3-b731-e8e93c9f7a1c | -12.13811 | -47.59971 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c26761c6-1afb-3e37-9e21-e2be52fe3702 | -10.91339 | -47.1997 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5f716a-dca8-3e7c-8113-7584003ba02b | -11.47709 | -43.60349 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31e53f56-d531-35e5-944f-34c1e27fba60 | -6.6188 | -55.30807 | 2025-09-14 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78bd6a76-9c40-3170-91ea-713e092f78bf | -10.70339 | -48.67644 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9daf5737-e70f-36ab-a21e-5a7ce1291bc4 | -9.50406 | -55.96226 | 2025-09-14 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 374b0a19-9260-3fc8-992b-2a2e7742f029 | -12.2521 | -46.78888 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 823cf9f6-b4a3-3d0b-896c-2c2923e76115 | -11.47112 | -50.78614 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86cfa673-6cd9-326f-9adb-9884c97617c6 | -12.77193 | -48.02171 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dddc9bd0-dc1d-3ac9-ad7f-1b2f057de789 | -11.38207 | -47.34303 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b6df7ee-b283-3bd4-b969-fb8ca65d8aca | -6.99677 | -44.54179 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07173eb-942f-3173-af85-f5256e10e2d2 | -11.86926 | -46.76233 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4e2e219-cd85-3d4b-b56e-d3564ebc72b2 | -6.56309 | -50.87629 | 2025-09-14 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f5f6da30-4402-3628-a7c1-697d6648867e | -8.11127 | -50.16655 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae32562-e49e-3c50-bd5b-b5b62eb349c4 | -12.73328 | -48.03684 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73d46eec-f6f0-371e-adf1-269f693c8f81 | -12.90907 | -46.54691 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2e6f880-c325-3214-896c-203d5efc2bdf | -10.40115 | -50.60197 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0472c76-b529-36b0-98c0-cb083a025876 | -13.93153 | -44.83537 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3676d5c-3d77-38ea-a026-fe8bcca2476b | -12.09264 | -44.86861 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 403f564b-8095-3d71-b368-c77d8c8f6ff9 | -9.02124 | -47.06472 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cecc6ac0-1f63-34fd-b6b2-a3b5c6df1a52 | -12.95647 | -48.04327 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0422b83-1583-34f1-b716-7bdda5406e57 | -11.4645 | -50.76357 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 989f64ed-c4c1-3f34-ae9c-8547e839b428 | -12.16886 | -48.71568 | 2025-09-14 04:40:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 755ccd22-f6bf-35f6-a0bd-f1daf94a28cd | -11.46945 | -50.7536 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6cbb8043-9ce3-3705-a48d-ffd57e7e4594 | -13.93427 | -44.84893 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| b4ea0ec1-9448-3906-b40d-f87ce4c7d478 | -11.48213 | -50.78074 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a165cb3-3228-35bb-bbac-f186cf7bb04e | -11.25073 | -44.78008 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0842d6f3-9210-343f-814e-a6af547bff43 | -8.76963 | -46.04207 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d9455b72-6928-33d3-b7df-ff91e401efde | -12.78559 | -48.02805 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fad8bd6a-4039-3630-ab8d-bc2983995ce6 | -10.66538 | -48.67412 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41cab5c2-3240-3e51-8586-71b2884c52dc | -5.57159 | -51.8978 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8303db21-379b-3e46-9f27-7b7fb352b387 | -11.44375 | -45.13656 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37943bd4-228a-319d-ba5b-3244cedd17c0 | -12.78443 | -48.01103 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5111bd69-9798-3d08-a70a-dd6ed26d071b | -7.3917 | -49.98104 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891de039-f359-317b-af1e-0d9e48401fff | -11.46505 | -50.76007 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4209c597-b21c-30d3-a993-e93bfe31cf0d | -11.44824 | -46.91626 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ee2a9a-5ac4-32fc-a976-6d965c4be336 | -10.76456 | -46.48186 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f4697ed-0a16-3144-8f69-bdad90037818 | -13.94143 | -44.82804 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c9bdc9c-4e13-38eb-bd2a-bdf7d49db307 | -11.36751 | -47.34103 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb97a45d-3246-310f-8216-8b1d5c266638 | -11.86402 | -50.49053 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36f24ba9-88ea-3e0c-94bb-5eafb291da9f | -11.46616 | -50.77459 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1e589cc-afe8-3fef-9ed3-353dabf8cf75 | -9.01706 | -47.0435 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63a10576-0a06-35b1-be2e-30e0c9482fac | -11.48377 | -50.77025 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84890f33-4edb-343a-a6ba-ed560e956fbb | -11.49148 | -50.78583 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4621cace-adf7-3a90-b012-8ef4930defe4 | -6.99115 | -44.55191 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 163ae4f2-c62c-34af-a6bb-59fe17220046 | -11.481 | -50.7447 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7886f9d9-2cf3-359e-99c7-c18302d10bb3 | -11.46228 | -50.73452 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4501525f-0c50-3aa2-b1c3-20c06c7f634d | -11.17647 | -48.34636 | 2025-09-14 04:40:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56416637-6bf1-38ea-9a9a-eb827743ed59 | -12.76005 | -48.00291 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18f20b51-1ae1-3e46-8bc4-f9daecf7efb9 | -11.24837 | -47.62999 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f6d0b0d-13a4-3456-8050-d4b0758c6fbd | -8.18608 | -45.5773 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daa598cd-43b8-3bdd-9559-5948bc9bb523 | -12.97075 | -48.04559 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |


[Clique aqui para ver as próximas entradas](README30.md)
