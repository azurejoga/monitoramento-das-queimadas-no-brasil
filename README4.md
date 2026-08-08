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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e627ae03-6301-375b-a315-53b48a27a572 | -10.45603 | -37.14644 | 2026-08-08 03:04:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b6d0f2d8-30ce-354c-99e2-1e96b0cae7a3 | -10.45237 | -37.14715 | 2026-08-08 03:04:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b9a6eaed-afd6-3727-9baf-cf02294f61aa | -10.45707 | -37.14115 | 2026-08-08 03:04:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 16107765-2501-3781-948a-5325c7cfe426 | -4.2634 | -48.2016 | 2026-08-08 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 031124ff-16c4-3915-bad5-3abc9a3846ee | -18.3738 | -50.7008 | 2026-08-08 03:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 831d3dbf-cce5-33a5-a265-f853cf8d972c | -18.3538 | -50.7044 | 2026-08-08 03:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6738f7d0-f82a-3f68-a1d7-88bcad5a2abc | -18.4616 | -50.3523 | 2026-08-08 03:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| d21c0661-25f8-3c3f-9249-7647ab1911d5 | -11.0334 | -44.2696 | 2026-08-08 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 02b81b69-4c26-3a26-98d2-bfc47d52e943 | -18.4611 | -50.3746 | 2026-08-08 03:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 17184421-892b-3ccd-ab54-230c3f8323bc | -18.3733 | -50.723 | 2026-08-08 03:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ea1ca99f-882a-35fd-a656-75fc4df06952 | -18.3533 | -50.7266 | 2026-08-08 03:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d4ceca89-7342-3a1a-8c09-4a5d7a66c012 | -18.3538 | -50.7044 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c4aabd19-5444-39a4-b70f-534cee3b4123 | -4.2635 | -48.1799 | 2026-08-08 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2cf07309-cb28-3110-a96a-37982936d20e | -18.3533 | -50.7266 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 015e1afa-9bc9-3d66-a1a3-df9897ffe3a3 | -4.2634 | -48.2016 | 2026-08-08 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ad82b9c2-8c26-3d39-a8ce-4474c3db0734 | -18.4411 | -50.3783 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 101.2 |
| bb742172-1275-35ec-9cda-37723333b163 | -18.4611 | -50.3746 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 80.8 |
| 9a0000d9-fe13-3850-a3a9-269f2011073c | -18.4616 | -50.3523 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 55.0 |
| e003e27c-4438-39d6-8855-441925717ca0 | -18.4416 | -50.356 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 268b4235-8eed-3098-9fe2-b9c7c54469f9 | -18.3738 | -50.7008 | 2026-08-08 03:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4383c971-80d7-3323-bbb1-c110ab77201f | -4.2634 | -48.2016 | 2026-08-08 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a556f9ed-d7ef-3933-98c4-b3b3aa2d4286 | -18.4139 | -50.6936 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| dc251270-6df2-32a8-b64a-41666c226dee | -14.381 | -54.9679 | 2026-08-08 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 009fbea9-96c6-37ef-b4a9-2a2caf6c7fb6 | -18.3738 | -50.7008 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 2a396390-86dc-3749-911d-b80e00b5b246 | -18.4144 | -50.6714 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6334aa7a-06c2-366c-bed8-473e3a99a726 | -18.3743 | -50.6786 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 116e01e8-85c8-3214-bd0d-24671df356fd | -14.3617 | -54.9701 | 2026-08-08 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 41f56155-72de-3d60-857c-7929e66bcbb0 | -18.3533 | -50.7266 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6dc55a3e-297c-3c26-ba4e-92bc2afed67c | -14.3229 | -54.995 | 2026-08-08 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2bde682a-382f-35a3-b04f-51b43e24ffa9 | -18.3938 | -50.6972 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 681a42b4-0b91-30ba-9910-d15a69da774f | -18.3944 | -50.675 | 2026-08-08 03:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 62f5ba52-be7e-392a-b44e-16eb24c72fba | -14.3425 | -54.9722 | 2026-08-08 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 79fedab6-1a8a-3cd5-bf9d-a376be761b56 | -14.3232 | -54.9744 | 2026-08-08 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ce55e180-782d-361e-be3a-6af2a8d1c83b | -14.3422 | -54.9929 | 2026-08-08 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5942a9bd-917a-3b0d-8fcc-4f79fe7d123b | -14.9254 | -48.2523 | 2026-08-08 03:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 32c45c57-8e71-3484-8e93-dd6271be376c | -4.2634 | -48.2016 | 2026-08-08 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6600bdde-1ffd-381e-be88-74792b84d0aa | -14.3229 | -54.995 | 2026-08-08 03:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a29919be-d431-31e9-9ac8-b508823db8fc | -4.2635 | -48.1799 | 2026-08-08 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d1f22a03-b391-302a-906f-6393abe037e9 | -4.25721 | -38.03259 | 2026-08-08 03:47:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 31e32c3b-d725-3dfb-8816-ac1c450e8668 | -4.90731 | -43.47213 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd473f68-ea20-3f29-90fb-6d7551c2b9a6 | -4.64522 | -43.12801 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16edd81c-0c11-3999-85d2-b200ccc5f91c | -5.03998 | -40.71457 | 2026-08-08 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d148474d-164a-35c5-8552-d2ba8a3da7d6 | -4.26004 | -38.03677 | 2026-08-08 03:47:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 50e111da-037d-3e39-9dae-e327d756b99a | -4.26886 | -48.19795 | 2026-08-08 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 7e2327d7-ce9b-3655-9069-2c5334010b1c | -4.63918 | -43.12451 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3ae77e4-7d48-3678-b0be-b9778e67ce45 | -2.83607 | -46.72146 | 2026-08-08 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d89f320-f2ed-32c4-805b-9d4fa146969d | -4.26343 | -38.0373 | 2026-08-08 03:47:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2483836f-8f8e-393e-966d-894c2a5d5080 | -4.64071 | -43.12729 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69d6f2d5-743a-3771-8dd5-e0e188eb8243 | -5.03939 | -40.71198 | 2026-08-08 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c63024a9-d5da-311d-a170-5d234bc3ad02 | -3.96776 | -48.11931 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ccfad9f-0893-3bbb-9f80-61444c672362 | -2.49196 | -47.08503 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12ebafa3-8ffe-3420-9df4-2f2e714bb9b8 | -5.04073 | -40.70986 | 2026-08-08 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 320905f1-a4f0-3598-9942-b4ff88e14ec4 | -4.26253 | -48.19687 | 2026-08-08 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| a77cef43-66d2-303c-8670-6376ef3191af | -2.48591 | -47.08387 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e1f3019e-0d40-3630-a86f-5d1969349e98 | -2.69851 | -47.3614 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28ac54cc-46fb-35b7-a6d9-ce2c673489e5 | -4.89151 | -37.50203 | 2026-08-08 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dc632cb6-b955-377c-991b-493ef9fffc9f | -2.4866 | -47.0864 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b438d065-c4a1-3377-9bfb-962081aed2ac | -2.76054 | -49.47252 | 2026-08-08 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68a48371-c328-3e2f-bc01-b5f54a7b98e3 | -2.83017 | -46.72044 | 2026-08-08 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 347d9da3-6f01-37c9-a53c-58e9581d2071 | -4.65398 | -42.43581 | 2026-08-08 03:47:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f14aca3-b88e-361b-9a52-02fa5771a6e4 | -4.59666 | -44.58009 | 2026-08-08 03:47:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9525a034-f70b-3627-9f90-2ef3e80ab8fe | -4.26061 | -38.03312 | 2026-08-08 03:47:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| c4bae9d1-b718-3e72-8f0b-63f71bb5f339 | -4.64148 | -43.12277 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e95bc34e-9be5-34c6-b6d9-a46a3132bfae | -4.33717 | -39.36206 | 2026-08-08 03:47:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1cf6c4e0-5c4f-3f74-adf4-852a1a45d5df | -2.82945 | -46.72478 | 2026-08-08 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20dd4201-1db8-3a6b-b5ea-31eced618851 | -3.05384 | -39.93092 | 2026-08-08 03:47:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b0d9126-f86e-31c9-a54e-7fdf0a11125a | -4.264 | -38.03365 | 2026-08-08 03:47:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| f42b72fe-b249-3f4e-b56c-fc6b27ad49f0 | -4.59617 | -44.58302 | 2026-08-08 03:47:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db27c64d-8dbd-34a6-984a-c9cd4bc55d11 | -4.46116 | -47.92083 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 342308ae-d025-3424-aab6-e8a919dc18ba | -2.48664 | -47.07937 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6669e90-fc89-3e9c-b177-2a684a2bc026 | -3.90196 | -40.377 | 2026-08-08 03:47:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 381b62e3-9609-38d6-80cf-a0375bb000c1 | -2.49266 | -47.08749 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87953ef6-9e07-32e4-bfaa-ce49f70ef49e | -2.69234 | -47.36039 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c5c0f2-160c-31a3-aeca-895f21d1f9a5 | -3.9541 | -48.12288 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 873d7a3e-0cef-3710-8205-da13bb0f4c17 | -5.07392 | -37.61767 | 2026-08-08 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9777b9d2-d597-341c-8309-67c948e0b268 | -3.05009 | -39.93035 | 2026-08-08 03:47:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a21b2596-8722-365d-becf-fa2469ab857c | -4.26342 | -48.19176 | 2026-08-08 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 04a8b831-6c79-3011-b67c-c7f17fa71a8d | -4.64819 | -43.12598 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| def6a185-a81d-379c-8b13-eb9b74a00aef | -2.75355 | -49.47137 | 2026-08-08 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a2a780f-9d6b-3257-8fe0-be96ae761143 | -4.64369 | -43.12524 | 2026-08-08 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22b08a10-0ec8-3817-a029-f732abce1fb4 | -5.27252 | -45.16838 | 2026-08-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21a4d36b-a512-3456-a648-4527628c7d12 | -4.88817 | -37.50151 | 2026-08-08 03:47:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b3e18dfd-c7ee-3fcb-a280-03307d69c134 | -5.42703 | -43.43308 | 2026-08-08 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3f10c63-7c8e-3719-a843-5928f3c5a74a | -4.4567 | -47.91799 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c27b0533-2f37-3224-aab9-9eeae4f0b29d | -3.9605 | -48.12357 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| aa51cf9b-686f-3db0-8607-370ea5931535 | -4.26975 | -48.19286 | 2026-08-08 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 8a49f97d-5d28-3fb4-bb35-c98af837109a | -4.38313 | -43.36564 | 2026-08-08 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9ebdade-681e-3b13-9a9e-b7da21a12bdf | -2.76867 | -49.467 | 2026-08-08 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db1c3a39-76a5-35f2-9caa-de968e566ec9 | -4.46291 | -47.91903 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2477f2f6-ad88-3236-bfa2-be02bbc8e8ad | -4.38329 | -43.36676 | 2026-08-08 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c8b624f-f7b1-3266-8feb-bcf71a4a1929 | -4.3676 | -47.77649 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 63287288-6c29-314e-8587-82c5f6137f3e | -4.36926 | -47.76683 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 610d0cc2-822f-3550-82b6-c1addba12172 | -2.48737 | -47.08189 | 2026-08-08 03:47:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b413e0f-d8da-38b6-b3ec-d59484501d88 | -4.27063 | -48.18781 | 2026-08-08 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 648d1b6d-6d1d-3bed-8164-660d6ed8c45c | -2.8783 | -40.29987 | 2026-08-08 03:47:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f2ef16fe-1157-3e45-b9b3-513abc4b99a9 | -2.42185 | -48.63739 | 2026-08-08 03:47:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2004368-f79a-3ee2-9f01-f0c52f712b98 | -3.96688 | -48.12441 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f91449eb-9cc4-3063-9f8f-39e83ffa15b5 | -4.46203 | -47.91597 | 2026-08-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6544a6a4-4e5c-3ec6-ab8f-d13e56aeb200 | -4.37869 | -43.36602 | 2026-08-08 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d06cba1a-0e2f-39d5-87be-c50b1a4e93be | -5.42779 | -43.42849 | 2026-08-08 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README5.md)
