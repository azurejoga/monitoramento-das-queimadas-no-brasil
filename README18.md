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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64153d05-fe04-3040-8dce-24d0a3119ac8 | -13.89538 | -54.63488 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ffca945c-a202-3ce7-a59f-d0f1be50c496 | -13.89268 | -54.627 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44735ddf-e8f2-3959-9c76-51912637beda | -17.65599 | -47.45516 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de7913f-34af-30b6-ab4d-b2b1c88afd68 | -11.90999 | -57.47063 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9f3a5e9-bf7d-36af-8e52-badf32cf8047 | -13.89808 | -54.64277 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5299388-95ac-339e-bfff-910f6e685b11 | -17.65458 | -47.45816 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1aaa396d-2222-3660-bef7-ab5ddbac717f | -13.90129 | -54.62506 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cc4ecdb-40b6-39a0-be09-05dc3ce733cd | -12.47306 | -58.47181 | 2025-06-13 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7125a959-c65e-3754-8dcb-068ed9b3b93c | -17.65576 | -47.44965 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 515ec0bc-cf84-3218-aa19-20e79df3c487 | -12.43198 | -54.86886 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 012a7c5a-da1a-3407-a71f-22ddd4f5ff8b | -16.50162 | -45.03767 | 2025-06-13 04:34:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 309e5e36-b608-3e63-a057-6469e6ad4964 | -12.42782 | -54.86807 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e137a26-73a1-348c-80f9-bbd817bfb22f | -12.43063 | -54.87654 | 2025-06-13 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc5b70a-fab5-3db3-8273-f473e6d58aca | -13.90256 | -54.61805 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82ac7cac-951c-33cc-9e90-810a7deaf248 | -12.51586 | -57.23724 | 2025-06-13 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0138e489-6706-3d86-a232-dda7d7cd1e0c | -15.36516 | -47.8675 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e09589b0-c64a-35b5-acc7-2ab499e58d66 | -14.02325 | -55.12749 | 2025-06-13 04:34:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78374410-fad6-3a42-97b5-4367055b7e8a | -13.90192 | -54.62154 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3004a9b3-ff55-35c5-931b-13846f2f6cbf | -15.38515 | -47.87477 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e564a068-9162-3607-b253-2bfb2596ff13 | -17.66586 | -47.45554 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3ee7ebe-ed7b-3002-9494-a1e96baab4fc | -14.66714 | -53.36179 | 2025-06-13 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5e3c0a8-5c22-382c-9bf0-501b0a34f729 | -13.9715 | -54.4395 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06e19ff1-7dfa-335f-853a-2e7222b95019 | -19.57955 | -49.11139 | 2025-06-13 04:34:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b57d8003-dd27-3f5d-a38e-ce212655d6af | -17.65042 | -47.46188 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d6dc9ff-ab91-32a1-8e42-b3008874318d | -12.70677 | -58.03922 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64d92ad3-86ab-3119-bc73-b6c2b9ee453a | -15.07748 | -48.94362 | 2025-06-13 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebff8d3c-dc51-35a8-97e9-bab8bc0c150a | -13.58482 | -54.27976 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd9c9885-2f53-3669-8054-ea9aef723b37 | -13.35484 | -52.28176 | 2025-06-13 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 807c93f4-36be-3fad-907d-a7691e4a04d5 | -12.70168 | -58.03819 | 2025-06-13 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aea3768b-1632-3e98-816d-167994468d56 | -12.46843 | -58.46746 | 2025-06-13 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd921f94-ee17-3b38-bf0e-92554f91b0b2 | -13.09273 | -52.28472 | 2025-06-13 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7db83080-b6d9-3c5c-a128-37e6501b230c | -15.38571 | -47.87096 | 2025-06-13 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b14ae9b-7eb7-356d-92f9-01d5e554616f | -13.89857 | -54.61726 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6b8e055a-4e33-30e9-ba10-b535dfa9d376 | -15.52877 | -49.62387 | 2025-06-13 04:34:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 622ba6c5-3b5d-342a-b3d1-0c31366c8ea4 | -18.40644 | -54.57142 | 2025-06-13 04:34:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9d6dd44-f1f7-3f04-b306-151ab659cf65 | -20.45951 | -49.74977 | 2025-06-13 04:34:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aed109e-08cd-3e73-94c0-6f30ddc3a9c2 | -20.41428 | -46.445 | 2025-06-13 04:34:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7184537d-f1a9-36fe-ac43-03876313844c | -11.92128 | -57.46547 | 2025-06-13 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 494859be-37a5-3b68-90ba-76c44e5b9951 | -19.70323 | -54.61485 | 2025-06-13 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01a7d7d4-2af2-34b1-8d69-9a170def6c28 | -15.93216 | -46.76411 | 2025-06-13 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5b0b6b9-fe94-3a82-b8c7-826b78de01f4 | -13.89331 | -54.62349 | 2025-06-13 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7af3575a-c844-34f7-8457-00ef77d2a21d | -17.65181 | -47.45888 | 2025-06-13 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a342a216-b63b-36cf-a1d2-3c288082950b | -21.54247 | -56.04871 | 2025-06-13 04:36:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0ae2cb7-a5b1-387f-ab95-b6f2f928180b | -21.17097 | -53.29859 | 2025-06-13 04:36:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c5d81a-451d-3ceb-a805-67e7fcc01fe4 | -20.99734 | -51.79127 | 2025-06-13 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3700763-566c-3f65-bed5-842cdd011207 | -23.59335 | -47.43844 | 2025-06-13 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 82f9d09a-3087-348e-b96c-2b8c287950b6 | -21.67255 | -56.6315 | 2025-06-13 04:36:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c39623f4-32ee-3196-8e43-03b70985f1cd | -21.19504 | -50.65963 | 2025-06-13 04:36:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e97f3608-9b8e-3af5-8abe-ce551576bd09 | -22.77133 | -49.31253 | 2025-06-13 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 274eb2bf-04b8-37cc-8a50-f6f22c4d5155 | -21.45672 | -48.5153 | 2025-06-13 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dde47a89-6895-35d7-b26b-d974ece4cfee | -21.34877 | -48.58999 | 2025-06-13 04:36:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0f7f4fe8-722c-3c7d-a017-7bdc44d116e9 | -22.77074 | -49.31666 | 2025-06-13 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff87d18f-bc0a-3fc7-b348-255708481627 | -23.23684 | -51.28461 | 2025-06-13 04:36:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 98a70bce-42f5-3d26-bdb6-dc68856385ff | -22.76727 | -49.3161 | 2025-06-13 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f078f1d-cc93-3808-890f-48cb496cfe07 | -23.59497 | -47.43779 | 2025-06-13 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87648bd6-72b2-3d9f-ac7c-5a316be5eb2f | -22.62783 | -47.35239 | 2025-06-13 04:36:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 647f27d4-b8f4-352a-a206-24c15448f3a7 | -23.9841 | -48.9157 | 2025-06-13 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ed0b3e1-4a5c-392e-aa2d-bda0308b3238 | -23.33819 | -46.77126 | 2025-06-13 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd20f38d-d76f-3911-abd2-0b09df0509d8 | -22.62799 | -47.35514 | 2025-06-13 04:36:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36fa33a4-923d-3e28-9490-474e7178c6ea | -21.61551 | -57.57468 | 2025-06-13 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25c2d441-f150-36d7-858b-29c982378a63 | -25.19175 | -49.32517 | 2025-06-13 04:36:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 84dceb42-0349-368c-ac0c-20bbb320a510 | -21.61474 | -57.578 | 2025-06-13 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 199554e5-64eb-3898-9fd5-7cc3532a3dbd | -21.19561 | -50.6559 | 2025-06-13 04:36:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8dd7ab68-2dd5-383f-9e28-76234c4b9575 | -23.50539 | -53.72786 | 2025-06-13 04:36:00 | NOAA-20 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 192994f4-ad36-3a3c-9687-b91bd7bd15ef | -21.45732 | -48.51109 | 2025-06-13 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a4da554-5925-3558-b2a0-87cd655cc762 | -21.34452 | -48.67057 | 2025-06-13 04:36:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5cda344d-78aa-3af5-a087-6d8de02eaefb | -21.34804 | -48.6711 | 2025-06-13 04:36:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 71aa5ffd-5a1f-3d5c-a5f5-174d6a63b45f | -21.6147 | -57.57887 | 2025-06-13 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76fdbd86-41f1-30b8-9add-a1d718a368ff | -21.67356 | -56.62612 | 2025-06-13 04:36:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01d92f86-1f9f-308b-8f4b-2e15a9143a6d | -22.53955 | -48.81266 | 2025-06-13 04:36:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e048297-6e2c-38ab-80b2-2331dfd9d549 | -21.34818 | -48.59416 | 2025-06-13 04:36:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9e5bda2b-11f6-3881-a123-9826e202565c | -21.61557 | -57.57384 | 2025-06-13 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a07c93c-7b9c-3e90-a8fc-c1afb58d6dc2 | -22.10658 | -47.017 | 2025-06-13 04:36:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e36a12ca-a757-329e-977e-9ed35f696eb4 | -21.53863 | -56.04792 | 2025-06-13 04:36:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0144a8aa-2422-35e9-be00-7ed110407a63 | -21.94154 | -57.26957 | 2025-06-13 04:36:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef929a9c-7afa-32bd-92c4-337ca93f049b | -29.28979 | -52.42432 | 2025-06-13 04:38:00 | NOAA-20 | BOQUEIRÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4302451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 96c0ab9b-87c1-380b-8c93-a27c5b3f5bef | -30.18913 | -51.1763 | 2025-06-13 04:38:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 0194e8f7-6b30-3988-860e-1c50432f4c23 | -28.58701 | -49.44378 | 2025-06-13 04:38:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f8859fb-7fac-3722-b671-b9853947fee6 | -8.07 | -43.1216 | 2025-06-13 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 82c4d395-ca2d-387b-9b89-32b94eea2c65 | -10.6492 | -49.4267 | 2025-06-13 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 5b539d3c-49bb-349b-a08b-0e3b4e43223a | -10.9355 | -56.8322 | 2025-06-13 04:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8e5d4524-a9de-3d6a-8302-b75774a4f265 | -13.9059 | -54.6291 | 2025-06-13 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| b2fee1ae-94ad-3e1c-939e-f650ce396f24 | -13.8867 | -54.6312 | 2025-06-13 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| facace62-1b6b-331a-8532-dd52f5b61c1f | -10.9167 | -56.8336 | 2025-06-13 04:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b9223f68-468e-3491-ada5-a844ea2c2aea | -13.9059 | -54.6291 | 2025-06-13 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b9496f22-d7fc-3c44-af6f-3b7d6344c48d | -13.8867 | -54.6312 | 2025-06-13 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| a0931590-39e3-3095-9dd7-08e8851ae054 | -10.6492 | -49.4267 | 2025-06-13 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 23d4b420-b691-317f-9839-4ced4a411869 | -10.6483 | -44.4861 | 2025-06-13 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9b824862-a666-39af-ade3-c850f5001dd8 | -13.8867 | -54.6312 | 2025-06-13 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| fa40d517-6ab4-339c-8360-a99b00fdb1bc | -13.9059 | -54.6291 | 2025-06-13 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| d0056354-d4ee-35f9-a223-312832f19459 | -10.6492 | -49.4267 | 2025-06-13 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| cd6d6b36-386c-309b-bb35-8183fa401f13 | -10.9355 | -56.8322 | 2025-06-13 05:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 91c178e3-c519-355c-aeeb-2a9e3e06aa5c | -13.9059 | -54.6291 | 2025-06-13 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 28ab9d5d-e80d-31ee-9abc-7896c391f066 | -13.8867 | -54.6312 | 2025-06-13 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 429c67fd-627e-3a56-8624-80e0519352ff | -13.9059 | -54.6291 | 2025-06-13 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f6bc5411-0683-3d20-90bd-5c52b8127503 | -10.29564 | -57.1375 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba58e70-ba71-3033-96be-13cf3d2b2005 | -9.10685 | -63.55797 | 2025-06-13 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7880137b-d279-3250-95bd-e7b3ab95f7dd | -10.92816 | -56.83728 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8cf77271-100d-3a7f-9360-68a9e67f99a5 | -5.12297 | -56.11514 | 2025-06-13 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d2dccb8-429f-380c-80d4-ceae3c047004 | -10.64529 | -49.43006 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README19.md)
