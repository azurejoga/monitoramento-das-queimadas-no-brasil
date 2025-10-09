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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56934cb7-65cb-3bf0-878a-7d2303f8aad4 | -7.42268 | -42.97433 | 2025-10-09 12:17:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 7f179e8d-964d-39cf-a971-6459a051cda4 | -5.84528 | -44.35702 | 2025-10-09 12:17:00 | TERRA_M-T | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0986da07-a32d-3e27-ae3b-afc132c56dff | -8.10096 | -44.82664 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8445983e-5782-3552-8d93-b904497f735d | -7.25455 | -45.81414 | 2025-10-09 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9fb85b11-8f73-3d8b-9aa8-e8297382b352 | -7.02329 | -42.86219 | 2025-10-09 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 33.8 |
| ae57d8c2-94a3-33cd-bdb4-a159ebaa13ee | -4.38952 | -43.05851 | 2025-10-09 12:17:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a28c494e-e233-3ce5-8ea2-7a6d4b275838 | -6.46003 | -44.57064 | 2025-10-09 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 4e29d97c-d7e4-322f-a8bb-e78ed85f0d41 | -4.57388 | -41.97678 | 2025-10-09 12:17:00 | TERRA_M-T | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 56058f90-2a9f-307e-9f02-cc2c000a8331 | -7.5503 | -44.29468 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| ab71adbf-1b13-313d-a2ba-781b9f1b3f00 | -7.52579 | -44.32591 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 389124de-0b29-3de5-900d-c185d872eeee | -7.5128 | -42.73137 | 2025-10-09 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 0b0b3108-2c58-353e-9850-f2e28e3a6d54 | -6.68838 | -46.29736 | 2025-10-09 12:17:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 623aaaba-bf34-30b5-a94a-e43437883087 | -14.85694 | -48.43267 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0c430208-6841-3e92-ba31-63917a971087 | -13.82675 | -45.85946 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 59f56f96-6597-3245-be57-1e0461cf9dc6 | -16.93403 | -48.73004 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 157ac4bc-93b9-3f5d-a1af-45ea21766c37 | -11.98496 | -45.19564 | 2025-10-09 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9350e695-0768-3dce-b783-3967b4af8e78 | -12.43531 | -45.73598 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 283a8255-6e0a-39e2-a5ea-acd4a4c7b2a0 | -18.65056 | -43.92817 | 2025-10-09 12:19:00 | TERRA_M-T | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 9c1ac56f-2601-3a2d-9339-beb5bca2b503 | -13.22405 | -47.78892 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53e801db-3667-3592-9820-9a03759a4df0 | -16.6052 | -46.53823 | 2025-10-09 12:19:00 | TERRA_M-T | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b68aa0ca-1baa-38c0-92c3-ccc2ef7b6c95 | -14.26478 | -45.86927 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4b00794d-f12f-31cf-9dfa-a6a74426b5d6 | -13.25668 | -46.4759 | 2025-10-09 12:19:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4a9c0c19-7ba9-30d8-a59f-395932f59b8c | -13.1334 | -47.77876 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 011019ca-5628-3a44-98cf-591dce6d1791 | -12.68596 | -47.68406 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d32440a3-700f-3138-8366-0cb99f9cb7f6 | -13.28618 | -48.4592 | 2025-10-09 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9ab8248c-6b34-3e48-b695-227ee7ef7396 | -14.44092 | -47.98465 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 559984af-09fd-3f37-90e1-d41b86ad0aa1 | -12.89783 | -43.14949 | 2025-10-09 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f146eac7-d7d3-3243-98b9-523252333f4d | -12.27704 | -47.64772 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a032555-01ce-3fc2-8325-36254814835d | -17.52583 | -46.74803 | 2025-10-09 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5e0845e9-059a-340b-a780-9bbbc00bd921 | -17.35579 | -46.64423 | 2025-10-09 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1cebfab6-a7d7-398b-a72e-5ed6595b9d7b | -15.78677 | -46.24712 | 2025-10-09 12:19:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1fcb6bbf-295f-3e5f-8679-50ebccb93cf6 | -15.48418 | -47.96428 | 2025-10-09 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 33c4083a-77c7-3204-8963-cc91d8c453c7 | -11.47188 | -43.48222 | 2025-10-09 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d8cd5b43-d003-347f-8690-990a277b7522 | -18.03152 | -44.94693 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 0449148b-052e-3b8f-84eb-c3b591cbbd94 | -14.25349 | -45.8795 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 49ed7448-a8dd-3e91-a730-89e0e8d3a620 | -11.53335 | -47.10189 | 2025-10-09 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 69e5b9b0-7130-3703-b206-c43f6381021f | -18.86135 | -44.10653 | 2025-10-09 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 67bf81d9-5c22-35f5-a1dd-47f16fcc4b33 | -13.83943 | -45.83857 | 2025-10-09 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 801fc954-5e62-32a6-8fba-7f6938afc3aa | -17.37592 | -46.89087 | 2025-10-09 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ccc89d71-c8a1-30d3-855a-cc8441b82c4a | -13.29278 | -48.01938 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2522f55d-fceb-3b42-b946-67e4bb344832 | -15.46621 | -47.96165 | 2025-10-09 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b479d4aa-7f9f-3503-8648-de3ed6308fb9 | -13.45056 | -47.61804 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1d99a8ec-4022-3d11-be95-9642b0da032e | -13.80431 | -45.87939 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| e78388ab-3397-3ab6-8f19-f26465b52e2e | -14.16739 | -43.13193 | 2025-10-09 12:19:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| b0d528ed-bc91-3eb9-8a03-ad35bcb89127 | -13.40335 | -47.56351 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 35.4 |
| dd272d46-0718-378d-a02b-013df960889b | -14.37869 | -46.00477 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| cb079adb-0ae9-3682-b524-8280991550c3 | -13.13211 | -47.78792 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e7c19149-9658-3ec2-a88f-e2fc50ab9c36 | -17.6373 | -47.22013 | 2025-10-09 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 73955311-0db1-327c-85ca-2105025cbc5c | -17.52444 | -46.05277 | 2025-10-09 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 68c389ba-0be7-3b67-84a3-1a1ba9d22db3 | -18.02874 | -44.95567 | 2025-10-09 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 51a0817b-0955-3a52-bc05-bbca0afcfbaa | -14.37723 | -46.01581 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0870d62d-781f-3e22-ac55-33f437635952 | -14.40838 | -46.02638 | 2025-10-09 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 15b62681-17d3-33ad-be31-854808fb1d43 | -14.53324 | -48.70124 | 2025-10-09 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 7b2bb052-9428-37a3-9ecd-9f217d661397 | -13.04345 | -47.89109 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5a6f8f34-521b-3567-a842-9462b44c266b | -11.78771 | -45.14449 | 2025-10-09 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d8c9cc30-359b-30b1-a3aa-ee940fcdf88a | -18.1353 | -45.71157 | 2025-10-09 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 31ab6fa2-247c-3adf-aeee-5f708006d103 | -13.80286 | -45.89056 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b54cb0c8-73b5-32b1-97f2-28b4f6682c4c | -12.69487 | -47.68531 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| e9420b43-e34d-3afa-8471-3b2e851cd3c0 | -15.75312 | -49.00617 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6f67492b-49f5-3cce-9b01-508dfa1897e6 | -17.21182 | -47.64951 | 2025-10-09 12:19:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| ca7759fa-74ff-3d82-bd3e-687dd000559c | -14.61327 | -42.21732 | 2025-10-09 12:19:00 | TERRA_M-T | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 977386d6-1e0a-35f6-9c1a-1e0af39fdd06 | -12.07701 | -45.73998 | 2025-10-09 12:19:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f5642dc8-2565-3f5e-b977-3629ad9c3e00 | -13.0448 | -47.88166 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 36b93aea-8ffc-3942-81d2-248cb2cfea01 | -15.89583 | -51.74087 | 2025-10-09 12:19:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7856fb39-4bd2-3a66-bbd4-5e80d46b090e | -15.23317 | -48.18293 | 2025-10-09 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ba28437b-4682-3814-ae21-4ef1c403060b | -13.20307 | -48.45914 | 2025-10-09 12:19:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9d685c02-afa3-3568-a653-eb69d252debd | -17.52933 | -46.74348 | 2025-10-09 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 063301ad-1ec9-36cd-a074-e96246dd3463 | -13.80035 | -45.83332 | 2025-10-09 12:19:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ed4a590c-8b61-304f-a068-8ae42afecb20 | -13.10279 | -47.80249 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 684633ad-7ca7-3ff5-90ca-a870d15b72d7 | -15.55735 | -45.32801 | 2025-10-09 12:19:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ad4fccd3-4191-36be-8863-bb36c85aa937 | -13.0526 | -47.82671 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7ac385b9-e2a1-3b36-863f-1413fccf1f73 | -13.14232 | -47.78003 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 757a5ea3-465b-30d7-8ff3-de38b3fe1eca | -12.42707 | -45.72382 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 5f2f5889-aec2-37c7-b0f3-7dd315045123 | -10.18196 | -44.55217 | 2025-10-09 12:19:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b7d67e4b-42a8-350f-b259-3bf64d598c08 | -15.38927 | -48.05018 | 2025-10-09 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fd329c41-2bc9-390d-bc69-64849393eacf | -13.30385 | -48.46178 | 2025-10-09 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 46ef1515-3f85-3102-882b-5959c95efd3b | -16.06098 | -50.98148 | 2025-10-09 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 58a9f7b8-c6a9-3af3-bd40-27e0eb3fa29f | -12.76172 | -42.66546 | 2025-10-09 12:19:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 21ae0903-bd8d-3e10-9ccf-82d25a14d24c | -12.23134 | -50.955 | 2025-10-09 12:19:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 05891216-92be-352c-bd3c-90f06bf8e706 | -13.05574 | -46.81182 | 2025-10-09 12:19:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ef5355d7-ee34-3e60-82ea-d4c0128ec3ca | -11.87034 | -45.51677 | 2025-10-09 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a4615dbc-e877-37a9-be43-db9a2c312715 | -12.42992 | -45.70198 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 41e818a8-4f11-30bc-a084-2148f2ce6371 | -16.29317 | -47.14807 | 2025-10-09 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 01b4d01b-320b-349a-8f61-5ed34b545f89 | -10.83376 | -47.09538 | 2025-10-09 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bd0687ce-deec-398f-a5a4-1c4eea959e0e | -11.66721 | -47.52695 | 2025-10-09 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 78602308-959e-3d93-a576-011141b6b770 | -17.63873 | -47.20945 | 2025-10-09 12:19:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 13146321-acef-30fc-bd0a-d79a035a571e | -15.73944 | -49.02555 | 2025-10-09 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 837e73ea-ba6e-319f-8876-7da7be7efa24 | -15.01035 | -47.52893 | 2025-10-09 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 80ae28ac-f9dd-31d5-8c84-5f78ef26dade | -8.62939 | -45.14054 | 2025-10-09 12:19:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6b857985-20da-3b71-af32-28fa1d9dd74a | -14.61366 | -42.2029 | 2025-10-09 12:19:00 | TERRA_M-T | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| c94950e4-7ebd-3c56-87c7-208dee2b7fbe | -17.22104 | -47.65079 | 2025-10-09 12:19:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f4baf8bc-1233-3a6a-8c8a-c5ad61179b93 | -15.75042 | -49.78675 | 2025-10-09 12:19:00 | TERRA_M-T | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e81200a5-2e2e-354e-9460-5ab18f717994 | -11.73602 | -46.36659 | 2025-10-09 12:19:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 409d53e6-2dae-37d9-8f33-fea48bfb109c | -17.21046 | -47.65949 | 2025-10-09 12:19:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| aba588bc-cc9a-36c8-9d69-d8f412f667e5 | -11.73736 | -46.35675 | 2025-10-09 12:19:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| ab93aafb-9094-33ae-8acd-bf8e5d54a6c5 | -13.34083 | -47.61395 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| aeacc4d0-b57c-32fc-be66-b5ed8d11edf8 | -13.43137 | -47.62468 | 2025-10-09 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 08e6105b-914d-3dcb-af75-1e8aaa876a24 | -16.93272 | -48.73936 | 2025-10-09 12:19:00 | TERRA_M-T | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81d13b32-d01d-3fc7-a2b1-205095a56f39 | -13.29372 | -48.46952 | 2025-10-09 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1f0375f5-e248-3509-a4d0-c0560fb16660 | -13.06203 | -47.834 | 2025-10-09 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README64.md)
