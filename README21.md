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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f03637-b004-33ae-989d-330f5c124066 | -11.63986 | -60.44247 | 2026-07-28 06:14:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e11f5565-712d-3ca5-80f7-8a4baa4c79e6 | -11.65654 | -61.22163 | 2026-07-28 06:14:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 001b5b87-b0c9-3552-ba7d-258b7d875f2f | -8.9281 | -65.01338 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0ebf20c-2b93-339c-95c4-f49552b9e8f0 | -11.63934 | -60.44684 | 2026-07-28 06:14:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6142d8c7-549b-3943-9872-b612fd872bb8 | -11.66226 | -61.22242 | 2026-07-28 06:14:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bd23aef-bb1a-3caa-b5a3-694d0d8fc9b6 | -10.9397 | -43.0593 | 2026-07-28 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3b7a6705-08c8-386b-b995-c08b891f2a1b | -18.3749 | -50.6564 | 2026-07-28 06:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c3ee1f22-a398-3dee-857d-5670603d8c4e | -10.9397 | -43.0593 | 2026-07-28 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 04d5bb5a-68fd-3878-91cc-23343dc1e9d6 | -8.93229 | -65.01772 | 2026-07-28 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 240e9bf4-3241-3b84-b528-09eca604dc4b | -8.93164 | -65.0231 | 2026-07-28 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93fe28de-212d-3c5d-8297-37c0d2200bf1 | -4.37278 | -47.76799 | 2026-07-28 06:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d8ce2c09-dead-31b3-ac55-4811c2b040c9 | -7.00431 | -45.42345 | 2026-07-28 06:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2fb1d504-6ce4-3520-bf8c-dcf6a5863750 | -6.8729 | -46.00117 | 2026-07-28 06:33:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 879e9dd7-658b-372c-9803-a1729577f150 | -10.38382 | -49.56696 | 2026-07-28 06:35:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c73c808c-27da-334d-8f04-62e40310134e | -10.38219 | -49.57737 | 2026-07-28 06:35:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 75e5e30a-e429-3e4b-8a95-bcb81e8d6905 | -10.93143 | -43.053 | 2026-07-28 06:35:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a1fadc7c-8ad7-39ae-b0da-77159cef5e93 | -9.36167 | -44.72779 | 2026-07-28 06:35:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a4158094-3e23-3871-95e6-b997ed4f8ab3 | -10.94384 | -43.04117 | 2026-07-28 06:35:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7665d025-8fc2-370d-96a3-2cbb516b1233 | -10.94202 | -43.05444 | 2026-07-28 06:35:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 8baf58d8-38fa-31fa-8a15-3e74f8f342a4 | -8.13086 | -46.77784 | 2026-07-28 06:35:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48dde358-34c0-33e9-add9-b8326358d498 | -13.29878 | -45.10522 | 2026-07-28 06:37:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f743a591-6ffb-3381-b82a-e5feb6c7f1bf | -11.98339 | -45.54564 | 2026-07-28 06:37:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 16e59735-1714-3e41-ab4a-bbf9d7e30978 | -18.37319 | -50.65515 | 2026-07-28 06:37:00 | AQUA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 81dea9ef-02ca-32e8-8ff9-0bd151e1ee70 | -13.90969 | -41.60598 | 2026-07-28 06:37:00 | AQUA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 3c7fb022-25f5-3ec7-b594-5bcca6e707be | -12.8459 | -44.38197 | 2026-07-28 06:37:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5345c50a-d009-38ab-8267-5150db77b93e | -11.97422 | -45.54434 | 2026-07-28 06:37:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 50d4c3d1-9c33-3bb8-ad67-4c2cc0a7990f | -12.45234 | -46.50714 | 2026-07-28 06:37:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8d7a80db-4f99-3fe5-abaf-115a63efaae9 | -13.91004 | -41.62948 | 2026-07-28 06:37:00 | AQUA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 39.1 |
| a358454d-6162-3f9f-87f3-cf079130f329 | -13.29073 | -45.0932 | 2026-07-28 06:37:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f2fe9725-f277-38ed-a05b-56129ff127bc | -13.90739 | -41.62403 | 2026-07-28 06:37:00 | AQUA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 45a9abd5-4ab6-3a6a-8fe8-ed84fb8f4d7c | -18.37159 | -50.66502 | 2026-07-28 06:37:00 | AQUA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 6a1117e8-2807-3793-b55a-01d05dd2f0a6 | -12.46123 | -46.50844 | 2026-07-28 06:37:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4707f2da-da2f-39fa-84c3-1b1f6aa8fdde | -13.91226 | -41.61098 | 2026-07-28 06:37:00 | AQUA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 52.3 |
| efc4300f-aa63-3cbb-8169-8da61b3af96f | -13.30027 | -45.09449 | 2026-07-28 06:37:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f87cb654-c8b7-34da-8d43-3152f26774d2 | -18.3749 | -50.6564 | 2026-07-28 06:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| bdcd3257-6b28-36a5-abb4-371cc10d0fdf | -10.9397 | -43.0593 | 2026-07-28 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b3593307-eebe-30ee-bc67-9febb0d5c704 | -20.7189 | -49.43708 | 2026-07-28 06:40:00 | AQUA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 6ecacdc1-6147-3b65-8741-d6b54ae8a9fe | -20.72031 | -49.42775 | 2026-07-28 06:40:00 | AQUA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 0d4b610b-789a-39f7-b91a-a11f671acb2a | -10.9397 | -43.0593 | 2026-07-28 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9c5938fc-1e61-364a-b288-1d3a33f9a7d4 | -10.9397 | -43.0593 | 2026-07-28 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| be1be236-56ca-3d84-b435-e857fc36b486 | -10.9397 | -43.0593 | 2026-07-28 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |


