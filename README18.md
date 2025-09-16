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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93dde3c0-ceb4-338f-88f4-777697574a4e | -8.0895 | -50.15928 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e44701b-46e0-39a5-8bb3-54bc8b4f6110 | -10.96157 | -49.57101 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fef02404-32f0-360c-93b7-2efe91fa0e60 | -11.12312 | -45.35351 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6eac66ee-4b6b-3a9c-a285-c61bf6d77636 | -5.76661 | -43.97115 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bca3061-a867-357c-b5fb-39ca159697f6 | -6.44572 | -43.30947 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f98bafa-fb4d-334b-8259-e47742a4a511 | -10.72115 | -44.7481 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bc15042a-e679-3c10-b7f2-953d4eaf600e | -5.78641 | -45.93656 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab1941a3-ddea-3c43-a38c-a69a81fc39fd | -5.21374 | -45.1826 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8159efbb-b910-336e-9ce4-1fa27c9dc9c2 | -5.89565 | -45.75172 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a369d33-1425-3aa7-bff2-7c4b9e5b6b11 | -6.1761 | -46.8164 | 2025-09-16 04:02:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae28016-f16d-346e-9138-8eef67259d20 | -8.87796 | -46.19232 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fad7739-42cc-3609-8bfa-67390518a4f9 | -10.73816 | -44.7598 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2bb5b99-8011-3cba-ab4c-357f146e39cf | -10.44509 | -45.15234 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 346825cb-727d-3b9e-bc05-5448c8d752c1 | -11.12258 | -45.33369 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe8bc3db-0f38-3f0c-a466-1c6e8e48736b | -7.19315 | -48.60403 | 2025-09-16 04:02:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 258fd25e-d0f1-3c06-9523-737a8a0db037 | -6.45034 | -43.60296 | 2025-09-16 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be003206-135c-3bc1-b76b-649f4eaa08d2 | -7.27189 | -46.59897 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b31f992-cb82-3210-b521-9516ccdd6431 | -7.69058 | -44.67129 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62343e22-ddb8-31fb-b0e8-96013883c70f | -11.3505 | -47.3622 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e686d6ce-3240-3455-abba-eaf9022d52d8 | -8.42519 | -47.20833 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6b30f11-2161-376e-91de-b04590ca32fb | -10.64166 | -48.74799 | 2025-09-16 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d7babdc-73a6-35b5-b897-59303bbd64d2 | -7.36608 | -44.28867 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 520ce894-9b3e-3c16-9ae9-ae2869a7d75f | -5.66293 | -43.32267 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be7a0d6a-d6d8-302a-896e-060e745c024a | -7.71203 | -45.304 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8521b439-10d9-3d79-8ba9-ef14ea5e215c | -8.60422 | -46.33803 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e985896e-a6a4-36eb-a472-7f5aeb0bccb5 | -11.46665 | -48.69633 | 2025-09-16 04:02:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d66ce9d-9314-360b-88ac-9bfd297aa9ab | -11.50478 | -43.72377 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68f8588e-0edd-3239-b995-5c9daea08aaf | -11.24104 | -49.95498 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23da7c6c-45e7-32ad-9349-068de2c57dde | -5.34725 | -44.83052 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54534294-9f4f-3afd-b28a-886b076976a2 | -6.25463 | -46.11842 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ddf932-1a85-3e59-b933-782d0e5e159d | -7.7286 | -45.30305 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77b9e592-efc1-3dd9-8302-d4d90fabea60 | -6.40331 | -42.65548 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e66abe84-0825-300a-9a35-ee07a95fc748 | -11.27991 | -50.79889 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 086a3924-e3b6-356c-9059-f0c36c916003 | -11.3529 | -47.36143 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b097167-9029-3789-9e63-423a57b31d36 | -10.64277 | -46.2271 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8a4bf73-e988-3b92-94dd-5ba35ec2786c | -10.11407 | -45.66705 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a1c8a27-955f-3de5-ba52-7be9cc25cb9e | -10.63747 | -46.2337 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9def3fb-d97a-3a81-b583-c041e2712830 | -10.64011 | -46.46233 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47f92f70-8395-3586-92db-426d5354629f | -5.81241 | -43.48639 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fd7b24f2-b4f3-3f7a-be67-cdd61649b00e | -10.961 | -49.574 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da632b1-2892-3b24-9a0f-d09edccf8014 | -6.76177 | -48.11465 | 2025-09-16 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2933ca38-ebb5-3850-80eb-3fc182484a11 | -6.13158 | -43.37125 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ad65bc-5eb0-3227-80cc-a3f6ce6060d6 | -10.64984 | -46.47254 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0ec6e84-354d-3915-9cd6-f336e3ad94c9 | -10.04897 | -44.34773 | 2025-09-16 04:02:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 997f881f-e536-364c-abe7-8b4e7366d1cf | -8.88146 | -46.1968 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f76907-ee51-33ea-96ee-50c141bf56ee | -8.92583 | -45.47012 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 912b84fd-a9f4-3d19-935e-f86cb6bd2de4 | -8.95386 | -45.87366 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06ffd21d-98de-37b8-87e8-ffef77314c1d | -7.97311 | -45.63755 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 210e1426-48fa-3d94-b3ef-8b874d8226ee | -11.4359 | -46.94574 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 019bad85-7a05-31ab-91bd-51b6cc121893 | -9.54166 | -46.30203 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3463202-69dd-3e42-a2ee-002bc2b9dbdf | -7.67484 | -46.30714 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f09e1a1e-4867-341d-9bf5-6b3dd3b3ec32 | -8.77121 | -46.08151 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0116608-608f-343a-b456-4d51f2a68073 | -7.68125 | -44.67973 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59bfc653-777a-304d-9073-a45975781d87 | -11.33682 | -43.48412 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60f327ab-5f34-3bab-baf8-03485b40c0ee | -11.76401 | -46.66636 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d409492e-5d7d-326a-928e-38ced82b2b5d | -12.11417 | -44.8251 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee760dda-6309-3278-922c-167932d1161b | -11.63565 | -46.58625 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90b002bb-5215-3e25-8184-8a7f539e255d | -8.99036 | -45.75689 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 912be76e-14b9-3db2-8cde-73d080bd7dc9 | -10.74187 | -44.76038 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 66b493fb-1c3f-39ca-9f06-a56d1c606f20 | -8.89165 | -46.18724 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac77706f-d312-3bb9-beba-65e223fe3c0f | -11.14076 | -45.34173 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8908a82b-2d6e-352d-80f3-7333b40c5dfe | -7.71767 | -50.35921 | 2025-09-16 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2050fd3-8bd4-3c68-9559-aca6974fec74 | -5.64454 | -45.95092 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1802d23e-7c3f-378f-ad62-a8b81594550c | -6.29252 | -42.39119 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 32f47722-c80d-340e-9437-a4b46f3a62df | -8.9686 | -46.03434 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fcbaf3f-1535-3d70-acba-507bc425aeae | -9.14997 | -46.93999 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75cc1925-3d57-302b-ad9d-739132e631f2 | -7.43032 | -44.87362 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e77eefd-54cb-30c7-8092-70f6cb5e629a | -5.79158 | -43.93721 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2d66a02-93ae-3b58-b401-ec9d4d5e5566 | -8.39868 | -47.25492 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9822edf2-aab0-3ae4-ac09-c49f28a3cfc8 | -11.426 | -46.9283 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4044db5-702d-3a89-a013-f514ca1b0251 | -6.18712 | -41.18848 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2c670692-3a3d-3944-a952-c3484afc9820 | -7.2683 | -46.59371 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ff69e999-d100-32c3-8c04-e04764c61c99 | -11.43702 | -46.94533 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 21a28a12-f0e4-33e2-9d80-b4f6b710ee46 | -6.22134 | -43.90054 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38fe6a79-b843-33e8-b528-fc0ac7f78191 | -7.36912 | -44.29371 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f76b7de2-fbfe-3d02-9219-b170ce11812c | -5.23808 | -43.68861 | 2025-09-16 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19077fab-6f10-34f0-91ca-6ee8ee429d82 | -5.99887 | -43.69781 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 356edc05-a118-3bbd-840e-9b449ca527b6 | -8.95448 | -45.77281 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17fd86c1-0ab7-381f-91aa-3f289e6900f1 | -6.16263 | -45.99521 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5af09ebd-98c8-3e68-ad44-f6eb3546266d | -6.34179 | -43.16614 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 34ee848d-7ca1-3f99-af30-7f1593bc4e4a | -7.6819 | -46.2915 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baf770a5-c09c-3018-8669-8f12d33d854b | -12.11565 | -44.81623 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77c62c18-f283-3806-86e3-1ee4d38f2205 | -10.71696 | -46.50011 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 86bdbaeb-064d-394f-90ad-6f9969f29a6b | -7.05499 | -44.17221 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f83733b-e3a9-35b2-b6e2-a9f346e65b46 | -9.04929 | -44.85168 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fed451a-4b34-3095-874b-a3dafef5c8ea | -4.17856 | -48.56982 | 2025-09-16 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4217a6ad-3918-321c-8109-488221eba4a3 | -8.08742 | -46.83146 | 2025-09-16 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc65b5cd-5d0d-3c42-b6e6-2734f708a783 | -9.06653 | -47.03331 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5e240aa7-9e28-3749-a8c7-474609b4ff76 | -11.39906 | -43.68183 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83e47137-ccce-3c00-8242-91f5392db3f5 | -10.84023 | -42.80166 | 2025-09-16 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b2a5478-babc-35eb-a42a-e1197acbd701 | -11.44074 | -43.53645 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d753c420-2b07-35ab-8c9c-b786307671f8 | -7.9806 | -45.64258 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f30c494-0de3-3eb4-af95-c0fbc09d2205 | -6.18617 | -45.11721 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fbeddb7-252c-33f3-9f34-48ee96e0ae4a | -4.79628 | -49.54261 | 2025-09-16 04:02:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437d78b3-a76c-38d3-8f31-d42c1522607a | -5.14293 | -45.39082 | 2025-09-16 04:02:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b649c5bd-0e95-3800-91ea-553ae3dada25 | -7.98682 | -45.65505 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d42e493-9ccf-3f3b-9f20-0ac99fdbc1be | -6.18963 | -45.1214 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa86f1ef-a61f-36b2-a10f-d1b9d8061f2c | -5.79209 | -45.92894 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85b01930-0f9c-3cdf-9d4e-e03c2b9f85ae | -11.70706 | -46.86937 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 636a61ba-0613-3d56-87a0-552ff7c3bb8d | -5.77611 | -45.8931 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
