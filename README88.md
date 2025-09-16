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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb358420-c5a1-3643-96c0-cdf30f5d310c | -9.08963 | -44.89383 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ee2ae585-4f5d-39ba-9869-97d8b3953a11 | -6.96897 | -44.55714 | 2025-09-16 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8ff11dad-636b-32b3-8b98-55e803f4f097 | -6.37507 | -44.4146 | 2025-09-16 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c7f81894-2234-3d49-a170-a791a18db6a0 | -5.53618 | -42.66158 | 2025-09-16 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 549a4601-b52c-3271-8284-7d3af99f914b | -5.5705 | -43.55655 | 2025-09-16 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 19d0ba01-c882-3bf7-b3ad-89b844f2cfad | -9.09455 | -44.86106 | 2025-09-16 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 953bb5af-aad6-33de-bf83-b91b3adff528 | -8.14229 | -43.63117 | 2025-09-16 11:57:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6bd311c9-d76d-374b-b21b-aa9ee870daae | -7.50946 | -44.70941 | 2025-09-16 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 52324a66-4f03-333d-91d8-3d142225ddfc | -6.96438 | -44.45583 | 2025-09-16 11:57:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b40368fc-e502-3e0a-93f4-23fcfe025d6c | -7.264 | -46.60757 | 2025-09-16 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7b52e26c-5080-31a1-b6ff-d495b246a0e3 | -8.59228 | -46.35172 | 2025-09-16 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 84e68ec2-6985-3b63-bf51-1a029ed3825d | -11.4853 | -43.5929 | 2025-09-16 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 076ac796-4d58-33d7-9362-e7a9b61d0d31 | -12.6729 | -47.9258 | 2025-09-16 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 668331eb-0c1f-37ec-93f7-aa7697c69c15 | -7.6946 | -44.509 | 2025-09-16 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 405472e8-fc51-364f-adc1-7ce9ab702031 | -7.9822 | -45.643 | 2025-09-16 12:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a38aa283-9a4b-37f2-bf58-f0f9f6449f13 | -12.6356 | -45.7422 | 2025-09-16 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 73842661-4281-352c-a260-27259fecf5a2 | -9.7409 | -48.1106 | 2025-09-16 12:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 077b5934-9ae6-3e41-8bf4-c3a23c4dfabf | -12.6352 | -45.7652 | 2025-09-16 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 47eb6c37-9e2a-3f79-8df1-66e1d01d6f11 | -7.6949 | -44.486 | 2025-09-16 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 01e66806-b5b2-34e6-b3c2-ccfb6edfd497 | -8.0007 | -45.6638 | 2025-09-16 12:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 68f4bf01-27ac-36e0-9f7c-cbc0108f8f68 | -4.5934 | -43.3239 | 2025-09-16 12:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 1611c4db-429e-3a9b-9a53-9756129fc4b0 | -12.6906 | -48.0121 | 2025-09-16 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 376b1baf-ce22-3290-8f0a-bd206709b760 | -8.613 | -46.39 | 2025-09-16 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ee94ff58-3652-3754-953f-2803c3c26221 | -12.6725 | -47.948 | 2025-09-16 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b7b403b9-b9d3-30d0-906e-a21a182c6b29 | -8.0196 | -45.662 | 2025-09-16 12:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 321.0 |
| c41785ac-a987-308d-aeff-8efd67e4581c | -10.7302 | -46.5082 | 2025-09-16 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0b3950fe-2929-31f0-b274-d1ba6d090ff7 | -9.0857 | -44.8893 | 2025-09-16 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b9837cde-1a22-3db9-a77c-b885c8214b64 | -12.6917 | -47.9454 | 2025-09-16 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1d04e127-cc99-3c2a-be7e-4c3a4f256a86 | -9.086 | -44.8663 | 2025-09-16 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 93eea4c9-1629-309d-9adb-12fbe1a9b0cb | -9.152 | -46.9812 | 2025-09-16 12:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 91204dbf-81b1-35d6-9567-a4bd36b721c0 | -8.5939 | -46.4143 | 2025-09-16 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f157579a-1102-3a1e-89dc-d5fe52fa71e2 | -9.105 | -44.8641 | 2025-09-16 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 17c91719-1ea1-317d-b0b9-1e8d90382668 | -9.7406 | -48.1326 | 2025-09-16 12:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 6802a1c7-20aa-38a3-97cd-11a576ab23ea | -9.5309 | -45.523 | 2025-09-16 12:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 36fb33eb-808d-371f-abe1-bcca3fde9a8b | -12.6909 | -47.9899 | 2025-09-16 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a52ae4c2-38cd-3b97-b36c-53f90ed99a20 | -11.7151 | -46.8739 | 2025-09-16 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 75fb3ac8-f2ad-3140-9482-abdff922b93b | -8.6127 | -46.4124 | 2025-09-16 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 05c46547-d00e-34e3-9f46-b72cb38fcc20 | -12.63958 | -45.74825 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 14ab3d67-a6de-3f7c-abf9-087173592c5d | -12.95065 | -47.15873 | 2025-09-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9f8750c2-0903-3b17-bc73-5025f9f45b4a | -13.64063 | -45.42738 | 2025-09-16 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cd4de5ce-284f-3fb9-94ab-c798cedbda28 | -12.68341 | -47.94801 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0a79c074-1dd1-377a-88e1-46f5b4e22920 | -12.68759 | -48.00676 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 3c981328-cce5-3d17-94de-7906b96f96c7 | -14.64602 | -46.36659 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3f638347-e439-3681-8f2f-1a37b2ed50c8 | -21.22397 | -46.94223 | 2025-09-16 12:00:00 | TERRA_M-T | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bb793ea0-e12b-3fd8-a75c-88fbec7d123d | -19.56228 | -43.78633 | 2025-09-16 12:00:00 | TERRA_M-T | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c9dee63-eade-3a1d-b1d1-90f7bb0529c8 | -18.89539 | -49.57952 | 2025-09-16 12:00:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 200.2 |
| 1de8c19d-79f2-3c97-8577-0c689e79fd31 | -19.15814 | -48.72374 | 2025-09-16 12:00:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 40.1 |
| cc293a6a-2a66-35de-9a0d-4331b3f339e4 | -15.90134 | -47.31255 | 2025-09-16 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b724c5c7-f5fc-3b60-a154-718deb91f98b | -15.41321 | -47.34436 | 2025-09-16 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 630c51cc-09cd-3ff1-9e64-d08970494113 | -18.90685 | -49.58194 | 2025-09-16 12:00:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7894103b-59de-3c21-b9c2-81d3af2b7a24 | -11.48528 | -43.6076 | 2025-09-16 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2d61eedd-8cb5-356d-8fe3-ed9d8c07b139 | -19.84041 | -46.4613 | 2025-09-16 12:00:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1f7e3cb3-8825-300e-a4cb-16a44bfbf259 | -12.686 | -47.93255 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a45ebcc2-4e5d-352b-8c3c-badd3a3658ce | -13.21728 | -47.29041 | 2025-09-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ee9aea49-1849-38dd-8598-efc3267357bc | -16.51111 | -41.41853 | 2025-09-16 12:00:00 | TERRA_M-T | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 90073216-f8d7-366f-86a9-7471fc0d10df | -15.53192 | -48.03882 | 2025-09-16 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 6f453515-0e25-3278-89e2-5ac9d019513b | -16.58863 | -40.60825 | 2025-09-16 12:00:00 | TERRA_M-T | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 339a73b6-c47d-345e-8bfc-2caa2fb673ff | -13.20407 | -47.30375 | 2025-09-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| bba5f5d9-425e-3fe2-af0e-e3c6b7ecc7d6 | -14.15897 | -46.13231 | 2025-09-16 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 2ad69b23-9cae-3a6d-8b4c-2de46a948244 | -14.35362 | -40.6968 | 2025-09-16 12:00:00 | TERRA_M-T | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b2e92ebc-2457-35cd-a209-46194e222a26 | -16.66925 | -41.73048 | 2025-09-16 12:00:00 | TERRA_M-T | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 29f8b3b9-422a-331e-834c-d9a910a3241a | -21.26747 | -45.69376 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 70a1b73b-898b-31a8-a102-15f62067c387 | -19.0087 | -47.14075 | 2025-09-16 12:00:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6967bbb3-ebe0-34d7-b869-7553a603e5c3 | -21.63065 | -46.22176 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 7b71c5d8-c943-321a-89e7-9956556b6e57 | -12.09822 | -42.82671 | 2025-09-16 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| dc712839-fe98-35b8-9c95-28dce88d4fdf | -18.56941 | -49.2612 | 2025-09-16 12:00:00 | TERRA_M-T | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| 1c47ac11-d4d1-33f4-9e08-8dbb1b40e29d | -21.62309 | -46.21032 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1cd1e0a0-a539-3722-9561-8bcde65de898 | -17.08736 | -45.81849 | 2025-09-16 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0c074c67-27a0-3da3-b9f0-f8974ee48181 | -12.6761 | -48.00483 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 232ef9e4-4350-3870-8787-c7c3db66b28a | -12.63785 | -45.75949 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 0ce9c5e6-9595-3dc2-b046-62bd360e12ad | -21.57178 | -46.1814 | 2025-09-16 12:00:00 | TERRA_M-T | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| e21740de-5fc4-3572-a2c0-4f303334ffcf | -12.67901 | -45.29975 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 5de84c4b-f88d-3d4a-b9c6-bde298f7ef11 | -21.57629 | -46.21261 | 2025-09-16 12:00:00 | TERRA_M-T | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| 84b08cee-eede-3dc6-a508-6323aab0e791 | -15.69215 | -49.91927 | 2025-09-16 12:00:00 | TERRA_M-T | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1e0c5ffb-4782-3b10-9933-a412d6215bc0 | -15.33055 | -47.41795 | 2025-09-16 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f83153d9-b1fc-322d-b316-aa0dc6770d35 | -12.1142 | -44.83103 | 2025-09-16 12:00:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d483b9ac-e45e-3ed7-8756-1cc0fb8953e3 | -12.11576 | -44.82077 | 2025-09-16 12:00:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 03e852ec-0ecf-3102-9133-bbee049244f0 | -11.28318 | -50.80169 | 2025-09-16 12:00:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9646ed76-9ff1-3a98-ab9f-9569b111d07b | -12.69014 | -45.29071 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| eb4d0e19-cefe-364c-8519-9985960556eb | -18.98101 | -42.19125 | 2025-09-16 12:00:00 | TERRA_M-T | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f0024420-26ed-32b0-8799-9829137aae67 | -16.34562 | -40.59085 | 2025-09-16 12:00:00 | TERRA_M-T | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 325a22c5-81bd-3dc1-bdb4-e11cf265d670 | -12.73797 | -47.1958 | 2025-09-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 68f894f4-5dcc-3bbd-8ab9-82927a52435d | -11.4298 | -46.92983 | 2025-09-16 12:00:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6f4f1cf5-13c9-31c5-aa3d-eca148a3b0f7 | -12.11731 | -44.81052 | 2025-09-16 12:00:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5787eb05-3bb6-3c56-a11a-2755ed6ddbb1 | -21.63213 | -46.21195 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| c0275fad-57a0-313d-8b2b-b78704bbed48 | -12.50832 | -44.23787 | 2025-09-16 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 03a7a0e7-6e70-3e74-8236-99a1e887a957 | -12.67282 | -48.01119 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| b063cafa-b90a-343a-a62c-f32764e0a138 | -18.42259 | -44.27879 | 2025-09-16 12:00:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 27a2f35d-5356-3908-aa7e-4dfa8ec2bf0e | -16.04477 | -43.83591 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b0053982-d0dc-359d-b460-17aa6a777825 | -16.53517 | -42.45353 | 2025-09-16 12:00:00 | TERRA_M-T | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7354cc54-30ce-3067-9345-8a784fc65764 | -21.494 | -45.90362 | 2025-09-16 12:00:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a827c0b6-88aa-3d7f-88e1-f75dadd70913 | -19.84202 | -46.45083 | 2025-09-16 12:00:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 29628ba1-a35f-34b9-8bf3-ccad0217e910 | -13.86235 | -41.54523 | 2025-09-16 12:00:00 | TERRA_M-T | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 12e6ab4a-f946-3e75-9074-08928913ad07 | -21.37063 | -46.34935 | 2025-09-16 12:00:00 | TERRA_M-T | MONTE BELO | MINAS GERAIS | Brasil | 3143005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 1b485236-2d3a-33e1-853e-b0e0d3974a32 | -20.82187 | -45.58869 | 2025-09-16 12:00:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 319b2ff9-c7d4-3c3d-9295-a8d3bdd9546b | -11.64592 | -46.59216 | 2025-09-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7c20a9c0-1d82-30b5-b411-d0956f5d4a17 | -12.70733 | -48.01684 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 5aa1accc-f921-393b-9f94-03d5daaca265 | -20.89685 | -45.82568 | 2025-09-16 12:00:00 | TERRA_M-T | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| caf13766-2f2f-37c1-abd5-b507b6b39ca5 | -15.89069 | -49.99559 | 2025-09-16 12:00:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e2c72f44-3c71-3d0a-8b5a-ee14fc16649a | -12.69318 | -48.03094 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |


[Clique aqui para ver as próximas entradas](README89.md)
