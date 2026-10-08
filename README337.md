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

## Dados Diários - Página 337

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c9743e-146a-3b9a-b400-d4fa8902eb46 | -8.92818 | -45.18723 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 353.4 |
| f7c8a109-7f0d-37c3-aed3-50685be54001 | -6.9893 | -43.97588 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa8be2d6-3743-3671-b053-e89edf34a590 | -6.22251 | -44.85424 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 340b1930-851c-327c-bf54-9016d78bf97a | -6.21972 | -44.85831 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 05d1a54c-2810-33cf-9944-caf994b46e9d | -9.97679 | -45.97194 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b63cce00-8723-350c-8ec5-a99d299be609 | -8.27242 | -46.90929 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40130483-62cb-3ef4-bc0c-fb044ba99820 | -11.07862 | -44.01256 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 19696586-80e3-3c34-9c94-a83c15397512 | -8.98036 | -45.93146 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 61a44bdd-13b6-33c6-b604-121376e146ae | -10.49911 | -47.30943 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c57afcbd-f644-3c00-9df0-aa3d13626683 | -13.22689 | -54.49703 | 2026-10-08 16:37:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7b98c7c1-b32d-3e29-b5c2-4283855f1813 | -6.97369 | -45.12294 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7c74e84a-69b2-3c30-9c0c-d5d2fa1cda25 | -10.43785 | -47.2914 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c7606ff7-393e-354d-976b-a48376661672 | -7.40819 | -43.74133 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| c1b0d5d5-d2f2-3f29-9214-a75c9e40c46c | -6.16081 | -42.59076 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| cbf30ee0-51c6-36c3-98aa-bfac6f6d1e09 | -14.18362 | -48.67105 | 2026-10-08 16:37:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b1d9dbea-7a1d-3be0-92d5-eb4cfcf69fe8 | -11.36318 | -46.71351 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a090558c-a1fa-3909-b28b-f467709fbbb0 | -6.31551 | -35.15382 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 97013634-ab94-3a64-9277-710a660b45b9 | -11.97589 | -57.58627 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 4e9bc082-81bc-3e1f-8098-738e6b8672f6 | -11.26197 | -47.74323 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdc6c119-eed2-31d5-b160-70eed95f56fc | -12.04508 | -43.43492 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| f3fa5835-9312-356d-9282-b76d5e0e8be2 | -11.79149 | -46.77305 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 281ff41e-0a2b-37fa-9740-31658a2694bb | -11.09083 | -44.00333 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b534cdad-f70f-3757-b0ab-7bdac3586a46 | -5.76107 | -42.06754 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| bb4fa354-1235-307b-9149-ed1b43ed88dc | -8.39866 | -46.91231 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 019189f6-b529-3381-b2c4-07589b237fc0 | -7.53652 | -45.87167 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c5481f7c-ebc5-3511-85b8-9f0d5a374d12 | -8.38235 | -46.91855 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8504a8d9-21b8-33f6-8922-816065696c9a | -10.87311 | -45.55118 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d1791b9-625c-3409-bd54-a42f728d2c80 | -10.15437 | -39.24749 | 2026-10-08 16:37:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 8507aa41-bc67-31ba-b7eb-e789df3bd454 | -8.30241 | -45.71071 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f146a4cb-181d-379b-80c5-e4693ad6e1af | -6.75524 | -45.13701 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66128789-a670-3538-aaf7-dc26b6efbc76 | -7.59919 | -42.38379 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 1603a815-dae3-3461-bd3b-7c5bab25dc00 | -7.34519 | -44.47707 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3cd4f89e-3dbe-392c-99de-2d3fd463a996 | -17.5803 | -42.27649 | 2026-10-08 16:37:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7a8e6852-ce8e-32a8-8d24-bafa23a6ea78 | -6.31761 | -35.15116 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 747d16eb-bd37-3607-908f-fb84404b5c0c | -11.00588 | -45.41847 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ee6d28f6-3b59-3f35-9831-73fe2d8f919f | -11.77651 | -45.56026 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f78ae492-9d28-3f69-b005-6562f5addf7e | -11.09139 | -44.00688 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 33dbe2e2-8ae4-3688-8b63-c47cd043632d | -12.26054 | -44.43379 | 2026-10-08 16:37:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1d16bb7c-b836-32d3-8eb2-655e37cf78cd | -10.77594 | -46.55149 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25470c2d-3c7d-3487-8c74-52c330e84185 | -8.29354 | -45.71918 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a0851489-0a07-35db-a261-f044e85ac14f | -5.82228 | -42.49051 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 97ae6ad1-4b9c-3266-829f-f619cff8b53c | -9.9815 | -39.53422 | 2026-10-08 16:37:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 619e76f8-1910-3051-b212-22b64f7281a1 | -6.93329 | -45.2578 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e3ba328d-3a45-35aa-9cf8-ce049f1df4a0 | -7.33868 | -45.2892 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 102e6af5-9a4f-30b8-bc93-aac50e069d46 | -11.77729 | -47.7402 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c9fdcbd-ffa5-30d7-923a-753714a2564c | -11.08749 | -44.02571 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f4bbb78c-f851-3e48-b5fa-6ac8e6aa7d0b | -17.90816 | -44.28611 | 2026-10-08 16:37:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a517f4b-0f47-3913-9751-970bcfb10183 | -7.87164 | -54.96442 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c939118-27c8-349e-931d-8266905cd4d3 | -8.96836 | -45.13789 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2b97cdd3-dc73-33fe-b831-f6412bb3661b | -14.51655 | -49.32989 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| cf996b2b-4427-35ec-9eb7-3f580db7033e | -7.16855 | -44.82568 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2f83c271-0688-3bca-9089-f1ec3341a69b | -7.47157 | -42.85344 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 5dfae212-b38b-3287-9570-786d534cfe58 | -9.84874 | -47.85412 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 63999515-2a06-330d-8464-aa411fad002a | -6.38988 | -42.548 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 919ca4d7-7195-3e62-9f03-678cce13c225 | -5.75048 | -41.73648 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| d04e8505-3a21-3d67-8cd5-53586d11c338 | -7.83716 | -45.50795 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 56dc3f5e-6b84-3b67-ba52-31579eef1a74 | -9.89735 | -44.80136 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a48d94db-b526-354a-a164-a904da443c7f | -10.16974 | -45.97077 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 52dae45b-b3ea-3a78-b388-4902b92b4e20 | -13.01758 | -47.20506 | 2026-10-08 16:37:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 958ed49f-8423-317b-a4bf-e3bd6fec82c3 | -6.66977 | -45.37562 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 427.2 |
| 39e78906-398a-3780-bdf6-255e2016f577 | -11.21966 | -45.26212 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 29c2933f-f3d5-3cf3-98f5-c04899014f28 | -6.4045 | -44.95207 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c69a1c90-e3f5-3b9b-bc28-cebd5a4a9f22 | -7.59268 | -46.69354 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9ed89d30-1576-3b5e-8a89-9a29869eceb0 | -10.86867 | -57.12291 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d8185000-1e23-34dc-a294-aa85b620e644 | -11.07529 | -44.01309 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 39dd291f-50da-3c5d-8a88-7fc335b29855 | -11.10693 | -43.99712 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 08b7b686-6142-3e2d-b07a-86c6a3f8b3d4 | -11.85121 | -47.30167 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 156556d9-a8df-3eb7-a6d7-ad68518abc03 | -8.3454 | -47.66612 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| db2bbc48-d092-382e-b4be-7f553a0b4d85 | -8.89125 | -45.38869 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7aa3900b-7de7-31e4-a1b1-3ad20062940f | -11.27216 | -45.20603 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dcfe3563-010b-3447-b1a5-81ad1b1b734f | -6.86085 | -41.74714 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e137bd1d-c940-397e-b857-10ca940681b9 | -11.2089 | -45.21347 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| ff9826e2-0794-359b-9278-2619a3b82bcb | -13.6159 | -43.27904 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 63.7 |
| f2b3360d-aec8-3cfd-97a7-a31eff05b0f4 | -7.00841 | -43.67407 | 2026-10-08 16:37:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7786a955-ffff-3f86-8889-76f0f00ee81a | -6.19963 | -40.80331 | 2026-10-08 16:37:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7cdd1c24-ee02-332f-b9d1-7cfc3ed777e8 | -10.59633 | -46.42193 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 88d736d3-e345-38bf-92a7-9735597cbec3 | -11.84525 | -47.35972 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6b4494b7-4bf8-3873-8c3f-3792a367d5bb | -7.61079 | -39.75176 | 2026-10-08 16:37:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 338561af-db5d-37d4-a16f-8e52788a7d29 | -19.5435 | -45.23021 | 2026-10-08 16:37:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 754fb6f3-134c-3709-8654-c4bec1cc77c2 | -9.98501 | -39.52969 | 2026-10-08 16:37:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 8b5837af-e206-3d8a-9465-f84f3e886aa3 | -14.17906 | -48.66662 | 2026-10-08 16:37:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46dfa29d-c739-3b72-9bec-806ee3be9fac | -8.2901 | -45.74102 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 0190840f-05d8-36b3-b247-9dc191fc6b4b | -13.68275 | -49.1024 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 083c1291-8534-3caa-b1f4-e407644797a8 | -7.46446 | -42.85453 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8c7ff0ba-6035-3cc6-b3cb-7471a0fc8c95 | -6.67031 | -45.37909 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 476.1 |
| 324afa01-f72d-32ed-a52d-767bfe1f3700 | -7.86389 | -40.49818 | 2026-10-08 16:37:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bea9c6bc-270e-33f1-ae67-7524b74cc51b | -18.38177 | -41.0878 | 2026-10-08 16:37:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0f3bdce5-c8e3-322e-a648-a16d0cb349e3 | -7.16803 | -47.78749 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad4d8329-6216-3b15-9a54-1a9a6f6c4b30 | -11.08528 | -44.01149 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed644756-a628-3146-a7b0-c95bea188b10 | -11.04754 | -53.99911 | 2026-10-08 16:37:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a4e1bad-0c9d-3441-8551-17ce17bddd0e | -10.84175 | -48.13781 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2383d88-bc2a-3ac2-a5f4-4bfdaa88bb99 | -12.22574 | -44.76099 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| df518895-1959-3b70-8429-129b6b049aad | -5.95433 | -43.87906 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47ba1736-5554-31f8-ba5e-703d613381ec | -12.04564 | -43.43853 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dab7a5c3-d616-3c75-bf7f-5b6dd6f862ff | -9.84168 | -47.85515 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6e633d38-33f5-37da-bdc9-d92e93f34518 | -5.51588 | -37.4859 | 2026-10-08 16:37:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 51a44a5e-9b18-3472-9c93-87e266316b2c | -8.30903 | -45.7097 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b000e8eb-c245-347d-b30b-545f3f2c52d6 | -5.70645 | -41.73358 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| a41e040f-6077-3845-b122-3202666f92e7 | -8.93427 | -45.18272 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c9704a6d-c117-3b47-9268-524a18b14a91 | -13.12558 | -46.35855 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README338.md)
