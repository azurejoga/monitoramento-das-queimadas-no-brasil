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

## Dados Diários - Página 240

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2aa2218-2fbd-37d5-aa5b-519a891a494c | 3.5493 | -60.2633 | 2026-10-09 13:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4f62f7d4-7483-3429-b6ec-4c562938b7cd | -10.4901 | -47.3201 | 2026-10-09 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 24e8e2f7-a38d-3328-a75c-a85cda2da4ef | -14.0044 | -48.7743 | 2026-10-09 13:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 045c5a2d-4cff-356f-91f5-3364db2dcffe | -9.8629 | -47.4809 | 2026-10-09 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 8e362de3-9b9d-31ef-93d4-fa643dce2e3b | -9.3101 | -46.4509 | 2026-10-09 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ef4daed1-56f0-3439-a7ca-83b83d721cd8 | -12.2158 | -57.0887 | 2026-10-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 68d27df5-8742-329e-af36-3d0a431a2f3c | -12.2343 | -57.1271 | 2026-10-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 27e7c2ec-6b39-3853-9c6a-ad86f8cbae4b | -10.4334 | -47.3046 | 2026-10-09 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| bdb5f4e4-d008-3c13-a2e2-a65bf28794b8 | -12.2149 | -44.6057 | 2026-10-09 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 858b7abf-7405-3e42-bd06-d041dfb49630 | -8.2364 | -46.405 | 2026-10-09 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 815f36ab-b637-3f24-8629-362bf6a3c063 | -11.2259 | -45.3064 | 2026-10-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 8ac1c42a-36a2-3b9c-90db-f2933c6511f9 | -9.0826 | -45.1186 | 2026-10-09 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c6fb72a5-664b-3a59-b964-f7a643dcbb99 | -11.8783 | -47.3892 | 2026-10-09 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 88431bfd-6189-3efd-9f52-41f74d3672d8 | -9.9208 | -44.7893 | 2026-10-09 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 271.6 |
| 673659d4-ca5b-35c5-b697-83d3ed105fcd | -10.491 | -47.2533 | 2026-10-09 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 6fba1496-c6c5-3135-8454-7d54d77dbb76 | -10.9536 | -50.6805 | 2026-10-09 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| feed21a3-20a0-3d0b-ae47-9bcf33f43799 | -11.8495 | -43.6072 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| a9504741-713c-320c-b919-80b05930f94e | -14.0238 | -48.7714 | 2026-10-09 13:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 5113811c-d2d8-3a9e-9e20-a9ce2a03357d | -12.2346 | -57.1071 | 2026-10-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 218.1 |
| a6856927-3eeb-39ae-99f0-39137101b390 | -8.3234 | -45.4506 | 2026-10-09 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 9f1625e5-6531-37f6-89af-a5480e3ee62b | -8.911 | -45.229 | 2026-10-09 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 5c46999e-4a4e-37eb-ad5a-574fb80f31ae | -12.8316 | -45.5509 | 2026-10-09 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 9740b7e2-7a26-3120-9b95-43697c36744d | -9.8798 | -50.4918 | 2026-10-09 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2c9c79a1-e742-3231-9d22-a755e0f4376a | -12.2156 | -57.1087 | 2026-10-09 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e47a6396-1533-3680-820a-c55867350b53 | -12.1729 | -44.7983 | 2026-10-09 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 266.7 |
| e9c6546e-ac4f-3e2b-81c6-df3c68bb1073 | -9.1015 | -45.1164 | 2026-10-09 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 299efd75-3118-38fe-93f4-ad98947e140c | -7.4883 | -42.8532 | 2026-10-09 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| d1dc0108-22ad-3775-8176-79a2965fd179 | -11.8499 | -43.5835 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 16879e94-8cae-3600-a3d3-0c5aeabe16b4 | -8.3045 | -45.4525 | 2026-10-09 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 773302fb-9665-35f7-8726-3dee5a1361a9 | -9.9018 | -44.7917 | 2026-10-09 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 51940a66-a1af-3d47-bc3f-c6abd8b5568c | -11.6566 | -43.661 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 56486257-77ad-3b13-8668-2c351c161aae | -18.0688 | -44.6019 | 2026-10-09 13:50:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a983fac5-699e-3986-a835-1d43548484e0 | -12.1725 | -44.8216 | 2026-10-09 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a549c0b6-ceca-37e5-b9c9-dd7e941b36c0 | -11.8302 | -43.6103 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 261.8 |
| d6759dd8-3681-36dc-8e34-3a0ef1e0f374 | -9.8818 | -47.4788 | 2026-10-09 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a6d113cf-4c94-3002-8b92-2a9751401ed6 | -7.4886 | -42.8295 | 2026-10-09 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 914f474a-42da-3356-a75e-4269145daa0b | -7.4694 | -42.8551 | 2026-10-09 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| ad630d39-89c6-38e7-8ae7-176563c99e7b | -12.2145 | -44.6291 | 2026-10-09 13:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| aebab802-8afd-39f2-b35e-9bb139140f3d | -11.4128 | -46.6897 | 2026-10-09 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 195.2 |
| c0b19d95-ca6d-390d-9a6a-6928d57cb5cf | -18.3327 | -42.3849 | 2026-10-09 13:50:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 8658bd6e-c72c-3f61-8c27-ffa720f29d40 | -8.0575 | -45.6357 | 2026-10-09 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 27db8961-026e-3e6b-90de-9fe826ae832c | -12.0063 | -43.4402 | 2026-10-09 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 978a0d4c-56f4-322a-83ee-1819b320ca4b | -11.8787 | -47.3668 | 2026-10-09 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 89e1f421-e977-38f8-8ddd-04f9afcac7ce | -12.0054 | -43.4878 | 2026-10-09 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 77c0c091-751f-3584-a744-670428344ba7 | -8.0766 | -45.6112 | 2026-10-09 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 5b956077-5422-3ddd-98f0-391b5de24276 | -16.6321 | -47.203 | 2026-10-09 13:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c59a1fbd-45b8-33bb-ad0c-b92f97e90811 | -11.5998 | -43.6226 | 2026-10-09 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 29d65c4f-34b3-35a6-a3a3-be2c80effccf | -10.5087 | -47.3401 | 2026-10-09 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 52972cf5-b72e-3281-b81e-5ad47b43ffb2 | -11.245 | -45.3037 | 2026-10-09 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 0b79829a-c51f-3139-a21f-865750fdb9e2 | -9.1012 | -45.1393 | 2026-10-09 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 30998410-df84-3a6d-ae49-2456a456d363 | -10.4917 | -47.2087 | 2026-10-09 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d166b0a4-e215-3814-9890-0bdae7951fc5 | -8.0764 | -45.6339 | 2026-10-09 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 6309349c-51f7-3a05-bc92-9829be1d8d66 | -15.3838 | -41.878 | 2026-10-09 13:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.9 |
| 3b212b3b-fe42-326c-abf0-f451181f09ea | -10.7475 | -46.6184 | 2026-10-09 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 7f0177b2-45a8-3afd-ac95-6fba48fd5c93 | -7.4697 | -42.8315 | 2026-10-09 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| e61bd5e0-50f1-373b-a9ec-53babe3a7515 | -11.4131 | -46.6671 | 2026-10-09 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 395.7 |
| 4b9e0ed5-91fe-3e16-a5e0-51159ef96c3d | -12.0063 | -43.4402 | 2026-10-09 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| e8327ba7-671c-3b21-b0ae-383bef288cda | -16.6321 | -47.203 | 2026-10-09 14:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 893d9781-3ae7-3ca2-95ef-dab7accf72b5 | -14.0044 | -48.7743 | 2026-10-09 14:00:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 00a36083-8e59-3f97-b99d-89787b92e050 | -10.9533 | -50.7018 | 2026-10-09 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 60f08904-af89-33ee-a97f-58ef9a341ddd | -10.7475 | -46.6184 | 2026-10-09 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 4117c0d2-e461-3724-ad7b-4cc2a1cec59c | -18.3327 | -42.3849 | 2026-10-09 14:00:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| f5968fd8-b3b3-3c3f-82b4-30e272fa2a0d | -12.1725 | -44.8216 | 2026-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| e65d8c2b-6133-33b2-aa1b-6676211a4a6c | 0.5246 | -50.8991 | 2026-10-09 14:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 60384450-0f9c-319d-9996-99fbdd645f72 | -15.2541 | -42.3495 | 2026-10-09 14:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 649e7943-43b1-3844-8420-7ffa087c4536 | -12.2504 | -44.7631 | 2026-10-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 5fce61f1-3870-3026-8874-e6fee4e61d2e | -11.8302 | -43.6103 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 6097161b-09b8-3c60-b1a8-1311a7abc718 | -12.8123 | -45.5539 | 2026-10-09 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 87ed3fba-bec9-35b5-a508-8fa1756aca03 | -15.3832 | -41.9029 | 2026-10-09 14:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| dcad96ac-8eb8-318e-81a2-02a55f343ef2 | -13.1056 | -46.3321 | 2026-10-09 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e91194ab-1451-3317-a901-0cf4e714a45b | -12.2311 | -44.7661 | 2026-10-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| f57a74a4-217c-3104-a538-a8b3b34e2928 | -11.8495 | -43.6072 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| eba55036-9702-3e2d-a850-45ed1126bfe3 | -15.2535 | -42.3741 | 2026-10-09 14:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.2 |
| 6d7187ec-7cee-3b36-bfd9-4e5b33964f0d | -11.5998 | -43.6226 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9fd46226-5880-36ac-938c-0dc640057829 | -12.2154 | -57.1287 | 2026-10-09 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f25a7eb7-a535-3041-be48-a9ee87632031 | -9.0147 | -45.9434 | 2026-10-09 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 802b1c8a-81d4-3c02-b333-ab74aeb1e880 | -10.8979 | -45.5343 | 2026-10-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a9c6c823-5606-3720-9631-e25d9bf7c36a | -9.1015 | -45.1164 | 2026-10-09 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 2dcc914f-14fe-3b50-a7f5-a0aba792d5df | -15.2738 | -42.3452 | 2026-10-09 14:00:00 | GOES-19 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |
| 69847ecd-8e3f-36ef-af2e-ad57853d5148 | -7.3909 | -44.7445 | 2026-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a241f963-b8f5-30a0-a091-2ce48e47aceb | -8.9775 | -45.9023 | 2026-10-09 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| c8c92d1f-d5cc-3128-89cf-d46a3ddddcd1 | -10.9536 | -50.6805 | 2026-10-09 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f1d1efa7-07ee-3336-803b-45008a15199d | -10.4917 | -47.2087 | 2026-10-09 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 4067f6dd-b7b5-3062-9177-8c4e5ce85cca | -9.0826 | -45.1186 | 2026-10-09 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 179.3 |
| fbc63eb0-f7c0-3b8c-a4f0-65decb15d157 | -7.4694 | -42.8551 | 2026-10-09 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| a223885a-dbf8-31e7-a40b-b47293050c86 | -11.6566 | -43.661 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| d709e740-67a8-31ab-9805-8f1aa17723dc | -11.8787 | -47.3668 | 2026-10-09 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| b2658ee3-077e-3c85-acb6-4e6757b8b440 | -11.245 | -45.3037 | 2026-10-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 8400505a-086a-3711-a751-d3230783e21b | 3.5677 | -60.2058 | 2026-10-09 14:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cbe60b9c-bfd0-3d02-bf51-823663b3341f | -9.0829 | -45.0957 | 2026-10-09 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 222.8 |
| b287cfd4-b2bc-3bf1-9ad9-27a164cfc160 | -14.3611 | -55.0114 | 2026-10-09 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 357057bf-3f5d-3533-8884-a6300e4b0795 | -7.4097 | -44.7427 | 2026-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5a379d71-2e09-30a4-8236-a432f94dfe6f | -10.3921 | -46.2575 | 2026-10-09 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 0517b435-51d8-3e08-b422-4e5bd3c05412 | -7.3245 | -43.9681 | 2026-10-09 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| fa33433a-0fc2-3219-bfd9-9db4498058dc | -11.5989 | -43.6699 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 20998b2d-58c7-3acb-9647-4fa7f3fb25d2 | -12.2307 | -44.7894 | 2026-10-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| b8672347-ac24-3cf0-9212-2176e4df30ad | -8.3234 | -45.4506 | 2026-10-09 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 462e4257-4215-36f7-a7ba-d8ba99fc512f | -7.4697 | -42.8315 | 2026-10-09 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 43365cdd-9460-3232-939b-960da7120b74 | -11.8783 | -47.3892 | 2026-10-09 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 0cbcb2e8-8513-3d25-a264-bd683f99e94d | -12.0054 | -43.4878 | 2026-10-09 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |


[Clique aqui para ver as próximas entradas](README241.md)
