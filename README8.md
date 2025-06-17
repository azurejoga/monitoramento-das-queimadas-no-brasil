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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38a19a3e-408e-3559-9b31-38d1494968ae | -9.41118 | -48.41906 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ac04f4b6-b24a-3472-bc9c-372124d097cc | -7.25335 | -44.61154 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4be21b91-b0d6-3344-a95c-257c53575105 | -8.33833 | -48.4459 | 2025-06-17 04:08:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6e25443-5970-3e9d-ade9-360e9caa8195 | -8.39348 | -47.46268 | 2025-06-17 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d8fbea4-306f-39c5-8a9b-ac3b5828b53b | -9.4158 | -48.43254 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fb0351c-22d2-30b1-a301-46f6686b1570 | -6.15573 | -48.05864 | 2025-06-17 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6928799f-0e5f-379e-a24e-f11a7a77f06d | -6.29971 | -47.00741 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd000875-a7f2-3bfa-82ba-349bdbd96d2e | -7.24783 | -44.62307 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c86790a7-6c02-3629-bf2d-2c83f9e66b66 | -8.07246 | -43.10968 | 2025-06-17 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 317b7b4f-8571-357e-8cde-128a0d939692 | -13.46711 | -46.26471 | 2025-06-17 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96626066-53df-3612-80cd-d37dcf866ef0 | -11.14702 | -53.93306 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6e7f1892-1fe6-3609-949e-d25be9ed8e33 | -11.71919 | -47.7352 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5c6aa9a-000a-3279-a583-b5b228c97964 | -14.82297 | -48.45451 | 2025-06-17 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 107dc14e-9a51-32cf-a621-d1a58aada8eb | -12.23021 | -44.20893 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef7f1006-f40c-3022-8162-75722ae2f6b1 | -11.90824 | -44.17849 | 2025-06-17 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dba04db5-3dfa-3601-b269-8aa6fc9f9d01 | -15.13744 | -49.5456 | 2025-06-17 04:10:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd941d82-6557-3f98-8da6-50716f0ee95d | -11.91754 | -54.81869 | 2025-06-17 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64648abc-ff7a-3288-a7d1-f5bfb0e5ac22 | -12.27161 | -44.58277 | 2025-06-17 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e132e6ab-3de4-3891-9dcb-9ae0c02565c3 | -13.58788 | -54.29347 | 2025-06-17 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00e09b5d-f509-393b-896f-d7c90dcfd408 | -12.34216 | -49.30947 | 2025-06-17 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 271f0b96-1c13-367c-a5f4-2500e50e02a1 | -15.40312 | -47.83743 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67e893e1-73bf-383c-a90b-5bcb24b40533 | -11.14011 | -53.93657 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f1d92d32-90c8-396e-8212-fc6a6f638cd0 | -10.93422 | -56.83215 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d7ab6e1c-08c2-3508-8743-3d6e4ef7e89e | -14.02921 | -55.11988 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75ee9b8f-0e6f-322e-9ee0-b46ef58bc2b7 | -11.1461 | -53.93772 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 76eadc14-f9bd-348f-81dd-effb8a4d26d9 | -14.54969 | -47.06639 | 2025-06-17 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d183b323-4645-3c5d-ad77-8c1652c71589 | -19.43751 | -44.34168 | 2025-06-17 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 736bf543-bb94-3c85-b756-7729465a4a53 | -11.72222 | -47.74117 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1f07ea9-b4af-3bbc-b4e6-881088cb2f3a | -14.84746 | -52.28455 | 2025-06-17 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8991b79f-5979-3c24-82aa-7d4391a4d0af | -16.68239 | -43.88543 | 2025-06-17 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f83d295-0705-38a0-84dc-28d4780724be | -17.4409 | -52.93397 | 2025-06-17 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 049be08c-a594-3a1e-af6c-2d94c4de4546 | -11.40278 | -47.62849 | 2025-06-17 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f20a4e64-d45a-3942-b5db-c7e2d413a271 | -18.32347 | -49.88845 | 2025-06-17 04:10:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3b8660c-6910-3473-9881-4147e318cf77 | -12.23238 | -44.21671 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efb324f5-fd4a-379e-8fd7-4344e610b475 | -11.0817 | -55.06413 | 2025-06-17 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c62555ab-fc18-367c-9972-fefb7729965d | -11.13827 | -53.94582 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41f429b4-d5de-3035-970e-914d516ce305 | -15.37654 | -47.69866 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cbb4bb2-b114-395c-bf11-c126e3f2b114 | -15.07974 | -48.94338 | 2025-06-17 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ab354e7-64ec-3fc6-9eb3-dc9d706d7aa5 | -11.75747 | -46.71071 | 2025-06-17 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10048995-3857-3f87-8968-75e507e9c858 | -15.26281 | -51.47307 | 2025-06-17 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb395f5f-c50d-3b74-b63c-cbba49d23e38 | -14.02777 | -55.12634 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98f56958-5726-3444-b0ab-3c9d5a4be94d | -16.29471 | -52.93826 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9778defe-1347-3a00-a7b7-a7b9534800b3 | -16.30202 | -52.93913 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fbe26f3-b56a-3501-8446-35916296016e | -15.40233 | -47.83982 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e27e482d-5764-37af-a9a7-4ce563b6c5bb | -10.93117 | -56.84644 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f6481a5b-84ef-3512-add2-5cadbd8a5cb9 | -12.20707 | -49.62862 | 2025-06-17 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3364d958-534f-397c-99d9-2c170091cf97 | -13.36258 | -47.85177 | 2025-06-17 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bc3d7c9-ca4a-36eb-8cfb-c9237bd07465 | -12.23297 | -44.2131 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f906ec0-ec87-3da1-bbf4-bbbbfe6b035c | -11.72315 | -47.73589 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee25fa43-ea4c-3654-acba-41ff0719b7c1 | -19.71999 | -40.353 | 2025-06-17 04:10:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 65dd9427-0f86-34be-808f-6a88b8a5f883 | -16.29989 | -52.93905 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0dec4a0-fb3d-3b67-bc5c-983162e5471d | -19.4558 | -45.30688 | 2025-06-17 04:10:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fc6aa2b-9dbb-3587-ad1c-91049d1edeae | -14.23479 | -45.47367 | 2025-06-17 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97b8f5fc-6946-3ac3-861b-14fd231494b5 | -12.3465 | -49.31025 | 2025-06-17 04:10:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 72dd17b8-e60e-3b0b-b1e6-251ce92f5994 | -15.38937 | -47.84735 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c59a7c7-1187-3d64-8f7b-a3b66c97b03e | -11.46227 | -47.28402 | 2025-06-17 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973011e2-87a9-304a-a306-9aa5cdedc1c7 | -15.57084 | -47.85725 | 2025-06-17 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44534d98-a715-35c9-82c2-463d5ef5cc2c | -14.02876 | -55.12164 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5959e28a-b4ec-39e6-a1a6-65b25450d775 | -12.66144 | -54.11607 | 2025-06-17 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dfd560e-b8eb-31c5-b234-9306505037d4 | -19.71859 | -40.35539 | 2025-06-17 04:10:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2fccf3c5-1f64-37f3-a249-890104048c30 | -11.07639 | -55.05738 | 2025-06-17 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a73e6d60-4dd6-31be-a19b-b5510a6e614d | -10.93107 | -56.83048 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0cf51425-ba29-37fa-8fa8-71f96cd7214b | -12.20542 | -49.63773 | 2025-06-17 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b17f2962-0ecf-3376-a541-8766c36782b1 | -11.13919 | -53.9412 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bd924a7a-3c34-3940-a20b-784cd4ae3274 | -14.02729 | -55.12929 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 519535e1-dbb1-34fe-a7c4-c59dd7ab1c54 | -15.7502 | -46.7344 | 2025-06-17 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37ca6638-6f6c-380b-9089-60917203940d | -16.14295 | -45.95058 | 2025-06-17 04:10:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c872486-a1f8-3a92-96cb-8e51f0404d63 | -16.13953 | -45.94998 | 2025-06-17 04:10:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7606b5a-cbf1-35da-ab5b-824f2acffb90 | -18.13632 | -43.96218 | 2025-06-17 04:10:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4b69650-505a-37a2-9a05-c4d49bc5ed83 | -13.38775 | -48.46341 | 2025-06-17 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5271103a-0ec7-3bc2-820a-a908422efddd | -15.57327 | -55.65194 | 2025-06-17 04:10:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f50ef3f1-5d64-3b2b-8b92-3f0339c424d6 | -15.92891 | -43.9829 | 2025-06-17 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e248153-a87b-3d8a-be12-88c772f0d1f9 | -15.39856 | -47.83915 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 091a2f80-25b8-3adb-95aa-6d8a17e72dcb | -11.89218 | -47.46415 | 2025-06-17 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3008408b-8ac3-3a31-b2fb-2931dd01dee0 | -13.73441 | -45.24542 | 2025-06-17 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20342d63-4ba5-3876-8117-8239dfca6a33 | -17.44153 | -52.93087 | 2025-06-17 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c32a7b2-30f8-3c09-980e-686e75098feb | -19.51237 | -44.27621 | 2025-06-17 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bae122f8-09b9-3b0b-9d23-5d2419cce1d3 | -15.07911 | -48.9469 | 2025-06-17 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ea8796-73d1-395f-b19b-8de390ad39f2 | -14.86426 | -45.12804 | 2025-06-17 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6629fbb-8633-395e-b094-d1e78502c64a | -16.59103 | -45.87777 | 2025-06-17 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba7e29d0-789f-359b-9ba6-6c4620e0d214 | -14.03388 | -55.12763 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0d38050-37f7-307e-9446-e34b0a977dc0 | -12.21068 | -49.63404 | 2025-06-17 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed16c977-88c5-33d6-8b56-7e1da7fa7387 | -13.39179 | -48.46409 | 2025-06-17 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dc0ecf8-db5a-3f59-a81b-de6f1d94d630 | -16.30048 | -52.93606 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83cf4f18-1821-3064-948d-5eab1349cfe2 | -13.29124 | -57.07789 | 2025-06-17 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 309ea1b4-1625-3f1b-8ac1-9f046534dc16 | -13.29227 | -57.07768 | 2025-06-17 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40ab2413-a543-3446-af35-bc6e7c093048 | -15.39478 | -47.83854 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53d8d002-9d6b-364d-ab3a-e3223905df3d | -10.9381 | -56.83225 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7484a073-d9b9-37f0-b4fc-6dfef8f72f7b | -17.91311 | -45.53925 | 2025-06-17 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1c853a2-0169-35ca-8035-ef79fe5f9614 | -15.62431 | -46.46808 | 2025-06-17 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab27513a-bf3b-3457-9e11-77b9c858a818 | -11.72368 | -47.7393 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b150bd0-e32b-3c68-8983-0abae16c64b2 | -12.20624 | -49.63317 | 2025-06-17 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 654a34bb-89c6-35a3-af4f-092a7d2772ad | -10.93272 | -56.83915 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 11745f1a-aa1b-3cd6-a7e1-e24f75205855 | -14.82386 | -48.44951 | 2025-06-17 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8ddf496-4d62-30e6-a019-f8ca303cfe5a | -13.3884 | -48.45976 | 2025-06-17 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ec6619f-746e-334f-a765-121be76755a4 | -10.93434 | -55.32645 | 2025-06-17 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7b0cae9-16ab-3dea-b40d-5bea7a63707e | -12.65554 | -54.11492 | 2025-06-17 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af51d1d0-1358-368e-89c5-c786af26df16 | -11.40416 | -47.62649 | 2025-06-17 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 001204c7-6c98-3954-9a27-eec089c61bf5 | -14.03487 | -55.12292 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c536c1eb-6dcf-3eea-b860-b008804d4522 | -18.06278 | -48.89718 | 2025-06-17 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
