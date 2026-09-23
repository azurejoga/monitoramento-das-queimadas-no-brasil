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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 500fd4c5-b389-3be6-bd0c-951740f47057 | -11.87748 | -45.7709 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d4ad07b7-b45e-3a43-90f2-4c3ca5eaa57d | -10.44222 | -45.10015 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ae945d2-c378-31e4-8498-5682166ca641 | -10.71009 | -48.71847 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7a601a2b-1b02-3c40-b538-db816f12f762 | -10.00433 | -45.19914 | 2026-09-23 03:45:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 731c7432-5962-34aa-aa80-7bbd4c1a9d9a | -9.70816 | -37.27415 | 2026-09-23 03:45:00 | NOAA-20 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05df6c40-3a50-3bc2-a323-c0b7af2cdef0 | -10.70458 | -48.70951 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 683ac803-3d3e-3e17-ab14-2bc08fb99d61 | -15.1673 | -43.56195 | 2026-09-23 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea3bebd5-ccd1-3a7e-87da-cc4dccf80b86 | -10.70636 | -48.73701 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 05c8d699-ecfa-3d22-93a2-66b83b614bfb | -14.6066 | -45.6512 | 2026-09-23 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c778417b-2e2e-3171-b8be-7723b833cf44 | -11.52797 | -45.35065 | 2026-09-23 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a34ed35-0421-3653-85ee-b35bcbc8d0ef | -11.79393 | -42.63189 | 2026-09-23 03:45:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d1d8806-6be3-3951-a8d8-816d7b6e0e3a | -11.26398 | -43.41776 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3951b17-229a-3e52-8591-534ba548e2ab | -11.65739 | -43.46407 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fbc5b89-00a3-3104-855b-fe2d94085ddc | -8.59493 | -44.53873 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7fe3ea4-eea4-3819-af12-cb40e6652a5d | -10.54195 | -43.97672 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 387fd550-50c9-374e-86bb-f63647464ce7 | -8.76494 | -45.83775 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f9dc875-161e-3a76-8f23-a5c7820aa103 | -9.86045 | -48.40107 | 2026-09-23 03:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f626235c-39da-31f4-93ee-1eeee820ce80 | -8.90816 | -45.95085 | 2026-09-23 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 413f8e72-5e14-3310-90e4-9c31824b318d | -12.12019 | -45.63586 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 38ab910f-5c90-36b6-a905-4c687ced4db3 | -11.34865 | -43.37774 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6903b4b2-505f-303b-8522-650f5588d3e2 | -11.12787 | -42.79205 | 2026-09-23 03:45:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2fb8879c-5545-3f2d-85af-72986aedc3e9 | -12.42145 | -46.97654 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25518cf0-9bda-3411-b946-9e94c5b140db | -10.45596 | -44.94663 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c28b39f3-9b2e-309a-8590-0ea00acad939 | -10.54321 | -43.97785 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47fa0c62-8b76-3d77-94c7-82582b0f1f6f | -10.44867 | -45.10427 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1cd40af-c76b-334b-afaf-c2f87eefdb2c | -11.87582 | -45.77931 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9d1b06d1-8386-392f-bfdc-74cba5676c72 | -13.30097 | -47.88706 | 2026-09-23 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf528818-2a95-369c-8b02-705a6a95d910 | -15.74025 | -41.89012 | 2026-09-23 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fa8550dc-ab83-39bc-bdb6-db4ea8256444 | -9.84004 | -46.38887 | 2026-09-23 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1c1473ed-f15e-38cc-a9c1-d6250921a614 | -10.0052 | -45.19467 | 2026-09-23 03:45:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9936432e-467c-36a5-909d-d09a059bb938 | -11.26287 | -43.42373 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbadfbaa-03fa-3dbd-b023-ee89214263bd | -13.92515 | -47.83545 | 2026-09-23 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46377706-7ee3-3ee7-97d5-ce9ee3723002 | -9.04234 | -44.99796 | 2026-09-23 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cb10e34-2c4f-30db-811b-2a470f00b0d9 | -8.8124 | -44.27578 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 10f53e98-872d-3a93-b3a2-3d459812d5b8 | -11.66018 | -43.47688 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bba2172-ebc5-38a8-8b52-544b05565336 | -11.65628 | -43.46997 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea5998e4-47fa-3b4f-a9ec-bbcc9b4a7967 | -10.5159 | -44.87876 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cf1e9d9-6893-3460-9876-7ddc06bafcd9 | -12.12491 | -47.39334 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aee9ed20-8a06-3667-838b-7277ac40c052 | -13.29977 | -47.89261 | 2026-09-23 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08eb236d-0224-3eaf-bcbf-c230d6448b27 | -10.94955 | -43.85559 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92dc3cae-43a7-3d36-89b6-957948505439 | -13.45723 | -46.27403 | 2026-09-23 03:45:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dc10711-c0b0-3002-9f46-8b73b3362606 | -10.54195 | -43.98466 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 266f4ad2-a3ef-3af0-a527-2f0e8f7220eb | -9.54358 | -45.77665 | 2026-09-23 03:45:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03cca30e-a7d9-3e9a-bcc9-414450852155 | -13.61937 | -42.44452 | 2026-09-23 03:45:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8b39e9c-f4b8-3756-8af0-6b360d9c408e | -12.41322 | -46.98506 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20efa83d-65a9-39b7-856c-a80200e164f1 | -9.86742 | -48.40266 | 2026-09-23 03:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9c38b979-7a1d-3466-a2db-56021a6f01eb | -14.96054 | -47.53899 | 2026-09-23 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cad78a6-537d-30ba-be74-55f4d075d574 | -11.43692 | -47.39847 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 828c1668-dc9c-35ac-a48c-955f6e16ca66 | -10.70409 | -48.73404 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fbad8cab-1013-31ff-a0db-b1a3e244163d | -10.53665 | -43.98364 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2ab432e-a76a-30e7-bbbf-2073acf75895 | -10.95415 | -43.85987 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebe70c21-9e40-3db4-b151-2f26ab3c45d8 | -11.4632 | -47.33521 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d8028a9-be45-3d7c-b604-177dba340e8f | -10.71305 | -48.72624 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c6df1e36-2b57-3ff5-a7e7-62898d031f50 | -11.66074 | -43.47391 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09ec575c-8d11-3f40-bf84-2d7d04f44f2b | -8.80623 | -44.27795 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 59a2095d-b30d-3804-8884-b9402caff288 | -11.47225 | -47.35651 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21abad3f-0ef7-36d7-962c-fadcf1ef6630 | -8.80141 | -44.2729 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5be9cc4-3495-3f67-8f04-1fcafcdec5d8 | -11.87084 | -45.77401 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ef4363e8-c8a2-3564-94ea-5f76c7bd21ea | -10.53791 | -43.97684 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bff22303-04ba-33e2-8aff-179389debaf6 | -11.35255 | -43.38466 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e677046a-2802-398a-8267-d7424dfacb3a | -15.16835 | -43.55915 | 2026-09-23 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b992ff00-4fa8-3c9f-bcb1-d9627001ccd9 | -11.25839 | -43.41977 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fffb8ad-4afe-3765-b86b-1cfe9babc655 | -13.35637 | -40.33518 | 2026-09-23 03:45:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e59f513d-a41f-36e4-b8b7-49bef746bb0f | -13.29968 | -47.8913 | 2026-09-23 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03d66770-3f39-373e-a9ea-3be18e69de09 | -11.35685 | -44.21434 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e5af49b-4a73-30fd-bcec-b5f66a33785d | -10.20968 | -44.161 | 2026-09-23 03:45:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fa1d7c4-94a9-3bb7-be90-9f038057e5bc | -10.45025 | -45.09615 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12717250-4f93-35d8-aecd-6c17166e4a4c | -12.38276 | -47.08067 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ce2ae08-4c12-35cb-9642-c814f22f8495 | -10.53601 | -43.97909 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9323c379-8156-3b91-a7fd-4eea56f1db39 | -9.86634 | -48.39713 | 2026-09-23 03:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 685e2e17-aa25-3be9-8a06-d6d1abbe60a3 | -7.98318 | -47.47766 | 2026-09-23 03:45:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25ff1970-9ced-32bc-879d-20b61260eaa8 | -13.85312 | -48.5781 | 2026-09-23 03:45:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18c16828-9969-3222-b6b6-5536346bac2f | -14.29467 | -43.19407 | 2026-09-23 03:45:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| e9b2aec2-561e-33fc-b1ae-1611f91e15ad | -14.75486 | -47.15598 | 2026-09-23 03:45:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a5c74ff-e805-33bb-a2c5-3932e89bd170 | -15.63338 | -43.53342 | 2026-09-23 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8be05b5d-4143-34cf-a07a-75375d8e15ab | -11.2651 | -43.41177 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94ac789a-4075-305e-b22f-391ff804f44c | -11.88411 | -45.76783 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f3decf5-f267-3ee2-9652-cb899776086a | -8.59621 | -44.54169 | 2026-09-23 03:45:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd24fc27-be3d-3129-8b90-a081d8d07ceb | -12.41014 | -46.97769 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99100159-96d7-303f-abf9-539be89569b4 | -12.121 | -45.63175 | 2026-09-23 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 9edc71ce-6af6-354d-bf52-1b349eae8945 | -10.54131 | -43.98008 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d6bf3ee-fe4c-31f7-812f-a096d0253d9e | -8.80205 | -44.26948 | 2026-09-23 03:45:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c96e4b33-e2ae-3f69-ae0e-75b4d2367b99 | -11.35757 | -43.38563 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 30fb7ed4-0ede-3e2a-90ac-465a4a2daa0d | -10.54065 | -43.98349 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f41ba70f-ae82-3468-9e08-43932d451a65 | -11.29225 | -44.04504 | 2026-09-23 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e7974547-387e-35f7-ba80-1e992867663f | -10.4479 | -45.10142 | 2026-09-23 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34f47d80-4e78-3bed-9724-0a751a828cce | -11.66408 | -43.4838 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9f83adb-d21f-352a-b790-34d23b55a509 | -12.41425 | -46.98016 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dd46f010-9918-3730-8e92-7ad26bb6a9b2 | -10.70804 | -48.72871 | 2026-09-23 03:45:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1fa13085-1711-3dc1-82f8-a54015c3c264 | -10.68514 | -37.11595 | 2026-09-23 03:45:00 | NOAA-20 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a09172d2-a67d-3045-8a98-b3f3f4e25dfc | -11.46337 | -47.36729 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ad07dd9-2100-3811-bf29-39a9af3aeaf4 | -12.41213 | -46.96782 | 2026-09-23 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 81b2ed50-8e02-32f2-b4fd-2833d087c23a | -11.47928 | -47.35486 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 844da02e-08c6-3415-affe-992fea4b5c6f | -13.9229 | -47.84603 | 2026-09-23 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46dd8931-fefd-3393-8714-bfb39802cc97 | -11.69025 | -43.45526 | 2026-09-23 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e32a609-9d98-3a01-b97b-d2baa9e49147 | -10.45128 | -46.2811 | 2026-09-23 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5103cdd-8c12-3167-a491-ef0411d934fb | -10.50837 | -44.85748 | 2026-09-23 03:45:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ce4204a-b0ee-394d-8624-cd127a8c09dc | -10.53729 | -43.98021 | 2026-09-23 03:45:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7e69c46-0ef9-309a-b70a-67b61f1e1af5 | -12.20602 | -47.28948 | 2026-09-23 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 46003752-9ae9-33fe-afec-b857dcf4cfff | -11.46857 | -47.34168 | 2026-09-23 03:45:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README46.md)
