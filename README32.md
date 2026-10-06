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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cfdc684-1a26-3fa2-a80d-628e07241ab1 | -3.15057 | -50.44209 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93f6398a-e708-3b5d-bed8-70fe0c9c51d0 | -7.01631 | -43.44546 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b45086f6-c5c6-33a5-b826-df7454c9fff3 | -6.87761 | -43.67361 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a32a51a0-24a6-3cb0-993a-1b499d6be7e4 | -3.09783 | -53.73653 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6bcee389-53fe-36e1-89e1-7ed333d0fb65 | -3.89552 | -49.71274 | 2026-10-06 04:19:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29e9113a-2333-3360-a747-0a2873261470 | -6.1489 | -47.12369 | 2026-10-06 04:19:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 098e449c-8c4d-329f-b44b-77b39f9335aa | -4.46564 | -54.96281 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba177bb-e9ee-3dd5-851d-3fa63c4f7f7a | -10.49873 | -47.25799 | 2026-10-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6914e59d-0532-33b6-80d5-6c197739bb04 | -3.06116 | -54.216 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a970e97-a67c-3b01-991f-96857b7bed41 | -10.95107 | -45.4154 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a716329a-a338-33d2-a927-e30d61df594f | -3.07253 | -54.25443 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d3690ac-2a03-35e6-9e0b-0556bbce2441 | -11.27801 | -45.51508 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ebf32081-698e-32bb-bd33-52fb5263b83c | -3.23006 | -53.8662 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7c53bbc-6579-31ff-acb3-e65f3523d614 | -7.89892 | -44.18205 | 2026-10-06 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7115fc95-2cf9-3428-9178-fc7252ea7777 | -3.09316 | -53.72289 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 42c37fbb-1f84-35c8-94c9-20482bea2afc | -6.87923 | -43.68555 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11310061-9572-3b01-9a5d-7b7953823d3f | -3.06716 | -54.18257 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02e44a94-39ce-34fd-82d5-5ad8004cf625 | -5.6683 | -42.57872 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b69f6c23-f37b-341f-a8e4-28d688da1708 | -6.00732 | -47.39415 | 2026-10-06 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f3304f58-1d7f-3f76-95d8-100f7593bd81 | -3.33344 | -53.38818 | 2026-10-06 04:19:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e190594f-09d6-3ae7-a35a-af6602dce74b | -5.0857 | -46.04376 | 2026-10-06 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2026093-3c0d-3077-b739-0ded29538ae4 | -6.36625 | -42.54299 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20e69468-e299-37d2-9bf9-44bfddf1ebec | -6.60472 | -37.89402 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd51d973-2c80-32de-9415-69b0128b7d87 | -3.1 | -53.72412 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b056f4a6-530b-3b64-9c36-11502d97d7fb | -3.08154 | -54.15975 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a66c62de-b675-3934-a96e-6e5e891ee451 | -5.43505 | -43.44378 | 2026-10-06 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| beac4b45-3bbe-36f5-b3b4-4e2b481f7360 | -11.26078 | -45.50785 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e02b344d-2b85-3827-a7b0-d5e42a4d2881 | -4.14194 | -54.03122 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9e12df7-a671-3732-b56c-30fce6d8eb97 | -3.10045 | -54.17602 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 72d9a821-76bc-337d-9377-610d0a4ffe18 | -7.76413 | -44.58028 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8eb7f98f-60a8-303e-8c5e-220cadb84aa4 | -4.77287 | -50.80789 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 051d8330-3e0b-3256-8b52-3ca58ebcd2d0 | -4.41389 | -49.66211 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c5418ff-04fe-3d5b-a559-3bf24ffe9d2e | -8.58039 | -45.6564 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51cce73b-2b36-34a4-8446-c270b4a6b585 | -3.09492 | -53.70956 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9648d2f1-7498-3234-99cb-4b351ed727d1 | -6.72124 | -44.28181 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8eda66f1-36ba-314a-8ca3-9d3553fd9091 | -5.83893 | -45.01108 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b78268ea-de79-380d-8429-9cd24fc148fe | -3.07008 | -54.18431 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edb47426-0fb3-31a9-9238-7c66bce5d7cd | -2.98457 | -54.13524 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 02ecd72d-b1cd-3831-8890-fe2ae4fd9b51 | -9.85768 | -44.80478 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dd91745-0541-315d-8eac-46fbe233fd37 | -11.23713 | -45.25602 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44041f3a-3944-3cb7-b30d-b328cb044518 | -6.89372 | -43.68401 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecf1edc8-4f22-3eb6-96b7-575a23c14fff | -6.19351 | -44.85941 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1baa4d9e-89ad-3d16-8664-87278479d519 | -6.81721 | -39.3034 | 2026-10-06 04:19:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 605518cc-06f7-3ff1-b881-7ba6012779e6 | -3.05137 | -54.20864 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3217c9c-54ff-3be9-9460-2d7f06e177d7 | -6.67194 | -43.8264 | 2026-10-06 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebda7593-ac8b-3b83-8b90-00a7ce56f600 | -2.86699 | -54.13537 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7823a61-73d1-3812-8c47-2396995f6ba2 | -7.46568 | -42.99822 | 2026-10-06 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5aa7709b-af4c-34fa-aab9-1e28d09aaf31 | -4.50724 | -43.69632 | 2026-10-06 04:19:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14c057a6-0241-3774-8ecd-aadb9706a58e | -2.79435 | -54.13637 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc04a4fb-034d-3a48-9d45-75157076afd3 | -4.14879 | -54.03248 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a01e2cc-8d41-3069-86ce-7c54aeb2ba90 | -3.10934 | -53.75146 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06f31272-e67b-3999-96de-b804f25627f2 | -3.27886 | -54.18276 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69f36ebb-8d60-3c21-942a-8f613082158a | -11.63734 | -43.64297 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2e957f6-51ae-373e-bd1d-a112921f3e31 | -2.92656 | -54.12541 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33fc184d-82c3-3424-81b0-67cd88e69bf0 | -6.13269 | -43.5096 | 2026-10-06 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 979d7f85-d3f6-361c-a9b7-95fdd5639db8 | -5.58785 | -47.27178 | 2026-10-06 04:19:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fb8fdca-2a50-3672-8e02-b52279de95ea | -2.87826 | -54.13589 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| becfd7ae-6f7c-3c8b-9fd8-b7d1c3c8ce31 | -5.60684 | -44.03204 | 2026-10-06 04:19:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 896d7790-5dcf-30f7-86bd-83c85f718664 | -8.69688 | -45.21043 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a846bab-570d-3d30-9c10-184f23ba7204 | -9.77237 | -44.79462 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d989cd8f-a4ee-321b-8785-e535f621c7c0 | -6.72421 | -44.27678 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32534480-aba6-34e7-95a6-fd01c4005d83 | -3.28127 | -54.18492 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e09007-ea03-390a-b527-9df7c1b30688 | -2.87448 | -54.15718 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 74f139c7-df9f-3026-aa18-de714ca2a02f | -6.60946 | -41.5792 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e1ffd34-5189-3051-a92e-9693c4d4657d | -11.28208 | -45.49056 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cd52b47-5791-3523-bc09-118d49c8e76a | -6.003 | -47.39339 | 2026-10-06 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| da399d47-c798-361d-a686-10fade569787 | -11.26009 | -45.512 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20769c51-57fa-3620-9aa6-73f5a9e2643e | -9.86343 | -44.81389 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82305df0-d248-3cc7-8f68-00f5c4339c1a | 3.32287 | -51.34001 | 2026-10-06 04:19:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 183b47ff-5208-318f-a766-35a267f8b4c3 | -9.76538 | -44.7945 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e519eb62-6425-3c31-8a98-bfccc82a0580 | -11.27359 | -45.4973 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fd9d30c2-cc98-32f0-b14f-9a891a61a19b | -6.92281 | -44.56307 | 2026-10-06 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e11adfc-5922-3e9b-bef7-940384034eb7 | -5.83073 | -45.01438 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ffb06f3e-090a-3d79-b290-4ea21a82c20a | -3.07883 | -54.15786 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e5bd96c-961d-3c60-899c-31731742bd25 | -7.28756 | -47.26643 | 2026-10-06 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6377895d-8b80-3adc-adf5-5c66b9533831 | -6.36903 | -42.54712 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdc174d7-749d-3329-88d9-3c2247baef76 | -3.09285 | -53.72179 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 24d67c09-2800-303a-9b47-02b6dc944843 | -2.9356 | -54.13927 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| daab4453-8bbe-3626-b3b2-cd8391aadf50 | -6.6078 | -41.54696 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4f3842a-0ae2-36f5-867f-22a62e1ba8cd | -4.10928 | -49.40049 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 97da8819-3ba4-3bd9-b0d4-0d9e4f54aab7 | -9.04256 | -45.17347 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 031e4a32-fc24-33eb-80b1-6e6135b6f9c8 | -6.61795 | -37.88203 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5cfff63a-2506-3ebd-8721-35b74a4902fc | -6.85745 | -41.80438 | 2026-10-06 04:19:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 441fce1f-8494-3b08-99d9-86a76db5d83e | -5.1875 | -48.31524 | 2026-10-06 04:19:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abef5660-5685-35e1-a0f6-fb9e36433d4c | -2.96354 | -54.14512 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 38c748ec-557b-36b9-a59b-87f30c629828 | -3.10343 | -54.1823 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| daeb0e59-fbf6-339e-9507-a1bde31bef94 | -5.84122 | -45.02066 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0f26af59-d08a-3594-9194-252500566606 | -7.41203 | -46.79329 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eceeb9e6-dbf7-30a8-94ef-0db7b5674be7 | -6.71998 | -44.28022 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03bb0b52-3cb2-33a3-9d73-921b22441f08 | -9.26064 | -45.65669 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0efabf6a-4bf0-3d79-8773-c34c05153d7b | 3.32379 | -51.34348 | 2026-10-06 04:19:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38615cfe-fd17-3200-b75a-36a26de48acd | -11.23577 | -45.26408 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd0d8fd1-c810-315a-aa11-1a13557f1f09 | -6.72487 | -44.2728 | 2026-10-06 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49b1641e-5e8d-3c19-aefa-a756b3c9e9f4 | -7.37749 | -46.22628 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c42a180a-4f4e-306c-b6f6-1b7d59ed6c8f | -8.69183 | -45.21832 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e45e52-e950-36f1-a6aa-b77be090a868 | -3.07749 | -54.2466 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50f03d19-0580-31ec-a087-9e76e2ed8ee6 | -2.90288 | -54.07857 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 538641ae-0777-3b5d-8283-cbfdefa37eae | -9.92138 | -48.13569 | 2026-10-06 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c75ec559-9618-3bc5-b5cd-77272ef7fe8c | -2.78556 | -51.67253 | 2026-10-06 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bf5f4c5e-7dac-3b08-8bef-c83b4927e825 | -10.94682 | -45.41879 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README33.md)
