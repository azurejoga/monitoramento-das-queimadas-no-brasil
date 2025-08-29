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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c463e0e5-ca6c-341f-9acd-74ecf403de47 | -14.3502 | -53.2453 | 2025-08-29 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 20ab9702-665e-3d30-b816-89c3eb099619 | -14.0328 | -44.487 | 2025-08-29 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 346.4 |
| 92278794-f89c-31fb-a0ed-828334f81920 | -6.2741 | -43.8299 | 2025-08-29 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 97047f7a-633e-3ce4-996b-c56db8e52986 | -9.4432 | -60.5692 | 2025-08-29 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 9ed010de-7f65-3f63-9c4d-cc16d10b002e | -10.641 | -48.6677 | 2025-08-29 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f37e629a-03b8-3dfd-b686-e45c3cefd127 | -6.1558 | -44.4385 | 2025-08-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0fc069db-1a8b-3a0f-987c-b03dec6b2de6 | -7.415 | -44.283 | 2025-08-29 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 038a043e-dac1-3b81-aa2f-40c42a66b66a | -13.5967 | -46.8684 | 2025-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 2b6f1065-d20c-39f6-bbd9-7a8eea21dc03 | -6.6948 | -43.0943 | 2025-08-29 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 79c02b9e-da95-38d1-b2e8-7ba49f3228b2 | -8.1758 | -61.3755 | 2025-08-29 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b709c36c-26ca-3e34-9fac-688f5ac83cca | -13.5774 | -46.8714 | 2025-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 387.9 |
| e7592ca0-70e2-30ff-92d8-3fb4acb2ecef | -14.3296 | -53.3318 | 2025-08-29 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 60a025c0-a2a5-3a68-b8e4-7bc8a72e7598 | -11.876 | -46.4007 | 2025-08-29 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 533aeb04-9980-3b86-9966-33649100836a | -9.7728 | -64.2657 | 2025-08-29 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1f0da8d1-7011-3ad2-9209-3ef90d8730bb | -11.3517 | -43.566 | 2025-08-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.5 |
| bee695a9-08e3-3a0a-8dce-99c533961e0c | -6.2743 | -43.8067 | 2025-08-29 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| af642a3b-feaf-3695-9668-4554374915f9 | -14.3299 | -53.3108 | 2025-08-29 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 55dfe0ba-3a84-3b8f-bce6-79ff15e1b1ab | -9.3238 | -56.9064 | 2025-08-29 14:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2bdf6a6f-dc47-37ac-b3ef-cf79afe04e67 | -11.3513 | -43.5897 | 2025-08-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 9006581e-43d6-3483-a2b1-edaad762597f | -13.558 | -46.8745 | 2025-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 472.3 |
| 75af335e-4125-3afd-9aba-5e38f9b6d5fc | -7.1106 | -44.6099 | 2025-08-29 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 25c79a7d-2f05-3ea0-aed0-188b4bf5edc6 | -6.887 | -44.4464 | 2025-08-29 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 48ec03b2-90c6-3e78-ae7a-0536fa2f38e2 | -13.3543 | -54.38 | 2025-08-29 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b660b557-b131-314c-9fcf-6309c0cebe9b | -12.4345 | -63.9173 | 2025-08-29 14:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3034f9e4-f6db-3109-aec1-4a79d652619d | -12.8416 | -48.1462 | 2025-08-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 62da6b2e-a93f-3fc1-be7d-01fb1f26090c | -10.848 | -47.4991 | 2025-08-29 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| a69080e4-a433-3e8e-a33b-07d72ac34d36 | -10.4736 | -57.9563 | 2025-08-29 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4c0799e9-32d4-30b3-bff4-cdc49809ef0a | -13.5576 | -46.8972 | 2025-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 15516c63-a542-3447-bc6f-1a54dd2287d4 | -12.9385 | -56.9655 | 2025-08-29 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 7a541251-ae5e-3002-8763-a6682ce6cde3 | -10.8607 | -60.8191 | 2025-08-29 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 0e2ec5c6-e9dd-3118-9579-0a8267bb8579 | -7.6222 | -42.6975 | 2025-08-29 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 184a4411-c018-345e-94db-818453b4718d | -9.773 | -64.2469 | 2025-08-29 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 9cfaf395-2356-39a8-9ca7-1cd62df82d7b | -12.0553 | -50.6425 | 2025-08-29 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b376f397-1a27-33e5-a127-4788f6a230e4 | -11.3856 | -63.2653 | 2025-08-29 14:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 696cdb5a-4226-3e20-8e6a-db91226f0fbe | -11.3713 | -43.5394 | 2025-08-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d7406823-ee1d-336d-a753-73c4e3a95f4e | -11.3521 | -43.5423 | 2025-08-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| eca25939-f751-39ff-bcc4-9b80fc45acfb | -8.1964 | -45.0541 | 2025-08-29 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| b7a796dc-6e4b-3b2f-a11a-8dc8e7d22083 | -6.7072 | -49.4774 | 2025-08-29 14:10:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| bfb31344-299a-3525-b099-2bcad6e2a087 | -9.7916 | -64.2461 | 2025-08-29 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 34d33442-b96a-3e3c-988a-3a824fc7af09 | -11.571 | -46.3525 | 2025-08-29 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2f3e35e7-110b-30e9-8741-127f1cea9de5 | -7.6408 | -42.7192 | 2025-08-29 14:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 168.6 |
| 8f6fafdf-2dff-3078-b607-4f183ae9af30 | -12.9382 | -56.9856 | 2025-08-29 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 53b303d5-f6a8-3756-8807-d7b1d3be012d | -6.9867 | -59.3354 | 2025-08-29 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b5900f6a-fac8-383a-ab64-5304624045e3 | -12.8413 | -48.1685 | 2025-08-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |
| e3dea4a7-d855-347d-9666-64fa552baa3f | -12.9194 | -56.9672 | 2025-08-29 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 761fcef9-0f17-3961-b9a7-c8bcc3824857 | -6.3916 | -45.2402 | 2025-08-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 38c478f2-5999-3a57-b8c0-2ff99df6e7b4 | -13.354 | -54.4006 | 2025-08-29 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 91bb444a-0f99-3465-a447-07e80f9241d0 | -15.6749 | -52.7552 | 2025-08-29 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 485f0fc2-f643-3731-adc6-78133dd59249 | -9.5637 | -45.882 | 2025-08-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| e7e1e333-3db7-380c-b13e-933c49afbe34 | -7.2105 | -44.0715 | 2025-08-29 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2a94acbb-b61d-3875-8fce-ad921bfa1783 | -8.1775 | -45.056 | 2025-08-29 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e23c543f-ae8d-39fb-8cde-84839987bf28 | -9.564 | -45.8594 | 2025-08-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3c65410f-0387-3b69-83c7-3f91b16613c7 | -6.156 | -44.4155 | 2025-08-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| fdfaebca-5381-3180-9403-d1fa91f56634 | -13.5584 | -46.8517 | 2025-08-29 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 159.6 |
| c260b174-78e0-33fb-8efa-bf23b82643eb | -9.2493 | -56.8914 | 2025-08-29 14:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 15924c94-d798-375e-b26e-549ec59f8e2d | -7.6219 | -42.7212 | 2025-08-29 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 156.8 |
| ff00747a-6e6b-3d12-b74c-4da451887263 | -11.5714 | -46.3298 | 2025-08-29 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 192.8 |
| f5425796-d4a5-331b-942d-29b8b6228023 | -6.137 | -44.4399 | 2025-08-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 9304cb7f-0a04-3ca7-b470-ac446c461906 | -11.3325 | -43.5689 | 2025-08-29 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 8ff7e04a-40a1-36e1-a557-c708509383d9 | -9.7915 | -64.265 | 2025-08-29 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| bf9cbf75-8cfe-3ab0-889d-452dd5429dba | -10.0247 | -48.08 | 2025-08-29 14:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4ecdc5f7-bb25-3157-a825-6392d212d919 | -15.0835 | -48.1367 | 2025-08-29 14:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 51b66670-572c-35f2-8d24-75990ac809d1 | -10.4551 | -57.9378 | 2025-08-29 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a96fd4cb-204a-3b76-9c2d-d17c52b5e627 | -10.8419 | -60.8202 | 2025-08-29 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 46ef5b6d-94d9-3ecb-a706-fbb173f740a8 | -7.9735 | -46.3854 | 2025-08-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 56e33df3-fae3-3a92-97f1-d26077d20f4f | -7.6183 | -46.2392 | 2025-08-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 16df22b7-56bf-38cc-9e02-7bfe8b436b67 | -6.3881 | -45.6018 | 2025-08-29 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8b234fdf-c000-3a78-a5e3-c8b1176f2486 | -11.3667 | -63.2853 | 2025-08-29 14:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fa97be72-3d81-39f9-9ce8-5a1d2c91b236 | -14.3506 | -53.2243 | 2025-08-29 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dfa643a4-6fc7-352a-9277-a0e50db81a96 | -12.822 | -48.1712 | 2025-08-29 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 9989b4d7-af77-30b0-867f-9a066a272d16 | -10.8483 | -47.4768 | 2025-08-29 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9b09d7a9-e3c0-3f03-abee-1ef9750bb3dc | -9.4618 | -60.5682 | 2025-08-29 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 6c7e5077-b0c7-3362-8899-545e81b20ccc | -6.3918 | -45.2175 | 2025-08-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 4a67fd82-3400-300c-bc08-58b932755088 | -11.0826 | -44.7503 | 2025-08-29 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a15abc8a-038f-31ed-bf7d-7a38092ddb1d | -6.1372 | -44.417 | 2025-08-29 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2b83c5ad-2d4a-311e-9e46-86bd16f6b9e8 | -9.1719 | -59.5017 | 2025-08-29 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 939b3e2c-37e4-3b45-b986-cc0080f51012 | -8.7714 | -68.7082 | 2025-08-29 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 2d7f56f9-c258-3cca-9610-ecdb7525ffb1 | -6.3881 | -45.6018 | 2025-08-29 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f9b12263-b2ba-3b60-ad0f-656191076247 | -13.5774 | -46.8714 | 2025-08-29 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 0362c3ff-418b-369c-8681-a546f6c3be8a | -7.6225 | -42.6738 | 2025-08-29 14:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 5b51e8c7-4719-3de8-93da-a54c9c9c37a5 | -11.0826 | -44.7503 | 2025-08-29 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7e371bdf-a63e-3a40-9ce4-ae04968499c1 | -8.8919 | -62.4487 | 2025-08-29 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 56865c0d-c550-3f3b-a879-52f8d956305a | -9.4618 | -60.5682 | 2025-08-29 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 166.1 |
| b87eeda0-9388-343d-bca8-9137cf128113 | -12.0553 | -50.6425 | 2025-08-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c1ec0916-c181-3b2c-948e-b29f915bd974 | -9.5139 | -45.3884 | 2025-08-29 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 723ac6d1-b5ab-312a-bcf2-fdad9499398d | -14.3506 | -53.2243 | 2025-08-29 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0aacec4c-70a5-33e6-a0b0-f2dd5354edf0 | -7.6183 | -46.2392 | 2025-08-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 838eea5a-0c03-3b00-bfb0-147e5df23306 | -13.354 | -54.4006 | 2025-08-29 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 4cc42ca2-aa8c-351f-9d15-2956502157e5 | -6.8131 | -44.338 | 2025-08-29 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 0e78f7f8-4dff-3974-ae62-e53bda876e88 | -9.7916 | -64.2461 | 2025-08-29 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 456cc684-5053-3c32-a4a3-9fe57b5caf1e | -10.8419 | -60.8202 | 2025-08-29 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1ed77e0f-36ad-3353-b02f-31243ad365b1 | -9.1906 | -59.5007 | 2025-08-29 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 20b9cb84-cc20-3539-94d1-5d5ad3ad0f97 | -10.848 | -47.4991 | 2025-08-29 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 44db45e4-df10-302f-bb27-1ef9b5e50cac | -13.5967 | -46.8684 | 2025-08-29 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 22a16c3f-10f9-337c-b5f2-0630b2b93065 | -9.2493 | -56.8914 | 2025-08-29 14:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a870839b-b510-3d7b-8ec7-58dfedda65f2 | -9.773 | -64.2469 | 2025-08-29 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 44062337-613f-3862-b84c-528940d0eded | -14.3502 | -53.2453 | 2025-08-29 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f6d3304a-5091-3bbb-8e18-c6c33c7ee6e8 | -6.2743 | -43.8067 | 2025-08-29 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| af733642-cf2b-34b8-9688-0d9aca25491a | -7.1106 | -44.6099 | 2025-08-29 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 217.4 |
| d32dd808-c4e4-3517-bf31-ce3105de806c | -6.19 | -44.7788 | 2025-08-29 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |


[Clique aqui para ver as próximas entradas](README98.md)
