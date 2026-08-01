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
| a78f03fd-369c-31c2-8b8d-f2114de764ac | -14.06232 | -46.2399 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| f2716d32-445d-3e01-b6e9-4fa827b94a4d | -14.05541 | -46.27615 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 93ad2094-2168-3fac-99fe-a07b66d80f75 | -14.0646 | -46.28289 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| a409bca6-7f23-3162-b83f-cb917ffbbafb | -14.07154 | -46.24768 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 6ee5602c-cfae-3290-bf0b-5f7223114a33 | -14.08068 | -46.28565 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 66c3d1f5-0eaa-3d11-be5c-1f0ffd11bb24 | -14.07812 | -46.24389 | 2026-08-01 05:53:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a027ad4e-ee1a-39c6-aec4-b302ca42392b | -17.42151 | -42.62591 | 2026-08-01 05:55:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e48a2f19-9caf-36c8-b529-2e3a9438c864 | -17.41873 | -42.64173 | 2026-08-01 05:55:00 | AQUA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c5bf9fab-1884-3758-b56d-5b122dbbd627 | -17.43284 | -42.61864 | 2026-08-01 05:55:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 113d1f35-0729-34bd-81bf-f7276a2c6002 | -17.43004 | -42.64395 | 2026-08-01 05:55:00 | AQUA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7a37b14a-15dd-300e-9801-8f2305809be9 | -17.43281 | -42.62803 | 2026-08-01 05:55:00 | AQUA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 95987e35-2622-3a89-a482-2008f75e5c41 | -17.42996 | -42.63445 | 2026-08-01 05:55:00 | AQUA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f1e22aa8-3910-35c9-a50d-077b790cbf1a | 4.42036 | -60.97954 | 2026-08-01 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ff9b7b1-a525-3f75-be80-1ba0c9636e4e | 4.41656 | -60.98439 | 2026-08-01 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 044089f3-84a6-3a87-9a81-d981252c2708 | 4.4158 | -60.97981 | 2026-08-01 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b94e623d-4086-379a-a358-279e376a0459 | 1.09702 | -60.51662 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68105567-34d8-3490-a22c-6c292f15a5b0 | 1.10279 | -60.52134 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b870c18-51d4-3bf0-9ab4-9cffd64fb404 | 1.10103 | -60.51036 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5b7c98c-8827-3c2f-b33f-6ba71db25197 | 1.09525 | -60.50564 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e771e607-d009-3810-a238-cdebcfb1e81a | 1.0979 | -60.52209 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 236209ce-0c63-3385-9c4e-02d173432cd4 | 1.32114 | -60.71578 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbf4bde4-148e-37a0-bd4e-8fb2cff94957 | 1.09614 | -60.51113 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85c1a9b2-dc63-36c1-b3d2-f892531e0c65 | 1.09436 | -60.50011 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2f5a145-d8d1-3ca8-8965-c706f96c0444 | 1.10191 | -60.51586 | 2026-08-01 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd14c23d-9509-34cb-b06b-ea0b710f572e | -14.0725 | -46.2899 | 2026-08-01 06:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 75850499-b075-37cb-b9c7-1fad9a0f7ccd | -17.4239 | -42.6386 | 2026-08-01 06:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 35670640-cdb9-345e-96f0-30fba224374e | -14.073 | -46.2669 | 2026-08-01 06:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 529c9329-daaa-3dd8-8d7b-0f32bd072832 | -14.0536 | -46.2702 | 2026-08-01 06:00:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 57566e54-57ec-3853-bd8b-4f6cf7442ad7 | -10.07478 | -60.50195 | 2026-08-01 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f56bf982-957f-3349-8a6f-1964061ce2cc | -9.08394 | -65.37485 | 2026-08-01 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61063c30-dac3-3a5c-b4bf-40b95954e961 | -10.28179 | -69.10805 | 2026-08-01 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9157d4b6-9008-3827-a3e9-265fa2b099ad | -9.08341 | -65.37856 | 2026-08-01 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7e35f3b-3965-3585-a30b-959b2b54bdb5 | -10.05541 | -68.542 | 2026-08-01 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f937c710-30c5-3db4-8b84-c81b1767ebb5 | -8.89889 | -72.70621 | 2026-08-01 06:01:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 316f2703-7db0-3ff1-8630-2b5e6f10765b | -10.08087 | -60.50447 | 2026-08-01 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91d812c9-25dd-3062-b038-1807a7d62527 | -10.07509 | -60.5036 | 2026-08-01 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96151ce9-53b8-3e17-9832-29e74fe3f044 | -14.073 | -46.2669 | 2026-08-01 06:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4b16e8a3-98d9-3099-99d5-b550915a918e | -14.0536 | -46.2702 | 2026-08-01 06:10:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| df2ff219-c0df-33c4-acab-fea01d2215c1 | -17.4239 | -42.6386 | 2026-08-01 06:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 1d34a238-f763-3998-a2e2-3b3288c104c4 | -17.4246 | -42.6137 | 2026-08-01 06:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 1a3beeaf-3e36-3854-97fe-9383f59b1aab | -14.0725 | -46.2899 | 2026-08-01 06:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 5a6bd89f-7ee3-386b-aacc-b353073f0ec5 | -14.073 | -46.2669 | 2026-08-01 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 02aa78ec-0637-3f85-a639-3fb6af8ab3fd | -14.0735 | -46.2439 | 2026-08-01 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 1aaa207d-45d5-3e94-85af-e682b6352491 | -14.0725 | -46.2899 | 2026-08-01 06:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 73099cd3-2b65-30b9-ae63-fc14bc93270a | -14.0725 | -46.2899 | 2026-08-01 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e628c696-a344-336c-a0d7-74b0a3ba5720 | -14.0735 | -46.2439 | 2026-08-01 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 15bab7a1-371e-32b2-967e-340447583929 | -14.073 | -46.2669 | 2026-08-01 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 581327cc-1f08-3339-8e15-e0f4e75bee92 | -8.89696 | -72.70435 | 2026-08-01 06:37:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 202013d6-dadd-325e-b9b1-5f64034c4301 | -14.073 | -46.2669 | 2026-08-01 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 279796ba-3193-3c3d-bcbc-adb2f51053d8 | -17.4239 | -42.6386 | 2026-08-01 06:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| bcfb3624-30d0-3ce8-bbb0-c2a977e42643 | -17.4447 | -42.6088 | 2026-08-01 06:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3fc7590f-d1b3-316a-9840-2d563537b120 | -14.073 | -46.2669 | 2026-08-01 06:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ced5d437-7816-3422-ba06-21198946c961 | -17.444 | -42.6337 | 2026-08-01 06:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b73e9273-b583-3043-b3e6-51d3d3148938 | -17.4246 | -42.6137 | 2026-08-01 06:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 98f875aa-15dc-3516-9c06-dd7d30155d11 | -17.444 | -42.6337 | 2026-08-01 07:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 66c40b4a-621d-3c83-b311-5ad8e68a850a | -14.073 | -46.2669 | 2026-08-01 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ea4dbb11-ee35-37e1-8253-8d030e70a3bf | -17.4239 | -42.6386 | 2026-08-01 07:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 116.9 |
| d847838f-ff03-3173-ab23-fcb627736b50 | -17.4246 | -42.6137 | 2026-08-01 07:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6eab9f5f-4864-39e1-b5e5-ee4a408221d3 | -17.4447 | -42.6088 | 2026-08-01 07:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 78a55a5f-1ca9-3cfe-80f8-8acef3f17bf3 | -14.0735 | -46.2439 | 2026-08-01 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 49a1b443-1da9-3728-8acd-30a4fda70439 | -14.0925 | -46.2637 | 2026-08-01 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| a0017229-a027-3857-b80c-8d8423803d12 | -14.0536 | -46.2702 | 2026-08-01 07:10:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9eccd396-0a01-39dc-ad47-6bcb99e74b32 | -17.4246 | -42.6137 | 2026-08-01 07:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 043b44f8-9d51-3e2b-84b5-face26eb0920 | -17.4239 | -42.6386 | 2026-08-01 07:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3354194a-096c-31fb-8ec7-289c75deeb22 | -17.444 | -42.6337 | 2026-08-01 07:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1bc2930a-542a-3ea2-a263-d1deee157fb2 | -14.073 | -46.2669 | 2026-08-01 07:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 127.3 |
| f9b09da0-b48a-3ff0-9ed9-3a5252f9a386 | -14.0735 | -46.2439 | 2026-08-01 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b6807050-00fa-3f47-bb9f-5a4f9e25e383 | -14.0536 | -46.2702 | 2026-08-01 07:20:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6cac7cf9-bbe2-3473-acd8-3845415a31e6 | -14.073 | -46.2669 | 2026-08-01 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 34ac2515-f689-3544-908c-ca464d15e4c9 | -17.4246 | -42.6137 | 2026-08-01 07:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 09ca610e-e10e-33b0-94cf-a3aa33b1b202 | -17.4239 | -42.6386 | 2026-08-01 07:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 86339d4b-c387-31e4-96de-68f271ecfbc7 | -17.444 | -42.6337 | 2026-08-01 07:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ba99a3e4-0697-3d60-a59b-e25d2940d729 | 1.0994 | -60.52241 | 2026-08-01 07:26:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 821c25fa-4f9a-34aa-b6fa-d881f0105242 | 1.09784 | -60.51205 | 2026-08-01 07:26:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3d4bec1e-e426-32bf-b0ad-42f38f3d31fb | -6.55959 | -55.15652 | 2026-08-01 07:29:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 2854bcb8-ef32-3444-b828-5a2faac7aadc | -11.24046 | -54.84794 | 2026-08-01 07:29:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9bf047b6-a408-3f56-90e7-0d01fd60dfa2 | -11.25256 | -54.84937 | 2026-08-01 07:29:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| b9ca0668-6237-36f5-9c52-c20a7faa3c3a | -11.25026 | -54.86703 | 2026-08-01 07:29:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4553f11f-0a85-3b06-bd88-7fe8731a08c7 | -17.4239 | -42.6386 | 2026-08-01 07:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 1ac7b052-d49d-389b-85b7-61d08646e7e7 | -14.073 | -46.2669 | 2026-08-01 07:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6a997565-d558-31bd-bd35-c7890ec86e41 | -14.0735 | -46.2439 | 2026-08-01 07:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ecb4ec99-6cf6-37e1-ba36-f123aab0d57f | -14.073 | -46.2669 | 2026-08-01 07:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7447de46-beff-3bfd-9ea8-e8326a28d2fb | -14.073 | -46.2669 | 2026-08-01 07:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d2e3828e-78ca-32a7-b51b-e6c235905db8 | -14.0735 | -46.2439 | 2026-08-01 07:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 39ce2b73-3287-3fec-839b-f3bbeacfc956 | -17.4239 | -42.6386 | 2026-08-01 07:50:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1c74d927-ba7c-3335-8ec5-1a452220e89b | -17.4239 | -42.6386 | 2026-08-01 08:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c24cdbe6-ccfe-3b0a-b521-9f0543c9e8f5 | -14.073 | -46.2669 | 2026-08-01 08:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a48b1028-ba29-3339-961b-fbdbace18f5d | -14.0925 | -46.2637 | 2026-08-01 08:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| fc45f6c0-fa0e-3c08-ae03-22121474f7be | -14.073 | -46.2669 | 2026-08-01 08:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a549216a-a60d-3595-8419-ef9c224ddaff | -14.073 | -46.2669 | 2026-08-01 08:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 4d4f02e5-6995-3764-9ed4-fda957dbc18b | -17.4239 | -42.6386 | 2026-08-01 08:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 0ff00d2b-e518-3329-ae5f-e339c0b7335b | -14.073 | -46.2669 | 2026-08-01 08:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8f4611b0-805e-3023-bfc4-f9fecd24335e | -14.073 | -46.2669 | 2026-08-01 08:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cd592f5b-4a93-35b5-a990-8ab3d99a264c | -10.4731 | -48.4901 | 2026-08-01 11:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| a5aae259-6b79-3080-952c-836181201bf7 | -13.35018 | -48.66236 | 2026-08-01 12:19:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 2f99f9c5-f67a-3f22-8fec-411b48c8139f | -11.37999 | -50.10814 | 2026-08-01 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e18e25a9-d0b9-392d-bd78-4600a682bd96 | -14.09255 | -46.24509 | 2026-08-01 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e491b93a-afc1-3c30-835b-bf4e72c4eb30 | -14.21889 | -57.39986 | 2026-08-01 12:19:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a47f908b-77e3-3e44-91f2-f9e9c9932174 | -13.53024 | -51.51478 | 2026-08-01 12:19:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ff3e746e-7610-3e6b-84d4-5547f593f6e3 | -13.34312 | -48.65498 | 2026-08-01 12:19:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |


[Clique aqui para ver as próximas entradas](README26.md)
