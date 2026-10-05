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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8099d95-c9d6-335d-8b38-dd4300c518ad | -3.21424 | -42.87429 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3af5c71d-7bad-38fa-9aff-fe39db46449e | -2.98947 | -54.03567 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 73ec816b-27dc-3615-8ce4-947c5a5c029d | -4.44337 | -54.96377 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8791bc69-ef60-3e35-abed-a3b5f742e8fb | -5.14607 | -37.40969 | 2026-10-05 16:39:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 077d124b-385e-3f2e-98b5-616090a70013 | -3.28973 | -59.41894 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bdd81ded-eebd-3bc2-b0e7-38474e229057 | -3.98893 | -55.81876 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 08fb6f18-77f5-37ff-8249-701b2c469db0 | -5.95414 | -41.346 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |
| b79b59b6-2ff4-33e2-8e65-c7c74ac1b46a | -3.07726 | -58.42734 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34f47083-6fda-3d88-959d-eca5ab0646bd | -3.69678 | -44.9682 | 2026-10-05 16:39:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 04bb5d4f-cccb-35df-b69a-3af3f53b3c1e | -4.06966 | -55.76785 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 4201652e-8c0f-3099-8743-a61016f74bc3 | -3.62828 | -58.61236 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d75b5837-ad62-3c20-a23c-65c6ea5d8518 | -7.22369 | -55.18093 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0c2de9f1-19eb-341f-9ad0-e313254932f9 | -4.46766 | -54.96949 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 94a81ee7-be23-3c4f-9d13-f90ee6e22721 | -3.6124 | -54.60172 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 445d1f30-567d-3963-aa00-7bdb3301361a | -6.04375 | -45.23371 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e27bc70f-8a76-3c38-91f0-bc8925328caa | -5.30888 | -42.7107 | 2026-10-05 16:39:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a3561c21-9cbf-3f76-ac16-d7f3f4ec8437 | -3.10123 | -53.71635 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| c230237e-cb8b-3c28-a5f7-f50e3f599df9 | -4.85335 | -42.20024 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 8ed28963-3c7b-3ba7-b538-d5c9f2fb7591 | -3.06503 | -54.16529 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3fa968ab-5105-3adc-ae39-3da5a107ce88 | -4.29656 | -42.19034 | 2026-10-05 16:39:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d550ab3b-4cfa-321b-ae0e-8619512d1c65 | -4.37189 | -43.91141 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94be5807-d9ef-3ddc-9ef3-38cd3d76b736 | -3.74485 | -39.53354 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d1943f77-4f0c-3686-9f81-9522c1cf7049 | -4.76989 | -43.68363 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a42b6bcd-3aa3-343c-b8dd-7f8dfa53d02c | -4.122 | -54.42347 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8a1fb860-5e21-33de-87e4-d5640dc675a1 | -3.45331 | -43.03456 | 2026-10-05 16:39:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4988cfcf-a5ba-3c56-b634-ebadb0b36ce1 | -1.42924 | -55.34669 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6fdf4607-7c43-36a6-a083-b2bcc678cbd5 | -3.27169 | -41.84411 | 2026-10-05 16:39:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4f730744-df04-336b-be71-867731a9c5d5 | -5.26935 | -47.90638 | 2026-10-05 16:39:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1c25a815-df0d-38ad-831a-4c81e37b0343 | -1.05838 | -53.5902 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e1350bb3-8f74-3fb3-91b0-ac4a34df06cc | -1.1887 | -50.2338 | 2026-10-05 16:39:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| edea328d-003a-3cb4-a598-f3e0d1ec162b | -2.51429 | -44.18195 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5281c36f-d9ac-30df-ac79-88a8da87ecbf | -1.51539 | -54.82362 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1d65a308-8d54-3a55-bbc2-c21716509e2a | -2.95779 | -41.99591 | 2026-10-05 16:39:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 581908ba-f7db-30a2-a737-e00298a32e9e | -6.70553 | -55.2133 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4d0c65e4-918f-3479-9397-aa4775a3c0a3 | -3.11651 | -40.15881 | 2026-10-05 16:39:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| dbf250a5-d383-3a21-9e92-21f0f4eda52e | -6.32945 | -55.31797 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6c2c8d3c-6ed9-3329-81a2-a45c5394884a | -3.12811 | -53.70792 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 63a46af3-0f81-3a21-989a-5eaca05604d2 | -2.89734 | -54.11588 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a0e86bff-2c53-38db-bd8d-339caf78538c | -3.66298 | -44.80061 | 2026-10-05 16:39:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 7a663fe1-30e5-3d80-ace5-047e4699269e | -2.83082 | -43.6861 | 2026-10-05 16:39:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 119cf9c9-7390-3652-8cbe-fa5652d2c5a3 | -3.53881 | -59.40726 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c398d23e-33a5-36e3-9ed9-3dc1476faab1 | -2.90332 | -54.12706 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e02ba5a6-7c2c-3595-a716-250f7d720827 | -0.9422 | -50.58945 | 2026-10-05 16:39:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8efc578b-3fc1-3098-8236-75b25e9e77dc | -1.48873 | -55.66811 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 516bf34f-12c0-36b0-864c-f8f5953789c9 | -1.18862 | -49.25346 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3b0c1ebe-d414-33bd-96fa-fa77ddfd80ee | -4.08225 | -59.12687 | 2026-10-05 16:39:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b03d1edb-3e23-3488-bdf6-a3faf0b10435 | -4.07572 | -55.77052 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| ddc0ffcc-5123-31a1-be7a-371195a857ef | -3.09162 | -54.17352 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a2b346b5-d7fb-365f-a4ec-55e5caa8ebd1 | -2.9391 | -54.10594 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e18b3001-8d54-3254-af38-7111df6ce26b | -4.33833 | -44.37934 | 2026-10-05 16:39:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3055e945-0624-3554-a205-38a498768d1a | -5.99673 | -53.63724 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d8ad0e8-55c1-3cc9-b197-2bb363d28216 | -2.28566 | -56.7924 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cb0f02c3-1d1c-3e35-86f7-cf744b3fca0e | -5.70378 | -45.84376 | 2026-10-05 16:39:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 33b0c417-1ae9-3778-abc2-712f1c69d19e | -3.20565 | -39.91951 | 2026-10-05 16:39:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f2ff3bc2-c594-3606-8c42-b15a94c14be1 | -3.23699 | -57.99043 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 360f9926-c540-3c98-9e1d-46ca49dabf3a | -5.4804 | -39.55653 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 519bcf60-747c-3866-a19c-9de41e24f0eb | -1.90611 | -48.56506 | 2026-10-05 16:39:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 94de5dc5-d716-39ea-b7b7-01eeb3595da0 | -2.86537 | -57.57116 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b542d94c-f749-36cd-950f-105f7fe6562f | -4.86248 | -38.98359 | 2026-10-05 16:39:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 8a2cbf7c-d4d3-37b9-95f1-67e7bbf29bb7 | -5.84693 | -53.82005 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 32e4a9ca-f9e3-3e0f-af8f-884f59c2a348 | -4.84902 | -40.25798 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 481892da-46cf-3265-98da-1dab3eac5e14 | -4.7827 | -39.97345 | 2026-10-05 16:39:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 166.2 |
| eabcc887-8443-30fe-be0a-525dcf7be340 | -3.04529 | -54.26672 | 2026-10-05 16:39:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6016fa25-be09-3a26-8d35-62f69435cf54 | -6.17234 | -43.42288 | 2026-10-05 16:39:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 246385a5-156a-32d6-83de-215b79a956b6 | -3.72203 | -45.40662 | 2026-10-05 16:39:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1b1412b1-e332-3a3f-8fa2-e20fa85b170b | -2.87835 | -54.07478 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d5e26596-1804-37c1-b735-c2ee822bbdf3 | -3.2148 | -56.84156 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b5224107-2e5e-3e67-a6f2-8a9abb2da582 | -2.92745 | -54.14376 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 82236449-5e66-350d-9834-f14eef30598d | -6.20431 | -44.80124 | 2026-10-05 16:39:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 009c6a0c-afda-3a19-9a0c-c2395bf2225c | -5.84371 | -53.8167 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| be35ef21-4074-3396-8769-4954b394bcc3 | -3.1296 | -53.70848 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a9d77bf0-7a86-387c-9c80-2d53d5875ef0 | -2.47265 | -49.40612 | 2026-10-05 16:39:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 14fc8e46-fadd-37cf-ba68-1c72c37ae93b | -3.03574 | -57.41723 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76497a30-eb96-32ee-8016-87db48aabfc5 | -3.06076 | -54.16587 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ecdfaf7-b4ff-3ee2-9df2-368a147ee904 | -1.9372 | -48.38739 | 2026-10-05 16:39:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0841b59e-9230-37a6-a58c-066fa764783d | -6.03966 | -45.2304 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e9cd4bfc-3013-37de-a267-fb6a453ffc30 | -2.2069 | -49.51472 | 2026-10-05 16:39:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 34d9a644-8036-3c90-86c8-88a3fc66a605 | -4.80598 | -42.15047 | 2026-10-05 16:39:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| b20e26fa-7656-334f-9d90-fca3dfecbb23 | -5.36521 | -44.37603 | 2026-10-05 16:39:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8207620-c279-34a7-9930-adf8b72043e5 | -6.45894 | -55.47449 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c62795b2-36a2-30c0-99c3-f9f981cd4602 | -3.86974 | -55.8347 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a77e2c83-57ff-3941-869c-e3894c0e3fab | -2.13893 | -54.42376 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50d67372-3624-36c8-b684-c7ff5cbf9075 | -4.89942 | -45.6813 | 2026-10-05 16:39:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 324f1ca6-d5b9-3b01-8e03-2d7d908bad75 | -3.5392 | -39.8845 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 01ba2caf-2c16-3c87-b1e5-5ed03cdd0c3c | -2.98652 | -54.10391 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| a1aaf6db-e313-3771-8cb7-ed5d7bdc65db | -3.8545 | -61.34797 | 2026-10-05 16:39:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f75e57c9-ba5e-356d-ae7b-59c53ef26780 | -1.51721 | -54.8064 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| abcef0e9-fd2e-32ac-a3f3-cb8c8bbcece9 | -3.53757 | -60.51973 | 2026-10-05 16:39:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 917dd80c-6091-3d07-b34e-cc58cefaa6f5 | -2.77542 | -57.65321 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 439534d5-0bb9-372d-8aef-5180846664de | -5.83938 | -44.90208 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3adcd80a-6981-3698-ba3a-0e5e27c3d9fc | -3.71612 | -58.93325 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| cd5ec4bc-b83c-385b-b917-8500fb8c1938 | -7.22475 | -55.17839 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 923026e1-931a-3dcd-9dc5-abaee220fa55 | -2.78125 | -57.21471 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a8a71a85-58de-3380-bca0-d438cc46b0fc | -1.80299 | -45.27365 | 2026-10-05 16:39:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4f7cab7d-269d-3b43-8d84-cec6c72d14c9 | -5.48635 | -39.56149 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 74ec6d98-ae95-3b12-8d61-7533eaa59c73 | -1.0134 | -49.17575 | 2026-10-05 16:39:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f154e78e-63d5-3fc9-a76f-f76d478d6fe0 | -4.37949 | -43.91022 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ad26661b-e9cf-3565-9afd-5a54ab602138 | -3.14268 | -53.72107 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a0ba3add-1646-3d2a-949b-7c29b0f0442a | -3.11014 | -42.92802 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| da5978b2-ed69-3b91-968d-b5462f59ea88 | -7.22579 | -55.19667 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |


[Clique aqui para ver as próximas entradas](README99.md)
