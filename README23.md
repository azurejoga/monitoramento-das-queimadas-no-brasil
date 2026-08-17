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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6f11a48-8e7d-3464-bac7-cb7c6c3f3e0c | -15.45613 | -53.04188 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f44e9c5-54ae-34e7-b427-a55133a67aed | -20.89351 | -50.50295 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d7e066fb-249e-3522-b708-6e0d88149efa | -16.72052 | -49.12978 | 2026-08-17 04:23:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcf3629b-bc25-3a6f-915d-30c6363b742d | -14.09963 | -58.43427 | 2026-08-17 04:23:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eddc773f-0ba8-3ace-ab45-e542a28f028d | -15.92123 | -55.53774 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6a26471-1e70-303a-82e5-31017974e44f | -15.83094 | -54.20895 | 2026-08-17 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c5d8505-9a0f-3cf9-91ef-d1b93b54d3d1 | -19.85436 | -46.3822 | 2026-08-17 04:23:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5dd59a5d-4733-321a-86d5-759b2e3791fb | -15.02298 | -52.72161 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0a197e7-ce40-325e-a9d3-8850a6de03bd | -15.46041 | -53.04262 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 013a4f67-c84a-364c-a3fa-224ec98ad660 | -16.67074 | -49.44942 | 2026-08-17 04:23:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2fd263a-1d53-3eb5-bc1f-215132ac4da6 | -17.53315 | -49.21218 | 2026-08-17 04:23:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 48ae6219-ec72-3385-b57b-1247f040191e | -15.91929 | -56.4794 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61fa2da-30b8-37e8-b61f-fab2c9038b3c | -16.2247 | -49.70209 | 2026-08-17 04:23:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb73c56b-23a3-3998-ad80-6490768e3df9 | -15.93647 | -47.8429 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48c86a53-fb08-302c-9f1d-4740429c08dc | -20.32175 | -46.72906 | 2026-08-17 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7beac03-2fa8-38d0-a8c6-cdd550669b78 | -15.94428 | -47.83681 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e3dac9d-3dcb-3c41-b8a8-f1258456a5c4 | -16.22403 | -49.70614 | 2026-08-17 04:23:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 389453bc-ab01-30bc-ac52-971fe5d65854 | -14.08923 | -58.45313 | 2026-08-17 04:23:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| faa83dfa-c591-304d-b73e-81ba855eed44 | -16.29151 | -53.17482 | 2026-08-17 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 721a0f36-7adb-3943-9162-155dcb033e23 | -16.29855 | -53.17911 | 2026-08-17 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03d05c23-1a01-3cd6-a705-d14ddf814f33 | -15.86481 | -56.34608 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46dd7593-487c-333c-a3b5-60eee4bdda38 | -16.20089 | -57.63614 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5b915338-0be4-3fbe-9393-2054d476fe9a | -15.90439 | -55.51796 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2ab2a028-c238-38f0-aef6-b1f1b85ebebb | -18.80767 | -46.73488 | 2026-08-17 04:23:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5b868b44-7d94-3075-9a95-25a74ea40af1 | -15.94919 | -47.84882 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68ba366a-1908-34ea-9ff1-305bec5f94ec | -15.90111 | -55.5346 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 885e7e7c-129f-3ddc-83d0-659782e13f6a | -14.49814 | -59.32541 | 2026-08-17 04:23:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81f52a8b-161f-3a70-aac1-c0dbccadb6ca | -15.90542 | -55.53907 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d0fa7099-ffd5-3819-8c25-80845f0f4a98 | -16.23246 | -57.65475 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 24466e17-163b-34d9-948b-327fac60b973 | -15.90929 | -55.51936 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3ece3c7-ff75-3ee2-a1fa-17cf3b298e92 | -21.27821 | -45.61826 | 2026-08-17 04:23:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c55b86fb-0e1f-3b42-adb4-40e5e3e79a6e | -18.17923 | -42.33708 | 2026-08-17 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f310c454-37cb-3d16-a4f7-174159141536 | -16.41505 | -49.63068 | 2026-08-17 04:23:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5c8148bd-c6b4-3978-bb96-f2f8e32ff06f | -20.89696 | -50.50362 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff7b8048-6bd6-33ac-9ae5-dd26ac120f97 | -18.6453 | -48.22206 | 2026-08-17 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 62977ed3-43bc-3d06-9071-9e624f6211e1 | -16.81823 | -49.0713 | 2026-08-17 04:23:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0af0780a-c222-3efd-ac80-012e60aa7ec5 | -15.82029 | -55.52419 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f60ba9cf-335f-3966-8b47-bf3be838340b | -16.75817 | -49.36695 | 2026-08-17 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92ec6f41-3415-3841-b162-96e975aabe60 | -16.41437 | -49.63472 | 2026-08-17 04:23:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c067bc4f-654b-3c72-96c9-6d62c9002756 | -17.32586 | -54.93415 | 2026-08-17 04:23:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 613b435d-ca4c-3ee5-a7d8-4fb5c9ff11a7 | -16.2282 | -49.70275 | 2026-08-17 04:23:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59959309-e5b5-3f7b-8d20-6b6ea92d48b3 | -16.21795 | -57.63937 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6357c8a4-2518-3217-b685-8da372676496 | -15.41536 | -53.03145 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 006061cc-76c6-3509-9b94-cca7be07a0dd | -15.81968 | -55.52729 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7b438f7a-fb48-3128-b9a6-0c28d98926db | -16.21712 | -57.64333 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| de579cf4-db60-34ba-b6ed-580603ea84b3 | -16.29622 | -53.19147 | 2026-08-17 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7534de62-02dd-355e-b38f-6cf6a973f7c6 | -15.92918 | -56.48507 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 102dfedd-f97e-3759-9195-aff46a42cce2 | -16.29775 | -53.18336 | 2026-08-17 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d22b9cb-8d76-3b25-b316-fad99fa11ab0 | -16.22752 | -49.70683 | 2026-08-17 04:23:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d0cc7bc-9589-347d-845b-b8eea0897f14 | -19.08187 | -44.41695 | 2026-08-17 04:23:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d277a67-ffa5-3dcd-91c8-be9d5c122742 | -18.17876 | -42.34068 | 2026-08-17 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81e48d2c-5c31-3906-a20a-ea4bf9d3d807 | -15.91087 | -55.53773 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 41dad3c6-c62e-3819-9040-8008955d493c | -14.49724 | -59.32907 | 2026-08-17 04:23:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a062ce8-8eaa-3760-bb26-2a14536360be | -16.22675 | -57.65382 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6bc8bf97-db4c-35f9-be37-f4b373651f5d | -15.63455 | -48.895 | 2026-08-17 04:23:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c6801a5-6e7c-3be4-a366-9a18171c30e2 | -16.71963 | -49.36923 | 2026-08-17 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eb92d75-158a-3fd6-9df3-5a7b29b76ba6 | -15.94703 | -47.84101 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 790cc889-7bb5-3577-859a-8390918a8d1a | -18.5801 | -46.9159 | 2026-08-17 04:23:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7293b6f1-3399-3532-ab97-58fb3b2b24aa | -16.92729 | -54.14999 | 2026-08-17 04:23:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86d53217-a6da-3b18-be66-02abceab96d0 | -15.81586 | -48.171 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f7d2767-3bbf-34f4-be28-259425bce78c | -15.47567 | -52.8688 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 807512dc-955c-3de5-91b0-1fb394400523 | -17.5329 | -49.21206 | 2026-08-17 04:23:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2c64c199-2552-3b50-80ac-4365c9b215a4 | -18.46666 | -49.72783 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aa840b03-acd5-331a-b838-51e825504faf | -15.15906 | -52.83376 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df600b95-ee22-3d03-856d-510f6b476bb7 | -16.22767 | -57.64938 | 2026-08-17 04:23:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9ffd25b0-c718-3025-9e29-b37d3e7f273c | -15.81646 | -48.16731 | 2026-08-17 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bcef449-4c26-31b3-81e2-8f0542cf25f0 | -15.90058 | -55.53732 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c2f2f48f-5da7-3459-9bb4-68c039fc9508 | -15.90275 | -55.52633 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 5ad1b322-f213-3958-9693-0fad05cc0907 | -18.4516 | -49.73314 | 2026-08-17 04:23:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ba1fd8d-518d-3f6c-84b3-e3308dc2ec3f | -15.47486 | -52.87166 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ef8f961-93b4-31ad-8571-0b4e02dd277c | -15.02223 | -52.72573 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2f0e0f0-a878-31bd-89c9-ed860920efe1 | -15.92986 | -56.4817 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba1c1151-dc81-392f-95dd-cffb0628ccad | -15.92458 | -56.48054 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a5cfe8a-e655-38e5-946a-2b7168f41bd7 | -15.92389 | -56.48392 | 2026-08-17 04:23:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 402a4c1b-0425-38ca-8bb7-0e8dbba4412e | -14.09028 | -58.44811 | 2026-08-17 04:23:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c49dfe03-c556-32ff-9668-b43766045078 | -16.75472 | -49.36637 | 2026-08-17 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6d380c0-4f90-3571-88b2-7b0f4bd0278c | -14.68701 | -57.19746 | 2026-08-17 04:23:00 | NOAA-21 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b28701a4-d6a1-34f7-9c93-06af0306a057 | -15.81467 | -55.5264 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6716d7f-20d9-3857-9b76-9efda3ba8129 | -15.81916 | -54.19599 | 2026-08-17 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d677a394-34d0-3438-9360-ccba09e6086b | -15.81408 | -55.52943 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c3a8d9d-7a1d-3ed4-a8e8-76f1927fafb3 | -19.02063 | -47.05676 | 2026-08-17 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3802529-5016-3ccf-aca3-970c80ee8f34 | -14.49694 | -59.33085 | 2026-08-17 04:23:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cdc3806-0c14-399d-b0a1-ceffa397d4c7 | -19.27899 | -44.97028 | 2026-08-17 04:23:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 295a7ca6-e8d7-35c6-b27d-6d22153362f4 | -15.90651 | -55.53352 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c741e428-7a11-3b19-b5f5-c74630020010 | -16.41157 | -49.63003 | 2026-08-17 04:23:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 209db799-756c-362d-9e12-ea961b406495 | -15.91521 | -55.54203 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50299f67-8664-39cd-99ab-77a7b3ecf09e | -15.82003 | -54.21634 | 2026-08-17 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d145e825-f928-3d5a-8e56-1b6657f08ece | -14.20846 | -60.20746 | 2026-08-17 04:23:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 019c3d5c-78a0-3bb4-91e8-2d88283841fa | -17.33051 | -54.9352 | 2026-08-17 04:23:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ed1b23c8-8657-3333-ac20-f39de7c1ed2e | -19.27841 | -44.97445 | 2026-08-17 04:23:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d3d58bb-1083-3eb0-9017-7be8cc1b71be | -15.90597 | -55.53627 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 88ac04c1-ba6b-3fee-aed6-149d43a5cf20 | -14.49839 | -59.32363 | 2026-08-17 04:23:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31b1e49a-1a23-38fb-9064-f0ad12e14941 | -15.90819 | -55.525 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee4bfaf1-cce4-34ff-9fa6-f4ae3aa41b59 | -16.60511 | -52.59843 | 2026-08-17 04:23:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 687d981b-ba56-32ed-b189-808186701fd1 | -17.35439 | -45.6235 | 2026-08-17 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a064dbd-572b-32ab-9d85-6bdc9a8fdbae | -15.15958 | -52.83479 | 2026-08-17 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b9f47f6-4c23-3648-b692-b1c2d20112ce | -15.90975 | -55.54345 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 32ffcae0-760b-32e8-b04b-fdfbe683e619 | -16.64572 | -49.26456 | 2026-08-17 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc09a705-a2a9-3fcc-91ff-96ad8e36abc4 | -15.91143 | -55.53489 | 2026-08-17 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecc661f0-0b8c-3434-95ea-0d64fc421a34 | -16.18171 | -46.80503 | 2026-08-17 04:23:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)
