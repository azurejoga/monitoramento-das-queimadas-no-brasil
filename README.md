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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c44d556-f497-3b55-a21b-b1016675aba4 | -11.8702 | -44.5656 | 2026-09-26 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0883f31c-d57b-3bd6-9788-f01eb17d5e09 | -3.2728 | -50.1372 | 2026-09-26 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| cd5e6dd3-8529-3ead-ad12-b1857174c60b | -11.851 | -44.5685 | 2026-09-26 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| ff721979-1a22-3067-b81f-20435d28abb5 | -3.2727 | -50.1583 | 2026-09-26 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e9d3d3ac-5849-396c-abe2-8d353ee0bb61 | -11.5298 | -43.2546 | 2026-09-26 00:00:00 | GOES-19 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 8c075836-dd49-3253-833d-c0b836e2a4a8 | -5.7569 | -45.084 | 2026-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 62889dc3-a3dc-370e-81f9-de9be493bcaa | -16.5732 | -43.9798 | 2026-09-26 00:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8a27944b-e189-3f1a-9f3a-ee4645806a8e | -5.7754 | -45.1053 | 2026-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 457c2133-6bca-36c2-b3cd-694ffd610436 | -5.7571 | -45.0613 | 2026-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 91fe2ee6-3b30-39b2-81a4-8866a5d3d559 | -3.984 | -48.4297 | 2026-09-26 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c5af1f3f-3370-3a1a-9a9b-0ea8ff3ea6d7 | -5.6754 | -45.8784 | 2026-09-26 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e86fa5e0-3190-30b8-bd71-1755b162f924 | -11.8698 | -44.589 | 2026-09-26 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b31dbf06-347c-31e1-9abe-91ea79bf4efa | -11.9365 | -38.2942 | 2026-09-26 00:00:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| c53b1447-7171-3b5a-b3d1-f51f50e350b8 | -4.2673 | -44.5866 | 2026-09-26 00:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b5e91578-bb0b-3c49-86f5-060877d49e01 | -3.8723 | -52.2769 | 2026-09-26 00:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f083d5b9-8266-3be9-a369-de313610767d | -11.8505 | -44.5919 | 2026-09-26 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 4808f944-a912-3e87-929f-7267b0aa2886 | -5.7756 | -45.0826 | 2026-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 25d6583c-bb14-3aa3-ae76-728a3bddb132 | -5.7384 | -45.0626 | 2026-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 25ebadd8-6dd0-3be8-9353-c593c1d24530 | -5.6756 | -45.856 | 2026-09-26 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 16e050e2-7378-3d4d-b969-ca5fd1cc508e | -5.7382 | -45.0853 | 2026-09-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b6723d45-2a07-3340-b122-42fdf1f54d86 | -5.6756 | -45.856 | 2026-09-26 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 91306a92-fb30-3e4f-ac3e-3b0cda47b5f8 | -5.7384 | -45.0626 | 2026-09-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 7aa69901-ce90-3e67-a432-b53c52621f0c | -11.8505 | -44.5919 | 2026-09-26 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 57823415-8d28-390a-922b-405e19dbc255 | -1.3459 | -55.4721 | 2026-09-26 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 95f71469-8135-3bf6-8179-caa1eaf34a68 | -5.7756 | -45.0826 | 2026-09-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 73625b6d-3914-3177-b895-95ada97077ac | -11.8698 | -44.589 | 2026-09-26 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 438b9801-284f-352c-bed8-cd435f3f4520 | -12.2636 | -50.7248 | 2026-09-26 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b9dba25a-dc07-3680-a5aa-842d51becf95 | -3.2728 | -50.1372 | 2026-09-26 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 2ce98bdd-1d1e-3f69-a3f3-8b2aeb59234c | -11.9365 | -38.2942 | 2026-09-26 00:10:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.9 |
| f6cf2dfa-4583-3910-8d7b-fdfd15bdf231 | -5.6941 | -45.8771 | 2026-09-26 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| fd7df16f-7426-35f7-94a1-0b61c83028c6 | -5.6943 | -45.8547 | 2026-09-26 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e5e37ffc-56b7-3a56-861d-1fe398fa6e5a | -5.6754 | -45.8784 | 2026-09-26 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 713e9352-d09b-34fb-99eb-d827db2b2850 | -5.7754 | -45.1053 | 2026-09-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 17e68d43-c8bb-387e-b56f-aabfc6a0333a | -11.5298 | -43.2546 | 2026-09-26 00:10:00 | GOES-19 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 513a3985-bd42-39fb-af2d-90af34af47c4 | -11.851 | -44.5685 | 2026-09-26 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d6c4be4e-9bc6-3702-9afa-3108febd902a | -20.42392 | -47.47235 | 2026-09-26 00:16:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5224407b-bcd8-3c7a-b9a5-12d02c2f9c85 | -20.34546 | -47.49265 | 2026-09-26 00:16:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e42721a6-da4b-3b7f-b170-57cdd036b1ce | -20.92161 | -49.09448 | 2026-09-26 00:16:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 596a4695-5169-3b89-ad78-371e00d6c72e | -21.11159 | -45.66109 | 2026-09-26 00:16:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 43a4467c-972b-3e16-8248-3fa58fa4d37d | -22.01714 | -49.57913 | 2026-09-26 00:16:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 3d4382e4-b674-39a3-8b8d-2fa654dde293 | -20.43207 | -47.45744 | 2026-09-26 00:16:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 12e90d27-f57b-3cc2-88ac-0f03aa42ef28 | -20.92004 | -49.08401 | 2026-09-26 00:16:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cf7f734d-75d3-3b79-8a67-809f14141308 | -20.42182 | -47.45947 | 2026-09-26 00:16:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 4e23a10b-fe64-37e4-bdc8-62ffd4cc02ff | -15.42208 | -47.89619 | 2026-09-26 00:18:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 267af9fc-bcca-3bb1-930d-46bd8c9ec53f | -16.75917 | -47.24874 | 2026-09-26 00:18:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5d3fd912-79f6-3a6a-b38b-b5317bfd64c5 | -17.13153 | -50.29123 | 2026-09-26 00:18:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 010ef62f-a944-358f-a660-5215ef08991a | -14.79893 | -45.96662 | 2026-09-26 00:18:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 28bad8f7-b5af-304a-90bf-4310fbc1a2af | -17.13298 | -50.3012 | 2026-09-26 00:18:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7894ef2-07f4-3072-8def-17a8ad397858 | -12.89642 | -52.06856 | 2026-09-26 00:18:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| abb069bd-c637-3456-8332-46674ee3dfc6 | -16.76129 | -47.25756 | 2026-09-26 00:18:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| dffbe9e4-449f-3ba1-b375-9a5eb3ffb2cf | -14.96236 | -47.54947 | 2026-09-26 00:18:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6ef14ea4-a45a-3b40-a490-019ffa984f12 | -19.91316 | -48.25625 | 2026-09-26 00:18:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 57077e0a-4428-318d-b635-a836c8d1af40 | -12.70475 | -47.29967 | 2026-09-26 00:18:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3da23533-8c83-3881-9d2b-7f5447bfa6ce | -16.76159 | -47.26391 | 2026-09-26 00:18:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| c4cfc998-f682-3e14-a681-cc7d626aeb34 | -14.33257 | -52.72449 | 2026-09-26 00:18:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| db0e64b6-fe4b-3a7f-bd0e-223fefdd82ba | -15.72923 | -50.79621 | 2026-09-26 00:18:00 | TERRA_M-M | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8fe76d16-ce16-3ee2-adae-7714942bf5e4 | -13.33277 | -51.32016 | 2026-09-26 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f5677a3e-4e98-3160-939e-44bebddd89f4 | -14.95965 | -47.53226 | 2026-09-26 00:18:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 52911f79-beb0-3cfb-8614-59194b718cff | -12.34483 | -48.20074 | 2026-09-26 00:18:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 87124aac-b195-323e-9008-b14ce2ec8c88 | -19.90333 | -48.25812 | 2026-09-26 00:18:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 3e3638e9-0d32-3abc-a419-2b719132f57a | -15.20162 | -49.29892 | 2026-09-26 00:18:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 10ee28f6-6a9a-3adb-a01b-b23bc9e86cc7 | -18.5416 | -50.66899 | 2026-09-26 00:18:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 57c369bd-a2b2-3aac-996d-c29012018ffe | -16.57243 | -53.07741 | 2026-09-26 00:18:00 | TERRA_M-M | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77d48bfa-cdb6-3e61-ad31-d72fc2751b29 | -15.73063 | -50.80596 | 2026-09-26 00:18:00 | TERRA_M-M | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1811b752-e0d8-3f6f-95e9-b5cbc9275410 | -18.61124 | -48.26715 | 2026-09-26 00:18:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fa269047-2071-37bc-80e2-ae85d6110d12 | -14.95799 | -47.52568 | 2026-09-26 00:18:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c5b900f1-5caf-3b4a-89db-923972566c78 | -16.57119 | -53.06815 | 2026-09-26 00:18:00 | TERRA_M-M | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f4db0c24-ae35-3528-a67e-53d4f344b0e2 | -15.19989 | -49.28758 | 2026-09-26 00:18:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a52471c8-9ba0-3c54-9f13-b430a0c7914f | -14.79775 | -45.96131 | 2026-09-26 00:18:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| a39fc7ec-5c52-37a1-9f3c-463ff834cac7 | -14.96077 | -47.54245 | 2026-09-26 00:18:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 4cd3d1fe-2c7c-3249-bbdc-64a4357a3375 | -16.7727 | -47.26169 | 2026-09-26 00:18:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6e54bedc-1b50-31d4-997e-275955aadf7a | -3.2727 | -50.1583 | 2026-09-26 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 73d96c38-5204-39cf-b22a-f80aa54d40ba | -3.9416 | -42.9879 | 2026-09-26 00:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 5de92755-edb8-35e4-9080-b306062d12ad | -11.8505 | -44.5919 | 2026-09-26 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| abf71c1c-12ad-35ad-bc9f-e4664d7aff08 | -5.6943 | -45.8547 | 2026-09-26 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 46a35210-64c5-3c4c-93b0-bed9f898b273 | -12.2636 | -50.7248 | 2026-09-26 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f7d22efb-74d2-37d8-8c7b-7a45bcf28e9f | -3.2728 | -50.1372 | 2026-09-26 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| f3798f49-8e66-3933-b913-49999d2d9eca | -5.7754 | -45.1053 | 2026-09-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 72dde72e-cd74-349a-8fd7-042c93244546 | -5.7384 | -45.0626 | 2026-09-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| be7eedf9-7326-37ad-8b60-cb18f500a416 | -11.9365 | -38.2942 | 2026-09-26 00:20:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| f125af43-1e73-3439-9dde-82c7dc88a135 | -5.6941 | -45.8771 | 2026-09-26 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d8349aec-50c5-3776-b1c3-300f877cda77 | -5.6756 | -45.856 | 2026-09-26 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| effad8dc-321c-3d71-bf81-0af8ccae32d9 | -9.7612 | -36.0738 | 2026-09-26 00:20:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| 792aee16-4fb5-3d87-944f-74e305914e6e | -5.7756 | -45.0826 | 2026-09-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| feab3f58-5abf-3627-a219-11d5b5bc8105 | -5.7382 | -45.0853 | 2026-09-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| bbc1c5c8-05d9-3d09-a5f5-30d5260a1b0d | -5.7357 | -43.2682 | 2026-09-26 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 60c17da3-22fe-3d82-952a-3c4efb3b34c8 | -5.7569 | -45.084 | 2026-09-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| a8d5e802-deb4-3290-aee9-0b3497f921cb | -3.984 | -48.4297 | 2026-09-26 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4cec1197-50e2-31c4-b8b0-d5c70a6da024 | -5.6754 | -45.8784 | 2026-09-26 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9d05083d-5401-3e9a-b692-a1dea507a886 | -11.851 | -44.5685 | 2026-09-26 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6d17720c-7a3d-36c6-a293-a4248628f85e | -12.2633 | -50.7463 | 2026-09-26 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 3c8f6073-dcb2-3e85-8c38-b87ab38ea2bd | -1.3459 | -55.4721 | 2026-09-26 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| fb7f738d-14d1-3075-816f-28e6a07c4203 | -9.7318 | -61.8969 | 2026-09-26 00:20:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1b4e797e-b755-3a73-b4da-54fa3e8dbfc4 | -11.5298 | -43.2546 | 2026-09-26 00:20:00 | GOES-19 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 242a2a74-a2dd-31e2-86be-a0cf9ab9b541 | -12.60437 | -51.96088 | 2026-09-26 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 427ea7f3-88a4-30d3-93b5-fc8a4dffe3ef | -3.97657 | -52.0363 | 2026-09-26 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 83522f11-d7f6-3e92-a399-7c342fb4a352 | -3.22883 | -54.33628 | 2026-09-26 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 571ed408-48c2-3dae-9b4a-3734f0b69a1a | -11.28689 | -54.43258 | 2026-09-26 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c7cf932c-0a1c-3d6b-92c6-62b3b294b423 | -3.06674 | -54.02641 | 2026-09-26 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c3371579-f295-3a2c-9b4b-ddf2b66d6ed8 | -3.80062 | -51.02892 | 2026-09-26 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |


[Clique aqui para ver as próximas entradas](README2.md)
