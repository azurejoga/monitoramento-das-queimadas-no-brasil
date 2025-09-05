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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 326faae4-8227-3a94-899e-fead4e0f89a7 | -7.07727 | -46.1988 | 2025-09-05 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ffcff37-7041-3ba4-b479-9c34b69bc160 | -6.73892 | -45.93356 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72bf734c-cdb7-3ed7-ab8a-6ddb7815ccb3 | -5.63303 | -43.68372 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f367756-512a-3288-98d3-4bb12d21af4e | -5.59899 | -45.02233 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edbe89d8-b10f-3d8f-a72c-44af9c9a2378 | -3.30029 | -43.54151 | 2025-09-05 04:34:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6add83ad-9011-35b0-b4cf-98554d472715 | -7.51726 | -45.35816 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72d7eb40-0bc8-3bde-88d0-5baaa2ff9b51 | -6.00405 | -46.69087 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7775521b-235b-3e8e-b582-3267b24f9c47 | -8.09587 | -42.43105 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d1185d5-f81f-303a-a3ab-05949dddf5fa | -2.37911 | -47.62606 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 127fb442-8611-306d-abc5-1307f57f8d1d | -4.56329 | -40.34592 | 2025-09-05 04:34:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd2322fc-f89b-32f6-830a-f3a6cc294b41 | -4.27652 | -48.18918 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cab7aee8-7460-33e7-b618-87cefcf098ea | -6.87933 | -45.57477 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1ddd61d-68a7-3b7c-84f9-ae2b120b3d5d | -5.26448 | -55.96091 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5492dd71-c207-3512-ad38-8c38bd9933dd | -5.37927 | -45.9486 | 2025-09-05 04:34:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b289fbc4-2a3b-3c07-a407-f2b87e4173d3 | -2.94495 | -48.98682 | 2025-09-05 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0bf4075-0f7a-3619-94af-d4403a81d677 | -7.71208 | -45.16533 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82193a70-a23a-3e8e-a705-71d1353b39bc | -7.59519 | -44.67153 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 797c2aaf-4f9f-3fc8-8992-c49f18bcd454 | -5.09403 | -56.15194 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 059feb8f-a330-308e-88c4-9328f501dd28 | -7.97578 | -44.52464 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d900193e-0c2d-3d8c-bb26-b04cd6e4185b | -5.90195 | -44.16161 | 2025-09-05 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43987a70-fe93-3847-979c-38ee75778aac | -6.42995 | -49.74795 | 2025-09-05 04:34:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 503fb46f-63f3-30d5-a92f-cba0522f2e0f | -6.54175 | -43.91355 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8161306-f44a-3bf7-a44a-79fde0fe72d7 | -6.02273 | -43.7011 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1281c70f-19aa-31fa-bd73-f6c6c3b2180a | -6.23019 | -42.61869 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b8a3a172-466a-38cc-86c0-52b50b4182fd | -5.21109 | -43.6981 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4680f2a-ec51-3fbf-aafb-289586e942b2 | -5.84746 | -45.30481 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c33bf91-ceca-3654-84d8-31af867917c0 | -7.26246 | -41.89658 | 2025-09-05 04:34:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5b8aee4-7f75-3b86-9567-4c264dda8c32 | -7.61304 | -43.84916 | 2025-09-05 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bc684be-9505-32db-b203-0e7b426b7abc | -7.89395 | -45.29834 | 2025-09-05 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5084c863-bff5-35ab-aeb6-bd6c3fced998 | -4.90962 | -47.39154 | 2025-09-05 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b59318-2222-3280-b6de-f1db8641610e | -4.90908 | -47.395 | 2025-09-05 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15692d06-2815-3617-8cce-b37abfd2dcc7 | -6.90717 | -45.18507 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef59d944-886c-39d0-8ddd-a56cf770ce4f | -4.99545 | -56.25821 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a9f84a8-f0b4-33d5-a9d9-3064339379d9 | -7.98895 | -44.51294 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83da802e-d39c-3920-a4ed-92126818634c | -2.556 | -47.72502 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b4cd1c3-df98-3125-a899-62e33e7a11dd | -6.23128 | -42.44386 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b220a460-6f01-3ce4-8da3-9662904048e0 | -6.0202 | -46.6535 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4ee48ba-2920-3a8b-922d-746aa1e583e9 | -5.99286 | -49.23543 | 2025-09-05 04:34:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e48e9172-d7e7-3799-b296-7bc5ca968784 | -6.25386 | -43.28064 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dd2df471-4bb2-3bd4-8d93-acf83fc985f4 | -5.05366 | -43.86815 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 083672d1-da2c-3569-b6d2-c0c4b2dfaefe | -3.15928 | -48.60578 | 2025-09-05 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7150424-b8e8-3b32-a06c-5a32910a11ac | -7.89229 | -45.23556 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 790aed04-99d8-3ebf-b116-5fc51354d6a9 | -6.24784 | -43.29454 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92979434-f7a1-3388-b3bf-ac49a6b3ecbb | -2.78296 | -49.61787 | 2025-09-05 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12b90488-e040-35db-bfb6-6540883dc3ea | -6.32513 | -44.48574 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a425bba-2d33-3c72-9a9e-87ac70deed89 | -5.76877 | -45.43936 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01eadf61-3721-3b19-997d-f050042fa31a | -5.70482 | -45.40661 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1d11726-3aa4-38a9-bc46-fb0c2351273f | -5.10701 | -56.13832 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c005c692-3e15-30d5-8999-935624efc723 | -5.20805 | -43.69063 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 832139ff-17f4-3dac-b589-ae7c618074ee | -6.59428 | -44.55175 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 712d1e37-479a-3c44-92a7-5f532453d716 | -7.90006 | -45.23251 | 2025-09-05 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc30610a-3349-39f6-85f6-f52bbab162d9 | -7.99743 | -44.77573 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dd39eb0-d578-3d57-8cd8-e1d724d04541 | -7.98457 | -44.51676 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 399b23ee-d5d6-351d-8a95-239a4cf33c99 | -6.95984 | -45.53944 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47ada77f-df0e-3fe9-b6d6-3cc5a8273832 | -6.99648 | -44.94103 | 2025-09-05 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c280f276-da56-35b4-883f-580c463bbfbf | -6.01131 | -46.68839 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75d93edd-df03-3ead-bae6-5126097dfde0 | -6.37697 | -42.99526 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8d5ad91-d196-38cb-9526-881623ce4b3a | -5.46012 | -42.64488 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1a511555-d2f9-3350-9455-13aa88882f56 | -5.76417 | -45.4231 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1b4f64f-e38c-302e-9ae9-c428008c99e9 | -6.74064 | -45.14021 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 237d49b5-a756-397f-992f-f6f419399e88 | -6.90843 | -43.81289 | 2025-09-05 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 831412cc-c61f-371b-9e81-31d3229c2528 | -5.60252 | -45.02288 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8fe63181-a353-3757-be2e-513de621b8e9 | -5.54764 | -45.67678 | 2025-09-05 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e08027b-66c8-3264-9934-6fdac009babc | -6.23073 | -42.44751 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76407621-830e-3e4f-af40-6402a572aeb9 | -6.02361 | -46.6976 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a97ed8a-ff11-3786-93e1-304cbc84f4f5 | -6.02653 | -43.70168 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6d53c8d-07ca-359f-8eaa-81925a667f76 | -6.30981 | -44.8536 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30688d69-5fdd-32c7-99cf-8eeb171de65c | -6.24934 | -43.30762 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4296657d-9c13-370f-b6f7-334e48a3d84f | -5.86411 | -46.11142 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80589722-7feb-326c-9230-0f1db94d1689 | -6.88221 | -45.55574 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c0706e0-00ac-340b-9914-0a1318cb6116 | -3.89991 | -54.68837 | 2025-09-05 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89b80377-93e4-3865-8994-f0fa4ed7761a | -4.23992 | -48.55685 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d9a6ea0-65d1-343f-b1d0-5bfb9fdab7c8 | -5.71166 | -45.15499 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7298083-7357-3aa2-9254-33704ec08ea7 | -5.98659 | -43.81291 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9ba9886-6c30-3cf6-9f5f-2d6b3f9a09fa | -6.5902 | -44.55695 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9c331c82-5274-35a2-84e9-bc58851786ac | -6.35645 | -47.09841 | 2025-09-05 04:34:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70125cc4-3b50-30be-bee5-cc2bd013c9a1 | -5.53885 | -50.89285 | 2025-09-05 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 249beacb-d65c-3cbd-aee5-1254f72a8457 | -5.50374 | -42.66242 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3136c20f-090b-3a22-90ee-6b5c39d42a5b | -6.59669 | -44.56065 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8ea54011-bfe9-3111-bde1-00bc45ab237b | -5.8607 | -46.1109 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40c2494e-06c9-38d3-a2da-7c439e401773 | -3.22932 | -47.12724 | 2025-09-05 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 921efdfb-b743-3724-ad69-bebf5f44838d | -5.93019 | -47.31431 | 2025-09-05 04:34:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34b53a45-b05f-342d-beab-1625d90b1532 | -5.7512 | -45.55312 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30012dee-28fa-3ebe-8f71-a706505e5e32 | -6.5118 | -43.50322 | 2025-09-05 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14cde5ae-c363-31eb-9f4a-4a15ad5e36d0 | -6.70028 | -44.81432 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29e97325-9f23-3b56-bd64-cc25fe4ba710 | -5.55727 | -46.19473 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bdc9627-5b18-3e31-b744-e674c29c3af3 | -5.43904 | -42.86373 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 40fe1127-1a38-38a4-9ea9-98296332b148 | -7.08353 | -43.87274 | 2025-09-05 04:34:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b836e24-a9ab-3ff5-a07f-3d7f6fcc50e5 | -6.49433 | -43.73575 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e514a0c4-6d53-374e-aeda-f6aeb8cfb540 | -4.07015 | -48.03798 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f66cf101-b589-39c0-a49c-9e3a2a7b8dd5 | -6.11661 | -44.14576 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c143bd0d-6383-354c-8fb2-5876b8806148 | -3.23823 | -50.04866 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c72ac0b-357b-3d4e-9ed3-3f518d7d3149 | -6.28897 | -43.85201 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b571fb5-bcc3-3bcc-8d0b-490c05a2467e | -6.80825 | -45.66583 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d4e5bc6-b841-38e6-889d-f581286d1300 | -6.38339 | -43.00674 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00f0968a-45eb-353d-8841-928d782f1bd7 | -6.61363 | -43.97697 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0eb6a29-b9aa-3cb0-9ede-12786e01fa4f | -5.44229 | -42.89546 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 46feeca0-05b9-35a6-b035-359cd7201b44 | -6.58937 | -44.55973 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| f4144f1e-e7dd-335f-8de5-d018f6a2ec54 | -6.59303 | -44.56018 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| bb0f681b-7882-3f78-a327-114c7d9401de | -2.94424 | -49.01353 | 2025-09-05 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
