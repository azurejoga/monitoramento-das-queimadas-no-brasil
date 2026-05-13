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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acc63a35-4846-3ef8-a8d5-dd34c3fba35e | -10.40347 | -46.65604 | 2026-05-13 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ab5f11e-6826-32cf-b885-a6868d86c2e5 | -11.93724 | -43.37721 | 2026-05-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e338bf-94c3-3231-ac44-2c47f8d59909 | -14.30519 | -49.24858 | 2026-05-13 04:21:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d2c0ea-4bfa-3638-aab6-ffa1ff9849a4 | -15.38476 | -43.76019 | 2026-05-13 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0a83544-50a9-316c-91ef-3db1ffee65c7 | -12.62273 | -44.51699 | 2026-05-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f42a5bc9-9e37-32f4-ad8b-908ef4bae7b9 | -9.4518 | -47.79158 | 2026-05-13 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e31b3bc-4671-35c0-bc19-c6b307999bb8 | -14.1288 | -45.3172 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b482c02a-9320-350d-bff5-b42740c45d7a | -13.03042 | -49.94199 | 2026-05-13 04:21:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19ea3f15-1fa5-3892-b615-daeab224c716 | -11.63115 | -54.15761 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0a0bbcd-af1d-3a8d-a084-462f9077d64d | -11.92679 | -54.10139 | 2026-05-13 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d589078b-e1b1-3c06-9cdb-e2e246d1cc3f | -14.14512 | -45.41212 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b3602f2-5e1a-3260-a4f6-6522d986bc76 | -14.12213 | -45.31614 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 233fa391-5420-3382-9eb6-498cd3957117 | -14.1188 | -45.3156 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96f2bd5c-9f32-357e-b277-7bd4542e7d78 | -12.62218 | -44.52066 | 2026-05-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f525f6c4-0eeb-35c1-9848-d8b4a14a9603 | -10.41235 | -46.77178 | 2026-05-13 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bfeb910-0091-35ed-b83c-4916e36656bb | -14.70499 | -43.21186 | 2026-05-13 04:21:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca0cdb2b-d0b7-3bee-a67a-d8a35bbae011 | -12.05383 | -45.28803 | 2026-05-13 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ededb830-a404-33dc-92f3-43b71a77fcde | -11.18403 | -55.92501 | 2026-05-13 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| bd542333-2218-3fc2-876f-0296d8af7de3 | -11.97268 | -46.78398 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d189b32-875e-3eb5-967a-14931da0ea6f | -12.858 | -43.75834 | 2026-05-13 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebbb089a-b31f-34c7-b486-495e8515b30e | -14.11825 | -45.31921 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ea6c831-0aba-3655-8d99-e687f6a0a633 | -8.74349 | -48.75254 | 2026-05-13 04:21:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 450e93f5-34f2-3ca2-928c-67fe1f3f7d65 | -10.61772 | -47.95759 | 2026-05-13 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d7d884a-292a-353c-bcc2-3123f3d5bc15 | -12.62555 | -44.52118 | 2026-05-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5a3be70-f427-3df8-878b-2b4613cef30d | -8.09158 | -44.17481 | 2026-05-13 04:21:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07a03ea0-322d-3f07-8595-5b223adcdd05 | -10.26683 | -38.1442 | 2026-05-13 04:21:00 | NOAA-21 | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f695e322-9b38-3084-9c5f-63cd922259c1 | -9.73046 | -48.54753 | 2026-05-13 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 064e6043-8119-3e3c-940b-3db8adb68e6e | -11.63556 | -54.16163 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa9eb290-c8c4-30eb-b854-f44ac70c853d | -13.65049 | -47.92947 | 2026-05-13 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7339611-7536-3d50-a9e3-5e0b94541ea5 | -14.14622 | -45.40491 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a50157c7-b7b4-3f1b-97fc-5c65f3f4f750 | -11.739 | -54.24444 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4219668-af41-343f-bd1c-1aec1afb5d66 | -11.93068 | -54.1008 | 2026-05-13 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5229a57f-0332-30f5-ac47-e9e26b3e1804 | -11.97922 | -44.36906 | 2026-05-13 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95d37dd2-3ac0-3076-93f0-df2cf7f794e7 | -11.73955 | -54.2415 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b799f861-e7bf-3b76-8601-f0fcbb7cad0a | -14.15958 | -45.42917 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c58cb064-9c39-3847-a123-91eb280c6cab | -14.11212 | -45.31453 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1756e7ab-a619-3614-8879-568fd7980012 | -10.12822 | -47.9152 | 2026-05-13 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05411042-1f9c-3706-8679-a5d4ba247e27 | -10.40405 | -46.65244 | 2026-05-13 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befe4d5b-1b43-3b35-ab93-969bde81a842 | -11.06256 | -52.45308 | 2026-05-13 04:21:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b219ef2-5716-38a9-b7a8-f4ca9d504b47 | -11.93667 | -43.3811 | 2026-05-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c93c8c1a-8415-39db-889d-d9536c327bd7 | -11.6361 | -54.15873 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94a522c6-7cc4-3067-bd20-408aea4af3d4 | -8.45283 | -49.57228 | 2026-05-13 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4877cd2-706a-30f4-8d82-df2802ca4f77 | -8.54111 | -45.97984 | 2026-05-13 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71588230-ece0-387c-be07-4764c54c6b90 | -11.40989 | -48.44386 | 2026-05-13 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e5b3e51-2764-3c3d-b73f-ab79110d623a | -14.15625 | -45.42864 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbdf3da2-7bb7-3ace-b0f5-bc11053bc832 | -11.93172 | -54.10238 | 2026-05-13 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2069c1e1-cdf0-310b-9051-af98194b5072 | -14.16291 | -45.4297 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70da2675-21cb-30e2-bd45-5959ff7d4917 | -7.63121 | -48.02488 | 2026-05-13 04:21:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3c9f783-1554-3cd5-a622-59cdc4fba779 | -10.48566 | -49.36312 | 2026-05-13 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 34d61ee9-ed33-3e62-830a-f9e1ac7f500e | -11.67262 | -49.00141 | 2026-05-13 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20ded0d4-4c04-3f50-b563-bf2d84882dfd | -12.11425 | -43.64911 | 2026-05-13 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6aab4061-510e-320a-b10d-f1bf090b6714 | -11.98267 | -46.78563 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e163a5d-661a-35f6-8ffa-709602372fed | -11.79844 | -43.63033 | 2026-05-13 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81b1aff2-d7c8-3d97-bb47-336843e6f5c8 | -11.96935 | -46.78344 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e90d4909-6557-33e2-a59a-811a17d48764 | -11.97601 | -46.78453 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e34544dd-c0f2-3afa-8133-332d8dd20b20 | -11.4035 | -48.43866 | 2026-05-13 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e293966-2797-3389-9f58-4aab84763ee4 | -10.12759 | -47.91908 | 2026-05-13 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91e6cb8a-8aa3-36ef-9022-2e41704839ab | -10.66151 | -49.70857 | 2026-05-13 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c444197-eab8-3103-adf1-39e50594633a | -10.12695 | -47.92297 | 2026-05-13 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3136b141-2930-3863-99e9-60d998474218 | -8.70458 | -47.98404 | 2026-05-13 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48dcc31e-e8e0-3719-b652-54e7fd85d649 | -12.59506 | -44.06827 | 2026-05-13 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7496e0d-44ec-3b79-a691-0fb3583e8d90 | -8.54312 | -45.98726 | 2026-05-13 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 90bed0ea-62ff-306f-ad4d-10fa3b554b55 | -11.96879 | -46.787 | 2026-05-13 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c54709b-e861-3c33-9f0a-0cc8313899f7 | -11.80804 | -52.51748 | 2026-05-13 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 942b85e0-baf7-34e4-aa54-03bc670c37a9 | -13.68608 | -44.2927 | 2026-05-13 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6807ab38-f01c-3156-af27-f1ac911d5d67 | -14.12322 | -45.30891 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30eb0915-fac9-3abb-bfdd-d280becf9aca | -10.97215 | -45.09457 | 2026-05-13 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d05b3dd4-31eb-34f7-abe7-5d14f216dd32 | -10.66141 | -49.70634 | 2026-05-13 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e907e85f-ffa8-35bf-9ceb-b01802c3f4e3 | -11.45213 | -39.28522 | 2026-05-13 04:21:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c52f2b02-26fc-3871-927f-08680577734e | -10.66521 | -49.70699 | 2026-05-13 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13230680-ef25-335f-9356-c247726af045 | -11.44714 | -39.28891 | 2026-05-13 04:21:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e07b84b8-3eb3-38f8-9e7a-a4be7ba9766a | -13.36885 | -43.20473 | 2026-05-13 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc31e277-8695-3daf-b611-6de2d6496170 | -14.13031 | -47.39915 | 2026-05-13 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c114739-b06b-3bfb-8902-233ba7bb0acf | -10.11314 | -49.17982 | 2026-05-13 04:21:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d14c36d-17bb-307c-889a-341484503266 | -14.12656 | -45.30944 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8055869e-7069-3377-a8d9-3ba11ba7f9d5 | -11.734 | -54.24344 | 2026-05-13 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c45400-d5df-3da8-a36a-613f4dc16bb7 | -12.13581 | -39.40651 | 2026-05-13 04:21:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e3c21f37-a4ac-35c4-be8e-df1bcb568d46 | -14.14677 | -45.40131 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea056dc-cc7f-3345-adad-21885f4cc6c3 | -14.1396 | -45.42599 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aed4b5b-7bef-3006-afae-18c5b571f034 | -8.08825 | -44.17429 | 2026-05-13 04:21:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f032bff7-b6ce-3fe2-a82a-a5003eef09da | -8.54368 | -45.98373 | 2026-05-13 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 763fb31c-54c9-3a94-a940-642e9152f17a | -9.45942 | -47.78883 | 2026-05-13 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 139b39d8-5148-3105-b69c-f57af48538be | -13.58429 | -47.40912 | 2026-05-13 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ef8f070-aa81-3f2a-9356-b9a1cb937375 | -10.40682 | -46.65657 | 2026-05-13 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a727f48-d261-3cd7-9455-93ea4be6b6c0 | -12.6261 | -44.51751 | 2026-05-13 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3b46cde-ad96-3719-9ae5-8c6c1a4bac8e | -14.13323 | -45.3105 | 2026-05-13 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c7452d2-2877-3317-a077-dab7491a7792 | -9.45529 | -47.79213 | 2026-05-13 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b79da85c-5f78-3a89-8226-e6eab3b2cc33 | -16.42602 | -52.79568 | 2026-05-13 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f30016da-4fe3-3bb7-b40c-ded16379b6ef | -21.33529 | -47.02322 | 2026-05-13 04:23:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b488546-42f4-36a4-8fb3-150e5d1e13cf | -19.19834 | -49.12889 | 2026-05-13 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5399b55-7e86-3a4f-9670-7144c90b28e2 | -18.3698 | -48.56961 | 2026-05-13 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b70bd255-1a03-388e-8cf4-2334e43ed352 | -19.20234 | -49.12571 | 2026-05-13 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8217818f-7f13-3abc-82b3-8b91218b662d | -16.42519 | -52.79641 | 2026-05-13 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d964af72-adbc-324a-936d-da3d95d77924 | -18.74017 | -49.09439 | 2026-05-13 04:23:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9677b8fb-2715-3f6d-bb72-f25f7c7fa4fc | -18.37311 | -49.2706 | 2026-05-13 04:23:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 230cf37d-3d5d-36bc-b2e1-e45cd3fb88ff | -17.534 | -45.31659 | 2026-05-13 04:23:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f307f1ff-131a-3c78-ae56-4a4b15b428b8 | -18.36585 | -48.57272 | 2026-05-13 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 31f1c40e-411e-3367-a28b-3d89935d6f36 | -16.46579 | -49.12854 | 2026-05-13 04:23:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 736a2c14-0e38-3e42-a485-d76680c08875 | -21.33417 | -47.03076 | 2026-05-13 04:23:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4f88d01f-18ac-38b2-bb90-f552bccefc1b | -21.33473 | -47.02699 | 2026-05-13 04:23:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README4.md)
