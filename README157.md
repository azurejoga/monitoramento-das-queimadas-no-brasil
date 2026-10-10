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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b03b3a85-8a3d-3377-b794-2c9d69364b13 | -11.3875 | -55.1656 | 2026-10-10 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 3fb4c3a3-591b-3a0a-a42a-0259e5df0c7d | -11.8595 | -47.3694 | 2026-10-10 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| fe1c64ae-f486-39cc-bff0-55c06e12d012 | -12.4837 | -51.2959 | 2026-10-10 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 472317df-2581-30c7-abf1-d10f1a7c0ce5 | -10.454 | -47.191 | 2026-10-10 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bd2a0082-ace5-393c-a6a5-6820c287db83 | -11.2853 | -45.1832 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 1408e961-75a6-3870-b957-b675db9d2e52 | -11.2083 | -45.217 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8dcd869c-8358-33da-a52f-430bd86f295f | -7.8798 | -49.817 | 2026-10-10 13:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 331e4e98-7a5c-39e0-b074-3439c87123ab | -12.1729 | -44.7983 | 2026-10-10 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 6b216b65-679e-3d87-b54c-a21b55d15180 | -11.6951 | -43.655 | 2026-10-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| fef0ce42-c043-30dc-8bbc-affd45aa69ce | -11.1873 | -45.3347 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| c73d7799-8b79-3926-afcc-f4c3570b174d | -8.9275 | -45.4094 | 2026-10-10 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| d4affd3d-5bc7-3689-8649-9ad2b87f5d88 | -10.9197 | -45.3712 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 1c3baafe-e67a-3721-99f8-e0daa2037cdd | -11.5793 | -43.6965 | 2026-10-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 340908fd-1975-3145-81f5-818f72a8048d | -7.88 | -49.7957 | 2026-10-10 13:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ca666009-2504-3620-8436-6ca7943fb328 | -11.7772 | -45.4806 | 2026-10-10 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 41119392-cca9-3c8a-bb9b-3881f4c28d08 | -9.9194 | -44.8815 | 2026-10-10 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 60ad31b3-3cf8-3909-b376-021c8b92e028 | -9.1009 | -45.1622 | 2026-10-10 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| df5b61e8-2c98-381c-bd9d-114042176d20 | -11.0933 | -44.1209 | 2026-10-10 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2a6043c5-b0e8-3f9e-bc01-3c8d909aee67 | -9.9381 | -44.9022 | 2026-10-10 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 716096ec-0142-3dd9-9dab-50d62b7dfe5a | -13.1827 | -54.3571 | 2026-10-10 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e3ffd189-10dc-3be1-b130-a565033a7f1e | -9.1924 | -49.7678 | 2026-10-10 13:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| bfe51fed-cff6-31b4-a8a3-611a3f7c42aa | -10.9388 | -45.3687 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 52918ae6-4930-3e74-b8e4-388f1077d4aa | -11.2064 | -45.3321 | 2026-10-10 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 26bb7f2e-1028-31d1-95b3-132e3f1106be | -12.1861 | -48.4124 | 2026-10-10 13:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8ece333a-cd5c-305a-bc69-0faa381bddbf | -12.2123 | -44.7457 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 8261119b-8135-39f8-810a-bb0a31345eee | -7.8372 | -45.181 | 2026-10-10 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 96de2353-c77c-3ac0-a641-a9e7ae2ebf33 | -10.4144 | -47.3069 | 2026-10-10 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 88cf2c7c-394b-33c3-9250-58afdfd72ae0 | -11.2083 | -45.217 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f10bd2d4-30a5-3162-9426-19b528bc635e | -9.1924 | -49.7678 | 2026-10-10 13:50:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| aa9a1bd4-f52d-3743-8d67-261b9866acbc | -11.5793 | -43.6965 | 2026-10-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 2c5b48fa-9186-30f0-85c7-0b678d2bb717 | -14.9757 | -41.6952 | 2026-10-10 13:50:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 216.0 |
| dec2d896-96f9-3ad6-8d81-a4f88ad0fe9b | -15.6892 | -43.8327 | 2026-10-10 13:50:00 | GOES-19 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 1b346222-457e-3445-befd-b9d3558da43d | -8.3014 | -45.7019 | 2026-10-10 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 2c35a422-965b-35e4-b668-c05ea35ee851 | -15.0233 | -41.362 | 2026-10-10 13:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 129.2 |
| b2b8f1ed-f0ab-3513-9c23-f0e35e2a4b6d | -12.1861 | -48.4124 | 2026-10-10 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 70ad098d-f5f6-3db6-a675-0a31df3cedf0 | -12.1926 | -44.772 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 299c56a3-c42e-3e7b-b90f-a1612055dc8d | -11.4055 | -50.887 | 2026-10-10 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ee65d2dc-a8ad-3ae8-9f83-4bd20ee9c106 | -7.8798 | -49.817 | 2026-10-10 13:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 5c496fa4-2e1e-3387-928d-d38c51a58033 | -9.9381 | -44.9022 | 2026-10-10 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 046ba343-638d-3a9f-8c92-c7ea87004e7e | -14.9763 | -41.6703 | 2026-10-10 13:50:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 149.9 |
| 4d8e7887-d476-34fc-b881-76ab89f817ec | -10.9796 | -45.2026 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 9dae2c6f-9ca8-3b0b-a937-fbfe55fc3182 | -13.1827 | -54.3571 | 2026-10-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| cd8cad51-3d11-3a9b-916b-2a08341e3efd | -12.0063 | -43.4402 | 2026-10-10 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e10c1d38-dc6c-3549-865b-ea48d24f1621 | -9.9208 | -44.7893 | 2026-10-10 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| ae4dcb26-3411-3a3d-af6b-81c04d09cbec | -7.7779 | -42.3246 | 2026-10-10 13:50:00 | GOES-19 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| af44b216-b5f4-316b-bc70-b1118de10de9 | -7.7782 | -42.3007 | 2026-10-10 13:50:00 | GOES-19 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 3de8dae7-806b-3901-ba36-3168fcccbabe | -11.2853 | -45.1832 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.1 |
| a10c6f79-18d9-35c9-a049-9809fd6c9a00 | -11.0379 | -44.012 | 2026-10-10 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| eb76c4f5-aef4-3891-8113-73eec6aa8bb5 | -11.6951 | -43.655 | 2026-10-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 65a66b2d-b929-34ea-9b88-e165c09cc629 | -13.7851 | -48.1195 | 2026-10-10 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1c23c21c-b3af-337d-8fbf-04c541bac7c6 | 2.727 | -60.2586 | 2026-10-10 13:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 91972598-7fa9-3d16-bedb-2bb0b79a328b | -11.7776 | -45.4576 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 816b0750-5b51-3c1c-9597-deb5423a3eab | -12.1733 | -44.775 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 4199972c-aeed-3796-b60b-2d59b327c7f2 | 1.6754 | -55.6266 | 2026-10-10 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fb51a412-6577-3af0-bf52-5387c19a01b0 | -11.1873 | -45.3347 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.8 |
| ce7d675d-9561-3d3d-bb52-4faf6d0b71ca | -13.7847 | -48.1418 | 2026-10-10 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 7ed3fa88-5d40-3510-be7a-fb86a6a4d2b1 | -9.9398 | -44.7869 | 2026-10-10 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 223.3 |
| b45340da-9c54-319a-a02c-8854d9ade8f9 | -9.9211 | -44.7662 | 2026-10-10 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1f949e13-5802-36cc-ab39-e1850d1e7a3a | -13.1636 | -54.3591 | 2026-10-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 3c2169a7-826b-3b49-a8b4-55b7c8d3d317 | -10.4147 | -47.2846 | 2026-10-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8ff4c252-a46b-3138-9b2f-8ba20c4f07e2 | -11.3865 | -50.8891 | 2026-10-10 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 38923302-e4d0-358e-8454-f3cb7c216393 | -10.4914 | -47.231 | 2026-10-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0fe7553c-c9a1-33b0-b1c8-18ce3ef0a8ad | -9.9384 | -44.8791 | 2026-10-10 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 310.9 |
| cb3b7583-6707-3857-9b7e-ad3125c7069f | -8.7075 | -44.9086 | 2026-10-10 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 7371c5c1-bc5b-3786-86c3-253a37a2e972 | -10.473 | -47.1887 | 2026-10-10 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 43bd14bb-1bcd-3cfe-a68e-5288a1691967 | -15.043 | -41.3576 | 2026-10-10 13:50:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| 6c125fd6-cf55-3b4e-a997-49e04a2e8abe | -17.4575 | -45.075 | 2026-10-10 13:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5c1ff8c0-1cce-324c-b96d-1e068ae0d694 | -11.2849 | -45.2063 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 1fa181b3-0fc2-394c-a203-35ac3bc5d1e8 | -13.183 | -54.3365 | 2026-10-10 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| d008711e-56b4-3035-b373-81acc4bb973d | -11.47 | -43.3824 | 2026-10-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| a6ad5170-a4d0-32e7-9723-ce40b08b0da1 | -12.2119 | -44.769 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| e75006fe-2243-3cc2-8b64-8f15299a14a9 | -11.2068 | -45.3091 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 02ce2d33-769d-3d8f-991c-f10d41adeec3 | -11.8787 | -47.3668 | 2026-10-10 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| b04ae1cc-0a05-39c1-8d30-67f735a973c6 | -9.0944 | -44.266 | 2026-10-10 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 7e5616a4-3f16-3d61-b046-1ab30d563686 | -11.8696 | -43.5568 | 2026-10-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 6f470aa3-a7be-397b-b71f-b7fadd71647f | -11.0745 | -44.1003 | 2026-10-10 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| b41eaf38-e4e5-340e-b21e-e2edd8e0f986 | -12.1729 | -44.7983 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| c02b689d-72c2-3f74-ab3e-1db1d6379d93 | -11.1876 | -45.3117 | 2026-10-10 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| bddca008-9d4d-30a9-b189-ad3947b5c650 | -11.7772 | -45.4806 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| e42c124c-c9a9-3a73-82d5-38f7805107d4 | -11.7742 | -43.5245 | 2026-10-10 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 1e097ff5-5efb-385e-9f4d-d0fc863bb62c | -12.211 | -44.8156 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 1003bd17-1aeb-3137-a388-8f143cbb3a83 | -7.88 | -49.7957 | 2026-10-10 13:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3a887a8b-2c9e-3348-9acd-5e68581425eb | -12.2127 | -44.7224 | 2026-10-10 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 309342c0-06b0-3436-8cde-4b84da98112b | -9.9395 | -44.81 | 2026-10-10 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4a209562-c8ec-3b63-b8ab-f1058b84cb96 | -11.5121 | -47.6155 | 2026-10-10 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 8d73f5d7-f0d2-3667-abf1-98f8fb7350cd | -12.1926 | -44.772 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 68df266b-ae1c-3987-b7c4-b730aee8400a | -11.8696 | -43.5568 | 2026-10-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| d84df35c-115f-3e52-bfef-4d31be6b88a3 | -11.0379 | -44.012 | 2026-10-10 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 306.2 |
| 1064035c-24c6-3fd7-8631-b32050b2d5c2 | -7.8798 | -49.817 | 2026-10-10 14:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 72f8ef8c-331d-3f00-a96c-ac3b69190575 | 1.6754 | -55.6266 | 2026-10-10 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bd5804e1-2b20-3426-be62-0753ef55d7d1 | -8.7075 | -44.9086 | 2026-10-10 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 20b754d0-abe3-30a7-a371-736456cb31b7 | -15.1088 | -46.9343 | 2026-10-10 14:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| d701c3ab-4b19-3242-abed-b70e9bf7de16 | -10.4147 | -47.2846 | 2026-10-10 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 20114c53-1d5b-308d-b112-2b7c289c87f6 | -11.8495 | -43.6072 | 2026-10-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 0bf71da9-d690-362a-8eb7-5fa9a5764342 | -12.2114 | -44.7923 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 298ed14d-c221-3b1f-a761-83a04adbfba6 | -15.0233 | -41.362 | 2026-10-10 14:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| 3b0cbe88-4878-36af-9451-a07cd2ca8aaa | -12.0507 | -47.3658 | 2026-10-10 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 42401bd7-83fa-3c27-94ce-b4851164699a | -9.9395 | -44.81 | 2026-10-10 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 3b42f27d-93ff-3d3e-9dd2-af28f8a95fbe | -12.39 | -46.5761 | 2026-10-10 14:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| cfa9440d-c6a6-33ab-82d6-fff36c00d9f5 | -12.1627 | -45.3547 | 2026-10-10 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |


[Clique aqui para ver as próximas entradas](README158.md)
