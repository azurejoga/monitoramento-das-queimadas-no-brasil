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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 086d40fa-5917-39b2-8a38-a4c5140eaca2 | -4.12942 | -43.08722 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eecc8b14-b955-3652-9566-3c096f3fb883 | -4.12887 | -43.09067 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54dd6891-fc1e-3a01-8aa9-e85faf862e6e | -4.12833 | -43.09413 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 212b28d3-44cf-3614-89ae-ac0f485b0ad0 | -4.12556 | -43.09015 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8daf5577-0dd5-3184-910f-83bffda4969f | -4.12502 | -43.09361 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12633430-0e02-3c25-a17a-7cf934098a4e | -4.04798 | -43.2376 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a3741f3-170d-3f02-9700-2e9db5ea150e | -4.04466 | -43.23708 | 2024-10-17 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd4415ef-de8c-35b5-adbd-9ca7d3771b80 | -4.04411 | -43.24054 | 2024-10-17 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce1ad58f-6265-33d9-9028-cc17aa5d21be | -4.04356 | -43.24401 | 2024-10-17 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e2d0a4-3506-3315-b5f9-3513a15fbb47 | -4.04025 | -43.24349 | 2024-10-17 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51f2c0f6-89f7-3017-bb31-0775d23caf80 | -3.8976 | -43.13543 | 2024-10-17 04:12:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88589c0a-2772-3b60-b067-3383b1bd1ed3 | -3.85635 | -43.24628 | 2024-10-17 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dd7c5bf-48ff-32dc-a17f-1166b3e1e248 | -3.773 | -43.94844 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d60194ad-c6e4-3945-a271-02c2ea25b4fd | -3.77074 | -43.96277 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ea331a5-7cc9-3703-8c59-b60c39739f87 | -3.76963 | -43.94791 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 961f7563-dd8c-3321-b2bc-77b198dcb7ce | -3.76907 | -43.95149 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 647abcdc-c46a-37bd-94a7-114842c48568 | -3.7685 | -43.95507 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a4b60e7-9f1f-311a-a667-596fcf89046f | -3.76737 | -43.96226 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 394a2f09-b68f-359e-923b-2f437ea211fd | -3.70433 | -43.79482 | 2024-10-17 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e37bb22f-c48b-354e-8f74-561520f74a22 | -5.03037 | -43.68526 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f853fd-6a37-3353-9873-49ce26bafc4c | -5.02419 | -43.66281 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f12b2e55-dc6c-3932-8d25-8ae445c3e0d2 | -5.02364 | -43.66631 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91581db0-9e24-35d5-a6c6-1bcf04ec9ec9 | -5.02086 | -43.66228 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7b3a2f50-7849-3225-9ca4-2a3be789a763 | -4.941 | -43.67121 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5eb9995-2f07-327c-a9de-a3b4fabb313b | -4.92703 | -43.78047 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca6edc98-6c00-3d83-b6b8-fa7319073cef | -4.92369 | -43.77995 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83b7b646-fc0d-3705-939a-8cd1440d17e5 | -4.79249 | -43.79147 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75e9fdd0-fd77-3fea-a7d1-15be1a005ccc | -4.7849 | -43.64997 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80e34d6e-8563-37a1-84b4-44da3163a546 | -5.67675 | -44.28407 | 2024-10-17 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 789f2bb0-aff8-351b-8ccf-153268701aa8 | -5.58251 | -44.87846 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 935a0880-e82f-3743-8c53-0700ea8d2715 | -5.5779 | -44.88538 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6bb68f0f-b67a-324b-b5ac-6ff71468b957 | -5.57388 | -44.88857 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c40d6bdb-7313-36af-bff5-3918fb8539ba | -5.57328 | -44.89233 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbfd41b-0954-3cd2-9c94-f266e7c43ff9 | -5.57105 | -44.88428 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 98ea24d0-79c4-3f85-898b-3821dc3cb174 | -5.57045 | -44.88802 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3da18b0b-fa27-3ba3-978d-d65700cd6dfc | -5.56926 | -44.89552 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1afd3e42-7172-3cc9-ba5c-b87ae9ce6385 | -5.56703 | -44.88749 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c07e558b-1942-3f85-9bc5-44271cdfd399 | -5.56583 | -44.89498 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ee6573c-770b-38c8-849d-4fceaa851543 | -5.5636 | -44.88696 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f6423be-dcb9-3135-84c1-39de253c03b6 | -5.56241 | -44.89443 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1fdfaa6-2b4a-310d-b7fc-cfce6056de62 | -5.42044 | -44.70884 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a21d0cff-606c-34ac-82a5-87a3ee89537b | -5.34427 | -44.52762 | 2024-10-17 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31247df3-54c5-3445-92b8-297d89951e46 | -5.23919 | -44.83256 | 2024-10-17 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2543f297-a7a2-3f7d-b638-7a6fc751ed82 | -6.05275 | -43.68964 | 2024-10-17 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d665a82a-b34c-3a74-afd0-1a4fb158815d | -5.73284 | -43.82149 | 2024-10-17 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5acbdaed-8dd2-31bd-b68e-67fd45394388 | -5.72009 | -43.77281 | 2024-10-17 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0a9b1b4-0c3a-3c3c-affa-6c1ce1e16a0f | -5.9789 | -44.00418 | 2024-10-17 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71600c1b-da0e-3537-ac54-fcf5523d29aa | -5.97834 | -44.00769 | 2024-10-17 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b0dadb8-9c98-362b-8b63-59cfc44b426b | -6.07317 | -43.6465 | 2024-10-17 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fa0f5a4-d40c-39cc-a6f9-009092bd9b96 | -5.72951 | -43.82096 | 2024-10-17 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b6c1500-277a-3f9c-b507-c45afb6291ae | -5.72618 | -43.82044 | 2024-10-17 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 861c8955-e7bd-3610-8ff9-68ce60acda0f | -5.72286 | -43.81992 | 2024-10-17 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 607d0c08-1499-321f-aad5-e085a384e5fd | -5.54513 | -43.91064 | 2024-10-17 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f494833-2ee4-37b3-a944-1d70e31872a8 | -5.54179 | -43.91012 | 2024-10-17 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 550e0a76-bf34-3273-8536-fcddd02f0991 | -5.54123 | -43.91363 | 2024-10-17 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebf3cca6-0a56-3499-bdb1-11a0904939e3 | -5.53845 | -43.9096 | 2024-10-17 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92261a1c-6e4d-33e7-898b-b4dc2a3c093d | -5.5074 | -43.69955 | 2024-10-17 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24a30fbb-460a-3e6a-bd23-b5a7d6a4ba95 | -5.50408 | -43.69902 | 2024-10-17 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 192c930f-806b-38b4-a5a4-6dd958da3bd8 | -5.40801 | -43.57674 | 2024-10-17 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 629d883e-f110-3a0f-959e-030876fc1504 | -5.40746 | -43.58021 | 2024-10-17 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c7e2cda-012f-344a-b409-860d2c8392d8 | -5.35007 | -43.62082 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf53c395-3d1a-3967-a145-41785aabe087 | -5.34384 | -43.48788 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a5f4a9e-c988-3ce7-8f6a-539814b2f2a0 | -5.33721 | -43.48684 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e578470f-b85e-38c5-b10a-e7a7b0ccab27 | -5.12367 | -43.76135 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dcd78fb-90bb-36f3-ab6e-a2fd66828cb5 | -5.53479 | -44.29845 | 2024-10-17 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7ec68ab-8415-376e-b770-48e786d48f48 | -5.5773 | -44.88913 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61e749ef-94c0-3369-8979-164d9115182e | -5.57447 | -44.88483 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 84016354-cd1c-367f-97a8-11f693ce232b | -5.56419 | -44.88324 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b74c8c32-03e6-3c69-af87-2d1f2b0c3da1 | -5.563 | -44.89069 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b128477-daa2-3798-84dd-e70a9f332f75 | -5.58192 | -44.8822 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aebeb289-a1d6-39f9-9d31-8b77a51380a1 | -5.56986 | -44.89177 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| cee860c6-8557-318d-818f-f3e83cbcffc7 | -5.56762 | -44.88376 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2509d6a2-2340-3561-95ba-ed62ad297b43 | -5.56643 | -44.89123 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a986259a-db8e-36c6-9c03-417e8273feeb | -5.19113 | -44.76008 | 2024-10-17 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 875b41f5-ef72-39a5-bd56-344e8378ccf0 | -7.60715 | -44.68189 | 2024-10-17 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f3fdbce-0b69-318a-b857-950708d0b09f | -7.42581 | -44.64943 | 2024-10-17 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af0b9867-4b3f-3258-ac77-60835203d629 | -7.19895 | -45.03709 | 2024-10-17 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c1fc7e0-9105-3fec-8fb4-d8073ea0295d | -6.91176 | -44.57081 | 2024-10-17 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a0d8e10-9c9d-3e2f-942d-9624deacd8e5 | -7.29069 | -43.94028 | 2024-10-17 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5238795-c9dc-31c3-a0c4-540548c6f7b8 | -6.57498 | -44.22901 | 2024-10-17 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35a8b98e-1a7d-3dd6-82b0-78a2365e2c8a | -7.77624 | -43.89985 | 2024-10-17 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 012ae926-700c-3bf8-9e88-a48166481de0 | -7.29401 | -43.94081 | 2024-10-17 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d8313e7-f106-36b0-b86e-f227c83e8289 | -6.96748 | -43.94197 | 2024-10-17 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e5e6f3e-2b7a-3767-8ba2-b35751574120 | -7.11949 | -44.07759 | 2024-10-17 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32608741-e45c-350c-a6e2-c175fbfa634e | -6.57832 | -44.22954 | 2024-10-17 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 780bff86-801f-33b1-8845-9f45ae8563c4 | -7.20235 | -45.03765 | 2024-10-17 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 814729ac-98ea-3e72-af1a-93b0ca395d7c | -7.19827 | -45.03802 | 2024-10-17 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 122bed22-891c-3b72-9e88-ce1209bbe8a3 | -7.86992 | -45.35598 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36b23a31-1ea6-31ed-a6a2-9b5a12f5acfc | -7.86711 | -45.3517 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1f1a1897-5434-3646-8efe-6d5c05b26169 | -7.86651 | -45.35542 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6ce6c8b5-5507-3e81-8019-d1b708324424 | -7.8653 | -45.36288 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a1275ed-bbdb-3837-ba16-74a8357ec7cc | -7.8647 | -45.36663 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68dd3290-efb4-34f3-84bf-7962178d2536 | -8.5026 | -45.45702 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 922a5db9-c785-3b9c-b354-52c46d2767f4 | -7.86811 | -45.3672 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b87af5df-79a2-35a5-880a-dd81ad407f13 | -7.86771 | -45.34798 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bfe54995-61c0-38b2-97a7-4d8e819a0733 | -7.86429 | -45.34742 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 06bf99d6-3cec-3526-8431-764d22c5858f | -7.86128 | -45.36607 | 2024-10-17 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17372b96-6a1c-37a4-a9f4-91ab98c023e1 | -8.89687 | -44.22528 | 2024-10-17 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5707ddfa-6e03-3e44-a9e0-c6d0d023a919 | -8.18446 | -44.11147 | 2024-10-17 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f542e5e4-54b3-3337-9870-359e35b97607 | -8.18778 | -44.11198 | 2024-10-17 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README28.md)
