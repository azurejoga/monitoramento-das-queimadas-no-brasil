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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41f06359-c77f-3112-b7ff-51e44bf1ca71 | -6.67358 | -44.69096 | 2025-10-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7086cab-1875-3639-b50e-20a8b75790e1 | -11.36152 | -49.79417 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 91e756fd-cb52-3d23-9eac-460b722b72d2 | -6.46353 | -44.28098 | 2025-10-23 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73ae446b-213a-3382-a8c9-35c120311d6e | -11.28637 | -45.51774 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9201bbfe-b719-33fb-b3a2-97bc39a6bcd3 | -11.99964 | -46.7828 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7e8dc9f-63ee-30a5-804f-efe24fd13bc0 | -6.72164 | -46.52213 | 2025-10-23 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e718ed9-4eb4-38e0-8f6e-94b0bb586d28 | -8.65757 | -44.78703 | 2025-10-23 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc0e353e-645a-3fd8-a388-d78862c9ec3f | -7.3246 | -45.28447 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af64ac7a-c4e1-3997-9e91-1ca2ebf28cb7 | -9.98384 | -37.04312 | 2025-10-23 04:08:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2be855a5-c3e0-3024-95e3-87d117bea5a9 | -11.99669 | -46.77745 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af2d6698-1a7d-3bed-a811-b743f293381b | -11.07612 | -51.56536 | 2025-10-23 04:08:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5667257b-1bc9-32a0-bafd-3ffb14b33508 | -11.12612 | -48.33732 | 2025-10-23 04:08:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e178c5dd-f60e-33af-8408-a6a513dd7987 | -8.62463 | -44.81029 | 2025-10-23 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1b784d3f-1484-3c76-aaf8-fe61f994287d | -11.99588 | -46.78214 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d3a3ac6-1c61-3e28-b2ed-624255ba3747 | -6.64602 | -43.60975 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b29aee7-31f3-3a22-b50f-49b93999203e | -13.01041 | -48.45598 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cae3513-316e-365d-a0eb-53df774aa0f7 | -13.12402 | -48.24395 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fcf6e3b-d9e2-3da9-ac89-4f1db6d77784 | -9.97977 | -37.04259 | 2025-10-23 04:08:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 10873d3c-0a2d-3a03-9e7b-5d816fdc2d2d | -6.90455 | -46.13183 | 2025-10-23 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 669bdb87-a39a-34a5-a8ba-e9e3555ebe18 | -7.63283 | -42.19166 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0925332c-1d6a-3aa3-a04e-d702f5fac5a1 | -9.55859 | -44.87291 | 2025-10-23 04:08:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 491d3ceb-7c52-3d09-a100-0cee7f9f2b35 | -6.32486 | -46.20358 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b35c8537-ecee-3b4c-9bad-3fcc603313bc | -12.90357 | -48.4904 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 053a8e65-fac0-3752-b668-bb64c65fc82c | -12.81585 | -48.63368 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2960fc9-7f89-373a-845d-c4df884f3bb5 | -6.28015 | -47.01443 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 611e612a-e60f-3737-8736-eed75480e25a | -6.64664 | -43.60597 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79455220-0eea-3783-9312-228c05940e27 | -6.83701 | -45.30107 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c6d821-8bef-37e9-8923-91c68002fbdd | -10.02919 | -47.06094 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 325e2a39-7eb1-3982-ae41-c985d2f3da03 | -6.74727 | -44.07397 | 2025-10-23 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 294f8621-9af5-3bb7-85bc-2743f1f64ef3 | -7.88905 | -43.55092 | 2025-10-23 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12e24588-d9de-302d-9628-b20867ad0c26 | -9.5642 | -46.68914 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 461c537b-5dc2-3463-b217-b5270f9686c1 | -6.90844 | -46.1325 | 2025-10-23 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b941ce6-0f85-3013-b1ea-cca4cac3496b | -12.67808 | -48.62577 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 13e4baf7-ce46-34f8-ab76-37fa229a9695 | -13.04973 | -47.21574 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc00ea15-e080-380f-84a1-28ee1c7fd45b | -12.44948 | -48.70868 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| febaad63-4c8f-3a0d-b4de-7a54bbf0b556 | -9.97546 | -47.0705 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d73aef94-31e5-3b21-a261-b49864ef5d2d | -13.2118 | -47.74241 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99a57076-4a73-358f-b695-a1592ce053c8 | -12.78785 | -48.57455 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dba1822-44cf-3a64-b98d-9735717b3af9 | -7.14937 | -42.36338 | 2025-10-23 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e82468f6-d680-3952-b941-d683234d8fe8 | -7.56132 | -47.36417 | 2025-10-23 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afb20870-5466-3cfd-99e2-fc5a30748527 | -9.23601 | -45.60189 | 2025-10-23 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c766dcad-bab6-32e8-b972-8b9107d90400 | -8.16267 | -42.92654 | 2025-10-23 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e4c7909-a574-3206-88b0-d3d2cf212247 | -7.06911 | -45.2145 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d12060-e6a5-3a9e-ba8a-7539077d787a | -7.51797 | -46.88527 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55230fd5-9cfd-3d98-961c-5d960688ec53 | -6.28078 | -47.0106 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf84febe-a8dc-32a0-858b-852be499b71f | -11.35659 | -49.80078 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3b321027-4bcb-3e5d-83f7-363f19955a1f | -11.13033 | -48.33802 | 2025-10-23 04:08:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8ef29bd-a5e1-32dc-9189-c9b2f05038d5 | -7.17322 | -44.78444 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d456fcc-5456-333a-9916-34b9185f9abc | -11.99418 | -46.78896 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b7cd47f-a4b8-3d88-825f-7cc481437c56 | -9.93405 | -47.58712 | 2025-10-23 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1e0c03f-c8da-3aaa-a6d5-fbf524cca6b4 | -11.00813 | -47.67281 | 2025-10-23 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df3e82a6-eb22-3eac-9186-f352724e5e47 | -9.2949 | -40.4462 | 2025-10-23 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 913ecede-77c5-3eb6-85d9-24dd524afce6 | -7.14737 | -45.28482 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 976bc6b0-bc12-334b-9279-a4bd09bd57d0 | -7.84041 | -45.38902 | 2025-10-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e623c359-7e87-35b0-9e04-6e8b1ebf8650 | -8.35091 | -46.18187 | 2025-10-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e3edb19-cc0a-3625-9158-62953dc5dfd3 | -11.36294 | -49.79185 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb9368e8-b245-3d32-a256-212bac790a8c | -9.23674 | -45.59744 | 2025-10-23 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67248781-0d7a-3ecb-8541-20fb385d48c2 | -11.99293 | -46.7768 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a48136a5-1305-3936-aec8-ffcda2ed730d | -6.60107 | -44.21643 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8587ac72-a1d0-37a3-a3fd-77937c2b8c1d | -11.35918 | -49.7862 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 58ef72a8-9a34-35c9-b040-9f9fa9926b47 | -11.99873 | -46.78493 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3350267d-79bd-39e5-9e25-49b8ea9fe335 | -7.1444 | -42.37334 | 2025-10-23 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f5a5cd43-fe53-37ad-9596-a70c71797163 | -6.28976 | -47.00805 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a568f5a0-552b-3082-b6b0-a1578ce9ced5 | -13.37178 | -47.91181 | 2025-10-23 04:08:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18b00efc-7528-3900-ab17-30afe55ac757 | -11.35832 | -49.79103 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7da0f8ec-93a1-3e6e-8400-661344d076a2 | -13.03875 | -47.23373 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c36fede5-6267-35f6-b141-ea8776792319 | -7.14882 | -42.36687 | 2025-10-23 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96e81e06-e5eb-3e52-b5d3-03613085de69 | -12.03228 | -46.61728 | 2025-10-23 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 048c874d-b5ae-32be-946d-86259043c301 | -13.88001 | -43.90002 | 2025-10-23 04:08:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c15c7fc-17ea-3cbf-93a1-ab73a695004f | -7.16927 | -45.17587 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47c808d2-38b8-35e7-9805-19b321464ba6 | -9.96977 | -47.08021 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 914aff46-8e55-383a-ad9f-59305c629700 | -9.45437 | -40.39457 | 2025-10-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 386069d6-133b-37fa-ac24-2d089c0f7ea6 | -11.99212 | -46.78147 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fde34fa9-5c0a-323d-bb27-1fa15aadb7ec | -11.3537 | -49.79021 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30e44a32-5aa5-360a-ac8d-a42088bd7071 | -6.28559 | -47.00739 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dea4dbc6-f739-3bab-9fe0-9da8b81ec1d2 | -6.32486 | -46.20359 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08a2327f-cbef-30ce-ad6c-d88333d1609d | -11.36062 | -49.79905 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 67fff5dc-b6bd-3834-aaaa-f3a76be077fb | -11.00232 | -47.80168 | 2025-10-23 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1bff9e5-2575-3326-928c-4b89d75e3965 | -6.29329 | -47.01262 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d135648-b1f4-34fd-9c6a-e9d26b52f3d8 | -10.91074 | -50.11684 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e86e6b67-cfc1-347b-ac6a-02c98f485f2c | -6.93575 | -43.57849 | 2025-10-23 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82d970e8-dd5b-303b-8396-d02dc3a75a8a | -8.13775 | -44.45965 | 2025-10-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05e8ef66-c793-37d5-9102-7811eb6a716c | -11.3578 | -49.78856 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5546187e-a1d7-3f0e-ba14-aa6e5d7ef0c9 | -9.97941 | -47.07116 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5726831e-7e4d-3ad6-ad55-fea79f6a31f4 | -7.27541 | -44.22015 | 2025-10-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee74daab-0a4e-377b-9d56-93a8514c5b7b | -11.99964 | -46.78279 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8881c7fe-0cc6-323c-ae77-56ae5cde937f | -7.63779 | -42.20312 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 326d7932-572f-38c5-a328-819a678f59fe | -9.93124 | -47.57912 | 2025-10-23 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fe2d3df-2a60-3990-a5a7-d171868636e4 | -11.35746 | -49.79587 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 48ec0808-4337-3141-925b-dc62720a6274 | -11.12119 | -48.34067 | 2025-10-23 04:08:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 810b2263-e652-362b-8496-ab8b2bf3b242 | -6.48561 | -47.50185 | 2025-10-23 04:08:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2291050e-e745-3228-994b-0815b7a7dbbc | -6.90538 | -46.12688 | 2025-10-23 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b28414da-970d-390c-801b-a55ebe3f16af | -6.78689 | -45.44117 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc9ec661-1c01-3715-b502-81f9855cd19d | -6.78391 | -45.43604 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b22db596-b091-3cdc-8fc4-6199fa4d7ba9 | -6.60526 | -44.21285 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d629d3c-6161-3b80-be05-39187fc6f187 | -13.29941 | -47.4771 | 2025-10-23 04:08:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba0ec2c5-943a-362b-a92e-030d2cacccf8 | -13.375 | -46.63998 | 2025-10-23 04:08:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aa91d60-1a7c-3aed-b227-d78ab42c1892 | -11.28992 | -45.51836 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5134e04e-c156-3387-b77b-c08adc785987 | -9.97372 | -47.08086 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| deb07e88-7967-3cfb-b1b4-82bec6e507f2 | -11.14306 | -44.93734 | 2025-10-23 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README12.md)
