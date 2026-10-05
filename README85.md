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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c81784e0-94f9-31f1-a196-3399876d1533 | -9.61709 | -45.82416 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff98de3c-a75b-39a1-bd87-af3022e32eee | -12.05079 | -43.44157 | 2026-10-05 16:37:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d23a18fd-4418-39dd-b13a-ead3abfe9121 | -11.47957 | -39.49624 | 2026-10-05 16:37:00 | NOAA-21 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| d6bdc432-925c-337c-9cc9-45cccd1a1e86 | -6.69025 | -45.24011 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 7de39d10-db7b-3f6d-8a96-7404240f17e6 | -6.59433 | -35.60103 | 2026-10-05 16:37:00 | NOAA-21 | DONA INÊS | PARAÍBA | Brasil | 2505709 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0d267759-1177-3a88-ac25-2d14c79f5725 | -9.83946 | -47.00896 | 2026-10-05 16:37:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76689b62-17db-3d20-b4a4-58b05b6d57c1 | -9.75291 | -48.17292 | 2026-10-05 16:37:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8a88dff-9ec2-37fa-b7ba-14ea08be4825 | -12.14302 | -50.98985 | 2026-10-05 16:37:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c8a1fd3-0a1c-39d2-a2b7-072cd0dfa724 | -11.68797 | -43.66592 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 891a4320-3b6f-3afd-9109-1938f07dfaa4 | -11.64272 | -43.63215 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09cb1b16-c955-326a-8b9d-b3e635a54ec7 | -9.87019 | -44.83931 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e4854c99-ac15-3a7e-b562-c5567a41cf0d | -6.68844 | -45.22858 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 470ad96f-93c4-3031-966b-83e9bb94a54d | -10.94938 | -45.42859 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3c713213-179e-359a-a58c-314db5170c5e | -11.02325 | -41.28133 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a94e8fdd-3eb9-3fae-ae61-506f946ea209 | -9.85091 | -44.78437 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 67a622ea-1506-31d5-965d-90a7b059c6dd | -11.00696 | -53.9986 | 2026-10-05 16:37:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1f167804-8373-3b73-8237-365af3cf56c6 | -9.85434 | -44.78379 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5812e71f-ddbf-358f-ab8e-a1c6f2bc212f | -6.34284 | -42.54345 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| a9465d54-af6c-3a16-9cea-17d41d4fb016 | -12.43289 | -51.33469 | 2026-10-05 16:37:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f5f683c-e000-32e0-b29a-e6ea09b56b4f | -8.53539 | -54.58667 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 17945789-77a0-3e6d-8318-358efe4fa7da | -6.3742 | -43.63731 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c4932de3-6b68-3196-8484-3435e262be6c | -6.68965 | -45.23628 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c930aea5-4e1a-3df1-b253-e575be5a7709 | -11.95859 | -46.39643 | 2026-10-05 16:37:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 257b56dc-44be-36ae-817c-6dec9ab232cf | -6.37607 | -43.62977 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 33630dd8-c075-3479-a2d3-bfce82b8d3bd | -7.48174 | -40.27873 | 2026-10-05 16:37:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 516b09ea-9e5a-3d8d-858e-14513c328fbf | -6.68212 | -45.23352 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f020b306-fa06-3bb5-987d-a15feb246feb | -6.69882 | -45.2269 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4b10d275-1c55-37c6-b2ba-363e3b110111 | -7.19487 | -44.30371 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91ba511b-a875-3152-86a0-a3a759a5eb51 | -13.51257 | -40.76858 | 2026-10-05 16:37:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| be779a94-e902-354d-a7e0-3f77c9042335 | -6.85559 | -38.67718 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 31e8a623-8b97-381c-8671-e2f5a034a982 | -6.87716 | -43.67722 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1fa43364-5f4d-3cb6-b832-0790ad96961e | -7.2053 | -44.32302 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b6f483fc-5abe-343c-87a6-b684638bcf61 | -8.53095 | -54.58409 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ccfd27b3-17c1-3cf9-8af0-68e5494962db | -6.63037 | -41.78715 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 028f8b4d-8537-3f51-a2bd-7fd407712286 | -10.12253 | -45.9059 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff10fa18-0eec-3f9a-bd2e-118952c21d95 | -9.16114 | -45.12919 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| e221a633-61c2-365a-b59f-a6f2c735588c | -11.45823 | -43.39419 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| eb8becc4-b09e-3d51-872d-a566e54780e6 | -7.64894 | -44.37682 | 2026-10-05 16:37:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d69dda27-bf75-38fa-92af-563f0778f2f2 | -11.63149 | -43.62988 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 0443f314-ebd0-3079-b978-90dac9a148bf | -9.60106 | -46.42595 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9745b653-4b1d-3fa3-92cb-69c5859ae7eb | -7.26586 | -44.29774 | 2026-10-05 16:37:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 321be1e9-b5c0-3d96-a330-beacd4829571 | -11.07445 | -47.49491 | 2026-10-05 16:37:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10ec105c-b6c3-3aed-8ba2-cb8205f9dcad | -9.76299 | -44.8059 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d87421c-0a71-39c2-b1bc-334c8be00a9e | -6.88462 | -43.67606 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| eef6fa6c-2490-307c-a086-37a7be034d28 | -10.39871 | -40.51018 | 2026-10-05 16:37:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8fb70e1b-3be8-37e9-93e1-5bbec406ec59 | -7.57458 | -46.20364 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77770fdd-1566-3c6c-b9c2-f1ced6919727 | -8.66434 | -54.55941 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 91f62bf8-27da-3d07-bcfa-db65d38b4108 | -11.38 | -47.72648 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bdb9f058-7bd0-3815-8ea8-5ca016ff781e | -6.70528 | -45.24555 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a44abb2d-9e5d-3de0-a98d-fea2c8ac8128 | -11.719 | -43.49969 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 841be501-4a30-3f5c-9438-312a5383bc6f | -8.53943 | -54.5809 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 731eb5a9-577c-39e5-8f12-c7076931cd88 | -13.86253 | -43.20101 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 896a1a43-9212-35c2-9f0b-49227f4aeba2 | -6.2866 | -43.08215 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8b58819d-f730-30f9-b488-21798675b970 | -11.63501 | -43.62927 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a32a4c17-fe90-3bc4-a26a-3be038e56f55 | -9.77207 | -44.79669 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d5885ec-7280-33f8-8727-852c5c50d21d | -11.67965 | -43.65912 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c3e81980-536c-3722-87ef-8ea8c8a9ab91 | -6.7267 | -44.28172 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f3717517-1f77-3749-838c-31613285f6a2 | -11.81828 | -43.52928 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7562e5c8-d6f9-30ac-b12c-70247513e1bf | -10.97886 | -45.44194 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 54edc7ea-9b1c-3b88-90ee-9cd70d24f1f1 | -11.15951 | -43.49708 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| b6cb4832-b198-3d52-8bad-a32469e006ad | -6.35607 | -42.52335 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| cd288567-24fd-3901-b22b-590d7b8a4755 | -14.07861 | -43.77321 | 2026-10-05 16:37:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a5172f2-6a24-3c98-b406-6701b13d1374 | -12.59431 | -47.21661 | 2026-10-05 16:37:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7eab6c54-2a6e-3473-81e3-5473e9f465be | -12.5579 | -46.6753 | 2026-10-05 16:37:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| df18f67e-de09-36cc-ae9a-a9a3b9bf1d64 | -9.85735 | -44.80273 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d599a89-ea6a-34e2-aab1-71d9346c4022 | -11.64493 | -43.62346 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a1d539d2-03dc-3b80-9882-81c7b69e88ff | -18.58993 | -41.27699 | 2026-10-05 16:37:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| f2388dbd-438d-3894-aa36-ed2e8c5baf16 | -17.82957 | -41.4244 | 2026-10-05 16:37:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| d6a000ba-aa45-3c4b-bdef-4a5dc26a3ce8 | -10.97998 | -45.44909 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| ec8fcb1e-339e-33a3-bebf-545863a9fa12 | -7.71529 | -37.02291 | 2026-10-05 16:37:00 | NOAA-21 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 0496ec53-9914-3be3-b555-f5731ee5ca4d | -8.53231 | -54.59447 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8c0e4215-83cf-3223-a1e1-6abb9b773633 | -6.72241 | -44.27809 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b3c7675e-4295-3a9f-b9cf-e519d023984d | -11.80501 | -47.3623 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e17a938f-3cf9-369b-8960-30d6754483d6 | -9.0212 | -37.68493 | 2026-10-05 16:37:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ccea9f3c-4225-326e-8ad3-edd219ff8e34 | -12.35058 | -47.06051 | 2026-10-05 16:37:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e2555b9-c498-3dac-a34e-fd5460fc2aa3 | -8.52659 | -54.59317 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 92b53b9d-5d24-3819-8d13-f9cae66bc02e | -11.09458 | -41.25782 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6532d509-1cfa-36d5-9406-c18b237c21b1 | -8.66638 | -54.53828 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b1374f41-a183-3387-8d9a-8bde702224e6 | -7.94311 | -43.84487 | 2026-10-05 16:37:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| fa62e82c-428f-3651-913c-a45dc5f341a9 | -6.71414 | -45.54924 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 26401e36-c97a-35dd-b0b7-c15b4e26bc68 | -7.24223 | -44.01297 | 2026-10-05 16:37:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 213528f0-57a4-31ba-8e53-c770a265181c | -11.63788 | -43.62462 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aeb4155c-fb4b-36c4-8251-5f60fe0db8ba | -10.58661 | -41.24863 | 2026-10-05 16:37:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| a1e70caf-639f-3b35-b644-3b2ced2f139c | -6.70063 | -45.23845 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 607ea22e-f541-331b-9cbf-35bea5c234e6 | -7.15356 | -44.68349 | 2026-10-05 16:37:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4fa6098-136a-3a16-93a3-e6c4d446804a | -8.34602 | -44.7467 | 2026-10-05 16:37:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78ed46ec-f4b4-3c09-834c-9365ee9835a4 | -6.61459 | -44.16878 | 2026-10-05 16:37:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 52cf1d57-6306-3dc1-b2e4-1d5e0a3d88ba | -7.73344 | -45.47096 | 2026-10-05 16:37:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 012cfbd2-bec2-3759-afa5-465badb31288 | -8.5273 | -54.59833 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c751d676-4022-3633-8982-ec6f877d7bd8 | -11.66584 | -43.64076 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2461062f-df18-3b56-b3db-4b93f66996e4 | -8.53278 | -54.60279 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ee972000-2245-30ec-9cc0-08a55df22648 | -11.26647 | -45.2368 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6c18e122-bc59-393c-b5e2-ee28af07ddba | -11.82557 | -47.3628 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4d64a0d-c605-3e05-b605-9d2b00460006 | -6.68152 | -45.22968 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f9b42cb-2415-38bb-b739-a76f8e4c2092 | -10.1801 | -46.72241 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd802cef-d603-30be-bfb5-f72d22124a0b | -8.55 | -54.58155 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b75d620d-d9be-3a82-9ca1-009ac80d3013 | -11.92694 | -46.816 | 2026-10-05 16:37:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8572dcb5-c2cf-3a44-ab19-2fa1d8a00c59 | -6.69311 | -45.23573 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 33025bd4-bba4-34d7-adb6-732f6cc195aa | -11.80941 | -47.36894 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c4b3404-e8fb-3791-bc78-af00462d102a | -7.5584 | -39.0898 | 2026-10-05 16:37:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |


[Clique aqui para ver as próximas entradas](README86.md)
