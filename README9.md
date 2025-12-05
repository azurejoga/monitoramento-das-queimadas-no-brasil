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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40cda4a2-d836-38f7-a275-c22cab008bed | -3.60557 | -46.00423 | 2025-12-05 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26c758b9-cb15-31d8-8675-72bd7699027a | -5.87051 | -35.37902 | 2025-12-05 04:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8d453486-1d20-352d-ac3e-c67c458275fc | -6.27556 | -40.64344 | 2025-12-05 04:29:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 765e056e-dfbd-348e-9ad7-2934b6fe984f | -3.42484 | -39.26344 | 2025-12-05 04:29:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8d6cfaa7-87f5-304a-99b2-b3dd263e4cde | -4.70239 | -46.42995 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3788f9ef-cccd-3c00-ad7e-fa64e0d59d31 | -6.42738 | -44.78027 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 754b2c82-d33c-35b3-a8df-d39539dace18 | -1.95212 | -46.37953 | 2025-12-05 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5213928a-8165-3074-816a-d669b3664fd0 | -4.73283 | -46.38852 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98835d2c-bfad-31f5-a7df-48e945125010 | -1.17464 | -53.89222 | 2025-12-05 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e1a290b-c165-381a-b8ab-a3cd6c0fcc9b | -4.73954 | -46.49633 | 2025-12-05 04:29:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc56c632-e27c-32bb-a206-f154041db24c | -3.50465 | -44.51934 | 2025-12-05 04:29:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4234fa29-00a7-3e4e-b42f-8804e8b41b77 | -3.34458 | -42.15429 | 2025-12-05 04:29:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0e66690e-7670-30d0-992d-a5b0c2170b95 | -5.00296 | -38.53729 | 2025-12-05 04:29:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a7ea420b-5e71-342e-aa68-c3ebb848731a | -3.07276 | -46.65219 | 2025-12-05 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86f19b08-e707-341d-9a97-a22c69b3f4b7 | -2.40428 | -47.13995 | 2025-12-05 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65e94a75-637f-3006-90fb-1c0a450b976c | -3.3768 | -44.10759 | 2025-12-05 04:29:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3dd2277-95d3-31a9-a1f2-2a3c3aede334 | -5.34823 | -42.11425 | 2025-12-05 04:29:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| edd8078f-87f7-38d1-800c-efb5f836264e | -5.86472 | -39.11043 | 2025-12-05 04:29:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d7a9fa3-06b9-300e-a610-4821674d74cb | -6.18843 | -40.61992 | 2025-12-05 04:29:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32b2dad5-ef34-345c-8ebf-cac7873889ae | -3.5052 | -44.5158 | 2025-12-05 04:29:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aceb15c1-8829-3ef6-8b7e-1cb019cf8811 | -0.782 | -49.16207 | 2025-12-05 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36321ed7-b497-3c9e-8a7c-e7cdf989a14b | -5.12808 | -36.42409 | 2025-12-05 04:29:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ec97e39c-4270-30bd-9abb-9f409178ce2a | -5.1754 | -43.088 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20b5e65f-1117-371b-a9d3-af0bac4c6f7d | -1.12316 | -53.446 | 2025-12-05 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1634d69d-e076-3aee-a724-d3e3b432bd19 | -4.73338 | -46.38506 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5a0e8a2-2449-3a52-bf16-a8c11519be30 | -5.624 | -37.33499 | 2025-12-05 04:29:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b82ba682-c2d5-3966-99ab-dc04093b705f | -5.12865 | -36.42463 | 2025-12-05 04:29:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de055660-5675-3af2-bd0d-922224163c6f | -4.508 | -40.51136 | 2025-12-05 04:29:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05b68f02-e0fe-3a43-beee-a75556900d7c | -1.12319 | -47.73822 | 2025-12-05 04:29:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a543a645-20b7-3365-b0cc-baba4416360d | -4.4183 | -45.31822 | 2025-12-05 04:29:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb3e491-a806-34a4-925d-208948938085 | -5.19079 | -37.63993 | 2025-12-05 04:29:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d4c8a06-b1a2-3109-a2b5-109c52bb90b2 | -6.41946 | -44.78655 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f162ac3-db1f-3ece-aa88-a21352837850 | -4.73006 | -46.38454 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a7a4d3a-1c43-35fe-94b4-ac4fc536f7be | -0.64408 | -52.38561 | 2025-12-05 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0b26f1-9fc4-3382-91af-0cc0f274a1f7 | -6.01196 | -41.13987 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7bf28c7d-2e26-38d3-9e3e-eed7166a5c31 | -4.71465 | -44.45952 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76948b18-c083-3b98-a958-c99d3c8d4b56 | -4.70627 | -46.427 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1878871e-382f-31ef-86f3-ea17928063a4 | -3.0606 | -40.08561 | 2025-12-05 04:29:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc569088-ba7e-31bc-b413-cf5e0d8fcd09 | -4.50441 | -40.50713 | 2025-12-05 04:29:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b38542a8-0605-3bf2-878c-415787bc2388 | -4.98659 | -43.8391 | 2025-12-05 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 376e0754-f611-3acd-87e2-005ecfe72bd1 | -1.45778 | -46.72207 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f555be0-05d5-38d2-8b57-6bc215ebc4f8 | -2.06986 | -45.3566 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af7b51f3-b035-31e3-9569-8f8a7f7bc9b3 | -4.7367 | -46.38559 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8431e566-b8c4-3793-96f0-00a4a01372f8 | -6.00334 | -41.14198 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| cea4a146-84bf-31a8-8cdf-53a58b45b3bc | -5.06511 | -40.47607 | 2025-12-05 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d9321b09-d7d8-3268-9dba-d28d591cdefb | -4.71182 | -44.4554 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e58168b-f570-3281-9f17-705cbf9fce42 | -6.01143 | -41.1434 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4deeed37-a0fc-3edc-8e83-d9751e07328c | -3.37737 | -44.10396 | 2025-12-05 04:29:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1a910f9-66c9-320a-83f8-f787bddec76a | -6.0004 | -41.1295 | 2025-12-05 04:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| d20e0a4a-1cb8-37b4-b7f9-efa8cea0d88d | -6.0002 | -41.1538 | 2025-12-05 04:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 4814dc12-b567-3533-8948-5edbbd2e7ba4 | -11.3617 | -54.33375 | 2025-12-05 04:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 688f8e28-106d-37d4-8028-58b7ba6d0511 | -21.1742 | -49.18137 | 2025-12-05 04:33:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5885bcea-784e-3b88-9e34-8ed13b37032b | -20.91732 | -56.38367 | 2025-12-05 04:33:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 11fc25e6-454e-37e9-80b7-4e377adb74b3 | -21.18467 | -49.20237 | 2025-12-05 04:33:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f8a1bdb-b400-3f0c-a623-689ff843d7c3 | -21.36958 | -48.53709 | 2025-12-05 04:33:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 69bfba34-1722-3823-bc7c-835860b4ba25 | -22.4933 | -46.93999 | 2025-12-05 04:33:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 879f4851-faa7-39a2-add7-15b3ead52d60 | -21.37296 | -48.53766 | 2025-12-05 04:33:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da3db753-1347-3d22-8f89-9935f1342271 | -19.57225 | -50.65356 | 2025-12-05 04:33:00 | NPP-375D | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6acae347-dd3e-3294-9d55-11cc4cf6cf87 | -20.59867 | -51.61155 | 2025-12-05 04:33:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d50a749f-69d2-3706-a29d-dc498e25e921 | -21.85872 | -48.80987 | 2025-12-05 04:33:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11cfb812-9e35-30df-981f-356e8eb4c5c5 | -21.24752 | -49.2509 | 2025-12-05 04:33:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad8954a9-0606-3cb9-97b7-fa2ef31371b2 | -20.87588 | -56.06391 | 2025-12-05 04:33:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40d7a0c1-5443-3e92-aa8b-351b23171a39 | -20.00245 | -55.76243 | 2025-12-05 04:33:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 74b64cb4-b0e8-3bf6-9037-84e2b427ccf2 | -20.92254 | -56.38021 | 2025-12-05 04:33:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6c72a30-3c83-3323-b3d2-74f11c84ebd1 | -22.49391 | -46.93557 | 2025-12-05 04:33:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15a2b68-bb74-3587-9ca9-4d93c587e047 | -20.96874 | -48.76281 | 2025-12-05 04:33:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9b7ff8d8-5099-3bdb-af2d-db8c5cfb3c39 | -21.37015 | -48.53329 | 2025-12-05 04:33:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79e35163-2acf-3ca2-8a80-9ac354aa21b6 | -22.6108 | -46.26934 | 2025-12-05 04:33:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f65c4439-5f4a-3446-ac93-5e271ee9b98d | -21.25085 | -49.25148 | 2025-12-05 04:33:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c2e6158a-0f02-38b5-bd62-f7a35e3fe0ac | -20.96089 | -48.76915 | 2025-12-05 04:33:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 88b68a49-3e0b-380a-963b-d9cb8642bc89 | -21.18133 | -49.20178 | 2025-12-05 04:33:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed6a3156-7046-3285-9c6b-bee5bbdd8ece | -19.99064 | -57.45949 | 2025-12-05 04:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e370096-13f6-3633-b687-882ab2679ed4 | -19.9801 | -57.46267 | 2025-12-05 04:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b3a60237-5ebd-346e-9151-6b9bd4fe136f | -20.96481 | -48.76598 | 2025-12-05 04:33:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 48e40d1f-323b-311c-8b47-f9df259b46c4 | -20.9182 | -56.37923 | 2025-12-05 04:33:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac881cc9-5ded-3c7a-87ed-3a13e9158c63 | -21.04584 | -55.81512 | 2025-12-05 04:33:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df19b661-f335-3060-97d4-c94d08cbb453 | -22.00378 | -49.43519 | 2025-12-05 04:33:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ee493c4-73c0-3be3-82ff-3d1203f4c99c | -21.18409 | -49.2061 | 2025-12-05 04:33:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b661b46-9dcc-3228-b796-04670844c3e3 | -19.99171 | -57.45411 | 2025-12-05 04:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2465363b-adf7-3256-b27e-7f00b7934122 | -21.62351 | -56.13059 | 2025-12-05 04:36:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7de0751-f38e-37be-a831-aeb3127d6195 | -28.20704 | -52.3563 | 2025-12-05 04:36:00 | NPP-375D | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5827bd7c-5094-3ccc-8e5e-fec4bdb7389c | -21.90146 | -57.30434 | 2025-12-05 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96f81b45-fc80-35e2-9b44-463932603208 | -27.01614 | -51.61138 | 2025-12-05 04:36:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 86e4cc12-394b-303b-b0e1-53a73eda5223 | -21.62773 | -56.13152 | 2025-12-05 04:36:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95ddd6e5-e73d-3003-bfdc-4474d9c3bddf | -23.70395 | -55.26699 | 2025-12-05 04:36:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d90ea056-adb3-3cd2-a341-5ccd0dc0e8eb | -22.95407 | -48.70643 | 2025-12-05 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda21331-85ac-3edf-8a1e-10c65fe059d2 | -27.01552 | -51.61525 | 2025-12-05 04:36:00 | NPP-375D | CATANDUVAS | SANTA CATARINA | Brasil | 4204004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd666e1e-f381-3193-923b-c97cae7be18a | -27.29172 | -53.44589 | 2025-12-05 04:36:00 | NPP-375D | CAIÇARA | RIO GRANDE DO SUL | Brasil | 4303400 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3e438c3b-2b74-31e7-8a28-c7193f82980d | -26.93478 | -52.29462 | 2025-12-05 04:36:00 | NPP-375D | FAXINAL DOS GUEDES | SANTA CATARINA | Brasil | 4205308 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a57e3bdb-e0aa-3a75-8f5d-fd52cff5ea10 | -23.60093 | -48.35065 | 2025-12-05 04:36:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2972de21-4f53-35d7-9caf-5ffbde2ac624 | -21.62693 | -56.13564 | 2025-12-05 04:36:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1dcdd26d-b53d-3931-969b-9c4b412a599a | -27.01946 | -51.61204 | 2025-12-05 04:36:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3d79ab5-f743-39d3-a89c-79c8eb480b96 | -26.31485 | -52.01942 | 2025-12-05 04:36:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dbd28d56-679f-3baa-9160-c758ad13ac95 | -23.70497 | -55.26167 | 2025-12-05 04:36:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c3b9730b-507d-3c2c-a671-57518558a53d | -23.60151 | -48.34658 | 2025-12-05 04:36:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f600f18-2981-3851-9e2a-7c64a342b701 | -23.37269 | -50.27964 | 2025-12-05 04:36:00 | NPP-375D | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 14959d08-bac0-3aa4-b5bc-c11809c8d194 | -23.70111 | -55.26077 | 2025-12-05 04:36:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0693c76-2f4f-3e7f-bb57-ab59d5f356a0 | -27.28831 | -53.44509 | 2025-12-05 04:36:00 | NPP-375D | CAIÇARA | RIO GRANDE DO SUL | Brasil | 4303400 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 56fdf200-a318-3357-ab2b-c63328edfad6 | -25.14452 | -49.33987 | 2025-12-05 04:36:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e5c3f0c5-79f9-3de5-b3a9-9f2314ad8490 | -23.60437 | -48.35124 | 2025-12-05 04:36:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
