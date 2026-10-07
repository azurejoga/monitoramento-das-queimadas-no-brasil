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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b55068e-ed81-37c0-9083-812e68851625 | -8.59232 | -45.69015 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1e003ba3-52cb-3a04-a449-b26215ce2a04 | -10.78867 | -46.54168 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2af1be44-68e8-3305-8e84-c0edc2ecf051 | -11.72838 | -43.65746 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 77d478b4-7fa6-37f9-9dfa-83fad2a940bf | -11.25917 | -45.18853 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 483deb7e-8550-35b9-9cca-d3e3d83819e9 | -8.58808 | -45.68747 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b8cec155-9431-349d-8c06-6d9dbfad1710 | -12.13954 | -43.30708 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 70aaadf7-da5a-3e0d-b0c6-c2a3ad043c1f | -11.81493 | -43.53231 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ef87747c-79ee-370b-a558-726816731c5c | -13.75084 | -48.12595 | 2026-10-07 16:01:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f4fce298-7ce9-33ac-bdce-931f1d353f6c | -11.62133 | -43.66054 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a9fb33e0-c3da-337c-9307-6a4f45564502 | -8.29318 | -45.47773 | 2026-10-07 16:01:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7a61dd54-c669-3061-a8f1-5e16b718e40d | -11.15214 | -46.11922 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 46e16664-cba1-3052-9900-15a9c03e5c72 | -10.78006 | -46.56113 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 9eab8fe0-09c3-3365-9c66-922f656ea4cf | -13.38784 | -43.87431 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4b3a4f14-3a3c-340e-8d00-bdedb7befeb7 | -12.17776 | -44.74716 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2366f1c0-4e53-398c-9b9f-3bf6935a10be | -11.21541 | -46.2345 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61e87907-fd75-3028-976d-70c72e0608c9 | -8.45202 | -46.42173 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3ca187c-b1f2-37dc-938d-15078a378b24 | -9.86717 | -46.31435 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09a393f9-c228-35a9-91d3-9548236e08f2 | -11.15625 | -46.10895 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 59c845d0-9b44-3bbb-b31a-4cd2c65f12eb | -11.08789 | -47.61912 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9d3f95ac-a79f-329b-833a-75131a88d775 | -10.3785 | -46.25274 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9ef14891-f1b0-3e6a-bbae-dbd7fa779bc3 | -9.37914 | -45.92577 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c56d086a-2c9c-3ef2-95ff-99129f9d7f91 | -11.71208 | -43.67347 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0cfaa0e4-1a98-3c9d-b63e-df3f4a2f5f96 | -9.03469 | -44.36353 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6f5d5476-0ca3-31a3-a12a-33e287cbb9a3 | -10.49318 | -47.26805 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 23bf9361-ee62-3dc3-872d-f1e8bee4d01f | -11.84524 | -43.5369 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e431a019-61d5-3dc5-9068-5c4cdbd9c11d | -9.81569 | -47.47066 | 2026-10-07 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 677b9b70-3641-32e8-932b-bd899cd0e802 | -9.93444 | -45.9176 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0810d171-339f-375b-9963-27fc6917993a | -9.96654 | -43.50173 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| af9de717-ce1f-333e-b717-2be3db0cec8e | -12.72519 | -38.46336 | 2026-10-07 16:01:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 4ff79b2e-6fe2-34a5-a988-78834ff36aa6 | -11.14813 | -47.29947 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8eb80480-e259-323d-89ee-3ea90541a823 | -9.99422 | -46.01414 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 87ee825d-417d-3c77-8b31-c818096586eb | -12.03367 | -42.94739 | 2026-10-07 16:01:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ba95382e-924e-3d80-ab2c-22b12506a9e7 | -11.84969 | -43.53598 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 4e89c768-65b5-37af-8b89-bef0ff76f5df | -9.44809 | -45.81937 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 06351158-606d-3061-bbc1-07b3795c16bb | -11.01718 | -47.97696 | 2026-10-07 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d71fcacc-f309-345d-aa01-2e5b2810bbed | -13.55275 | -49.15255 | 2026-10-07 16:01:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 402e6c20-f4c4-352f-8575-1b9e6442963c | -13.33572 | -39.0083 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c08e6eac-93eb-3d24-bb4f-91e0c89d1b1e | -12.16656 | -44.73736 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| bc3dce6d-6b6e-385f-b4ec-a9d41d163a69 | -11.15666 | -46.11226 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| eb783bb7-dde2-33f8-9272-4b0295940308 | -10.78234 | -46.53519 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 92ae62c5-5269-3fb2-b23f-e649ee8c3cbb | -10.78164 | -46.57379 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8470e3ce-0480-342f-90fd-53126331aec4 | -9.91787 | -46.8062 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6529e54c-c81b-380d-bd05-8c2d2f5cec89 | -9.03297 | -46.884 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f50fb3dd-acc9-3988-8f05-0b391917fe8b | -12.45124 | -38.57738 | 2026-10-07 16:01:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 814ceb9c-9477-3681-9c49-dc73a110d95e | -8.99349 | -45.9365 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 89047240-e803-34b7-a611-c8b7dc1349f5 | -5.97496 | -40.95592 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| b7f1b068-af4c-3d78-aa96-d8fd59338787 | -2.72287 | -43.57467 | 2026-10-07 16:03:00 | NOAA-21 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87bb155c-5ce7-3782-906d-5596bdd0047a | -7.54643 | -46.73586 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ce79ded9-53f5-31d3-998e-159b935a3ded | -5.71643 | -41.67531 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| a53e3df4-3e06-369d-a526-22aff6cd8c4a | -5.94149 | -46.63693 | 2026-10-07 16:03:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2cdb77cf-8348-3a61-b5b5-433d8388db88 | -3.69932 | -40.83646 | 2026-10-07 16:03:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8f0629fd-8269-3bb3-88ef-2f7702ddab2c | -3.53396 | -43.81959 | 2026-10-07 16:03:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5066fda4-6e29-3d66-afab-4d280b52f6a8 | -7.18161 | -44.31384 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d80fc154-8934-3f7c-93ff-37949d96df1a | -2.2628 | -48.75266 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9e643e1-9ad3-33e7-95af-dfcc272380a1 | -6.61428 | -37.8821 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 20.7 |
| f6163c93-8f5c-3c79-ac73-3339b0bce147 | -4.57082 | -43.88326 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ed27f3d1-e61e-377a-beb6-0980a274ae62 | -7.77026 | -48.23556 | 2026-10-07 16:03:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 3d61dac1-5e69-3621-b89a-27698074dd07 | -3.10654 | -42.95292 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7efff6b3-a3f8-3560-818a-ff9c8c2762bc | -7.5778 | -46.19906 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5b35258c-2a78-3732-97c2-9e7263bca3a5 | -3.51081 | -41.94334 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 32846a96-93b5-3e30-8db0-5b0e9c316832 | -7.75704 | -43.8054 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d9d51ba9-d447-3795-8a15-b56461f79cdd | -7.77112 | -43.8117 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 1c8f35ea-c760-3f5b-8813-c06523f44393 | -2.8851 | -43.63709 | 2026-10-07 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 15368609-b145-3533-aaf8-c9e860200d5c | -3.5588 | -39.46962 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 02b59a87-8db2-3935-848f-de41492396f0 | -6.22157 | -44.84288 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4dcfc7dd-d39f-327c-9036-742c20a6e671 | -6.12801 | -47.92236 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2d389215-00ca-3b8d-be0a-01f23f6ba65c | -6.71629 | -44.04748 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8887d9a-c0fb-3320-97a3-4bd510e3bf0c | -5.97742 | -40.92291 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 84aa3e50-e8ce-36ed-824a-6775b6170065 | -5.74011 | -41.73375 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 93933f75-1ca3-3767-83a2-7f3a9b9bebd5 | -7.52264 | -47.75363 | 2026-10-07 16:03:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 12c82d2e-9837-3674-bd2c-4c71fba56237 | -5.9666 | -40.92441 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 83945a0b-95f1-3746-8c1c-85f8833c1e7a | -2.06152 | -45.97596 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 848188b9-cbde-3388-862e-8ad9aefa6b88 | -7.1702 | -47.80031 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f9b1ed43-2146-3253-a907-33f5e3cd96e3 | -3.88232 | -44.12077 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 568d99f2-eb4a-3061-9d74-406bd9c4586a | -7.68156 | -47.3432 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9496b214-d9d6-3764-8caa-44221b42072f | -4.57442 | -43.87891 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 24ad5962-b5f1-3b33-b0b0-6d1a2b222e0e | -4.08245 | -43.2465 | 2026-10-07 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70cffb93-5235-366f-b238-987b858d7310 | -5.96601 | -40.92047 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 8b830ffd-a005-3fa0-b0f1-ff0be91417d8 | -7.37414 | -46.88951 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f8c3660-94a0-3cea-8593-cddfbcfd341f | -6.94963 | -45.26608 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 6e72cf7e-f736-3c81-be70-463c9f64c9c8 | -3.15739 | -48.58087 | 2026-10-07 16:03:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e98a66cf-31a7-33c1-bf46-f8fcd315762c | -2.41414 | -51.29929 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6ef9316a-8e09-36d4-b9ed-c4638ce92815 | -7.75875 | -43.81754 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| d9e97275-6eb8-3d9f-b9df-cdc03782ba27 | -5.07977 | -37.60668 | 2026-10-07 16:03:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 24a52758-5220-3a88-afd6-bf3b6d0753cc | -6.07719 | -44.38702 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d2d8a73-dd20-3a63-97d4-f4c076361cba | -6.93949 | -45.26212 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 9474e000-5de5-3247-b3f0-2d247161fcd7 | -5.96521 | -43.87194 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 69045a80-29fb-3497-8f94-ffe70edb9c33 | -7.06732 | -45.3738 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3192b6aa-4170-3e31-9751-f4a5fc51e493 | -7.28575 | -43.86724 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4f6eb150-dd68-3906-8a57-f630e30fe8df | -7.40438 | -45.65046 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 3395f251-ee9d-3f4c-87a5-6144ac59673e | -5.98565 | -40.92977 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 85178e71-b983-33fd-869b-064e7cd54b31 | -3.89201 | -44.10007 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a4bde410-ba8d-3394-bdee-287a25be4974 | -2.53252 | -47.44312 | 2026-10-07 16:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 00e01b66-f8ce-33b1-956b-e4d9105ec07d | -6.28965 | -44.89927 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 565d337a-9847-3cea-acfd-94f521e765b8 | -3.80594 | -38.43498 | 2026-10-07 16:03:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ad3ac897-91bd-3624-a8c2-1a4a54018d98 | -3.39841 | -42.83466 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6df84e72-96a9-38ad-908b-26a8bab3aa51 | -4.69851 | -40.27575 | 2026-10-07 16:03:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 00976e92-a118-3615-a5dc-d9016be235a0 | -5.95207 | -46.37971 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 84940bec-dd1e-3c01-b5da-ab5c5b87144a | -5.95371 | -46.39134 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49a44f75-b8f8-3614-88c9-44f78582c727 | -3.1918 | -50.57382 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |


[Clique aqui para ver as próximas entradas](README159.md)
