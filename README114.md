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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 017fc397-e17c-38d3-a15b-524d339de58a | -11.8343 | -51.4339 | 2025-09-04 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 771a3239-6ca3-3138-a822-1059cfb5446d | -12.9001 | -56.989 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 555362c2-2bd8-338c-b446-80bf682de465 | -6.2604 | -43.3194 | 2025-09-04 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5f3c4a63-959b-31f0-a539-14bb908ea65b | -7.9341 | -44.9436 | 2025-09-04 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 79b5518c-82e4-3128-b426-d3d2b302b80a | -13.8651 | -47.9734 | 2025-09-04 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 092cddcc-297f-3988-b040-931d72c7f09c | -12.4977 | -48.0832 | 2025-09-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 83142777-3c08-345a-9824-e58944763a6a | -16.5497 | -55.0991 | 2025-09-04 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 01378136-45a8-3b95-8302-16b1032917e7 | -9.6848 | -51.0397 | 2025-09-04 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1af34bee-587f-3e1e-8ff8-09bcb5d58c7b | -22.6567 | -43.6825 | 2025-09-04 14:40:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 123.0 |
| fbdee75a-7549-3717-9236-6f8da85e639c | -4.9051 | -41.7457 | 2025-09-04 14:40:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 0e35d154-5273-3ee9-b952-48667ef4e876 | -15.737 | -53.635 | 2025-09-04 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 336.2 |
| 5ac92fe1-6566-31e7-a36a-30c5035e84c0 | -8.479 | -45.0704 | 2025-09-04 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3a065bbd-464d-31c2-ae17-99494fa7ea77 | -12.523 | -53.8278 | 2025-09-04 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 34aeb3ff-7a17-3b43-9ef5-f7f652e5c3b1 | -5.6994 | -45.2466 | 2025-09-04 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4f4563da-5619-3c96-9a7b-663299e911ce | -10.1457 | -46.2424 | 2025-09-04 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 57019dd9-6b04-3204-a019-2ddfd0b2ab98 | -11.6525 | -52.212 | 2025-09-04 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 302db3be-7f34-3461-8c7d-55b9ce06c669 | -11.3893 | -43.6075 | 2025-09-04 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 501.5 |
| 85ef3c81-cd9a-3baa-ab96-ea2f8ca11ff8 | -8.3641 | -48.3334 | 2025-09-04 14:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 380ddc40-a542-3661-85ae-adc65b5a6703 | -11.6599 | -54.5297 | 2025-09-04 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 1394dfa3-f16d-31cc-8fe0-0dd63bb51926 | -12.9668 | -54.791 | 2025-09-04 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 00628d75-50de-315a-ba3e-724dd7a07550 | -11.0062 | -45.9072 | 2025-09-04 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3a2b6aa6-0c76-3495-8f59-b2880fa304d8 | -13.0889 | -57.1126 | 2025-09-04 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.2 |
| bbaa510c-882f-36f3-96e1-33eddba5cb33 | -8.9037 | -45.7747 | 2025-09-04 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |


