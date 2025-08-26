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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ffe3920-1dfc-344f-b021-cd770617fb3d | -9.64221 | -59.63401 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4611f1c1-b585-3784-9f87-9aec1d313e2d | -9.16723 | -60.77421 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ed0206f-d4a0-37ce-9a96-d85fe05f2625 | -8.98431 | -65.42384 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2b37927-e109-33c6-a4d8-b9be232672bd | -9.0149 | -65.38161 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a0865fa-6434-3bf9-ad8e-61301f59aced | -14.97181 | -52.87943 | 2025-08-26 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69d486a3-28d5-3ecd-ab19-991674c302b4 | -9.16585 | -59.53947 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac75613c-10fe-359c-b660-ca4c1fcb9861 | -9.25906 | -56.90575 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c03013f-0662-3d51-9378-6b489433f74a | -9.20155 | -60.91769 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 663b5ce0-9e63-359a-8451-1fc3f990809c | -9.10579 | -62.67566 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3172550-c452-3067-8b1b-465653bed228 | -9.9569 | -64.86551 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc966c1c-7ce2-3354-8f52-f567d5210443 | -9.16936 | -59.54361 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45484744-394d-3edf-bf69-bed181523ad5 | -8.97042 | -65.42525 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88ece004-4636-387d-88ee-4aee0d568fd4 | -9.31483 | -63.43916 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3358b30e-ab40-3c87-9165-5ce7bd31df48 | -9.18982 | -60.78906 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f04aec1-6d0b-31c6-ad1a-5bebb5e9ab5f | -9.17183 | -59.52599 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81f36d0b-95d4-3e70-a38e-6dfff9502e5b | -8.51359 | -63.87242 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bba1627a-5a66-3888-b4e2-e12d79b28997 | -9.1959 | -59.5295 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2ea3ba4-6f72-33f7-b063-15c270d46937 | -9.0826 | -66.0649 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a2b9606-2e26-3489-a09a-9dec7af50fb2 | -8.54332 | -62.63993 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a16898b6-b7a1-3427-b20d-3ca3d50248a9 | -10.82188 | -62.44608 | 2025-08-26 05:38:00 | NOAA-21 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 125c34f0-6b99-3a0d-948e-bb5989af971c | -10.45322 | -58.00124 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e513b77-da0d-3cae-9b71-6067df7c0339 | -9.16437 | -59.55002 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d677ad3-1732-30e1-825e-a687392929bf | -9.18336 | -59.5313 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a4d4de21-ebf0-3db8-aa67-4843af6f1222 | -9.58143 | -55.37482 | 2025-08-26 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 006beca0-3b16-3871-8ba0-69172032672c | -8.53936 | -62.64309 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98a6536d-1fc4-3b27-ab13-990fce5d9aa6 | -8.55068 | -62.6373 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c96a313b-7c41-3e03-af00-a25a667ebafb | -8.85888 | -62.4553 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 591cd229-959f-3343-8810-cf6794de7ca2 | -8.68628 | -62.87867 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 984cdb36-4a62-3c54-a602-45bd89c07a8b | -8.54784 | -62.63309 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cf6af32-2de6-36d0-987f-e4eecf7dd1bc | -8.86343 | -62.44832 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 025dec80-0e67-3669-a925-e8cac9e5c8a3 | -9.17331 | -59.51543 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86c46471-b713-3c02-bbc4-87e9983c61d9 | -8.98543 | -65.41676 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 008fabee-4d4c-3900-9d79-e1cfa2c77e40 | -9.04638 | -65.74028 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80d20b08-af34-307a-bbd3-5bf88544cb3a | -9.07946 | -65.71985 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1cdca94b-10df-3661-817e-b52c3f8077a9 | -9.0895 | -65.7215 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 038c725c-ff9e-3644-92d1-2ca42f02deb2 | -8.61272 | -62.60095 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 314db58a-bc61-31dc-ba16-d1d11f8bf8eb | -9.02406 | -65.72935 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 844490c8-6577-3540-a429-9cead44c5175 | -9.26936 | -56.90193 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec956e97-4fd0-3a02-a9c4-47a2c828a2e0 | -11.60062 | -63.49129 | 2025-08-26 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46901f24-8ff5-3bc2-949b-4fe866069b38 | -9.18684 | -59.50663 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48a2a235-c65f-38bf-822e-bf06293b11ed | -9.65123 | -59.62813 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61f5d00e-c013-3175-bb7b-8d16bc48af84 | -9.18237 | -59.53836 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 753ee939-7cd8-321e-ab1f-9fc27ae2f104 | -9.09678 | -65.719 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8c73fe6-48ff-35e8-9baa-fbfcfd84be7f | -9.26863 | -56.90724 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a285c56-126b-3730-9cc2-aef0f287e084 | -9.07247 | -66.06325 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3ce2f5c4-b676-3229-ba7a-e3f6f606b664 | -9.18083 | -59.52016 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a25b25a2-2194-302d-a907-823641aa792d | -10.10513 | -57.76707 | 2025-08-26 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c795013-100a-381f-8bc9-16a9b38d0cf4 | -9.08004 | -65.71626 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ae5aeb4c-a60e-32f2-a5c5-0f88dd0b81a0 | -9.18232 | -59.50959 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf7d2479-ec57-36fa-a6f5-5bec07f5a63a | -9.16381 | -59.52477 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd2383e4-e882-3ada-af8f-baa1663a6ceb | -8.98378 | -65.40562 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb54dbd8-8f0b-334e-a613-9007e52bb72b | -8.86456 | -62.44082 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37aa3582-7c70-376f-b143-049dfbab55b1 | -9.47412 | -57.82608 | 2025-08-26 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1d5dffb-da83-34d1-b549-3a8619c9be3b | -9.17803 | -60.79185 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 527d944c-342d-3d53-b7fe-4490292fc239 | -9.18124 | -59.45874 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 50a70978-6ea7-32fe-8073-2624822e0111 | -9.49799 | -64.75624 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0dbdb29-1723-3107-b7e5-0ac4edcb9d62 | -8.54896 | -62.62574 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d71a862-1f1c-3b69-9b57-e3e0aaa0adcf | -10.41198 | -64.41322 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9e27b8a-44fd-33a9-a089-3abbcc44a097 | -8.56368 | -62.62046 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 468f47aa-243d-36e4-a701-1f4997ec003b | -9.18837 | -59.52481 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 772e6956-faa9-3db4-b640-82875f7c1e0c | -14.43022 | -56.45067 | 2025-08-26 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5674a522-46f1-3267-bce8-af494242e95a | -8.56708 | -62.62101 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78203520-f45b-3b66-886c-d006cda14902 | -8.84287 | -62.44518 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 567a2fba-27af-3e5c-8743-08caa9dfa9f7 | -8.90286 | -62.4659 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b81fbb1a-43d8-39c0-9023-e8c19de4a82f | -9.22129 | -60.91163 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c5ed2f1-5575-31dc-8ad7-14450af74270 | -9.18918 | -60.79355 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11f963d4-eee2-3894-bbe5-a6131685aae7 | -9.65073 | -59.63166 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5566a4a5-0281-3aed-84b4-f86254a4184a | -9.25861 | -65.62457 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70976141-bc27-3d17-89fd-8d5dea98a1fa | -8.57331 | -62.62574 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6292c6a-5e12-3b0f-9a85-c1c82e95a96a | -9.00854 | -65.69745 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7f4b207-cfd3-33e8-9a7e-7ca75c8e6d4a | -8.99375 | -63.64643 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e3a4a1-693d-3bb8-b5fb-b4a513ace651 | -9.13988 | -60.77938 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f81facac-9a3b-3dac-a4e3-614067eda474 | -9.31538 | -63.43561 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa54b64e-75aa-37ec-91c4-4c7a79dd537d | -8.90054 | -62.41174 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d0c444b4-241c-3cdb-9cfb-99ac36540de1 | -11.55112 | -52.10291 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41bcfa26-1aa5-393b-a4c8-5243b3be6275 | -8.86282 | -62.42902 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b47fdc5e-e036-32b3-a1a7-cf41cd736db8 | -14.11312 | -53.97857 | 2025-08-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d06eef01-7706-34c2-aaf0-f5f6c9944e91 | -9.07718 | -65.71949 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a8a1a97d-e824-3825-98e6-844076c24282 | -9.01687 | -65.70982 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ffab040-79b4-35bb-a37e-429ff7bd1511 | -11.53422 | -52.13164 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8cf2fc93-c4ce-300c-9a4f-736531d99f41 | -9.08307 | -62.66455 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e234f31f-1193-334d-b5c0-68da1e7c53c2 | -8.57334 | -63.92461 | 2025-08-26 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76cb781c-af6a-3035-859a-1f276b2589b0 | -9.01467 | -65.70209 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02675d33-ac1d-35d9-acae-a0d9d5b35e0a | -10.41908 | -64.38926 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee5c3392-fdc0-3075-b5dc-1703f0592e73 | -11.56052 | -52.10337 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91b74821-4cd6-3488-931d-e712c1f72bb6 | -9.00377 | -65.40881 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dc3a449e-c8c2-3c0d-86ad-7eea5952f728 | -13.04055 | -56.84901 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2b006b7-9268-32d5-8392-198b49b471bb | -7.74894 | -67.1524 | 2025-08-26 05:38:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a1e61ea-f54b-3398-b6cd-be122801f16a | -9.25148 | -60.91167 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08031fc0-bc3d-3106-a6fa-dbe4443bfbdf | -9.19138 | -59.53247 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57e15f1e-484c-3e40-97cf-e275cc686dd7 | -10.3957 | -57.69295 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69b84cbf-760d-3a77-bade-8bc017c7dc4a | -9.18074 | -59.4623 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2424672f-b5c6-3320-8bb1-6a6e16842933 | -9.17931 | -59.50187 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ebab5fe-6066-364a-a2b4-da2732150ea3 | -9.15939 | -59.55644 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 14eca800-9077-3951-83e7-99d083ddccac | -10.25263 | -59.10941 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6227196-de52-3244-afb9-0efba24fcd0b | -8.86057 | -62.44405 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4dc3dd7-edc3-3b48-8d85-d0ed9e1486cd | -9.16979 | -59.51129 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d1b0904c-0494-3a75-acbc-f6f0e586178c | -11.55508 | -52.1283 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b3713e7-d469-3874-99dc-ed16b32e9c67 | -9.26687 | -59.79169 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 491c34d0-5209-3839-8a3a-c0a491f9e8bc | -8.85203 | -62.45425 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README85.md)
