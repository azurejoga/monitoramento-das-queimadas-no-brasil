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
| d908d13d-57ab-3c59-afd7-85f1a99c3686 | -15.15931 | -41.29648 | 2026-04-23 03:10:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ce861ca-795e-33f2-98be-e4c5b4b0d2a1 | -8.7853 | -44.8311 | 2026-04-23 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7f14440-1a3d-3f88-8d8a-6bc485198fe3 | -6.03927 | -44.23327 | 2026-04-23 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf67179a-a895-3179-ae8c-4fdc3e51a8d2 | -6.04129 | -44.23368 | 2026-04-23 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68d3b58-7573-3207-ba9c-5ae4ba3c61bc | -17.48478 | -42.21809 | 2026-04-23 03:57:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cf58b5f0-6aac-379a-8b8f-b8008a888217 | -13.38628 | -45.3252 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0027f6b3-8294-3a9d-9ddf-701835c6685a | -11.79532 | -43.62353 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| daada4b8-aa7d-317d-96ae-eb8842a3f974 | -11.77755 | -43.65931 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c5ab212-7546-36a6-949a-e75214d9f170 | -11.77675 | -43.66403 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c885a2f7-5b40-39b4-bff7-a8d00caab59f | -12.57055 | -45.474 | 2026-04-23 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eac70536-c09a-38e6-b8d9-2aff9dad81a8 | -15.15966 | -41.28968 | 2026-04-23 03:57:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 295cc4ea-efe5-3e53-bd59-7e3ca9f7e8ac | -12.24058 | -44.18515 | 2026-04-23 03:57:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf729dfd-dc2a-3020-88ba-d13898edd187 | -11.77154 | -43.64856 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4c015c9-0d77-350d-aab3-24a85519b81f | -11.9768 | -43.83832 | 2026-04-23 03:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14ebbe44-1767-32d2-8864-ba18976d61a4 | -11.79072 | -43.62761 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ac1a53e-7d91-3868-b5e7-a4818f917cb1 | -13.38285 | -45.32067 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 170df89b-8a69-3ed6-be2d-d4b6d09ac4c9 | -11.79152 | -43.62289 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48115a56-668e-3d79-a56d-a66b2d7f8d1d | -11.77074 | -43.65329 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b071867-c44f-3c58-9284-cb41dccf2c30 | -12.27961 | -44.61663 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bafaee82-a436-395e-9346-ceec69adb9d2 | -12.5844 | -45.47174 | 2026-04-23 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1e56c8e-ed4e-3121-a86a-1870d6774705 | -17.48669 | -51.08683 | 2026-04-23 03:57:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac8b5e6a-7f98-3a2e-a8e7-899487cc3aa0 | -12.2784 | -44.6237 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 428579b8-7a60-3ef8-8ac3-cf1ba4ee56c1 | -13.37875 | -45.31992 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9393babd-6075-30bf-b79f-ca02b88b1131 | -17.48586 | -51.09072 | 2026-04-23 03:57:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4db1599c-c00f-3e52-9442-292f0865b13f | -13.02736 | -43.58722 | 2026-04-23 03:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd6e8fcb-8272-381c-b08c-a933bea711ac | -13.38149 | -45.32822 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e16d299a-8e25-3ee4-9a6c-6f4aa5488799 | -11.78136 | -43.65993 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afcea1d8-d0c1-3dbb-8b2f-558e77182c39 | -11.76853 | -43.64319 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e48b88a5-4cf4-3142-a174-0bccd1aa11d5 | -12.5886 | -45.47253 | 2026-04-23 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7667e78c-f750-386b-bae7-91683ef07a3e | -12.28388 | -44.62577 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b583725-3b59-3fb8-895a-ad045dcd866b | -11.76693 | -43.65264 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39f6ccf2-5519-3298-898d-7366b59a07cc | -11.76393 | -43.64727 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3465d06a-3db0-3351-919e-7306c0a156bd | -12.283 | -44.62091 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 412638c3-0382-3f7c-b693-5d37ef85ac81 | -11.97598 | -43.84314 | 2026-04-23 03:57:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8420653-8178-3c97-92b9-962a39ee830c | -17.48122 | -51.09026 | 2026-04-23 03:57:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5830222b-d500-3d5b-8830-b1359a2cbd58 | -12.28451 | -44.62222 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb0ca98c-3928-3536-81e8-5cca283609b5 | -16.64898 | -41.14847 | 2026-04-23 03:57:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 541f5695-d029-311c-8251-ba0238eb03e9 | -17.88754 | -40.35723 | 2026-04-23 03:57:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b5c1ee4-b45d-3d61-8bb0-7ad783471f51 | -17.16873 | -46.83477 | 2026-04-23 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b104d2d-ded9-3d39-98a0-f03c81a527d8 | -16.43051 | -54.91543 | 2026-04-23 03:57:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6d2fbba-363a-378a-b7f2-b771c29f8d3b | -14.09953 | -47.21093 | 2026-04-23 03:57:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4835ddcc-613a-31df-abed-671e322055fc | -17.89981 | -42.86148 | 2026-04-23 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03251fc2-05f2-3352-baa6-814fb57b6da3 | -11.79231 | -43.61817 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 526c7212-54f1-3a55-80fd-b5df46c82ea4 | -12.0537 | -45.34507 | 2026-04-23 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daaccf5e-4f29-30db-89de-584400b3c97a | -11.79611 | -43.61882 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44c07ef2-3ff9-3fec-9ca3-78da8f7c6fe5 | -13.37806 | -45.32369 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea41c45c-186a-3f64-9e6c-0cdf2c77b7a4 | -11.77374 | -43.65866 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88e0d176-7566-3508-8be6-f9f23f241b9a | -17.48502 | -51.09464 | 2026-04-23 03:57:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f619d6d-a157-3981-822c-6fed6a6a4236 | -18.30971 | -40.01367 | 2026-04-23 03:57:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 88d7ffa0-add4-3e7b-a71c-2ed1eb027e5b | -12.28514 | -44.61869 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb69f05a-2c06-37a3-8898-95cfce731672 | -14.90352 | -45.17941 | 2026-04-23 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1424081c-1cde-336c-9d98-b4cdc5b87301 | -11.76473 | -43.64254 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a1836ec-14e8-3933-996b-f681fee1f0f4 | -11.78472 | -43.61686 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 660f24cd-801a-393e-813f-a3021e0cbcb5 | -14.09915 | -47.20961 | 2026-04-23 03:57:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fef8f12-ad3a-3374-9d24-ea8f60374410 | -13.38696 | -45.32143 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b76fd5a8-4f76-370c-a674-ab12e51d3573 | -18.02888 | -42.3798 | 2026-04-23 03:57:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8fd1bdcc-55ee-3c70-a382-1306c0d804f7 | -11.78056 | -43.66466 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9664162a-87b7-37c2-94b9-794b2edf6d76 | -13.37815 | -40.04276 | 2026-04-23 03:57:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 75bb103f-6f32-308f-bf0c-86b2a97257f2 | -17.48203 | -51.08633 | 2026-04-23 03:57:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76f4fbc8-8b2d-30c7-b080-7cb88524abea | -11.76773 | -43.64791 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e5801a2-8fde-31af-9964-05f256bace87 | -18.89 | -39.92537 | 2026-04-23 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc73207d-feef-323b-97e2-ec12ede96961 | -16.42591 | -54.92286 | 2026-04-23 03:57:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f69f2bd4-15a1-315a-9248-7dedab9482f3 | -18.88944 | -39.92911 | 2026-04-23 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7916b4f3-05b5-37b5-9279-b1a2840e5923 | -17.48142 | -42.21749 | 2026-04-23 03:57:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b233716b-8f78-3d98-9821-813c7b90f521 | -12.2824 | -44.62446 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cdbd4ea7-1736-3297-9c75-79df8813853c | -16.709 | -44.95264 | 2026-04-23 03:57:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed7fc033-c661-3a8f-abe1-7a312a743bb7 | -11.06007 | -49.49929 | 2026-04-23 03:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b7323b-588c-333b-beb7-1001d0c68eff | -15.6725 | -39.80157 | 2026-04-23 03:57:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13511f33-1375-3dbe-9967-e8da44111b99 | -12.28361 | -44.61739 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e45c280-ce70-327b-97fa-3521a968d989 | -12.57037 | -45.47726 | 2026-04-23 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3129a6f1-f1be-32cf-9082-2523cffb19d6 | -15.95834 | -39.10229 | 2026-04-23 03:57:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d82e550-d3d6-31a3-9893-4fcff91fc530 | -12.27901 | -44.62016 | 2026-04-23 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c47e2e21-471d-3678-9014-21486e5ae2ef | -11.79311 | -43.61346 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93ef723d-d9f5-3484-944e-630b53cc12c5 | -12.58512 | -45.4678 | 2026-04-23 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31e8dec5-035e-3aa9-ac15-51994123dc8a | -11.78392 | -43.62158 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5ce71dc-4aeb-3419-82ec-a24544edec1a | -16.42773 | -54.91504 | 2026-04-23 03:57:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39058d14-b990-3ecb-a2d5-333530e62021 | -18.63332 | -40.18731 | 2026-04-23 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc267b85-e040-321a-bcf5-7e341bfb7087 | -11.77234 | -43.64383 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc22710a-23c7-3061-9c25-1caefc0d3d9e | -12.05409 | -45.34439 | 2026-04-23 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1224b2a2-31dd-3dca-aeb4-b6a88c50a3e9 | -13.3856 | -45.32898 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4099219-c9d3-3a31-8b35-a58d5ba2731b | -12.56985 | -45.47797 | 2026-04-23 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 114e4276-2f1e-3cbf-b962-e3414b2635da | -16.42878 | -54.92308 | 2026-04-23 03:57:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e328857-9e39-3139-be59-409d0d6e1091 | -11.78852 | -43.61752 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 088aec84-c37d-3465-98d9-42f033fc0eda | -11.78772 | -43.62223 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e625b6f7-91ec-37d4-b614-432528c1e91f | -15.36787 | -41.68977 | 2026-04-23 03:57:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7c1f17d4-133b-3cf9-84c4-51460e10cde8 | -11.77534 | -43.6492 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2ff8c2d-f9b6-3268-993d-875924c41899 | -11.78517 | -43.66055 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66ccdc73-df88-3963-8683-213f088888e3 | -11.98868 | -47.11681 | 2026-04-23 03:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70fdbbd8-8d9b-3e37-9cf1-4cf405b96b68 | -11.77454 | -43.65393 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42d80efa-06dd-3459-895e-941ffa875dbc | -11.77314 | -43.63911 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc874bd5-598f-389e-9c78-694b18ace955 | -11.78931 | -43.6128 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fff2554f-874c-32a1-8782-7b60e0b9e326 | -11.76994 | -43.65802 | 2026-04-23 03:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee7cd36f-ab14-3e72-ac01-ea88ebea59f1 | -13.38217 | -45.32445 | 2026-04-23 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06f16c64-6a3f-37c8-84b3-6a4cac45a8c6 | -15.15907 | -41.29333 | 2026-04-23 03:57:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aba17585-34be-3353-9364-b55d2b693e26 | -19.69115 | -51.34185 | 2026-04-23 04:00:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b195bf1-a00d-3218-8730-c6dbaf088b73 | -20.19017 | -46.91151 | 2026-04-23 04:00:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b2dfcbf-5843-379e-93fb-cd9d99dd821d | -18.2691 | -52.88861 | 2026-04-23 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f33b2d55-d1ea-3953-b4aa-93bbab3f65af | -20.19872 | -46.73444 | 2026-04-23 04:00:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08d8f93f-f673-329e-b3a5-cfbed29afca7 | -22.19237 | -42.65488 | 2026-04-23 04:00:00 | NOAA-21 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19821b9b-409a-31ee-8909-46aca0b5932e | -21.05078 | -48.66605 | 2026-04-23 04:00:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README3.md)
