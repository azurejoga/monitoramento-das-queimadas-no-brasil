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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 021bfa38-71df-386e-8117-c1326efc5246 | -3.1884 | -54.09485 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faceb288-29f9-37c9-b3a3-c2daceff2997 | -2.79018 | -54.10051 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f0ae005-c428-33a6-829e-e9c905d790dc | -3.11173 | -53.74375 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0172801b-15b9-3d6e-b526-148c74b97eef | -2.8149 | -54.09584 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ffbc253-45bf-3c65-ad18-0dc08ea5a2ff | -1.25044 | -55.88081 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8bb62a7-421e-352f-8f22-5fde00b70166 | -2.95504 | -54.14772 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 33646556-8a16-315e-8513-c35001b42e96 | -3.88053 | -55.80839 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e411457c-8aa9-3a2b-9d89-01c7fcc37b5f | -3.10101 | -53.73285 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cff01113-d027-35ef-9f76-f038b1693623 | -3.36317 | -59.41594 | 2026-10-05 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e692f266-1981-3a3f-bcf6-b53a3aefcd31 | -2.16728 | -53.66593 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca3fe17c-1778-31ef-ad22-2007410ae51f | -6.21516 | -52.68359 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ef3f6ed4-90f6-39b0-94d5-c6dcab1e150c | -2.81239 | -54.11269 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb8e7e8-cd05-39ba-9075-7b26a68880ae | -3.11042 | -53.7216 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 14d5ba68-116b-3a62-a5bd-671ffeec91fb | -3.5109 | -54.61223 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a856ecf7-ef01-3b54-b575-d46ded60bde9 | -6.20658 | -52.82716 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e002463a-5af0-344f-a2d5-9cef86206945 | -3.50611 | -54.61493 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ab855d6-db72-36ec-97e1-96388a232953 | -2.54331 | -65.87599 | 2026-10-05 05:42:00 | NOAA-21 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b20c0adc-ff56-32be-a523-ce9fb673f734 | -3.27726 | -54.17679 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b46b3e2b-ea46-39e8-9f10-65e83b8e5eca | -2.94529 | -54.13926 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a1a8996-c93d-3b72-8e4d-093b6d390c02 | -2.7837 | -54.10374 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 82e3b1ee-801c-3d0e-8a66-510d2dbee61c | -2.90481 | -54.12888 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41748080-7b3e-3a4a-8f17-2bad8dbac7e4 | -3.10169 | -53.72831 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7896bb97-2e19-330f-aa60-ee5b80e49427 | -3.12055 | -53.73717 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc737d3e-9ea8-35d7-a48b-7d42e8736074 | -3.32316 | -53.85584 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fd071dd-434f-3fd1-8ee5-cd49bd91b068 | -3.57246 | -55.41515 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b961ab6-6270-3221-b71b-03cb6c38f736 | -3.12854 | -53.72449 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4cc71ca7-b9cf-3fcc-913a-3c092ad3dbf8 | -3.06058 | -54.16458 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af000cb8-c798-3e2f-aab4-c05e03bdf481 | -2.78246 | -54.11218 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6861822-e3bc-38de-9756-5db59f8497f7 | -3.08261 | -54.16953 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 70158420-6a26-3ab3-87db-d8a0b80a03f2 | -3.11516 | -53.73163 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16f909ab-3aa4-3dd4-bdf7-a57489a91617 | -3.37809 | -54.10609 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 509499bb-4ffc-3401-8ec6-a538d85972b0 | -3.1044 | -53.71012 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 87f08960-cadc-33ed-9709-55b3e915e3b8 | -3.1164 | -53.75373 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 755160f8-ba73-3438-8489-e0a8d8812ce4 | -2.93454 | -54.12319 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2ae548ce-39b5-331b-b89e-925d706ca0f3 | -3.11387 | -53.74072 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10ae8a53-4184-3aa7-8ea4-378c84c621fd | -3.30704 | -53.83951 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd5810b1-c404-3f71-9535-3b809159d936 | -2.7948 | -54.10993 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84502e5b-a7ae-37d0-91a7-729b9121586d | -3.12314 | -53.71901 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a4ee0ee-cd15-33f3-868f-67256dbb3381 | -3.11444 | -53.72564 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39e14247-215b-3d1d-b4aa-c147b4dbc183 | -2.22518 | -53.70779 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4784bb25-a9ef-3140-b270-c8afd9550e29 | -2.94631 | -54.1249 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28876936-8834-32b9-8382-384c28ded80d | -3.18244 | -54.09427 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69bf32c6-7127-3f38-91e4-c641de866d10 | -3.11112 | -53.70656 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 45fd6490-649a-3a1f-8b16-48c9feda05a5 | -3.11043 | -53.71112 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 77b0bcd4-9eb4-3b57-9ea7-b3ceaefaa7b4 | -2.90521 | -54.08545 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8286b069-1e31-3db0-a04a-a0abd2517592 | -7.22311 | -55.19168 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc71e506-6758-3424-b96a-e8681e3f4991 | -3.17363 | -54.0834 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d189f3c2-a6e0-35f2-9fa8-29d03b7e64b0 | -3.51129 | -54.61975 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b0b2c1d-fcda-371b-86d8-d48d9e3096ea | -3.18778 | -54.09914 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2870a2ed-7cc3-3109-9c38-63b2fcfccf2a | -3.326 | -59.47545 | 2026-10-05 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c63386d-9987-36dd-b85d-a0a81f93bdc5 | -2.90458 | -54.08969 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 29266b85-64c0-363c-bad9-bfed54f7d56b | -2.82329 | -54.11155 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85a31c3d-b00b-3332-8a66-6dc0bc470bb0 | -3.07486 | -54.18161 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 520612fb-e032-3202-99c7-3a5537ab49b5 | -2.78956 | -54.10471 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e47812b6-f488-31b6-b991-2fa55b986995 | -3.14128 | -53.72182 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64347c37-7366-38c1-b701-4dceb4f8d500 | -3.04942 | -54.23352 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a01fd06-7733-320f-abe3-76ae899dae52 | -2.95347 | -59.16182 | 2026-10-05 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7f9143f-f6e1-34ea-839a-c1d97fd791e1 | -2.16133 | -53.66485 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 081e7530-53c5-381a-9f49-6d47851560f6 | -2.59544 | -51.84954 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61e8130b-b199-34f0-b4d3-111f1690f4d4 | -3.13393 | -53.72994 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 418c6bc4-e689-3704-a422-8f8af120438d | -2.80652 | -54.11179 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6434098a-572f-320a-a784-b9e21ba66605 | -2.81176 | -54.11692 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f4c219-0787-38dc-b6fb-344844585d1c | -3.22031 | -53.87282 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01f3fd06-b34d-35c0-8614-c2150ba91c73 | -2.22451 | -53.71226 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73606fdc-e7aa-3cdf-b8f5-25836948e0f1 | -2.48425 | -56.09156 | 2026-10-05 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10a43bd-cc5d-3ce1-b80c-0cfbd1b1b758 | -2.79542 | -54.10569 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeecad56-250f-3e98-9ca8-3d9a383f7db8 | -2.81365 | -54.10426 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0260de50-00db-34cf-9d63-c801df13d95f | -2.86278 | -53.91918 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dd585a1-a766-38b5-8a87-d6f6863573a3 | -3.30351 | -53.84945 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3192db29-7539-3849-89fb-773d1a124281 | -3.6762 | -55.51584 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a907cbaa-24af-39ac-b2ae-53e80c0fc1f4 | -3.22694 | -53.86935 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e6c8444c-a74f-3e45-b0e0-7c58674669a1 | -3.13523 | -53.72088 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8d2e7a6d-0e5e-3096-8ab2-863b5a310d62 | -2.5784 | -51.87187 | 2026-10-05 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 787df193-8e93-3853-a961-2ebd4de10e1c | -3.10367 | -53.75636 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 073d5a77-fd0b-3cac-b03c-ab93f6c704b9 | -2.81051 | -54.12533 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 290c0993-b645-3e08-9129-813592a53029 | -2.93607 | -54.12065 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 870af3c0-ea0b-31c1-ad31-33d70692cad1 | -2.81302 | -54.10847 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28a289cd-e09c-30d8-bf87-56093352283b | -3.97552 | -59.33878 | 2026-10-05 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78398a34-8a74-31fd-bf3a-5c50b96b0cc2 | -3.99029 | -55.81815 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 994c8b7c-0a20-32f8-9f24-ef105b2fb192 | -2.99174 | -54.1018 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b61471a4-14c1-3404-acc1-b4f086abdeb1 | -3.07611 | -54.17297 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 36f371d8-437e-3515-be88-388db12756a7 | -2.82389 | -54.10735 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db4e07cb-1f92-3bcd-8c6a-fc2dc00af639 | -2.81952 | -54.10519 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffacf8ab-f83c-3b51-910f-f74eedbabe4c | -2.82224 | -54.1271 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db997feb-4ad5-3df6-9674-8a73884de3ba | -2.82269 | -54.11579 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca9a713e-7e37-3c28-9525-150e8e1c5a6b | -2.94189 | -54.19754 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f9c19c4-793f-35ad-9318-807b68ab574f | -2.95565 | -54.14347 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4efa1de8-1894-334d-80e8-b6b1500d0eeb | -3.98447 | -55.82078 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c25e33f-26cb-3b36-8412-0ce6b563b039 | -3.32749 | -53.38971 | 2026-10-05 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62239b09-ff83-3079-83c6-11e1058ecb69 | -6.20579 | -52.83324 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca6452b7-9a00-32f2-a470-1ed3f3bf28dd | -3.18372 | -54.08534 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c101edaa-d624-3f46-a708-1a302d40ab53 | -3.11241 | -53.73923 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 519f38b1-c6ec-3b6e-ba79-6228582c1ad1 | -2.95643 | -54.14502 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c698be18-426c-3bae-8716-d6ba24ecaad4 | -3.84264 | -55.84391 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c86ffee-f15d-36f7-8528-8c2eb304de31 | -3.1186 | -53.75075 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6ac547f6-75af-39ee-bf3d-fa0ae4241be4 | -3.08197 | -54.17392 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 706bcbbd-0908-3fcb-a68a-82f2559e3f3d | -3.11708 | -53.7492 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a83c5841-0093-3b09-a072-813b785c772c | -6.26489 | -52.84816 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4af84ac-b4a1-3d02-a468-12561c048efc | -3.51703 | -54.62065 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86fb6112-f9c3-3f77-a4b9-f85064892398 | -2.57695 | -56.1559 | 2026-10-05 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README53.md)
