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

## Dados Diários - Página 290

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4acbb03f-6a2f-3c38-8c6f-b528ba1f1047 | -3.4463 | -57.9618 | 2026-10-09 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2b9cc3b0-85e8-33ae-ad71-5dff3d6dd53c | -2.4942 | -58.0768 | 2026-10-09 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fc001cb8-db06-3b4b-80f2-6a7eb99bb26d | -12.1759 | -44.6351 | 2026-10-09 18:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4490d5bf-5cfa-39dc-aabc-944e4770fc93 | -2.572 | -56.1646 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 553d7faf-11bc-31f5-9f27-ff7f33e6bae4 | -3.5526 | -59.0973 | 2026-10-09 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9b319358-9c7b-391a-87bd-55636a4d3d40 | -2.5492 | -58.0179 | 2026-10-09 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1432c3da-5474-32f0-96dd-f53074a4c042 | -12.193 | -44.7487 | 2026-10-09 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1b72f75d-5d4a-34c5-867a-e46ab6a946f4 | -7.5575 | -40.3364 | 2026-10-09 18:20:00 | GOES-19 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 765cc6c5-abed-33ac-8f3b-f9bdfe59085d | -12.0058 | -43.464 | 2026-10-09 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 312d8edc-4842-3016-a67d-8a3e1b05b2a4 | -1.3264 | -56.4176 | 2026-10-09 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| d058be3f-6776-3442-8681-317ccae42b8c | -2.4259 | -55.9901 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4a513580-9fa6-3ed5-802b-2808dc8de1d3 | -14.3611 | -55.0114 | 2026-10-09 18:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 881d7541-f017-31af-bbc0-68b8a1b68e03 | -18.3335 | -42.3598 | 2026-10-09 18:20:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 211.5 |
| 188213d4-acf7-394c-9ff1-f6f9639e28f8 | -14.4339 | -43.9396 | 2026-10-09 18:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 302.7 |
| fd84f666-e7c0-3154-b29e-d0a90726ce65 | -11.0144 | -45.4042 | 2026-10-09 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e768a317-d4ea-3423-900c-9b16746bbe60 | -2.4806 | -56.0678 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| cd3d0ea8-6aa0-3a14-ba95-393c2106f0d2 | -10.8594 | -45.5622 | 2026-10-09 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 27e7ea5b-ceb5-3b7f-9ee0-f5dc32f3c2d7 | -2.9795 | -54.7696 | 2026-10-09 18:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1774898e-f186-3337-a1db-15bf4a3e871c | -6.2363 | -43.8562 | 2026-10-09 18:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b5b21cdb-0409-3bce-ada2-4574c95b20a8 | -13.1636 | -54.3591 | 2026-10-09 18:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 245.4 |
| 8dc7eda1-a820-3243-a4a0-4dbfde9203ed | -13.2467 | -42.2401 | 2026-10-09 18:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 95.8 |
| d12e8b55-76b1-352a-8d28-e7e6ab734e52 | -2.8997 | -56.9423 | 2026-10-09 18:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1c564f7f-1c90-3a32-9c5a-84eb2f8b8e73 | -2.9173 | -57.2151 | 2026-10-09 18:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f5c19e27-958a-3a76-b091-515e044fa4d2 | -2.853 | -54.1322 | 2026-10-09 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b07d18c2-58c5-37cd-8a15-4bfb7a066c93 | -3.5156 | -59.2324 | 2026-10-09 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9eb09107-92ae-3475-8123-85248adbd37a | -2.9267 | -54.0501 | 2026-10-09 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ae18f2af-3dab-3b84-aa34-ed0ec4f7ca12 | -8.2063 | -45.7791 | 2026-10-09 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| b35192f6-65ab-333d-bbb3-077886920373 | -13.1639 | -54.3385 | 2026-10-09 18:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 8b687544-ccae-3736-883d-5282cb807328 | -9.8828 | -44.794 | 2026-10-09 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 07ddf2fb-b016-376e-b280-7e4e4a7763fa | -15.3825 | -41.9277 | 2026-10-09 18:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1609.2 |
| 2f96b269-467b-31a0-953a-cabcd7973d1a | -2.8247 | -57.606 | 2026-10-09 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ca8b8d1d-2878-39e8-8bab-3f6a2744a83f | -14.0472 | -43.8222 | 2026-10-09 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 82b92c90-193b-3e02-9e33-4aca34be28ce | -15.2535 | -42.3741 | 2026-10-09 18:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 254.2 |
| cfcb8d46-c62c-32d4-8213-85c090f20c23 | -12.2123 | -44.7457 | 2026-10-09 18:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| be8cd149-3340-35f8-bdb9-846534c369ec | -3.9311 | -55.7179 | 2026-10-09 18:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| ccc31da7-1651-3b17-bb1f-0a7aa84e8694 | -18.3327 | -42.3849 | 2026-10-09 18:20:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.4 |
| ffc3b191-2998-32ff-9218-b94afbba3810 | -2.5492 | -58.0373 | 2026-10-09 18:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 14c99409-9079-3e2d-9a39-9609c8a41644 | -10.9953 | -45.4068 | 2026-10-09 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ae887124-8d3f-37ca-87d1-462b6bd5936b | -5.7131 | -41.6604 | 2026-10-09 18:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| a2eceb4b-1986-3604-ad55-775c6cf1ec52 | -8.9876 | -45.1521 | 2026-10-09 18:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| f96da9a7-c7aa-355f-a1d9-551990727390 | -9.297 | -47.4313 | 2026-10-09 18:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 80c84bd4-95a4-3975-9ebb-5374e5f55a9a | -5.8166 | -42.628 | 2026-10-09 18:20:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| 4030bb1e-619e-3e5a-9e8b-37fef88a0d28 | -15.4029 | -41.8985 | 2026-10-09 18:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 896.1 |
| 0327d86e-472a-3b1d-9a1a-6a67c4f5739b | -3.1697 | -58.6244 | 2026-10-09 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 73474995-11c8-3429-bee7-69c9e8e46ab0 | -12.8303 | -44.6239 | 2026-10-09 18:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 9a98dbc9-1cd4-3d7c-a657-a9dd13e27c64 | -1.8972 | -54.6706 | 2026-10-09 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| df436c63-2866-3e0d-9a77-ee984a4954e1 | -6.8458 | -44.7934 | 2026-10-09 18:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2d95d7e4-fb0f-3e9b-96db-20b0da514c66 | -2.5689 | -57.4163 | 2026-10-09 18:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| a6beb061-9401-3a86-9020-ba65b109220f | -2.5721 | -56.1449 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| f43e267a-51f8-3958-80c2-0c683fa5cce3 | -5.7119 | -53.4658 | 2026-10-09 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 892bc889-748b-3255-899c-9ff4bdec5fdf | -10.4334 | -47.3046 | 2026-10-09 18:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 176.7 |
| b3c2905a-633b-3b89-b13c-a9751929b80c | -9.4306 | -44.5959 | 2026-10-09 18:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4cbf12a2-d925-3ce5-959f-49ee01952663 | -10.1766 | -48.0412 | 2026-10-09 18:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b861cb4c-66f1-386c-81b1-11cd4810a9a0 | -9.9194 | -44.8815 | 2026-10-09 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 275.3 |
| 7f36a235-24a9-3ff9-a30a-26b37c810665 | -16.5627 | -46.8031 | 2026-10-09 18:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 111acf23-94c7-3f44-94a9-ddc6a904f06f | -2.8713 | -54.1518 | 2026-10-09 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 070e1539-eaef-32a5-9403-5dfb0ba6ee25 | -9.9204 | -43.5802 | 2026-10-09 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0cb66cc3-4cd5-30ef-913f-7d8dff55b0c5 | -12.1952 | -44.6321 | 2026-10-09 18:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 5b5e71d3-f295-3c1f-8ad4-9ac31af8187e | -2.5171 | -56.1262 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d17d1537-91f4-394c-b729-cf4f6e65b666 | -10.4524 | -47.3024 | 2026-10-09 18:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e3d8d43f-d495-34d7-82ed-446cd9ec4aa9 | -3.5193 | -58.0183 | 2026-10-09 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 50b7d6cb-a1f9-3918-ab03-7d53ba86737c | -9.75 | -44.7875 | 2026-10-09 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| df47b13a-2012-3387-8c32-f115a32810c0 | -14.4535 | -43.9359 | 2026-10-09 18:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 395.1 |
| fb76fdd8-5230-3f39-b983-062abcff2b35 | -12.2145 | -44.6291 | 2026-10-09 18:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 1f487342-e2aa-3632-8690-ed958dff6520 | -12.0063 | -43.4402 | 2026-10-09 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 37fbe538-8085-3f8d-a6b8-a9796fc8cafc | -12.3708 | -46.5789 | 2026-10-09 18:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 388.8 |
| 8bb7641d-558a-3d06-8cfe-0f230bc16162 | -13.3865 | -43.8708 | 2026-10-09 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 216.4 |
| aa36316b-4209-3aa1-9a4a-677e169584d2 | -4.6113 | -55.7162 | 2026-10-09 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ef446ac3-260f-3628-9238-ffa7021bc237 | -2.4806 | -56.0875 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b4d621da-86ff-3cc4-9ede-af5a77ec5ee2 | -9.7559 | -45.6783 | 2026-10-09 18:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4d3a9d06-78a0-3fa6-96db-45f179bd5fda | -15.3838 | -41.878 | 2026-10-09 18:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| ac45718e-9718-3f8a-b95b-b4c68f9f3abf | -14.0647 | -44.8098 | 2026-10-09 18:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 6a275b23-4559-3a58-9ace-2b2a7c9fe031 | -7.4697 | -42.8315 | 2026-10-09 18:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 4147e98f-d4e6-32bc-b391-41fc36f7df1f | -11.8787 | -47.3668 | 2026-10-09 18:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dfb5fc21-693c-324c-a721-0d2c21d8eb1c | -11.014 | -45.4272 | 2026-10-09 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 98841c85-07e3-3af1-bf97-f01d006c1982 | -3.1601 | -50.6021 | 2026-10-09 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 897845ec-cc2a-3962-a8a2-aff06d417be3 | -2.4623 | -56.0682 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| b06a39f5-c060-37e9-9ff5-d7669f15fa21 | -7.4886 | -42.8295 | 2026-10-09 18:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 200.6 |
| 8c3071d9-a188-3a46-a347-3e8f0bed0fcc | 0.543 | -50.899 | 2026-10-09 18:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 49b244e9-da8e-301e-82d6-b246b332dfbb | -4.937 | -56.8675 | 2026-10-09 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c1715aed-58da-3a44-b03c-7ab29535c6fa | -10.8909 | -44.8001 | 2026-10-09 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 0e7840c5-8961-3048-90b3-a3faf10bfd22 | -3.7564 | -45.9422 | 2026-10-09 18:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 8f315fce-987d-34ef-8d78-222bc93c9bac | -2.0577 | -56.8591 | 2026-10-09 18:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 941dc755-caae-3282-a21d-4db3b0fc5fc3 | -14.0652 | -44.7863 | 2026-10-09 18:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 30ca56aa-110a-3872-ae7c-0dd4b80c14be | -12.1436 | -43.2992 | 2026-10-09 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 30b53a5f-f39d-3607-9671-b93b2a23035c | -7.5162 | -45.3024 | 2026-10-09 18:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| defdd8d0-a89b-39d7-87b7-e0c37feaae54 | -15.2732 | -42.3699 | 2026-10-09 18:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| 90c7ad72-fc73-3584-96ce-767737671ca6 | -9.0173 | -44.3676 | 2026-10-09 18:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 65f5ca05-269c-3d2c-b61f-e533e4f47198 | -14.0662 | -43.8424 | 2026-10-09 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 214.8 |
| c38f8bdf-a275-3d45-ac12-81e652404b2d | -13.3666 | -43.8979 | 2026-10-09 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1225.4 |
| 8c9ae599-1369-3c4f-998f-89306a02835b | -14.0667 | -43.8185 | 2026-10-09 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 305.7 |
| 1daa5979-148b-37ff-97a8-093b7d28d65b | -12.214 | -44.6524 | 2026-10-09 18:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 64c6e819-f48c-38a5-93af-f810e55fefe1 | -13.6896 | -49.107 | 2026-10-09 18:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3535c77c-9f35-3aaf-9930-4e0ab090fab2 | -3.1114 | -53.7839 | 2026-10-09 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| fe64096f-5b69-3f75-a119-cdb9d4d0427f | -2.4623 | -56.0879 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| fc931f47-7e9c-36f3-b3dc-c86d08db6d02 | -4.104 | -53.9963 | 2026-10-09 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 6b5f3b29-39f5-3faa-ade7-1296c8c326d5 | -5.5315 | -43.0498 | 2026-10-09 18:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 347dc3ae-289d-3de1-95b8-2aa7bf4661ff | -2.7727 | -56.4946 | 2026-10-09 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 31e85a18-63a8-3175-9df8-8f7b8ec34bad | -2.3848 | -57.9044 | 2026-10-09 18:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 8079b323-d1fb-339d-92fe-7805a9ff77f2 | -9.0829 | -45.0957 | 2026-10-09 18:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |


[Clique aqui para ver as próximas entradas](README291.md)
