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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bd9ec10-4970-3084-9dad-19e248fc5d19 | -7.12529 | -47.00149 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5704716-f4b8-327a-a90c-f30ceb29843e | -10.74543 | -44.74563 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b102656b-bdb2-3f41-a649-d59ec154c247 | -7.7936 | -48.30371 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73973226-0f17-3241-b243-5d1fb6b78428 | -6.88442 | -45.55595 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b15a4387-5eee-3702-952d-c02e002ec649 | -8.70305 | -47.90957 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f56bc14-c156-314d-95b6-5b4c8f0c12e4 | -8.33412 | -47.93826 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4112380-f49f-36f6-bbeb-9db2b5502083 | -6.13798 | -41.7116 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2c009236-d82b-3e1c-980b-8ebf61c776eb | -11.03228 | -47.79739 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba8edcd2-4273-3b58-9203-2f180d7b6364 | -7.78041 | -46.49023 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61d011c9-c4de-3fd9-a52f-2f8639f06846 | -4.69968 | -45.83906 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d66bcd5f-e74c-394f-8f74-06c94201b89b | -8.79557 | -42.83046 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e7cee6bd-8733-33cf-a093-2491d0625fda | -9.93858 | -47.17479 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64369d31-1857-384c-9fb0-51a671569e1f | -7.86811 | -44.23923 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96311983-6524-33f7-bc04-e4534746f45f | -7.32823 | -42.47797 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b27ea593-e724-3b48-9bab-33fa0b2a6e27 | -5.81686 | -44.41312 | 2025-10-30 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08bd7308-547f-35b4-bd01-4a37cd48b24d | -7.43713 | -44.242 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1517ca27-5798-3c8e-81fb-9475a1135d5d | -5.53063 | -43.22689 | 2025-10-30 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eff39cab-1cf7-3bd7-9514-9ec10cbaba49 | -5.67435 | -48.81368 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42498dc1-e9fe-3023-8380-1fc816489c47 | -8.88156 | -49.79337 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3a12576-a54e-3fbd-9b7c-f05e72d559d9 | -6.15059 | -41.67138 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2010b5eb-77d5-309d-98de-46d46cde2513 | -5.70683 | -43.1606 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 23bff0be-1100-33be-aa46-fc2adad580b5 | -7.34834 | -43.90232 | 2025-10-30 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc7d24f-1034-3eda-afe2-bd55a0988e2b | -5.75947 | -42.85857 | 2025-10-30 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fa53845-134a-35f8-a328-a881523e2dcf | -7.86928 | -44.23156 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef6e0a67-6ba2-3b9a-a51a-bd7b858731b1 | -7.50684 | -46.26619 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e51a3be-7b39-3575-8c10-30d0962f98c6 | -7.50353 | -46.26566 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd92fa33-711a-30ee-ad9c-385a29832a54 | -7.42631 | -41.8566 | 2025-10-30 04:25:00 | NOAA-20 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c2931c9-8f9c-31d2-93ca-c7ad42ee4f25 | -7.30076 | -44.97196 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 64b032f2-7e15-383f-8585-6daa8d40793b | -6.0698 | -43.07933 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3dfe5245-db84-3539-9c65-cbe56c03148d | -9.85239 | -47.69566 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf950b1e-5fed-33e7-a399-ce05e6617138 | -6.15613 | -45.71581 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35115482-6ad1-394e-bced-ecee83447cda | -10.89199 | -47.59095 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7c701f9-7ba7-3a48-8eca-c9e06f013861 | -8.04933 | -45.18231 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1e04b5e-1812-3a77-b8ee-56c89ae88cb4 | -12.68905 | -48.65426 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2fc225a-0b8d-3e74-8114-9d93b939e35a | -13.70022 | -47.6853 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6e9249f-cb56-3443-85da-8971c9544f07 | -15.38455 | -46.20945 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d9b0c301-daa6-35a8-ada0-a2150c2bfce0 | -12.4943 | -50.56539 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 82500b05-341f-34d8-93b5-66ba58d210df | -15.83891 | -44.36874 | 2025-10-30 04:27:00 | NOAA-20 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a646158f-9173-3b5f-b5fc-bb993e44625a | -12.24393 | -47.93472 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b6fd80e-f65c-37f1-aa9c-fd9a838837e1 | -14.97352 | -43.3894 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a70ff50f-23bd-3bda-908c-d0c8699fca70 | -13.63256 | -47.0516 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 367d8aa8-3f58-3b38-8b66-c2008f6dc8e2 | -12.26766 | -46.76814 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed10d5de-e868-3269-9bfe-d364316190d6 | -13.67205 | -47.16787 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11affe31-c627-36eb-a3ce-24e3ab849740 | -13.43418 | -47.36642 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14daad03-4baf-3672-8b7f-d8673022dc86 | -13.47395 | -47.99935 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 493d2fdb-3891-32d0-b458-6e723e582e18 | -15.01861 | -46.31916 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e558a2ae-e9f7-3053-a03e-9b99f9a51c5d | -15.09052 | -41.99015 | 2025-10-30 04:27:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9e0817dd-02e5-3b13-8282-01e222944089 | -17.40414 | -46.90523 | 2025-10-30 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fe87c9e-aa33-320b-bdf1-33ff5de3950d | -13.35669 | -43.0865 | 2025-10-30 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6a36b93d-df70-348a-a85c-76d51209e4d6 | -12.8832 | -48.63407 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96fbb798-05f9-3687-b607-9fc97d862c22 | -13.67905 | -47.68887 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcd809b6-a0ef-3453-a49a-716bb36485f4 | -14.75397 | -44.96029 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a2a5a22-b42c-3a4c-874c-48da9ff4fbbd | -13.57564 | -47.33076 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b27cd482-6120-33eb-860e-42b8e01aa223 | -12.39479 | -46.82509 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 853ed64e-c083-3cd0-abb3-4ff3de3c88e4 | -13.30656 | -47.70431 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b49ebef2-8d6b-3f1b-8bc3-4e156634974f | -12.2987 | -50.32727 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75d6a842-e5b3-3f37-852b-01381fe41f98 | -19.46794 | -41.5582 | 2025-10-30 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cc5a6a12-deec-30c7-aea3-9eb8d4a5afe4 | -13.93366 | -48.48277 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5adf5fe0-6790-341d-8407-a85a3b8ebeb7 | -11.95687 | -49.94299 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5829f2e-477c-3520-b316-2c3a03e1912e | -12.27154 | -46.76512 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42479c07-9b5d-3388-acab-48241f8aeb56 | -18.04259 | -42.08639 | 2025-10-30 04:27:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4496fc2c-34a3-3baa-bd37-b89e728fa317 | -13.93641 | -48.48689 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b6ffeb1-4a0f-309a-9b3f-7dc458187b17 | -14.83558 | -45.1983 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee8f9437-3a41-349c-8e3b-7df5a46eb76d | -12.6383 | -47.89109 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74527128-1da5-3024-8876-4060cbbf77d0 | -12.48576 | -50.57241 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 25c5a73b-685f-3b54-86ce-e928cf618dd1 | -13.43087 | -47.36592 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b82255e-9557-3b58-b364-0af711f71635 | -12.2253 | -46.47296 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdd203b6-c328-34ef-b467-5a1d07d1ac4a | -13.3735 | -47.38578 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1432b14b-fd67-357d-a5e7-d7032e5bd97c | -13.16794 | -48.44707 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c89611b7-3606-38de-8d7c-4d785113f755 | -14.12715 | -46.38557 | 2025-10-30 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e1e8b61-4225-3bfa-9069-5df054b87c79 | -12.18938 | -46.70486 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f14409a-1125-394c-bc2b-808dcfb8d8d3 | -13.0278 | -48.81022 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f0f4d1c-a22f-3fad-b22a-de4779e84b14 | -19.22359 | -44.93148 | 2025-10-30 04:27:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b2e7842-6afa-300b-977e-736d027d2582 | -19.32908 | -43.05938 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a2d6b7e-f25a-3b00-86bf-d33eccc359c8 | -19.33281 | -43.06438 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 43558be6-6191-35b5-85e7-c3e6425f6fae | -13.32993 | -47.44744 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1ca8072-9976-3705-831f-e3c9db041c2f | -13.21964 | -47.04416 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985acdf9-3355-3bce-bebf-3cffdc1552c8 | -12.86856 | -48.66135 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6280732c-958f-379c-b217-cd3e3fb319b0 | -13.57232 | -47.33025 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71900c12-15dc-387d-9fe6-6e841a4fff80 | -15.62813 | -48.87352 | 2025-10-30 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63694b8b-e35d-39c3-a882-8c7af5f2bc82 | -13.27231 | -47.74938 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98795ea2-8f63-31e8-a38d-a73b5adb8dbc | -14.78368 | -44.35247 | 2025-10-30 04:27:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef8e2e78-c4b6-3e1b-9908-965462a50a7d | -13.65238 | -48.43637 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 828fa744-84c5-3efa-bbcc-2a23aa4e6de9 | -12.29233 | -50.32198 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b2d1dd7-2724-3418-b6de-98aa25802b06 | -12.88921 | -48.6352 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77fbac3e-0b6e-3b40-96e0-9df7bb6b3ce3 | -13.34683 | -47.66391 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2acb007-a753-3486-ac07-a720084c80db | -14.01083 | -48.87066 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23d0e23d-4e28-3a53-9daf-ca8a6a1fa772 | -13.64598 | -46.45815 | 2025-10-30 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a364d0f4-4a1f-3d3b-bb11-7d46a50dcead | -12.39756 | -46.82918 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cbeffa1-7639-302b-ab73-4e0ecaba326e | -13.93823 | -48.45428 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91e0078b-a4a3-3ae3-8d67-052482f3cfb1 | -18.03964 | -42.08904 | 2025-10-30 04:27:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1419bf3b-c42e-3313-9772-87ae2fab7471 | -13.04071 | -46.75268 | 2025-10-30 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ff14368-dabf-3688-952a-29802005afdd | -14.76056 | -44.96562 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54749260-592f-355e-b9a0-ff6f9b34fc61 | -13.23228 | -48.55289 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8731842-3b3e-3dc8-9ec8-9087c54ac3ce | -14.90378 | -43.09853 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64ef7ccb-4075-3c0b-9e25-b4468dfe73e9 | -12.50569 | -50.56313 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 705d5016-5d6e-349b-96c6-3ae96e9c48a4 | -13.37461 | -47.3787 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cab010ed-e2e2-3a1b-b396-8f90b191a702 | -15.06572 | -41.97799 | 2025-10-30 04:27:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 330913d5-2219-37df-947b-3347507cd5dc | -13.30932 | -47.70838 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 490551a5-34ca-39a1-9d9c-fb8ec990e1af | -15.27241 | -43.06544 | 2025-10-30 04:27:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README55.md)
