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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fb06ddc-9352-326f-9bbf-440a23a1675e | -3.89208 | -52.11871 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f7e5e7c-c404-353c-90c6-425c8dc3f087 | -3.45084 | -58.39655 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5774852-a307-3cf1-9397-9e7bd92e5831 | -5.73322 | -53.45763 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c86574a9-a247-3bb7-9b32-e9b38b45645b | -1.33115 | -54.66077 | 2026-09-21 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab454153-a0e3-3c76-8656-db7a4561f20c | -5.01057 | -56.08689 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7bea71f-260e-3cd0-aef0-7b385e325b77 | -3.79729 | -59.70742 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e542f8e-a476-3188-8c00-4aa96aa88de6 | -3.3901 | -61.29558 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f60395f-fb12-3fa1-ae9f-d036199a05a9 | -2.25902 | -52.02482 | 2026-09-21 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15577a6-7b99-3047-b05a-4b9af6775e70 | -6.39517 | -52.29502 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3d5456d-034d-3bba-8a02-c059acb69bbd | -6.14151 | -55.70391 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36200228-dd06-3363-a35f-01f15c8d12c2 | -5.91686 | -57.67494 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 073f703f-7670-30d3-9805-a6fbe72b5e95 | -6.49908 | -58.37884 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8d4844e-73c1-3709-ad0c-00a2a27eed93 | -6.36028 | -58.28638 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18fa292d-9b84-3f4f-bf16-866c6c62e093 | -6.25824 | -55.436 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b30071b-307d-38f6-ae46-8d38d8e73d15 | -5.85005 | -53.54576 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82c91552-07c8-3d65-bc89-2af8a0c54747 | -6.94087 | -55.02256 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd65afd-2360-39ec-aa65-9808bcff69d8 | -5.87224 | -52.03654 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afe8fc54-c88a-39a0-bdb6-a2093e41decb | -2.46423 | -49.22013 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0b03cf0-e7da-3d8b-9f45-54979bb8af87 | -6.19164 | -55.45045 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e77088cc-f24e-3fec-bd63-15f4ff0389bf | -6.10422 | -57.62534 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9ad9e8b8-2b8e-3922-b180-4f4741d86983 | -4.06992 | -52.12703 | 2026-09-21 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c804f6b5-0de4-3d6d-ac26-a43dd296c2a6 | -2.97072 | -54.76939 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d790962-6e5a-3356-96bc-6a6e98e6c93f | -7.89005 | -44.84283 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86c92f5c-6952-31a5-8d5e-902ece9d9f5a | -3.26946 | -60.8876 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f211c89d-5bdf-3ff7-9fc6-af1adbc88533 | -6.17497 | -57.77608 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cb89cd5-7211-38c6-a89d-4eaedf25a9f3 | -5.8719 | -50.1607 | 2026-09-21 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0bfd7c2-3a18-3ac9-88e6-c6fefdca4288 | -6.15831 | -57.70136 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54fa0ac6-f6ba-325a-af6e-15e730fc1769 | -3.54725 | -56.8905 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c6ff766-d7f3-3b2c-b2d9-3809c6bbf0cc | -3.05445 | -61.27794 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07180ba4-09a0-3bcf-b9c9-ab8dbb42dc7d | -7.4469 | -44.74066 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef8e9dba-1706-380f-80e2-4d8394a60039 | -5.04766 | -56.9748 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95b365ff-99fb-339f-9cf0-1f286072ad7c | -4.35101 | -55.64788 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1239d0e2-76f7-3434-ac9a-599059ba2c08 | -7.34076 | -44.46556 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f3a1e22-55eb-303f-9f5d-25db11a89df7 | -2.98117 | -54.76749 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c64a6db7-965d-30a1-b121-f6c74b0990cc | -5.9771 | -57.7826 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9a45572-804f-3b76-8036-d3493e2089e9 | -8.38324 | -45.63062 | 2026-09-21 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59c6c765-a155-3286-977c-b45d5384746a | -6.14063 | -57.72494 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc2b5d0-cf30-3982-8d7c-47d0b5d2ea99 | -2.8302 | -50.46235 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a75eafc9-35eb-3d20-aa63-441093989cc8 | -4.34663 | -55.65425 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17b05395-bd6a-31cd-863b-37ed4b07ad24 | -5.37917 | -55.90501 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94ea835c-affb-3314-88ca-ce2654e46a1f | -5.89553 | -53.64252 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33d7bdba-5744-3be0-bfde-04df01e0b1df | -6.31175 | -60.00972 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5110a851-83ce-38c6-98fa-b9b74fa511de | -3.42655 | -59.26445 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7cedb7f-1881-398b-a737-c66d1b7ccf43 | -3.49981 | -59.19217 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b13abd1-e581-3a73-9f76-605f762a44dd | -5.75655 | -57.58186 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba8c055-ee02-3d35-878e-bca3bea416c4 | -3.48101 | -54.65841 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86792927-67ec-3593-85f0-a3325ec77c85 | -5.3731 | -55.90054 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db0b6209-111f-33f3-b71d-535cbd43ed43 | -2.94475 | -51.04214 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90e2c1a9-1c3f-32ac-b02a-452ec0d36ce5 | -3.49512 | -59.60759 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8747c92-6c4a-36a6-8579-dd203e28803e | -3.43314 | -50.66838 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25aa1ba4-caa6-3b1b-9a1b-29d6ed2acffa | -3.61882 | -56.84235 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16f37d91-3ec2-3dd0-b911-9fcb7e04e79c | -2.50775 | -56.60014 | 2026-09-21 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 61744737-a2a6-3b8b-a603-644546cccf56 | -5.88519 | -53.64084 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae065227-e010-3b79-a2c7-16c2705da0fa | -6.91363 | -43.74187 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7dab4f0-2ce7-318d-be66-d109b0012edc | -5.84136 | -53.50912 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cec22bf-1e0f-306b-8f24-e6f7c8401e3d | -6.24698 | -53.31032 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| deef0237-63f7-3a37-9b73-56054f519e82 | -3.60244 | -59.01469 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 664135fe-290f-3c54-9d0f-9e69080d550d | -3.44555 | -50.61391 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f54cb3c7-2698-3751-9026-8ec7ff4d6ce7 | -2.60465 | -59.76237 | 2026-09-21 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7cae5cee-e93f-3e1c-8df6-5226e58d371c | -5.82053 | -53.51419 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0566124b-06ee-30a3-a3ac-7361f4e52c2c | -6.73871 | -55.09995 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be774b8b-5081-34c0-a03c-b89eced2be71 | -2.58273 | -55.98929 | 2026-09-21 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d4cbbf4-bf82-3fd1-a22a-b6f81376d9b7 | -2.89161 | -57.64803 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b98000f-bc60-3b4b-a917-6c236ef7b158 | -3.36766 | -50.44257 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b52391-db26-307a-aad3-0bc3a5415b29 | -5.20913 | -56.07603 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 057c528a-f312-3428-801e-b5c1a3a643f5 | -5.76249 | -56.5186 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bb98bfc-6e8e-31b6-8070-2a3d2bd74f38 | -5.8512 | -53.53811 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe1f387e-0165-3d6c-aece-f85634c64c7c | -6.8722 | -55.29251 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc1cdb4f-4f01-393b-8df4-26afce76f882 | -5.76341 | -47.28452 | 2026-09-21 05:04:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44c6d78a-823c-38c4-bd9c-ce4b3f95f0a5 | -3.73435 | -59.37798 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ae2708d-391d-3192-8aeb-39f44c855b68 | -7.9688 | -47.45789 | 2026-09-21 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa41a514-5296-36ac-87b0-db51df61d655 | -6.31545 | -59.96297 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f28f8091-5131-3adb-864b-fa3bb253f915 | -2.58676 | -48.43933 | 2026-09-21 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef9566ad-e364-3f5e-9da3-37aeac7d2c39 | -5.97959 | -55.36747 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d957ab1-7b9d-34fc-a980-cf7f98d630c7 | -6.72648 | -55.09087 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3610d4e1-17f2-3e1b-8cfd-14dec6f38362 | -3.17294 | -51.35422 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5202f98f-d5a2-3a09-bae3-28e7f9f0f588 | -5.76629 | -57.45634 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55a5eb43-f314-324c-91ea-07e9ed54766e | -3.00381 | -54.16341 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0a198d8-6ccc-3b92-a755-af89c007e59b | -5.86213 | -53.48902 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ff92851-a49c-387c-bd5a-f8270abba392 | -4.34108 | -46.37 | 2026-09-21 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e75689-adda-3aee-9751-f99d53c67d6e | -6.55 | -45.57467 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00a791ff-25c0-3bc9-9cd1-89837114c258 | -3.43916 | -58.01871 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 387e62bf-0a14-3167-b9f2-a32296994f9c | -3.59093 | -59.06258 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 718809af-7259-3d1a-b68a-d387938ee02d | -6.30797 | -60.00909 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48c1127b-3238-359f-b156-5db58a9f977a | -2.91672 | -57.79145 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8da83f6-5b7e-31ed-9fd6-38ffe792935d | -6.06969 | -55.62215 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7dfab28-29bc-3977-9c7a-4a88df36a762 | -3.4077 | -50.75593 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc428bfb-96ba-3abc-ac22-fca6316c767b | -5.84133 | -53.48551 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c6b676f-917d-3819-90e5-7055de0b4cc5 | -5.8409 | -53.47411 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5dcec63-7d67-37f2-a514-07664477fd2d | -4.38486 | -56.32189 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bce1b6f-7747-3f92-9e67-a3805c46f18f | -5.37587 | -55.9045 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4fac9bd-171a-3630-80f8-0e63dd82f938 | -5.20757 | -56.10764 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9300249f-d867-38d4-91d4-bb239efe513f | -4.43122 | -55.35056 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8b6cd8f-6517-3f8d-b8d1-bf9c61514d30 | -2.85653 | -54.21262 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7b00a9e-31f5-3595-8a49-302366d37990 | -6.72918 | -55.07329 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd57a7dd-27e6-3d09-944c-52a5a9586908 | -3.30605 | -59.45665 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41deff49-44ad-3c25-8fee-053e560ce3d2 | -3.01455 | -54.17938 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b283c6c1-45ca-3c16-a26b-2b2c770d50b6 | -5.89288 | -52.10283 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f18e7a1-04e7-322d-9c41-a14141982923 | -3.4471 | -50.60384 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 142bbe00-1838-3abf-8a25-d7dfac141e83 | -4.59028 | -45.16157 | 2026-09-21 05:04:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README64.md)
