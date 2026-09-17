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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca7321a3-a096-313d-bf76-9a64d7eb0403 | -12.7515 | -51.2639 | 2026-09-17 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8d7861ff-a98d-33c3-ae8c-4237ec6dbf8f | -8.8647 | -45.8693 | 2026-09-17 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 39941083-6e07-3d15-a089-de409e216495 | -12.5493 | -50.7546 | 2026-09-17 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| dd6ab098-2bba-3956-95b6-848298687227 | -8.4982 | -57.6468 | 2026-09-17 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 172.7 |
| f5fe82b0-472a-3825-a97d-f00e9c705097 | -7.0084 | -43.6497 | 2026-09-17 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 66f17b83-9109-31f0-9bfb-e8f33a64e777 | -11.3437 | -44.0141 | 2026-09-17 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 186.0 |
| fe7d76fa-9319-38ac-8e75-4baa0e7bf02b | -7.4492 | -44.5786 | 2026-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 32482cb4-a60c-31b8-a1da-55eb76fa075c | -9.3803 | -46.8455 | 2026-09-17 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 02713513-4fea-3f9d-989e-390e02f6bf60 | -9.852 | -46.9046 | 2026-09-17 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 90791651-5c95-36c7-a6d8-619cf991f946 | -7.3669 | -38.9584 | 2026-09-17 14:00:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 181.6 |
| d40c4e65-45c6-310e-9759-ddb7cb046701 | -12.7243 | -48.2734 | 2026-09-17 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| efd12c51-c9b5-3e20-90b4-505fcd15222e | -30.6109 | -53.0283 | 2026-09-17 14:00:00 | GOES-19 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 277.5 |
| 58ae4fbe-e12f-3052-93bf-e50cc8cd87bd | -7.1381 | -42.1768 | 2026-09-17 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| f5088d9a-6d8d-3d5f-bb04-fbffad8c46d3 | -10.0612 | -45.5504 | 2026-09-17 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 2b7075a7-4f41-3713-9576-c1412844a1f9 | -8.4796 | -57.6478 | 2026-09-17 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 9439526b-41e4-36c5-a37c-007365452ca1 | -13.6531 | -45.97 | 2026-09-17 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 545.6 |
| b49a1116-839a-3128-bb12-be68ad7c6113 | -8.4983 | -57.6271 | 2026-09-17 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 152311e1-a6a1-3a44-9c97-1ad32c2d92fd | -4.5044 | -54.9845 | 2026-09-17 14:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| ff0bf88d-0467-315e-a0e4-18804c417fe5 | -7.8033 | -44.8651 | 2026-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 86a434d6-0b30-3151-baba-fd78308baecf | -14.1742 | -45.1407 | 2026-09-17 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 8007b0ae-848e-3729-8e77-88ce488544f3 | -13.3758 | -57.026 | 2026-09-17 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 292854fb-cc7c-3d78-ab89-48090c3aa4c8 | -11.3442 | -43.9906 | 2026-09-17 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 04fd865f-dd38-3567-ad99-4d04b519e493 | -15.552 | -54.2255 | 2026-09-17 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9c515d04-68c1-37df-83e4-521bbb8b2f2a | -10.8308 | -46.1569 | 2026-09-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| d8a25242-ab49-30a8-90c1-219abe55bfa4 | -14.8376 | -59.5515 | 2026-09-17 14:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5f4c9787-5317-3f73-b53c-5902513da380 | -11.738 | -50.2295 | 2026-09-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f4188b3a-67ff-31e0-90d2-995f599e0bdf | -10.8919 | -54.0062 | 2026-09-17 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| a86f0bfe-57cb-3e12-8c1f-4ea64df664ab | -11.8924 | -50.0823 | 2026-09-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9877d3bc-f7d1-3a33-bae9-f8d37864a801 | -8.8737 | -62.3925 | 2026-09-17 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 57543986-4ea6-3a80-9670-b0c93a368f4d | -12.7518 | -51.2426 | 2026-09-17 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| e3fe9621-3c0d-3cba-9754-56f638f3117e | -13.6526 | -45.993 | 2026-09-17 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 218.3 |
| a5a7bae2-3801-3f71-b419-c49b33a5233e | -8.4797 | -57.6282 | 2026-09-17 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 8393c962-8a46-3a29-9000-01cb899decaf | -8.9108 | -62.391 | 2026-09-17 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 997c2061-6fca-33f8-a139-a316fe3d7c54 | -12.7051 | -48.276 | 2026-09-17 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7efcc6e2-8552-31e4-b83e-281f0758cbdb | -7.0804 | -47.5031 | 2026-09-17 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4faec0ec-43fc-3596-84b5-7ab360e4a92b | -15.5715 | -54.223 | 2026-09-17 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 7e6e22b9-c0b4-30a6-9af8-993fd4035901 | -11.8928 | -50.0608 | 2026-09-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f8f8f78d-b300-37e0-b430-22660b93a750 | -10.8118 | -46.1594 | 2026-09-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 34c5dc22-7765-30d1-a7a4-a0c599213796 | -12.3085 | -47.9539 | 2026-09-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1067c268-add5-3234-870d-869f2d756e82 | -7.6402 | -44.3303 | 2026-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 392cdfab-927f-34e5-b74e-974da410fa3a | -11.8941 | -47.5876 | 2026-09-17 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f388f8fe-7ee3-364c-8ffd-85b71dc7afbb | -14.5709 | -46.5941 | 2026-09-17 14:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 902ed033-33c5-3080-bb96-960d7dc144fd | -7.0262 | -42.0685 | 2026-09-17 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| da48620c-1492-3b19-877e-ca6f9a4868f2 | -7.8221 | -44.8632 | 2026-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5bc0c108-aee6-3d16-b8f5-5d7804982dcf | -18.8906 | -46.8284 | 2026-09-17 14:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| aa9c1a87-66a9-31a6-8ada-70ecd7866fb7 | -7.0451 | -42.0666 | 2026-09-17 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 163.1 |
| 34e268f9-0281-3a68-b83e-e38ffa78dfc5 | -10.0418 | -45.5756 | 2026-09-17 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 613f1296-d205-3459-8c5f-363bfb9828d7 | -9.7608 | -60.4561 | 2026-09-17 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 37b54b7a-1786-365e-af2a-89f7ce29c7bc | -11.8069 | -58.1759 | 2026-09-17 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 941ec8a0-4c2a-3831-9cba-2120e5a94656 | -12.49 | -50.8901 | 2026-09-17 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5b3a6400-292a-3668-be39-2b588997dc2e | -9.5512 | -45.4296 | 2026-09-17 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| a5980110-b666-37ab-a666-9255c755bf26 | -11.3446 | -43.9671 | 2026-09-17 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d807b1e3-c4ab-355e-932b-8db52e40f5bd | -10.8312 | -46.1342 | 2026-09-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 42b3188a-257b-3888-98ce-d472c81f8d80 | -14.1547 | -45.1442 | 2026-09-17 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 8a53d5c5-5931-3721-8108-85347f18303b | -7.6381 | -46.1478 | 2026-09-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 14206faa-d361-3bb5-9eee-72f25fd3d51f | -9.7497 | -46.1089 | 2026-09-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e580b549-77f2-3b68-8afd-884562c22d71 | -12.7894 | -51.2807 | 2026-09-17 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 5743bb28-e477-3e82-a00f-b51124d46686 | -7.3669 | -38.9584 | 2026-09-17 14:10:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 214.9 |
| 4b3d8069-8e8e-3866-b49f-4c58bb200d26 | -13.6143 | -46.9561 | 2026-09-17 14:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 824c3778-ec85-344a-887a-15cb1a89fea9 | -13.6526 | -45.993 | 2026-09-17 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 324.6 |
| 36866774-369c-3b36-a75b-9a5da3ee51b2 | -9.8508 | -48.3615 | 2026-09-17 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 945646f6-2cf8-3e3d-bf3f-7282a2f28328 | -8.8644 | -45.8919 | 2026-09-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 85fedbba-7035-3b93-b7c1-71a698c52106 | -7.0454 | -42.0427 | 2026-09-17 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 9a64f5e0-422e-32c3-b24e-43ee94f5f3fd | -6.9896 | -43.6514 | 2026-09-17 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| d404affb-7b7e-3b91-b2c3-aeb4c13a0dc8 | -9.8694 | -48.3814 | 2026-09-17 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| eb97d95d-e8f5-3c61-a1d5-b475e5821d56 | -15.4623 | -53.7972 | 2026-09-17 14:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0450b777-9397-3e79-a18b-f584f0e58075 | -8.4796 | -57.6478 | 2026-09-17 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| edb8a8ea-27cf-30d1-a9ee-fde48a325eb7 | -7.0617 | -47.5046 | 2026-09-17 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d73cd1a8-745c-3b07-8eb9-34f6957af232 | -12.7243 | -48.2734 | 2026-09-17 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 82835ae6-147e-3f94-8e78-2b4bc07d0385 | -7.0084 | -43.6497 | 2026-09-17 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 384e0a26-da3a-33ec-b82c-e6d247ed3473 | -12.7051 | -48.276 | 2026-09-17 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e54ab30a-295a-3d41-89d5-2aa314f5a376 | -9.7793 | -60.4744 | 2026-09-17 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 9704e11a-0106-38ff-bb01-f9a003e0f3f0 | -10.0422 | -45.5528 | 2026-09-17 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| c36b3748-17ac-34fa-a334-d8832fb62685 | -13.6531 | -45.97 | 2026-09-17 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 701.1 |
| 345dd8bd-595b-37c8-a679-25666b6c1005 | -10.0612 | -45.5504 | 2026-09-17 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 8eab4afe-7836-3882-8a17-fdafb7416b89 | -8.4797 | -57.6282 | 2026-09-17 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 52628d66-debe-3909-8fdb-524c24e0db17 | -13.3758 | -57.026 | 2026-09-17 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 5f4d3e18-e2c2-3fa9-bc9b-9825aaa1155f | -8.8642 | -45.9145 | 2026-09-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 001c6154-c873-3ee9-a5be-16748fd7b006 | -7.0112 | -43.393 | 2026-09-17 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 92d004db-2eb7-3c76-83ac-b88713114864 | -10.8308 | -46.1569 | 2026-09-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 68498fb4-6fba-357a-8909-a10bc00780f8 | -7.1192 | -42.1786 | 2026-09-17 14:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 110e0199-ce4f-30fc-8a26-f57942ca21a3 | -11.3437 | -44.0141 | 2026-09-17 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| c69e0fe5-c34d-38ff-884f-4061aeeae9a2 | -7.8221 | -44.8632 | 2026-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 262.1 |
| c7b4658e-37c9-391c-9347-37340624cc61 | -8.9107 | -62.41 | 2026-09-17 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 184.1 |
| 1585e313-d616-3c13-9613-7da41fb7da9d | -3.2028 | -53.9427 | 2026-09-17 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4575f1e4-41f3-3773-88b7-904ea0c7320a | -14.1547 | -45.1442 | 2026-09-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d8adb1f8-966f-393b-bd17-83172808dc35 | -7.1381 | -42.1768 | 2026-09-17 14:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| baa27f8c-f48d-358b-95e9-da710aec4ebd | -9.852 | -46.9046 | 2026-09-17 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| d2be3005-ccfc-397c-9a17-3ef275a34cda | -11.8941 | -47.5876 | 2026-09-17 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| bbb360f9-e25f-3f44-ace6-54fa89a1dedd | -18.8906 | -46.8284 | 2026-09-17 14:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 7b258440-e11d-32a7-b346-ee719df5f68e | -7.6402 | -44.3303 | 2026-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| b0268e84-0a9a-3baf-b1e9-23a4e1771474 | -7.0262 | -42.0685 | 2026-09-17 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 4fdeaeb2-39e3-3c47-91aa-6a7f87cdcbc6 | -18.8899 | -46.8519 | 2026-09-17 14:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c91c77f9-41dd-350c-a448-10331293c203 | -9.1711 | -49.9835 | 2026-09-17 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 74baa2d2-063c-3d1b-b32b-2cf8bb1799e4 | -8.8647 | -45.8693 | 2026-09-17 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| ed608fda-ec75-31fa-aa98-63395e6ce45e | -8.1124 | -54.8073 | 2026-09-17 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0509e6b1-56ab-3baa-aa73-9ca4e0bb16c4 | -11.5811 | -46.8919 | 2026-09-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 358bf4c2-9e74-3d1e-bbf1-d46961c2ecbb | -7.0265 | -42.0446 | 2026-09-17 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 39be16c8-9766-311b-8abb-24c1213109dd | -7.8033 | -44.8651 | 2026-09-17 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 315.6 |
| fd13ca45-f2b7-36e7-a590-e4280d83a756 | -11.8924 | -50.0823 | 2026-09-17 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |


[Clique aqui para ver as próximas entradas](README92.md)
