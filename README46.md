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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c68d98e7-24a6-36fb-b458-d9eba0e2ef33 | -2.52511 | -49.67551 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f74cd4dc-02fc-3298-9531-9966d6b95856 | -2.51592 | -49.75551 | 2024-10-16 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a5f1539-c3d9-31c5-8375-4feb8f214def | -2.48481 | -49.38155 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55e1ac68-3039-3cd1-86aa-3c56349d3c0a | -2.48132 | -49.381 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f866c7e3-8da9-3052-a667-2706dbd2f502 | -2.47541 | -49.59951 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd8a84a2-dd59-3cca-9aae-1b734debe353 | -2.44663 | -50.3748 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad3fa8e1-e0a0-3a85-8afc-d1d8396c2855 | -2.43848 | -50.23866 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c210b897-c598-3955-88cf-ce775a9b8c8b | -2.43552 | -50.23389 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ce4b3cf-8c81-3678-b638-5b4d711f99c4 | -2.43485 | -50.23809 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2a5aa91-858c-3623-9487-5dcdd54b04c9 | -2.43189 | -50.23331 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bfd24c0-aa7e-3ba0-8fdf-19ce216e187e | -2.42912 | -50.18129 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612855b0-1659-347b-aab4-37804617499f | -2.4255 | -50.1807 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 659e0d2a-75bd-3362-b8c8-e5cad2cbf8e0 | -2.40156 | -50.39841 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9b132ca-cd29-36a9-80b4-b6846eabbf1b | -2.40143 | -50.30644 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34336f3c-6790-3ca3-86cb-639c5a0e7258 | -2.39799 | -50.3028 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a368fe0-c051-370c-903a-c0d0a1e5854f | -2.39778 | -50.30586 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c7917c8-70ee-3b36-a697-2e281a4a0786 | -2.39733 | -50.30705 | 2024-10-16 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef0c0914-5eee-32b6-8adb-b2550a51fa03 | -2.33316 | -49.56186 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c5127ca-059a-3cae-90af-5275997d80d5 | -2.28123 | -49.59066 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a8a9bf6-ea7a-33c7-9f15-d513ac6095df | -2.2777 | -49.5901 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1602814-8748-3f92-95ee-c02e9c53a559 | -2.27418 | -49.58954 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19b525b2-c2cd-3a90-bf04-ad186b93e333 | -2.19469 | -49.79375 | 2024-10-16 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16588e14-c5cf-35ee-9b7a-cc92d3da1935 | -2.73004 | -49.1617 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de3d1331-630b-3aab-8970-039ca529d4a4 | -2.61785 | -49.11761 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5faa21b1-0fc7-3d15-9771-daef1159882f | -2.61636 | -49.08278 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 476a7c19-b18e-36a3-bfaa-fe8cda19ba39 | -2.61576 | -49.08651 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d590478-26ba-3ed9-8b75-8df61d0e6f79 | -2.61561 | -49.10955 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 712f32fe-3b84-3cc7-a74c-d4c98bc5afb9 | -2.61516 | -49.09025 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e949634-dafd-3a5d-9e50-dd218c5ea76e | -2.61501 | -49.1133 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e6d53dc-0724-3138-8681-ee7bcab712b3 | -2.61456 | -49.094 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5e2f4c2-9162-3a40-a9ef-6b8e94e93fab | -2.61441 | -49.11706 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bca48c9-2dd9-32aa-9c5d-26cf55f895c6 | -2.61232 | -49.08598 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7387a3a8-a005-3ea8-b865-9dfa0ec16c5c | -2.61217 | -49.10902 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 178c228b-f9ae-3975-b1c7-2a6d733450ca | -2.61172 | -49.08972 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb896669-2a22-3a23-bd86-1719e1ffe074 | -2.61157 | -49.11276 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d9a35ec-9019-38a4-80ae-bc321873cce6 | -2.61112 | -49.09346 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf325107-244e-39f7-a00f-8416426de94d | -2.60828 | -49.08918 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b166dd95-134f-331c-b84f-541f29bd6617 | -2.60768 | -49.09292 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 536b49b8-cebd-3e5e-8e65-4ffa2136956c | -2.60408 | -49.11545 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 451d4633-be4a-3c1d-adde-3e3904ae4971 | -2.60063 | -49.11491 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad222fb1-95b6-3785-923e-2d765609bab0 | -2.5806 | -48.95506 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e82ed626-78ac-3170-a6ca-5250e04fb835 | -2.57718 | -48.95452 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7499931f-8b29-3e31-815f-e0d67674af6e | -2.49807 | -49.07592 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b94acb8d-a8e3-3b86-880e-b5797934820b | -2.49463 | -49.07538 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf023b5c-1801-3d1e-874c-de3d4fd54687 | -2.43877 | -48.89904 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e47217ca-754d-321d-ad45-837a14e894a0 | -2.41396 | -48.94462 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0852a7b-541e-33c7-8339-6f4e5d879292 | -2.40993 | -48.94779 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eee87390-81ea-3cdf-b2eb-e48c561bc0aa | -2.39906 | -48.9499 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 254efaab-e5d6-38be-9be7-43562773265e | -2.39563 | -48.94936 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68f545c0-684f-39e4-881c-a35b0e45bfe1 | -2.39389 | -49.20328 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e22ed0f-c16f-30f9-8daa-c05bd9f3641c | -2.38851 | -49.14806 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57554992-2661-33b4-b93f-c84755f93bb8 | -3.45793 | -50.60778 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1546722-b24a-3947-b81a-e203ea8d479b | -3.44523 | -49.74134 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b9bf26-262f-3eaf-93d0-8efec554a82f | -3.44234 | -49.73686 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3baae9cd-ba2f-3f7f-92f3-609886d778d2 | -3.44172 | -49.74078 | 2024-10-16 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 975baf92-1b19-3fe6-8865-836c93b5b333 | -3.3412 | -49.15499 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d597de7-85f8-36c6-8ec1-8e50a42a926d | -3.33957 | -49.14332 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7aa7596-9daa-39a9-bd1f-07a9fe2b0ccd | -3.30273 | -49.08937 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f04730e1-7858-38a5-b44e-c7bd86beacb7 | -3.23408 | -50.1804 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c2e636d-0cb4-38e6-a40f-752d96e7465f | -3.23343 | -50.18451 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 806c17c5-fd55-3705-b647-2fe5423e86ad | -3.19061 | -50.3134 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359c46e5-2e91-3ef8-98fa-d14d6eb82f8c | -3.18217 | -50.4586 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6b480d7-1c3b-33b1-acf2-a37ab111290b | -3.17422 | -50.46164 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dc5e6d9-1915-367a-9d6f-89860a405b8e | -3.17286 | -50.47009 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef668d3b-f638-3688-950c-311b271ebca3 | -3.16625 | -50.46469 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3270d32c-6cd4-3e84-98a1-8f6b6749c9eb | -4.96472 | -50.48034 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17fd2763-1221-32e9-b172-8d2a9b5a6e0f | -3.98083 | -50.70987 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67af6d9-2a63-3262-aa22-faa380974cb7 | -3.97717 | -50.70929 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99cd41ef-3071-32c5-8b3a-3a8cf319c566 | -3.97647 | -50.71357 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6049b03-e740-361d-a1f7-f2f9e0743e55 | -3.97624 | -50.38776 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa405274-b0e9-3886-8c1e-a51a41a19d97 | -3.97282 | -50.71299 | 2024-10-16 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee40328e-c45d-34b1-b90a-3ac5e11243f6 | -3.9401 | -49.40477 | 2024-10-16 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c70739-433d-3d3e-967f-18b4b1c8e974 | -3.93666 | -49.40422 | 2024-10-16 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 349ea01e-ea66-3ca6-9763-6e089273c87d | -3.91986 | -50.2201 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73b431b1-bca4-3501-a8e9-030391e513f7 | -3.91629 | -50.21955 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01a738e6-2919-35cd-b6f6-371dd5f992d1 | -3.91565 | -50.22361 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 390a0149-242f-3f78-912b-345893cd44c3 | -3.91272 | -50.21901 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55a051f1-bc86-325b-8448-9b28fe0cab4e | -3.91208 | -50.22307 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7092ffe4-8cba-3633-9293-9f3f1eaff04f | -3.7108 | -50.16853 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85d49dab-3629-31f4-a9d6-9803178ad0b3 | -3.67672 | -50.03913 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af20e354-71b5-339c-9ad9-098d036c16cc | -3.63757 | -49.83081 | 2024-10-16 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42b758be-69a9-3f21-98aa-7da6fc455e24 | -3.57735 | -50.56399 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f099b2a8-a1c4-3314-8178-70a8a5acf0d4 | -3.57666 | -50.56823 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4ea1f8-826a-3a74-8fe9-290bf53f9359 | -3.57598 | -50.57246 | 2024-10-16 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18fad8ed-1eee-3a39-a9e5-579fc5b3f4ab | -4.99396 | -50.88536 | 2024-10-16 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1117f5ed-bc7c-316d-83ef-5be7ccfa5745 | -5.83249 | -50.15279 | 2024-10-16 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81f4e8a2-9399-3ca0-9852-5c3432212728 | -5.78814 | -50.16146 | 2024-10-16 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3e2694b-5a6c-3558-94e0-ea438bfc5cec | -5.78751 | -50.16532 | 2024-10-16 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73077201-7bf8-36b0-b5d8-edfdf6c1fd36 | -5.78667 | -50.16274 | 2024-10-16 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d37015f0-fbd4-3349-b034-aacd0bdaab77 | -5.35099 | -50.62183 | 2024-10-16 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a3dcc01-84ca-33af-bb1b-9fe5c6fe7862 | -5.25113 | -49.86686 | 2024-10-16 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5a5059e-e3e2-3e8b-8add-f8fe744faab6 | -5.23157 | -49.85593 | 2024-10-16 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdb711ab-962e-3040-bc32-06da90436359 | -5.23123 | -50.87978 | 2024-10-16 04:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0877191f-702a-3954-82b4-33787c040af9 | -5.2305 | -50.88124 | 2024-10-16 04:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2693dac-f8ea-319b-9693-a4c7d94b4f85 | -5.18476 | -50.05756 | 2024-10-16 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5c02bb1-dceb-377c-b4bc-0f73ee80bcef | -2.27371 | -50.42356 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3350dd-786e-394e-99fd-509dec492002 | -2.24371 | -50.45171 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86ea7478-ff6c-3187-85b0-f56dad4220bb | -2.24002 | -50.45112 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c68440da-baac-3bc5-a4ab-82d6818bf48e | -2.16666 | -50.89246 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed862654-3893-3f09-8537-c84d2e26a8af | -2.15459 | -50.89525 | 2024-10-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README47.md)
