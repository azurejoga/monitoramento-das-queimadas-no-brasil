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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdd29131-1bf9-3f2d-a80a-0d1903d6d655 | -13.62551 | -44.32403 | 2026-01-01 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1770cc22-6bfe-302f-9684-2b9be5fc926e | -13.62897 | -44.3246 | 2026-01-01 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35d8ba3f-32d2-35a2-85b3-3a9e7f6ab9c0 | -17.70519 | -53.27138 | 2026-01-01 04:27:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52370b1b-530e-39f5-ad55-b64706e337a7 | -15.1283 | -52.94379 | 2026-01-01 04:27:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 884991b5-c4a2-38d1-bdde-e48db66eb5f8 | -18.50117 | -47.60054 | 2026-01-01 04:27:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13cdba6b-a342-3b06-bd8d-4fa3de9d742b | -13.76306 | -54.64548 | 2026-01-01 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da55e1cd-814e-33f2-aef0-aaca9d0c3878 | -13.65032 | -44.32418 | 2026-01-01 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee5978f3-da72-3b31-8b77-b295de51a40d | -14.6319 | -55.82327 | 2026-01-01 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 042b1af2-8dec-318d-8b86-955e96905a3d | -16.9165 | -43.49319 | 2026-01-01 04:27:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a342306-8536-3521-81a7-c2f3d5a511d1 | -17.36191 | -41.52075 | 2026-01-01 04:27:00 | NPP-375D | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2ba7434b-6044-342c-b863-bed0597f5805 | -12.96347 | -48.68203 | 2026-01-01 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90f396b1-bf5e-3929-9159-4de4b1e54144 | -17.2987 | -41.74733 | 2026-01-01 04:27:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1e5b25d-4cf6-3292-a917-082c6a2eaa59 | -14.64298 | -55.8221 | 2026-01-01 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 422a985b-18d1-3b6c-9783-a9bba6d450e0 | -15.91009 | -53.01091 | 2026-01-01 04:27:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da3248d3-758c-3d6e-a78b-7cc561cd1d02 | -17.36615 | -41.52122 | 2026-01-01 04:27:00 | NPP-375D | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5ca1232-95f5-3482-82e0-dbb7b15a7ba2 | -16.91212 | -43.49723 | 2026-01-01 04:27:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d81e3c02-be5c-334e-ace0-992414f8b305 | -12.95998 | -48.68144 | 2026-01-01 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41920f34-1b1f-3fb0-a3a0-a395a35fd657 | -14.64233 | -55.82535 | 2026-01-01 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32df0fed-a824-3d84-bbd9-a81472c3d618 | -19.69481 | -43.07985 | 2026-01-01 04:27:00 | NPP-375D | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b24fb03b-743d-3bcc-8f96-afa707d38d7c | -14.55377 | -40.1372 | 2026-01-01 04:27:00 | NPP-375D | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b1031fca-c4c4-3ffb-a3c0-4879adf05ccf | -16.65845 | -43.52734 | 2026-01-01 04:27:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9763209-3eaa-3bdf-a097-4fa02dde8ad6 | -16.14923 | -42.31056 | 2026-01-01 04:27:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ef099ad8-cef6-3d53-9285-7e1f7e6b9c12 | -19.21658 | -53.43884 | 2026-01-01 04:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 948db71d-1af0-3bc7-8361-7a164526491f | -14.51192 | -52.54685 | 2026-01-01 04:27:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01bd877c-1624-38b5-97fb-40cf8e9d5a1b | -16.85046 | -50.16894 | 2026-01-01 04:27:00 | NPP-375D | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ab485a1-46d6-3945-abeb-c5dfe80f6188 | -16.91586 | -43.49774 | 2026-01-01 04:27:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6438e46-1d73-3a5d-8e93-92e2f9e620c1 | -18.49784 | -47.59996 | 2026-01-01 04:27:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 631974ca-4bdc-3ff8-a450-456e720a1805 | -14.64168 | -55.82859 | 2026-01-01 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff02e172-20b3-3868-87f2-dfe595562667 | -13.49197 | -43.69526 | 2026-01-01 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9494d0b5-7c53-314b-8750-c668ee64ccbe | -14.55329 | -40.14088 | 2026-01-01 04:27:00 | NPP-375D | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90e85c40-3372-3ba1-9df1-544caf4b7f5a | -12.80964 | -48.56739 | 2026-01-01 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46ab3f61-52d3-35f4-a24e-86da8ec015d1 | -19.21173 | -53.44186 | 2026-01-01 04:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2951cfc0-2026-38fc-8494-3dd0dd85674c | -19.21249 | -53.43789 | 2026-01-01 04:27:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f75d6372-a9c6-3e16-a947-e216208760d4 | -16.12425 | -52.33547 | 2026-01-01 04:27:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24ca87d3-f774-3b44-b414-a007e8203e3f | -18.8741 | -48.51104 | 2026-01-01 04:27:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e6707a5-6f3c-3786-bd77-78754094c2f9 | -13.47737 | -44.01406 | 2026-01-01 04:27:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40b303cc-4fdc-37b5-9d1a-c67526f67f81 | -16.91277 | -43.49267 | 2026-01-01 04:27:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04dfbbc7-2a73-31f2-9b3b-d4b21e16f435 | -15.14077 | -45.27746 | 2026-01-01 04:27:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa907b43-099b-3bdb-af6c-c57769dd70a0 | -16.39243 | -41.04594 | 2026-01-01 04:27:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40ad645a-3216-382a-91d4-fdf4f20405e0 | -17.31284 | -44.92818 | 2026-01-01 04:27:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56126abd-8bbc-3e0d-99c6-59b52fb61f98 | -14.63712 | -55.82428 | 2026-01-01 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad3560af-2ca5-36e5-88f4-afdbe3e5507e | -17.71562 | -50.87562 | 2026-01-01 04:27:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c6d023b-4178-3a73-b267-b5dc8f2a1f84 | -13.64686 | -44.32362 | 2026-01-01 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18cd4d38-9ce9-3bfa-8446-6f3872221271 | -14.50773 | -52.54588 | 2026-01-01 04:27:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f8eeccb-ff74-3c8e-8049-1342fb31479b | -17.71577 | -50.87682 | 2026-01-01 04:27:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53d507e2-2586-3781-b5a8-b6b090c4776a | -15.13737 | -45.27693 | 2026-01-01 04:27:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 450fd67d-8827-3308-92e0-499fe5af68b3 | -22.92421 | -42.64444 | 2026-01-01 04:29:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3259298f-127d-37f2-a032-b83fdd56acda | -22.92472 | -42.64022 | 2026-01-01 04:29:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69a2874a-94fb-3fbc-8b97-3e2f9ff12362 | -30.05315 | -50.1777 | 2026-01-01 04:31:00 | NPP-375D | TRAMANDAÍ | RIO GRANDE DO SUL | Brasil | 4321600 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 139071d1-95a8-315c-be8b-9fff26fa826c | -29.84775 | -52.11044 | 2026-01-01 04:31:00 | NPP-375D | VALE VERDE | RIO GRANDE DO SUL | Brasil | 4322525 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| b3f7ad3f-6479-3f56-a5aa-2cc7f2347cf7 | -9.5631 | -44.603 | 2026-01-01 04:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 93e9bc7b-6e2d-3691-91a6-4a1205379e91 | -1.36616 | -46.05716 | 2026-01-01 04:44:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ea84c0f-c295-361b-a35e-00691ce8db01 | -0.92196 | -46.90284 | 2026-01-01 04:44:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 04839ac2-80cd-31e0-b66f-db92e1e7f619 | -0.61331 | -47.34819 | 2026-01-01 04:44:00 | NOAA-20 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc7d82f5-a657-3e7d-ae97-e9cad6d483b0 | -2.2432 | -47.87333 | 2026-01-01 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cd8abb6-a2cf-3276-b0ac-854143d21218 | -0.9628 | -46.78248 | 2026-01-01 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 992ba184-2717-3bde-b6bb-ab5e3548ada4 | -1.36543 | -46.06172 | 2026-01-01 04:44:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4213e26-8895-34f0-b43f-25df1a7cba47 | -2.0937 | -45.98625 | 2026-01-01 04:44:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aafb142a-0dbb-391a-bdd3-ef076f373846 | -1.12045 | -47.74512 | 2026-01-01 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a56b17d-60ef-30f0-93ab-e1ab5a1517e4 | -1.48587 | -46.03382 | 2026-01-01 04:44:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4663fce5-dc0b-3c51-b078-8f6ec20c2c4d | -2.37569 | -47.41919 | 2026-01-01 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c834fc06-6ec6-3ce0-9370-cd7fedc8294d | -1.79005 | -45.89819 | 2026-01-01 04:44:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b71d016f-b737-3eae-be72-03357026da0a | -1.6176 | -47.66263 | 2026-01-01 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d88345-601c-3553-9188-cff1cc5c09e7 | -1.39955 | -52.52911 | 2026-01-01 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5910c8e-4835-3d7b-b53a-8f9acbddf9d1 | -0.9626 | -47.94769 | 2026-01-01 04:44:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdc97ae1-a256-3e8a-98b6-63dffeb0296f | -1.83165 | -44.88865 | 2026-01-01 04:44:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab2fc828-05e2-3558-841e-6634a33d70a7 | -1.36588 | -46.05992 | 2026-01-01 04:44:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83d8a4b3-7a9d-3812-87b7-faba77655ad7 | -1.54266 | -47.21655 | 2026-01-01 04:44:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad2e95fb-7ab6-3b99-9104-2640370ba5dd | -0.08906 | -51.28053 | 2026-01-01 04:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 184a9fbd-a67c-3a54-ad2a-eeaa2209b101 | -0.96215 | -46.78663 | 2026-01-01 04:44:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5be17b8f-d8d0-3460-8375-fcf8cdc771d1 | -1.48283 | -46.03097 | 2026-01-01 04:44:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 038b42cc-8263-3bc5-9a2e-479b6bd0bd17 | -1.48207 | -46.03323 | 2026-01-01 04:44:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54d551a5-b681-33a3-af76-27f5db8e2fb7 | -1.61699 | -47.66648 | 2026-01-01 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d455daf-0be7-385b-a8c3-29eef762eae5 | -1.7893 | -45.90293 | 2026-01-01 04:44:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2f5a65-c09e-33de-9475-0deb388bde14 | -2.24744 | -47.84639 | 2026-01-01 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56039fc0-360d-3565-bd6c-569a4c9a0e36 | -2.24683 | -47.85023 | 2026-01-01 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0712d106-fcc2-36b9-ba23-29dcb257fb99 | -0.92132 | -46.90693 | 2026-01-01 04:44:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f348fee3-a2e0-3660-8db2-eb3895f95f6f | -7.57155 | -49.39437 | 2026-01-01 04:46:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1628a0b-5839-3059-bd4e-464188c824de | -3.02537 | -50.51637 | 2026-01-01 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72ee34c6-422a-339b-ba0a-48c2817a8a6b | -5.72093 | -45.04306 | 2026-01-01 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d7f081f-8337-375b-961d-ff58a8922502 | -8.11681 | -47.98887 | 2026-01-01 04:46:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19343cdf-a0c1-3d4d-b313-1e057e6268f7 | -5.92591 | -43.39827 | 2026-01-01 04:46:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5453e879-38cf-3505-9f68-e25ce00dcc33 | -3.65406 | -52.05917 | 2026-01-01 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb7bd327-cbb0-3025-9398-637e336e423e | -5.71231 | -49.09832 | 2026-01-01 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fe2cbc-e0db-3010-a562-caa5e87de996 | -5.5924 | -46.36892 | 2026-01-01 04:46:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ab4df7e-4e46-3e73-a0a6-973134729dff | -2.55988 | -53.87641 | 2026-01-01 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9fddef1-5c41-3e05-95af-011fb90e940e | -8.11601 | -48.06265 | 2026-01-01 04:46:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc29dda5-bfb3-3328-9c13-ad9ef5e1336c | -3.86861 | -54.23046 | 2026-01-01 04:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 225732e9-9d11-3bca-baac-878e22f4c3d7 | -3.02206 | -50.51585 | 2026-01-01 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d65aeb5e-5f6a-3ae3-bfe9-953766ab3b2d | -3.6538 | -48.93401 | 2026-01-01 04:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 656a2483-4b26-31ca-a01e-ad6278827df0 | -5.28595 | -45.83076 | 2026-01-01 04:46:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16bcb7a2-f374-374b-bef1-61001c75c1f2 | -8.60901 | -49.16936 | 2026-01-01 04:46:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 773e323a-7d0c-3045-ac58-157d3b5b6c47 | -5.26289 | -44.77409 | 2026-01-01 04:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9de6427f-5a18-3770-ba8b-569a3014ed5b | -9.56861 | -44.60495 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b7e5c1a8-c95d-3173-94f2-0d8167886dee | -5.92516 | -43.40351 | 2026-01-01 04:46:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a9c4309-9a4d-3edf-8f2c-b004be646a0f | -2.26378 | -50.43505 | 2026-01-01 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5521a56b-d151-322e-821f-4651ab5e4962 | -2.54805 | -48.92709 | 2026-01-01 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ce78eec-dad2-3f6f-b02e-acb8171e9697 | -5.04968 | -43.60604 | 2026-01-01 04:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12812a09-bbcb-3391-9b48-b0cd44d45fac | -3.4217 | -50.2226 | 2026-01-01 04:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87b84673-991b-3835-9654-6c80b416888e | -5.08768 | -50.01784 | 2026-01-01 04:46:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
