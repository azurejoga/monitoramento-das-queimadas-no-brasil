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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e97c22-4e22-3822-8744-e3b1bc0c62e6 | -8.42769 | -46.38535 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fc1ef82-c11b-3c07-ac3e-d901613ebd0f | -8.4275 | -46.29994 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 38e4bd2f-ee1d-3eb2-ac20-38652a52983f | -8.42695 | -46.30342 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e001009e-8bc0-35c0-b94a-5003eceebe2f | -8.42641 | -46.3069 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d4bd018-e8c8-39a2-900f-3085d95c833b | -8.42602 | -46.37441 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 247eda0d-932a-345e-8041-8c855e89bc10 | -8.42596 | -46.85347 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f9089ea-e632-305d-943b-157f70f6d228 | -8.42473 | -46.29594 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e304421-e895-39e8-861c-d1ff28288619 | -8.42439 | -46.38483 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dcf48c6-f9fa-3ff8-8b88-772ccd3ba8e2 | -8.42419 | -46.29942 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1acb8be6-a987-322f-b8c8-e6ea42f057e9 | -8.42375 | -46.84603 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2390058-92db-3e77-9fa6-e7c559134d16 | -8.42311 | -46.30638 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac15474b-f93a-387b-91ad-871ddc9882ba | -8.4198 | -46.30586 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c215a7bc-f417-3067-954b-70e648f52cb3 | -8.41596 | -46.30882 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5003cddc-4bb2-35ea-b8b6-339de5d12609 | -8.41542 | -46.3123 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbc6481a-9a5d-3cfd-8d53-7beffb854b95 | -8.41103 | -46.31873 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9a77617-465a-3aa2-94c1-8d874a238b99 | -8.40773 | -46.31821 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38372f0e-426b-3916-938e-3125540b4b4d | -8.40719 | -46.32168 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d1c7a9b-564a-3855-8bad-a3d994172d95 | -8.40664 | -46.32515 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb5866f6-2994-38a7-bc1f-fa5981d21b0a | -8.40388 | -46.32116 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea188234-682b-3eed-be0a-c3180f7b1230 | -8.32765 | -46.63567 | 2024-10-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de3ca5b6-ef43-3a91-9d05-788a21369070 | -8.3271 | -46.63913 | 2024-10-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ebd6b8a-ff3d-3a1d-b31a-2da2839a637d | -8.24537 | -46.28859 | 2024-10-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32cbfd18-4c3d-3183-abcf-4f7f5926863d | -8.19586 | -46.82409 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21cdf26d-ce3f-3de3-938a-736a854b9361 | -8.18597 | -46.82253 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7d7f46e-b2f9-3af4-8abb-6d127f21c377 | -8.18267 | -46.82201 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fa11a6e-7988-3cec-9441-50162e6f1d7d | -9.91722 | -45.90434 | 2024-10-03 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb82710-a498-3ac3-892a-68ec25cc9e49 | -11.79884 | -47.58479 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a524b149-3a5d-35cd-9e8f-d679a6a38569 | -9.91444 | -45.90022 | 2024-10-03 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f990a1f7-f8b8-364e-985f-c9bcdbc1a886 | -9.87663 | -47.21535 | 2024-10-03 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73010143-182e-3806-ab71-4bf7342a4a84 | -9.87279 | -47.21831 | 2024-10-03 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df72c964-2b6d-3054-97a0-25247131cf03 | -9.84599 | -46.07877 | 2024-10-03 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3ecc9f2-52b6-3f13-8d33-538c865eb062 | -10.72791 | -46.18098 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd25b8a9-b715-3f61-8577-ebbf13ac40dd | -10.72737 | -46.18454 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3634c460-d4ef-3f82-9c05-9bc922586b73 | -10.72343 | -46.16569 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2fcd166d-8cbf-3fb0-94c0-3ba11dc24102 | -10.7201 | -46.16517 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd484c1-7d47-376c-8ad0-4d8967e48229 | -10.71955 | -46.16877 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73f0e26c-3881-38b5-ae58-f59e9684ddc3 | -10.719 | -46.17235 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 157522bf-80da-34df-b202-949b4b9c77f2 | -10.71677 | -46.16464 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55890ac8-29b8-32ad-be09-3b50765f04fb | -10.3394 | -46.14202 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7778c2fe-ccbe-373d-a03a-8dc5e2f47d41 | -10.33627 | -46.1419 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 333af759-8c45-309b-bab6-90736c623509 | -10.32906 | -46.14441 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fed4acda-60f3-331c-9476-43f7f3fe315d | -10.1106 | -46.56736 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 987b7e45-bbf0-318c-bc7e-dd241b1d13fb | -10.11005 | -46.57085 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de84ce3f-f897-3fc4-b6f8-2c7b97ea15a5 | -10.10729 | -46.56684 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 59b8eb83-8dfa-308b-bbc7-304a171c902f | -10.10398 | -46.56632 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fb1f0928-c968-388a-86fb-51cf9540ad92 | -10.10067 | -46.5658 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1d4d7815-61ee-362b-8ad4-635d4703f655 | -11.82139 | -47.59203 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae11c8ab-e8f1-34b6-8035-c236f16badb7 | -11.81809 | -47.5915 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af3540fa-938d-3bc8-92cd-bad7f55f6088 | -11.81754 | -47.595 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b076793f-4e79-31ed-ad7b-ac5b188f1fb1 | -11.81534 | -47.58746 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53f83ba7-b1e7-3c93-a71d-2d21b72136f1 | -11.80433 | -47.57137 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1b52046-72e5-34c8-9cd3-e48d35a78bea | -11.8038 | -47.57481 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4e32f86-092c-3345-9fd0-f12bdfa720d6 | -11.80157 | -47.56733 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf26897b-5be3-3f32-bd53-bc01179f1840 | -11.80105 | -47.57078 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 710e4061-7329-34fe-84fc-c0314abe89a3 | -11.79939 | -47.58129 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 044f7578-1b33-30d5-8b03-d7d147e59624 | -11.79775 | -47.57024 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60b05371-6f81-3292-b6b2-1e41569950b4 | -11.70982 | -47.71696 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f63812c0-1f1a-3ec1-8d00-8307fc83f4bd | -11.70652 | -47.71643 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3452990-94be-3a8b-b12f-35ed25b1e49e | -11.70377 | -47.71237 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 455ca85f-630d-3f88-abda-a6dceec0c7ae | -11.70214 | -47.70125 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 923e9380-d76e-3be9-99ed-2071b5c90aa7 | -11.70158 | -47.70477 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2992dcc-4ba8-39da-97d4-e27c35e9bae3 | -11.70103 | -47.70829 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fb035de-3630-3a00-8af0-4cd4a4652dac | -11.69884 | -47.7007 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba2f1e6f-b315-3258-a398-a11749180ed8 | -11.69773 | -47.70774 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c60d3d0-9c86-3c0d-8f0b-d263d2ecb22e | -11.69606 | -47.71832 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b6ffca1-e11a-3e46-9831-5e93909775f2 | -11.69554 | -47.70016 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 552feded-e3b7-344c-82ba-937d9a7addb2 | -11.69224 | -47.69962 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34e0b254-32e3-35a1-9fb0-286010e6eab6 | -11.69169 | -47.70313 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ac086b-f62d-3546-8922-b3c6c2b2ba02 | -11.69002 | -47.71371 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 53af1d51-2d01-35e6-9a2d-6b3e3e53258f | -11.68894 | -47.69909 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56af12e6-9f76-39f5-a881-61a4d587f9b6 | -11.68839 | -47.70259 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4774ddb4-efa3-36b2-a428-945f83816cbb | -11.68727 | -47.70965 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf853642-cc2a-3c03-ab0b-d63c439c4944 | -11.68672 | -47.71318 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7d8ed925-d611-32c6-b8a0-e57581231ef5 | -11.68509 | -47.70207 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eb8e0cf-f599-3057-b6b5-7266381b2d79 | -11.68397 | -47.70912 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b72cb18c-bf09-3075-9eb5-660d8f15f7b4 | -11.68341 | -47.71265 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c90f0646-c1cf-3e23-95a7-f1ba61a6059a | -11.68178 | -47.70155 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0971b40e-bd18-34d5-8fdc-23b4b38dd22b | -11.68123 | -47.70506 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eca4f211-9774-347f-8668-0cde4c059281 | -11.68067 | -47.7086 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5bc158c1-c1e1-376b-9d92-7d43c1ac5827 | -11.68011 | -47.71213 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dc81f756-e243-34f4-ac3e-0eee98a7040a | -11.67848 | -47.70102 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9995227-9174-313b-92ab-49e7bae330c2 | -11.67792 | -47.70454 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 300a5e07-4830-3607-a8dc-2caee5c85099 | -11.67737 | -47.70807 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e9658a26-fc87-3b04-b607-f499d8a2f761 | -11.32787 | -46.83345 | 2024-10-03 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7c44dc5-f62a-3fba-a9c2-d61ed5b6fd80 | -11.31141 | -46.82754 | 2024-10-03 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9acef471-2cc5-31a3-8ff0-692c29dd658e | -11.27077 | -46.91455 | 2024-10-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 269c5343-28d0-39ee-8f0d-73dff3dff0ac | -11.25537 | -46.92648 | 2024-10-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00604ae0-b800-3005-b0f0-5d670105efb1 | -11.25483 | -46.92997 | 2024-10-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4a65e63-e421-352a-a4dd-35b18fdf4c7d | -11.0378 | -46.53114 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3890b760-016b-3809-ba51-e057dca48e4f | -11.02171 | -46.50331 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 055b137d-aa25-3818-be4f-10e521f146d4 | -11.01893 | -46.49932 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4336b58c-2cb3-3c06-b29e-4a79dff06c14 | -11.01839 | -46.50278 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca3e5da6-7922-30fb-9f06-767a0341d4ac | -11.01561 | -46.49875 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a8ebdac-370b-35be-a10c-eb6f4a6b5418 | -11.01507 | -46.50224 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13ab1d4e-5773-3307-940c-451f5d7ca5ec | -11.0106 | -46.48717 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1d818b-b8b2-3dda-8684-259fa8fdfd61 | -10.98703 | -46.57373 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e258733-1cae-3cb1-9fd7-14bd9cab9ae4 | -10.98649 | -46.57726 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a30b8d2-f526-3084-87bf-48fbbfa2a9f5 | -10.97041 | -46.5494 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b2fa5b7-0827-3f7e-85c1-9703b1075c95 | -10.96709 | -46.54888 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2f1c70c-04de-3be6-b3ee-1cd7b0504001 | -10.94399 | -46.58857 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |


[Clique aqui para ver as próximas entradas](README90.md)
