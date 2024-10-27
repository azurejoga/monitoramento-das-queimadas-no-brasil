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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00b2b7fa-4982-39c0-b05c-48d76df160f0 | -2.54363 | -51.17292 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0230067a-38f9-3b87-acc4-a65f2d0c145a | -2.54282 | -51.18663 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0fb18122-8ac5-36ae-a8d2-0824c90e7676 | -2.54269 | -51.17837 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8aa9d387-4d10-3553-8a2d-54888482cb63 | -2.54192 | -51.1921 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 410dca9f-1420-33a3-ad74-5ed0a690751d | -2.54176 | -51.1838 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| adcc2321-4074-3910-8eef-28217ad8645b | -2.54101 | -51.1976 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8259e0-dcfc-34ad-8877-835ec5158b7f | -2.54082 | -51.18924 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c454a9b9-f36b-3b5b-b10f-b860130089dd | -2.53991 | -51.16366 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a698c99-0b87-32a9-8a03-0d48225df136 | -2.53987 | -51.19473 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 373d0fe8-20d3-3262-b64b-f2581d33974e | -2.539 | -51.16916 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fdfbc5f-bf9e-3af1-8d01-d55d75835af7 | -2.53898 | -51.16095 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c92d4af3-4d3d-3229-9b69-62e0838190af | -2.53893 | -51.20023 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b24358-eaf1-332c-93a6-8e99321e1137 | -2.53809 | -51.17462 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9cc07284-c8b8-39a1-b02c-c2d3b6f33afc | -2.53804 | -51.16637 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 563a8c97-84ff-32b9-a5cc-c2ebaf7ede3f | -2.53719 | -51.18007 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9957add2-e1f4-3ff1-a098-6a5d62893806 | -2.5371 | -51.17184 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 61e24e5d-0962-32ac-8112-302eccdc1bf5 | -2.5363 | -51.18546 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2dfe2121-bebd-3aa9-8bcc-ee444b5d37cf | -2.53616 | -51.17729 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 21c5f380-4bd8-309b-9f48-8c2c1508bfe1 | -2.53539 | -51.19095 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e8b82a17-90be-3c09-8600-36580279963a | -2.53523 | -51.18271 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b563d6d5-ac21-3858-b796-6097711f2d39 | -2.53448 | -51.19648 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aa5d84c-07aa-319d-bdb5-5d5bc02c9f87 | -2.53429 | -51.18813 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6e53d446-94f7-392f-9723-8c38428d53b4 | -2.53356 | -51.20206 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bcf0c73-e910-3b3e-86db-61765fff40ff | -2.53337 | -51.16267 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f836b49d-5a0b-3939-b83d-b7a4e5c5d054 | -2.53335 | -51.19362 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca946c13-4ce6-3051-a470-71e1ea16baca | -2.53247 | -51.16808 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad0ee71a-3591-3f59-81ca-1994a8612c35 | -2.53239 | -51.19917 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 633af355-3292-3ac5-9354-87b8186d48fc | -2.53157 | -51.17352 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bcea8d16-56f8-3427-949d-a846a24db77a | -2.53151 | -51.16536 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdffb68a-dcb4-3a1d-a97d-0c78223a98f4 | -2.53067 | -51.17895 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d8e48c7f-09e9-358e-b013-64605ed2be88 | -2.53058 | -51.17077 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7b3aa943-b42b-3cbb-8bd0-f996f8f8f3b0 | -2.52977 | -51.18439 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 99418fc7-98c1-3d29-ae9d-184ebd9cd61b | -2.52964 | -51.17618 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9dffe6a4-b697-3ac7-b367-b52b9ee15bdf | -2.52886 | -51.18985 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 08eb46f0-4a3a-36b5-9875-d0f5835d0d79 | -2.5287 | -51.18162 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9f06fabf-9eda-31a9-b777-639a00b2b46b | -2.52795 | -51.19536 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a52a451f-8f63-38e5-afc0-1052fd8f5bda | -2.52776 | -51.18707 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 96eff4ab-4096-3df7-aa82-3f8896519d5c | -2.52682 | -51.19253 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d7ab7f4-aad2-3e45-985b-6d434881e87d | -2.52593 | -51.16711 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19c897f7-65c1-34ac-9a6c-378b878a6f94 | -2.52504 | -51.17248 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06c5df8c-472d-3af2-b12c-7b3cdc1af2d1 | -2.52414 | -51.17786 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dbb174c-ea77-3b5a-b9b1-fe48e0667e2a | -2.52403 | -51.1698 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc5ccae1-004f-3c80-917f-77fe05565b0b | -2.52324 | -51.18328 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c380185-5118-3eaa-86c1-b18e903dfa65 | -2.52311 | -51.17515 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7aa4ba37-6070-351e-b3f4-f723921b46ad | -2.52217 | -51.18054 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac1d7b39-545d-3401-906b-4c6878a27a17 | -2.51849 | -51.1715 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 735e6fac-d5d4-330f-8c81-c2450fdcb6ad | -2.5176 | -51.17684 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac6ff09a-ba7f-31fd-bf10-5521d7c78eb6 | -2.51656 | -51.17419 | 2024-10-27 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef36b0a3-c85e-3ffa-bbc1-fd2fb74ac141 | -16.09254 | -39.07512 | 2024-10-27 04:02:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aa7379de-5d34-3a53-a3e8-c312978037e3 | -17.5305 | -39.46816 | 2024-10-27 04:02:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d75a1138-1211-3b2a-8adb-d3d74144abc8 | -17.52533 | -39.46466 | 2024-10-27 04:02:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 533770eb-8819-322d-a85e-228d67411128 | -12.18425 | -39.94398 | 2024-10-27 04:02:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 91c9a97c-ca26-3518-871a-951601324896 | -14.9136 | -40.68092 | 2024-10-27 04:02:00 | NPP-375D | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d43e90af-493d-3148-a4d9-230e004bb793 | -16.28852 | -40.1086 | 2024-10-27 04:02:00 | NPP-375D | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a2108f74-d34f-312e-8e3f-5f4608c397cd | -12.23474 | -40.97533 | 2024-10-27 04:02:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d8ba0ef1-55c8-348c-a06f-a49f0fc5df96 | -12.23418 | -40.97886 | 2024-10-27 04:02:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2cef1b40-39ca-38a6-9e17-e3ff69e13bd6 | -12.12042 | -40.36146 | 2024-10-27 04:02:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0690dd5-92c9-3036-b134-994f80bd965d | -12.10491 | -40.39555 | 2024-10-27 04:02:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b1c3ef9-060b-3317-a806-5492598b8372 | -11.59882 | -40.65682 | 2024-10-27 04:02:00 | NPP-375D | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b10b408-63fd-3463-a78b-9ced61e7f98d | -11.53891 | -40.41142 | 2024-10-27 04:02:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea4a590c-5760-37e2-b6cb-605ce766a97f | -15.00525 | -41.55587 | 2024-10-27 04:02:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 54f161ea-168e-3d33-902c-244d2669e5ad | -15.0047 | -41.55944 | 2024-10-27 04:02:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8e30d4c-2f7d-320c-acea-c57281cce153 | -14.13533 | -41.69093 | 2024-10-27 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 859e5cb5-d4f6-3211-b891-7946bb442c7e | -14.1204 | -41.67754 | 2024-10-27 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df2d1917-0d0e-3500-a068-3f83c1b66f97 | -15.00414 | -41.56301 | 2024-10-27 04:02:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8a1c295f-d153-3f53-82c4-b7e0fa55ee0d | -16.37181 | -42.26309 | 2024-10-27 04:02:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd3aa5cc-a9fd-31f9-96f9-bd59d1d0dbab | -10.19457 | -42.45346 | 2024-10-27 04:02:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78d7be70-82ad-333a-8b46-8800c66d0144 | -10.16385 | -42.44836 | 2024-10-27 04:02:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 178d48f3-9cd5-3045-8369-d7e5e6296a04 | -10.16043 | -42.4478 | 2024-10-27 04:02:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbf3bf38-561e-36ab-b38b-83b62c33fe62 | -12.21669 | -42.78408 | 2024-10-27 04:02:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dec773e3-a4bc-3466-a3a7-e19da5caa558 | -12.21329 | -42.7835 | 2024-10-27 04:02:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1065c32f-a3a2-34c0-88f7-470155ee1e95 | -13.71568 | -42.91473 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 07230eb6-1f51-3cdd-97a4-cd4a462d7dde | -13.7123 | -42.91414 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7ba3f6f-d953-3b2b-b9c0-5e1c34cf8c2c | -13.55893 | -42.99885 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7bcf687b-2b29-3ac7-8a1a-c1c468c5aff4 | -13.48126 | -42.46317 | 2024-10-27 04:02:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aceb5275-652d-3a7c-aa20-11cff5b065c9 | -13.45566 | -43.0307 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4d6e8983-ad0b-3706-9f30-703c2c4a1646 | -13.45226 | -43.03012 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0870edc4-1ad0-30a8-93ef-73d3a228c66e | -13.07019 | -42.1328 | 2024-10-27 04:02:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 27f4b341-9df4-3d86-8d7d-135f4f02527e | -12.9233 | -42.28573 | 2024-10-27 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 405eaf32-e7c3-3ce7-90a1-d32cd130c538 | -12.70472 | -42.29801 | 2024-10-27 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 099c5987-5dcb-3e15-a6f4-fff644eae83d | -14.27963 | -43.24926 | 2024-10-27 04:02:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc1e7d94-b245-3b5b-92c8-8b24a15d9add | -14.27901 | -43.25301 | 2024-10-27 04:02:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 15484eed-c9cd-32a2-8a05-ba297b1f285f | -14.27624 | -43.24867 | 2024-10-27 04:02:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 431774a5-c073-3f49-b62d-e98b10bf14e3 | -14.27562 | -43.25241 | 2024-10-27 04:02:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1c79f01-2914-3e46-a593-a2b5f04d3a37 | -14.27557 | -43.03913 | 2024-10-27 04:02:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5806d74-73b6-39a2-96ee-e23bb57d55cf | -14.24131 | -43.07891 | 2024-10-27 04:02:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 04939a49-1ae5-3ec9-a4a7-5db91bdf9501 | -13.8276 | -43.23483 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f8eff9e-ae98-3513-b248-b9b83f599df2 | -13.76616 | -43.16341 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56455669-69a7-3dff-a10e-3bee3f8e73c0 | -13.7497 | -43.07249 | 2024-10-27 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c36358b9-b899-3361-a9d3-5d5bb57930b1 | -15.25449 | -42.52245 | 2024-10-27 04:02:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f740e9d5-f95b-342e-a9c1-bb8baf87b646 | -15.56379 | -43.1546 | 2024-10-27 04:02:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 811f4ed0-2428-3f74-8a84-6f97d0f74cb5 | -15.56102 | -43.15034 | 2024-10-27 04:02:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 55263c12-6db4-3674-ba68-64a427b80b31 | -15.56042 | -43.15401 | 2024-10-27 04:02:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| abe0060a-bb09-3390-9789-3ba1d80a650e | -15.55983 | -43.15768 | 2024-10-27 04:02:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e267be07-e0d6-3886-b31f-d9db530e253f | -15.20109 | -43.53611 | 2024-10-27 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0cba1ee-a564-3cf9-b11e-c397219cb5fb | -15.19769 | -43.53551 | 2024-10-27 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaeadf15-b368-37cd-a7be-7fa47334ff62 | -16.68236 | -43.88243 | 2024-10-27 04:02:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0765be1f-c90e-3661-9f89-e067309e855e | -9.96785 | -44.16281 | 2024-10-27 04:02:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f13054-4980-3bed-9540-e5d856c4dc87 | -9.96712 | -44.1672 | 2024-10-27 04:02:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a579f465-9676-3201-818e-a82fdeeb89e1 | -9.96417 | -44.16216 | 2024-10-27 04:02:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
