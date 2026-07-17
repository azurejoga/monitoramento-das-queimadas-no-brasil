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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c594e19-c0ca-3a8d-9f09-f7ab2aa4214e | -3.98549 | -47.93245 | 2026-07-17 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64b6db54-161d-3231-81ce-754a699a23fa | -2.46263 | -48.50106 | 2026-07-17 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 663b94dc-c93c-3a05-abdf-1354dbcca439 | -5.60592 | -36.86689 | 2026-07-17 04:36:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fc3c448-e960-3719-8b71-0dbff8bf8df7 | -5.80438 | -43.6352 | 2026-07-17 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f86a98d1-06b4-3e57-ba59-9b2ce45103cd | -5.79314 | -43.63755 | 2026-07-17 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66209857-15c4-3813-a456-589524fa1b16 | -4.46882 | -42.30745 | 2026-07-17 04:36:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| adecf87d-bdee-3d5c-84fa-1d93e80eba4c | -3.1465 | -48.15011 | 2026-07-17 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4da48894-0b89-33bd-8223-fa504511fc63 | -9.00322 | -47.99738 | 2026-07-17 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c52a7f0-983b-372c-8730-f81d300c1e44 | -10.863 | -46.51025 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bef25b70-a81e-376e-8e7a-f917181f569d | -9.56841 | -48.67155 | 2026-07-17 04:38:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76a89e65-4930-3e6b-8050-78680ed2dcf7 | -10.03651 | -51.66711 | 2026-07-17 04:38:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b7b68a5-3ecf-3bbf-ad57-cb7a27f8a917 | -12.68625 | -48.21046 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59820d4b-e67a-3acd-8883-3d8e21c65fa4 | -10.81916 | -47.39332 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b37a44e2-a289-3f8a-9cc0-79e5d83adc05 | -8.50781 | -48.07467 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bdbf06f-b75e-369f-8012-ace4435089a3 | -9.90741 | -53.37235 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f86975b-7170-3c58-8021-f05c37944ff6 | -13.28258 | -45.20556 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaa12f88-590d-3e58-b834-3b712c9dcb6f | -13.43685 | -43.86097 | 2026-07-17 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a0d26c86-48fa-3b4b-a389-398f49760939 | -5.89718 | -46.20781 | 2026-07-17 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ee15af6-8522-3c93-8b38-673e6d97699a | -9.67651 | -47.89595 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1099f93a-cabe-3442-9d31-18eaf74f5175 | -8.50723 | -48.07826 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54d2bd8a-4938-33d9-8470-3921b370c48c | -10.8363 | -46.57188 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93ef8f64-ee4c-33fe-b6de-3d1b4dedecd6 | -10.81862 | -47.37524 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec4abb23-17a7-3d9d-8162-8ea60b560627 | -12.44081 | -49.57528 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2792c5fa-df52-3c06-9498-65287587f5e5 | -9.6981 | -47.69737 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1584844-6b43-3cb5-b23d-411ce1949856 | -10.85965 | -46.50972 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b02e63b-88b0-3849-b229-61ff390dbcdc | -9.56503 | -48.67099 | 2026-07-17 04:38:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7ce7461-2513-3370-a76d-f2d55fb7ccd9 | -6.25628 | -49.876 | 2026-07-17 04:38:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e32d2959-a015-3296-8d8c-1e6a73c48143 | -12.66292 | -48.2284 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 035c909f-d2fb-3abc-8cf4-00309a44cb9d | -7.9087 | -48.25832 | 2026-07-17 04:38:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0b3c142-2f95-3927-899c-8c7def286839 | -10.04505 | -51.66362 | 2026-07-17 04:38:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ae498c6-a0d3-3e1f-9034-6f1bb1d40a39 | -7.73052 | -44.56144 | 2026-07-17 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2967894c-ca33-35d3-a51f-2a1db28f5c9c | -12.11211 | -49.94203 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 734c5f6d-397d-33a5-83c7-c13d7b47b088 | -7.29198 | -46.25032 | 2026-07-17 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c715e7e6-5cc5-3837-8154-7f683222189c | -13.44066 | -43.8617 | 2026-07-17 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e7949ebd-e002-30e6-ae65-10dc6c290560 | -8.5056 | -48.06699 | 2026-07-17 04:38:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 146cf622-1e52-3de7-9b15-9718db754fe3 | -10.81922 | -45.13759 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0179fcf-f9bb-30f7-89b2-b3de414dca24 | -12.69782 | -46.51067 | 2026-07-17 04:38:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b468f95-bfa3-3c08-b184-ca0f2335459c | -7.83578 | -47.1069 | 2026-07-17 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdec4147-0cfa-3833-94bc-4a782d3c6131 | -10.82137 | -47.40088 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c33767c-c634-3527-b0ca-21d9d28c54a5 | -13.25258 | -45.11237 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| eeaff818-c395-3b8e-a2fe-55f0503abd0e | -10.82172 | -45.12903 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7c115d9b-177d-39b9-957c-dccff0fc39e7 | -5.9121 | -46.67153 | 2026-07-17 04:38:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99dbfefe-3a35-35a7-84a3-488b080d522d | -10.81513 | -46.57575 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59cdd213-4d79-324f-b6f2-e6e4f86790de | -12.11557 | -49.94263 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2d834063-e9c5-3f80-bdf9-7fef1d0d4ffd | -9.85853 | -40.29873 | 2026-07-17 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e0ec9c7-ff7f-36fa-987a-483aa6711f41 | -10.82229 | -46.5294 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e89e401-ae1b-3ea6-a3d1-2857ff9ed0fc | -12.65797 | -48.21669 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b197a74-fd86-3040-a7ac-b484d661d995 | -8.7326 | -48.06681 | 2026-07-17 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39ee4eed-3914-3a45-be91-1af2bd7667f5 | -10.85909 | -46.51329 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5985e98c-b318-3645-8a67-696d9dc351c2 | -7.29429 | -46.25108 | 2026-07-17 04:38:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c77e9d49-5211-3b0e-8eb9-7f1c5e71575f | -11.64749 | -48.50547 | 2026-07-17 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 036e2742-2d71-3bdb-a851-f99a02462b17 | -11.76463 | -49.07657 | 2026-07-17 04:38:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d07349ef-79b4-31a0-b619-e6ca53bcc833 | -12.68349 | -48.20638 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2ab10d7-e4e4-35bc-9559-762eb785ca13 | -8.65767 | -46.96414 | 2026-07-17 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3047b0f7-5939-3025-b729-d255736fff6a | -12.11362 | -49.94134 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c64d5c4e-1670-3bca-a7da-a9203f6a2013 | -9.91124 | -53.32641 | 2026-07-17 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35c8dcbb-a59c-3023-aca4-a37abe68ccb2 | -10.82119 | -46.53653 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2f8e48a8-6403-32b0-a36e-da28c88686b2 | -10.81633 | -45.13314 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| da7f1600-79f9-3b84-b055-4820d64916bf | -10.81765 | -45.13236 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d13c92c7-d0db-3ab7-abda-9bf1565ecf85 | -12.45601 | -49.58937 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e53f9ef-da2a-3eea-beca-f72c4976f440 | -9.00208 | -48.00446 | 2026-07-17 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa300226-4a1b-3bcf-8438-923019d489dc | -13.24542 | -45.11125 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a06b46de-1a48-3da1-a07b-995e96f0f83b | -11.64415 | -48.50491 | 2026-07-17 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e55f9dd-6df8-383f-8f37-5a6b954bcac6 | -10.82193 | -47.39737 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fb726a4-9d6b-3065-96b8-25366a3149ac | -10.82194 | -47.37578 | 2026-07-17 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dec78538-b611-3101-8f0f-c2db31f4a41b | -10.8402 | -46.56885 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26647348-a9a1-3690-86a7-04d29daa0474 | -9.64799 | -48.57239 | 2026-07-17 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3adf258-0df3-39b3-b3b9-ba184a59a29a | -11.63733 | -49.12691 | 2026-07-17 04:38:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceac14f6-0bc9-3c22-96bb-0258a965d4e4 | -9.95598 | -50.5572 | 2026-07-17 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d91875c-4d00-3c4d-8732-4578ea361c05 | -10.81708 | -45.13624 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b2352e85-bd60-3950-bae7-3fa35f20ed02 | -12.69444 | -46.51014 | 2026-07-17 04:38:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bde7224-ee5b-3d12-876b-f348beb6af8e | -10.80965 | -46.5751 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cecff359-b0c4-3ef9-a008-fd6e2db6cc71 | -8.71076 | -49.60685 | 2026-07-17 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9b1e471-68e7-3cbb-b758-019fa5103315 | -9.51646 | -47.14066 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a7b26116-1086-3de9-b00a-379d71ed2ea9 | -12.50344 | -46.34544 | 2026-07-17 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fbc5bfea-4c9e-36ec-9e9e-6cbd3eea6294 | -9.11044 | -47.62771 | 2026-07-17 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9ad77d3-2ae0-3265-9f33-529ad2d55476 | -10.81574 | -45.13702 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72f861cb-ebbe-3e64-9486-182811447d89 | -10.81692 | -45.12926 | 2026-07-17 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8940359e-cdb8-3b71-bd70-5d051c8f587a | -12.12053 | -49.94254 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaf8e37e-8a87-3e9d-9e3a-cd9a8f6a919a | -12.50683 | -46.34597 | 2026-07-17 04:38:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9e7c189-3c53-342b-9321-73dee365515d | -10.82619 | -46.52637 | 2026-07-17 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07ef5171-3da7-347f-a1a8-acec7498a8c8 | -12.695 | -46.50647 | 2026-07-17 04:38:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4aaff45d-ed9b-34b9-b361-09a767ffbf53 | -13.43753 | -43.85614 | 2026-07-17 04:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 17523a26-6ca5-3854-af1c-f7c0d90ad588 | -12.6574 | -48.22023 | 2026-07-17 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9bb48323-6cd1-397d-b7fa-10d66167c68d | -8.7178 | -49.60804 | 2026-07-17 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82436ff2-26f3-38a4-ae3b-62df71bce888 | -12.11707 | -49.94194 | 2026-07-17 04:38:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3e795c73-4a3a-375e-9e0d-4dab0b59a86a | -9.95725 | -47.9599 | 2026-07-17 04:38:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f21b583d-458b-3d33-af04-b700d3707171 | -8.71428 | -49.60743 | 2026-07-17 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efe1d1a5-4bf7-3b7a-b676-f8864f341cdb | -9.51701 | -47.13717 | 2026-07-17 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d88465f-df29-30b6-8231-3015248d7343 | -10.47706 | -49.14481 | 2026-07-17 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb654ab0-bee7-365e-9ea5-1395f32c993d | -6.50091 | -42.21271 | 2026-07-17 04:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69523b89-1966-33e8-903f-af8af0baf992 | -8.76044 | -43.93953 | 2026-07-17 04:38:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b41f2e3c-ad6e-37d9-b618-f384af19b22c | -11.78383 | -47.09327 | 2026-07-17 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f495db1f-8e5c-3b38-9ff9-1cffb694a941 | -13.2832 | -45.20145 | 2026-07-17 04:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53ebe2ad-f3f7-3063-bbf4-81b9458a30a1 | -5.5298 | -47.4951 | 2026-07-17 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f77e0740-bc1a-39ff-be55-b8175b7630ad | -11.76403 | -49.08023 | 2026-07-17 04:38:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1917e815-e64f-3351-87fe-f02331e1065d | -8.04939 | -46.72363 | 2026-07-17 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f78d660d-e1c0-3bb1-8716-55a698cc996b | -6.64796 | -43.9143 | 2026-07-17 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fecc036-058b-36f5-bf1a-5ca6f368bc25 | -6.01392 | -46.32547 | 2026-07-17 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a419262-4b41-331a-8c28-53b2eaa67239 | -11.39702 | -47.53078 | 2026-07-17 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
