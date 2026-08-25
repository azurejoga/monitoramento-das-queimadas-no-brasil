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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24c19199-1a6e-3723-8456-01542e45a8e3 | -16.40047 | -49.93333 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b377adf9-d884-3658-85e6-3bfd57a0d9a8 | -20.95572 | -47.47004 | 2026-08-25 04:10:00 | NPP-375D | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4284e0e7-17d1-351b-855d-87e06591e133 | -16.42197 | -51.83957 | 2026-08-25 04:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fba1760f-97c8-3e62-b9de-8174239d81a6 | -16.4162 | -51.83797 | 2026-08-25 04:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe41f04b-d0dc-30cc-bad0-bab93ee8468f | -21.13409 | -50.24144 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f4279066-40a9-3885-813b-fbd79c8fa3a3 | -14.37743 | -51.97334 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ae67ac7-1f08-37a2-a444-b272ae1a2b1a | -22.44818 | -47.40845 | 2026-08-25 04:10:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 444dd7fc-416c-3fe1-bf12-cbf6ab384ff2 | -13.86891 | -54.00342 | 2026-08-25 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e4920a9-6d1c-3c85-a4f8-f6ab69963a9a | -16.63959 | -49.40923 | 2026-08-25 04:10:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 039e934e-d27b-38ce-956a-ed0bb5a4e1b4 | -18.96346 | -48.18105 | 2026-08-25 04:10:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0abf8cb2-cae2-3917-b855-55a99ce27633 | -19.67761 | -47.17178 | 2026-08-25 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc5e30d8-dccd-349e-b3ff-52cf71ef9467 | -14.38829 | -51.76796 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fc647a8-38ed-3cf1-a26c-a8999e24d3b6 | -16.39281 | -49.91766 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21352630-21b0-34e8-ada0-3299d65d673e | -21.06417 | -48.46242 | 2026-08-25 04:10:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b503cb6-2d8b-32f8-b133-48f3790fe366 | -14.39431 | -51.76933 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29c42df6-6045-3b50-9829-7471bf22ad42 | -14.9747 | -52.68528 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c94642e3-af3b-3c34-842b-7a5eeeb95a34 | -18.56146 | -48.27578 | 2026-08-25 04:10:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 358fa96b-ca5d-31c0-afda-bcec7c73de17 | -14.38429 | -51.96577 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5f39c4a2-5f8f-3671-8ddf-70079115fe0b | -16.41151 | -49.87834 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae8b6a7a-f852-3343-b547-d2397d329461 | -14.37718 | -51.96916 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 53c97714-2b12-381c-8477-848e5718dca6 | -16.842 | -42.02353 | 2026-08-25 04:10:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 707b0c0a-9bcb-3ec9-8f32-d679b2b45a83 | -16.86301 | -43.23965 | 2026-08-25 04:10:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec1523ac-e7a0-3a21-a283-414bdca70322 | -16.41291 | -49.92523 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 509af728-429a-3bfd-b648-a19b781b4e80 | -16.4072 | -49.9283 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a299e954-27a7-377b-a8d8-4df59c9181c5 | -18.44469 | -48.41537 | 2026-08-25 04:10:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9da09e39-93ae-3d5c-ba2d-25bddc10b1de | -14.97748 | -52.70334 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5c4b414-2781-3434-ae20-8c5472a68c77 | -21.33827 | -45.33686 | 2026-08-25 04:10:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c80efda1-e867-3eed-8004-a24cf3ec8b56 | -16.06573 | -50.46399 | 2026-08-25 04:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cab46c41-bdd9-3f8f-8d40-16ba18768ab1 | -16.40182 | -49.92662 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52cec517-70c3-3d6b-a3c5-78c2ef9079c2 | -21.13758 | -50.23939 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3c569541-08c1-3137-aa84-4060acaf0556 | -14.91738 | -52.64498 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b61e7f1-550f-3851-9d39-541d15a783bc | -16.41729 | -49.93041 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 323fc5be-ad5d-3a3f-843f-7a72baeed911 | -16.41217 | -49.87506 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec297e45-6d46-345f-948d-a8b05a61c3a1 | -16.83925 | -42.01925 | 2026-08-25 04:10:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 10cc0ba5-1e14-3ae1-bc6e-170aa5aa6e2f | -16.06647 | -50.46035 | 2026-08-25 04:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e772d93a-6aa0-3277-a216-10d92f9f9357 | -16.40763 | -49.87084 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffaeb87e-996d-35ea-beff-101ee29061e7 | -14.9185 | -52.63982 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 972db57c-222c-34f8-a8bf-37dace589b08 | -16.84261 | -42.01983 | 2026-08-25 04:10:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| b9d35638-845f-3083-b62c-96055bb21f43 | -13.86197 | -54.002 | 2026-08-25 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9d3f8dc-7a04-3509-ab4a-cf05d9dafac1 | -16.065 | -50.46758 | 2026-08-25 04:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33a9829e-7cba-3da4-b0c1-14aab258de35 | -21.1388 | -50.23366 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d88bf899-bea9-3cd6-b962-ffeea1002146 | -16.62252 | -43.4205 | 2026-08-25 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f9cbb0d-20d7-3801-ba67-352be87be475 | -16.01735 | -42.98239 | 2026-08-25 04:10:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa96dc8e-c942-3dbd-a69e-ff8f5865469f | -16.38765 | -49.91641 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32b3d581-8e7f-348c-9659-8b873ffd8880 | -14.86892 | -52.67837 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36f082c3-049c-3ffe-9bb6-5c5ace8675d2 | -20.46629 | -46.57035 | 2026-08-25 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62805880-c46b-322f-b581-6e2d4b241840 | -14.91104 | -52.64384 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1839dec3-e233-39fb-aad1-7a10e5b153d7 | -16.417 | -51.83421 | 2026-08-25 04:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d62ecbe-4cdb-3577-863b-c423706ff106 | -15.24179 | -52.79268 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2df0e734-1584-32b3-a8f9-176d28bdc62f | -16.407 | -49.92776 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ee43fe6-7c8a-30ee-b96b-0f888c75935d | -16.40771 | -49.92422 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3d6b7d2-47ce-3183-8d33-0a69153f4b80 | -14.97128 | -52.70141 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fda2036b-36b8-30bf-a78e-4d1564c32f0a | -20.98375 | -47.3684 | 2026-08-25 04:10:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbd98525-59ca-3a3b-b7a1-d41029d045a8 | -14.35915 | -51.75654 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 219c4463-1906-3807-9420-cf15b6a342f9 | -14.28067 | -53.19747 | 2026-08-25 04:10:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84eb748e-c32e-38e6-a315-d51ff7fbf8cd | -19.87604 | -46.21427 | 2026-08-25 04:10:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 497cf912-d468-3185-9f6e-c4a789180454 | -22.15402 | -46.6521 | 2026-08-25 04:10:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6438e49a-9d8f-35f2-af9a-99041602ab5c | -16.06033 | -50.46282 | 2026-08-25 04:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dffbb247-480e-3ad1-b071-dce85b4146f4 | -16.41735 | -49.87608 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5bb122e-b1b9-3e37-95ee-fdd87c65a9c9 | -21.27165 | -49.16313 | 2026-08-25 04:10:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| db6626eb-5f39-335b-a96d-74834e9b0844 | -21.13889 | -50.24266 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 660660e2-e41c-3da7-96d2-3ff866e56e0e | -13.87578 | -54.0382 | 2026-08-25 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e520a6-40c1-3871-9dc4-02c2ca488696 | -20.86688 | -45.7491 | 2026-08-25 04:10:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 237a8531-10f7-305d-8e38-bb0f0fc109dc | -16.14062 | -48.905 | 2026-08-25 04:10:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a05baff-1352-3e32-a7de-0ec063ed0977 | -14.27944 | -53.20318 | 2026-08-25 04:10:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea0d5758-46e4-3856-96c1-017b8a07b7b9 | -16.83864 | -42.02295 | 2026-08-25 04:10:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| cc0c2dc9-e259-3a0a-828a-7f68792a6bcc | -22.15785 | -46.65284 | 2026-08-25 04:10:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6520d58f-dbc5-3655-9ed6-10721027d3ce | -15.6017 | -46.57973 | 2026-08-25 04:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc9d489-92de-3655-bcac-e65044ff2363 | -18.44397 | -48.41805 | 2026-08-25 04:10:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe5e2fe-b85c-3b13-b355-51be0a1ecc5d | -16.0596 | -50.4664 | 2026-08-25 04:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc883161-6f14-34f1-afee-026821a6ea67 | -21.13527 | -50.23568 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8d7e7490-7a3f-3784-9396-226e5c96903d | -14.35817 | -51.76119 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a016816-32a4-30a2-a056-7f7264b87444 | -20.42143 | -46.46642 | 2026-08-25 04:10:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a453bc0-375a-3edf-b5fd-a19fbcec49dc | -15.70439 | -48.31712 | 2026-08-25 04:10:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a1f1777-c3b9-3e8c-840b-2d8b099c28b0 | -20.98516 | -47.36102 | 2026-08-25 04:10:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2df68bc-c0b5-31c2-bf43-c5565808216e | -16.44109 | -43.46425 | 2026-08-25 04:10:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90f0a0a1-db35-3bf9-8d52-ffd8e0e7bb5e | -20.98446 | -47.36469 | 2026-08-25 04:10:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd0a0ee7-beb9-3f97-9636-4395394828fb | -16.41313 | -49.92582 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a166ba7b-e849-34d1-b476-b13ca18326eb | -15.24053 | -52.79857 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af38a464-1891-3f95-aa8a-5c1b9508930e | -14.92485 | -52.64094 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 556fa0d3-9457-33c0-9a7e-6121b91e3c00 | -14.38451 | -51.96995 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5147207c-401e-3d63-a536-0e9c2af9da15 | -14.38327 | -51.97057 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 457a7cff-2c5e-39fe-a5d6-3a440da917cb | -14.97641 | -52.68818 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a096592e-5067-3789-af26-ac71e8c7e797 | -15.70911 | -48.31816 | 2026-08-25 04:10:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0597e2c3-55a6-38ba-8bfd-d18875e393f4 | -22.15519 | -46.65394 | 2026-08-25 04:10:00 | NPP-375D | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8607fb45-55a0-37ec-b421-29c07ae2f695 | -14.37941 | -51.96372 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 317f43c5-0ff7-35b2-bba4-7848e0ee90f2 | -19.68167 | -47.1728 | 2026-08-25 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35f906c3-21d8-3f7e-a434-9ffc31e5c1a3 | -20.46244 | -46.56929 | 2026-08-25 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 607b308a-5149-325a-88d0-65ec6c1a52e6 | -16.4182 | -49.92748 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3bff19c-d802-3832-8864-8c6ad59a7ad9 | -18.55697 | -48.27488 | 2026-08-25 04:10:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31142586-717f-38d1-baa9-d964c4a64694 | -16.3793 | -42.97644 | 2026-08-25 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3664dc8-c162-37be-bf06-76b8531aa717 | -14.27819 | -53.20898 | 2026-08-25 04:10:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5bd21194-2836-3205-b6f1-1cd72ae496a2 | -21.50962 | -45.75877 | 2026-08-25 04:10:00 | NPP-375D | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 10979b44-4db4-343b-aaaa-2a48c538e564 | -20.46726 | -46.56516 | 2026-08-25 04:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17ebcbf0-0d9c-3b3e-8384-6c97be19f48c | -19.04486 | -40.40098 | 2026-08-25 04:10:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d73ebf8-ae26-3e2a-a4a2-47e2ea9405b1 | -22.45213 | -47.40936 | 2026-08-25 04:10:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 349e666b-9ee3-324b-9982-2f713e91ebb3 | -15.27532 | -52.79802 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b02181f8-3b88-37f5-9540-70a28f0f1c43 | -21.14008 | -50.23687 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 824073fe-122b-3f9d-9efe-2ad728cfe367 | -16.14171 | -48.89946 | 2026-08-25 04:10:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2292336-ae0b-3f93-b787-36f35df00e8e | -21.13277 | -50.23824 | 2026-08-25 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |


[Clique aqui para ver as próximas entradas](README27.md)
