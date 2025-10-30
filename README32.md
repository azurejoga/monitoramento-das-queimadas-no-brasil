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
| e4361e6c-41d1-33df-bbe3-0d48b012e80c | -10.74508 | -44.74579 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fd1945b-2080-3a7e-b3c1-0718d202db69 | -13.11586 | -40.22414 | 2025-10-30 04:06:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6274e18e-0d2d-375d-bfcc-f02ae580beb3 | -9.84367 | -44.88738 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20aeedef-ada9-3d73-a470-34f0893cea25 | -8.32178 | -47.93228 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ea1e060d-a0da-3b83-9944-cecd57241753 | -11.04204 | -47.84047 | 2025-10-30 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91140d20-de8f-3495-a101-2544ec6c5200 | -8.72035 | -48.00758 | 2025-10-30 04:06:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e0526d6-4f05-3b72-8493-9f44cb227050 | -12.58239 | -44.96026 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4668e7a-696a-3f5a-ba4a-366c4a944337 | -14.38886 | -43.7198 | 2025-10-30 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fed64f2f-cf96-39ba-9b38-50bb37be9806 | -12.80947 | -43.45472 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86cb15ba-6964-381a-bb24-203636555a5a | -10.35739 | -48.699 | 2025-10-30 04:06:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dfc5275-7f64-33f3-b670-ab91d62c9d27 | -12.33028 | -50.173 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed58c52-28ab-3abf-b658-026ad2208f72 | -10.47433 | -44.08378 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b330129e-f515-3a4c-8940-da858d13a264 | -8.1995 | -44.44802 | 2025-10-30 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad1a398c-ba21-330b-a9e8-fb48e061c7c4 | -9.32066 | -43.09602 | 2025-10-30 04:06:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2824d15f-f8dd-3f93-8a6d-975b1d5b65c4 | -13.13306 | -42.50511 | 2025-10-30 04:06:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 831e424f-0705-3d11-8340-41fe4d39dbe3 | -12.87912 | -48.64227 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ce26169-29d4-37e0-a83e-dd41bb09247c | -8.78977 | -42.82837 | 2025-10-30 04:06:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 653e73c7-bde3-391a-ae19-f7b55e85bb29 | -14.28782 | -42.33612 | 2025-10-30 04:06:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9290a8c7-f9ef-30a3-bf34-86bd5a869264 | -13.60014 | -42.50872 | 2025-10-30 04:06:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 418bdd73-af81-3b74-b47b-971b7de8e107 | -10.74147 | -44.74714 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b34136a4-565f-3a3e-a0de-b7d17c49b6f6 | -9.81452 | -47.586 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e02c258c-8593-3493-9e0e-aba7522dec8a | -13.75274 | -46.92527 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0294bc83-f99a-329a-8006-d256f1fff57c | -10.27763 | -44.58511 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1df5e9c3-f365-3b01-99eb-9bc9cf8cc11e | -12.48631 | -50.57211 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b81d207c-871e-3740-8e5c-505507098e4a | -9.85365 | -44.87458 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa5e11c2-55ad-3752-9f86-8dda04b82c19 | -10.33741 | -47.0912 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b373292-64b0-345b-b538-602480735f80 | -10.65168 | -39.93229 | 2025-10-30 04:06:00 | NPP-375D | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3123b0e-d80e-3f3a-80d3-31d948c36f1e | -13.4256 | -47.36363 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 756a009e-29f7-3d3d-a11a-27a1fad8b051 | -13.57101 | -47.32625 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70a57350-7dcb-34bf-80f3-08181a872e4d | -10.74881 | -44.74647 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e0f8992-9ae2-332b-8b90-0be94f02d62e | -11.06313 | -47.54304 | 2025-10-30 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4721cf5f-00e8-35f1-8dd5-1a57ad7ec6d8 | -9.84985 | -44.87389 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb25f414-159c-3346-8aa8-d50e660d698d | -13.25205 | -47.04925 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d93dd29c-581a-37c1-af37-0a2cccc04004 | -10.62062 | -44.1248 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14b00477-31af-3318-ba3a-d1b75193d3cb | -9.90561 | -44.90493 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6efbbd4-a31e-3ece-a5c2-6b4e5cb30349 | -10.74223 | -44.74276 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04e63ec1-71b9-31f1-bc42-a977ab50f9cb | -10.75407 | -44.73794 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18b30463-5eb0-3aae-bc68-c0956e8b2c23 | -10.35392 | -47.27542 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66d74250-f3d2-3e26-932b-36290f12173f | -14.28449 | -42.33554 | 2025-10-30 04:06:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a92b98b-a624-32bb-826b-1595f71839a9 | -13.42984 | -47.36417 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 247c33d8-f315-3a00-b353-df3f41d290d5 | -14.7126 | -42.4472 | 2025-10-30 04:06:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cab9cea7-ab1d-3026-8052-a525a1c69877 | -12.29083 | -50.32343 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a977a1e2-af35-32fa-b07e-6227718ee096 | -12.91559 | -45.04529 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b0483ee-2417-3ff4-afad-0d386df3edc3 | -11.00684 | -47.77738 | 2025-10-30 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10a3c8bb-00c6-35f3-a616-e20c0b9d1917 | -13.59356 | -42.29376 | 2025-10-30 04:06:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0eabe1ea-124f-38f5-bc13-259f0e0e6ea2 | -9.8852 | -47.45279 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ea4facd2-2b63-30fb-a894-d8e031301c7b | -9.2247 | -45.6006 | 2025-10-30 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bbbf612-bb93-35b0-ad57-fe6f78c21562 | -11.55244 | -44.68887 | 2025-10-30 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9665ec43-fa6d-3477-9958-26802122a9f3 | -11.54951 | -44.68384 | 2025-10-30 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec2897dd-9222-3025-9d68-3adde008d169 | -13.58151 | -47.33982 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47c2fa99-8332-385d-bb6c-1817b95dfbea | -12.6069 | -43.20327 | 2025-10-30 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e33d741b-930d-30ff-8433-4234a1107f53 | -14.03359 | -42.2938 | 2025-10-30 04:06:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3b31257-3805-31ec-af50-cee603e68a6a | -13.53755 | -47.12752 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb6b95b8-1fe2-3528-8c67-4e93884dc854 | -8.69887 | -47.90902 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c14fae7-5e92-35b4-93e0-162375103961 | -14.86132 | -41.55183 | 2025-10-30 04:06:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cdc45e7a-cf64-3a63-ba13-c88d6d91a35e | -13.92674 | -42.37172 | 2025-10-30 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43103453-2c8d-3129-afb8-5aa15d4701da | -13.41497 | -43.74468 | 2025-10-30 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7e503c8-b668-3a3d-af43-b5f571b4b5d6 | -10.67634 | -48.04428 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72882261-6608-3894-90b0-be3d80553062 | -12.68803 | -46.30421 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edccb300-9eb1-32a1-b82e-7e8df0152419 | -12.88105 | -48.63208 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2313e60b-9953-34e8-b124-09e9af2ba51a | -12.88373 | -48.64317 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a623af06-4b4a-3041-bc66-7643737d496b | -13.27685 | -47.7473 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe05f1e6-684d-3045-9abe-52c226572907 | -13.64368 | -48.42952 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0142e111-4e1d-3247-b359-604d6115ed89 | -10.38841 | -37.45065 | 2025-10-30 04:06:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2ac50f13-8adc-3bb7-bff7-d0c490aa6fb7 | -13.3184 | -47.474 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8e72eae-d57d-3878-8e78-2ad397768007 | -13.5292 | -47.1265 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad7e0050-051b-3c83-8b59-96cce9d5b20d | -12.70673 | -46.29122 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 03a20dbd-90cc-3e85-93ef-d45383a3f5b6 | -8.43206 | -48.70027 | 2025-10-30 04:06:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 423b505a-6921-396f-82ef-28341db2d567 | -13.33222 | -47.44647 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f49ff55-92ff-3ac5-ad90-0328f44f4473 | -10.58411 | -40.51003 | 2025-10-30 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 99ed5a79-f990-345b-bbaf-3bc732ba2266 | -11.36289 | -42.25703 | 2025-10-30 04:06:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fa6d8f0c-96e9-3475-8575-d79d4a762e9d | -12.49285 | -50.56656 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92966e57-47e4-3c04-8732-6fad802c96d5 | -9.88601 | -47.4483 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed9ed307-5310-3731-aef3-542e9af15135 | -12.51517 | -50.56426 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5eac3383-fabf-3f2c-8217-92f52ae46e62 | -13.27333 | -47.71808 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46bd57d1-4e6a-33d6-b834-669866f62979 | -8.32561 | -47.93846 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8fe0c3c-24e0-36fc-9163-06fe0a475da6 | -14.12967 | -44.06894 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 397310ee-7b4d-3752-9dee-acf88c641c2d | -9.84748 | -44.88807 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 825a1350-b2de-3ba3-80c9-f54c990f71ad | -12.31889 | -48.0661 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d417d95f-23ce-3fd1-b23d-dfbec7eed72e | -13.4415 | -47.37169 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cdf2349-1f85-399e-bfcf-dfb6ebf18a3f | -12.68804 | -46.32735 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4adc3f69-86bb-36bf-933c-bc95ce181a72 | -10.74968 | -44.74413 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f62dc869-f04b-35f0-b3b4-5b1fda56bda0 | -12.47659 | -50.59431 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e29ff503-2db8-3810-8aab-464243ef798b | -9.84603 | -47.69752 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fb9fc4c-7311-310c-aa9a-706aafcc5a0e | -12.62036 | -44.25435 | 2025-10-30 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ad57cf-16f3-33db-86a2-42222b3beb92 | -12.90943 | -43.19206 | 2025-10-30 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dcd3fc2f-d694-3ded-a6db-60442aa5ffb2 | -11.96129 | -43.28355 | 2025-10-30 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c61f7316-9eca-305a-8d31-1725cef49f1e | -10.75421 | -44.74016 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c1df550-07be-34d4-bee7-bac2a11910e0 | -12.88707 | -43.11518 | 2025-10-30 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87a69605-258a-3103-a8b9-496766651a13 | -12.83483 | -43.45124 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61ab2052-f903-3650-96c5-916805ea7559 | -7.95259 | -46.74347 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 068cb7c0-a122-392e-8042-fab040a0ee92 | -9.0934 | -47.78563 | 2025-10-30 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c80fb459-ba75-3b68-b164-6060b6701338 | -11.06917 | -47.53489 | 2025-10-30 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25eb6d70-0005-3a53-9b6e-c71715f7c136 | -11.17885 | -43.15083 | 2025-10-30 04:06:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69b1bc57-1006-381b-bbee-ae012b45f767 | -13.40379 | -48.3794 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cd98699-2baf-31ac-a82c-bdbe4ff7e5b6 | -13.74551 | -48.39038 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50399106-615b-3c65-8d03-d4942dcf2503 | -10.28212 | -44.58128 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d75fe5b7-ef28-3d9e-9b52-28d3d06f2413 | -10.88876 | -47.59137 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96cf6acb-83c2-3edc-b537-ff4bed4e0f72 | -13.59746 | -42.29075 | 2025-10-30 04:06:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a9259f00-7e25-37b0-9c3b-1ecd370d3c53 | -10.75795 | -44.74078 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
