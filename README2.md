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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfe3f436-6abc-3995-a4ea-a20d1b190799 | -20.1666 | -46.86479 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e475d8bb-1688-3c34-844b-d58d495723bb | -14.7511 | -42.46296 | 2026-04-24 03:40:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcbd4605-cc0f-3dc7-8a81-4bd2dd6c2525 | -20.21143 | -46.81562 | 2026-04-24 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0830e472-d56c-38ae-b283-1a7a75d365bc | -15.33087 | -43.80265 | 2026-04-24 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ce4d525-33cf-36a1-bab8-aef4551b2bd9 | -17.53421 | -44.75122 | 2026-04-24 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 063e9da7-1338-331e-bff0-46e177cf7f52 | -20.19918 | -46.92406 | 2026-04-24 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ed90ee9-9291-3e89-94b8-21363a73f58a | -17.50415 | -45.00773 | 2026-04-24 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6b1d799-5415-394c-90d3-ff84191fb4f7 | -17.50103 | -45.01115 | 2026-04-24 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7be961b-469f-3e3e-b968-19d05e68246d | -20.18964 | -46.88944 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89260f00-0835-39cb-8db7-736dafb834f9 | -17.49847 | -45.00966 | 2026-04-24 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef45eb40-26d8-3d61-834b-b84179402ffe | -20.2411 | -46.757 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4338e9ba-7d57-36eb-ac59-6bea3b40dae6 | -20.19405 | -46.73008 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9beaeb6-bef0-3d66-b366-89f628b34d61 | -20.19609 | -46.73069 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f77d89-88be-3fff-b997-ae23bd6f27b3 | -15.32754 | -43.80353 | 2026-04-24 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7d7bddd-13a1-3d4d-b4d7-f41dcd3ad27a | -20.16055 | -46.86643 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b460c82-8275-3c4c-a473-4bc8b0313f53 | -20.24036 | -46.76042 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c43f2766-1a8f-3b7d-bf54-69a549b82d97 | -20.16464 | -46.86841 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c97d1945-8b7c-3cb2-a5ed-7c4ffb869a9a | -20.19752 | -46.87944 | 2026-04-24 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25606948-39e8-38b2-8dba-cd2ebf0d8e2b | -20.16581 | -46.86838 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33064670-5fda-3e5b-ad53-fb10243c205f | -17.50354 | -45.01082 | 2026-04-24 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d57b9d62-aa60-3dad-bec1-ad8b4bca5aaf | -20.21229 | -46.81168 | 2026-04-24 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e0cac6e-41e5-38d4-87f2-c629dd290766 | -20.24321 | -46.77337 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e6e1c91-dc49-3bdd-9e6c-7c8cfa244e68 | -20.16738 | -46.86126 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05247eff-6e5f-342b-b04a-356bb75c95d8 | -20.56329 | -41.02302 | 2026-04-24 03:40:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a63a4605-891d-3f7c-b962-71e9e36cc7cd | -20.1594 | -46.86631 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50b4942b-b67a-337e-9134-352ad18e25d1 | -20.20271 | -46.88169 | 2026-04-24 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e2c01e2-ce2c-3219-b168-9b0ce6833e1c | -17.16872 | -46.83375 | 2026-04-24 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fd5f758-1dab-3eb5-a7d2-95c37b088cee | -19.80095 | -44.64061 | 2026-04-24 03:40:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ec1062e-5c11-349b-969a-d412e1fd5bbe | -20.24383 | -46.77048 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3b47ace-13f5-35f2-a9c1-7ba371b18787 | -20.23577 | -46.75554 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe489b97-2933-3b5a-a8c5-e87fd99acf8f | -20.16542 | -46.86472 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 064c7a5c-6d37-3d54-817f-2f2dbf480203 | -20.1905 | -46.88553 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 159f1c81-4f3b-3fec-9ef9-5c78e4376aea | -25.65493 | -50.12592 | 2026-04-24 03:42:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 56a66d0c-87ab-32ff-b2f8-9832481c0ec5 | -25.65671 | -50.12876 | 2026-04-24 03:42:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b03123a4-4913-35c1-b007-cc93bf30e4c7 | -22.71201 | -45.0531 | 2026-04-24 03:42:00 | NOAA-21 | CANAS | SÃO PAULO | Brasil | 3509957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63d93ca4-3c9a-32f0-8cf8-758adee3d894 | -26.19256 | -51.37684 | 2026-04-24 03:42:00 | NOAA-21 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 151e164a-2983-37e8-b91a-98ddc866834b | -22.74828 | -43.46223 | 2026-04-24 03:42:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0aec4dbe-c707-3544-aaff-3d86cf8a78da | -25.6578 | -50.12423 | 2026-04-24 03:42:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 519b5313-89db-340b-ae06-e7add96c0a1c | -22.7019 | -43.36248 | 2026-04-24 03:42:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b997743a-b57f-342f-add1-6ed5b0793066 | -21.69917 | -48.43651 | 2026-04-24 03:42:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3def2c3-aed0-39fb-8c50-35308152114b | -27.49583 | -51.39988 | 2026-04-24 03:45:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e24fabeb-1c43-3b80-ae7a-b074538a58e6 | -27.49712 | -51.39477 | 2026-04-24 03:45:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b07355e9-e971-388c-8e0c-2408437cd5c3 | -4.36499 | -37.90164 | 2026-04-24 04:08:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4dfd8f7b-fb1b-3b0e-82cd-6a3d83db4b87 | -4.36557 | -37.89799 | 2026-04-24 04:08:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6a9f42b-34b5-38fe-b531-619dbc4e1f66 | -11.95423 | -43.38274 | 2026-04-24 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17119670-469e-3940-969d-143b21fcd21d | -13.37887 | -45.30817 | 2026-04-24 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecf51ee0-e144-3dad-a372-1f1fc9895038 | -11.8615 | -43.86847 | 2026-04-24 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df9527f0-0d4f-3a25-b1aa-9aa06e7d315f | -11.77546 | -43.64762 | 2026-04-24 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b31ef46-1c64-3462-bb6b-3e31f9562485 | -13.38101 | -45.31778 | 2026-04-24 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d313f9-ec80-364e-b5d0-2b1c24f31d36 | -12.28117 | -44.62737 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5475ab5-fa84-331a-9f61-40d732c4d0c1 | -11.86177 | -43.86764 | 2026-04-24 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 047e9719-2c6f-3ee8-8e37-85d1388b67b2 | -10.97686 | -49.43355 | 2026-04-24 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17e47e18-2cb4-308f-84b5-bdbba4f41b05 | -12.27829 | -44.62246 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1342caf3-4c6c-380e-8019-b91896e5cfe4 | -12.09348 | -51.22719 | 2026-04-24 04:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ecbd18-530c-307b-afc1-f141322deaf6 | -11.06194 | -49.50098 | 2026-04-24 04:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffcbfa9c-293d-32a4-827c-e431c77878a8 | -12.27797 | -44.6242 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 764f2a22-7356-3ccb-b0a1-baaa4bdcd1d3 | -13.06721 | -42.13479 | 2026-04-24 04:10:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 549991e2-d5a3-339c-b21d-b14191ecd51d | -12.09276 | -51.23087 | 2026-04-24 04:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1d3585c-8647-3d13-8e1c-f886a4718149 | -10.00752 | -48.67046 | 2026-04-24 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88ed3862-13a0-3362-8f97-8dc772f3719d | -12.27755 | -44.6267 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36806d9e-7a5c-31a0-b20a-9f15f6425b91 | -12.27725 | -44.62844 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 998029c1-2226-305e-90e7-d78a271475b4 | -8.7864 | -44.84162 | 2026-04-24 04:10:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 346c4200-4183-31af-9531-b828b48ef9c2 | -13.07385 | -42.13597 | 2026-04-24 04:10:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 604147a2-1ff0-306f-af5b-8291c26b955b | -12.27868 | -44.61995 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5f61916-9624-3e87-a76c-ee0081fbbfbf | -13.37439 | -45.31197 | 2026-04-24 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 374ba45f-0cb4-35d3-ba76-4dee5e043a8c | -11.86529 | -43.86824 | 2026-04-24 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f253c452-1196-305a-833c-d93d669be643 | -13.37809 | -45.31264 | 2026-04-24 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 756d5bba-cd0c-3531-a43d-180749d2e712 | -12.28478 | -44.62804 | 2026-04-24 04:10:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e75124be-5fdc-3ed3-a9c1-d08429545555 | -13.54311 | -47.8891 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abb1bc6b-ae9a-31a3-b9db-fa73e35e5297 | -14.89707 | -43.41345 | 2026-04-24 04:12:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe5c8255-2016-3d86-b681-fa48a523d08a | -13.53639 | -47.89355 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47188ce0-25c5-3a87-91eb-464e3f265674 | -18.28192 | -52.9241 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cee1d979-60a8-3de4-bd0a-7150201f0d29 | -18.27412 | -52.9068 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a764d8-1c64-373f-b1b5-9a8f6e75582d | -14.59125 | -47.97465 | 2026-04-24 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca2a296-f859-3056-b470-7fd9344e1125 | -13.54236 | -47.89309 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0289415f-45b7-37c8-93ab-9f05964190e9 | -13.54577 | -47.891 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be8a478d-9907-32d1-b81b-979369460f9e | -17.48105 | -51.09095 | 2026-04-24 04:12:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fdf59b2-5456-3f03-b3d7-276c7361be53 | -19.963 | -44.6893 | 2026-04-24 04:12:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e40ef29-4323-3a6d-80dd-cfd9f0f8720a | -18.26866 | -52.90562 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f4bf231-70b8-354c-8d2e-9e29e31aea08 | -18.27724 | -52.91914 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d6d6610-d118-3cd8-8482-c51dbcf58d91 | -19.94895 | -44.70707 | 2026-04-24 04:12:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be7aedda-0527-3433-aba3-c168739e5dc0 | -13.53803 | -47.89238 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f1de50f6-7a31-3f7e-bc39-9b5f5ace73ef | -18.28231 | -52.91904 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcd2a8bf-b062-38cd-b1c0-7b1a3fb4bdab | -18.28151 | -52.92275 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b8e9988-7aef-38e5-af96-b16d5143387e | -18.2827 | -52.92038 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8a3f166-b363-3157-be0d-38c1c77891a5 | -17.5345 | -44.75441 | 2026-04-24 04:12:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d6583b1-f5b0-3269-9a79-c8c5ba5a21a1 | -14.34123 | -47.23296 | 2026-04-24 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fbdfe1a-a45a-3a4c-ab3a-511c44fd2e7c | -17.50216 | -45.00962 | 2026-04-24 04:12:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21f1f480-839b-32ad-9292-34c7b40a58a8 | -16.43121 | -54.91626 | 2026-04-24 04:12:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9975b71-a65d-308c-b70d-5e1d4a0b63c7 | -17.48 | -51.09441 | 2026-04-24 04:12:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abfe8573-4c36-32fd-a4f4-3bd3c46f6b4e | -17.56331 | -46.6082 | 2026-04-24 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5d55d00-5d6f-3d54-b41f-6fd65342e3f0 | -17.16633 | -46.83375 | 2026-04-24 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3422ce6e-cc87-33bd-be41-2abc3bc7beee | -17.2621 | -51.8836 | 2026-04-24 04:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c42d8dc-a006-3327-a123-77276d9e9ae3 | -18.29439 | -52.94649 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4ba4752-6283-343e-9ad9-4279ddbcef30 | -13.55171 | -47.89085 | 2026-04-24 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da899199-14dc-33b3-8544-184309ef5513 | -18.29362 | -52.9502 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dade9473-ce42-3241-8d1d-d4d5b31e060e | -18.27955 | -52.88108 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e6d2a4a-cefd-3265-b2a9-d43739725ef1 | -18.27098 | -52.89461 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e65c4113-1195-3a35-8174-f209001ac371 | -18.29306 | -52.94872 | 2026-04-24 04:12:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 034dc0f8-c69d-38f6-8059-cbda8e760ce2 | -15.3292 | -43.80246 | 2026-04-24 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
