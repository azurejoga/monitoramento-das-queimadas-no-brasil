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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ce4eb53-18a4-315b-b009-9fa45296f46b | -20.13134 | -41.80257 | 2025-09-06 12:00:00 | TERRA_M-T | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fdce7597-4ac4-3d4f-91e8-802e687c146e | -16.09905 | -47.85473 | 2025-09-06 12:00:00 | TERRA_M-T | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0f8b7724-aa16-3dbb-994b-3fe54f75d007 | -19.36239 | -44.72444 | 2025-09-06 12:00:00 | TERRA_M-T | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 843d8772-7a74-3ac3-befe-af69de19b942 | -16.27115 | -48.48141 | 2025-09-06 12:00:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cbfbd96c-838a-3950-b53b-8ee125a00799 | -14.439 | -48.44607 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| daa89524-7c90-355b-95ca-8d219196fd58 | -16.92549 | -45.7519 | 2025-09-06 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f42115bf-02b4-3cb9-932c-72ac37102985 | -20.00175 | -41.00593 | 2025-09-06 12:00:00 | TERRA_M-T | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| e0da0f6c-e389-3a4a-8649-71972aec2504 | -17.62306 | -43.76009 | 2025-09-06 12:00:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3a1744e-7d75-3b6e-a677-67d15c04afb2 | -20.00028 | -41.01765 | 2025-09-06 12:00:00 | TERRA_M-T | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5446f56c-f509-3e6a-adb6-392497eacea3 | -14.42723 | -48.4435 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d12a010b-6b59-351b-b90d-cfb581aacf29 | -18.44234 | -45.93221 | 2025-09-06 12:00:00 | TERRA_M-T | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a2735171-b87a-3af7-a20c-10b182ab2a65 | -13.84962 | -46.25668 | 2025-09-06 12:00:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e607b8b0-eed0-3011-8170-e4c2aa39c1fd | -18.11699 | -44.48231 | 2025-09-06 12:00:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 25ce4428-f795-3b73-8846-2c458937797a | -14.43086 | -48.45466 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 161.8 |
| e7fb6ca2-2678-3fa6-a5c2-713f368d8849 | -20.42439 | -42.22045 | 2025-09-06 12:00:00 | TERRA_M-T | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 4111f17c-7c97-3fcc-8a82-913ada2d1361 | -16.26778 | -48.4877 | 2025-09-06 12:00:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 12b4ee62-ad98-39b3-8bed-30609110b66c | -18.4335 | -44.70698 | 2025-09-06 12:00:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 9731dc41-9543-3628-913b-1c0a64e8469c | -18.30932 | -43.926 | 2025-09-06 12:00:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30105b6e-d71e-31d6-b3a9-1e0bf5aa2531 | -20.20752 | -44.87543 | 2025-09-06 12:00:00 | TERRA_M-T | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ca6837cb-3d24-30ed-bbf5-9ab224f8e91f | -19.06796 | -41.13691 | 2025-09-06 12:00:00 | TERRA_M-T | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 139f6eb8-e83e-3865-a4f9-859bff9da616 | -14.59252 | -48.08758 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3db19a39-9a24-3870-96d6-75422e7f0084 | -14.56915 | -48.02824 | 2025-09-06 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| dbd442ce-c821-375e-9bc8-58256319d25e | -15.72179 | -53.5633 | 2025-09-06 12:00:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f7f6aeff-b69c-3daa-9ea8-ffcfcd6dfa54 | -19.36099 | -44.73389 | 2025-09-06 12:00:00 | TERRA_M-T | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f282f515-77be-3712-a2f1-8f8c65dd2341 | -20.80355 | -43.42059 | 2025-09-06 12:00:00 | TERRA_M-T | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7300efd4-c74a-36ba-83bc-d2d98cc86c51 | -20.37349 | -42.4612 | 2025-09-06 12:00:00 | TERRA_M-T | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 173876ba-d029-3d3a-93c3-4637b9434a7c | -18.53695 | -47.41623 | 2025-09-06 12:00:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7521deaf-372e-3c06-b4c8-e9438839ae46 | -17.82022 | -42.16532 | 2025-09-06 12:00:00 | TERRA_M-T | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 914236f4-795b-3f80-864b-c0dd12f9a575 | -13.73534 | -46.91163 | 2025-09-06 12:00:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f1f12ae3-99cc-3caa-b407-e5d9d08db9c1 | -21.84118 | -46.45425 | 2025-09-06 12:00:00 | TERRA_M-T | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4b08b662-82f2-3ed8-9c35-7863c33fb0d8 | -21.08299 | -43.65783 | 2025-09-06 12:00:00 | TERRA_M-T | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e500587a-c7d7-3028-9174-869c2ed1ccec | -20.45094 | -50.00599 | 2025-09-06 12:00:00 | TERRA_M-T | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e2c46302-0238-312a-9158-0272b7a41fa7 | -21.32874 | -45.39792 | 2025-09-06 12:00:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0ad4c6b2-9155-36eb-9921-8346328b3cfd | -21.67387 | -46.15969 | 2025-09-06 12:00:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 551e3db5-7066-366d-a3a2-38b04c17cb85 | -22.65865 | -46.82699 | 2025-09-06 12:00:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| 8c55c024-cd70-3e05-8ba4-884b582069d6 | -20.53739 | -46.46271 | 2025-09-06 12:00:00 | TERRA_M-T | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a833d5b8-d522-3eff-b9ee-d4b7f439d06e | -21.31977 | -45.3965 | 2025-09-06 12:00:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9d0cd1bb-6442-391c-b661-de25a023b593 | -20.94702 | -46.45103 | 2025-09-06 12:00:00 | TERRA_M-T | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 95a494ea-a8ec-352b-8941-474e22bbe0ea | -21.58619 | -46.19075 | 2025-09-06 12:00:00 | TERRA_M-T | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b1c51d6c-dbfb-340b-8cad-de9083f4bccb | -21.84817 | -43.45226 | 2025-09-06 12:00:00 | TERRA_M-T | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 84c11be1-267c-3957-97c0-ed1eadd86781 | -21.38839 | -45.12136 | 2025-09-06 12:00:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a1d7eabf-ae23-3b47-96a8-868ca8fa3aca | -20.53908 | -46.45192 | 2025-09-06 12:00:00 | TERRA_M-T | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c57d190d-4d6f-37a2-b3d7-d72efbdacd56 | -14.4364 | -48.4421 | 2025-09-06 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3304a473-ba63-3222-88fc-858703adabb2 | -10.6128 | -44.3284 | 2025-09-06 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 222.7 |
| c75f97d5-f0cd-34f6-a6cb-f5eaeedc9501 | -9.6841 | -51.103 | 2025-09-06 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 222.9 |
| d8c521c2-3ce2-3621-a977-3984e723a573 | -9.0951 | -47.0093 | 2025-09-06 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a621a299-bfa0-3c66-aaca-05f6ccad51c1 | -13.0161 | -48.0549 | 2025-09-06 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 6a0feb62-d252-3b99-bfe6-357458e78aa6 | -9.7029 | -51.1013 | 2025-09-06 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6491ac0b-9db9-34ec-8786-efb9c2ac4fa6 | -7.6881 | -50.2991 | 2025-09-06 12:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 510c5af4-533d-363d-8ccb-1ebcc1103116 | -9.7031 | -51.0802 | 2025-09-06 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 48b5eb76-ea64-3381-afc6-df5c8c9e8dcc | -10.5937 | -44.331 | 2025-09-06 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 8399ab31-0652-3726-bd96-52201e33068d | -10.3137 | -46.4248 | 2025-09-06 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 8616897d-a6d1-370a-9321-9034cf5b7f89 | -10.314 | -46.4022 | 2025-09-06 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 7ca3bd66-66e2-330c-9e75-b28fe4dc3bc7 | -14.1061 | -51.7113 | 2025-09-06 12:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1101b075-6dde-3693-8465-48ccbc397355 | -9.6843 | -51.0819 | 2025-09-06 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 054cbf89-0db7-355c-949d-f5fb2320cf75 | -9.7029 | -51.1013 | 2025-09-06 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 8c145e54-168e-3c61-ac8a-14680c2a3226 | -13.0157 | -48.0771 | 2025-09-06 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f5b05c79-6507-3ed8-b24c-05037c2b063f | -9.0951 | -47.0093 | 2025-09-06 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 223785d8-f4d6-3ab7-b225-823d12221e91 | -10.3137 | -46.4248 | 2025-09-06 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9e86bdb7-e69c-3a4e-8ed7-d8d16d4b08d0 | -9.7031 | -51.0802 | 2025-09-06 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 754814e5-ba03-3a05-a9e3-a46fb603b6bd | -10.5937 | -44.331 | 2025-09-06 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 886c451f-2a99-377b-bafe-592bd2e6eac8 | -10.314 | -46.4022 | 2025-09-06 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3e5066f7-dfe7-350c-b1ee-760daa034cbd | -10.6128 | -44.3284 | 2025-09-06 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 261.5 |
| add0abe0-cb1e-32f3-b1d9-28e16edf42a3 | -6.2127 | -42.4532 | 2025-09-06 12:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 5235e57b-7957-3577-b41b-7c5584eee8c8 | -11.0055 | -45.9527 | 2025-09-06 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 04035e4b-32ef-3e4e-9e8d-f0b709c0eaf2 | -13.0161 | -48.0549 | 2025-09-06 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3dd1dfc3-97df-39bd-b85d-3888e25ce610 | -9.6843 | -51.0819 | 2025-09-06 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 207.4 |
| 2920e988-227b-314a-b2a7-58ea58871e78 | -7.6881 | -50.2991 | 2025-09-06 12:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 057f0f45-eecd-38a6-ac9e-62bae1b0dd14 | -14.1254 | -51.7088 | 2025-09-06 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| e8be9b17-3c51-3747-af64-3455abd33dcf | -14.1061 | -51.7113 | 2025-09-06 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 0126be36-2f7b-323a-92a1-0e2b7bef3b5c | -9.6841 | -51.103 | 2025-09-06 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 9f483e38-1409-3968-810b-8f426dbd6e1b | -15.7186 | -53.5743 | 2025-09-06 12:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3fd63349-5ece-3a18-aa3c-8524ca7b65bf | -15.719 | -53.5532 | 2025-09-06 12:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3f882eb0-23f8-319b-b86a-e1b567ee65ee | -14.1061 | -51.7113 | 2025-09-06 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 3dce6e62-5307-318c-b9ab-1e27cc87d732 | -9.0951 | -47.0093 | 2025-09-06 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 0839b556-7683-33a9-8624-2bd07b605bdd | -10.314 | -46.4022 | 2025-09-06 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| eae82f2d-7f4c-3701-b297-939921790f7d | -9.7029 | -51.1013 | 2025-09-06 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 462fcec1-c6b0-3a42-aa82-37641a31e458 | -10.315 | -46.3346 | 2025-09-06 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 7b92adaa-3b14-3b48-9bd1-20321f165fd9 | -8.0988 | -45.3371 | 2025-09-06 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 39961583-c312-3185-891c-73b13ed01125 | -9.6843 | -51.0819 | 2025-09-06 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 7553a076-d1bf-3694-adb2-e18e68d2ba2e | -14.1254 | -51.7088 | 2025-09-06 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 10b85a5c-513d-357a-930b-9628e051bd34 | -14.125 | -51.7301 | 2025-09-06 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 776fe4e2-4d93-34c3-b8f3-51caf832f018 | -7.1681 | -48.0861 | 2025-09-06 12:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 1c10d4f9-c712-31b8-beaf-2e68701e33a6 | -10.6128 | -44.3284 | 2025-09-06 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 299.8 |
| 1922b0e4-7880-3391-b7ba-cb9278eff72f | -10.5937 | -44.331 | 2025-09-06 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 87986b79-acfb-360c-b5ed-f6ef65b8c68e | -13.0161 | -48.0549 | 2025-09-06 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 9ad9c62e-a37b-332c-b23b-040172eb5d36 | -13.0157 | -48.0771 | 2025-09-06 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b88d3df7-3c6a-33f1-8797-855860e55a15 | -6.2127 | -42.4532 | 2025-09-06 12:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| a4dc7d40-e9bd-3d3e-b461-caf8cb3fd1e9 | -9.6841 | -51.103 | 2025-09-06 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 21b49a14-0f90-312f-a3b4-c56d3b0e16db | -9.7031 | -51.0802 | 2025-09-06 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d1a16c7f-bebe-3e9d-b96c-77319757bf48 | -10.3137 | -46.4248 | 2025-09-06 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 767a6552-197d-32a1-bf66-54a92056f3cd | -10.3147 | -46.3571 | 2025-09-06 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f9f295a5-ba43-3532-94c4-2614a05ee75a | -5.7298 | -43.9189 | 2025-09-06 12:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e59873a0-9151-3ef1-9e5a-09a4f9b54e68 | -7.6351 | -44.7671 | 2025-09-06 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e1982417-2743-35b0-8634-cb14a3513f86 | -8.099 | -45.3144 | 2025-09-06 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 8ff75cbe-c65a-3260-a1ff-3228e1b7def2 | -6.8841 | -44.7215 | 2025-09-06 12:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| dcffda90-a68f-3158-b31c-eb59ce749a95 | -9.7031 | -51.0802 | 2025-09-06 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 344.9 |
| fab14a63-062e-3f66-bf9c-94367e989608 | -9.7029 | -51.1013 | 2025-09-06 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 348.0 |
| d280a4cf-32a9-3cc2-b1c7-f688cc918cc6 | -13.9026 | -48.0347 | 2025-09-06 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b6ac0e76-dae5-37da-b9aa-45c5e0038794 | -6.8844 | -44.6987 | 2025-09-06 12:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |


[Clique aqui para ver as próximas entradas](README91.md)
