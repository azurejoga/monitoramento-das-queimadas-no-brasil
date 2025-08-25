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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 352ba2bd-2cb8-3879-a30b-ad075ba96721 | -20.37117 | -46.77322 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 701138dc-b626-3daf-87c1-7a8fb25be3b1 | -12.94361 | -46.31414 | 2025-08-25 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47f800a3-d195-3fb0-ad51-69d0e124b599 | -11.28806 | -44.96817 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33cfca0a-07ed-32fd-8cc1-9bbdb09c4545 | -21.6356 | -44.01867 | 2025-08-25 04:17:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e09cb7fb-7f4e-3268-b8a9-9ef977d92ce1 | -14.73704 | -55.9276 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1acdb674-b20f-3d82-a9cc-234a063dc461 | -12.7368 | -48.13726 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17cc9d90-c932-3ea4-a0dd-6663ed098bfb | -13.48598 | -46.88544 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a8195fd-3d6b-3286-ab33-f56e341b0fc8 | -20.34839 | -46.72358 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cee9bd49-7d3e-3af8-b19e-10d8ab004122 | -14.72336 | -55.9324 | 2025-08-25 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 869f44f5-4106-3562-8aca-2571743257d0 | -14.12487 | -53.99944 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dddbb932-c45f-3426-a6cf-dac76e98e1f8 | -11.27806 | -44.98827 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 068d9dba-11fe-3dbd-bc14-e49e7fe68bb2 | -13.15587 | -53.73555 | 2025-08-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71a7b69a-8245-36d9-920e-295781022a6b | -11.20193 | -55.04354 | 2025-08-25 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8d71d84-d29d-3b55-9924-c33208cf72df | -12.73543 | -48.1016 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc64b25-8124-3f50-8df6-8ec4834460de | -20.36457 | -46.77203 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1c2dc16-e59a-38ad-a5a9-c8ec08c3b9ef | -15.0463 | -48.67859 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c38fe238-7b93-36f8-8a5d-2f2d30eccb16 | -11.04896 | -49.11766 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a11b6044-05f1-3073-834e-ab1c58abdfa0 | -20.37466 | -46.75119 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbc0f6f-1e12-3c8b-a32c-5f2a28f6ed49 | -10.79641 | -46.42131 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 244258b1-1024-3a26-9699-ed9c5f47d2ef | -20.61977 | -45.02396 | 2025-08-25 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c39e77e6-2448-3459-9f39-3d7ec6dc3915 | -11.60195 | -46.35174 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 196e9c77-0057-34a2-aa9c-d2f036610e1c | -20.61856 | -45.0239 | 2025-08-25 04:17:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e28f6ac0-4285-3d4e-b05f-4b5d1e93806c | -20.93082 | -46.84822 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c93fc6d-c14c-382c-8866-f960c5defbfb | -15.08317 | -48.72542 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c55005-5882-33df-b350-09ff48330f9d | -13.47001 | -46.87548 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7042d41-5fa8-38a6-8722-a437010e3bc7 | -11.27029 | -44.97258 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 638301c8-0dec-3d57-9776-9c467816f1b1 | -20.38242 | -46.74504 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7683c82c-9a64-33d7-b613-39421c09efbc | -20.37679 | -46.75913 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f5f28d7-78d0-37f9-8e18-91bbe5875cdb | -11.86329 | -45.11684 | 2025-08-25 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79a5bf98-259c-3b9d-8fb0-d08f05d1f0a3 | -13.4782 | -47.01728 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9c6a9df-1b09-3fde-8bd4-016bf93d099b | -14.26086 | -48.0447 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7ff13163-bb45-3ae5-9f09-77c7f1b7dabd | -14.09913 | -53.99463 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cc292846-cffc-3bb3-8ce3-9c6a153d1cde | -12.73909 | -48.1021 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f0b55a8-5703-3f46-8544-e787cc0dbc7e | -21.59301 | -43.90963 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2c3ed37-8bcb-306e-9d79-454fc5f8dcdd | -11.11289 | -44.78505 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a84b599-4824-3534-9297-489b66b3fd61 | -13.83584 | -46.7046 | 2025-08-25 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f24bceb-0c51-374d-868b-284ec59ec521 | -14.78508 | -47.93305 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1021f406-d894-34db-83ae-c3011a0e44c6 | -19.94621 | -50.44416 | 2025-08-25 04:17:00 | NOAA-21 | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6f0a8738-a3db-3112-9e4f-c82fa9d6e813 | -19.93511 | -47.49693 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7ac0e21-12f6-3bc2-90b7-6eea219d380d | -20.39076 | -46.73523 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3cae077d-4d9a-34a4-b372-e35a657cc0e9 | -13.45695 | -47.01759 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cde6939f-bb32-352e-bb13-7f4278a664ea | -11.8688 | -45.12495 | 2025-08-25 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 862d6639-84dc-3049-89af-2700dc0eb68e | -14.81724 | -47.91368 | 2025-08-25 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41f4826c-fac4-3193-aa6a-50a83ea5e5dc | -14.25874 | -48.04087 | 2025-08-25 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a2c57145-3c11-3b27-925e-68fa36cba70a | -19.94818 | -47.47997 | 2025-08-25 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34f3f9fe-193b-3ac6-90ec-b98392f664a3 | -10.02467 | -51.07077 | 2025-08-25 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 066c72e7-d8c5-3e6a-88dc-a4152755f46a | -11.10903 | -44.78803 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62564ce7-7383-3d5c-83b3-2673118966a1 | -13.5108 | -46.90546 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6923655b-b6a9-3a6c-a2fb-d8b5eeb7f74f | -11.33813 | -47.85299 | 2025-08-25 04:17:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c31aa670-2618-3f55-8e1e-ba76ed84c639 | -20.38068 | -46.75606 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ba11f5a-5c67-39fb-95c5-f52ba28373f1 | -11.17628 | -55.02113 | 2025-08-25 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70fc0aec-e959-3add-9050-859f8a88a9cd | -12.41821 | -46.4945 | 2025-08-25 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 505d89e9-3476-3a47-b05c-c13ff73371bf | -20.36938 | -46.72009 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a28f8b11-0697-32a2-a27f-c1c44ca5d367 | -14.65346 | -44.07443 | 2025-08-25 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f80f161-5036-3abb-a3fe-99dee38ee820 | -20.36515 | -46.76835 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4908780c-572c-3225-9108-ef5e139f179c | -14.42787 | -56.46986 | 2025-08-25 04:17:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd24eacf-a7f9-3bd1-8696-ca7fa46933eb | -13.45824 | -46.90456 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be4491fd-7ad0-3c89-92f1-d74779b7781d | -12.73312 | -48.13682 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ced63b0-389d-3c78-8613-88032d60bfe7 | -21.12277 | -48.9171 | 2025-08-25 04:17:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3512fd51-d72b-3b00-b3c6-ddb47c1e0672 | -13.34758 | -54.39078 | 2025-08-25 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ea416a0-1f83-356d-87d8-b87bc914c6db | -22.01364 | -42.09 | 2025-08-25 04:17:00 | NOAA-21 | SANTA MARIA MADALENA | RIO DE JANEIRO | Brasil | 3304607 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a860be70-481b-3426-bf47-42322911dbac | -11.48789 | -42.94802 | 2025-08-25 04:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 481804a4-486a-31ee-8b9a-267866070daa | -12.74058 | -48.11525 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bbfc6b23-2d5d-3686-8928-62a401881ca3 | -15.03734 | -48.50778 | 2025-08-25 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cccc2bb3-42ed-30ca-9e33-8b4c8d58b522 | -11.15376 | -44.69814 | 2025-08-25 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b331f211-5e4c-3bf3-a9df-83cdbcd19787 | -14.77444 | -45.37952 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdac634e-4e5a-3f20-ae58-207083bb5c41 | -13.49902 | -46.89164 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 399a4b96-70eb-3d59-8887-b8c07a186243 | -12.75438 | -48.122 | 2025-08-25 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b128df4-24fc-352e-bcb4-c011c42b735e | -11.60104 | -46.33605 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdae4f24-e9ca-3b35-8bc3-150eb7e77900 | -11.64292 | -46.20877 | 2025-08-25 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95b6d823-2091-326f-9e53-9f895c991cc3 | -15.14345 | -48.64015 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8adf5c9e-23b3-3fe1-8bcb-c96b313ae825 | -10.70886 | -48.31675 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7863353-08ee-339a-a711-33cb8d378d38 | -10.70967 | -48.31187 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec8301e2-ad19-3190-8f62-0c434de4bf88 | -15.08697 | -48.68135 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d89cc9a6-764f-3950-94cb-3ed8b27672c6 | -15.14858 | -48.63211 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da4cd146-a848-35e1-8da6-d371c99a8087 | -13.67101 | -47.96817 | 2025-08-25 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fae63d21-c88a-3a98-8dbf-5d5c170c72f4 | -10.81345 | -46.38159 | 2025-08-25 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fba4d935-5001-3b2d-babf-ddb08ff14be1 | -9.57742 | -55.37256 | 2025-08-25 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63e6a6cd-0ea5-3764-a7e0-b02258eeffa6 | -14.92497 | -45.54714 | 2025-08-25 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5916d37e-13d5-3112-8bf0-ecd18de9adc4 | -13.45025 | -46.91033 | 2025-08-25 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cdc4e8-c3fa-30ec-b9fa-fb906a8b48a7 | -21.42282 | -47.6022 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3519f09-fee4-3828-9a06-92d215c61c3b | -14.38946 | -51.95438 | 2025-08-25 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db13130b-03b7-3931-b6a6-84e01d9e19d8 | -13.65385 | -46.89013 | 2025-08-25 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0799711c-a65b-3b8b-b812-21214d9908f0 | -15.04779 | -48.66999 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0ea5cd5-9eb4-381c-acd4-dff03bcaff27 | -20.35773 | -46.72898 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5809d09a-e0aa-31ee-a475-ed1ef0e7aa6d | -10.71342 | -48.3127 | 2025-08-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8abd5e2-2a64-3ecf-91ad-7e0bf11793d7 | -22.69141 | -47.35197 | 2025-08-25 04:17:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7617c933-2d74-3751-afd0-44584f61124f | -19.71466 | -49.12965 | 2025-08-25 04:17:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 059aaffc-67a2-3b0e-af43-d1df616b8826 | -21.72558 | -46.81043 | 2025-08-25 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7c2f5d43-8aed-3ae0-8d19-52e2dc831529 | -20.3801 | -46.75973 | 2025-08-25 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a73da137-8e44-30af-ba38-9fbe9f638b73 | -14.26858 | -58.61438 | 2025-08-25 04:17:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be1281e8-7906-3bbe-beb0-40c87b9e7600 | -10.70876 | -47.13595 | 2025-08-25 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85fa3956-c4f4-3b4d-993d-f944d4c4f797 | -21.32258 | -48.67232 | 2025-08-25 04:17:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ae4bbea-5466-3b67-9a89-750f86bdd19a | -15.11543 | -48.6459 | 2025-08-25 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c77a1984-5520-31e2-9922-a56574b3f803 | -15.63751 | -52.72 | 2025-08-25 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 156da778-2619-30fc-be10-e414e23f6d8e | -13.14949 | -53.7409 | 2025-08-25 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b43332e6-8600-300a-9168-a98981ea63d9 | -20.9836 | -45.48854 | 2025-08-25 04:17:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4f27b90-8733-3f01-8bca-b0c2ed9df75d | -9.68981 | -48.34114 | 2025-08-25 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed7e9a1d-1190-37f7-a39d-e296e8afa502 | -11.13681 | -46.33672 | 2025-08-25 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c89babf-1440-307d-94b7-196f88b1380c | -11.67142 | -51.58269 | 2025-08-25 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
