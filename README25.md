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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7595865-5874-3657-af55-16ab644bb942 | -8.16713 | -45.49159 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a8a3581-1fcd-3467-ab26-08a35ebc80d8 | -11.36112 | -42.28834 | 2025-10-31 04:08:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9cbd6103-97a9-3d57-bc0a-a9482e761448 | -13.32457 | -47.45686 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93ae013f-6f86-3e25-85a5-4bf4a0b90344 | -7.61672 | -46.47198 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a3fc7a2-65a9-339b-965b-180c690eb0b9 | -13.88617 | -47.33921 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e83d7b4-b5da-37ae-b8a0-87390889d5ca | -9.52615 | -47.27356 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f55fadd0-7f98-3bd4-a6e5-a4ef605bd7ff | -7.30166 | -45.65469 | 2025-10-31 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5c4c590-46d6-36f7-a2d9-4f99a78ef41a | -8.1513 | -44.79654 | 2025-10-31 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d897e593-a2e8-3b8d-8d8c-a8dc18d243c3 | -8.16787 | -45.48716 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25cf2f4f-a0d5-3d0c-9a76-6e326b1daf43 | -11.02654 | -44.64455 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1200fb75-0c0e-39f4-95d3-07ac219f4092 | -14.07374 | -44.01231 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a69f7b28-b1ec-381d-bf93-d9a719c31647 | -13.59728 | -47.34718 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f404cee-2968-386e-a86c-40d5689e16cd | -14.51216 | -43.92771 | 2025-10-31 04:08:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 845b10ea-0c73-3e9a-82f8-3f79d9ecf7f5 | -13.81349 | -47.06321 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31143ffa-91a7-359a-b8d6-115c16e06da2 | -8.10568 | -45.16148 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 868381cd-3b26-3476-8347-ffdc45483212 | -12.82514 | -43.49006 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e8059c6-cec3-37c1-83fb-64fb2c5ae29f | -9.50196 | -47.26924 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89995a24-6cc2-3181-99c3-6b58a16e2277 | -7.66858 | -43.58906 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f7bed308-6a93-3825-a977-00f85f145502 | -12.6011 | -47.53242 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af946191-1264-3361-912c-eff4f98a5073 | -9.73266 | -48.02314 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2545ef98-03bc-3aea-85f0-235823af5223 | -8.10137 | -46.75531 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 699babc1-0228-3429-923b-cb1b18ab8ff4 | -9.88094 | -44.86289 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9a085556-0086-39f9-9c55-4f16efe3042b | -7.88252 | -45.68729 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 809c2f05-f6c9-3290-a2d9-8f23f32b75ca | -11.79215 | -44.59835 | 2025-10-31 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4661e61-4f97-3382-840e-5aba5d291a7b | -9.93062 | -44.91212 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fd9f20d-e1d7-3d20-8ded-1f50246aca5e | -12.49817 | -43.95599 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa44603f-94bd-3929-a838-405347702304 | -10.88795 | -47.44843 | 2025-10-31 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7508ac47-7bf1-350e-928b-4136d5a60964 | -8.16122 | -45.50434 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 717e000b-9949-3fb0-9e57-904e954386fa | -8.06785 | -45.14199 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c2ead37-8475-30a1-9747-ed44988e1d2e | -7.65435 | -43.59042 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| af7f51aa-19af-3db4-a98e-d565d75a7483 | -13.00061 | -43.22129 | 2025-10-31 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a3263267-fd25-3165-b9a8-e982404c510e | -13.04704 | -43.37746 | 2025-10-31 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18b1ff37-528b-38b4-9de0-6e70d3ab59df | -12.098 | -47.13814 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 793d3cbf-c8c7-380d-b22a-8d387ba173c1 | -13.62412 | -47.58692 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46c6d4bc-11fd-3a0a-b466-5e417bdc8133 | -11.50816 | -44.00085 | 2025-10-31 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5de9fe49-cc9c-3d11-b422-2c30c21a64a7 | -12.93799 | -47.92871 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e4e6677-2afe-3b07-a787-6dcbd34a846f | -10.50375 | -42.40437 | 2025-10-31 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 5a150432-5cff-3d4c-9ec1-715fa146b6d7 | -8.33449 | -45.38456 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4fbae62-dae0-3beb-9f65-21fb20dcdaaa | -9.83615 | -44.1556 | 2025-10-31 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42b939a7-fbbc-32f2-9d77-a5d990b44bb8 | -13.83075 | -47.05906 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80f89543-9169-3c20-aef1-12bd0a178d47 | -8.08743 | -45.1365 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4a94419-86f2-384b-b988-71c510bc8e6b | -10.24667 | -44.60365 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c111b614-6fd9-3d69-82af-e55d44b85a1f | -9.52212 | -47.27283 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 063cb994-4049-37d1-85b1-2b85319ee175 | -13.85196 | -43.55127 | 2025-10-31 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b3a84da-00e8-3e5d-ac5d-48cf7e632034 | -11.50645 | -43.25818 | 2025-10-31 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4b7cd3-a5c5-399d-8e17-62f3026ae818 | -7.62129 | -43.61989 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb03e758-e9fa-3608-bd81-8c6669ebda56 | -12.52925 | -47.55068 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f714ab81-889b-3aba-a650-ba41f42b71d7 | -9.31676 | -43.09324 | 2025-10-31 04:08:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21824717-c475-37d0-9eea-beffa6150dae | -7.907 | -43.17394 | 2025-10-31 04:08:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad7ba938-e048-3a2a-8c20-116d4a490442 | -8.05144 | -49.63919 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a0af739-b14f-3416-80de-de0784db9f36 | -8.0504 | -49.63474 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66db4528-a49b-3ffc-ba5d-03dcf77006f9 | -12.43924 | -43.92411 | 2025-10-31 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b147d40-3dfb-3ae2-9838-c957acadb14c | -8.10195 | -46.75182 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbfb249f-a494-3cf2-8e85-966bbea31299 | -9.51871 | -47.26849 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a34f52b1-f665-3f26-803e-cba0adba22d5 | -14.00101 | -44.0184 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bad54fd-00fb-36f0-a6eb-1ee42a229731 | -8.10287 | -45.17847 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfaa854e-83af-31f6-82d1-d93dc96f9b36 | -12.84067 | -43.47809 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 039586ec-9085-3f18-b85a-c54c3a682311 | -10.63944 | -52.18602 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97a80491-9151-32f7-998c-149c62501a79 | -12.23871 | -47.25158 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2ea8ed5-b4f1-32fe-9e33-2ffa020236a8 | -12.02755 | -44.80865 | 2025-10-31 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f21854ef-e863-326e-8aed-1c4814130f9d | -8.09177 | -45.13281 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a56f9c2f-6aae-39df-ba43-e478e8c25803 | -10.88682 | -44.31887 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 869e7ce7-5731-30df-aa35-3328514d9fe5 | -12.05235 | -43.5408 | 2025-10-31 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8242f977-60d4-3db0-b38b-1c8e515b65fb | -12.84123 | -43.47455 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 372429cc-3cdc-35eb-9db0-0ff69a91fb6b | -9.52335 | -47.26559 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f23667f9-e2c8-391c-b772-49e321b2e8b8 | -14.73601 | -42.81184 | 2025-10-31 04:08:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 325b1192-d312-3cf5-9584-e3aebfa341ca | -8.09035 | -45.14139 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cdb35cb-0033-346c-be0e-80915865ab3e | -10.8822 | -44.32577 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e89d8406-a1b6-3d5f-bc84-5133f31866da | -9.2209 | -45.57978 | 2025-10-31 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d5492a3-a4f7-3d91-aed5-dd853406159a | -9.86139 | -44.87191 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44723cb6-d9c1-3ba4-97ea-97deffa2bfd2 | -9.65637 | -44.54893 | 2025-10-31 04:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04f99902-a60a-3686-9d97-64ac073c2b73 | -14.21067 | -43.17397 | 2025-10-31 04:08:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c9f1b736-b079-3233-bac2-a696e2b6679e | -9.86556 | -44.8685 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df80294-48ae-33e3-b9bc-d49e97448371 | -11.71564 | -44.14721 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fe214f7-973a-3c64-a7e6-eaf51749806c | -14.08056 | -44.16115 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02578cbd-ec40-3d57-ab40-4857b4ddf464 | -6.21598 | -52.00427 | 2025-10-31 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce66237-46df-3279-94e1-3a0e70c23fb6 | -11.72021 | -43.91674 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0af236a6-a9cf-3c2d-9767-98eef9f8f853 | -13.05004 | -41.16409 | 2025-10-31 04:08:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b20fdf0-a1f0-3b0f-b0cb-906439be52d6 | -13.81638 | -43.28363 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d261f3d-4b88-37fc-9c83-f817e246ee3d | -7.96613 | -43.78624 | 2025-10-31 04:08:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9adb98c1-4280-37d4-b27a-793a8061f9eb | -13.61594 | -43.98329 | 2025-10-31 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c71d4f8-7035-3ce2-9685-bf28adc3b7a8 | -7.76577 | -46.47271 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8312d3f-f9b7-3099-a881-a820d63393f0 | -12.80193 | -43.4862 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b285940-af16-39e4-b414-8ae6c4cefd5e | -13.81032 | -47.06562 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e824f6a1-4a6e-3b92-a655-4ba7a7c7b103 | -7.65715 | -43.59468 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 86c7cb05-12dc-36d7-a220-577cf3f1c224 | -12.15339 | -48.01026 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 68ec4946-5502-37e6-bbda-0345f3b6a346 | -13.79481 | -47.05983 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 592de96d-2dc9-3ad7-94df-0fd808e75a03 | -7.74046 | -46.74381 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e34649d4-9182-30d7-99d2-0ab18856f4ac | -8.31777 | -45.37568 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8959dd99-1439-3b2b-8719-c42155feeae0 | -11.01173 | -43.87779 | 2025-10-31 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31105870-7424-3494-ba76-ed170aad1365 | -7.62008 | -43.62735 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8809c10-ab35-3337-99e2-be55c1bf3fa1 | -7.81475 | -46.39769 | 2025-10-31 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1a1cf3c8-3001-35f1-adaa-ec9d767499c3 | -7.66736 | -43.59652 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e600573-b200-30bd-8b04-3223915497c5 | -12.84406 | -43.45684 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b6e513d-ced8-3e77-a80a-3ba89b9bc006 | -7.65593 | -43.60215 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 23f0b971-8a80-3ce1-b174-b3367b9b8cf0 | -10.88634 | -44.36496 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6f54694-def0-3ef1-8289-f68ad7a25f23 | -7.91649 | -46.79209 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89519c42-a628-384a-bbed-3f51735bc378 | -9.72772 | -48.02575 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc4197ae-e9c8-3a60-9baf-4a2313c6660d | -7.64719 | -43.58946 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1f9bca4f-fc73-3539-b097-3f79c1107abf | -8.09628 | -45.1731 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README26.md)
