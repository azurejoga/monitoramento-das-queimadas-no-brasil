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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27d8b9e6-e22e-3e0d-a7e6-3209aeebc216 | -22.06277 | -56.53018 | 2026-07-28 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7e4b81b6-9793-3db9-8cef-00f64234a1e4 | -23.97878 | -48.52339 | 2026-07-28 04:36:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1d481fad-c756-39fb-98f7-aceecab7cac4 | -22.06389 | -56.52484 | 2026-07-28 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c91afbdf-3996-317a-8f5f-691836005832 | -23.02106 | -46.67829 | 2026-07-28 04:36:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8c34492-efee-3a9b-a675-288c020842f1 | -20.65588 | -57.27852 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0d936cf-e3eb-3c31-9d57-ebb69f85f2b5 | -20.61284 | -57.25616 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13c69a9c-8f46-3fbe-91a4-deda6343915e | -20.60541 | -57.24125 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28ed32db-0273-35bd-a937-198e545d94df | -21.71268 | -43.36607 | 2026-07-28 04:36:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae046be8-a44d-3f9f-bde8-7fb1ffabf2e8 | -20.29488 | -53.72773 | 2026-07-28 04:36:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d631c34-987d-3daf-83e8-3bdb1d7f7e6c | -20.61723 | -57.26045 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5391472c-267d-32aa-885d-1a2e924c771c | -20.65022 | -57.28016 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa520dfe-0ce6-34f1-9bb6-fb1be72276ba | -20.62538 | -57.2721 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b9a61cc-8a22-3f6f-9b30-ff4c6d1c78c6 | -20.55846 | -57.28639 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c8f716c-bc51-3421-a435-f6bd3049906f | -22.6856 | -46.23064 | 2026-07-28 04:36:00 | NPP-375D | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b00155fb-d575-30f0-a817-c4e13dcf4439 | -20.61218 | -57.25924 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f152950b-108d-31ec-8b60-e2ae14fbbf49 | -20.64517 | -57.27894 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e385963d-c99e-3d43-bc59-8b02293fb9d5 | -20.62669 | -57.26593 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9576589-a6e4-3094-b7c5-2bce9639bfd7 | -20.5642 | -57.28448 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef57bf86-820b-3553-8da3-cab27c5ceda2 | -20.62604 | -57.26899 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e51936e-8cdb-3145-86f9-00f9e282d95c | -20.64446 | -57.2823 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 393316cd-01a7-32a7-97c6-4e25d48c86c0 | -20.61658 | -57.26353 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8a5cff0-689f-3386-9264-aff7ea28a05f | -20.59665 | -57.2821 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 135beea6-24ad-37b8-894a-dc08705b59fb | -20.65086 | -57.27714 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81ee526a-3594-36ce-8a56-05738bc6cf21 | -20.59157 | -57.28099 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95bf4ea3-120c-3c45-a0a4-93e0513415d9 | -20.60608 | -57.23813 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21d37603-de17-3ed2-bacb-8e39e05cb096 | -20.58582 | -57.28302 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abe11b82-3a91-3634-97d2-b90288cbc71f | -20.60105 | -57.23685 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b2c04d1-cc31-3920-a05e-cfe0dcd7fe44 | -20.62162 | -57.26478 | 2026-07-28 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624e1ffc-62e1-33a5-b838-5042a4ee464a | -27.34768 | -50.73 | 2026-07-28 04:38:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a85e3d50-aa62-3de5-9d4e-f1b793a63d29 | -13.3037 | -45.0812 | 2026-07-28 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b6ca8200-262b-38fa-8299-69549a171551 | -10.9401 | -43.0355 | 2026-07-28 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| c0e2ac4a-c5d7-3381-b44a-c1125e0ae0e9 | -18.3749 | -50.6564 | 2026-07-28 04:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 467b139b-d8f9-3db6-8ea6-f7cd3c1ab345 | -20.723 | -49.4242 | 2026-07-28 04:40:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1fc221df-94e1-3745-a7ca-71c2bfd11021 | -18.3743 | -50.6786 | 2026-07-28 04:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| e1506cb8-fa09-3765-8182-dac8bc9fd4a1 | -13.3032 | -45.1045 | 2026-07-28 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| af23c40e-34d1-35f9-a466-e64cf7ace59f | -10.9588 | -43.0565 | 2026-07-28 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f5718133-9356-3e9f-86b5-90e446d2db93 | -20.7223 | -49.4471 | 2026-07-28 04:40:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 51.1 |
| db76a8e7-f6e7-37da-aed0-eb5e6e484d04 | -10.9397 | -43.0593 | 2026-07-28 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.7 |
| d721056f-e8c2-3a2b-85cd-5f82bbef7903 | -0.8949 | -50.66998 | 2026-07-28 04:49:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5017663-99ae-3854-a706-700b8e62a45d | -0.64989 | -50.50064 | 2026-07-28 04:49:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e74f7e1-3512-3be1-89b1-0da8dc03089a | -18.3743 | -50.6786 | 2026-07-28 04:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 245.6 |
| 3b3772b2-72d7-31ae-87ac-b41b949f0b9b | -10.9397 | -43.0593 | 2026-07-28 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.4 |
| e4edf53c-3867-3fbf-8d0b-30ad51c712e7 | -18.3944 | -50.675 | 2026-07-28 04:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5b0be046-7044-382e-9454-e5ad20808248 | -18.3543 | -50.6822 | 2026-07-28 04:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| db87834e-0f57-3029-b160-55684840fbfb | -18.3738 | -50.7008 | 2026-07-28 04:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 13ff4c28-1ea0-33b7-97e5-9fd19c947b94 | -10.9588 | -43.0565 | 2026-07-28 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a85f9c5d-ccea-39d7-80a5-38deb60ec4eb | -13.3032 | -45.1045 | 2026-07-28 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e10f0410-8145-3fc8-87ae-07b8c1ac72df | -20.723 | -49.4242 | 2026-07-28 04:50:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 51.2 |
| f6464c23-5a3d-359d-91e6-a82f48a61fde | -10.9401 | -43.0355 | 2026-07-28 04:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 3e1cc630-9075-37d1-9085-99bcc89d1781 | -18.3749 | -50.6564 | 2026-07-28 04:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3c4db258-433e-3ef0-944d-ef34b48dcd5e | -7.73163 | -44.55682 | 2026-07-28 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bf50acc-2e6c-3c26-a81e-c29100a29cae | -9.20686 | -49.8249 | 2026-07-28 04:51:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e433c5c5-b7a2-341c-a857-749ce09914ab | -7.24129 | -43.14009 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 378a50d2-fa30-359e-b39a-f8a5b090b3bf | -9.36803 | -44.72457 | 2026-07-28 04:51:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f22710f-4947-3812-a2a2-1b7b131db534 | -6.48082 | -42.2251 | 2026-07-28 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d21c9cf1-ff39-3baf-be50-73de14436bc0 | -8.20278 | -47.24496 | 2026-07-28 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dca444c-0b26-3e8d-8352-6f90a4043471 | -7.01115 | -45.42905 | 2026-07-28 04:51:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dd1fc99-7f2d-3e48-87d1-22720549d6a0 | -7.45771 | -41.11435 | 2026-07-28 04:51:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d0058ce-101e-30be-9b65-53499176c7d0 | -3.59763 | -51.47752 | 2026-07-28 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98d192e3-a6a7-3000-bf21-1c8d67b8a332 | -6.87428 | -45.99907 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 060af732-0498-3368-a49e-c7b0f9b0f159 | -2.47979 | -47.08715 | 2026-07-28 04:51:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e8c0857-7e20-34ee-9c39-afae0b5ef279 | -6.86554 | -46.0015 | 2026-07-28 04:51:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6459a53-58a2-31c7-86d4-529bde844c86 | -5.48879 | -44.98294 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34cd97c3-b18c-319c-9e42-37afbb7796f7 | -2.47845 | -47.08801 | 2026-07-28 04:51:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8d0743-e1b2-3383-81f6-8b056f472085 | -5.82427 | -43.48702 | 2026-07-28 04:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76fd6274-845a-3797-86f7-f819cb6ddc1d | -3.67851 | -49.48311 | 2026-07-28 04:51:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a726283d-af2a-361a-b287-3c8598d7cbf8 | -9.36271 | -44.72892 | 2026-07-28 04:51:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c377a548-03b6-32ee-9d53-6919aebda169 | -8.13442 | -46.77911 | 2026-07-28 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b05fd025-f15c-3b85-af68-e58eeed7f5c4 | -7.2983 | -45.28464 | 2026-07-28 04:51:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d64d092-766c-30ea-9e04-68d70bab4bf3 | -7.7223 | -46.5031 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 926ed054-0818-3302-92c3-c827a2f0f078 | -7.72581 | -46.50715 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04b13ae8-4e4e-3b31-b6b8-b1027bbe0aab | -6.8735 | -45.99754 | 2026-07-28 04:51:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69b0e4b8-5b15-3e14-9112-fcc9306bdfb2 | -9.33744 | -47.91967 | 2026-07-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 118e689f-ed13-3a79-8c4b-d185a5b1a5c2 | -7.24089 | -43.14299 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0af5324f-5569-324b-b51f-799fe8f702d6 | -4.01209 | -48.06216 | 2026-07-28 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfda61eb-3452-3836-b558-8d1872cfc366 | -6.86888 | -46.00057 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0d9a4c2-3f1d-37c3-ac92-09a6f8f5ca17 | -1.6728 | -54.46653 | 2026-07-28 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d461cbbe-3ea7-3776-94c8-9c98b996dd7c | -8.87864 | -50.04879 | 2026-07-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08af5dcd-b381-333a-a23e-7fec87a69b52 | -7.83517 | -47.09745 | 2026-07-28 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87c711f0-b52b-3a1b-8926-2206dc7fbb9a | -7.92597 | -55.0362 | 2026-07-28 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8331372-4047-341b-8e61-4695d020da7f | -7.46349 | -41.11508 | 2026-07-28 04:51:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f33ffe98-bc62-363e-b793-c94fd95c6552 | -7.58088 | -49.71766 | 2026-07-28 04:51:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3005172-0e0a-3647-970d-433b473e1eb7 | -5.82352 | -43.49213 | 2026-07-28 04:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f932bb5-0562-3edf-b8e8-896fa6e38af8 | -4.37221 | -47.76841 | 2026-07-28 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9736641a-806b-3e51-9d9c-32f14de70c1b | -5.82462 | -43.48404 | 2026-07-28 04:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 580a594e-a8f5-3d11-9d84-b171631c0d02 | -6.4799 | -42.23169 | 2026-07-28 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 641ae6c6-b734-3d45-be64-25e129c84b0c | -6.87318 | -46.0064 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98fa40a1-99d9-37b5-b247-6bb172390a80 | -5.4901 | -45.1189 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ecb301a-3f9f-3a0d-ac10-1d9cab398274 | -2.4252 | -48.19492 | 2026-07-28 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 487fe0e3-17bd-342b-a3f0-e841f78a1013 | -7.16559 | -59.31937 | 2026-07-28 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89060ac-308a-3191-a550-a88c4de24c8e | -3.67517 | -49.48259 | 2026-07-28 04:51:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08286b9c-0daa-3e52-b1d3-951228770d83 | -6.48035 | -42.22845 | 2026-07-28 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c1e23ce-b0c8-3064-831e-e4663ba1cd9c | -7.83129 | -47.09694 | 2026-07-28 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 767069c9-f759-3504-8910-b758474a0b94 | -5.69922 | -49.22297 | 2026-07-28 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22c22524-e3a9-3af7-98c3-7eab0e5ddb46 | -5.48157 | -45.11774 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 550b4475-0ef3-3ce5-b1fc-f6a339efd037 | -6.86835 | -46.00424 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 05fa4c66-dbcc-3cd4-a23d-38dd5ed61b23 | -6.12586 | -43.76267 | 2026-07-28 04:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 031b7d83-f6a1-30f0-972e-73f8efb1acaa | -6.86909 | -46.00576 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ac7c3e5-ef12-3492-af72-353d74e8e422 | -8.6863 | -49.23922 | 2026-07-28 04:51:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7800c3af-727b-3a53-9c72-66cdfe9aadc8 | -4.94277 | -48.24556 | 2026-07-28 04:51:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README17.md)
