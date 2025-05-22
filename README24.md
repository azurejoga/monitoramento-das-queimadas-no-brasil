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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee677a09-56d3-3d42-b044-f8ff6cde275f | -12.294 | -52.5205 | 2025-05-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| fd71d16e-c97d-378c-8749-1d30f2642c6c | -12.3137 | -52.4764 | 2025-05-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fc5747a2-2924-34fc-a06e-0d5c191e082d | -12.2943 | -52.4995 | 2025-05-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 850.6 |
| 9201ff6b-8ff9-31c6-913d-9666076abbe7 | -12.3134 | -52.4974 | 2025-05-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 173.6 |
| e8fb0a93-3637-30fb-9508-a03b5c804727 | -14.0404 | -53.3669 | 2025-05-22 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 39b948fc-a955-3856-849d-439fef1dc24e | -10.4154 | -49.9254 | 2025-05-22 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 6baca743-e1be-38a6-b349-0653219fbff0 | -11.5528 | -47.4546 | 2025-05-22 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 90bd2071-e283-326b-abc7-a9861e38ad6f | -11.5528 | -47.4546 | 2025-05-22 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a90a3ea5-3e7a-3ddd-8d9a-4f4d354a66bc | -12.2753 | -52.5016 | 2025-05-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 247.0 |
| ae6cdad0-59ef-3ddc-a973-8524c23f12a6 | -14.0401 | -53.3878 | 2025-05-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3ecdd785-5d60-363f-9835-c3f6093180dc | -14.0404 | -53.3669 | 2025-05-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 10f96d73-7f84-32e1-90f4-1d167f2e43da | -12.3137 | -52.4764 | 2025-05-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8f66256d-f8f8-39fe-99ea-6d815aa53b77 | -12.2756 | -52.4806 | 2025-05-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| cba70b8a-fea3-3be4-b589-47136bc0fd56 | -12.3134 | -52.4974 | 2025-05-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 150.9 |
| b086028d-46e2-331c-9bab-8d53e375ab03 | -11.5719 | -47.4521 | 2025-05-22 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b2145f49-bd88-3a19-924c-c27326ac3f1a | -12.2946 | -52.4785 | 2025-05-22 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 262.1 |
| a1c7ca49-4f9a-315a-8bae-651125eb866a | -14.0328 | -55.13 | 2025-05-22 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3c6b74f2-f1d6-3974-873b-23204bcc834c | -12.2753 | -52.5016 | 2025-05-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 278.9 |
| c922e9b3-30ca-301d-b65d-6c940200c8cf | -14.0328 | -55.13 | 2025-05-22 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c51bce4f-5d43-3a70-ad95-3549f7e88741 | -12.294 | -52.5205 | 2025-05-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f3ebce0c-4c17-334c-9ed4-c0aff3dc5d98 | -14.0401 | -53.3878 | 2025-05-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| aa658b34-5327-33d4-9962-6231c70f8f35 | -13.1687 | -56.8238 | 2025-05-22 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c215f3a6-81aa-382c-80d9-40044bb1d0a8 | -14.0404 | -53.3669 | 2025-05-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 18bcb8e3-4e1d-391f-9ab3-555a95066f81 | -14.0304 | -45.5143 | 2025-05-22 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 60745d55-414a-37c0-87f3-658ef36f2d7a | -12.2946 | -52.4785 | 2025-05-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 336.9 |
| bc18fb15-504b-3918-9927-0908d932439e | -11.5719 | -47.4521 | 2025-05-22 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 25571b80-efa9-3a70-af7a-2f003c02ada7 | -11.5528 | -47.4546 | 2025-05-22 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 41f4c796-5ceb-3860-aadc-4df693a2344c | -12.3137 | -52.4764 | 2025-05-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 1aabd522-9119-386d-82f9-bd2c66feb0b5 | -12.2756 | -52.4806 | 2025-05-22 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 302de940-4b90-30bd-a5a1-bd8c686874d8 | -14.0594 | -53.3855 | 2025-05-22 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 37ae392a-cf3d-3a11-9e29-99d58503b16d | -11.5719 | -47.4521 | 2025-05-22 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 38aa3d57-3891-3f88-9c67-b294f693b1c7 | -12.2756 | -52.4806 | 2025-05-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 3e1d8393-fa8f-3a9b-b42e-a7c1d996c23d | -12.2753 | -52.5016 | 2025-05-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 01ecde69-0fa8-3c80-9227-bd5575c48c4d | -14.0401 | -53.3878 | 2025-05-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 9c8112f9-4698-330a-b66f-b0be0f2af35e | -13.1687 | -56.8238 | 2025-05-22 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3f693c6b-07d9-3a50-a07c-d82a8ad23081 | -14.0404 | -53.3669 | 2025-05-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 4dc3a86a-79b0-3899-9826-269984b094fc | -13.1498 | -56.8054 | 2025-05-22 14:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 229362e1-8480-3f6d-8407-43bee277b612 | -12.3137 | -52.4764 | 2025-05-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 415b72aa-bd44-31c3-88a0-ec75d716f2bf | -14.0594 | -53.3855 | 2025-05-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 38377b3a-cd11-3b54-b65f-868c9202d877 | -14.0304 | -45.5143 | 2025-05-22 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f0405b6e-396a-3d1d-be17-c0b3eb617c08 | -12.2946 | -52.4785 | 2025-05-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 535.3 |
| c22b0788-8e99-3947-b95f-18bfad70d452 | -10.8318 | -49.9023 | 2025-05-22 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c959a625-98fc-3978-903f-7f1ab9cbeb38 | -12.294 | -52.5205 | 2025-05-22 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1617533f-1a70-34f1-b689-df24e81d549a | -11.5528 | -47.4546 | 2025-05-22 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 25fd4978-1887-37aa-977a-458d4ccf826d | -14.0136 | -55.1321 | 2025-05-22 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 02d3ceca-6540-3c2e-99a9-404d118fc553 | -14.0499 | -45.511 | 2025-05-22 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |


