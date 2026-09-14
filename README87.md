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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c7577e2-2753-380b-8a0e-b36b6c5aab39 | -7.09936 | -41.8082 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 03f43d26-9a43-3741-89e1-b5793c13f201 | -7.13269 | -42.09609 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| df4167b7-a87e-3838-9b11-e772310ecdd5 | -3.96684 | -43.10991 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7274e802-94fc-3c68-987a-01d5013d0509 | -7.01552 | -44.62373 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3d75c958-7557-3ccd-a419-610a6dd7497d | -6.77061 | -42.75687 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 45e08565-a7af-3d0c-8a0e-7dd1919fbfd5 | -9.84706 | -45.99279 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| de4bc5a3-3341-34fc-ab72-a8f03524a9a9 | -6.62701 | -45.1283 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 87ba3139-862d-3487-bee1-8f21f91717c9 | -9.84361 | -45.9763 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6eb40e79-5f2e-39c4-8bc0-e522f8ef4453 | -7.02717 | -44.62608 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b0000fa-0809-337f-a29d-1a7a2e7a380f | -6.19603 | -42.44952 | 2026-09-14 15:48:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ecfbfb79-26e8-3217-9f53-71ffbade9a7c | -4.0419 | -39.4903 | 2026-09-14 15:48:00 | NOAA-20 | GENERAL SAMPAIO | CEARÁ | Brasil | 2304608 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 78417826-7b7c-3356-864a-4c381ae7c845 | -4.76128 | -42.78855 | 2026-09-14 15:48:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f701de10-cf21-3073-9705-d9f07abaa351 | -6.41043 | -42.95719 | 2026-09-14 15:48:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a6e2512c-1cb6-3592-a070-c93660066b4a | -4.99201 | -42.4113 | 2026-09-14 15:48:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4ed6119a-9481-3dd1-b5ec-7eb91da341ba | -9.98739 | -45.88203 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 72ba4e2c-231a-3f31-a3aa-19f78ddda704 | -6.28189 | -42.67747 | 2026-09-14 15:48:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| dd67f307-7723-37e1-992a-7aad3d2a3ab2 | -5.67608 | -45.03403 | 2026-09-14 15:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9ef3eb38-ff1c-35b4-a8c4-6c820d85bb86 | -8.55589 | -36.95599 | 2026-09-14 15:48:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7347f130-3e49-34cd-95e7-aab3a16469b1 | -5.64245 | -40.85572 | 2026-09-14 15:48:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 646fd9f9-bf7a-36ec-acb2-7a0f69059d5e | -6.60159 | -42.2373 | 2026-09-14 15:48:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8dfb8f72-507f-365f-b739-6f14b7e23ad2 | -6.82834 | -43.51061 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 551ac3bf-b580-3929-acc8-b78508e53875 | -8.56363 | -44.49029 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13e2dbeb-db3b-3f79-8cd7-be0802dde980 | -5.4054 | -42.21999 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 118a80b3-c636-3d87-8569-e6eeb9aac937 | -5.66823 | -45.53522 | 2026-09-14 15:48:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d27f547b-8813-3993-9479-d37dc29b50fd | -9.85279 | -45.99445 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 96deebb4-8ecb-343a-8473-b0e4b9c3faea | -4.44755 | -39.34145 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 86929de2-ae8b-3b38-a517-8b08a4ca87c2 | -7.09584 | -41.82124 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 572820de-62fe-3488-8d02-045f83c4bd43 | -6.7709 | -42.75397 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 12279c8a-47cd-364a-93df-58fca6a39547 | -7.30926 | -39.28944 | 2026-09-14 15:48:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 74221367-2af4-3667-87c2-d4599b63fbaa | -8.83204 | -45.89751 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 72079d68-435c-3cba-afc8-a01d3ca2a346 | -8.61831 | -44.43986 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a42aed77-91cf-3eb4-bee9-f0465e24a2c6 | -9.14883 | -44.77922 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d1351e0f-755d-34e6-8bbd-94a4353304af | -9.87377 | -45.99179 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 29d71d2d-4dd2-3558-b79f-75b17f3980c6 | -9.84552 | -45.98011 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b6438e07-97d6-322a-8d19-4be7d0f4b990 | -6.42474 | -38.37668 | 2026-09-14 15:48:00 | NOAA-20 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0485c04f-3206-3bc5-9267-cf2449bc5414 | -8.83125 | -45.89109 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 10479517-de37-3f4a-9cf5-c6d459226864 | -8.21794 | -43.78708 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da16ada7-a399-308e-aed6-ef1e9f933997 | -4.45345 | -39.35225 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| af8a721d-f723-3086-a1c5-a271fd792086 | -5.85785 | -40.58263 | 2026-09-14 15:48:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 3801949e-d327-3488-9039-edd0524cf3ab | -4.71679 | -42.28307 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6a156186-ca5b-3975-b176-832ae62cecb5 | -7.18947 | -46.13225 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1099d2bb-7b5e-3bf9-8a7f-7519daa4408a | -5.41188 | -42.22863 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 03fef7cc-b008-35b4-900d-a3a3d2bc6a37 | -9.31951 | -44.35303 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ea78c7f2-f456-3be1-85d2-2b912dd7f9b0 | -8.12899 | -44.06939 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c24a63a6-45a1-3e1d-9b2c-16c76af2dc28 | -4.99878 | -42.38451 | 2026-09-14 15:48:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 484c108d-d86f-388b-b8c6-f6839822f28a | -6.65364 | -43.66288 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 25c41285-252c-396d-aee8-68eea262081b | -8.59212 | -44.48642 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bccf379b-bfeb-3aa8-9cb3-08c18cae7b70 | -7.08687 | -41.79373 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 6838cb85-19b9-3a2a-9b55-0f1fa55df7f1 | -9.20158 | -46.58422 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 07237ee4-ff12-33f7-8755-d7ff0e0c6e3d | -7.29586 | -42.35494 | 2026-09-14 15:48:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d8383f9b-4539-3acf-8b5c-3d148baa7b92 | -8.36259 | -44.82946 | 2026-09-14 15:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 169b15e7-3315-322a-a280-d71a0696ee79 | -8.39762 | -42.21819 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 29205fa8-9df6-332d-8bdd-fc4c22461c39 | -5.40928 | -42.22002 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b233aca3-b204-3fd1-aaa5-5d9639de8adf | -7.11451 | -41.80325 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0d35dd44-f5ab-362e-bc28-fb520ebf14af | -6.09779 | -44.13627 | 2026-09-14 15:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8ee391c-4e7b-3d8d-90bb-d2036b3a6bb5 | -5.41146 | -42.22554 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e7d70788-6a09-3fa2-83a3-f2a774237686 | -8.41298 | -44.75135 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1f9e69b8-667a-30fe-aead-fede4cc972e5 | -9.63008 | -46.06897 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a8a6701-fd45-3ceb-acdf-a820ee8bc6bb | -7.15695 | -42.11632 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d4c9a053-ad5b-3ed3-9832-21152bf1d0cc | -7.85193 | -38.07458 | 2026-09-14 15:48:00 | NOAA-20 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a84aeb5a-12c7-3c12-bf9d-6b9dfc6339aa | -7.4652 | -45.97657 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 137f5f44-a699-3788-947a-bc2d921f7424 | -6.79172 | -43.76135 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 516a5bbb-5cf2-3b8f-bbcc-01738f440b73 | -7.1521 | -42.12029 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 4605b466-cb77-327d-8d4a-0dbb9dd30de8 | -6.70069 | -43.14344 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c4e39f64-51c7-3ed5-a3bb-539468ed75fe | -8.41077 | -44.74858 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ff971e12-0024-33a4-96f1-1aceb0a07c4a | -3.94891 | -44.74249 | 2026-09-14 15:48:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1517f486-0719-3c62-bd64-925868b7e88d | -8.16201 | -39.73631 | 2026-09-14 15:48:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 24cab089-ada2-34bf-b88e-de2ac82989ff | -5.92059 | -45.03702 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5957d72b-202f-3acb-8610-aa53c21b12bd | -9.49816 | -45.48096 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d6c9f950-9e4c-39e9-a851-6cfb01ef2c53 | -7.26873 | -44.12686 | 2026-09-14 15:48:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7ca9045-2746-3041-ba78-e205cf862590 | -8.12813 | -44.06765 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9e898e66-0fb0-30eb-b8e8-a4af03f20c6d | -9.5334 | -45.43229 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 47ca538e-4acf-3dae-82d9-79ec522d03c9 | -7.11926 | -41.79943 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 98d0692e-987e-3548-87d8-ca3f0c862b9e | -9.19837 | -46.58347 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8d7ef853-c488-3246-9c29-f51a39983e83 | -6.87427 | -38.73956 | 2026-09-14 15:48:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 82b53490-0f84-3767-9d74-ba6781be5831 | -7.11114 | -42.09573 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cf770c93-9d70-3b75-a553-1c40aeba63e1 | -6.165 | -45.18377 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cf50ef0d-7422-3907-b247-c41d3c9c37f3 | -8.56992 | -44.48946 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6f25fd35-54ee-3002-b8c7-b0461942ef1d | -4.0995 | -42.50237 | 2026-09-14 15:48:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 327c6b2c-a0ec-35e0-8f6f-146fc4678913 | -9.8618 | -45.99727 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1b57fa74-cb53-36a7-940b-15e3a0964d64 | -4.61996 | -41.39795 | 2026-09-14 15:48:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 84124110-b3d6-3498-a683-1f09f58cb8a8 | -6.40991 | -42.95338 | 2026-09-14 15:48:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 6374e61e-73aa-37cd-bdc4-76361de8a657 | -7.45415 | -43.08646 | 2026-09-14 15:48:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| beeaadd5-2c91-38c7-a3b3-04f1d6527b87 | -8.5532 | -36.95882 | 2026-09-14 15:48:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ccf98d15-8ff9-323a-9954-008af29c5330 | -7.08701 | -43.54019 | 2026-09-14 15:48:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 311fb855-4bf3-39a5-b4e0-de1e500177b0 | -5.92312 | -45.03431 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8c6bb1ec-71e0-326c-a86c-f8cdf4d28051 | -7.10591 | -41.77873 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| de222961-7f36-3dda-8b11-d9b460c3b61f | -3.91234 | -44.48027 | 2026-09-14 15:48:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a75d7cf8-99d6-368e-8c2c-6634ec769643 | -5.49275 | -45.55512 | 2026-09-14 15:48:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19a8f20e-a87a-3ff6-9c80-6817de6461e4 | -7.98431 | -38.87875 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ae67d5dd-81c7-3d4e-bda1-b3001903f9ba | -7.08834 | -42.12239 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| e3f6f3e1-55f5-3a61-b987-7f1427ab9a55 | -8.42405 | -44.75089 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6c58db7-ae3d-3712-86fb-f17d5b0cd6bd | -3.42613 | -39.61865 | 2026-09-14 15:48:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| f05fef5d-dc77-3517-b453-3d5b48cefee7 | -7.0879 | -42.11915 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 554abe9e-1923-34d5-9388-a43025962956 | -7.19556 | -46.12571 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ae6c97bf-e97f-34db-b3e9-f164628e2e84 | -3.93378 | -42.9934 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| ada93632-dde7-3dae-ad3c-90b390d8631e | -6.77014 | -42.75348 | 2026-09-14 15:48:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| bada481f-f663-39b7-bbab-cda7737f4aa0 | -8.99844 | -39.97972 | 2026-09-14 15:48:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8df12ec4-bfbf-30df-9cfc-32609ca2b67c | -6.93814 | -43.87767 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2cf8a2c2-2b2c-3c94-90dc-65217c43350d | -6.19647 | -42.4528 | 2026-09-14 15:48:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README88.md)
