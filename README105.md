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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b1fe33c-a9b7-30d1-9e9c-64ea10d299d3 | -7.1959 | -43.7019 | 2025-08-30 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 0a3496d4-2bb0-3e4a-b2f2-e1f2ddb70b00 | -13.3632 | -46.9727 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 076ed83e-ac1e-3559-a0ec-04889bb69065 | -11.3517 | -43.566 | 2025-08-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 492f416f-c342-359b-b30f-e38f77e9ff24 | -7.4278 | -44.8096 | 2025-08-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| c85fc9b0-51fe-3a45-bfc4-2ccfba514f0d | -12.8409 | -48.1907 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3c349238-a143-3cd3-9f43-3940deb7bba4 | -10.9897 | -50.8043 | 2025-08-30 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 168.7 |
| d5344426-b4a3-35f4-b49e-a7393702860c | -13.5373 | -46.9456 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c0ca7d86-e323-3abc-899b-df0f625feef5 | -14.4674 | -52.0046 | 2025-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 762234ce-ca89-32fe-a76a-ce307b19e72f | -14.0313 | -44.5578 | 2025-08-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 221.8 |
| f3a2f3a4-647c-3ffb-a134-ba71fb7fe3ae | -12.649 | -48.1953 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c0755a4e-fa19-3a69-893d-d5fcf04789cb | -8.386 | -44.966 | 2025-08-30 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7f559b07-37d9-3cfd-9f74-7dd411815190 | -11.3521 | -43.5423 | 2025-08-30 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 1ecd298d-5ee3-3602-a04a-dd4a8c31ca6e | -6.944 | -46.1856 | 2025-08-30 14:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 46e89c52-1875-356d-bfe6-37d025bbe1a2 | -9.4683 | -62.3476 | 2025-08-30 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9747da88-6976-331a-adeb-833b33f51339 | -13.401 | -47.012 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6a177940-06fc-3bb1-9b28-398ac054805e | -6.185 | -43.3491 | 2025-08-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 46d31092-c510-3c40-977f-49a476a1285d | -9.4311 | -62.3493 | 2025-08-30 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 3c3e6e52-f945-318f-bb46-be7816158cf2 | -13.0154 | -56.8982 | 2025-08-30 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 65f670f4-283d-3990-9e2c-1c4ce6e488a2 | -13.3817 | -47.015 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 0c5d4027-9f6a-3bf1-9700-a6c06506a047 | -6.1665 | -43.3273 | 2025-08-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 9eb7ac17-d4a6-3973-8e98-58a666c3e644 | -14.4484 | -51.9858 | 2025-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| e33e6350-4fa3-3cdd-ae26-b4c9afda0c30 | -6.4255 | -45.5989 | 2025-08-30 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4370648e-4d96-3c00-8d20-97dd4ba79ff6 | -6.7037 | -44.0248 | 2025-08-30 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a34ebb52-d465-3602-a0b6-d44bbeec87ed | -7.0951 | -44.3128 | 2025-08-30 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 7b7090dc-8771-3403-a369-a7d5696b3fab | -6.3815 | -44.3515 | 2025-08-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1a7a030b-a767-3250-ac73-4ef0d72053bf | -13.518 | -46.9486 | 2025-08-30 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e8ab9e9d-d45a-3b6e-a63c-cdd1a355656b | -9.4432 | -60.5692 | 2025-08-30 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| fc8644f3-8443-3a11-b6b6-483026659dec | -9.0614 | -65.4355 | 2025-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 03679191-9271-3324-aa17-d2be36f937da | -7.3232 | -44.084 | 2025-08-30 14:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| fcba1130-d4bd-34e6-bb4c-c3ac32a811ab | -14.4671 | -52.0259 | 2025-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 965f4fcb-7e20-3457-b771-c8c9a4da70c1 | -6.5951 | -43.6403 | 2025-08-30 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4293950b-d680-3091-8c68-fd3a434ed547 | -12.8605 | -48.1657 | 2025-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |


