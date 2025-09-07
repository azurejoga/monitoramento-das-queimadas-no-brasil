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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48ee217b-8cfa-3157-b8f1-ea7294d1acad | -6.2108 | -42.6426 | 2025-09-07 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| f5d3d4be-2ec3-3f54-bc2e-381582a8cd7a | -9.1834 | -46.0377 | 2025-09-07 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b019864d-3906-3d77-be19-4ead772d3d3e | -12.3016 | -47.2416 | 2025-09-07 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| dc9eb12b-39f9-3f4e-a2d1-a534e71c6634 | -10.4632 | -53.6132 | 2025-09-07 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 344.9 |
| 25d8b1a8-466b-3cc9-96fd-dc9b24aba5a0 | -13.0542 | -48.0716 | 2025-09-07 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 5fdbe675-5d69-37dd-b666-be73b89c473b | -8.1612 | -44.8521 | 2025-09-07 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 60d8efc2-0198-365d-b05a-16ed5647bda6 | -12.9477 | -54.793 | 2025-09-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| c9e7aa7e-4879-3518-8b60-d7af6c7a75b8 | -12.8252 | -47.9932 | 2025-09-07 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 327bc35c-00f1-305c-9ef9-49b8d729edce | -19.4898 | -47.7646 | 2025-09-07 13:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d6359ee8-54cb-3f17-b4db-54afc772029f | -8.6912 | -54.6682 | 2025-09-07 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| d68f4525-d6b3-3798-b516-34fdb472d316 | -11.4089 | -43.581 | 2025-09-07 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| bb39fe67-20e3-3d88-aa9d-824d3a601900 | -10.8066 | -47.7256 | 2025-09-07 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 2f6da7c1-b17b-3b40-a0df-ddb4e4f6946c | -6.5915 | -43.9883 | 2025-09-07 13:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9e9bfe1b-c67a-347f-b86c-e5e8553d6b67 | -13.9342 | -54.0256 | 2025-09-07 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 50797f86-15fa-3266-bb62-00010908cdd5 | -12.7832 | -52.9477 | 2025-09-07 13:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d016312e-44b7-350a-9651-55502058ad43 | -7.7437 | -50.3372 | 2025-09-07 13:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 198fa5e9-7ed2-3188-877f-0a3f127a2801 | -5.9754 | -45.7452 | 2025-09-07 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 12406b60-e7a2-35f2-b5d6-98da769815e3 | -12.7641 | -52.9498 | 2025-09-07 13:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 8e78d6c8-bc86-39e1-9656-87228537094d | -8.1421 | -44.8769 | 2025-09-07 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 12d54231-87e1-330a-895e-bbf8c357d197 | -18.043 | -47.0812 | 2025-09-07 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| df638db3-2688-3e88-98a5-6ea54c6447e9 | -11.586 | -47.7613 | 2025-09-07 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| d87c899e-db54-3ff7-8825-51b4e19f92e5 | -11.264 | -46.4617 | 2025-09-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ba65bcb2-47cf-3d98-9558-f0ae2f66e00b | -12.8248 | -48.0155 | 2025-09-07 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 19a72555-73ba-39fe-bd71-da80466fb084 | -8.922 | -45.8179 | 2025-09-07 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 41304226-04f8-31d5-adb4-04354f253e97 | -8.6832 | -45.3221 | 2025-09-07 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| ed0fe1ce-9c87-3180-82e9-fab2ac0b1199 | -11.3901 | -43.5602 | 2025-09-07 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| ea275542-bb5a-3f37-877b-54629bc99f61 | -7.7439 | -50.316 | 2025-09-07 13:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0d83024b-7905-3393-b1d7-2505a1a567bb | -12.822 | -52.9016 | 2025-09-07 13:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b4f84ac3-e2b2-33a2-87a3-08b884486f16 | -13.8606 | -46.2337 | 2025-09-07 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 937fcab0-121b-3d8b-9791-bdf79904dfb6 | -13.0349 | -48.0744 | 2025-09-07 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| e913103f-2174-3998-93d6-e9fa1db79329 | -12.9289 | -54.7744 | 2025-09-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| d36b8e68-493e-3e1c-95bd-726a91e5354e | -7.725 | -50.3386 | 2025-09-07 13:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b0cdd416-48f4-3608-8cf5-0898a2fa4f5d | -11.3552 | -45.5634 | 2025-09-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 62b0e45a-b3ef-32f7-a4a5-afc9276b9d39 | -12.948 | -54.7724 | 2025-09-07 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 251.5 |
| fc4daba9-5e56-3968-a600-b80effd547ae | -6.4976 | -43.9963 | 2025-09-07 13:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| c8db4bba-89ae-3c98-afa3-7d37cc2e6939 | -6.1388 | -44.2561 | 2025-09-07 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 371ae0eb-054c-395a-bcd6-6796a4e90430 | -15.124 | -48.0627 | 2025-09-07 13:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 153f5c96-5639-325e-b032-a77493be01ac | -9.9783 | -51.6646 | 2025-09-07 13:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9e7df511-356e-345f-842c-6e2536504050 | -11.5669 | -47.7638 | 2025-09-07 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| fedc8a08-c91a-3c3e-a519-4c2415a65c56 | -9.0229 | -49.8048 | 2025-09-07 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a96d57af-78ea-3f0c-b7d0-230fa67a1062 | -17.95 | -45.2974 | 2025-09-07 13:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 59e8770d-5a07-337e-a43c-2d7850d39a34 | -11.5856 | -47.7836 | 2025-09-07 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f7bfad40-22d7-3841-ab6d-f725a182e816 | -9.7765 | -46.8908 | 2025-09-07 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c771e567-e3ba-3f66-b304-8e1447150cb9 | -6.192 | -42.6442 | 2025-09-07 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 55982c53-b7f9-321b-b1d2-2fe6d32888d7 | -7.6173 | -44.6772 | 2025-09-07 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 77d8215c-7849-3aef-9de1-9eb5fd494e47 | -6.1923 | -42.6205 | 2025-09-07 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 6089818f-4417-3082-bcba-8112fc68d52a | -18.0424 | -47.1044 | 2025-09-07 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9fa9e15d-7ba6-31be-a1d0-b7e3adc03ad9 | -11.1575 | -48.3883 | 2025-09-07 13:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e9512aaf-00ac-3b5e-873e-945a3cffdc66 | -11.0245 | -45.9502 | 2025-09-07 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ee61e07d-92aa-3c7c-8ad6-9fe405a4a921 | -5.9901 | -44.1297 | 2025-09-07 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 9d9a3642-1706-30e6-a8f4-bb49d1aca06d | -6.2127 | -42.4532 | 2025-09-07 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 13e503d9-72c7-392b-8cad-80de9cad3169 | -11.4093 | -43.5573 | 2025-09-07 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| d5c20845-906c-39df-9795-888a160f34a1 | -14.5076 | -48.7641 | 2025-09-07 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 0a6b241a-430b-3b82-935d-fcbdda07af5c | -5.9899 | -44.1528 | 2025-09-07 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 4bda533d-d7e1-3171-aa23-1a0328dc061b | -5.8403 | -44.1181 | 2025-09-07 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a4e4faba-6a25-34ea-a273-4e4bdb776cc9 | -5.8401 | -44.1412 | 2025-09-07 13:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0bc753b4-3f61-312a-abaa-7746c728d857 | -6.8281 | -52.8143 | 2025-09-07 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1f09aebf-657f-3baf-850b-54396d3ae446 | -14.4882 | -48.7671 | 2025-09-07 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 194.9 |
| a31c1cac-9222-371e-9cc7-32175d1cbdbc | -19.4891 | -47.7879 | 2025-09-07 13:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 205.9 |
| e2836a04-0b5f-3f36-88ba-d3f9add314d3 | -7.6176 | -44.6543 | 2025-09-07 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c8633905-2043-3b6d-806b-b88dff609b98 | -6.3497 | -43.7773 | 2025-09-07 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 82e20629-7d23-3055-a781-56fa051277c3 | -12.8252 | -47.9932 | 2025-09-07 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3877bf12-2d3b-3288-9ea9-7c64eab7e45c | -11.586 | -47.7613 | 2025-09-07 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| c1365911-b2e3-3d6f-9391-aaad141b1ea8 | -9.0229 | -49.8048 | 2025-09-07 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8e00bd09-3648-39aa-bddf-421252511097 | -12.948 | -54.7724 | 2025-09-07 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 247.2 |
| 03a84287-c1bc-34f7-b7c2-477a5dd7da29 | -11.3897 | -43.5839 | 2025-09-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 318ea53a-dcac-361d-82b2-c9e8a9a56044 | -8.0392 | -44.0588 | 2025-09-07 13:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 09263d0b-3d6b-3b2c-9b52-d9d06fbe5f10 | -7.7437 | -50.3372 | 2025-09-07 13:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 35fcaa4c-ebaa-3075-9e7e-0f252734e4dc | -14.4882 | -48.7671 | 2025-09-07 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 07eba0e5-1e1a-3fd2-9bf1-078fb50dd923 | -15.7385 | -53.5506 | 2025-09-07 13:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 88afb670-e850-358d-9a10-64b5884a2053 | -8.1421 | -44.8769 | 2025-09-07 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 361.0 |
| 09c50031-0e96-3c45-8365-6508007da609 | -12.6186 | -44.6116 | 2025-09-07 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8117c914-6699-3cb4-a189-b256f2503a91 | -8.161 | -44.875 | 2025-09-07 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.4 |
| b9c4752e-5611-31b4-a054-25e42676bdcc | -5.9899 | -44.1528 | 2025-09-07 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 4d56324c-9778-3db0-901d-f0446adfee9e | -5.5884 | -45.1185 | 2025-09-07 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 88c61890-6ad1-305c-84f0-c3f6ef45421a | -5.8081 | -45.6448 | 2025-09-07 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8ac8d216-b28d-37ad-a037-8547ae344309 | -12.8248 | -48.0155 | 2025-09-07 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c4eb0273-00a6-3765-acda-613a81c754f2 | -14.5076 | -48.7641 | 2025-09-07 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 135d0da9-e085-375b-9412-5a51a833a792 | -15.103 | -48.1334 | 2025-09-07 13:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3a03d74f-9d93-3426-b8ac-5f477d3cad80 | -15.1235 | -48.0852 | 2025-09-07 13:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 0984adce-f742-3528-8af7-bb281083e937 | -6.4976 | -43.9963 | 2025-09-07 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| d03a9cdf-711c-3e1e-85ab-0e85f13cdcbb | -11.3901 | -43.5602 | 2025-09-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 00b68a99-c5f2-3fef-8c0c-e52b5f1eac1f | -11.4093 | -43.5573 | 2025-09-07 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 41852ced-b3c5-3d2e-afb1-343fea286775 | -8.1424 | -44.854 | 2025-09-07 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7dff7f3f-3846-3ccb-925d-a527b0fb3c66 | -5.9901 | -44.1297 | 2025-09-07 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a04ea43c-048c-3f00-85d9-ce4786eb9099 | -11.264 | -46.4617 | 2025-09-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1f0a42c9-e0d3-3289-91cd-f5625bbf8e58 | -5.8403 | -44.1181 | 2025-09-07 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1dd8f5cc-8395-3686-914e-55c5082ba128 | -8.922 | -45.8179 | 2025-09-07 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 51816d5c-c4a6-360c-8c0c-8204712f8f41 | -8.6912 | -54.6682 | 2025-09-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fa239fa9-c492-3484-92fa-b697161ee659 | -5.5882 | -45.1412 | 2025-09-07 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4588a255-8463-35a8-9995-1d91377bc10a | -9.7765 | -46.8908 | 2025-09-07 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3313147b-e274-3d5a-b21c-99365744b568 | -11.2636 | -46.4843 | 2025-09-07 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 302.8 |
| 801b474d-0c70-3c7f-84f7-89efb5bb3940 | -12.8444 | -47.9905 | 2025-09-07 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 05dc5ebe-d976-3ace-b789-d369a062f5d8 | -12.7835 | -52.9268 | 2025-09-07 13:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 861baeef-39ce-303f-a3a0-c494d714708f | -18.043 | -47.0812 | 2025-09-07 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 503c192d-1bf4-37f0-b97a-d74bc2f2b906 | -7.7252 | -50.3174 | 2025-09-07 13:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b5f35b18-bd02-3141-9ba6-35973f4fc425 | -6.1388 | -44.2561 | 2025-09-07 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e36369b1-0df9-3c93-8b2a-f204187b1573 | -17.95 | -45.2974 | 2025-09-07 13:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c5fa6076-f114-3ef7-a5fd-01a02cad007b | -6.192 | -42.6442 | 2025-09-07 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 113.6 |
| df23e57d-5ab7-353f-95f0-9cdd5db8eb25 | -6.2857 | -53.4369 | 2025-09-07 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README89.md)
