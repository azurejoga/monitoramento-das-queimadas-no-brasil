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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 620e9828-1aa2-32b5-bc29-829596c2e6df | -3.39036 | -50.44298 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52fb0604-8631-3340-bb80-cf7320026773 | -3.44725 | -50.59998 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e729169-6aca-3405-9eda-0a56caa63e5e | -7.51428 | -46.22492 | 2026-09-21 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59e6d0b2-c5e3-32b9-a68a-86dc093bf9c0 | -5.84076 | -53.48936 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26746468-d4d0-3656-974a-bbf3d94f0708 | -6.73196 | -55.07737 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30ef0307-7208-3f4d-bb01-f762851d76e1 | -5.82196 | -55.70287 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19682da8-b615-38ec-aa80-a20b1debbc40 | -5.86023 | -57.54982 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fdedef0d-8549-3655-8d54-2aa38230cfe2 | -2.87303 | -57.81281 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0139d989-10c4-383e-a660-accf5cd7eea1 | -6.73916 | -55.0749 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| feb88721-80ae-30e6-a970-5d8c3c18252a | -3.71764 | -60.55108 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6c69eb6-77f1-3494-91b5-fccea964e891 | -3.4813 | -59.59569 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c733dd85-d0cf-3274-92fe-368addd50191 | -5.84887 | -53.50632 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 573aa900-8111-39a8-8374-5c31fe9f0f24 | -3.50648 | -59.93405 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b93aa391-a2e6-3870-a1fa-68cc6506017e | -6.73529 | -55.0779 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d2c4e1-2d4a-34c9-af34-58553b84b583 | -6.41892 | -57.87483 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8adb91c-a0a1-36a3-b65a-de1ee9a3fb63 | -3.14867 | -58.63994 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80c93636-ca5c-354d-8c03-4585c7534a0b | -7.41102 | -44.77455 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 14c4532d-39e3-3c81-9771-57ba30bcec6f | -6.40069 | -55.26243 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a1489fc-8f0e-3527-8bc0-203869411b44 | -4.61601 | -55.75655 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df4a72e9-599e-3716-adfd-43669de2169f | -3.33375 | -58.13398 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ae94e00-0a13-3728-a0ec-59980f74e326 | -5.8896 | -52.04813 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d57187b3-2e2f-36a7-9ff1-38c232396cf6 | -6.18016 | -57.76553 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ef3c06f-20b2-3677-9e66-8e721f9e8867 | -3.23517 | -60.8003 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c5690ba-47f6-3b02-9614-7c9eb383ad5d | -6.93111 | -55.6159 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b2f8bc4-85d6-31ad-be74-4338de5d91db | -1.20532 | -54.22268 | 2026-09-21 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e60a45c-4b18-3866-8506-3f6107b8146f | -3.06008 | -61.27041 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 972659d8-0172-302d-994c-2465eaae088f | -6.49498 | -58.38211 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6786865-bbb8-330c-885f-cc441653cfbf | -7.4295 | -44.77769 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfcf1899-2b18-3d53-8757-be5fae2fcf6b | -5.01278 | -56.09432 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 98d15401-df10-3f35-b4b4-031e431bd4a0 | -6.92148 | -55.6102 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a61a9133-43d3-3a71-a135-a534c40fc98f | -1.54215 | -48.65163 | 2026-09-21 05:04:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f1f93fd-3bd5-3f63-b371-1039590715fb | -5.21088 | -56.10815 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b920ba8e-6556-3f46-b370-c735f13dc4f6 | -7.42144 | -44.79141 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a8295f0-4039-3a04-98f1-cc9ef74f39b4 | -7.82218 | -45.26697 | 2026-09-21 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8b30d0b-49f7-365b-9550-4fe04878b28e | 0.789 | -59.20137 | 2026-09-21 05:04:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce58272f-dac4-3c30-bb12-51b673c52580 | -6.06966 | -53.37721 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c23c552c-164a-3a21-b81d-54b2b95f209e | -2.25075 | -56.6524 | 2026-09-21 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81d4d21d-0654-3c55-af2b-febbcadd2e65 | -3.48667 | -59.61113 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18be33a9-aa69-3bb4-9fd0-f8932d349f15 | -2.99993 | -54.1664 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ce4a0a7-a907-3990-a6ff-f02971ef3596 | -5.8302 | -52.05072 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06eafd43-592b-3839-b1c0-8e06bf6d17da | -7.31841 | -46.7696 | 2026-09-21 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1568261a-adf5-3da6-a9b3-83c4d1159ca9 | -6.73593 | -55.0959 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f10ee10-ffb0-34d0-a2fe-fc0f805fd6d7 | -4.68365 | -46.41433 | 2026-09-21 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e00b7e40-7a01-32e1-985a-1f0e5062b2ef | -4.49803 | -55.51225 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9174c006-e8e1-3bbe-a0a8-4743fe08a834 | -5.83327 | -53.51572 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a74736e-5686-3ffe-b4c8-ba707214cf66 | -3.05942 | -61.27452 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1e11b0d-2d21-36e0-b41c-9720f2de2be4 | -3.82487 | -58.89082 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66ecba82-cfd3-3704-9b73-9679637928be | -6.47366 | -48.44771 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f806687-5b4a-303a-b61d-2799e8c8b62d | -6.34173 | -55.29248 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b82fa698-e3df-3fb5-b146-d096fba80324 | -3.06308 | -61.27932 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 758be0d0-f3a0-328b-9a9b-77f2a77d442f | -6.02791 | -55.34299 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3845c3f0-3e39-38ee-a66c-b12d9c8d3bf1 | -4.49571 | -55.48373 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 726ad108-f67d-3d71-84f3-058b64f5b60e | -6.73251 | -55.07383 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4576c445-ff00-3be4-80df-404bc4ceaec2 | -3.45365 | -50.61135 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d9748fc-104c-3acd-b63b-30e34b0817f7 | -4.26346 | -55.77152 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93ee4ba7-77bf-38c7-8b48-1ba5a5ad8f8f | -4.35098 | -55.49655 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9065bb5f-f665-3331-9484-f9f614ab5be1 | -6.668 | -50.89075 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32887a95-24aa-3e79-8fb8-b609599c9036 | -3.78736 | -55.87972 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 193cf00e-82d7-3058-8281-1297620a6cf3 | -2.87532 | -57.82121 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ada5c20-8da6-33c4-bd6c-2b95ac0e2904 | -6.03843 | -53.27638 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ccf3c67-73ba-31f5-a96c-5acc2ec2e4c4 | -5.85293 | -53.52658 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 141920f3-3cd4-3587-bde7-bf43b58ed21d | -3.00081 | -60.80193 | 2026-09-21 05:04:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af1b4a1d-b899-3a41-b788-a00bea3d0bd9 | -5.96966 | -57.78529 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b270570-a793-3aca-9ea3-f0b618a95327 | -5.89225 | -52.28324 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b3fc0f9-a56f-36a6-93de-1df0053c7ae1 | -5.20372 | -56.11058 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eeb90c71-e5ae-31c5-ad20-f6093f3319b1 | -7.12911 | -48.41679 | 2026-09-21 05:04:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3bd65a5-9213-3d92-9473-290a4593b113 | -3.6666 | -54.27277 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18f14b3-404c-3760-9bfe-eb6ad6aa27cc | -2.97787 | -54.76698 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4df553c-45e9-3be1-8450-d679e923892d | -5.84196 | -53.52881 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec4e9dbf-0e02-3890-9e43-c3e836bcb641 | -6.31478 | -60.01503 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd39ecbc-a108-31c2-8016-53df2b4d9512 | -3.73364 | -59.40614 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5485169a-8c4b-320d-b303-77f17e09f834 | -3.90255 | -60.59587 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ace745d-0da2-3cb8-9e15-831f13647d83 | -6.72315 | -55.09033 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ddf8d76-b06c-3b17-b520-45a8d68e6808 | -6.92094 | -55.61367 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eb03ed2-28f3-3482-900f-476a962f0cff | -6.61673 | -50.06342 | 2026-09-21 05:04:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 658eefde-2f79-3cfe-9a35-e99ca6436130 | -6.29658 | -59.95988 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e698889-d106-35dc-8499-5a5c19a55e4b | -3.62723 | -54.52804 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9af3f38d-3496-362c-a957-6dbfd53e25ae | -6.19004 | -55.46083 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b965045-5000-39fb-ac5f-5e24d3e407bc | -6.12176 | -57.75589 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73c8ec15-190a-3763-b71b-609f9c20b887 | -3.39112 | -59.5789 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30017572-ce69-346b-98ce-11b7b6586982 | -6.20564 | -57.78091 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2632ca51-6ac8-32d7-8225-60d344d6a5a9 | -5.21034 | -56.11161 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39db6504-868a-37e2-a66d-67cf737050d0 | -5.76966 | -57.45691 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1094f8a5-9a44-3ea0-9db0-1b2504e59ace | -2.85793 | -57.63486 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d7b88a8-339b-313c-8909-2c572143571e | -7.34013 | -44.47028 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48f6d785-34bb-33b2-856b-7abd2ca34bc7 | -3.44238 | -50.60828 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb86632a-31fe-3ae3-9570-8a9451c9fc4d | -3.3858 | -61.29489 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51662490-4fef-31d3-8a79-70ec0ed528b3 | -3.60582 | -54.05018 | 2026-09-21 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6dc5204-1691-3133-af02-b03c41bea94c | -6.1262 | -59.95723 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39941dba-e58a-3a72-84ea-8c02ce88e565 | -6.33494 | -60.01119 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcbf711d-6af0-3304-af0b-6a7add509a2c | -4.01383 | -53.49324 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c284a6f9-09fc-3aa6-93bc-272481eca0d4 | -5.81994 | -53.51802 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645483e9-efcb-35e3-bc1b-21733cec24f2 | -7.72583 | -49.3825 | 2026-09-21 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 431e18e4-bd5b-3e6d-86d5-1dfff28da5c0 | -5.85837 | -49.8031 | 2026-09-21 05:04:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bcc88703-7577-3a76-b404-fb0d9417759e | -3.64463 | -58.86927 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 501a462c-d3cb-38c3-bc4a-0af18e0a6234 | -5.83061 | -52.07307 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9a9b909-fae0-30c1-a055-da106cfe5248 | -5.84659 | -53.54522 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36f6c80c-82f7-3bf6-b32c-1f16c71012d6 | -6.11724 | -55.68603 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15582777-972a-3d21-abcf-523af2200a28 | -3.06876 | -59.16888 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16268315-44e7-3a7e-a5d6-f3785d7aec6e | -6.36097 | -43.36585 | 2026-09-21 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |


[Clique aqui para ver as próximas entradas](README62.md)
