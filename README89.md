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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a69ea6f9-d924-3856-970b-411b890ca623 | -6.89607 | -43.68644 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 06f43eb7-33a3-37d3-ae3c-d4317789e96c | -4.29221 | -42.98504 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| efa3b336-dbbe-3a17-874d-0c0fecf7c229 | -4.31439 | -41.78146 | 2026-10-06 15:35:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6e9f14ae-f4fc-34c4-a96b-a08c495d9ee7 | -6.76052 | -43.70647 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e8b9e222-820a-39de-b110-4a9148d16cb1 | -4.54627 | -43.71676 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3d4ac0a5-3f45-3fae-8126-ea700053c3c7 | -7.41967 | -38.90928 | 2026-10-06 15:35:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 5910ccb1-479c-3c35-aca8-47815b78fdf4 | -3.28159 | -42.26223 | 2026-10-06 15:35:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd92e406-d93d-36bd-a3a4-1a80996f3988 | -6.93076 | -43.67529 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1d4bd343-d1cc-3571-9f7d-5175bead31fe | -4.53387 | -43.72629 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bf0e7b6b-4a44-3083-9e84-9782699a0efd | -6.64051 | -43.78495 | 2026-10-06 15:35:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e831c46a-bc93-3ada-b0a2-2d48a3acdd82 | -4.35714 | -43.91697 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e428b9c2-c142-318f-9ab3-bedfa7111b29 | -6.20801 | -41.5932 | 2026-10-06 15:35:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0152a24c-6ad3-394e-9556-5583c000f63f | -3.67645 | -42.93247 | 2026-10-06 15:35:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 80bbfb81-4253-31da-8cfe-5e66ce93837f | -4.29954 | -42.98942 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3f64ccfd-1bfa-3005-98de-a5b259ad64ac | -6.32216 | -43.81651 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| df2cc8d5-8b21-367f-bf05-a06e9a40abdb | -3.25984 | -42.98752 | 2026-10-06 15:35:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2dc3f796-a989-33b4-a996-bb6acdcb277c | -3.78099 | -41.77279 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5d4765c1-f41f-3699-9fc2-4a846c5c1043 | -3.81828 | -41.81211 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3603829a-869b-370f-ba51-821a63bf46cd | -4.36234 | -41.7199 | 2026-10-06 15:35:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2d058e5f-0547-34c5-b642-c391db1ed1cf | -8.45502 | -39.55941 | 2026-10-06 15:35:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8df44130-4a14-3b31-b3b2-96587d8fc262 | -6.45835 | -37.27594 | 2026-10-06 15:35:00 | NOAA-20 | TIMBAÚBA DOS BATISTAS | RIO GRANDE DO NORTE | Brasil | 2414308 | 24 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 297743f9-ec97-391e-8bf3-d6e7636f6d8e | -7.42497 | -38.90845 | 2026-10-06 15:35:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a09798a6-8f07-385e-b04c-6d49bd60cd17 | -6.42851 | -43.82767 | 2026-10-06 15:35:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cafb6453-3be9-347c-a065-c682e61b5fe3 | -3.81893 | -41.81674 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6b3bdaa3-0844-3a4e-ad9c-c2b42de6af72 | -3.81753 | -41.81025 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 3f3a0e25-795e-37f7-87d6-eb2d7270dc5a | -6.94215 | -43.67521 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f80e1560-1008-33f2-97f7-06b7a53f1db1 | -3.3013 | -42.35484 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 994785a1-6d64-3c72-954c-16d265be52b6 | -3.40236 | -43.1986 | 2026-10-06 15:35:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8d60cc67-d98a-39af-88f8-32207c2679e1 | -6.94434 | -41.49469 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 7592fe30-6260-3be4-80ba-dcc2868561a3 | -3.70515 | -38.69923 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6ebf8ecd-f08b-3786-8a99-d6d845b8b55d | -3.77568 | -41.69359 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b938458b-55a5-30f2-9307-230b86061d60 | -7.64059 | -37.98165 | 2026-10-06 15:35:00 | NOAA-20 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 8dfe415d-2066-3eeb-88c7-3f72e96106f1 | -3.29587 | -39.26171 | 2026-10-06 15:35:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 74ca47a8-1698-3d66-a6fc-020922cba667 | -3.30409 | -40.08503 | 2026-10-06 15:35:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 437ff78f-c9f0-3900-b456-c14b950ad654 | -6.2307 | -37.45921 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 196104f7-67b4-3ecc-941c-c3e118c3f292 | -3.30575 | -42.47512 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6655e2fa-e79b-31eb-9eb7-e94f4926b648 | -6.83599 | -39.54124 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| a67972af-634b-3a1c-b789-8b64027deb44 | -7.51656 | -35.29327 | 2026-10-06 15:35:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5bdd92d0-eab7-3aeb-9216-628eb1338c3a | -6.42514 | -43.82851 | 2026-10-06 15:35:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8a01e8c7-6008-33e3-ab0a-84ba6bdc0311 | -6.94501 | -41.49971 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 382dd34b-0ba9-3036-bd85-b12b98920e11 | -4.51189 | -42.06155 | 2026-10-06 15:35:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 3f01d601-1d32-3713-9440-199dd3dc9782 | -3.95002 | -44.02355 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 76b28263-fa6b-3b72-9f86-fb9d38c04ccf | -6.02238 | -42.27398 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 1a0e84a0-1794-3aa5-aa5e-1345eeca1ac0 | -3.5803 | -39.6283 | 2026-10-06 15:35:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a739f92e-3e74-37d8-83c1-b48063c0f3d3 | -8.83799 | -41.10247 | 2026-10-06 15:35:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 109.8 |
| be817db5-b450-3f2a-8bfc-dbd178392904 | -6.75775 | -43.70804 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4928889e-fb7f-3645-8b3a-992cd7a548d0 | -5.9516 | -41.36383 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 45d0c16f-7368-314d-aeef-4102c8c254f7 | -4.1216 | -41.7874 | 2026-10-06 15:35:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7c9218f7-6c97-3300-a65b-dd3bfdb27f16 | -3.82975 | -41.80872 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0486fd47-d5cf-3846-a700-e9c8f4045865 | -4.17599 | -42.43729 | 2026-10-06 15:35:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| be33160b-72b5-3661-b661-0404fc12d73d | -6.01668 | -42.2804 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 2e0ea836-f0cb-32cd-bad8-c2a9ebdc7cea | -6.8801 | -43.6747 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d79f21bd-8b1c-37be-bfd7-d36cad83db4d | -3.81279 | -41.82038 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 36be177a-4f8f-34ef-b689-0a3dd74217e7 | -3.76361 | -41.69546 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 58ea004e-d836-3144-b50e-19a473a0cd78 | -7.17029 | -41.99337 | 2026-10-06 15:35:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2e2470c3-30ac-341d-963a-0a1e116e25cc | -3.30753 | -42.35369 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f30cbf3-da9f-3585-99a8-d33f46b697df | -3.81697 | -41.80272 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| efb941e1-72f7-3339-9a8f-4fc94ba67e77 | -4.31372 | -41.7768 | 2026-10-06 15:35:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f4b3a10c-85e8-3b14-89cc-fe852a132eac | -8.83676 | -41.09244 | 2026-10-06 15:35:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 912831e7-0abf-3db1-a90a-9be672e053e4 | -3.80738 | -41.82597 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 74fc7850-6cba-33a6-9c8c-a89392e81c98 | -3.72964 | -38.76405 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| f887535d-bc4a-3ab6-b155-e5d4ba7e31fc | -5.96249 | -41.35253 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 277ac3b6-0dfb-3c65-bb4b-1a7af254130c | -4.50735 | -43.68959 | 2026-10-06 15:35:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 50aff35c-88ae-36f9-8718-56fabcd9da93 | -6.59188 | -41.57347 | 2026-10-06 15:35:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 482a8b03-6764-31ee-90be-c51d39ae71cd | -5.93977 | -41.3227 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 59f356bc-5507-36c9-be91-1015a2464a49 | -4.75612 | -42.60084 | 2026-10-06 15:35:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 4d5afeeb-7034-3954-b130-59dbd7300e1b | -4.84583 | -40.3933 | 2026-10-06 15:35:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c4e12558-e821-3369-891a-5c12a965e27d | -5.38416 | -38.28289 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| cbf7773a-6c90-37c7-9f4b-308e5bd80aa7 | -6.7969 | -43.73118 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db1925d3-ecbe-3893-b71f-cff2cfc931ec | -3.81822 | -41.81492 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 649a818a-de9f-34b0-a271-2b35aa45e8c4 | -6.02883 | -42.27299 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 04433bec-79a1-3b7c-b51d-9a6f52a6ad3a | -5.80376 | -38.03516 | 2026-10-06 15:35:00 | NOAA-20 | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 18860f14-7f37-3f5f-a98f-806214a981a0 | -6.02318 | -42.27719 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 0dd1b94a-c467-3d8c-bd32-11b5b02ba5bf | -4.29296 | -42.99055 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7798495c-64de-3a69-bf0c-6fbd1bcaf684 | -3.81615 | -41.80088 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 4bcc2ef3-4e9c-3099-8b27-901626f6c8f4 | -3.78031 | -41.76814 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c1da7b14-c61c-3a1e-9ce5-7f1ec941ac15 | -5.97853 | -41.32699 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6bd78759-43a6-313d-95ba-c5d69fa14cbc | -3.8755 | -42.2688 | 2026-10-06 15:35:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b92eb4c0-45bd-3642-a4a1-e4fecbda5ba6 | -3.95096 | -44.02995 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e0b9edba-d5ca-3640-9b45-50b8d39d6785 | -3.30503 | -42.47008 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2bd7f99b-5b28-33ea-a4a3-d878435c6e13 | -6.9489 | -41.49686 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 242864cc-4736-34f9-ab52-1e56e3cf0da8 | -8.83278 | -41.09542 | 2026-10-06 15:35:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f8965dae-be6b-3ad7-9e84-9a2842790753 | -6.87303 | -43.6759 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c3ee3f48-9af1-302c-96af-658ea937344f | -4.54079 | -43.72532 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 14a4ed2d-eb6d-3845-b163-7d5b1fb91529 | -3.70882 | -38.70002 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2e4b233a-7d0e-32a3-a641-7ebf91c24973 | -3.25219 | -41.88591 | 2026-10-06 15:35:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d238c196-42eb-3656-867e-11f2fba3b5e1 | -4.1794 | -38.43488 | 2026-10-06 15:35:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a7d8daf6-82f0-3f2f-aa35-8fcf2ec85769 | -4.91107 | -41.7541 | 2026-10-06 15:35:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| f0b7d09e-4300-3e25-a371-d0c949103e93 | -8.57838 | -36.72115 | 2026-10-06 15:35:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 734cbec3-f531-33fe-81c1-015664813cd9 | -5.96644 | -41.38122 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ed0ae0ab-b762-37b2-a15d-b06d9ad16daf | -6.92367 | -43.67638 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 12509be6-9a1d-3ab5-9fae-42b5581235c5 | -6.64431 | -43.78514 | 2026-10-06 15:35:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 884c80ed-a1fa-36d3-bc3e-ce8309cb291b | -3.97932 | -42.87049 | 2026-10-06 15:35:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| bfdcde90-2b25-30d6-95ff-95563647ca71 | -3.30684 | -42.34889 | 2026-10-06 15:35:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ebc0a98f-a5de-3fd2-9907-281727a0880c | -3.81086 | -41.80349 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 4d16e223-8fbe-37f9-bfb7-ae65516be936 | -3.81073 | -41.80631 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 3245b6f4-843d-33bc-b21b-6b7a18061a7f | -4.93007 | -37.38609 | 2026-10-06 15:35:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42441cb3-a372-3b07-9dfc-d029aa53b2ae | -6.19292 | -40.70621 | 2026-10-06 15:35:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d36a3ec2-2d87-31da-8870-98f64f4f5088 | -3.87235 | -42.27156 | 2026-10-06 15:35:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2b21d064-2d75-3ac8-9bf2-8f2fc2566c30 | -7.92017 | -40.94265 | 2026-10-06 15:35:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |


[Clique aqui para ver as próximas entradas](README90.md)
