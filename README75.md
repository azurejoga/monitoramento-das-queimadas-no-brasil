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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 644a238d-a5fa-318a-a9e5-6990f2cc6bdd | -14.42337 | -60.19584 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9160374e-0746-3897-bf36-bbd82f9809fd | -14.85391 | -46.6911 | 2025-09-07 05:14:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8d09e387-72fb-370b-bd58-53bd44fade31 | -19.61501 | -46.43795 | 2025-09-07 05:14:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bba58111-1210-3af8-9961-53b744eafcd3 | -20.83587 | -49.42749 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6f000e60-6210-367e-84dc-bd1fcf8db605 | -15.13748 | -52.35704 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e71c330-fa2a-36b8-bb91-c8c0bb3cb228 | -14.41746 | -49.6877 | 2025-09-07 05:14:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7411a6ce-2e8d-32f2-9c42-6f4c82bf30fc | -21.45837 | -46.92034 | 2025-09-07 05:14:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1c1f277c-ed9e-3b77-84a5-1d551d279c3c | -15.76431 | -53.65274 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 133cfe48-4c9e-39f0-8beb-01c37cfc2b19 | -14.58653 | -48.10098 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c3f40e-c023-3e71-9984-784880a07f4b | -13.9123 | -54.01502 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2e3f457-66cf-34a3-b2a2-7f1fea49a955 | -14.5991 | -48.08222 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| af37aa25-abd1-3f36-a8d2-5754540b250a | -16.69498 | -46.80357 | 2025-09-07 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7182591a-93d7-3cb1-977a-0401d2317587 | -13.28378 | -58.46244 | 2025-09-07 05:14:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 360ea7a0-5266-3232-9e6b-ae99aced90a2 | -16.93773 | -45.75471 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c4e51c0-5975-37f9-85c1-fc4148cd05fd | -15.14269 | -52.35281 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67066687-ef48-36b4-a6b1-39066608fe97 | -14.9366 | -55.88995 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92bede0e-c7a5-3160-935f-13ecb47e69df | -16.34166 | -46.85028 | 2025-09-07 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 687ca953-b05f-3360-af5a-684663c3a04e | -13.91166 | -53.98849 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c147fea3-0ba7-3fc0-ac97-aef48e042fb3 | -14.50504 | -48.76461 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4fe9a4b-6dbb-3616-92fd-2b2edd5eb430 | -14.93305 | -55.89178 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36715147-5de9-3784-86e4-a29bd5bc3f12 | -14.59271 | -48.10049 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35ce4d64-bb6a-3d0b-a9a7-5b5f9dbf5e4a | -14.58846 | -48.08216 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83e73e82-e2a9-337d-bb86-7b8e70ede2ef | -14.41581 | -49.68943 | 2025-09-07 05:14:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79b6dc40-d284-3f01-b898-2a34e6f15a06 | -20.83627 | -49.42293 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a1fbfe3a-6e51-3728-92eb-f5c960fd2029 | -14.49882 | -48.76769 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 69f1a4a5-e97b-3026-a257-917d0635285d | -19.47069 | -47.75991 | 2025-09-07 05:14:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bb0621c-b6dd-367b-8fea-3c2ba730e70a | -15.12824 | -52.35603 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37b80cc0-e6e4-3bce-a484-1aeddabedf73 | -19.88433 | -57.89691 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 280542db-5a29-3d51-8486-22a71c4457ac | -15.012 | -48.00962 | 2025-09-07 05:14:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6df0fa7-35a1-3ceb-b3df-14b935bc9925 | -14.59668 | -48.10403 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fef4c6e3-5ec5-3d7e-967e-b74b93a9f0ee | -19.8673 | -57.88995 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| cb5af50d-6de5-3c16-85ca-db4e2c8e4c87 | -12.41575 | -63.9057 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4ca74dc-37ae-3871-ae26-af5ffbfd0c54 | -17.70771 | -49.10932 | 2025-09-07 05:14:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1fba79f1-06de-337d-bd2a-4f3e11da04ca | -14.30852 | -53.42152 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5ed8f64-c679-35ed-92fa-19177bc2bddf | -13.90967 | -54.00364 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1318dcba-8dd9-38ee-b9ad-1606b29e303e | -15.12008 | -52.34626 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23b68764-9032-3513-bcf3-6123e30693de | -15.33593 | -52.74366 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40010092-78ce-3f34-a96a-f1fddda8c05e | -15.87775 | -56.47443 | 2025-09-07 05:14:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b787f7c-abf1-3ee7-9c99-e7b2ad5f02d3 | -16.94366 | -45.76871 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e28af111-f139-3632-8f63-8f9cec78d4df | -19.07319 | -46.77725 | 2025-09-07 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b85e2af3-f707-3815-9725-6abee66ae8e1 | -20.82951 | -49.43114 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| cd108167-f24b-338d-a41c-2586b348239a | -16.93586 | -45.77547 | 2025-09-07 05:14:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f100dae-421e-3774-8f3b-ba7f6bd85bd6 | -12.35754 | -63.63726 | 2025-09-07 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16ea8229-fe90-34e8-82b1-141a89b14eca | -14.59049 | -48.10463 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f076ae4c-d98e-3bd7-9058-0495e89583f7 | -18.73339 | -49.62549 | 2025-09-07 05:14:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 42ccab0f-27f6-31bb-aacc-43c58edb7938 | -15.10221 | -50.10868 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 929241e6-a98d-30f2-abb5-43f6cd410de0 | -17.38374 | -49.23185 | 2025-09-07 05:14:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40f168a1-451b-3e86-b709-329737ffb53a | -13.94067 | -54.01917 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f9d3231-16cc-3fa4-a477-be749078e60a | -16.4478 | -49.28341 | 2025-09-07 05:14:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09de4187-f885-3f7f-9bb3-94d99f16c61c | -14.59867 | -48.08604 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4fac7f6f-4b99-3f78-a883-2d401f761f44 | -15.73141 | -53.54348 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9144d09-5a35-3587-b8a2-5c3736ed1353 | -19.86377 | -57.88939 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 1b525963-a218-3f49-a615-a136e5b673f0 | -14.54325 | -53.15054 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 694d97e8-a964-3554-a9a1-13559d05a66a | -16.28766 | -45.68958 | 2025-09-07 05:14:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87da0272-6405-30b8-81ca-d79073d7bb1f | -15.72766 | -53.53867 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f25721ca-31d9-31bb-93ed-be5707e883c2 | -19.46981 | -47.77081 | 2025-09-07 05:14:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0749978-67a8-3f16-a882-d0808fc9753f | -14.54269 | -53.15482 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83fad9a9-aa7f-36cf-9809-c7a071b6fd05 | -14.59819 | -48.09041 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a91a4897-9b85-3daf-a0a4-a158622a3e2f | -14.53987 | -53.15641 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a495701-6d51-3c91-b370-6d02f89d374f | -14.93173 | -55.89803 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a68b1b77-2e83-34c9-af80-1fba1749b57c | -14.93961 | -55.81968 | 2025-09-07 05:14:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca32d0d7-dccb-36a9-93ca-63e9ed82ab5f | -13.91715 | -53.97833 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3fffbd2-dca5-3a04-8892-92e6d3f82ff2 | -14.56531 | -49.12206 | 2025-09-07 05:14:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 017532db-98a3-357a-a80c-7097c889d442 | -14.58685 | -48.08198 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c769ff6-ae27-32d3-9b07-7a42c9c675fc | -13.93518 | -54.02929 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1548fa2f-0c31-34e9-ac98-16ecab1d52f2 | -13.9092 | -54.00723 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9bf5f83-49d9-3693-8d7a-5c017703cdd5 | -14.49256 | -48.77109 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6fc267f8-8f95-367e-9183-7b52de7adbbe | -19.87728 | -57.8958 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| c4ae670e-352a-31a6-b0a8-eac99dde0598 | -19.88081 | -57.89636 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| c327b34a-ee5a-3818-8b7a-75c624480e0f | -15.17814 | -47.96922 | 2025-09-07 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d5c943f-ed0a-380d-b050-c08f51a9e4da | -16.29694 | -58.10007 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a5acf061-1842-35e5-ad07-be162d5b0a86 | -14.53783 | -53.15821 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ce9af95-66e6-3030-8816-47ed1479bb74 | -20.54529 | -46.44917 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80c66c40-9f93-36b9-afdc-a41276cb6f1e | -14.58098 | -52.13884 | 2025-09-07 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3ed2d9c-e03c-3056-8da4-8e2aa406c20a | -13.92119 | -53.97904 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b890b3da-dd8f-3b8a-9a50-aee463bd2e9d | -14.5404 | -53.15217 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eca1e81c-a8e2-383b-ba96-419906cedf3e | -15.72713 | -53.54285 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21012f8b-fb78-3564-928a-a1300e133aa9 | -19.55768 | -49.73848 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 66470179-d6bf-3176-b727-bd839d0fe77e | -20.5486 | -46.4449 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 00fb165a-6338-3239-86c8-04e64737eda4 | -15.76485 | -53.65481 | 2025-09-07 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e40b1ce-7bc7-3567-88bf-1f162fe46612 | -13.91277 | -54.01147 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9929064-32dc-31f5-aafb-bfbf22fb48ce | -13.90208 | -53.99849 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdda329e-5c33-33b1-a198-2b91239065ae | -15.10259 | -50.10547 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d34de67-589d-3c10-bc4a-f31d0ff35169 | -15.10297 | -50.10213 | 2025-09-07 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0823216e-54c4-396e-bd1a-9d1a29b81a1c | -16.28119 | -45.68169 | 2025-09-07 05:14:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb19c7e1-2d11-3dd2-bcdc-7ce51e085f92 | -14.48677 | -48.77034 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36167263-e696-30ba-9839-44831d146d93 | -15.8404 | -52.30104 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eaa1715d-8fac-3ece-bc3d-334460bdd8e0 | -16.44738 | -49.28744 | 2025-09-07 05:14:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c291baef-cdea-3f21-bd31-9b385f441663 | -14.85227 | -46.68724 | 2025-09-07 05:14:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3bd06998-80f2-3d47-be07-ee00af78e7b9 | -14.35274 | -60.31981 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25165049-9486-33be-8828-acc8f0cdfb0e | -12.42157 | -63.89587 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c1720e3-7f74-3155-b29a-0c85e871d6c1 | -14.82613 | -48.18547 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3f6b799-74d4-32a8-9586-32bf3aea24b9 | -14.4437 | -48.45551 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0967e87-bbeb-33cb-8e04-822af7f6837a | -15.12465 | -52.3472 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b61d58f3-3fd5-3d66-a482-47d6aadfc0ba | -13.90825 | -54.01439 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e77cb64f-c6ed-3513-b50b-827401394d35 | -14.42395 | -60.19225 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61a49125-1717-3f6b-848c-006e1f010ed6 | -14.54418 | -53.15722 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f9c4116-16dc-3453-83a1-812faff258bd | -20.83301 | -49.42697 | 2025-09-07 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| d6d3f65e-368c-30db-b5a4-4e98deba5331 | -15.83899 | -52.29807 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c90db426-b2c9-3504-8a12-d383d9b1ba45 | -15.12364 | -52.35534 | 2025-09-07 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README76.md)
